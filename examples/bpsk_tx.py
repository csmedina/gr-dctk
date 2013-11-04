#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Bpsk Tx
# Generated: Mon Nov  4 13:00:16 2013
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import dctk
import numpy

class bpsk_tx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Bpsk Tx")

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
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(samp_per_symb, firdes.root_raised_cosine(
        	samp_per_symb, samp_per_symb, 1, bandwidth_excess, 11*samp_per_symb))
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.dctk_generic_tx_path_0 = dctk.generic_tx_path(
            payload_packet_len=packet_len,
            sync_packet_len=len(sync_word),
            )
        self.blocks_vector_source_x_0 = blocks.vector_source_c(sync_word, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/csmedina/WiComModules/gr-dctk/build/tx_bits.txt")
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/csmedina/WiComModules/gr-dctk/build/tx_symbols.txt")
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/csmedina/WiComModules/gr-dctk/build/tx_2usrp.txt")
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, packet_len)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.dctk_generic_tx_path_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.dctk_generic_tx_path_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.dctk_generic_tx_path_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.root_raised_cosine_filter_0, 0))


# QT sink close method reimplementation

    def get_sync_word(self):
        return self.sync_word

    def set_sync_word(self, sync_word):
        self.sync_word = sync_word
        self.dctk_generic_tx_path_0.set_sync_packet_len(len(self.sync_word))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_symb, self.samp_per_symb, 1, self.bandwidth_excess, 11*self.samp_per_symb))

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.dctk_generic_tx_path_0.set_payload_packet_len(self.packet_len)

    def get_length_tag_name(self):
        return self.length_tag_name

    def set_length_tag_name(self, length_tag_name):
        self.length_tag_name = length_tag_name

    def get_bandwidth_excess(self):
        return self.bandwidth_excess

    def set_bandwidth_excess(self, bandwidth_excess):
        self.bandwidth_excess = bandwidth_excess
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_symb, self.samp_per_symb, 1, self.bandwidth_excess, 11*self.samp_per_symb))

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = bpsk_tx()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

