#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Bpsk Rx
# Generated: Mon Nov  4 16:30:15 2013
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dctk
import wx

class bpsk_rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Bpsk Rx")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sync_word = sync_word = [complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0)]
        self.samp_rate = samp_rate = 100000
        self.samp_per_symb = samp_per_symb = 8
        self.payload_mod = payload_mod = digital.constellation_bpsk()
        self.packet_len = packet_len = 96
        self.length_tag_name = length_tag_name = "packet_len"
        self.bandwidth_excess = bandwidth_excess = .9

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Correlation and Detection",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_per_symb, 1, bandwidth_excess, 11*samp_per_symb))
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(samp_per_symb, 0.03*0.03, 0.05, .03, 0.5)
        self.dctk_generic_rx_path_0 = dctk.generic_rx_path(
        		payload_len=packet_len, sync_seq=(sync_word), threshold=.8
        		)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/csmedina/WiComModules/gr-dctk/build/tx_2usrp.txt", True)
        self.blocks_file_sink_0_0_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/csmedina/WiComModules/gr-dctk/build/rx_header.txt")
        self.blocks_file_sink_0_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/csmedina/WiComModules/gr-dctk/build/rx.txt")
        self.blocks_file_sink_0_0_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.dctk_generic_rx_path_0, 2), (self.wxgui_scopesink2_0, 0))
        self.connect((self.dctk_generic_rx_path_0, 1), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.dctk_generic_rx_path_0, 0))
        self.connect((self.dctk_generic_rx_path_0, 0), (self.blocks_file_sink_0_0_0_1, 0))


# QT sink close method reimplementation

    def get_sync_word(self):
        return self.sync_word

    def set_sync_word(self, sync_word):
        self.sync_word = sync_word

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_per_symb, 1, self.bandwidth_excess, 11*self.samp_per_symb))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_symb)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_length_tag_name(self):
        return self.length_tag_name

    def set_length_tag_name(self, length_tag_name):
        self.length_tag_name = length_tag_name

    def get_bandwidth_excess(self):
        return self.bandwidth_excess

    def set_bandwidth_excess(self, bandwidth_excess):
        self.bandwidth_excess = bandwidth_excess
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_per_symb, 1, self.bandwidth_excess, 11*self.samp_per_symb))

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = bpsk_rx()
    tb.Start(True)
    tb.Wait()

