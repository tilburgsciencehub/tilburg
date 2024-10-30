---
title: "Local Randomization Approach"
description: "The local randomization approach to regression discontinuity analysis: an introduction, example, estimation and inference"
keywords: "regression, discontinuity, local, randomization, approach, example, estimation, inference"
date: 2023-07-10
weight: 6
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /regression/discontinuity
  - /local/randomization
  - /estimation/inference
---

## Introduction

This topic introduces the local randomization approach, which can be considered as an extension to the standard [Continuity-Based Approach to RD Analysis](/continuity/approach). It is recommended to read this continuity-based approach topic before delving into this one.

In a sharp RDD, the assignment mechanism is determined by the running variable being above or below a prespecified cutoff. The local randomized approach views the running variable as random, allowing to interpret the RDD as a randomized experiment near the cutoff.

The local randomization approach imposes certain conditions, ensuring that units who are in a small window around the cutoff are comparable and treated as if they were randomly assigned to treatment and control. The next section discusses these conditions in detail. After that, estimation and inference methods for are discussed followed by a practical example.

{{% tip %}}
_Choice of approach depending on variable type_

Depending on the nature of the running variable, one can choose whether to use the continuity-based approach or the local randomization approach.

If the variable is discrete, the local randomization approach does not impose strong assumptions and can be used for estimation and inference. However, if the variable is continuous, the local randomization requires stronger assumptions than the continuity-based approach Here, the continuity-based approach is preferred for main RD analysis and the local randomization as a robustness check.
{{% /tip %}}

## The assumptions

As mentioned in the introduction, certain conditions are imposed to make sure that units in a small window are treated as if they were randomly assigned to treatment. We make the following assumptions:

