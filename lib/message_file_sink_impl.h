/* -*- c++ -*- */


#ifndef INCLUDED_LORA_MESSAGE_FILE_SINK_IMPL_H
#define INCLUDED_LORA_MESSAGE_FILE_SINK_IMPL_H

#include <lora/message_file_sink.h>
#include <string>
#include <fstream>

namespace gr {
  namespace lora {

    class message_file_sink_impl : public message_file_sink {
        private:
            std::ofstream d_file;

        public:
            message_file_sink_impl(const std::string path);
            ~message_file_sink_impl();

            void msg_handler(pmt::pmt_t msg);
    };

  } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_MESSAGE_FILE_SINK_IMPL_H */
