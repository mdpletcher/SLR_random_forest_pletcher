# Random Forest snow-to-liquid ratio method

## Introduction
This repository is the code associated with the [WAF](https://journals.ametsoc.org/view/journals/wefo/wefo-overview.xml) manuscript titled: "Validation of cool-season snowfall forecasts at a high-elevation site in Utah's Little Cottonwood Canyon" written by Pletcher, M. D., Veals, P. G., Wessler, M., Church, D., Harnos, K., Correia Jr., J., Chase, R. J., and W. James Steenburgh. *in review*. 

## Motivation

The accuracy of current operational SLR methods is largely unknown over the western U.S. and over complex terrain. In this study, we validate operational SLR methods and a newly developed random forest (RF) based SLR algorithm using high quality snowfall observations at a mountain site in Little Cottonwood Canyon, Utah. We find the RF-based SLR method produces more accurate SLR forecasts at this location, which can be used by forecasters and snow-safety personnel. 

## Background on example dataset

We've provided a sample dataset (sample_data.pd) that was built using [HRRR BUFKIT data](https://meteor.geol.iastate.edu/~ckarsten/bufkit/bufkit.html)

Instead of using the HRRR's native grids, we used BUFKIT files because of their smaller file size (~0.2 MB), increased vertical resolution, and hourly temporal resolution. 
The BUFKIT data was extracted from the Alta BUFKIT locaton.

## Notes
* Because the model was trained on 12-h snowfall observations, we recommend using 1-h predictor variables integrated over 12-h time periods or 12-h mean predictor variables as features for this model.
* While this model can be used to predict SLR in any snow climate, it may produce skewed predictions when applied to regions with different snow climatologies (i.e., regions that experience winter storms that feature warm air aloft). CLN is a very cold site and its predictions take that into account.

Questions? Email me at michael.pletcher@utah.edu
