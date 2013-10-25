/* -*- c++ -*- */

#define DCTK_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "dctk_swig_doc.i"

%{
#include "dctk/spread_ccc.h"
#include "dctk/despread_ccc.h"
#include "dctk/stream_to_tagged_stream_cc.h"
#include "dctk/frame_sync.h"
#include "dctk/peak_detector_abs_value_fb.h"
#include "dctk/header_tag_generator.h"
%}


%include "dctk/spread_ccc.h"
GR_SWIG_BLOCK_MAGIC2(dctk, spread_ccc);
%include "dctk/despread_ccc.h"
GR_SWIG_BLOCK_MAGIC2(dctk, despread_ccc);

%include "dctk/stream_to_tagged_stream_cc.h"
GR_SWIG_BLOCK_MAGIC2(dctk, stream_to_tagged_stream_cc);
%include "dctk/frame_sync.h"
GR_SWIG_BLOCK_MAGIC2(dctk, frame_sync);
%include "dctk/peak_detector_abs_value_fb.h"
GR_SWIG_BLOCK_MAGIC2(dctk, peak_detector_abs_value_fb);
%include "dctk/header_tag_generator.h"
GR_SWIG_BLOCK_MAGIC2(dctk, header_tag_generator);
