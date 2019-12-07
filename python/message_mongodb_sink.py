import numpy
import pmt
from pymongo import MongoClient
from gnuradio import gr
from bson.binary import Binary
from datetime import datetime


class message_mongodb_sink(gr.basic_block):
    """
    Message block to store to MongoDB
    """
    def __init__(self, ip, port, db, collection, tag):
        gr.basic_block.__init__(self,
            name="message_mongodb_sink",
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.msg_handler)

        self.mongo_client = MongoClient(ip, port)
        self.db = self.mongo_client[db]
        self.collection = self.db[collection]

        if not tag is None:
            self.tag = tag
        else:
            self.tag = ''

    def msg_handler(self, msg):
        msg = pmt.to_python(msg)

        record = {
            "date": datetime.now(),
            "tag": self.tag,
            "chirp": Binary(msg.tobytes())
        }

        self.collection.insert_one(record)
