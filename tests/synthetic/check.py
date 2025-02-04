#!/usr/bin/env python3

# Copyright (C) 2021-2023 Guillaume Jouvet <guillaume.jouvet@unil.ch>
# Published under the GNU GPL (Version 3), check at the LICENSE file 

import tensorflow as tf
import numpy as np

def params_check(parser):
    pass 

def initialize_check(params,state):
    pass    

def update_check(params,state):
    pass

def finalize_check(params, state):
    
    modules = [A for A in state.__dict__.keys() if 'tcomp_' in A]

    state.tcomp_all = [ np.sum([np.sum(getattr(state,m)) for m in modules]) ]
   
    vol = np.sum(state.thk) * (state.dx**2) / 10**9
    if (vol<11.5)&(vol>11.0):
       print(":-) test Passed in "+ str(int(state.tcomp_all[0]))+" sec (ref 11)")
    else:
       print(":-( test NOT PASSED")
       
    
