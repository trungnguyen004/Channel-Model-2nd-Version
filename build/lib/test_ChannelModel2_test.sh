#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jason/gr-ChannelModel2/lib
export PATH=/home/jason/gr-ChannelModel2/build/lib:$PATH
export LD_LIBRARY_PATH=/home/jason/gr-ChannelModel2/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-ChannelModel2 
