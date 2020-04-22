# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:52:38 2019

@author: HP
"""

import pickle    

# load it again
with open('filename.pkl', 'rb') as fid:
    gnb_loaded = pickle.load(fid)