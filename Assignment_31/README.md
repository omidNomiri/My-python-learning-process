# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

in this project i made a histogram maker, noise redactor,foreground focus, edge detection and side edge detection.

### Output

#### Histogram

plot histogram
![plot histogram](output/plot.jpg)

hist histogram
![hist histogram](output/hist.jpg)

bar histogram
![bar histogram](output/bar.jpg)

#### Foreground Focus

![focused image](output/focused_image.png)

#### Edge Detector

![lion edge](output/lion_edge.png)

#### Side Edge Detector

horizontal edge

![horizontal edge](output/horizontal_edge_image.png)

vertical edge

![vertical edge](output/vertical_edge_image.png)

#### Noise Redactor

3x3 noise redacted
![alt text](output/3X3_noise_board_redacted.png)
![alt text](output/3X3_noise_redacted.png)
![alt text](output/3X3_noise_skeleton_redacted.png)

5x5 noise redacted
![alt text](output/5X5_noise_board_redacted.png)
![alt text](output/5X5_noise_redacted.png)
![alt text](output/5X5_noise_skeleton_redacted.png)

15x15 noise redacted
![alt text](output/15X15_noise_board_redacted.png)
![alt text](output/15X15_noise_redacted.png)
![alt text](output/15X15_noise_skeleton_redacted.png)

## Getting Started <a name = "getting_started"></a>

### Installing

First of all you need install requirements library copy this code and run in terminal.

``` terminal
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

After you install requirements library you can choice between the projects and run it.

### histogram

``` terminal
python histogram.py
```

### foreground focus

``` terminal
python foreground_focus.py
```

### edge detection

``` terminal
python edge_detection.py
```

### side edge detection

``` terminal
python side_edge_detection.py
```

### noise redactor

``` terminal
python noise_redactor.py
```
