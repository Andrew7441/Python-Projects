# Turtle Crossing

## Summary

Simple arcade-style Turtle Crossing game built with Python's turtle module. Guide the turtle from the bottom to the top of the screen while avoiding cars. Each successful crossing increases the level and game speed.

## Requirements

- Python 3.8+ (standard library only)
- No external packages

## Files

- main.py — game setup and event loop
- player.py — Player class (turtle controlled by player)
- car_manager.py — CarManager class (spawns and moves cars)
- scoreboard.py — Scoreboard class (tracks level / game over)

## Installation & Run

- Save the four files into a folder.
- From that folder run:
```python
python main.py
```
## Controls

- Up arrow — move forward
- Down arrow — move backward

## Behavior

- Reaching the top resets the player to start, increases level and car speed.
- Collision with a car displays GAME OVER and stops the game.