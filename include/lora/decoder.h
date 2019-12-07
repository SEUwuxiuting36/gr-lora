/* -*- c++ -*- */


#ifndef INCLUDED_LORA_DECODER_H
#define INCLUDED_LORA_DECODER_H

#include <lora/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace lora {

    /*!
     * \brief <+description of block+>
     * \ingroup lora
     *
     */
    class LORA_API decoder : virtual public gr::sync_block {
     public:
      typedef boost::shared_ptr<decoder> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of lora::decoder.
       *
       * To avoid accidental use of raw pointers, lora::decoder's
       * constructor is in a private implementation
       * class. lora::decoder::make is the public interface for
       * creating new instances.
       */
      static sptr make(float samp_rate, uint32_t bandwidth, uint8_t sf, bool implicit, uint8_t cr, bool crc, bool reduced_rate, bool disable_drift_correction);

      virtual void set_sf(uint8_t sf) = 0;
      virtual void set_samp_rate(float samp_rate) = 0;
    };

  } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_DECODER_H */
