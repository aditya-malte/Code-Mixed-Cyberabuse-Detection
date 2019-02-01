# -*- coding: utf-8 -*-
"""
Task:
    Transliterate if word not present in english dictionary
"""

import pandas as pd

hi_train = pd.read_csv("hindi/agr_hi_train.csv", header=None)