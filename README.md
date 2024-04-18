<h1 align = "center">DunHuangStitch: Unsupervised Deep Image Stitching of Dunhuang Murals</h1>
<h2 align = "center">Yuan Mei, Lichun Yang, Mengsi Wang, Tianxiu Yu, Kaijun Wu</h2>

# <p align="center">DunHuangStitch: Unsupervised Deep Image Stitching of Dunhuang Murals</p>
<p align="center">Yuan Mei*, Lichun Yang*, Mengsi Wang*, Tianxiu Yu`, Kaijun Wu*</p>
<p align="center">* the School of Electronic and Information Engineering, Lanzhou Jiaotong University</p>
<p align="center">` Institute of Digitization of Cultural Relics, Dunhuang Research Institute</p>

![image](https://github.com/nie-lang/UDIS2/blob/main/fig1.png)

## Dataset (UDIS-D)
We use the UDIS-D dataset to train and evaluate our method. Please refer to [UDIS](https://github.com/nie-lang/UnsupervisedDeepImageStitching) for more details about this dataset.


## Code
#### Requirement
* numpy 1.19.5
* pytorch 1.7.1
* scikit-image 0.15.0
* tensorboard 2.9.0

We implement this work with Ubuntu, 3090Ti, and CUDA11. Refer to [environment.yml](https://github.com/nie-lang/UDIS2/blob/main/environment.yml) for more details.

#### How to run it
Similar to UDIS, we also implement this solution in two stages:
* Stage 1 (unsupervised warp): please refer to  [Warp/readme.md](https://github.com/nie-lang/UDIS2/blob/main/Warp/readme.md).
* Stage 2 (unsupervised composition): please refer to [Composition/readme.md](https://github.com/nie-lang/UDIS2/blob/main/Composition/readme.md).



## Meta
If you have any questions about this project, please feel free to drop me an email.

Yuan Mei -- 123

