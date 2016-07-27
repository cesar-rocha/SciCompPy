# Installation of scientific python environment
This page is under development.

## Anaconda
Install [anaconda](https://www.continuum.io/downloads) with python 3.5.
This is a free scientific python platform available for Linux, OSX and Windows.
We call it scientific python because anaconda ships with the main packages (
libraries and "toolboxes" if you will) used in science such as numpy, scipy,
and matplotlib.

### Updating 
(If you are not familiar with command-line tools, there exists a GUI option.)

Anaconda ships with a package manager called `conda` that comes in handy. To update
anaconda you can use:

<code>
$ conda update --prefix CONDA_PATH anaconda
</code>

where `CONDA_PATH` is the path where anaconda is installed. For example, on my computer
`CONDA_PATH=/Users/crocha/anaconda3`.

To install or update a specific package use

<code>
$ conda install PACKAGE
</code>

where `PACKAGE` is the name of the package you want to install/update.
For example, we will be using a package called basemap for plotting maps.
To install basemap use

<code>
$ conda install basemap
</code>

Packages that are not available directly through Anaconda can still be install
with `conda` thanks to [conda-forge](https://conda-forge.github.io/). For example, 
to install the commonly used [Gibbs-Sea-Water](http://www.teos-10.org/software.htm#1) "toolbox"

<code>
$ conda install gsw --chanell conda-forge
</code>

## Why Python 3?
(If you never used python before, you do not need to worry about this.)

Most of scientific packages support python3. If you are a python newbie,
you should start using python3. [PSF](https://www.python.org/psf/) will drop support to python2 by 2020
and the next version of IPython (6.0) will no longer support python2.

If you currently use python2, consider migrating to python3. I encourage you
to check this [webpage](http://python-3-for-scientists.readthedocs.io/en/latest/) that some friends have put together to help scientists
migrate from 2 to 3.
