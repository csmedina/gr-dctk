#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Bpsk Tx Rx
# Generated: Fri Oct 25 15:48:37 2013
##################################################

execfile("/home/csmedina/.grc_gnuradio/generic_rx_path.py")
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import dctk
import numpy

class bpsk_tx_rx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Bpsk Tx Rx")

        ##################################################
        # Variables
        ##################################################
        self.sync_word = sync_word = [complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(-1, 0), complex(1, 0), complex(1, 0), complex(-1, 0)]
        self.samp_rate = samp_rate = 32000
        self.payload_mod = payload_mod = digital.constellation_bpsk()
        self.packet_len = packet_len = 96
        self.length_tag_name = length_tag_name = "packet_len"

        ##################################################
        # Blocks
        ##################################################
        self.generic_rx_path_0 = generic_rx_path(
            sync_header_len=len(sync_word),
            items_per_header_symbol=1,
            frequency_mod_sensitivity=-2,
            payload_len=packet_len,
        )
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(payload_mod.base())
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.dctk_generic_tx_path_0 = dctk.generic_tx_path(
            payload_packet_len=packet_len,
            sync_packet_len=len(sync_word),
            )
        self.dctk_frame_sync_0 = dctk.frame_sync((sync_word), .9)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(sync_word, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/csmedina/WiComModules/gr-dctk/build/rx.txt")
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/csmedina/WiComModules/gr-dctk/build/tx.txt")
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, packet_len)), True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.dctk_generic_tx_path_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.dctk_generic_tx_path_0, 1))
        self.connect((self.dctk_generic_tx_path_0, 0), (self.dctk_frame_sync_0, 0))
        self.connect((self.dctk_generic_tx_path_0, 0), (self.generic_rx_path_0, 0))
        self.connect((self.generic_rx_path_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.generic_rx_path_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.generic_rx_path_0, 1), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.dctk_frame_sync_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.dctk_frame_sync_0, 1), (self.generic_rx_path_0, 2))


# QT sink close method reimplementation

    def get_sync_word(self):
        return self.sync_word

    def set_sync_word(self, sync_word):
        self.sync_word = sync_word
        self.dctk_generic_tx_path_0.set_sync_packet_len(len(self.sync_word))
        self.generic_rx_path_0.set_sync_header_len(len(self.sync_word))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.dctk_generic_tx_path_0.set_payload_packet_len(self.packet_len)
        self.generic_rx_path_0.set_payload_len(self.packet_len)

    def get_length_tag_name(self):
        return self.length_tag_name

    def set_length_tag_name(self, length_tag_name):
        self.length_tag_name = length_tag_name

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = bpsk_tx_rx()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

