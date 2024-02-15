# Random Forest snow-to-liquid ratio method

## Introduction
This repository is the code associated with the [WAF](https://journals.ametsoc.org/view/journals/wefo/wefo-overview.xml) manuscript titled: "Validation of cool-season snowfall forecasts at a high-elevation site in Utah's Little Cottonwood Canyon" written by Pletcher, M. D., Veals, P. G., Wessler, M., Church, D., Harnos, K., Correia Jr., J., Chase, R. J., and W. James Steenburgh. *in review*. 

## Motivation

The accuracy of current operational SLR methods is largely unknown over the western U.S. and over complex terrain. In this study, we validate operational SLR methods and a newly developed random forest (RF) based SLR algorithm using high quality snowfall observations at a mountain site in Little Cottonwood Canyon, Utah. We find the RF-based SLR method produces more accurate SLR forecasts at this location, which can be used by forecasters and avalanche personnel. 

## Background on example dataset

We've provided the model (SingleSite_RF_slr_modelAGL30.pickle), the keys (SingleSite_slr_model_keysAGL30.npy), and a scaler (SingleSite_slr_model_scalerAGL30.npy)
