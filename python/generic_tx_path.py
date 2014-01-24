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
##################################################
# Title: Generic transmission path
# Author: Cesar Medina (csmedina@gmail.com)
# Description: This forms a generic transmission path for digital communications, it accepts a payload and a synchronizatino header to form a
#              digital transmission packet
##################################################

from gnuradio import blocks
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.filter import firdes
import dctk_swig as dctk

class generic_tx_path(gr.hier_block2):
    """
    This forms a generic transmission path for digital communications, it accepts a payload and a synchronizatino header to form a digital transmission packet.
    """
    def __init__(self, payload_packet_len=96, sync_packet_len=96):
        gr.hier_block2.__init__(self,
            "Generic transmission path",
            gr.io_signaturev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            )

        ##################################################
        # Parameters
        ##################################################
        self.payload_packet_len = payload_packet_len
        self.sync_packet_len = sync_packet_len

        ##################################################
        # Variables
        ##################################################
        self.length_tag_name = length_tag_name = "packet_len"

        ##################################################
        # Blocks
        ##################################################
        self.dctk_stream_to_tagged_stream_cc_1 = dctk.stream_to_tagged_stream_cc(payload_packet_len, tagged_streams.make_lengthtags((payload_packet_len,), (0,), length_tag_name))
        self.dctk_stream_to_tagged_stream_cc_0 = dctk.stream_to_tagged_stream_cc(sync_packet_len, tagged_streams.make_lengthtags((sync_packet_len,), (0,), length_tag_name))
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, length_tag_name)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self, 0))
        self.connect((self, 0), (self.dctk_stream_to_tagged_stream_cc_0, 0))
        self.connect((self.dctk_stream_to_tagged_stream_cc_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self, 1), (self.dctk_stream_to_tagged_stream_cc_1, 0))
        self.connect((self.dctk_stream_to_tagged_stream_cc_1, 0), (self.blocks_tagged_stream_mux_0, 1))

# QT sink close method reimplementation

    def get_payload_packet_len(self):
        return self.payload_packet_len

    def set_payload_packet_len(self, payload_packet_len):
        self.payload_packet_len = payload_packet_len

    def get_sync_packet_len(self):
        return self.sync_packet_len

    def set_sync_packet_len(self, sync_packet_len):
        self.sync_packet_len = sync_packet_len

    def get_length_tag_name(self):
        return self.length_tag_name

    def set_length_tag_name(self, length_tag_name):
        self.length_tag_name = length_tag_name
