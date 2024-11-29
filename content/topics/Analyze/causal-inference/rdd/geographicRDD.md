---
title: "Geographic Regression Discontinuity (GRD) Design"

description: "Identifying treatment effects with geographic boundaries as discontinuities"
keywords: "RDD, causal, inference, regression, R, causal inference, effect, discontinuity, running variable, GRD, SRD, spatial, geographic, manipulation, treatment, identification"
draft: false
weight: 10
author: "Victor Arutyunov"
aliases:
  - /grd
  - /srd
  - /geographic-rdd
  - /spatial-rdd
---

## Overview 

Regression discontinuity designs (RDDs) are a commonly used quasi-experimental framework in economics, political science, public health and many other fields. RDDs are suitable in settings where treatment status depends on the value of some running (or ‘assignment’) variable. In a [sharp RD design](/sharp/designs), a unit is treated above a certain cutoff (or ‘threshold’) of the running variable, while below it is not, or vice-versa. Sometimes, this cutoff can be an actual geographic boundary, such as a border between countries or regions, to one side of which treatment occurs, while to the other it does not. 

{{% example %}}
Examples of settings where treatment status is determined by a geographic cutoff are almost countless. Think of neighbouring countries with different mandatory schooling years, adjacent states with different minimum wage levels, or a natural boundary like a mountain range that creates variation in climatic conditions between two contiguous areas. 
{{% /example %}}

RDDs where the cutoff is a geographic boundary are known as geographic regression discontinuity (GRD) or spatial regression discontinuity (SRD) designs. In this topic, we discuss how GRD differs from canonical RDD, what kind of identification challenges this implies, and how these can be addressed to successfully identify a causal effect in GRD settings. 

## Differences between GRD and canonical RD designs

GRD designs are in essence similar to RDDs. We choose a limited bandwidth of the running variable around the cutoff, fit a local polynomial on either side, and estimate the discontinuity (the difference in the intercepts of the two polynomials at the cutoff) in the outcome variable at the cutoff. Nonetheless, the geographic context does have numerous peculiarities which must be taken into account when identifying a treatment effect. 

### Two running variables

A key difference between standard RD and GRD designs is that geographical location, unlike other commonly used running variables, such as income or age, cannot be measured in one dimension. Instead, we use longitude and latitude to define spatial positions. As such, in a GRD setting we actually have **two** running variables! This means that our cutoff, and the treatment status determined by it, is multidimensional – it depends on the combination of the longitude and latitude of a unit’s location. Consequently, the standard continuity assumption that is central to canonical RD designs is extended: we assume that the conditional expectation functions (CEFs) relating the running variable to the outcome are continuous in the running variable at _all_ cutoff points. 

{{% tip %}}
It is possible to estimate the treatment effect with a single running variable in a GRD setting, using a technique known as ‘naïve distance’, which we consider below. However, this method may fail to capture some of the intricacies of a spatial setting, which is why the ‘complete’ GRD with two running variables is generally preferred. 
{{% /tip %}}

{{% example %}}
For instance, if a treatment is applied above the latitude of 50 and below the longitude of 30, a unit that has latitude 55 and longitude 35 is not treated, even though it is above the first treatment cutoff. Only units with latitude > 50 **and** longitude < 30 should be in the treatment group.
{{% /example %}} 

### Stronger continuity assumptions

The fundamental identifying assumption in a conventional [continuity-based](/continuity/approach) RD designs is that nothing varies _discontinuously_ at the cutoff except treatment exposure. [Local randomisation-based](/local/randomization) designs likewise require that the groups on either side of the cutoff are sufficiently similar in terms of their observable and unobservable characteristics. In a GRD context, these assumptions may be much stronger than in conventional RD settings. 

For example, if the cutoff determining treatment status is a country border, the units on either side of the cutoff may fundamentally differ in terms of language, ethnicity, cultural and social norms, religion, age, and many other demographic characteristics. This is especially the case where the geographic boundary is natural or long-standing. In these settings, it is difficult for us to argue that units on either side are fundamentally comparable or that potential confounders change continuously and smoothly across the border. 

