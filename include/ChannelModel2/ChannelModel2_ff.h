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


#ifndef INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_H
#define INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_H

#include <ChannelModel2/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ChannelModel2 {

    /*!
     * \brief <+description of block+>
     * \ingroup ChannelModel2
     *
     */
    class CHANNELMODEL2_API ChannelModel2_ff : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<ChannelModel2_ff> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ChannelModel2::ChannelModel2_ff.
       *
       * To avoid accidental use of raw pointers, ChannelModel2::ChannelModel2_ff's
       * constructor is in a private implementation
       * class. ChannelModel2::ChannelModel2_ff::make is the public interface for
       * creating new instances.
       */
      static sptr make(float gt, float gr1, float dis, float ampl); //
	virtual void d_gt(float gt) =0; //
	virtual float gt() =0;
	virtual void d_gr1(float gr1) =0;
	virtual float gr1() =0;
	virtual void d_dis(float dis) =0;
	virtual float dis() =0;
	virtual void d_ampl(float ampl) =0;
	virtual float ampl() =0;

    };

  } // namespace ChannelModel2
} // namespace gr

#endif /* INCLUDED_CHANNELMODEL2_CHANNELMODEL2_FF_H */

