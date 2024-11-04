---
title: "Fixed Effects Regression Assumptions"
description: "A topic that covers the Fixed Effects Regression Assumptions"
keywords: "paneldata, panel, data, R, regression, model, assumptions, fixed, effects"
draft: false
weight: 5
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /fixedeffectsassumptions
  - /run/fixedeffectsassumptions/
  - /run/fixedeffectsassumptions
---

# Overview

This topic covers the fixed effects regression assumptions for Ordinary Least Squares (OLS) models. These 4 assumptions should hold in a Fixed Effects regression model to establish the unbiasedness of OLS.

To refresh your understanding of panel data and fixed effects, you can refer to the [panel data article](/paneldata). For a comprehensive explanation of fixed effects regressions in R, check the [`fixest` article](https://tilburgsciencehub.com/topics/analyze/causal-inference/panel-data/fixest/).

The assumptions are taken from the online course [Introduction to Econometrics with R](https://www.econometrics-with-r.org/10.5-tferaaseffer.html).

{{% summary %}}
In the fixed effects model
<br/>

$Y_{it} = \beta_1 X_{it} + \alpha_i + u_{it}, i = 1,...,n, t = 1,...,T,$

<br/>
we assume the following:

1. Zero conditional mean: $E(u_{it}|X_{i1},...,X_{iT}) = 0$.
2. Observations across entities are i.i.d. draws from their joint distribution.
3. Large outliers are unlikely.
4. There is no perfect collinearity.

When there are multiple regressors, $X_{it}$ is replaced by $X_{1,it}, X_{2,it},..., X_{k,it}$.
{{% /summary %}}

Now, the assumptions are explained in greater detail.

Examples are given to clarify the assumptions. This is done with the panel data set called `Grunfeld`, which is already used in the [panel data](/paneldata) and [`fixest` topic](https://tilburgsciencehub.com/topics/analyze/causal-inference/panel-data/fixest/). Please refer to these for further context on the `Grunfeld` data and the regression model.

## Assumption 1: Zero Conditional Mean

This assumption is also called **Strict Exogeneity**. The error term $u_{it}$ has an expected value of zero given any values of the independent variables. In other words, $E(u_{it}|X_{i1},...,X_{it}) = 0$.

It states that the error term $u_{it}$ is uncorrelated with each explanatory variable for all entities (each `i`) across all time periods (each `t`).

Violating this assumption introduces an **Omitted Variable Bias**.

{{% example %}}
This is the Fixed Effects model with `Grunfeld` data in which $\alpha_i$ denotes the firm fixed effects.

$invest_{it} = \beta_0 + \beta_1 value_{it} + \beta_2 capital_{it} + \alpha_i + \epsilon_{it}$

For assumption 1 to hold, the error term $\epsilon_{it}$ should be uncorrelated with each observation of the independent variables. This implies that all factors impacting `invest` that are not included in the model are uncorrelated with all the observations of `value` and `capital` over time.
{{% /example %}}

## Assumption 2: Observations across entities are i.d.d. draws from their joint distribution

$(X_{i1}, X_{i2},...,X_{it}, u_{i1},...,u_{it})$, $i = 1,...,n$ are independent and identically distributed (i.i.d.) draws from their joint distribution.

This assumption is justified when entities are selected through simple random sampling, where each entity in the population has an equal chance of being included in the sample. This ensures that the observed data is representative of the entire population, and an OLS estimation can make valid inferences about the population based on the sample data.

It is important to note that this assumption is just about independence _across entities_. It does allow for observations to be correlated _within entities_, meaning that there can be autocorrelation within entities (firms) over time. This autocorrelation within an entity (over time) is commonly observed in time series and panel data. Similarly, the errors $u_{it}$ are allowed to be correlated over time.

{{% example %}}
In the context of the `Grunfeld` data set, this assumption implies the following:

- In the Fixed Effects model, we assume that the variables `value` and `capital` are independent across different firms. The firm `value` of U.S. Steel for example is assumed to be independent of the firm `value` of General Motors.
- Within each firm, there can still be autocorrelation over time. For instance, the firm `value` of U.S. Steel in one year may be dependent on its `value` in the previous year.
  {{% /example %}}

## Assumption 3: Large outliers are unlikely

This assumption tells that $(X_{it}, u_{it})$ have nonzero finite fourth moments. In other words, the observations and error term have finite distributions.

Large outliers are extreme observations deviating considerably from the usual range of the data. In OLS, each observation is given equal weighting. Therefore, large outliers receive a relatively heavy weighting in the estimation of unknown regression coefficients. This can distort the estimates and lead to biased results.

By assuming the absence of large outliers, we expect that the observations will generally fall within a reasonable range and not have extreme values that would significantly affect the estimation of the regression coefficients. This assumption helps ensure the OLS estimates are unbiased.

## Assumption 4: No perfect collinearity

Assumption 4 holds when there are no exact linear relationships among the independent variables. Perfect collinearity between two or more independent variables means that one variable can be written as a linear combination of the other(s). For example, one variable is a constant multiple of another. In the presence of perfect collinearity, the model cannot be estimated by OLS.

Note that the assumption does allow the independent variables to be correlated. They just cannot be perfectly correlated.

{{% summary %}}
The Fixed Effects (FE) regression model relies on 4 key assumptions. These assumptions form the foundation for various models that account for different forms of error correlation over time.

In the following topics, we will explore these models that are commonly used to analyze panel data:

- [Pooled OLS](/pooledOLS)
- [First-difference estimator](/firstdifference)
- [Within estimator (Fixed effects)](/withinestimator)
- [Between estimator](/betweenestimator)
- [Random effects](/randomeffects)

{{% /summary %}}
