# DroneMapp

## Color Relief + Slope and Shaded Relief

View Jupyter Notebook on [Jupyter Notebook Viewer](http://nbviewer.jupyter.org/github/leocamello/ColorReliefChallenge/blob/master/ColorReliefChallenge.ipynb) or on [GitHub](https://github.com/leocamello/ColorReliefChallenge/blob/master/ColorReliefChallenge.ipynb)

<img src="jotunheimen_output.png" alt="" width="550px" height="550px">

### Libraries

- GDAL
- Numpy

### Installation

In my development environment I have been using [Conda](http://conda.pydata.org/docs/index.html) package manager. It is included in [Anaconda](https://www.continuum.io/downloads) Python distribution.

#### GDAL

To install GDAL in the environment:

```bash
$ conda install GDAL
```

### How To Run

```bash
$ python main.py <input_dem> <color_relief_txt> <slope_color_txt> <output_dem>
```
