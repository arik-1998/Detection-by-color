# Detection by color:
In this task I used the open-cv and numpy libraries. With the help of the first method, we can find the HSV values of a particular color. This site can help with that. https://imagecolorpicker.online/ru/ be careful that you need to reduce the value of H by 2 times, and calculate the values of C and V by the percentage of 255.
![2](https://github.com/arik-1998/detection/assets/116187220/b2b41f89-ae11-4717-a6da-05d4fb20760c)
After that, we must assign an interval of HSV values between which all colors will be displayed. HL(low)-H, SL-S, VL-V
![1](https://github.com/arik-1998/detection/assets/116187220/849335ee-3d63-41e7-9c52-307aee2b10c8)
After that, when we already know the frame values, we can draw outlines or segment objects.
![3](https://github.com/arik-1998/detection/assets/116187220/ce9debfe-e297-4bfe-80a7-6a5c5f37644f)
![4](https://github.com/arik-1998/detection/assets/116187220/89d2c0dd-8d44-4c04-9481-c78ff05ab0d4)
In a similar way, you can also use a combination of frames to detect different objects.
