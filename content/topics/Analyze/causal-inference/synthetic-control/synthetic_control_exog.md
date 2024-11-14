---
title: "Synthetic Control Method without Exogenous Variables "
description: "This article illustrates how to perform causal inference with synthetic control methods without exogenous variables and an example implementation in R"
keywords: "causal, inference, econometrics, model, treatment, effect, control, synthetic, exogenous"
draft: false
weight: 1
author: "Virginia Mirabile"
---

## Overview 

In this article we will delve into the fundamental concepts, implementation steps, and applications of synthetic control methods without exogenous variables.

## Synthetic control method 

The synthetic control method is a statistical technique originally proposed by Abadie et al., (2010) used to evaluate the causal impact of an intervention or treatment. It is particularly valuable in observational studies where the goal is to estimate what would have happened to a treated unit (e.g., a region, country, or company) in the absence of the intervention. This method constructs a synthetic control by creating a weighted combination of untreated units that closely resembles the treated unit's characteristics before the intervention. The difference between the actual post-intervention outcome of the treated unit and the outcome of the synthetic control is attributed to the intervention's effect.

If you are new to this method, I suggest to check out [this](/topics/Analyze/causal-inference/synthetic-control/intro-synthetic-control/) article to first familiarize with the theoretical background and a traditional implementation in R. 

{{% tip %}}

Key Concepts:
- **Treated Unit**: The entity (e.g., a country, city, or firm) that receives the intervention.
- **Control Units**: A set of similar entities that did not receive the intervention.
- **Synthetic Control**: A weighted average of control units that approximates the treated unit's characteristics in the pre-intervention period.

{{% /tip %}}

In the **traditional** synthetic control method, the construction of the synthetic control typically involves matching the treated unit with control units based on both pre-intervention outcome variables and a set of exogenous predictors (such as demographic, economic, or geographic factors). These predictors help ensure that the synthetic control closely mirrors the treated unit, thereby providing a more accurate counterfactual scenario.

## Variant without exogenous variables 

A simplified variant of the synthetic control method has emerged in recent literature (Kim et al., 2020), particularly in fields like marketing, where the method is applied without the inclusion of exogenous variables. In this approach, the synthetic control is constructed solely on pre-intervention outcomes of each control unit as separate predictors, without incorporating additional covariates. For example, if we’re looking at sales, we only use past sales data of control units to find a match. This simplifies the model and is especially useful when reliable or relevant exogenous variables are unavailable or when their inclusion might introduce bias or noise.

The theoretical foundations advocating for this approach include greater predictive power of control unit outcomes (Doudchenko and Imbens, 2016) and concerns about overfitting (Powell, 2018). Additionally, Kaul et al. (2015) have shown, both theoretically and empirically, that using the outcomes of control units as predictors makes other covariates unnecessary. 

Key Features of the Variant:
- **Outcome-Driven Matching**: The matching process relies exclusively on the outcome variables observed before the intervention. For example, if the outcome of interest is sales, the synthetic control is created by matching on pre-intervention sales figures alone.
- **Simplicity**: By excluding exogenous variables, the model becomes more straightforward, focusing purely on replicating the treated unit’s outcome trajectory with a combination of control units.
- **Applicability**: This variant is particularly useful in contexts where the outcome itself is a robust predictor of future trends, or where including exogenous variables may not substantially improve the accuracy of the synthetic control.

Using synthetic control methods without exogenous variables offers a flexible and less data-intensive approach to causal inference. However, it also requires careful consideration of the pre-intervention period to ensure that the constructed synthetic control provides a valid counterfactual. While it might be less comprehensive than the traditional method, this approach has been successfully applied in recent studies, demonstrating its effectiveness in certain scenarios.

## Implementation in R 

The code snippets that follow will implement the variant without exogenous variables using two different R packages: `tidysynth` and `Synth`. 

### How to do this using `tidysynth`

The package we are going to be using in this section is called `tidysynth`, with functionalities specific for the implementation of this method.

The setting of the study focuses on California's Tobacco Control Program, which was implemented in 1988 as a comprehensive effort to reduce smoking through public education, policy changes, and increased taxation on tobacco products. For this example we will work with the `smoking` dataset. 

To familiarize with the data and the traditonal implementation visit [this article](/topics/Analyze/causal-inference/synthetic-control/intro-synthetic-control/). 

### Step 1: Installing the package and loading the dataset

{{% codeblock %}}
```R
install.packages('tidysynth')
library(tidysynth)
library(dplyr)
library(haven)
```
{{% /codeblock %}}

