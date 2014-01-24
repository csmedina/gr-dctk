#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr
from gnuradio import blocks
from gnuradio import digital
import dctk_swig as dctk

class generic_rx_path(gr.hier_block2):
    """
    This block represents a generic receiver path, which implements the phase, frame, carrier and symbol sinchronism. Also it cuts the frame into header and payload frames.
    """
    def __init__(self, payload_len=96, sync_seq=[complex(1,0),complex(-1,0)], threshold=.8):
        gr.hier_block2.__init__(self,
            "generic_rx_path",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signaturev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_float*1]),
            )

        ##################################################
        # Parameters
        ##################################################
        self.threshold = threshold
        self.sync_seq = sync_seq
        self.sync_header_len = len(sync_seq)
        self.items_per_header_symbol = 1
        self.payload_len = payload_len

        ##################################################
        # Variables
        ##################################################
        self.tag_len_name = tag_len_name = "packet_len"

        ##################################################
        # Blocks
        ##################################################
        self.frame_sync_0 = dctk.frame_sync (self.sync_seq, self.threshold)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(self.sync_header_len, self.items_per_header_symbol, 0, tag_len_name, "", False, gr.sizeof_gr_complex)
        self.dctk_header_tag_generator_0 = dctk.header_tag_generator(self.sync_header_len, payload_len, tag_len_name)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, self.sync_header_len)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.frame_sync_0, 0)) 
               
        self.connect((self.blocks_delay_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.frame_sync_0, 1), (self.digital_header_payload_demux_0, 1))
        
        self.connect((self.digital_header_payload_demux_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.dctk_header_tag_generator_0, 0))
        
        self.connect((self.frame_sync_0, 0), (self, 2))
        self.connect((self.digital_header_payload_demux_0, 1), (self, 1))
        self.connect((self.digital_header_payload_demux_0, 0), (self, 0))
        
        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.dctk_header_tag_generator_0, "header_data", self.digital_header_payload_demux_0, "header_data")
