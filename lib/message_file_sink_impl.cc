#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "message_file_sink_impl.h"

namespace gr {
  namespace lora {

    message_file_sink::sptr
    message_file_sink::make(const std::string path) {
        return gnuradio::get_initial_sptr(new message_file_sink_impl(path));
    }

    /*
     * The private constructor
     */
    message_file_sink_impl::message_file_sink_impl(const std::string path)
      : gr::block("message_file_sink",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)) {

        message_port_register_in(pmt::mp("in"));
        set_msg_handler(pmt::mp("in"), boost::bind(&message_file_sink_impl::msg_handler, this, _1));

        d_file.open(path.c_str(), std::ios::out | std::ios::binary);
    }

    /*
     * Our virtual destructor.
     */
    message_file_sink_impl::~message_file_sink_impl() {
        if(d_file.is_open())
            d_file.close();
    }

    /*
     * Incoming message handler
     */
    void message_file_sink_impl::msg_handler(pmt::pmt_t msg) {
        uint32_t length = pmt::length(msg);
        //std::cout << "Writing " << length / sizeof(gr_complex) << " samples" << std::endl;
        gr_complex* raw_samples = (gr_complex *)pmt::blob_data(msg);
        d_file.write(reinterpret_cast<const char *>(raw_samples), length);
    }

  } /* namespace lora */
} /* namespace gr */
