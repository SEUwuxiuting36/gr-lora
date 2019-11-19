#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lora Receive Realtime
# Generated: Tue Nov 19 14:40:29 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import lora
import time
import wx


class lora_receive_realtime(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Lora Receive Realtime")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sf = sf = 7
        self.samp_rate = samp_rate = 5e6
        self.capture_freq = capture_freq = 433e6
        self.bw = bw = 125000
        self.target_freq = target_freq = capture_freq+0e6
        self.symbols_per_sec = symbols_per_sec = float(bw) / (2**sf)
        self.firdes_tap = firdes_tap = firdes.low_pass(1, samp_rate, bw, 10000, firdes.WIN_HAMMING, 6.67)
        self.downlink = downlink = False
        self.decimation = decimation = 5
        self.bitrate = bitrate = sf * (1 / (2**sf / float(bw)))

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=capture_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=True,
        )
        self.Add(self.wxgui_fftsink2_1.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(capture_freq, 0)
        self.uhd_usrp_source_0.set_gain(50, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.lora_message_socket_sink_0 = lora.message_socket_sink("127.0.0.1", 8000, 0)
        self.lora_lora_receiver_0 = lora.lora_receiver(samp_rate, capture_freq, (target_freq, ), bw, sf, False, 3, False, False, downlink, decimation, False, False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/wxt/Downloads/gr-lora/data/2/No2_74", False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_lora_receiver_0, 'frames'), (self.lora_message_socket_sink_0, 'in'))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.lora_lora_receiver_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_1, 0))    

    def get_sf(self):
        return self.sf

    def set_sf(self, sf):
        self.sf = sf
        self.set_bitrate(self.sf * (1 / (2**self.sf / float(self.bw))))
        self.set_symbols_per_sec(float(self.bw) / (2**self.sf))
        self.lora_lora_receiver_0.set_sf(self.sf)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_tap(firdes.low_pass(1, self.samp_rate, self.bw, 10000, firdes.WIN_HAMMING, 6.67))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)

    def get_capture_freq(self):
        return self.capture_freq

    def set_capture_freq(self, capture_freq):
        self.capture_freq = capture_freq
        self.set_target_freq(self.capture_freq+0e6)
        self.uhd_usrp_source_0.set_center_freq(self.capture_freq, 0)
        self.wxgui_fftsink2_1.set_baseband_freq(self.capture_freq)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_bitrate(self.sf * (1 / (2**self.sf / float(self.bw))))
        self.set_firdes_tap(firdes.low_pass(1, self.samp_rate, self.bw, 10000, firdes.WIN_HAMMING, 6.67))
        self.set_symbols_per_sec(float(self.bw) / (2**self.sf))

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq

    def get_symbols_per_sec(self):
        return self.symbols_per_sec

    def set_symbols_per_sec(self, symbols_per_sec):
        self.symbols_per_sec = symbols_per_sec

    def get_firdes_tap(self):
        return self.firdes_tap

    def set_firdes_tap(self, firdes_tap):
        self.firdes_tap = firdes_tap

    def get_downlink(self):
        return self.downlink

    def set_downlink(self, downlink):
        self.downlink = downlink

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_bitrate(self):
        return self.bitrate

    def set_bitrate(self, bitrate):
        self.bitrate = bitrate


def main(top_block_cls=lora_receive_realtime, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
