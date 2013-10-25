/* -*- c++ -*- */
/*
 * Copyright 2013 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_DCTK_STREAM_TO_TAGGED_STREAM_CC_IMPL_H
#define INCLUDED_DCTK_STREAM_TO_TAGGED_STREAM_CC_IMPL_H

#include <dctk/stream_to_tagged_stream_cc.h>

namespace gr {
  namespace dctk {

    class stream_to_tagged_stream_cc_impl : public stream_to_tagged_stream_cc
    {
     private:
      std::vector<tag_t> d_tags;
      int d_len_stream;

     public:
      stream_to_tagged_stream_cc_impl(const int len_stream, const std::vector<tag_t> &tags);
      ~stream_to_tagged_stream_cc_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace dctk
} // namespace gr

#endif /* INCLUDED_DCTK_STREAM_TO_TAGGED_STREAM_CC_IMPL_H */

