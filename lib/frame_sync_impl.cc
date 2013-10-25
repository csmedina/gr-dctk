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

#include <gnuradio/filter/fir_filter_ccc.h>
#include <gnuradio/blocks/complex_to_mag.h>
#include <gnuradio/blocks/multiply_const_ff.h>

#include <gnuradio/io_signature.h>
#include "frame_sync_impl.h"
#include "dctk/peak_detector_abs_value_fb.h"

namespace gr {
  namespace dctk {

    frame_sync::sptr
    frame_sync::make(const std::vector<gr_complex>& sync_sequence, float threshold)
    {
      return gnuradio::get_initial_sptr
        (new frame_sync_impl(sync_sequence, threshold));
    }

    /*
     * The private constructor
     */
    frame_sync_impl::frame_sync_impl(const std::vector<gr_complex>& sync_sequence, float threshold)
      : gr::hier_block2("frame_sync",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make2(2, 2, sizeof(float), sizeof(char)))
    {
        std::vector<gr_complex> d_sync_sequence = std::vector<gr_complex> (sync_sequence);
        std::vector<int>::size_type sz = sync_sequence.size();
        float norm = 0;

        for (unsigned i=0; i<sz; i++)
        {
            float n = std::norm(sync_sequence[i]);
            norm += (n*n);
        }

        // reverse vector using operator[]:
        for (unsigned i=0; i<sz/2; i++)
        {
          gr_complex temp;
          temp = d_sync_sequence[sz-1-i];
          d_sync_sequence[sz-1-i] = std::conj(d_sync_sequence[i]);
          d_sync_sequence[i] = std::conj(temp);
        }

        gr::blocks::multiply_const_ff::sptr         normalizer(gr::blocks::multiply_const_ff::make(
                                                        sqrt( 1. / (norm * sync_sequence.size()))
                                                        ));
        gr::filter::fir_filter_ccc::sptr            convolutor(gr::filter::fir_filter_ccc::make(1, d_sync_sequence));
        dctk::peak_detector_abs_value_fb::sptr      detector(dctk::peak_detector_abs_value_fb::make(threshold));
        gr::blocks::complex_to_mag::sptr            mag(gr::blocks::complex_to_mag::make());

        connect(self(),                     0, convolutor,              0);
        connect(convolutor,                 0, mag,                     0);
        connect(mag,                        0, normalizer,              0);
        connect(normalizer,                 0, self(),                  0);

        connect(normalizer,                 0, detector,                0);
        connect(detector,                   0, self(),                  1);
    }

    /*
     * Our virtual destructor.
     */
    frame_sync_impl::~frame_sync_impl()
    {
    }


  } /* namespace dctk */
} /* namespace gr */

