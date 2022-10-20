# Real-time pitch detector
This project aimed to provide instant pitch detection. The project uses [CREPE](https://github.com/marl/crepe) detector which is based on a deep convolutional neural network.

![image](https://user-images.githubusercontent.com/88551054/196546237-defc1f4e-8902-4613-90bd-bba3dfc7a153.png)

Now prediction provides right into the console in Hz. Color sticker represents the voice (sound) activity and is set up as >0,4 confidence rate.
My laptop on Intel Core i7-8550U process one chunk of data in 130 ms on average. Which is pretty good because human reaction speed lies down between 150 and 300 ms.

## Future improvements:
1. Connect the matplotlib library and implement real-time plotting
2. Convert frequencies (Hz) into notes
3. Add a stave or piano keyboard to visual feedback to provide a more user-friendly interface
4. Add a module that will compare the user's singing and actual notes of the song providing instant feedback to the singer
