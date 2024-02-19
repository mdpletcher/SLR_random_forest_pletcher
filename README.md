# Random Forest snow-to-liquid ratio method

## Introduction
This repository is the code associated with the [WAF](https://journals.ametsoc.org/view/journals/wefo/wefo-overview.xml) manuscript titled: "Validation of cool-season snowfall forecasts at a high-elevation site in Utah's Little Cottonwood Canyon" written by Pletcher, M. D., Veals, P. G., Wessler, M., Church, D., Harnos, K., Correia Jr., J., Chase, R. J., and W. James Steenburgh. *in review*. 

## Motivation

In this study, we developed a random forest based snow-to-liquid ratio (SLR) algorithm using high quality snowfall observations at a mountain site in Little Cottonwood Canyon, UT [(Wassserstein and Steenburgh (2023))](https://hive.utah.edu/concern/datasets/8s45q882q) and the ERA5 reanalysis [(Hersbach et al. (2018))](https://doi.org/10.24381/cds.bd0915c6).

## Background on example dataset

We've provided a sample dataset (sample_data.pd) that was built using [HRRR BUFKIT data](https://meteor.geol.iastate.edu/~ckarsten/bufkit/bufkit.html).

Instead of using the HRRR's native grids, we used BUFKIT files because of their smaller file size (~0.2 MB), increased vertical resolution, and hourly temporal resolution. 
The BUFKIT data was extracted from the Alta BUFKIT locaton.

## Notes
* The model was trained using 12-h snowfall and liquid precipitaton equivalent observations, but we typically apply it using 1-h predictor variables to produce high-frequency SLR and snowfall forecasts, although it can be applied at lower temporal frequencies.
* While this model can be used to predict SLR in any snow climate, it may produce skewed predictions when applied to regions with different snow climatologies (e.g., regions that experience winter storms that feature warm air aloft).

## Acknowledgments
* The research done to develop this model would not have been possible without Alta Ski Area and the hard work of Alta's ski patrol. We also acknowledge [scikit-learn](https://doi.org/10.48550/arXiv.1201.0490) and the availability of the ERA5 reanalysis for algorithm testing and development.

Questions? Email me at michael.pletcher@utah.edu
