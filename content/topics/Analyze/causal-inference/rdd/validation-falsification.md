---
title: "Validation and Falsification Analysis for RDD"
description: "Validation and falsification analysis methods for the RD designs. Explanation of methods, how to implement them for both continuity and local randomization approaches, how to interpret results"
keywords: "regression, discontinuity, validation, falsification, analysis"
date: 2023-07-17
weight: 7
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /validation/analysis
  - /falsification/analysis
---

## Introduction

This topic provides a comprehensive overview of several tests used to verify the assumptions of the RDD design that ensure robustness of the analysis.

The Regression Discontuinity Design (RDD) assumes **no precise manipulation** at the cutoff. Precise manipulation happens if subjects know the cutoff and manipulate accordingly whether they end up below or above the cutoff, which determines whether they belong to the treatment or control group. As a result, treatment assignment is not as good as random anymore at the cutoff value of the running variable. An example of precise manipulation would be if in a targeted aid program for lower-income groups, some subject position themselves just below the cutoff of income level to qualify for this aid.

In this topic we discuss 6 validation methods, based on various empirical implications of the unobservable RD assumptions that are expected to hold in most cases. These methods are explored within both the standard [continuity-based approach](/continuity/approach) and the extended [local randomization approach](/local/randomization).

{{% tip %}}
**Falsification Test**

A falsification test serves to "falsify" (=prove something to be false) other discontinuities at the cutoff. By doing this test and proving there are no other discontinuities, we can be sure the observed effects are not the result of other factors and ensure the robustness of the RD Design.
{{% /tip %}}

### 1. Predetermined covariates and placebo outcomes

The first and most important falsification test examines whether units near the cutoff (in both treatment and control groups) are similar in terms of observable characteristics. For the validity of the RDD to hold, the units with scores just above and below the cutoff should be similar in the variables that could not have been affected by the treatment.

These variables include:

- **Predetermined covariates**: variables that are determined before the treatment is assigned
- **Placebo outcomes**: variables that are determined after the treatment is assigned and that could not have been affected by the treatment

The principle behind this test is that all predetermined covariates and placebo outcomes are analyzed in the same way as the outcome of interest. The null hypothesis is: the treatment effect is 0 for each predetermined covariate and placebo outcome.

If the p-value is lower than 0.05, the null hypothesis can be rejected and other discontinuities in covariates around found are found around the cutoff. This may imply that the discontinuity found in the outcome variable is not due to the treatment effect but a discontuinity in a confounder. Thus, for the validity of the RDD to hold, the p-value should be higher than 0.05 such that the H0 cannot be rejected.

#### The continuity-based approach

For each predetermined covariate or placebo outcome, an optimal bandwidth should be chosen first, and then the local polynomial estimation techniques within that bandwidth can be used to estimate the treatment effect. In the [continuity-based approach topic](/continuity/approach), this estimation method is explained in more detail.

Specifically, `rdrobust` function should be run using each covariate of interest as the outcome variable (`Y` in the code). The running variable is specified by `R` and bandwidth (`bw`) is set to 0.2 here. The kernel used is the triangular kernel.

{{% codeblock %}}

```R
# Continuity-Based Approach
out <- rdrobust(Y, R, bw = 0.2, kernel = "triangular")
summary(out)
```

{{% /codeblock %}}

If the resulting p-values are higher than 0.05, H0 cannot be rejected and there is no evidence of discontuinities in the variables.

#### The local randomization approach

In the local randomization approach, the analysis is conducted within the window where the assumption of randomization is assumed to hold. The `rdrandinf` function should be run using each covariate as outcome (specified by `Y`). `R` is the running variable and `wl` and `wr` represent the left and right bounds of the window. The `seed` parameter is used for setting the random seed.

{{% codeblock %}}

```R
# Local Randomization Approach
out <- rdrandinf(Y, R, wl = -2.5, wr = 2.5, seed = 50)
summary(out)
```

{{% /codeblock %}}

Again, if the p-values are above 0.05, it indicates that the variables are balanced inside the window, suggesting that no other discontinuities are found around the cutoff, thus reinforcing the validity of the RD design.

### 2. Density of the running variable

