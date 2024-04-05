# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

in this project i made a histogram equalizer normal and clahe, reveal hidden item,2d convolution, median noise redactor.

### Output

#### 2D Convolution

| filter | input image | output image |
|--------------|-----------|-----------|
| sharpening filter | ![input image](input/spider.png) | ![sharpening filter](output/sharpening_result.png) |
| emboss filter | ![input image](input/spider.png) | ![emboss filter](output/emboss_result.png) |
| edge filter | ![input image](input/spider.png) | ![edge filter](output/edge_detection_result.png) |
| black zone filter | ![input image](input/spider.png) | ![black zone filter](output/black_zone_result.png) |

#### Item Reveal

average item reveal filter 3x3
![average item reveal filter](output/item_reveal_3X3_result.png)

average item reveal filter 5x5
![average item reveal filter](output/item_reveal_5X5_result.png)

#### Histogram Equalizer

| equalizer | input image VS output image |
|--------------|-----------|
| normal equalizer | ![landing place](output/landing_place_equalizer_result.png) |
| normal equalizer | ![land](output/land_equalizer_result.png) |
| clahe equalizer | ![figure](output/figure_equalizer_result.png) |

#### Median Noise Redactor

|image name | input image | output image |
|--------------|-----------|-----------|
| image A | ![a](input/a.png) | ![a](output/a_result.png) |
| image board | ![board](input/noisy_board.png) | ![board](output/image_board_result.png) |
| image circle | ![image circle](input/noisy_image.png) | ![image circle](output/image_circle_result.png) |
| image man woman | ![image man woman](input/man_woman.png) | ![image man woman](output/image_man_woman_result.png) |
| image skeleton | ![image skeleton](input/noisy_skeleton.png) | ![image skeleton](output/image_skeleton_result.png) |
| image woman | ![image woman](input/woman.png) | ![image woman](output/image_woman_result.png) |

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
