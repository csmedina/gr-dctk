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
#include "despread_ccc_impl.h"

namespace gr {
  namespace dctk {

    despread_ccc::sptr
    despread_ccc::make(const std::vector<gr_complex>& despreading_code)
    {
      return gnuradio::get_initial_sptr
        (new despread_ccc_impl(despreading_code));
    }

    /*
     * The private constructor
     */
    despread_ccc_impl::despread_ccc_impl(const std::vector<gr_complex>& despreading_code)
      : gr::sync_decimator("despread_ccc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
		      gr::io_signature::make(1, 1, sizeof(gr_complex)), despreading_code.size()),
		      d_code (despreading_code)
    {}

    /*
     * Our virtual destructor.
     */
    despread_ccc_impl::~despread_ccc_impl()
    {
    }

    int
    despread_ccc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];

        size_t codeSize = d_code.size();

        // Do spreading
        int no = 0;
        for(int i = 0; i < noutput_items; i++)
        {
			out[i] = 0;
			for(int j = 0; j < codeSize; j++)
			{
				out[i] += (in[j+no] * d_code[j]); //Input data is multipled with the code
			}
			no += codeSize;
		}
        return noutput_items;
    }

  } /* namespace dctk */
} /* namespace gr */

