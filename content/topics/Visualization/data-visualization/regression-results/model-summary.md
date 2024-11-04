---
title: "Generate regression tables in R with the `modelsummary` package"
description: "Use the package `modelsummary` to generate regression tables in R"
keywords: "modelsummary, packages, regression, regressions, model, table, R"
draft: false
weight: 2
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /modelsummary
  - /run/modelsummary/
  - /run/modelsummary
---

# Overview

The `modelsummary` package is a powerful and user-friendly package for summarizing regression results in R. It allows for easy comparison of multiple models, and offers a wide range of options for controlling the output format. This page will provide you with a summary of the most useful functions by replicating Table 1 from the paper ["Doing well by doing good? Green office buildings"](https://www.aeaweb.org/articles?id=10.1257/aer.100.5.2492) by Eichholtz et al. (2010) as an example.

## The Setting

Eichholtz et al. (2010) investigate the relationship between investments in energy efficiency in design and construction of commercial office buildings and the rents, the effective rents and the selling prices of these properties. Green ratings assess the energy footprint of buildings and can be used by building owners or tenants to evaluate the energy efficiency and sustainability of buildings.

Their empirical approach boils down to regressing the logarithm of rent per square foot in commercial office buildings on a dummy variable (1 if rated as green) and other characteristics of the buildings. The regression equation is:

$log R_{in} = \alpha + \beta_i X_i + \sum\limits_{n=1}^{N}\gamma_n c_n  + \delta g_i + \epsilon_{in}$

where

- $R_{in}$ is the rent per square foot in commercial office building `i` in cluster `n`
- $X_{i}$ is a vector of the hedonic characteristics of building `i`
- $c_n$ is a dummy variable with a value of 1 if building i is located in cluster n and zero otherwise (fixed effects)
- $g_{i}$ is a dummy variable with a value of 1 if building `i` is rated by Energy Star or USGBC and zero otherwise
- $\epsilon_{in}$ is the error term

## Load packages and data

The data set to replicate Table 1 comes from the [replication package of Eichholtz et al. (2010)](https://www.openicpsr.org/openicpsr/project/112392/version/V1/view). It contains data for 8,105 commercial office buildings in the US, both green buildings and control buildings. Green rated buildings are clustered to nearby commercial buildings in the same market.

<!-- On average, there are 12 buildings in each cluster.  -->

We use a tidied version of the data in their replication package.

{{% codeblock %}}

```R
# Load packages
library(modelsummary)
library(dplyr)
library(fixest)
library(stringr)


# Load data
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/topics/Visualization/data-visualization/regression-results/data_rent.Rda"

load(url(data_url)) #data_rent is the cleaned data set
```

{{% /codeblock %}}

## Regression equations

Below, we are estimating regression 1 until 5 displayed in Table 1 of Eichholtz et al. (2010). To control for locational effects, each regression also includes 694 dummy variables, one for each locational cluster. Regression (5) also includes an additional 694 dummy variables, one for each green building in the sample.

{{% codeblock %}}

```R
reg1 <- feols(logrent ~
                green_rating + size_new + oocc_new + class_a + class_b +
                net + empl_new |
                id,
                data = data_rent
                )

# Split "green rating" into two classifications: energystar and leed
reg2 <- feols(logrent ~
                energystar + leed + size_new + oocc_new + class_a + class_b +
                net + empl_new |
                id,
                data = data_rent
                )


reg3 <- feols(logrent ~
                 green_rating + size_new + oocc_new + class_a + class_b +
                 net + empl_new +
                 age_0_10 + age_10_20 + age_20_30 + age_30_40 + renovated |
                 id,
                 data = data_rent
                 )

reg4 <- feols(logrent ~
                 green_rating + size_new + oocc_new + class_a + class_b +
                 net + empl_new +
                 age_0_10 + age_10_20 + age_20_30 + age_30_40 +
                 renovated + story_medium + story_high + amenities  |
                 id, data = data_rent
                 )

# add fixed effects for green rating
reg5 <- feols(logrent ~
                 size_new + oocc_new + class_a + class_b +
                 net + empl_new  + renovated +
                 age_0_10 + age_10_20 + age_20_30 + age_30_40 +
                 story_medium + story_high + amenities |
                 id + green_rating,
                 data = data_rent
                 )
```

{{% /codeblock %}}

{{% tip %}}

- 78 observations are removed because of NA values in all 5 regressions. This results in a similar number of observations of 8105 as reported in Table 1 of Eichholtz et al. (2010).

- The variable `empl_new` is removed because of collinearity.
- Note that Eichholtz et al. (2010) do report an estimate for `empl_new`.
  <!-- `empl_new` defines the increase in employment in the service sector for the CBSA containing a cluster of a green building and its nearby control. The `empl_new` value is the same for all variables in one cluster; therefore it is already includes in the fixed effects `id` and it makes sense that R removes the variable.  -->
  <!-- However, Eichholtz et al. (2010) do report an estimate for `empl_new`. -->

<!-- - There is no constant in our output.
 Fixed effects models estimate separate intercepts for each level of a categorical variable (each id), which means that including a global intercept term would lead to perfect multicollinearity. Here, the model estimates a separate intercept term for each unique value of `id`, so there is no need to include a global intercept term. However, Eichholtz et al. (2010) do report a constant.  -->

{{% /tip %}}

## Output of table with `modelsummary`

Now we have estimated the regression equations for our table, we can move on to applying `modelsummary`. `models` defines a list of regression 1 until 5.

{{% codeblock %}}

```R
models <- list(
  "(1)" = reg1,
  "(2)" = reg2,
  "(3)" = reg3,
  "(4)" = reg4,
  "(5)" = reg5)

msummary(models)
```

{{% /codeblock %}}

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;"> <thead> <tr> <th style="text-align:left;"> </th> <th style="text-align:center;">  (1) </th> <th style="text-align:center;">   (2) </th> <th style="text-align:center;">   (3) </th> <th style="text-align:center;">   (4) </th> <th style="text-align:center;">   (5) </th> </tr> </thead> <tbody> <tr> <td style="text-align:left;"> green_rating </td> <td style="text-align:center;"> 0.035 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> 0.028 </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> size_new </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.102 </td> <td style="text-align:center;"> 0.110 </td> <td style="text-align:center;"> 0.110 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.023) </td> <td style="text-align:center;"> (0.023) </td> <td style="text-align:center;"> (0.022) </td> <td style="text-align:center;"> (0.027) </td> <td style="text-align:center;"> (0.027) </td> </tr> <tr> <td style="text-align:left;"> oocc_new </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.011 </td> <td style="text-align:center;"> 0.011 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.018) </td> <td style="text-align:center;"> (0.018) </td> <td style="text-align:center;"> (0.018) </td> <td style="text-align:center;"> (0.017) </td> <td style="text-align:center;"> (0.017) </td> </tr> <tr> <td style="text-align:left;"> class_a </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.192 </td> <td style="text-align:center;"> 0.173 </td> <td style="text-align:center;"> 0.173 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.015) </td> <td style="text-align:center;"> (0.015) </td> </tr> <tr> <td style="text-align:left;"> class_b </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.092 </td> <td style="text-align:center;"> 0.083 </td> <td style="text-align:center;"> 0.083 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> </tr> <tr> <td style="text-align:left;"> net </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.050 </td> <td style="text-align:center;"> -0.051 </td> <td style="text-align:center;"> -0.051 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> energystar </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> leed </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.052 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.035) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> age_0_10 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.118 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> </tr> <tr> <td style="text-align:left;"> age_10_20 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.079 </td> <td style="text-align:center;"> 0.084 </td> <td style="text-align:center;"> 0.084 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.017) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> </tr> <tr> <td style="text-align:left;"> age_20_30 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.048 </td> <td style="text-align:center;"> 0.048 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> age_30_40 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.043 </td> <td style="text-align:center;"> 0.044 </td> <td style="text-align:center;"> 0.044 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> </tr> <tr> <td style="text-align:left;"> renovated </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.010) </td> <td style="text-align:center;"> (0.010) </td> <td style="text-align:center;"> (0.010) </td> </tr> <tr> <td style="text-align:left;"> story_medium </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.010 </td> <td style="text-align:center;"> 0.010 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> </tr> <tr> <td style="text-align:left;"> story_high </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.027 </td> <td style="text-align:center;"> -0.027 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> </tr> <tr> <td style="text-align:left;"> amenities </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.047 </td> </tr> <tr> <td style="text-align:left;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.008) </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.008) </td> </tr> <tr> <td style="text-align:left;"> Num.Obs. </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> </tr> <tr> <td style="text-align:left;"> R2 </td> <td style="text-align:center;"> 0.715 </td> <td style="text-align:center;"> 0.715 </td> <td style="text-align:center;"> 0.718 </td> <td style="text-align:center;"> 0.720 </td> <td style="text-align:center;"> 0.720 </td> </tr> <tr> <td style="text-align:left;"> R2 Adj. </td> <td style="text-align:center;"> 0.688 </td> <td style="text-align:center;"> 0.688 </td> <td style="text-align:center;"> 0.691 </td> <td style="text-align:center;"> 0.693 </td> <td style="text-align:center;"> 0.693 </td> </tr> <tr> <td style="text-align:left;"> R2 Within </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.140 </td> <td style="text-align:center;"> 0.146 </td> <td style="text-align:center;"> 0.133 </td> </tr> <tr> <td style="text-align:left;"> R2 Within Adj. </td> <td style="text-align:center;"> 0.130 </td> <td style="text-align:center;"> 0.130 </td> <td style="text-align:center;"> 0.138 </td> <td style="text-align:center;"> 0.144 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> AIC </td> <td style="text-align:center;"> 1530.9 </td> <td style="text-align:center;"> 1532.5 </td> <td style="text-align:center;"> 1460.4 </td> <td style="text-align:center;"> 1409.2 </td> <td style="text-align:center;"> 1409.2 </td> </tr> <tr> <td style="text-align:left;"> BIC </td> <td style="text-align:center;"> 6389.1 </td> <td style="text-align:center;"> 6397.7 </td> <td style="text-align:center;"> 6353.6 </td> <td style="text-align:center;"> 6323.4 </td> <td style="text-align:center;"> 6323.4 </td> </tr> <tr> <td style="text-align:left;"> RMSE </td> <td style="text-align:center;"> 0.24 </td> <td style="text-align:center;"> 0.24 </td> <td style="text-align:center;"> 0.24 </td> <td style="text-align:center;"> 0.24 </td> <td style="text-align:center;"> 0.24 </td> </tr> <tr> <td style="text-align:left;"> Std.Errors </td> <td style="text-align:center;"> by: id </td> <td style="text-align:center;"> by: id </td> <td style="text-align:center;"> by: id </td> <td style="text-align:center;"> by: id </td> <td style="text-align:center;"> by: id </td> </tr> <tr> <td style="text-align:left;"> FE: id </td> <td style="text-align:center;"> X </td> <td style="text-align:center;"> X </td> <td style="text-align:center;"> X </td> <td style="text-align:center;"> X </td> <td style="text-align:center;"> X </td> </tr> <tr> <td style="text-align:left;"> FE: green_rating </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> X </td> </tr> </tbody> </table>

