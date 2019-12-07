/* -*- c++ -*- */


#ifndef INCLUDED_LORA_MESSAGE_FILE_SINK_H
#define INCLUDED_LORA_MESSAGE_FILE_SINK_H

#include <lora/api.h>
#include <gnuradio/block.h>
#include <string>

namespace gr {
  namespace lora {

    /*!
     * \brief <+description of block+>
     * \ingroup lora
     *
     */
    class LORA_API message_file_sink : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<message_file_sink> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of lora::message_file_sink.
       *
       * To avoid accidental use of raw pointers, lora::message_file_sink's
       * constructor is in a private implementation
       * class. lora::message_file_sink::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string path);
    };

  } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_MESSAGE_FILE_SINK_H */
