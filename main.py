import pyaudio
import crepe
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Hide TF logging

CHUNK = 1024  # Number of samples per buffer
WIDTH = 2  # Bytes per sample
CHANNELS = 1  # Mono sound
RATE = 16000  # Sampling rate (number of samples per second)

try:
    print("Recording is starting...")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    while True:
        bytes_data = stream.read(CHUNK)
        nparray_data = np.frombuffer(bytes_data, dtype=np.int16)  # Convert bytes to NumPy ndarray

        time, frequency, confidence, activation = crepe.predict(nparray_data, RATE, model_capacity="tiny",
                                                                step_size=65, verbose=0)
        confidence_mark = "🟥"
        if confidence[0] >= 0.4:
            confidence_mark = "🟩"
        print(f"{confidence_mark} {round(frequency[0], 1)} Hz | {confidence[0]}")
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Recording stopped")
