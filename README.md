# Nearest Neighbour and Bilinear Interpolation in Python

This Python project implements two common image interpolation techniques: Nearest Neighbour Interpolation and Bilinear Interpolation. These techniques are useful for resizing images while preserving their quality to some extent.

## Features

- **Nearest Neighbour Interpolation**: This method selects the nearest pixel value to the interpolated point. It's simple and fast but may produce blocky artifacts.
  
- **Bilinear Interpolation**: This method considers the closest four pixels surrounding the interpolated point and calculates the weighted average. It provides smoother results compared to Nearest Neighbour Interpolation.

## Dependencies

- Python (>= 3.x)
- PIL (Python Imaging Library)
- NumPy

## Installation

You can install the required dependencies using pip:

```bash
pip install pillow numpy
