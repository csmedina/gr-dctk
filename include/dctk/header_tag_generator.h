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


#ifndef INCLUDED_DCTK_HEADER_TAG_GENERATOR_H
#define INCLUDED_DCTK_HEADER_TAG_GENERATOR_H

#include <dctk/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace dctk {

    /*!
     * \brief Creates a intermodule comunication message to inform the tagged stream demux the size of the header stream.
     * \ingroup dctk
     *
     */
    class DCTK_API header_tag_generator : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<header_tag_generator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of dctk::header_tag_generator.
       *
       * To avoid accidental use of raw pointers, dctk::header_tag_generator's
       * constructor is in a private implementation
       * class. dctk::header_tag_generator::make is the public interface for
       * creating new instances.
       */
      static sptr make(int header_len, int payload_len, std::string length_tag_name);
    };

  } // namespace dctk
} // namespace gr

#endif /* INCLUDED_DCTK_HEADER_TAG_GENERATOR_H */

