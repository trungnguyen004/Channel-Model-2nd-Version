#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jason/gr-ChannelModel2/python
export PATH=/home/jason/gr-ChannelModel2/build/python:$PATH
export LD_LIBRARY_PATH=/home/jason/gr-ChannelModel2/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/jason/gr-ChannelModel2/build/swig:$PYTHONPATH
/usr/bin/python2 /home/jason/gr-ChannelModel2/python/qa_ChannelModel2_ff.py 
