/* -*- c++ -*- */


#ifndef INCLUDED_LORA_MESSAGE_SOCKET_SINK_H
#define INCLUDED_LORA_MESSAGE_SOCKET_SINK_H

#include <lora/api.h>
#include <gnuradio/block.h>

namespace gr {
    namespace lora {
        /*!
        * \brief Sink for messages, sent to socket.
        * \ingroup lora
        *
        */
        class LORA_API message_socket_sink : virtual public gr::block {
            public:
                typedef boost::shared_ptr<message_socket_sink> sptr;
                enum lora_layer { LORATAP = 0, LORAPHY, LORAMAC };

                /*!
                * \brief Return a shared_ptr to a new instance of lora::message_socket_sink.
                *
                * To avoid accidental use of raw pointers, lora::message_socket_sink's
                * constructor is in a private implementation
                * class. lora::message_socket_sink::make is the public interface for
                * creating new instances.
                */
                static sptr make(std::string ip, int port, enum lora_layer layer);
        };

    } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_MESSAGE_SOCKET_SINK_H */
