# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

in this part i did some exercise with HSV color model and code balloon detection, color detection, mater welon, spiderman outfit changer, superman background changer, T_shirt color changer and skin detector.

### Output

#### mater welon

| title | image |
|--------------|-----------|
| input image | ![input](input/melon.png) |
| output image | ![decoder encoder app](output/materwelon.png) |

#### spiderman outfit changer

| title | image |
|--------------|-----------|
| input image | ![input image](input/spiderman.png) |
| output image | ![output image](output/spiderman.png) |

#### balloon detection

| title | image |
|--------------|-----------|
| input image | ![input image](input/balloon.png) |
| output image | ![output image](output/red_balloon.png) |

#### T_shirt color changer

| title | image |
|--------------|-----------|
| input image | ![input image](input/T_shirt.png) |
| output image | ![output image](output/blue_T_shirt.png) |

#### superman green curtain

| title | image |
|--------------|-----------|
| input image | ![input image](input/superman.png) |
| output image | ![output image](output/superman_sky.png) |

## Getting Started <a name = "getting_started"></a>

### Installing

First of all you need install requirements library copy this code and run in terminal.

``` terminal
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

After you install requirements library you can choice between the projects and run it.

### decoder/encoder app

``` terminal
python enc_and_dec_image/app.py
```

### color detection

``` terminal
jupyter nbconvert --to script color_detection.ipynb
```

### pillow(PIL) exercise

``` terminal
jupyter nbconvert --to script PIL.ipynb
```

### pos landmark detection

> **use python 3.10**

``` terminal
jupyter nbconvert --to script pos_landmark.ipynb
```

### remove background

``` terminal
jupyter nbconvert --to script remove_background.ipynb
```