The test for the density of the running variable analyzes whether the number of observations slightly below the cutoff is significantly different from the number of observations slightly above it. If units don't have the ability to change the scores (and precisely manipulate themselves to a score below or above the cutoff), the number of treated observations above the cutoff should be similar to the number of control observations below it.

#### The continuity-based approach

For the continuity-based approach, the null hypothesis is that the density of the running variable is continuous at the cutoff. Thus, the test consists of a density estimation of observations near the cutoff using the `rddensity` function from the `rddensity` library, which only requires the running variable as argument (`R`).

{{% codeblock %}}

```R
# Continuity-Based Approach
out <- rddensity(R)
summary(out)
```

{{% /codeblock %}}

If the p-value is above 0.05, there is no significant difference in the density of the treated and control variables at the cutoff.

#### The local randomization approach

For the local randomization approach, the null hypothesis is that the number of treated and control observations is consistent with the assumed randomization assignment mechanism within the specified window. To test this we can use the `rdwinselect` function of the `rdlocrand` package. The running variable is specified with `R` and `X` is a matrix of the predetermined covariates considered to be independent of the assignment treatment.

Further arguments include:

- `seed` to specify the seed to be used for the randomization test
- `reps` to specify the number of replications
- `wobs` to specify the number of observations to be added at each side of the cutoff at each step
- `nwindows = 1` to specify we only use one window

{{% codeblock %}}

```R
# Local Randomization Approach
out <- rdwinselect(R, X, seed = 50, reps = 1000, wobs = 2, nwindows = 1)
summary(out)
```

{{% /codeblock %}}

Again, when the p-value is above 0.05, there is no evidence against the null hypothesis and the density of the running variable does not change significantly from below and above the cutoff.

### 3. Placebo cutoffs

This analysis studies the treatment effects at artificial or placebo cutoff values. This artificial value replaces the true cutoff and the test then performs estimation and inference using the artificial cutoff. To ensure the validity of the RD Design, no significant treatment effect should occur at the placebo cutoff values.

#### The continuity-based approach

For the continuity-based approach, this test is implemented using the local polynomial estimation by employing `rdrobust`. The artificial cutoff (`c`) is set to 2.5 here instead of the default which is `c = 0`.

{{% codeblock %}}

```R
# Continuity-Based Approach
out <- rdrobust(Y, X, c = 2.5, kernel = "triangular")
summary(out)
```

{{% /codeblock %}}

A p-value higher than 0.05 would show that the outcome of interest doesn't jump at the artificial cutoff. This ensures the validity of the RD Design, by indicating that the observed treatment effects are indeed the result of the treatment itself.

#### The local randomization approach

In the local randomization approach, this test is conducted using a randomization-based analysis of the outcome with a symmetric window, equal to the original window, that is used around each of the chosen artificial cutoffs. The necessary function is `rdrandinf`.

{{% codeblock %}}

```R
# Local Randomization Approach
out <- rdrandinf(Y, R, wl = -2.5, wr = 2.5, seed = 50)
summary(out)
```

{{% /codeblock %}}

### 4. Sensitivity of observations around the cutoff

This test investigates how sensitive the results are to the response of units located very close to the cutoff. If there is any manipulation of the score, the units closest to the cutoff are most likely to be involved in the manipulation. This sensitivity analysis is done by excluding these units and redoing the estimation using the remaining sample.

Simply use `rdrobust` for the [continuity-based approach](/continuity/approach) and `rdrandinf` in the context of the [local randomization approach](/local/randomization), but now on the reduced dataset.

{{% codeblock %}}

```R
# Continuity-Based Approach
out_reduced <- rdrobust(Y_reduced, R_reduced, bw = 0.2, kernel = "triangular")
summary(out_reduced)

# Local Randomization Approach
out_reduced <- rdrandinf(Y_reduced, R_reduced, wl = -2.5, wr = 2.5, seed = 50)
summary(out_reduced)
```

{{% /codeblock %}}

In both cases, the comparison of the results from the full dataset and the reduced dataset helps to evaluate whether leaving out the units closest to the cutoff changed the overall results of the analysis. With no precise manipulation, the new results remain largely unchanged compared to the original results using the entire sample of the data.

