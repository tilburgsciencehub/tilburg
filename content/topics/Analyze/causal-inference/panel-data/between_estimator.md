---
title: "The Between Estimator"
description: "A building block about the Between estimator"
keywords: "paneldata, panel, data, R, regression, model, random, fixed, pooled, OLS, within, between"
draft: false
weight: 6
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /betweenestimator
  - /between
  - /run/betweenestimator
---

# Overview

The **Between estimator** is a method used to estimate the relationship between variables by taking averages across time for each entity. It uses only the *between-group variation* in the data by averaging out the time component of panel data. With, this, the panel data effectively turns into a pooled cross-sectional data set. Consequently, important information about how variables change over time is ignored.

{{% tip %}}
__Practical application of between estimator__

The Between estimator is considered more of a technical concept than a model to use in practice. Think of it as a step between the Fixed Effects and Random Effects model.
{{% /tip %}}

## Estimation of the Between estimator 
The Between estimator is obtained by regressing the averaged variables on each other using OLS regression.

To obtain unbiased estimates, the error term should be uncorrelated with any of the averaged independent variables. And if the error term is assumed to be uncorrelated with the independent variables, the [Random Effects model](/randomeffects), discussed in the next building block, is generally more appropriate. 

Nonetheless, the Between estimator can be suitable for research questions that specifically address variation between different entities rather than changes within entities over time. 

## Estimation in R
To estimate the Between estimator in R, you can use the `plm()` function from the `plm` package. Specify the model type as "between". 

{{% codeblock %}}
```R
# Load packages & data
library(plm)
library(AER) 
data(Grunfeld) 

# Estimate Between model
model_between <- plm(inv ~ value + capital, 
                      data = Grunfeld,
                      index = c("firm", "year"),
                      model = "between")
```
{{% /codeblock %}}

{{% summary %}}
The Between estimator averages out the time component of panel data to estimate the relationship between variables. This approach effectively transforms the panel data into a pooled-cross sectional data set and thus overlooks important information about how variables change over time. 

To obtain unbiased estimates, it is crucial to ensure the assumption of zero correlation between the error term and averaged independent variables. 
{{% /summary %}}
