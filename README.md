# Detection by color:
For this task, I utilized two popular libraries, OpenCV and NumPy. One useful method provided by OpenCV is the ability to identify the HSV (Hue, Saturation, Value) values of a specific color. To do this, I used a helpful online tool, such as https://imagecolorpicker.online/ru/. However, it's important to note that the H value must be divided by two, and the S and V values should be calculated as a percentage of 255. 
![2](https://github.com/arik-1998/detection/assets/116187220/b2b41f89-ae11-4717-a6da-05d4fb20760c)
After that, we must assign an interval of HSV values between which all colors will be displayed. HL(low)-H, SL-S, VL-V
![1](https://github.com/arik-1998/detection/assets/116187220/849335ee-3d63-41e7-9c52-307aee2b10c8)
After that, when we already know the frame values, we can draw outlines or segment objects.
![3](https://github.com/arik-1998/detection/assets/116187220/ce9debfe-e297-4bfe-80a7-6a5c5f37644f)
![4](https://github.com/arik-1998/detection/assets/116187220/89d2c0dd-8d44-4c04-9481-c78ff05ab0d4)
In a similar way, you can also use a combination of frames to detect different objects.
