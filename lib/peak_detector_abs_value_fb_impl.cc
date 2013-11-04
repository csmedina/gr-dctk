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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "peak_detector_abs_value_fb_impl.h"

namespace gr {
  namespace dctk {

    peak_detector_abs_value_fb::sptr
    peak_detector_abs_value_fb::make(float threshold)
    {
      return gnuradio::get_initial_sptr
        (new peak_detector_abs_value_fb_impl(threshold));
    }

    /*
     * The private constructor
     */
    peak_detector_abs_value_fb_impl::peak_detector_abs_value_fb_impl(float threshold)
      : gr::sync_block("peak_detector_abs_value_fb",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(char))), d_threshold(threshold)
    {}

    /*
     * Our virtual destructor.
     */
    peak_detector_abs_value_fb_impl::~peak_detector_abs_value_fb_impl()
    {
    }

    int
    peak_detector_abs_value_fb_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *iptr = (const float *) input_items[0];
        char *optr = (char *) output_items[0];

        memset(optr, 0, noutput_items*sizeof(char));

      float peak_val = -(float)INFINITY;
      int peak_ind = 0;
      unsigned char state = 0;
      int i = 0;

      //printf("noutput_items %d\n",noutput_items);
      while(i < noutput_items) {
        if(state == 0) {  // below threshold
          if(iptr[i] > d_threshold) {
            state = 1;
          }
          else {
            i++;
          }
        }
        else if(state == 1) {  // above threshold, have not found peak
          //printf("Entered State 1: %f  i: %d  noutput_items: %d\n", iptr[i], i, noutput_items);
          if(iptr[i] > peak_val) {
            peak_val = iptr[i];
            //peak_ind = i+1;
            peak_ind = i;
            i++;
          }
          else if(iptr[i] > d_threshold) {
            i++;
          }
          else {
            optr[peak_ind] = 1;
            state = 0;
            peak_val = -(float)INFINITY;
            //printf("Leaving  State 1: Peak: %f  Peak Ind: %d   i: %d  noutput_items: %d\n",
            //peak_val, peak_ind, i, noutput_items);
          }
        }
      }

      if(state == 0) {
        //printf("Leave in State 0, produced %d\n",noutput_items);
        return noutput_items;
      }
      else {   // only return up to passing the threshold
        //printf("Leave in State 1, only produced %d of %d\n",peak_ind,noutput_items);
        return peak_ind+1;
      }
    }

  } /* namespace dctk */
} /* namespace gr */

