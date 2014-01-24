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
from gnuradio import digital

class generic_synch(gr.hier_block2):
    """
    The generic synchronizer is used to prototype at the receiver the phase, carrier and symbol syncronization.
    It uses a costas loop algorithm followed by a Muller&Muller symbol synchronization algorithm.
    """
    def __init__(self, costas_loop_bw = 10E-3, costas_order = 2, mm_omega = 2, mm_gain_omega = 0.00765625, mm_mu = .5, mm_gain_mu = .175, mm_omega_relative_limit = .005):
        gr.hier_block2.__init__(self,
            "generic_synch",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            )
            
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(costas_loop_bw, costas_order)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(mm_omega, mm_gain_omega, mm_mu, mm_gain_mu, mm_omega_relative_limit)
        
        self.connect((self, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self, 0))
            
