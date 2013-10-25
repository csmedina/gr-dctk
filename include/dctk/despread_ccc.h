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


#ifndef INCLUDED_DCTK_DESPREAD_CCC_H
#define INCLUDED_DCTK_DESPREAD_CCC_H

#include <dctk/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace dctk {

    /*!
     * \brief Despreads the symbols by a spreading code.
     * \ingroup dctk
     *
     * Block that implements the de-spreading of a sequence of symbols (complex) 
     * by a de-spreading code (complex). The output is a complex sequence.
     */
    class DCTK_API despread_ccc : virtual public gr::sync_decimator
    {
     public:
      typedef boost::shared_ptr<despread_ccc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of dctk::despread_ccc.
       *
       * To avoid accidental use of raw pointers, dctk::despread_ccc's
       * constructor is in a private implementation
       * class. dctk::despread_ccc::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<gr_complex>& despreading_code);
    };

  } // namespace dctk
} // namespace gr

#endif /* INCLUDED_DCTK_DESPREAD_CCC_H */

