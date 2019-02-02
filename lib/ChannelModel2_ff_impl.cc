/* -*- c++ -*- */
/* 
 * Copyright 2019 Jason Nguyen.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "ChannelModel2_ff_impl.h"
#include <stdexcept> //
#include <math.h> //

namespace gr {
  namespace ChannelModel2 {

    ChannelModel2_ff::sptr
    ChannelModel2_ff::make(float gt, float gr1, float dis, float ampl) //
    {
      return gnuradio::get_initial_sptr
        (new ChannelModel2_ff_impl(gt, gr1, dis, ampl)); //
    }

    /*
     * The private constructor
     */
    ChannelModel2_ff_impl::ChannelModel2_ff_impl(float gt, float gr1, float dis, float ampl) //
      : gr::block("ChannelModel2_ff",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
	d_gt(gt);	//
	d_gr1(gr1);
	d_dis(dis);
	d_ampl(ampl);
	}

    /*
     * Our virtual destructor.
     */
    ChannelModel2_ff_impl::~ChannelModel2_ff_impl()
    {
    }

    int
    ChannelModel2_ff_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

	for(int i = 0; i < noutput_items; i++) {
	  out[i] = ((float)(ampl() * d_rng.gasdev())) + (in[i]*((gt()*gr1())/(dis()*dis()))); //
	}

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ChannelModel2 */
} /* namespace gr */

