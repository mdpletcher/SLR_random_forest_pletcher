Dataset Name: sample_data.pd
Author: Michael D. Pletcher
Date Created: 15 February 2024
Email: michael.pletcher@utah.edu

Description:

This directory contains sample features that can be input into the random forest script
(predict_slr.py) in the scripts directory in this repository. The features were generated
using 10 days of HRRR BUFKIT forecasts (available at https://meteor.geol.iastate.edu/~ckarsten/bufkit/bufkit.html).
Each day contained 12 hours (12-24-h forecasts) of data that were obtained from the ALTA BUFKIT location. 
The five variables contained are:

1. Temperature interpolated to 0.5-km AGL Alta-Collins (T05K, in Kelvin)
2. Temperature interpolated to 1-km AGL Alta-Collins (T1K, Kelvin)
3. Temperature interpolated to 2-km AGL Alta-Collins (T2K, Kelvin)
4. Wind interpolated to 0.5-km AGL Alta-Collins (SPD05K, m/s)
5. Wind interpolated to 1-km AGL Alta-Collins (SPD1K, m/s)
6. Wind interpolated to 2-km AGL Alta-Collins (SPD2K, m/s)

