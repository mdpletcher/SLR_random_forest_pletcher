'''
Description:
-----------
This script imports the sample dataset "sample_data.pd" and predicts SLR using the random forest model components.

The code that interpolates temperature and wind to AGL levels is not included in this script. Please contact 
Michael Pletcher (michael.pletcher@utah.edu) for more information.
'''

# Library imports
import numpy as np
import pandas as pd
import time

# Import sample data
data = pd.read_pickle('/path/to/sample_data.pd')

# Random forest function
def rf(_data):

    # Begin time counter
    tic = time.perf_counter()

    '''
    :param _data: file in .pd format that contains keys to predict
    SLR using the random forest.
    :return: 1-d array of predicted SLR values.
    '''

    # Load model components
    model  = np.load('/path/to/RF_SLR_model.pickle', allow_pickle = True)
    keys   = np.load('/path/to/RF_SLR_keys.npy', allow_pickle = True)
    scaler = np.load('/path/to/RF_SLR_scaler.npy', allow_pickle = True)[()]

    # Define empty column for predicted SLR
    _data['slr_rf'] = np.nan

    # Trim and normalize data
    data_trim = _data.loc[:, keys]
    data_norm = pd.DataFrame(scaler.transform(data_trim), 
        index = data_trim.index, columns = data_trim.keys()) # Normalize data based on scaler

    # Predict SLR
    _data['slr_rf'] = model.predict(data_norm)

    # Remove erroneous values (if necessary)
    _data['slr_rf'][_data['slr_rf'] > 50] = np.nan
    _data['slr_rf'][_data['slr_rf'] < 0]  = np.nan

    slr = _data['slr_rf']

    # End time counter
    toc = time.perf_counter()
    print(f"Random forest model runtime: {toc - tic:0.2f} sec")

    return slr