This table provides a relatively clean, easy to read summary of the five regression models.
In the rest of the post, we will extend and improve this table making it into something to that could be used in a research paper or presentation.
We will:

- Report different standard errors
- Choosing which coefficients to report and renaming them
- Reformat estimates and statistics
- Add a caption title and table notes
- Add stars denoting statistical significance
- Format the number of decimals
- Report confidence interval rather than standard errora
- Export the output to a file

## Report different standard errors

Within the `modelsummary` function, it is possible to specify different types of standard errors, such as robust or clustered standard errors. To replicate the output of Eichholtz et al. (2010), we use robust standard errors by specifying `vcov = "HC1"`. This is appropriate when the variance of the errors varies across observations, which can result in biased standard errors.

On the other hand, clustered standard errors are appropriate when there are groups of observations that are likely to be correlated with each other. To specify standard errors clustered around the id values, we could use `cluster = ~id`. Note that the default behavior is to cluster standard errors by the variable used to estimate the fixed effects, which in this case is the id variable.

{{% codeblock %}}

```R
#robust standard errors
msummary(models, vcov = "HC1")
```

{{% /codeblock %}}

## Selecting and formatting estimates

`coef_map = cm` is used to specify the variable names in our output table, and to rearrange the order of the rows to match Table 1.

{{% codeblock %}}

