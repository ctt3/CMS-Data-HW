#!/bin/bash -e

# install dependencies using pip
pip install numpy
pip install pandas
pip install bokeh
pip install ipython
pip install pokitdok
pip install jupyter

# reset bash profile
. ~/.bash_profile

echo "Requirements installed."