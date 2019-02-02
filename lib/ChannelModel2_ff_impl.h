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

#ifndef INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_IMPL_H
#define INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_IMPL_H

#include <ChannelModel2/ChannelModel2_ff.h>
#include <gnuradio/random.h> //

namespace gr {
  namespace ChannelModel2 {

    class ChannelModel2_ff_impl : public ChannelModel2_ff
    {
     private:
      float my_gt;
	float my_gr1;
	float my_dis;
	float my_ampl;
	gr::random d_rng;

     public:
      ChannelModel2_ff_impl(float gt, float gr1, float dis, float ampl); //
      ~ChannelModel2_ff_impl();

	void d_gt(float gt) {my_gt = gt;}
	float gt() {return my_gt;}
	void d_gr1(float gr1) {my_gr1 = gr1;}
	float gr1() {return my_gr1;}
	void d_dis(float dis) {my_dis = dis;}
	float dis() {return my_dis;}
	void d_ampl(float ampl) {my_ampl = ampl;}
	float ampl() {return my_ampl;}

      // Where all the action really happens

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace ChannelModel2
} // namespace gr

#endif /* INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_IMPL_H */

