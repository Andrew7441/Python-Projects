# Turtle Dot Painting

## Project Summary

This small Python script uses the turtle graphics library to paint a grid of coloured dots on the screen. The colour palette is embedded as a list of RGB tuples (the script contains a commented-out snippet that shows how to extract a palette from an image using colorgram). The program demonstrates basic turtle control (positioning, pen up/down, heading), procedural drawing in rows, and the use of a custom colour palette to produce a Hirst-style dot painting.

## Quick Facts

Language: Python 3.x

Libraries used: turtle (standard library), random (standard library), optional colorgram.py to extract colours from an image

Visual output: a grid of coloured dots (17 dots per row × 14 rows in the included configuration)


## How to Run

- Ensure you have Python 3 installed.

- (Optional) If you want to extract colours from an image, install colorgram
'''python
pip install colorgram.py
'''

- Click the turtle graphics window to exit (screen.exitonclick() is used).


## License

This README and the example script are provided under the MIT License. Use and adapt freely.

## Acknowledgements

Colour extraction snippet: colorgram.py (optional)

Concept: Hirst-style dot grids and common Python turtle package
