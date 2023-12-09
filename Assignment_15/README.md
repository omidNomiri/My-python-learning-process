# Snake Game

This repository contains two versions of a Snake game implemented in Python using the Arcade library.

## AI Snake Game

### [Code with AI](main_ai.py)

```python
import arcade
from snake import Snake
from food import Meat
```

### [Code without AI](main.py)

```python
import arcade
from snake import Snake
from food import Meatloaf
from food import Meat
from food import Plant
```

Instructions: Use arrow keys (UP, DOWN, LEFT, RIGHT) to control the snake in the non-AI version.
The AI version automatically moves the snake towards the food.
How to Run
Install the required dependencies:

```bash
pip install arcade
```

Run the AI Snake Game:

```bash
python main_ai.py
```

Run the Non-AI Snake Game:

``` bash
python main.py
```

## Screenshots

![Game Screenshot](https://github.com/omidNomiri/My-learning-process/blob/main/Assignment_15/game_image.png)

![Game Screenshot](https://github.com/omidNomiri/My-learning-process/blob/main/Assignment_15/README.md)

## License

This project is licensed under the MIT License.
