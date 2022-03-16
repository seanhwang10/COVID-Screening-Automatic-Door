# COVID-Screening-Automatic-Door

This is a senior design (graduation) project of my team in Purdue Univ school of Electrical and Computer Engineering. 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/overall_diagram.jpg)



## Description 

Studies have shown that wearing a face mask can reduce the spreading of ongoing COVID-19 viruses by **65 percent** [1]. However, there still are many people who forget - or choose not - to wear a face mask in a public area. The main purpose of COVIDoor’s COVID screening automatic door is to ‘screen’ the potential spreading of this highly contagious virus in populated buildings by only granting access to those with a face mask on and has a normal temperature. The system will utilize an infrared sensor that measures the user’s temperature, as well as a camera that is pre-trained to detect a mask. The CPU will be programmed to take in the data from the infrared sensor and the camera and make a decision whether to open the door or not. Finally, the system will have an automatic door module that is controlled automatically by the CPU, which will allow access to those who pass the screening process.  

[1] https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)31142-9/fulltext



## Operation 

COVIDoor operates in the following sequence: 

**User Recognition, Mask Detection, Temperature Checking, and Door Operation.** 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/operation_sequence.JPG)

1. <u>**User recognition**</u> 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/initial_face_recognition.gif)

Message: *"Welcome! Please wear a mask to enter"*

2. <u>**Mask Detection**</u> 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/mask_detect.gif)

Message: *"Please fit your face to the circle"*

We designed a guiding circle to lead the users to come closer to the IR sensor for a more accurate temperature measurement. 

3. <u>**Temperature Checking**</u> 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/temperature.gif)

Message: *"Checking temperature..."*

Success: *"Thank you! Please enter"*

Failure: *"Your temperature is too high (low)"*

4. <u>**Automatic Door Operation**</u> 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/dooropen.gif)

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/dooropen2.gif)



### Entire system operation 

We have built a small demonstration of our system using a door built with a small servo motor and straws. Obviously, this would need more improvements on the motor choice and the door will need to be made with something much stronger, for it to be actually be used in real life :) 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/demo_setup.JPG)

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/full2.gif)

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/full1.gif)



## Acknowledgements 

**Caroline Dunn**, on setting up Mask Detector on Raspberry Pi. 

```
https://github.com/carolinedunn 
```

**ExplainingComputers**, on setting up Servo Motor on Raspberry Pi. 

```
https://www.explainingcomputers.com/pi_servos_video.html
```

**Teammates**: Seojune Jung, BSEE 21; Teddy Kim, BSEE 21; Hayley Yoo, BSCmpE 22; Natt Towiwat, BSEE 21
