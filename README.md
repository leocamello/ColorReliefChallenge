# DroneMapp

## Color Relief + Slope and Shaded Relief

![](output.png)

### Libraries

- GDAL
- Mapnik

### Installation

In my development environment I have been using [Conda](http://conda.pydata.org/docs/index.html) package manager. It is included in [Anaconda](https://www.continuum.io/downloads) Python distribution.

#### Environment

As [Mapnik](http://mapnik.org/index.html) for Windows is 32-bit I created a new environment with Python 2.7 32 bit.

```bash
$ set CONDA_FORCE_32BIT=1
$ conda create --name dronemapp python=2.7
```

To activate the environment:

```bash
$ set CONDA_FORCE_32BIT=1
$ activate dronemapp
```

To deactivate the environment:

```bash
$ deactivate
```

#### GDAL

To install GDAL in the environment:

```bash
$ conda install GDAL
```

#### Mapnik

Mapnik installation was a little more confused. In my development environment I use Windows 10. Maybe in other platforms it can be easier to make Mapnik work. I will describe the steps I took:

Download the Windows Runtime package for use via Python from: 
[http://mapnik.s3.amazonaws.com/dist/v2.2.0/mapnik-win-v2.2.0.zip](http://mapnik.s3.amazonaws.com/dist/v2.2.0/mapnik-win-v2.2.0.zip)

Extract the archive to:
C:\mapnik-v2.2.0\

Setup the environment variables:

```bash
$ set PATH=c:\\mapnik-v2.2.0\lib;%PATH%
$ set PATH=c:\\mapnik-v2.2.0\bin;%PATH%
```

And here comes the difference from Mapnik's website:

Copy the Mapnik site-packages folder:
C:\mapnik-v2.2.0\python\2.7\site-packages\mapnik

To your environment site-packages folder:
C:\Anaconda2\envs\dronemapp\Lib\site-packages

After that create the following folder:
C:\Anaconda2\envs\dronemapp\Lib\mapnik\

And move the following folders to that location:
C:\mapnik-v2.2.0\bin
C:\mapnik-v2.2.0\demo
C:\mapnik-v2.2.0\lib
C:\mapnik-v2.2.0\share

So now you have:
C:\Anaconda2\envs\dronemapp\Lib\mapnik\bin
C:\Anaconda2\envs\dronemapp\Lib\mapnik\demo
C:\Anaconda2\envs\dronemapp\Lib\mapnik\lib
C:\Anaconda2\envs\dronemapp\Lib\mapnik\share

To finish you have to modify two Python scripts:

C:\Anaconda2\envs\dronemapp32\Lib\site-packages\mapnik\paths.py

```python
...
mapniklibpath = path.normpath(path.join(__file__,'../../../mapnik/lib/')) 
...
```

C:\Anaconda2\envs\dronemapp32\Lib\site-packages\mapnik\mapnik_settings.py

```python
...
mapnik_data_dir = path.normpath(path.join(__file__,'../../../mapnik/share/')) 
...
```

Now everything should work!

:)

### How To Run

```bash
$ python main.py ./Example/jotunheimen/jotunheimen.tif ./Example/jotunheimen/jotunheimen_color_relief.txt ./Example/jotunheimen/jotunheimen_color_slope.txt ./Example/jotunheimen/output.png
```