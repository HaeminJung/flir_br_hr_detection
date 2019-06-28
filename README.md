# BR(Breathing Rate) and HR(Heart Rate) detection
(This project is to replecate the results of [Hu, Meng-Han & Zhai, Guangtao & Li, Duo & Fan, Yezhao & Duan, Huiyu & Zhu, Wenhan & Yang, Xiaokang. (2018). Combination of near-infrared and thermal imaging techniques for the remote and simultaneous measurements of breathing and heart rates under sleep situation. PLOS ONE. 13. e0190466. 10.1371/journal.pone.0190466.](https://www.researchgate.net/publication/322278898_Combination_of_near-infrared_and_thermal_imaging_techniques_for_the_remote_and_simultaneous_measurements_of_breathing_and_heart_rates_under_sleep_situation) with Raspberry Pi 3 B, 5MP IR-cut Pi-cam, [FLiR Lepton 2.5 LWIR](https://www.sparkfun.com/products/14654))

The paper aims on finding the breathing rate and the geart rate of a sleeping person using IR camera and thermal imaging.
This project aims to replicate the results using open-source algorithms along with a few adjustments for the Raspberry Pi.

## Getting Started
Associated Hardware:
-Raspberry Pi 3B
-5MP IR-cut Pi-cam(Chinese replica, non-official)
-[FLiR Lepton 2.5 LWIR](https://www.sparkfun.com/products/14654))(from Sparkfun)

Wiring of the cameras should not be much of a hassle, since the IR camera's ribbon cable will plug directly into the camera port & SparkFun has a detail tutorial on how to configure the FLiR dev board.

The Raspberry Pi is running on Raspbian Stretch 9.9

shape_predictor and cam.py will not be synced. It is to keep the system running both for the laptop(Ubuntu18.04) and Raspberry Pi.

##Commit from r pi