```R
cm = c('green_rating'    = 'Green rating (1 = yes)',
  'energystar'    = 'Energystar (1 = yes)',
  'leed'    = 'LEED (1 = yes)',
  'size_new'    = 'Building size (millions of sq.ft)',
  'oocc_new' = 'Fraction occupied',
  'class_a' = 'Building class A (1 = yes)',
  'class_b' = 'Building class B (1 = yes)',
  'net' = 'Net contract (1 = yes)',
  'age_0_10' = 'Age: <10 years',
  'age_10_20' = 'Age: 10-20 years',
  'age_20_30' = 'Age: 20-30 years',
  'age_30_40' = 'Age: 30-40 years',
  'renovated' = 'Renovated (1 = yes)',
  'story_medium' = 'Stories: Intermediate (1 = yes)',
  'story_high' = 'Stories: High (1 = yes)',
  'amenities' = 'Amenities (1 = yes)')

msummary(models, vcov="HC1",
         coef_map = cm)
```

{{% /codeblock %}}

## Selecting and formatting statistics

- `gof_omit =` allows us to exclude certain statistics from being displayed in the table's bottom section.
- `gof_map = gm` is used to specify which statistics we want to include in the bottom section, as well as their desired formatting. The names of the statistics are specified using `clean=` and the number of decimals places are specified using `fmt=`.

{{% codeblock %}}

```R
gm <- list(
  list("raw" = "nobs", "clean" = "Sample size", "fmt" = 0),
  list("raw" = "r.squared", "clean" = "R<sup>2</sup>", "fmt" = 2),
  list("raw" = "adj.r.squared", "clean" = "Adjusted R<sup>2</sup>", "fmt" = 2))
      #get_gof(reg1) to see "raw" names of these statistics.

msummary(models, vcov="HC1",
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm)
```

{{% /codeblock %}}