{{% example %}}
Suppose we are using the border between Bulgaria and Turkey as our cutoff. The median age in Bulgaria is 45.1, while in Turkey it is just 34. On the Bulgarian side of the border, just about 10% of the population is Muslim, while on the Turkish side, around 90% is. Age and religion therefore do not change _continuously_ at the cutoff: if these characteristics strongly affect our outcome of interest, this invalidates the crucial continuity assumption.
{{% /example %}}

### Compound treatments

When geographic cutoffs overlap with administrative borders, it is also highly likely that they serve as cutoffs for multiple treatments simultaneously. Administrative borders separate jurisdictions, and different jurisdictions are likely to implement different policies or laws on their territory at the same time. This can make it difficult to isolate the effect of the specific treatment that we want to study. 

{{% example %}}
Suppose we are studying the effects of a minimum wage change on employment in the Netherlands, and we want to compare Dutch municipalities on the border with Belgium with neighbouring Belgian municipalities, where the minimum wage remained unaltered. However, when changing the minimum wage, the Dutch government also adopted other labour market reforms, such as a reduction in layoff costs, which are also expected to affect employment. Multiple treatments vary at the same cutoff (the Dutch-Belgian border), so we would struggle to identify the effect of minimum wages specifically. 
{{% /example %}}

### Location-specific treatment effects

Regression discontinuity estimates yield _local_ average treatment effects (LATE). In a conventional RD design, this means that we find effects that are valid _at the cutoff_. In a geographic setting, however, the cutoff does not have a single value. Rather, the cutoff consists of _many_ individual points that together form a boundary. The local effects we estimate in a GRD context are therefore local to each individual boundary point, so we have as many treatment effect estimates as we have boundary points. It is possible to aggregate these location-specific effects into an average effect for the entire cutoff, but often we are interested in studying the potential spatial heterogeneity in treatment effects across different positions on the boundary. 

{{% example %}}
Suppose we are using a standard RDD, our running variable is income and our cutoff is 1000. The treatment effect that we estimate will be valid locally at this cutoff; that is, for people who earn an income of just around 1000. In a GRD design, we cannot define a single value that represents the entire boundary between the treated and control areas, so we estimate separate local effects for each identifiable point on the boundary. 
{{% /example %}}

{{% tip %}}
Of course, a cutoff is technically a continuum of an infinite number of boundary points. For the purpose of estimating LATEs in a GRD setting, however, we select a subset of this continuum to serve as our boundary points. We can determine the size of this subset ourselves, but it is generally better to include more points so as to more accurately reflect the complexity of the actual boundary. 
{{% /tip %}}

## Identification in GRD

In a sharp GRD design, treatment status is a deterministic and discontinuous function of geographic location. The general regression equation is akin to a standard RD estimation equation:

{{<katex>}}
{{</katex>}}

$$Y_i = \alpha + \beta T_i + \gamma f(geographic location_i) + \delta T*f(geographic location_i) + \epsilon_i$$

Where Y is the outcome, T is the treatment dummy, $f(geographic location)$ is a function relating geographic location to the outcome, and $\epsilon$ is the error term. $\beta$ is the coefficient of interest. 

The fundamental challenge is to accurately define the polynomial describing the relationship between the running variable and the outcome ( $f(geographic location)$ ), as geographic location is captured by two variables – the longitude and the latitude. We discuss two ways of approaching this below. 

### Naïve distance estimation

The first approach is to ‘force’ the two-dimensional running variable into a one-dimensional one, approximating a conventional, single-running variable RD design. We do so by collapsing longitude and latitude into a single running variable: distance to the cutoff. This method is known as ‘naïve distance’ and relies on measuring the Euclidean distance between each observation and the point on the boundary (cutoff) nearest to it. The (linear) regression equation then becomes:

{{<katex>}}
{{</katex>}}

$$Y_i = \alpha + \beta T_i + \gamma DistanceToBoundary_i + \delta T_i*DistanceToBoundary_i + \epsilon_i$$

Where Y is the outcome, T is the treatment dummy, $DistanceToBoundary$ is the Euclidean distance between the observation $i$ and the nearest boundary point, and $\epsilon$ is the error term. $\beta$ is the coefficient of interest. 

{{% tip %}}
Euclidean distance is simply the formal term for the length of the straight line segment between any two points. 
{{% /tip %}}

