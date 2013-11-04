# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
install(FILES
    dctk_spread_ccc.xml
    dctk_despread_ccc.xml
    dctk_stream_to_tagged_stream_cc.xml
    dctk_generic_tx_path.xml
    dctk_frame_sync.xml
    dctk_peak_detector_abs_value_fb.xml
    dctk_header_tag_generator.xml
    dctk_generic_rx_path.xml DESTINATION share/gnuradio/grc/blocks
)
