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
#include "spread_ccc_impl.h"

namespace gr {
  namespace dctk {

    spread_ccc::sptr
    spread_ccc::make(const std::vector<gr_complex>& spreading_code)
    {
      return gnuradio::get_initial_sptr
        (new spread_ccc_impl(spreading_code));
    }

    /*
     * The private constructor
     */
    spread_ccc_impl::spread_ccc_impl(const std::vector<gr_complex>& spreading_code)
      : gr::sync_interpolator("spread_ccc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
		      gr::io_signature::make(1, 1, sizeof(gr_complex)), spreading_code.size()),
		      d_code (spreading_code)
    {}

    /*
     * Our virtual destructor.
     */
    spread_ccc_impl::~spread_ccc_impl()
    {
    }

    int
    spread_ccc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];
        
        size_t codeSize = d_code.size();
        
        // Do spreading
        int no = 0;
        int ninput_items = noutput_items/codeSize;
        for(int i = 0; i < ninput_items; i++)
        {
			for(int j = 0; j < codeSize; j++)
			{
				out[j+no] = in[i] * d_code[j]; //Input data is multipled with the code
			}
			no += codeSize;
		}
        
        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace dctk */
} /* namespace gr */