Naïve distance is a very intuitive way of defining the RD polynomial, but estimation based on naïve distance may be subject to two considerable flaws:

1.	**Bad comparisons**: Merging longitude and latitude into a single distance variable means that we ignore an observation's exact geographic position. Instead, we only consider its position _relative to the boundary_. This is problematic because it implies that observations equally distant from the boundary but located in entirely different locations will be compared to each other. The image below illustrates this: points i and j will have the same value of the running variable, as they are equidistant from their respective nearest boundary points and will thus be compared to the treated observation k in the same manner; however, they clearly have very different geographical positions relative to k and to each individual boundary point. 

<p align = "center">
<img src = "../images/GRD_naive.png" width="400">
</p>

These comparisons are problematic if geographic location itself affects our outcome or strongly correlates with unobservable covariates that do so. If we compare such disparate units, our treatment effect estimator could be picking up geographic position effects, instead of the true treatment effect. 

2.	**Disregards spatial heterogeneity**: As discussed above, there is a continuum of treatment effects in a GRD setting, with a separate LATE for each point on the boundary. Naturally, converting latitude and longitude into a one-dimensional distance variable disregards the complex spatial nature of the boundary – it becomes a single value (0, as distance to the boundary at the boundary is zero). This means that we only estimate the treatment effect at zero distance to the boundary: in practice, this amounts to an average of the LATEs at each boundary point. 

{{% warning %}}
The first flaw can be remedied by including border segment fixed effects in the model. This involves splitting the border into multiple segments, within which we expect the outcomes to be spatially dependent, i.e., influenced by their geographic position. However, segment fixed effects only aid us in making better comparisons if we select the segments accurately – that is, the observations within each segment on either side of the boundary are indeed influenced in a uniform manner by their geographic location. Moreover, they do not help us in addressing the second problem of ignoring spatial treatment effect heterogeneity. This issue can only be solved by conducting a geographic estimation of the GRD, as explained below. 
{{% /warning %}}

### Geographic estimation

By geographic estimation we refer to the use of the two original geographic variables, latitude and longitude, to define the RD polynomial. In other words, we compute the GRD with two running variables. Doing so allows us to fully exploit the spatial nature of our setting, where we can calculate the local average treatment effect at _each_ boundary point, as opposed to just one average for the entire cutoff, and ensure that the comparisons we make are reasonable. 

{{% tip %}}
The practical method for computing LATEs at each boundary point will be described in the Geographic Regression Discontinuity topic. 
{{% /tip %}}

