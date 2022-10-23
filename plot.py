import pyaudio
import crepe
import os
import numpy as np
import matplotlib.pyplot as plt
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Hide TF logging

CHUNK = 1024  # Number of samples per buffer
WIDTH = 2  # Bytes per sample
CHANNELS = 1  # Mono sound
RATE = 16000  # Sampling rate (number of samples per second)

try:
    at = []
    print("Recording is starting...")

    # Launch mic stream
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Preparing plot
    plot_data = np.random.rand(360, 50)
    fig = plt.figure()
    ax = fig.add_subplot()
    line = ax.imshow(plot_data, cmap='inferno', origin='lower', extent=[0, 100, 0, 50])

    while True:
        st = time.time()

        # Get mic data
        bytes_data = stream.read(CHUNK)
        nparray_data = np.frombuffer(bytes_data, dtype=np.int16)  # Convert bytes to NumPy ndarray

        # Predict pitches
        frame, frequency, confidence, activation = crepe.predict(nparray_data, RATE, model_capacity="tiny",
                                                                 step_size=65, verbose=0)

        # Convert data
        activation = np.reshape(activation, (360, 1))
        plot_data = np.append(plot_data, activation, axis=1)
        plot_data = np.delete(plot_data, 0, axis=1)

        # Plot title
        if confidence[0] > 0.5:
            plt.title(f"Voice pitch: {round(frequency[0], 1)} Hz\n"
                      f"Confidence: {'{:.2f}'.format(confidence[0])}")  # round() doesn't work properly
        else:
            plt.title("Voice pitch:\n"
                      f"Confidence: {'{:.2f}'.format(confidence[0])}")

        # Plotting
        line.set_data(plot_data)
        plt.pause(0.001)
        ax.relim()  # recompute the ax.dataLim
        ax.autoscale_view()  # update ax.viewLim using the new dataLim

        at.append(time.time() - st)
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Recording stopped")

    at.pop(0)
    print(f"Average time per frame: {round(sum(at) / len(at), 3)} sec.")
