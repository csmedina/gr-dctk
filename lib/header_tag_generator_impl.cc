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
#include "header_tag_generator_impl.h"

#define msg_port_id     pmt::mp("header_data")

namespace gr {
  namespace dctk {

    header_tag_generator::sptr
    header_tag_generator::make(int header_len, int payload_len, std::string length_tag_name)
    {
      return gnuradio::get_initial_sptr
        (new header_tag_generator_impl(header_len, payload_len, length_tag_name));
    }

    /*
     * The private constructor
     */
    header_tag_generator_impl::header_tag_generator_impl(int header_len, int payload_len, std::string length_tag_name)
      : gr::sync_block("header_tag_generator",
              io_signature::make(1, 1, sizeof (unsigned char)),
              gr::io_signature::make(0, 0, 0)
              ), d_header_len(header_len), d_length_tag_name(length_tag_name), d_payload_len(payload_len)
    {
        message_port_register_out(msg_port_id);
        set_output_multiple(header_len);
    }

    /*
     * Our virtual destructor.
     */
    header_tag_generator_impl::~header_tag_generator_impl()
    {
    }

    int
    header_tag_generator_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const unsigned char *in = (const unsigned char *) input_items[0];

        if (noutput_items < d_header_len) {
            return 0;
        }

        pmt::pmt_t dict(pmt::make_dict());
        dict = pmt::dict_add(dict, pmt::string_to_symbol(d_length_tag_name), pmt::from_long(d_payload_len));
        message_port_pub(msg_port_id, dict);

        return d_header_len;
    }

  } /* namespace dctk */
} /* namespace gr */