After applying the first few steps, the output table looks like this:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;"> <thead> <tr> <th style="text-align:left;"> </th> <th style="text-align:center;">  (1) </th> <th style="text-align:center;">   (2) </th> <th style="text-align:center;">   (3) </th> <th style="text-align:center;">   (4) </th> <th style="text-align:center;">   (5) </th> </tr> </thead> <tbody> <tr> <td style="text-align:left;"> Green rating (1 = yes) </td> <td style="text-align:center;"> 0.035 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> 0.028 </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Energystar (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> LEED (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.052 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.036) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Building size (millions of sq.ft) </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.102 </td> <td style="text-align:center;"> 0.110 </td> <td style="text-align:center;"> 0.110 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.021) </td> <td style="text-align:center;"> (0.021) </td> </tr> <tr> <td style="text-align:left;"> Fraction occupied </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.011 </td> <td style="text-align:center;"> 0.011 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> </tr> <tr> <td style="text-align:left;"> Building class A (1 = yes) </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.192 </td> <td style="text-align:center;"> 0.173 </td> <td style="text-align:center;"> 0.173 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.015) </td> <td style="text-align:center;"> (0.015) </td> </tr> <tr> <td style="text-align:left;"> Building class B (1 = yes) </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.092 </td> <td style="text-align:center;"> 0.083 </td> <td style="text-align:center;"> 0.083 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> </tr> <tr> <td style="text-align:left;"> Net contract (1 = yes) </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.050 </td> <td style="text-align:center;"> -0.051 </td> <td style="text-align:center;"> -0.051 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> Age: &lt;10 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.118 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.017) </td> <td style="text-align:center;"> (0.017) </td> </tr> <tr> <td style="text-align:left;"> Age: 10-20 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.079 </td> <td style="text-align:center;"> 0.084 </td> <td style="text-align:center;"> 0.084 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> </tr> <tr> <td style="text-align:left;"> Age: 20-30 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.048 </td> <td style="text-align:center;"> 0.048 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> Age: 30-40 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.043 </td> <td style="text-align:center;"> 0.044 </td> <td style="text-align:center;"> 0.044 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> </tr> <tr> <td style="text-align:left;"> Renovated (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> </tr> <tr> <td style="text-align:left;"> Stories: Intermediate (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.010 </td> <td style="text-align:center;"> 0.010 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> </tr> <tr> <td style="text-align:left;"> Stories: High (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.027 </td> <td style="text-align:center;"> -0.027 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.015) </td> <td style="text-align:center;"> (0.015) </td> </tr> <tr> <td style="text-align:left;"> Amenities (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.047 </td> </tr> <tr> <td style="text-align:left;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.007) </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.007) </td> </tr> <tr> <td style="text-align:left;"> Sample size </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> </tr> <tr> <td style="text-align:left;"> R<sup>2</sup> </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> </tr> <tr> <td style="text-align:left;"> Adjusted R<sup>2</sup> </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> </tr> </tbody> </table>

## Add a caption to the table and include table notes

We can also add a title and note to our table.

{{% codeblock %}}

```R
notetable1 <- c(
  "Notes: Each regression also includes 694 dummy variables, one for each locational cluster.
  Regression (5) also includes an additional 694 dummy variables, one for each green building in the sample.
  Standard errors are in parentheses")

titletable1 <- 'Table 1—Regression Results, Commercial Office Rents and Green Ratings
(dependent variable: logarithm of effective rent in dollars per square foot)'

msummary(models, vcov="HC1",
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm,
         notes = notetable1,
         title = titletable1)

```

{{% /codeblock %}}

