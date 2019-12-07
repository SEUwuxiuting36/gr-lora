#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from gnuradio import gr, gr_unittest
from gnuradio import blocks
import lora_swig as lora

class qa_receiver (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_receiver, "qa_receiver.xml")