### 5. Sensitivity to Bandwidth Choice

This method analyzes how the results respond to changes in the bandwidth choice when units are added or removed at the end points of the neighborhood.

In the **continuity-based approach** this test is conducted by changing the bandwidth used for local polynomial estimation. Example code is given below. Adjust the bandwith values (`bw`) as necessary.

{{% codeblock %}}

```R
# Conducting sensitivity to bandwidth choice analysis
out_low <- rdrobust(Y, R, bw = 0.1, kernel = "triangular")
out_mid <- rdrobust(Y, R, bw = 0.2, kernel = "triangular")
out_high <- rdrobust(Y, R, bw = 0.3, kernel = "triangular")

# Compare the results
summary(out_low)
summary(out_mid)
summary(out_high)
```

{{% /codeblock %}}

A desirable outcome is to obtain broadly consistent results across various bandwidth choices, as this indicates the robustness of the findings.

{{% tip %}}
**The bandwidth choice: a trade-off between noise and bias**

An increase in the bandwidth leads to:

- An increased bias of the local polynomial estimator: data points that are more distant from the cutoff are included now.
- A lower variance ("noise") in the estimator: more observations are considered, so the treatment effect becomes less noisy.

For more details on bandwidth selection, see the [Continuity-based approach](/continuity/approach) topic.
{{% /tip %}}

### 6. Sensitivity to Window Choice

This test is the **local randomization approach** equivalent of the previous discussed Sensitivity to Bandwidth choice of the continuity-based approach.

Here, the sensitivity to the window choice is analyzed instead of the bandwidth choice. This analysis should only consider smaller windows than the original one, since a larger window would not lead to reliable results because the treated and control groups would be imbalanced in such windows.

To implement the test, you can use the `rdrandinf` function to specify a smaller window (`wl = -1.5` and `wr = 1.5` in this case) and analyze the results.

{{% codeblock %}}

```R
# Local Randomization Approach,
out_small_w <- rdrandinf(Y, R, wl = -1.5, wr = 1.5, seed = 50)
summary(out_small_w)
```

{{% /codeblock %}}

Given that the statistic test of this function is the difference in means, a p-value higher than 0.05 indicates that there is no significant difference in the results when a smaller window is implemented.

## Overview

This table gives an overview of all the tests for validation of the RDD discussed in this building block, including which function in R to use in the context of a continuity-based or local randomization approach.

{{%table%}}

| Test                                                       | Description                                                                  | Continuity-<BR> based <BR> Approach | Local <BR> Randomization <BR> Approach |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------- |
| 1. Predetermined <BR> covariates and <BR> placebo outcomes | Checks for <BR> similar observable <BR> characteristics <BR> near the cutoff | `rdrobust`                          | `rdrandinf`                            |
| 2. Density of <BR> Running Variable                        | Analyzes density <BR> differences near the <BR> cutoff                       | `rddensity`                         | `rdwinselect`                          |
| 3. Placebo cutoffs                                         | Tests for treatment <BR> effects at artificial <BR> cutoff values            | `rdrobust`                          | `rdrandinf`                            |
| 4. Sensitivity of <BR> observations around <BR> the cutoff | Investigates the effect <BR> of excluding units near <BR> the cutoff         | `rdrobust`                          | -                                      |
| 5. Sensitivity to <BR> Bandwidth Choice                    | Analyzes the impact <BR> of bandwidth changes <BR> on the results            | `rdrobust`                          | -                                      |
| 6. Sensitivity to <BR> Window Choice                       | Examines the effect of <BR> changes in window size <BR> on the results       | -                                   | `rdrandinf`                            |

{{%/table%}}

{{% summary %}}

In this topic we have discussed 6 validation methods, based on various empirical implications of the unobservable RD assumptions that are expected to hold in most cases. These methods were explored within both the standard [continuity-based approach](/continuity/approach) and the extended [local randomization approach](/local/randomization).

{{% /summary %}}

## See also

- [A Practical Introduction to Regression Discontinuity Designs: Foundations - Cattaneo, Idrobo & Titiunik (2020)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf)

- [A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2024_CUP.pdf)
