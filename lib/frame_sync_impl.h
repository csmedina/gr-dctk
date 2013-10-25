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

#ifndef INCLUDED_DCTK_FRAME_SYNC_IMPL_H
#define INCLUDED_DCTK_FRAME_SYNC_IMPL_H

#include <dctk/frame_sync.h>

namespace gr {
  namespace dctk {

    class frame_sync_impl : public frame_sync
    {
     private:
     public:
      frame_sync_impl(const std::vector<gr_complex>& sync_sequence, float threshold);
      ~frame_sync_impl();

      // Where all the action really happens
    };

  } // namespace dctk
} // namespace gr

#endif /* INCLUDED_DCTK_FRAME_SYNC_IMPL_H */

