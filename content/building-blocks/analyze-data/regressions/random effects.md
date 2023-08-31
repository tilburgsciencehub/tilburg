---
title: "Fixed Effects Models: Random Effects Model"
description: "A building block about the Random Effects model"
keywords: "paneldata, panel, data, R, regression, model, random, fixed, pooled, OLS, within, between"
draft: false
weight: 14
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /randomeffects
  - /run/randomeffects/
  - /run/randomeffects
---

# Overview

The **Random Effects (RE) model** is the last method for panel data analysis discussed in this series of building blocks. Unlike the Fixed Effects (FE) model, which focuses on within-group variations, the RE model treats the unobserved entity-specific effects in the model as random and assumes they are uncorrelated with the explanatory variables. 

{{% summary %}}
Thus, the biggest difference between RE and FE is:
- In a FE model, the unobserved effects are assumed to be **correlated** with the independent variables
- In a RE model, the unobserved effects are assumed to be **uncorrelated** with the independent variables
{{% /summary %}}

## The Random Effects model

Let's continue with the model where we estimate the relationship of market and stock value on gross investment of firms, using `Grunfeld` data. This is the regression equation:
<br/>
{{<katex>}}
invest_{it} = \beta_0 + \beta_1 value_{it} + \beta_2 capital_{it} + \alpha_i + \epsilon_{it}
{{</katex>}}
<br/>
where,
- $invest_{it}$ is the gross investment of firm `i` in year `t`
- $value_{it}$ is the market value of assets of firm `i` in year `t`
- $capital_{it}$ is the stock value of plant and equipment of firm `i` in year `t`
- $\alpha_i$ is the fixed effect for firm `i`
- $\epsilon_{it}$ is the error term, which includes all other unobserved factors that affect investment but are not accounted for by the independent variables or the fixed effects.

The fixed effects $\alpha_i$ represent the time-invariant unobserved heterogeneity that differs across firms. This effect is assumed to be uncorrelated with the explanatory variables in the RE model. Consequently, the RE model also allows for the inclusion of time-invariant variables, such as a person's gender or education level, unlike the FE model.

### Error term in the RE model
The error term (capturing everything unobserved in the model) consists of two components: 

- The individual-specific error component: $\alpha_i$.
This term captures the unobserved heterogeneity that varies across individuals but remains constant over time. It is assumed to be uncorrelated with the explanatory variables.
- A time-varying error component: $\epsilon_{it}$.
This component captures the within-firm variation in gross investment over time. It accounts for the fluctuations and changes that occur within each firm over different time periods. Although this error term can be correlated within firms, it is uncorrelated across different firms. This term also exists in a FE model, where correlation of error across time is allowed as well.

### Estimation in R
To estimate the RE model in R, you can use the `plm()` function and specify the model type as `"random"`. 

{{% codeblock %}}
```R
# Load packages & data
library(plm)
library(AER) 
data(Grunfeld) 

# Model estimation
model_random <- plm(invest ~ value + capital,
                    data = Grunfeld,
                    index = c("firm", "year"),  
                    model = "random")

summary(model_random)

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summaryrandomeffects.png" width="700">
</p>

The estimated coefficients capture the average effect of the independent variable (X) on the dependent variable (Y) while accounting for both within-entity and between-entity effects. This means that the coefficients represent the average effect of X on Y when X changes within each entity (e.g., firm) over time and when X varies between different entities.

### Two-way Random Effects model

The RE model can be extended to a `twoway` model by including time-specific effects. These time-specific effects are also uobservable and assumed to be uncorrelated with the independent variables, just like the entity-specific effects. 

Include `effect = "twoways"` within the `plm()` function in R:


{{% codeblock %}}
```R
# Estimate two-way RE model 
model_random_twoway <- plm(invest ~ value + capital,
                    data = Grunfeld,
                    index = c("firm", "year"),  
                    model = "random",
                    effect = "twoway")
```
{{% /codeblock %}}

## Choice between Fixed or Random Effects
When deciding between the FE and RE model for panel data analysis, it is important to consider the correlation between the unobserved effects and the independent variables. If there is a correlation, the FE model is preferred as it controls for time-invariant heterogeneity. However, if the individual-specific effects are assumed to be uncorrelated with the independent variables, the RE model can be applied.

### Hausman test
To determine the appropriate model, a Hausman test can be conducted to test the endogeneity of the entity-specific effects. 
- The null hypothesis states no correlation between the independent variables and the entity-specific effects $\alpha_i$. If $H_{0}$ is true, the RE model is preferred.
- The alternative hypothesis states correlation between the independent variables and the entity-specific effects($\alpha_i$). If $H_{0}$ is rejected, the FE model is preferred.

The Hausman test can be performed in R with the `phtest()` function from the package `plm`. Specify the FE and RE model as arguments in this function. Note that the models includes as arguments shoudl be estimated with `plm`. Therefore, the Within model estimated is also estimated with `plm()` first (instead of with `feols()`from the `fixest` package like in the [Fixed Effects model building block](/withinestimator). 

{{% codeblock %}}
```R
# Estimate Two-way FE (Within) model
model_within_twoway <- plm(invest ~ value + capital, 
                    data = Grunfeld,
                    index = c("firm", "year"),
                    model = "within",
                    effect = "twoway") 

# Perform Hausman test
phtest(model_within_twoway, 
       model_random_twoway)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/hausmantest.png" width="700">
</p>

The p-value is 0.0013, which is lower than 0.05. Thus the $H_{0}$ is rejected and a FE model is preferred.

{{% summary %}}
The Random Effects (RE) model is a method for panel data analysis that treats unobserved entity-specific effects as random and assumes they are uncorrelated with the explanatory variables. Therefore, it also allows for the inclusion of time-invariant variables. 

When choosing between the FE and RE models, the correlation between the unobserved effects and independent variables should be considered. The Hausman test can be used to test for endogeneity of the entity-specific effects and help you decide in which model to choose. 
{{% /summary %}}