Let's load the dataset and get an overview of it's structure: 

{{% codeblock %}}
```R
data("smoking")
```
{{% /codeblock %}}

### Step 2: Initiate the synthetic control object

{{% codeblock %}}
```R
smoking_out <-
    smoking %>%
    # initiate the synthetic control object
    synthetic_control(outcome = cigsale, # outcome
                      unit = state, # unit index in the panel data
                      time = year, # time index in the panel data
                      i_unit = "California", # unit where the intervention occurred
                      i_time = 1988, # time period when the intervention occurred
                      generate_placebos=T # generate placebo synthetic controls (for inference)
    )
```
{{% /codeblock %}}

Up to this point, the steps to follow are the same in the **traditional** and **variant** methodologies. 

### Step 3: Generate `predictors` for the model

In this step, using the  `generate_predictor` function, we create the set of predictors for the model. Predictors are variables that describe each unit before the intervention, used to assess similarity between the treated and control units. The synthetic control method relies on these predictors to closely create a credible synthetic control. 

In this case, the only predictors we are going to use are the pre-intervention outcome variables `cigsale`, discarding other exogenous variables that characterize states before the intervention. 

Follow the code below: 

{{% codeblock %}}
```R
# Using Lags of dependent var to be predictors
smoking_out <- smoking_out %>%
  generate_predictor(time_window = 1975,
                       cigsale_1975 = cigsale) %>%
    generate_predictor(time_window = 1980,
                       cigsale_1980 = cigsale) %>%
    generate_predictor(time_window = 1988,
                       cigsale_1988 = cigsale)
```
{{% /codeblock %}}

### Step 4: Fitting the weights 

This step is specular to the traditional approach. 

{{% codeblock %}}
```R
# Generate the fitted weights for the synthetic control
smoking_out <- smoking_out %>%
    generate_weights(optimization_window = 1970:1988, # time to use in the optimization task
                     margin_ipop = .02,sigf_ipop = 7,bound_ipop = 6 # optimizer options
    )
```
{{% /codeblock %}}

### Step 5: Generate the synthetic control

Lastly, generate the synthetic control object: 

{{% codeblock %}}
```R
smoking_out <- smoking_out %>%
generate_control()
```
{{% /codeblock %}}

## How to do this in `Synth`

