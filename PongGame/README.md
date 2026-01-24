# Pong Game

## Summary 

Simple two-player Pong clone implemented with Python's turtle. Lightweight, dependency-free (uses Python standard library), and easy to run and tweak.

## Files

- main.py — game loop / entry point (the script that imports ball, paddle, scoreboard)
- ball.py — Ball class
- paddle.py — Paddle class
- scoreboard.py — Scoreboard class
- If your entry script has a different name, run that file instead of main.py.

## Run

From the project directory:
```python
python main.py
```
## Controls

- Left paddle: w (up), s (down)
- Right paddle: Up (up), Down (down)

## Behavior / Notes

- Ball speed is controlled by Ball.spd. Smaller values → faster frame updates.
- Ball.Reset_Position() recenters the ball and resets speed.
- Collisions: paddles reverse X direction; top/bottom edges reverse Y direction.
- Scoring: when the ball passes the left or right edge, the opposite player’s score increments.

## Quick Tweaks

- Increase/decrease Ball.Xmove / Ball.Ymove to change movement per frame.
- Adjust Ball.spd to change overall game tempo.
- Change paddle movement step in Paddle.up() / Paddle.down().

## License

Use however you like. Attribution appreciated but not required. ENJOY
