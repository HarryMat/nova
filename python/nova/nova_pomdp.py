""" The MIT License (MIT)

    Copyright (c) 2015 Kyle Hollins Wray, University of Massachusetts

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import ctypes as ct
import platform
import os.path


# Check if we need to create the nova variable. If so, import the correct library
# file depending on the platform.
#try:
#    _nova
#except NameError:
_nova = None
if platform.system() == "Windows":
    _nova = ct.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                    "..", "..", "lib", "nova.dll"))
else:
    _nova = ct.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                    "..", "..", "lib", "nova.so"))


class NovaPOMDP(ct.Structure):
    """ The C struct POMDP object. """

    _fields_ = [("n", ct.c_uint),
                ("ns", ct.c_uint),
                ("m", ct.c_uint),
                ("z", ct.c_uint),
                ("r", ct.c_uint),
                ("rz", ct.c_uint),
                ("gamma", ct.c_float),
                ("horizon", ct.c_uint),
                ("S", ct.POINTER(ct.c_int)),
                ("T", ct.POINTER(ct.c_float)),
                ("O", ct.POINTER(ct.c_float)),
                ("R", ct.POINTER(ct.c_float)),
                ("Z", ct.POINTER(ct.c_int)),
                ("B", ct.POINTER(ct.c_float)),
                ("currentHorizon", ct.c_uint),
                ("Gamma", ct.POINTER(ct.c_float)),
                ("GammaPrime", ct.POINTER(ct.c_float)),
                ("pi", ct.POINTER(ct.c_uint)),
                ("d_S", ct.POINTER(ct.c_int)),
                ("d_T", ct.POINTER(ct.c_float)),
                ("d_O", ct.POINTER(ct.c_float)),
                ("d_R", ct.POINTER(ct.c_float)),
                ("d_Z", ct.POINTER(ct.c_int)),
                ("d_B", ct.POINTER(ct.c_float)),
                ("d_Gamma", ct.POINTER(ct.c_float)),
                ("d_GammaPrime", ct.POINTER(ct.c_float)),
                ("d_pi", ct.POINTER(ct.c_uint)),
                ("d_alphaBA", ct.POINTER(ct.c_float)),
                ]


_nova.pomdp_pbvi_complete_cpu.argtypes = (ct.POINTER(NovaPOMDP),
                                        ct.POINTER(ct.c_float), # Gamma
                                        ct.POINTER(ct.c_uint))  # pi

_nova.pomdp_pbvi_complete_gpu.argtypes = (ct.POINTER(NovaPOMDP),
                                        ct.c_uint,              # numThreadss
                                        ct.POINTER(ct.c_float), # Gamma
                                        ct.POINTER(ct.c_uint))  # pi

_nova.pomdp_pbvi_expand_random_cpu.argtypes = (ct.POINTER(NovaPOMDP),
                                                ct.c_uint,              # numDesiredBeliefPoints
                                                ct.POINTER(ct.c_uint),  # maxNonZeroValues
                                                ct.POINTER(ct.c_float)) # Bnew
