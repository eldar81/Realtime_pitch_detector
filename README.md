# Real-time pitch detector
This project aimed to provide instant pitch detection. The project uses [CREPE](https://github.com/marl/crepe) detector which is based on a deep convolutional neural network.

![image](https://user-images.githubusercontent.com/88551054/197404811-4c4ebcac-542c-45d8-9f72-d3aef20340ae.png)

Results can be provided both in the console and as a graph using matplotlib.

My laptop on Intel Core i7-8550U process one chunk of data in 60 ms on average in console script and 120 ms in plot script. Which is pretty good because human reaction speed lies down between 150 and 300 ms.

## Future improvements:
1. Improve plotting speed
2. Convert frequencies (Hz) into notes
3. Add a stave or piano keyboard to visual feedback to provide a more user-friendly interface
4. Add a module that will compare the user's singing and actual notes of the song providing instant feedback to the singer
