/* -*- c++ -*- */

#define CHANNELMODEL2_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ChannelModel2_swig_doc.i"

%{
#include "ChannelModel2/ChannelModel2_ff.h"
%}


%include "ChannelModel2/ChannelModel2_ff.h"
GR_SWIG_BLOCK_MAGIC2(ChannelModel2, ChannelModel2_ff);