<table style="NAborder-bottom: 0; width: auto !important; margin-left: auto; margin-right: auto;" class="table"> <caption>Table 1—Regression Results, Commercial Office Rents and Green Ratings <br> (dependent variable: logarithm of effective rent in dollars per square foot)</caption> <thead> <tr> <th style="text-align:left;"> </th> <th style="text-align:center;">  (1) </th> <th style="text-align:center;">   (2) </th> <th style="text-align:center;">   (3) </th> <th style="text-align:center;">   (4) </th> <th style="text-align:center;">   (5) </th> </tr> </thead> <tbody> <tr> <td style="text-align:left;"> Green rating (1 = yes) </td> <td style="text-align:center;"> 0.035 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> 0.028 </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Energystar (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> LEED (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.052 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.036) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Building size (millions of sq.ft) </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.102 </td> <td style="text-align:center;"> 0.110 </td> <td style="text-align:center;"> 0.110 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.019) </td> <td style="text-align:center;"> (0.021) </td> <td style="text-align:center;"> (0.021) </td> </tr> <tr> <td style="text-align:left;"> Fraction occupied </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.011 </td> <td style="text-align:center;"> 0.011 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.016) </td> </tr> <tr> <td style="text-align:left;"> Building class A (1 = yes) </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.192 </td> <td style="text-align:center;"> 0.173 </td> <td style="text-align:center;"> 0.173 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.012) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.015) </td> <td style="text-align:center;"> (0.015) </td> </tr> <tr> <td style="text-align:left;"> Building class B (1 = yes) </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.092 </td> <td style="text-align:center;"> 0.083 </td> <td style="text-align:center;"> 0.083 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> </tr> <tr> <td style="text-align:left;"> Net contract (1 = yes) </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.050 </td> <td style="text-align:center;"> -0.051 </td> <td style="text-align:center;"> -0.051 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> Age: &lt;10 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.118 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.016) </td> <td style="text-align:center;"> (0.017) </td> <td style="text-align:center;"> (0.017) </td> </tr> <tr> <td style="text-align:left;"> Age: 10-20 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.079 </td> <td style="text-align:center;"> 0.084 </td> <td style="text-align:center;"> 0.084 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> <td style="text-align:center;"> (0.014) </td> </tr> <tr> <td style="text-align:left;"> Age: 20-30 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.048 </td> <td style="text-align:center;"> 0.048 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> <td style="text-align:center;"> (0.013) </td> </tr> <tr> <td style="text-align:left;"> Age: 30-40 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.043 </td> <td style="text-align:center;"> 0.044 </td> <td style="text-align:center;"> 0.044 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> <td style="text-align:center;"> (0.011) </td> </tr> <tr> <td style="text-align:left;"> Renovated (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> </tr> <tr> <td style="text-align:left;"> Stories: Intermediate (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.010 </td> <td style="text-align:center;"> 0.010 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.009) </td> <td style="text-align:center;"> (0.009) </td> </tr> <tr> <td style="text-align:left;"> Stories: High (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.027 </td> <td style="text-align:center;"> -0.027 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> (0.015) </td> <td style="text-align:center;"> (0.015) </td> </tr> <tr> <td style="text-align:left;"> Amenities (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.047 </td> </tr> <tr> <td style="text-align:left;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.007) </td> <td style="text-align:center;box-shadow: 0px 1.5px"> (0.007) </td> </tr> <tr> <td style="text-align:left;"> Sample size </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> </tr> <tr> <td style="text-align:left;"> R<sup>2</sup> </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> </tr> <tr> <td style="text-align:left;"> Adjusted R<sup>2</sup> </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> </tr> </tbody> <tfoot><tr><td style="padding: 0; " colspan="100%"> <sup></sup> Notes: Each regression also includes 694 dummy variables, one for each locational <br> cluster. Regression (5) also includes an additional 694 dummy variables, one for <br> each green building in the sample. Standard errors are in parentheses.</td></tr></tfoot> </table>

## Add stars denoting statistical significance

The stars in a regression table are used to indicate the level of statistical significance of the coefficients in the regression model. They are based on the p-values, which measure the probability of obtaining the observed results when there is in fact no effect.

### Argument "stars = TRUE"

To add stars to our regression table, we can use the `stars = TRUE` argument. This will automatically add stars to the table based on a default threshold of statistical significance. By default, a note explaining the significance levels will be added at the bottom of the table: + p < 0.1, \* p < 0.05, ** p < 0.01, \*** p < 0.001.

{{% codeblock %}}

```R
msummary(models,
         vcov = "HC1",
         stars=TRUE,
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm,
         notes = notetable1,
         title = titletable1)
```

{{% /codeblock %}}

### Manually add stars

To replicate Table 1 of Eichholtz et al. (2010), we need to customize the output of the regression table to show the significance of coefficients using stars.

- By default, the stars are printed next to the coefficient estimate, but we want the stars to be printed on the row of the standard error. This can be done by manually adding a list for stars and adding it to the `statistics` argument. Check the code block below!
- Additionally, we want a different note about the stars so we change our note and add the new note to the `notes` argument.

{{% codeblock %}}

```R
note2table1 <- c(
  "Notes: Each regression also includes 694 dummy variables, one for each locational cluster.
  Regression (5) also includes an additional 694 dummy variables, one for each green building in the sample.
  Standard errors are in brackets.",
  "***Significant at the 1 percent level.",
  "**Significant at the 5 percent level.",
  "*Significant at the 10 percent level.")


msummary(models,
         stars  = c('*' = .1, '**' = 0.05, '***' = .01),
         estimate = "{estimate}",
         statistic = "[{std.error}]{stars}",
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm,
         notes = note2table1,
         title = titletable1)

```

{{% /codeblock %}}

<table style="NAborder-bottom: 0; width: auto !important; margin-left: auto; margin-right: auto;" class="table"> <caption>Table 1—Regression Results, Commercial Office Rents and Green Ratings <br> (dependent variable: logarithm of effective rent in dollars per square foot)</caption> <thead> <tr> <th style="text-align:left;"> </th> <th style="text-align:center;">  (1) </th> <th style="text-align:center;">   (2) </th> <th style="text-align:center;">   (3) </th> <th style="text-align:center;">   (4) </th> <th style="text-align:center;">   (5) </th> </tr> </thead> <tbody> <tr> <td style="text-align:left;"> Green rating (1 = yes) </td> <td style="text-align:center;"> 0.035 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> 0.028 </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.009]*** </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.009]*** </td> <td style="text-align:center;"> [0.009]*** </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Energystar (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.009]*** </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> LEED (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.052 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.035] </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Building size (millions of sq.ft) </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.102 </td> <td style="text-align:center;"> 0.110 </td> <td style="text-align:center;"> 0.110 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.023]*** </td> <td style="text-align:center;"> [0.023]*** </td> <td style="text-align:center;"> [0.022]*** </td> <td style="text-align:center;"> [0.027]*** </td> <td style="text-align:center;"> [0.027]*** </td> </tr> <tr> <td style="text-align:left;"> Fraction occupied </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.011 </td> <td style="text-align:center;"> 0.011 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.018] </td> <td style="text-align:center;"> [0.018] </td> <td style="text-align:center;"> [0.018] </td> <td style="text-align:center;"> [0.017] </td> <td style="text-align:center;"> [0.017] </td> </tr> <tr> <td style="text-align:left;"> Building class A (1 = yes) </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.192 </td> <td style="text-align:center;"> 0.173 </td> <td style="text-align:center;"> 0.173 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.012]*** </td> <td style="text-align:center;"> [0.012]*** </td> <td style="text-align:center;"> [0.013]*** </td> <td style="text-align:center;"> [0.015]*** </td> <td style="text-align:center;"> [0.015]*** </td> </tr> <tr> <td style="text-align:left;"> Building class B (1 = yes) </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.092 </td> <td style="text-align:center;"> 0.083 </td> <td style="text-align:center;"> 0.083 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.011]*** </td> <td style="text-align:center;"> [0.011]*** </td> <td style="text-align:center;"> [0.011]*** </td> <td style="text-align:center;"> [0.011]*** </td> <td style="text-align:center;"> [0.011]*** </td> </tr> <tr> <td style="text-align:left;"> Net contract (1 = yes) </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.050 </td> <td style="text-align:center;"> -0.051 </td> <td style="text-align:center;"> -0.051 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.014]*** </td> <td style="text-align:center;"> [0.014]*** </td> <td style="text-align:center;"> [0.014]*** </td> <td style="text-align:center;"> [0.013]*** </td> <td style="text-align:center;"> [0.013]*** </td> </tr> <tr> <td style="text-align:left;"> Age: &lt;10 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.118 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.019]*** </td> <td style="text-align:center;"> [0.019]*** </td> <td style="text-align:center;"> [0.019]*** </td> </tr> <tr> <td style="text-align:left;"> Age: 10-20 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.079 </td> <td style="text-align:center;"> 0.084 </td> <td style="text-align:center;"> 0.084 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.017]*** </td> <td style="text-align:center;"> [0.016]*** </td> <td style="text-align:center;"> [0.016]*** </td> </tr> <tr> <td style="text-align:left;"> Age: 20-30 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.048 </td> <td style="text-align:center;"> 0.048 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.013]*** </td> <td style="text-align:center;"> [0.013]*** </td> <td style="text-align:center;"> [0.013]*** </td> </tr> <tr> <td style="text-align:left;"> Age: 30-40 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.043 </td> <td style="text-align:center;"> 0.044 </td> <td style="text-align:center;"> 0.044 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.012]*** </td> <td style="text-align:center;"> [0.012]*** </td> <td style="text-align:center;"> [0.012]*** </td> </tr> <tr> <td style="text-align:left;"> Renovated (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.010] </td> <td style="text-align:center;"> [0.010] </td> <td style="text-align:center;"> [0.010] </td> </tr> <tr> <td style="text-align:left;"> Stories: Intermediate (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.010 </td> <td style="text-align:center;"> 0.010 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.012] </td> <td style="text-align:center;"> [0.012] </td> </tr> <tr> <td style="text-align:left;"> Stories: High (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.027 </td> <td style="text-align:center;"> -0.027 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.019] </td> <td style="text-align:center;"> [0.019] </td> </tr> <tr> <td style="text-align:left;"> Amenities (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.047 </td> </tr> <tr> <td style="text-align:left;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> [0.008]*** </td> <td style="text-align:center;box-shadow: 0px 1.5px"> [0.008]*** </td> </tr> <tr> <td style="text-align:left;"> Sample size </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> </tr> <tr> <td style="text-align:left;"> R<sup>2</sup> </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> </tr> <tr> <td style="text-align:left;"> Adjusted R<sup>2</sup> </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> </tr> </tbody> <tfoot> <tr><td style="padding: 0; " colspan="100%"> <sup></sup> Notes: Each regression also includes 694 dummy variables, one for each locational cluster. Regression (5) <br> also includes an additional 694 dummy variables, one for each green building in the sample. Standard <br> errors are in brackets.</td></tr> <tr><td style="padding: 0; " colspan="100%"> <sup></sup> *** Significant at the 1 percent level.</td></tr> <tr><td style="padding: 0; " colspan="100%"> <sup></sup> ** Significant at the 5 percent level.</td></tr> <tr><td style="padding: 0; " colspan="100%"> <sup></sup> * Significant at the 10 percent level.</td></tr> </tfoot> </table>

## Format the number of decimals

The `fmt` argument in the `modelsummary` functions allows us to control how numeric values are rounded and presented in the table. In order to match the formatting of Table 1 in Eichholtz et al. (2010), we set the number of decimal digits to 3.

There is various ways to get the desired number of decimals. For example, it is possible to give statistics a different number of decimals than estimates, or to display the values in scientific (exponential) notation by specifying `fmt = fmt_sprintf("%.3e")`.

{{% codeblock %}}

```R
msummary(models,
         vcov = "HC1",
         fmt = fmt_statistic(estimate = 3, std.error = 3),
        #just adding "fmt = 3" gives same result, since estimate and standard error are both set to 3 decimals.
         stars  = c('*' = .1, '**' = 0.05, '***' = .01),
         estimate = "{estimate}",
         statistic = "[{std.error}]{stars}",
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm,
         notes = note2table1,
         title = titletable1)

```

{{% /codeblock %}}

## Report confidence intervals instead of standard errors

Some scientific associations discourage the use of stars. For instance, one of the [guidelines](https://www.aeaweb.org/journals/aer/submissions) of the American Economic Association is to report standard errors in parentheses but to not use \*s to report significance levels.

In this step, we leave out the stars and report confidence intervals instead of standard errors. In some situations confidence intervals might be more informative, as they provide a range of plausible values that can be used to estimate the true value of a population parameter.

{{% codeblock %}}

```R
#Change the note to be correct
note3table1 <-  c("Notes: Each regression also includes 694 dummy variables, one for
each locational cluster. Regression (5) also includes an additional 694 dummy variables,
one for each green building in the sample. Confidence intervals are in brackets.")

msummary(models,
         vcov = "HC1",
         fmt = fmt_statistic(estimate = 3, conf.int = 3),
         statistic ='conf.int',
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|Std.Errors|FE',
         gof_map = gm,
         notes = note3table1,
         title = titletable1)
```

{{% /codeblock %}}

<table style="NAborder-bottom: 0; width: auto !important; margin-left: auto; margin-right: auto;" class="table"> <caption>Table 1—Regression Results, Commercial Office Rents and Green Ratings <br> (dependent variable: logarithm of effective rent in dollars per square foot)</caption> <thead> <tr> <th style="text-align:left;"> </th> <th style="text-align:center;">  (1) </th> <th style="text-align:center;">   (2) </th> <th style="text-align:center;">   (3) </th> <th style="text-align:center;">   (4) </th> <th style="text-align:center;">   (5) </th> </tr> </thead> <tbody> <tr> <td style="text-align:left;"> Green rating (1 = yes) </td> <td style="text-align:center;"> 0.035 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> 0.028 </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.018, 0.053] </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.015, 0.050] </td> <td style="text-align:center;"> [0.011, 0.046] </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Energystar (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.033 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.016, 0.050] </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> LEED (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.052 </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [-0.019, 0.123] </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> </tr> <tr> <td style="text-align:left;"> Building size (millions of sq.ft) </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.113 </td> <td style="text-align:center;"> 0.102 </td> <td style="text-align:center;"> 0.110 </td> <td style="text-align:center;"> 0.110 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.076, 0.150] </td> <td style="text-align:center;"> [0.076, 0.150] </td> <td style="text-align:center;"> [0.065, 0.139] </td> <td style="text-align:center;"> [0.069, 0.152] </td> <td style="text-align:center;"> [0.069, 0.152] </td> </tr> <tr> <td style="text-align:left;"> Fraction occupied </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.020 </td> <td style="text-align:center;"> 0.011 </td> <td style="text-align:center;"> 0.011 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [-0.011, 0.051] </td> <td style="text-align:center;"> [-0.011, 0.051] </td> <td style="text-align:center;"> [-0.010, 0.051] </td> <td style="text-align:center;"> [-0.020, 0.041] </td> <td style="text-align:center;"> [-0.020, 0.041] </td> </tr> <tr> <td style="text-align:left;"> Building class A (1 = yes) </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.231 </td> <td style="text-align:center;"> 0.192 </td> <td style="text-align:center;"> 0.173 </td> <td style="text-align:center;"> 0.173 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.207, 0.255] </td> <td style="text-align:center;"> [0.207, 0.255] </td> <td style="text-align:center;"> [0.165, 0.220] </td> <td style="text-align:center;"> [0.143, 0.203] </td> <td style="text-align:center;"> [0.143, 0.203] </td> </tr> <tr> <td style="text-align:left;"> Building class B (1 = yes) </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.101 </td> <td style="text-align:center;"> 0.092 </td> <td style="text-align:center;"> 0.083 </td> <td style="text-align:center;"> 0.083 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [0.080, 0.123] </td> <td style="text-align:center;"> [0.080, 0.122] </td> <td style="text-align:center;"> [0.070, 0.113] </td> <td style="text-align:center;"> [0.060, 0.105] </td> <td style="text-align:center;"> [0.060, 0.105] </td> </tr> <tr> <td style="text-align:left;"> Net contract (1 = yes) </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.047 </td> <td style="text-align:center;"> -0.050 </td> <td style="text-align:center;"> -0.051 </td> <td style="text-align:center;"> -0.051 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> [-0.072, -0.022] </td> <td style="text-align:center;"> [-0.072, -0.022] </td> <td style="text-align:center;"> [-0.076, -0.025] </td> <td style="text-align:center;"> [-0.076, -0.026] </td> <td style="text-align:center;"> [-0.076, -0.026] </td> </tr> <tr> <td style="text-align:left;"> Age: &lt;10 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.118 </td> <td style="text-align:center;"> 0.131 </td> <td style="text-align:center;"> 0.131 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.086, 0.151] </td> <td style="text-align:center;"> [0.098, 0.163] </td> <td style="text-align:center;"> [0.098, 0.163] </td> </tr> <tr> <td style="text-align:left;"> Age: 10-20 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.079 </td> <td style="text-align:center;"> 0.084 </td> <td style="text-align:center;"> 0.084 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.052, 0.106] </td> <td style="text-align:center;"> [0.058, 0.111] </td> <td style="text-align:center;"> [0.058, 0.111] </td> </tr> <tr> <td style="text-align:left;"> Age: 20-30 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.048 </td> <td style="text-align:center;"> 0.048 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.022, 0.072] </td> <td style="text-align:center;"> [0.024, 0.073] </td> <td style="text-align:center;"> [0.024, 0.073] </td> </tr> <tr> <td style="text-align:left;"> Age: 30-40 years </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.043 </td> <td style="text-align:center;"> 0.044 </td> <td style="text-align:center;"> 0.044 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [0.023, 0.064] </td> <td style="text-align:center;"> [0.024, 0.065] </td> <td style="text-align:center;"> [0.024, 0.065] </td> </tr> <tr> <td style="text-align:left;"> Renovated (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> <td style="text-align:center;"> -0.008 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [-0.026, 0.011] </td> <td style="text-align:center;"> [-0.026, 0.010] </td> <td style="text-align:center;"> [-0.026, 0.010] </td> </tr> <tr> <td style="text-align:left;"> Stories: Intermediate (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.010 </td> <td style="text-align:center;"> 0.010 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [-0.008, 0.027] </td> <td style="text-align:center;"> [-0.008, 0.027] </td> </tr> <tr> <td style="text-align:left;"> Stories: High (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> -0.027 </td> <td style="text-align:center;"> -0.027 </td> </tr> <tr> <td style="text-align:left;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> [-0.056, 0.001] </td> <td style="text-align:center;"> [-0.056, 0.001] </td> </tr> <tr> <td style="text-align:left;"> Amenities (1 = yes) </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> </td> <td style="text-align:center;"> 0.047 </td> <td style="text-align:center;"> 0.047 </td> </tr> <tr> <td style="text-align:left;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> </td> <td style="text-align:center;box-shadow: 0px 1.5px"> [0.033, 0.061] </td> <td style="text-align:center;box-shadow: 0px 1.5px"> [0.033, 0.061] </td> </tr> <tr> <td style="text-align:left;"> Sample size </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> <td style="text-align:center;"> 8105 </td> </tr> <tr> <td style="text-align:left;"> R<sup>2</sup> </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.71 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> <td style="text-align:center;"> 0.72 </td> </tr> <tr> <td style="text-align:left;"> Adjusted R<sup>2</sup> </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> <td style="text-align:center;"> 0.69 </td> </tr> </tbody> <tfoot><tr><td style="padding: 0; " colspan="100%"> <sup></sup> Notes: Each regression also includes 694 dummy variables, one for each locational cluster. Regression (5) also includes an <br> additional 694 dummy variables, one for each green building in the sample. Confidence intervals are in brackets.</td></tr></tfoot> </table>

## Exporting the table to a file

The `output` argument specifies the destination where the output can be exported. In the given code, the output is named `table1.html`. The extension `.html` specifies that the table will be printed in HTML format. Other possible extensions are for example `.docx`, `.md`, and `.txt`. If the `output` argument is not included, the output will be printed directly in the console.

{{% codeblock %}}

```R
msummary(models, output = "table1.html",
         vcov = "HC1",
         fmt = fmt_statistic(estimate = 3, std.error = 3),
         stars  = c('*' = .1, '**' = 0.05, '***' = .01),
         estimate = "{estimate}",
         statistic = "[{std.error}]{stars}",
         coef_map = cm,
         gof_omit = 'AIC|BIC|RMSE|Within|FE',
         gof_map = gm,
         notes = note2table1,
         title = titletable1)
```

{{% /codeblock %}}

{{% summary %}}

In this building block, we covered the most useful functions of the `modelsummary` package:

- You can customize the standard errors printed in your model. For instance, `vcov = "HC1"` will give robust standard errors, and `cluster= ~id` will produce clustered standard errors by the variable `id`.
- You can customize the way estimates and statistics are presented, including the order of the estimates, variable names and which goodness-of-fit measures are printed.
- It is possible to add a title and note at the bottom of your table.
- You can add stars to indicate the level of statistical significance of the coefficients with `stars = TRUE`, which provides default values and a note at the bottom. Alternatively, you can add stars manually to customize the threshold for significance or the note at the bottom.
- You can choose to include confidence intervals instead of standard errors for your estimates.
- The `fmt` argument allows you to specify the number of decimal places for estimates and statistics.
- You can export the table using the `output` argument. Adding extensions like `.html` and `.docx` will produce the table in that format.

{{% /summary %}}
