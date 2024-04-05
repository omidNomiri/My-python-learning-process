# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

in this project i made a histogram equalizer normal and clahe, reveal hidden item,2d convolution, median noise redactor.

### Output

#### 2D Convolution

sharpening filter
![sharpening filter](output\sharpening_result.png)

identity filter
![identity filter](output\identity_result.png)

emboss filter
![emboss filter](output\emboss_result.png)

edge filter
![edge filter](output\edge_detection_result.png)

black zone filter
![black zone filter](output\black_zone_result.png)

#### Item Reveal

average item reveal filter 3x3
![average item reveal filter](output/item_reveal_3X3_result.png)

average item reveal filter 5x5
![average item reveal filter](output/item_reveal_5X5_result.png)

#### Histogram Equalizer

normal landing place VS equalized landing place
![landing place](output/landing_place_equalizer_result.png)

normal land VS equalized land
![land](output/land_equalizer_result.png)

normal figure VS clahe equalized figure
![figure](output/figure_equalizer_result.png)

#### Median Noise Redactor

image A noise redacted
![a](output/a_result.png)

image board noise redacted
![board](output/image_board_result.png)

image circle noise redacted
![image circle](output\image_circle_result.png)

image man woman noise redacted
![image man woman](output\image_man_woman_result.png)

image skeleton noise redacted
![image skeleton](output\image_skeleton_result.png)

image woman noise redacted
![image woman](output\image_woman_result.png)

## Getting Started <a name = "getting_started"></a>

### Installing

First of all you need install requirements library copy this code and run in terminal.

``` terminal
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

After you install requirements library you can choice between the projects and run it.

### 2d_convolution

``` terminal
python 2d_convolution.ipynb
```

### average reveal

``` terminal
python average_reveal.ipynb
```

### histogram equalizer

``` terminal
python histogram_equalizer.ipynb
```

### median noise redactor

``` terminal
python median_noise_redactor.ipynb
```