The most common geographic estimation procedure, described by [Keele and Titiunik (2015)](https://www.cambridge.org/core/journals/political-analysis/article/geographic-boundaries-as-regression-discontinuities/2A59F3077F49AD2B908B531F6E458430), works in the following way:

1.	Calculate the Euclidean distance from each point on either side (both in the treated and control areas) to _each_ boundary point. 

2.	Estimate the discontinuity at _each_ boundary point with the distance to that boundary point as the running variable. This gives us a treatment effect $\tau_b$ for every point $b$ on the boundary. The (linear) regression equation, at the boundary point $b$, will look like this:

{{<katex>}}
{{</katex>}}

$$Y_i = \alpha_b + \tau_b T_i + \gamma_b DistanceToBoundary_{ib} + \delta_b T_i*DistanceToBoundary_{ib} + \epsilon_{ib}$$

Where Y is the outcome, T is the treatment dummy, $DistanceToBoundary$ is the Euclidean distance between the observation $i$ and boundary point $b$, and $\epsilon$ is the error term. $\tau_b$ is the coefficient of interest. 

{{% tip %}}
The software package used for GRD analysis in R and State, `SpatialRDD`, also automatically calculates the _average_ treatment effect for the _entire_ boundary. 
{{% /tip %}} 

{{% tip %}}
There are also ways of estimating treatment effects where treatment exposure is determined by a geographic discontinuity without using regression discontinuity methods. One such approach is spatial nearest-neighbour [matching](/exact-matching), where we compare each observation to its geographically closest ‘neighbour’, regressing their differences in outcomes on their differences in treatment status. Another approach is to use spatial fixed effects (or spatial demeaning), which in effect is a hybrid combination of matching with standard RDD. We do not discuss these methods in detail in this topic, but further information on them can be found [here](https://blogs.worldbank.org/en/impactevaluations/spatial-jumps). 
{{% /tip %}} 

## Challenges to identification in GRD designs and solutions

### Sorting and manipulation

Geographic location, and more precisely latitude and longitude, are running variables that are comparatively easy to manipulate for individuals and households. It tends to be fairly straightforward for people to move between adjacent areas on either side of a border cutoff. If this is the case, the subjects can determine their treatment status themselves – for instance, an individual can move to a neighbouring state that decreases the income tax precisely to benefit from this ‘treatment’. In this way, subjects can non-randomly self-select into treatment, causing selection bias. 

This issue does not _always_ arise in GRD settings – for example, it may not be so straightforward for a worker to find a new job in a neighbouring country immediately after that country raises the minimum wage. There are two important points to consider here:

1.	Manipulation is more likely if policy or institutional differences in the past are strongly correlated with policy differences (treatments) in the present. This allows people the time to observe consistent differences across the cutoff and decide on which side of the boundary to live or work. This amounts to self-selection and can make the composition of the groups on either side of the border (cutoff) substantially and discontinuously different.

2.	There may be a trade-off between manipulation probability and the plausibility of continuity assumptions. On the one hand, a tightly sealed border reduces the probability of movement across it – and thus manipulation; on the other, it can also lead to the development of stark and discontinuous differences in relevant characteristics between the populations on either side of it, threatening the validity of the continuity assumption. 

#### Solutions

Given the high likelihood of sorting and running variable manipulation in GRD settings, it is a good idea to run the standard test for manipulation, the [McCrary density test](/validation/analysis), and the standard robustness check for such cases, the so-called [‘donut RDD’](/time/designs). The donut RDD method can also be used as the main estimation technique when sorting _is_ present: we eliminate the effects of intentional movements across the boundary by removing the observations just around the cutoff from our estimation. 

### Compound treatments

As previously mentioned, many geographic cutoffs are conducive to a setting where multiple treatments are applied to the same treatment group. This creates a fundamental difficulty for the precise identification of the causal effect of the treatment that we are interested in. Namely, we are unable to disentangle the individual effects of all of the treatments that are being applied at the same time. 

#### Solutions

Compound treatments may make it difficult to isolate the effect of the treatment that we are interested in. When working in GRD settings, we are always advised to search for boundaries that do not overlap with stark administrative borders, so as to minimise the probability of multiple treatments occurring. Nevertheless, this is often not possible. In these cases we either have to argue for the validity of the compound treatment irrelevance assumption or to exploit the difference-in-discontinuities (diff-in-disc) design. 

{{% tip %}}
Compound treatment irrelevance assumption: the only treatment that affects our outcome of interest is our treatment of interest. The other treatments have no effect whatsoever on the outcome. 
{{% /tip %}}

The difference-in-discontinuities approach is useful in cases where the treatments operate along the same boundary but were not applied in exactly the same time period. The crucial assumption here is that treatment effects are constant over time. 

{{% example %}}
Suppose we have two treatments, A and B, that both affect one side of a boundary, with the other side serving as the control group. Treatment A is applied in both periods 1 and 2. Treatment B, which is our treatment of interest, is only introduced in period 2. If we assume time-invariant treatment effects for treatment A, we can conclude that the difference in discontinuities between periods 2 and 1 is equal to the B’s treatment effect. In the below example, we observe that the treatment effect (discontinuity size) increases by 0.3 from 0.5 in period 1 to 0.8 in period 2. We assume that this difference is attributable to the introduction of treatment B in period 2; thus, B’s treatment effect is 0.8 – 0.5 = 0.3. 
| treatment | period 1 | period 2 |
|---|---|---|
| A | 0.5 | 0.5 |
| B | 0 | 0.3 |
| Total (observed) | 0.5 | 0.8 |

{{% /example %}}

{{% tip %}}
See [Grembi et al. (2016)](https://www.aeaweb.org/articles?id=10.1257/app.20150076) for a seminal application of the diff-in-disc method. 
{{% /tip %}}

### Strong continuity assumptions

The fact that the continuity assumptions are less likely to hold is of course also a major challenge. An RD design, in its continuity-based version, identifies a treatment effect by measuring a discontinuity in the outcome at the cutoff. Such a discontinuity can only be attributed to the treatment if treatment exposure or status is the _only_ variable changing _discontinuously_ at the threshold. If other relevant variables also change discontinuously at the cutoff, they become confounders and will create bias in our treatment effect estimates unless adequately adjusted for. 

#### Solutions

Firstly, it is always useful to check for violations of the continuity assumptions by testing for discontinuities in the relevant predetermined covariates at the cutoff. Keele and Titiunik propose the following method to do this in a GRD context: 

1. Calculate the geographic distance between every observation in our sample. 
2. Match each treated observation $i$ to a _single_ control observation that is closest to it.
3. Run a test (e.g., a t-test) for balance in covariates between the matched treated and control units. 

If we fail to reject the null hypotheses, we can infer that the continuity assumption holds. If we do reject it, we will have to incorporate the discontinuously changing covariate as a control variable in our regression. 

A major challenge is that many potential confounders are unobservable, and it is impossible to test or control for any potential discontinuities that they experience at the threshold. To avoid this issue invalidating our design, we need to carefully consider whether unobservable variables are likely to vary smoothly around our boundary, and to only select boundaries that where continuous covariate variation is likely.

### Spatial correlation

Given that in GRD designs we are working with spatial data, both outcomes and standard errors are likely to be spatially correlated. Spatial correlation in standard errors implies that the errors can be dependent on each other, where dependence is an increasing function of spatial proximity; i.e., units that are closer together have standard errors which correlate to a higher degree. Spatial correlation in outcomes means that units that are geographically closer together have more mutually similar outcome values due to their spatial proximity. 

#### Solutions

The standard solution to spatially correlated _standard errors_ is to estimate Conley standard errors, which are robust to spatial correlation. This can be done using the `conleyreg` package in R. One approach to address spatial correlation in outcomes is to include geographic area-specific fixed effects, sometimes called ‘segment fixed effects’. In order to do so, we would have to divide the boundary into several segments, within which we believe outcomes can be spatially correlated, and to assign each observation to one of the segments. As with any other fixed effects model, we would then include a dummy for each of these segments in our regression. 

{{% tip %}}
Other typical RDD robustness checks, such as sensitivity tests for bandwidths and polynomial orders and placebo cutoffs are also useful to implement in GRD designs. Read more about these in this [topic](/validation/analysis). 
{{% /tip %}}

## Summary

{{% summary %}}
-	Geographic regression discontinuity (GRD) designs are RDDs where the cutoff is a geographic boundary. They differ from canonical RDDs in that they have two running variables (latitude and longitude), stronger continuity and smoothness assumptions, compound treatments, and a continuum of location-specific local average treatment effects. 
-	The two main approaches to GRD estimation are **naïve distance** and **geographic estimation**. Naïve distance relies on collapsing longitude and latitude into a single running variable (distance to the cutoff), while geographic estimation preserves the original two running variables. Although naïve distance seems more intuitive, it may malfunction because it ignores spatial effect heterogeneity and may result in unreasonable comparisons. 
-	We discuss solutions to four major identification challenges in GRD: sorting and manipulation, compound treatments, stronger continuity assumptions, and spatial correlation. 
-	In GRD settings, it is particularly important to have a comprehensive understanding of the study setting and be able to assess to what extent our treatment estimates are likely to be affected by the peculiarities of a geographic context: how feasible manipulation is, whether other treatments can affect the outcome, how likely the continuity assumption is to hold, etc. 
{{% /summary %}}

## See Also

[Geographic boundaries as regression discontinuities - Keele and Titiunik (2015)](https://www.cambridge.org/core/journals/political-analysis/article/geographic-boundaries-as-regression-discontinuities/2A59F3077F49AD2B908B531F6E458430)

[A Note on Spatial Regression Discontinuity Designs - Lehner (2023)](https://lehner.xyz/publication/2021-spatialrdd_note/)

[SpatialRDD - R package](https://github.com/axlehner/SpatialRDD)

