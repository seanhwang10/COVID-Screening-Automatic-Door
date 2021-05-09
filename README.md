# COVID-Screening-Automatic-Door

This is a senior design (graduation) project of our team in Purdue school of Electrical and Computer Engineering. 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/overall_diagram.jpg)



## Description 

Studies have shown that wearing a face mask can reduce the spreading of ongoing COVID-19 viruses by **65 percent** [1]. However, there still are many people who forget - or choose not - to wear a face mask in a public area. The main purpose of COVIDoor’s COVID screening automatic door is to ‘screen’ the potential spreading of this highly contagious virus in populated buildings by only granting access to those with a face mask on and has a normal temperature. The system will utilize an infrared sensor that measures the user’s temperature, as well as a camera that is pre-trained to detect a mask. The CPU will be programmed to take in the data from the infrared sensor and the camera and make a decision whether to open the door or not. Finally, the system will have an automatic door module that is controlled automatically by the CPU, which will allow access to those who pass the screening process.  

[1] https://www.ucdavis.edu/coronavirus/news/your-mask-cuts-own-risk-65-percent 



## Operation 

COVIDoor operates in the following sequence: User Recognition, Mask Detection, Temperature Checking, and Door Operation. 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/operation_sequence.JPG)

1. **User recognition** 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/initial_face_recognition.gif)

2. **Mask Detection** 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/mask_detect.gif)

3. **Temperature Checking** 

![](https://github.com/seanhwang10/COVID-Screening-Automatic-Door/blob/main/images/temperature.gif)

4. **Automatic Door Operation** 

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