The `Synth` package was developed by Abadie et al., (2011) in order to implement synthetic control methods in R. 
The original version of the code used in this section can be found at [Abadie et al., (2011)](https://www.jstatsoft.org/article/view/v042i13). 

Our data example called `basque` is from Abadie and Gardeazabal (2003), which introduced synthetic control methods to investigate the effects of the terrorist conflict in the Basque Country on the Basque economy using other Spanish regions as potential control units.

The `basque` data contains information from 1955–1997 on 17 Spanish regions, including per-capita GDP
(the outcome variable), as well as population density, sectoral production, investment, and
human capital. This dataset is organized in standard panel-data format.

Here is an overview of the main variables: 

| **Variables** 	| **Description** 	|
|---	|---	|
| `regionname` 	| Name of the respective region|
| `year` 	| 1955–1997 |
| `gdpcap` 	| Averages for real GDP per capita measured in thousands of 1986 USD |
| `sec.agriculture` 	| Average for agricultural sector share as a percentage of total production|
| `popdens`	|  Population density measured in persons per square kilometer |      
| `invest`  	| Average for gross total investment/GDP |  
| `school.post.grad`  	|  Average for the share of the working-age population with more than high school diploma|  


In our case, we modify the original example to exclude exogenous variables of control units and only rely on `gdpcap` to build the synthetic control. 

### Step 1: Installing the package and loading the dataset

{{% codeblock %}}
```R
# Install the Synth package if you haven't already
install.packages("Synth")

# Load the required library
library(Synth)

# Load the dataset 
 data("basque")
```
{{% /codeblock %}}

### Step 2: Preparing data using `dataprep()`

The first step is to reorganize the panel dataset into an appropriate format that is suitable for the main estimator function `Synth`. The package provides a conevient function called `dataprep()` that we can run to organize our data. 
The authors recomend using `dataprep()` because it allows to conveniently extract and package all the necessary inputs for `Synth` in a single list object that can the be used further in the analysis with other functions as well. 

Follow the code below to implement this second step. 

{{% codeblock %}}
```R
dataprep.out <- dataprep(
  foo = basque,
  predictors = NULL, # No additional predictors
  time.predictors.prior = 1964:1969 , #set time period
  special.predictors = list(
    list("gdpcap", 1960:1969, "mean")  # Use only past outcomes (pre-intervention GDP per capita)
  ),
  dependent = "gdpcap",
  unit.variable = "regionno",
  unit.names.variable = "regionname",
  time.variable = "year",
  treatment.identifier = 17,  # Basque Country identifier 
  controls.identifier = c(2:16, 18),  # All other regions as controls
  time.optimize.ssr = 1960:1969,  # Pre-intervention period
  time.plot = 1955:1997  # Full time period for the plot
)
```
{{% /codeblock %}}

### Step 3: Running `Synth()`

The `Synth()` command solves the optimization problem by minimizing the difference between the pre-intervention characteristics for the treated unit and the pre-intervention characteristics for the untreated units (e.g. between treatment and control).

The "BFGS" below refers to the optimization algorithm used by the `Synth` package to estimate the weights for the control units in the synthetic control method, in our case we stick to the methodology used by the authors.

{{% codeblock %}}
```R
synth.out <- synth(data.prep.obj = dataprep.out,
                    method = "BFGS")
 ```                   
{{% /codeblock %}}

### What are the differences between `Synth` and `tidysynth`? 

When implementing the synthetic control method in R, you have the option to use two different packages. Both serve the same general purpose but they have different features, functionalities, and user experiences. Below, we'll explore some of the key differences between these two packages.

| **Tidysynth** 	| **Synth** 	|
|---	|---	|
| Offers a more intuitive workflow as it is built with the tidyverse ecosystem in mind. | Well-suited for who wants to follow the theoretical foundations and methodology proposed by Abadie et al. (2011). |
|  It automates several steps in the synthetic control process, which reduces the need for manual data preparation and makes it easier to customize the analysis. 	| Requires data preparation before the analysis, making the process more cumberstone and less user friendly. |
|  By leveraging on `ggplot2` and other `tidyverse` tools you can create clean, customizable plots with ease.	| Visualization is somewhat more basic and less integrated compared to tidysynth. |
 

## Summary 

{{% summary %}}

 - Using the synthetic control method without exogenous variables is less complicated than the traditional version and can be just as effective in many cases, though it’s important to carefully consider whether this simplified approach is appropriate for the specific situation you’re studying.

- Use `tidysynth` if you are looking for an intuitive and user friendly implementation in R and have little experience with synthetic control methods.  

- Use `Synth` for an approach that closely follows the literature on syntehtic control methods and requires manual specifications within the functions (e.g. data preparation, defining predictors). 

{{% /summary %}}

## References 

- Alberto Abadie, Alexis Diamond & Jens Hainmueller (2010) Synthetic
[Control Methods for Comparative Case Studies: Estimating the Effect of California’s Tobacco
Control Program](https://www.tandfonline.com/doi/abs/10.1198/jasa.2009.ap08746), Journal of the American Statistical Association, 105:490, 493-505, DOI:
10.1198/jasa.2009.ap08746

- Kim, Sungjin and Lee, Clarence and Gupta, Sachin, [Bayesian Synthetic Control Methods](https://ssrn.com/abstract=3382359) (June 2, 2020). Journal of Marketing Research (forthcoming).

- Doudchenko, N., & Imbens, G. W. (2016). [Balancing, regression, difference-in-differences and synthetic control methods: A synthesis.](https://www.nber.org/papers/w22791) National Bureau of Economic Research (NBER) Working Paper No. 22791.

- Powell, David, [Imperfect Synthetic Controls: Did the Massachusetts Health Care Reform Save Lives?](https://ssrn.com/abstract=3192710) (May 2018). 

- Kaul, Ashok & Klößner, Stefan & Pfeifer, Gregor & Schieler, Manuel, 2015. [Synthetic Control Methods: Never Use All Pre-Intervention Outcomes Together With Covariates](https://ideas.repec.org/p/pra/mprapa/83790.html) MPRA Paper 83790, University Library of Munich, Germany. 

- Abadie, A., Diamond, A., & Hainmueller, J. (2011). [Synth: An R Package for Synthetic Control Methods in Comparative Case Studies](https://doi.org/10.18637/jss.v042.i13). Journal of Statistical Software, 42(13), 1–17.

- Abadie A, Gardeazabal J (2003). [The Economic Costs of Conflict: A Case Study of the
Basque Country.](https://www.aeaweb.org/articles?id=10.1257/000282803321455188) American Economic Review, 93(1), 112–132 