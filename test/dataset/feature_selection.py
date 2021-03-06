#!/usr/bin/env python
# vim: fdm=indent
'''
author:     Fabio Zanini
date:       07/08/17
content:    Test Dataset class.
'''
import numpy as np


# Script
if __name__ == '__main__':

    # NOTE: an env variable for the config file needs to be set when
    # calling this script
    from singlet.dataset import Dataset
    ds = Dataset(
            samplesheet='example_sheet_tsv',
            counts_table='example_table_tsv')

    print('Test feature selection by expression')
    res = ds.feature_selection.expressed(n_samples=1, exp_min=1)
    assert(res[0] == 'TSPAN6')
    print('Done!')

    print('Test feature selection by expression, in place')
    dsp = ds.copy()
    dsp.feature_selection.expressed(n_samples=1, exp_min=1, inplace=True)
    assert(dsp.featurenames[0] == 'TSPAN6')
    print('Done!')

    print('Test feature selection by overdispersed strata')
    res = ds.feature_selection.overdispersed_strata()
    assert(res[-1] == 'GLIPR2')
    print('Done!')

    print('Test feature selection by overdispersed strata, in place')
    dsp = ds.copy()
    dsp.feature_selection.overdispersed_strata(inplace=True)
    assert(dsp.featurenames[-1] == 'GLIPR2')
    print('Done!')