- The RDD is sharp, indicating an abrupt change in treatment assignment around the cutoff. Check the [Sharp RDD topic](//sharp/designs) for more context on this.

- There is perfect compliance. Each subject assigned to the treatment actually received the treatment.

- The _As if random assignment_ assumption. This means within the window $W = [c-w, c+w]$ around the cutoff value $c$, unit placement into treatment or control is as if it would have been assigned in a random experiment. Due to this assumption, the running variable is unrelated to the average potential outcomes of these units within the defined window.

### Graphical comparison: Randomized experiment and a continuity-based design

<p align = "center">
<img src = "../images/local-rand.png" width="500">
</p>

The above graphs compare a randomized experiment (left graph) with a continuity-based design (right graph). They illustrate the fundamental differences between a randomized experiment (what we assume to happen within the window in this approach) and a standard continuity-based design.

In the left graph, the randomized experiment implies that the treatment assignment is completely random, leading to constant values of $\mu_{1}(x) = \mathbb{E}[Y_{i}(1)|X_{i}=x]$ and $\mu_{0}(x) = \mathbb{E}[Y_{i}(0)|X_{i}=x]$ for all values of $x$ values within the specified range. This randomness ensures that the potential outcomes remain unaffected by the values of the running variable.

This emphasizes that for allowing to interpret the RD design as a randomized experiment, the value of the score (the running variable) within the defined window needs to be unrelated to the potential outcomes.

{{% summary %}}
The local randomization approach needs to fullfill two conditions:

- The joint probability distribution of scores within the window $W$ is known.
- The potential outcomes are not affected by the score within window $W$.
  {{% /summary %}}

### Notations

To clarify the conditions of the local randomization approach discussed above, these are its notations:

- Condition 1

The probability is defined as $\mathbb{P_W}[.]$ for those units with $X_{i}\in W$.
As such, the first condition requires that $\mathbb{P_W}[X_{W} \leq x]=F(x)$ for some known joint cumulative distribution function $F(x)$.

- Condition 2

Let $Y_{i}(0,x)$ and $Y_{i}(1,x)$ be the potential outcomes with explicit dependence on the score variable, so that $Y_{i}(0) = Y_{i}(0, X_{i})$ and $Y_{i}(1) = Y_{i}(1, X_{i})$. As such, if the potential outcomes are non-random, the second condition means that $Y_{i}(0,x') = Y_{i}(0, X_{i})$ and $Y_{i}(1,x') = Y_{i}(1, X_{i})$ for all $x$, $x' \in W$ and all units such that $X_{i} \in W$. If the potential outcomes are non-random, the condition becomes $\mathbb{P_W}[Y_{i}(0,x') = Y_{i}(0,x)]=1$ and $\mathbb{P_W}[Y_{i}(1,x') = Y_{i}(1,x)]$ = 1 for all $x$, $x' \in W$.

## Estimation and Inference

### Small sample: Fisherian Inference

Since in many RD cases a local randomization assumption is only plausible in a very small window around the cutoff, it means that this window will most likely contain few observations. For this case, a Fisherian inference approach is appropriate, as it is valid in any finite sample and leads to correct inferences even with small samples.

With the Fisherian approach, the potential outcomes are fixed or non-stochastic (i.e. they are not subject to random variation). The null hypothesis, also called the _sharp null hypothesis_ is:
$H^F_{0}: Y_{i}(0) = Y_{i}(1)$ for all $i$.

The sharp null hypothesis with the non-stochastic potential outcomes lead to inferences that are (type I error) correct for any sample size, since under $H^F_{0}$ the observed outcome of each unit is equal to the unit's potential outcomes ($Y_{i} = Y_{i}(1) = Y_{i}(0)$) and there is no missing data.

### Large sample: Neyman and Super-population methods

Although the window around the cutoff is small, some RD applications can have many observations in these windows. The Fisherian inference method would still work well and be valid, but there are some large sample methods that provide consistent point estimators. Both the Neyman and Super-population are large sample methods, and they require that the number of observations within the window are large enough.

#### Neyman method

In the Neyman method, the potential outcomes are non-stochastic and not not subject to random fluctuations.
Therefore, when applying the Neyman method for estimation and inference, all parameters are conditional on these fixed potential outcomes. The "urn model" of treatment assignment entails that there is one urn per treatment condition and each urn has the potential outcomes that correspond to that treatment condition for each unit.

In a Neyman framework, the average treatment effect is :
$$\theta_{SRD} = \frac{1}{N_{W}} \sum_{i:X_{i} \in W} [Y_{i}(1) - Y_{i}(0)]$$

Note that $\theta_{SRD}$ is different from the continuity-based parameter $\tau_{SRD}$, because the former is an average effect inside the window, while the latter is an average at the cutoff point.

#### Super-population method

In the Super-population method, units are assumed to be drawn from a larger population using independently and identically distributed sampling (i.i.d.). This results in the potential outcomes being random variables, not fixed quantities.

In the Super-population framework, the average treatment effect is:
$$\theta_{SRD} = \mathbb{E}[Y_{i}(1) - Y_{i}(0)|X_{i} \in W]$$

### Summary of statistical methods

The table below provides an overview of the statistical methods discussed in this section.

{{%table%}}

|                    | Fisher     | Neyman      | Super-population |
| ------------------ | ---------- | ----------- | ---------------- |
| Sampling           | None       | Urn model   | i.i.d.           |
| Potential Outcomes | Non-random | Non-random  | Random           |
| Sample size        | Fixed      | Large       | Large            |
| Null hypothesis    | Sharp      | Non-sharp   | Non-sharp        |
| Inferences         | Exact      | Approximate | Approximate      |

{{%/table%}}

For all three methods, the parameter of interest is $\mathbb{E_W}[.]$, denoting the expectation computed with respect to the probability $\mathbb{P_W}$.

## Practical Example: US Senate Elections

To demonstrate the Local Randomization Approach, we analyze the effect of winning elections on future vote shares in the context of US Senate Elections.

There is a discontinuous relationship between the incumbency status of a political party and the vote share obtained in an election. This means that when there are two parties that compete for a seat, the party with just above 50% of the vote wins and becomes the incumbent, while the other loses.

Here, the unit of analysis is the US state and the score is the Democratic party's margin of victory at election $t$. This is calculated as the difference between the vote share of the Democratic party and the vote share of its strongest opponent.

The variables are defined as follows:

- $Y$ - vote share obtained by the Democratic party in the election in a given state
- $X$ - margin of victory of the Democratic party. This is the running variable.
- $T$ - electoral victory of the Democratic party, being equal to 1 if they won and 0 otherwise

### Estimation in R

The R library for local randomization is `rdlocrand`, from which we use the function `rdrandinf`. The main parameters of the function are the outcome variable $Y$, the running variable $X$ and the bounds of the window: `wr` (right bound), `wl` (left bound). For now we set them to -2.5 and 2.5.

{{% codeblock %}}

```R
out <- rdrandinf(Y, X, wl = -2.5, wr = 2.5, seed = 50)
summary(out)
```

{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../images/output1.png" width="400">
</p>

The output shows that there are 1297 observations in total, with a default polynomial order of 0 and a uniform kernel. It also shows that there are 1000 simulations used, the null hypothesis tested (by default $\tau_{0} = 0$) and the randomization mechanism is by default fixed margins randomization.

The middle part of the output shows the distribution of the observations left and right of the cutoff. There are 595 control and 702 treated observations, but in the chosen window there are only 63 elections below the cutoff and 57 above.

The mean difference of 9.167 is the difference between the mean of outcome above cutoff and the mean of outcome below the cutoff. It shows the difference of Democratic vote shares in election where the party wins (53.235%) and the Democratic vote shares in elections where the party loses (44.068%). It highlights the importance of a cutoff value of 50% on the election outcome.

The p-value shows that we can reject the null hypothesis, suggesting a significant impact of the incumbency status on future vote shares.

{{% tip %}}
Kernel type can be changed using the `kernel` argument and number of simulations can be changed using the `reps` argument.
{{% /tip %}}

### Choice of window

Manually choosing the window around the cutoff lacks transparency and objectivity. The `rdlocrand` library contains the function `rdwinselect` which selects a window. It takes as argument the score variable $X$ and a matrix of predetermined covariates. We can also set the number of simulations to 1000 by using `reps`. Additionally, one can use `wstep` to increase the length of the windows in fixed steps, or `wobs` to increase the window length so that the observations number increases by a minimum fixed amount every step. `wobs` = 2 means that at least 2 observations are added on each side of the cutoff in every step.

{{% codeblock %}}

```R
out <- rdwinselect(X, Z, seed = 50, reps = 1000, wobs = 2)
summary(out)
```

{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../images/output2.png" width="400">
</p>

The output shows that the optimum window is [-0.7652, 0.7652].
The function only shows the first 20 windows, but we can increase it by using the argument `nwindows`.

{{% summary %}}
The Local randomization approach extends the standard continuity-based RD Design by treating the running variable as if it were randomized within a defined window around the cutoff. Three methods are discussed for estimation and inference, each suitable depending on the size of the sample within this window.

The next [topic](/validation/analysis) in this series about Regression Discontuinity describes several tests that can be used to validate the robustness of your RDD.
{{% /summary %}}

## See also

[A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2024_CUP.pdf)
