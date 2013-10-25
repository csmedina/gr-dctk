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
#include "stream_to_tagged_stream_cc_impl.h"
#include <stdio.h>

namespace gr {
  namespace dctk {

    stream_to_tagged_stream_cc::sptr
    stream_to_tagged_stream_cc::make(int len_stream, const std::vector<tag_t> &tags)
    {
      return gnuradio::get_initial_sptr
        (new stream_to_tagged_stream_cc_impl(len_stream, tags));
    }

    /*
     * The private constructor
     */
    stream_to_tagged_stream_cc_impl::stream_to_tagged_stream_cc_impl(const int len_stream, const std::vector<tag_t> &tags)
      : gr::sync_block("stream_to_tagged_stream_cc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
              d_tags(tags),
              d_len_stream (len_stream)
    {
        set_output_multiple(d_len_stream);
    }

    /*
     * Our virtual destructor.
     */
    stream_to_tagged_stream_cc_impl::~stream_to_tagged_stream_cc_impl()
    {
    }

    int
    stream_to_tagged_stream_cc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];

          for(int i = 0; i < noutput_items; i += d_len_stream) {
            memcpy((void *) out, (void*)in, d_len_stream*sizeof (gr_complex));
            for(unsigned t = 0; t < d_tags.size(); t++) {
              add_item_tag(0, nitems_written(0)+i+d_tags[t].offset,
                           d_tags[t].key, d_tags[t].value);
            }
/*
            for(int j = 0; j < d_len_stream; ++j) {
                fprintf (stderr, "%f  ", std::real(in[j]));
            }
            fprintf (stderr, "\nTx\n");
            for(int j = 0; j < d_len_stream; ++j) {
                fprintf (stderr, "%f  ", std::real(out[j]));
            }
            fprintf (stderr, "\nRx\n");
*/
            out += d_len_stream;
            in += d_len_stream;
          }

        return noutput_items;
    }

  } /* namespace dctk */
} /* namespace gr */

