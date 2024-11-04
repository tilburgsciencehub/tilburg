---
title: "SPSS Data in R"
description: "Learn how to import, export and work with SPSS data in R"
keywords: "R, SPSS, sav, labelled data, metadata, categorical, ordinal, nominal, interval, dplyr"
weight: 100000
date: 2023/07/07
draft: false
author: "Stefan Kirsch"
authorlink: "https://www.linkedin.com/in/stefan-kirsch-6b407078/"
aliases:
  - topics/prepare-your-data-for-analysis/data-preparation/spss-files-in-R
---

# Learning goals

- Read, process and manipulate SPSS (or other labelled) data in R while maintaining the labels
- Learn the most common operations on labels
- Enable you to seamlessly work with both R and SPSS so you can split your workflow between the two as you (or your teammates) wish

# Overview

Researchers often work with both R and SPSS, so it is helpful to work with `.sav` files in R. While working with SPSS data in R is not particularly hard, it can be quite confusing to chose the right approach. There are several packages available on [CRAN](https://cran.r-project.org/index.html) that offer more or less the same functionality, but some of them don't work well in conjunction with each other and most of them don't offer all the features you might need. This building block is intended to guide you through the tasks you will find yourself doing most often when working with SPSS data in R.

## Required packages

For this workflow, we'll need two packages: the ubiquitous `tidyverse` as well as `sjlabelled`.

{{% codeblock %}}

```R
library(tidyverse)
library(sjlabelled)
```

{{% /codeblock %}}

There are several packages on CRAN that allow reading `.sav` files and handling labelled data. [`haven`](https://haven.tidyverse.org/) (co-authored by Hadley Wickham) and [`labelled`](https://cran.r-project.org/web/packages/labelled/index.html) seem to be the most well-maintained ones, but they both lack some crucial functions, like converting factors to numeric. [`sjlabelled`](https://cran.r-project.org/web/packages/sjlabelled/index.html) is yet another package that does provide this functionality. While `haven` and `labelled` work great in conjunction with each other, it is not recommended combine them with `sjlabelled`, as there are several name conflicts, which can make things confusing. Hence, we will be only using `sjlabelled` in this tutorial.

## Importing and inspecting labelled data

To read a `.sav` file, we can use `read_spss()` from the `sjlabelled` package. Categorical variables that SPSS stores as numbers are automatically converted to factors. Note that at this point the displayed levels will still be numbers. In version 1.2.0 of `sjlabelled`, which was the latest version when this tutorial was written, `read_spss()` returns a data.frame. We recommend to convert to a [tibble](https://tibble.tidyverse.org/reference/tibble.html) right away:

{{% codeblock %}}

```R
sjlabelled::read_spss("path_to_your_data.sav") |> as_tibble()
```

{{% /codeblock %}}

For this tutorial, we'll work with the `efc` dataset on informal care. It comes with the `sjlabelled` package.

{{% codeblock %}}

```r
# attach the dataset and create a dataframe
data(efc)
df <- efc
```

{{% /codeblock %}}

SPSS works with both _variable labels_ and _value labels_. _Value labels_ can be very handy to store relevant metadata. For example, you can store the whole question that the participants got to see.

{{% tip %}}

Unfortunately, R doesn't do the best job of communicating the labels to you as the user. When we print the dataset to the console, we don't see any indication that we are dealing with labelled data.

If we `View()` the dataframe, we do at least see the _variable labels_ in the columns.

You can inspect the data labels with dedicated `sjlabelled` functions, though. `get_label()` returns a named vector of the variable labels, while `get_labels()` returns a named list of named vectors containing the value labels.

```R
# vector of VARIABLE labels
get_label(df)

# list of vectors with VALUE labels for the factor levels
get_labels(df)
```

{{% /tip %}}

## Manipulating labels

Unlike SPSS, R does not gain any performance by storing categorical data as numbers instead of the actual (character) value. This has the benefit that the data it is more easily readable by a human and makes data manipulation by category more intuitive. We can replace the numeric levels with the actual categories with `as_label()`.

{{% codeblock %}}

```R
df_factor <- as_label(df)
df_factor
```

{{% /codeblock %}}

If we want to be safe, we can also smush together the value ID and the value of the factor levels.

{{% codeblock %}}

```R
df_id_factor <- as_label(df, prefix = TRUE)
df_id_factor
```

{{% /codeblock %}}

The latter variant is not recommended though, as it it a bit tricky to get rid of the numbers in square brackets again.

{{% tip %}}

Behind the scenes, `sjlabelled` maintains the original level order. This is equivalent to fixing the level order when converting strings to [factors](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/factor) with the `levels=` argument.

{{% /tip %}}

## Assigning labels to data

### Storing and reassigning labels

The most common types of data frames, such as tibbles and data.tables should all support variable and value labels. Still, depending on your analysis it can happen that you lose the labels in the process. In that case, you can simply store the labels in a separate object at the beginning of the analysis and re-assign them at the end.

{{% codeblock %}}

```R
# Store the labels
variable_labels <- get_label(df) # returns a named vector
value_labels <- get_labels(df) # retuns a named list of named vectors

# Simulate some analysis that drops all labels
df_processed <- remove_all_labels(df_factor)
```

{{% /codeblock %}}

This data frame does not carry any labels anymore, just like a "normal" R dataframe. Let's try to re-assign the variable labels we stored in a variable. We can use `var_labels()` and `val_labels()` to to do that. Both functions accept name-value pairs as arguments, one per variable to be labelled. However, we can splice a named vector to a list of arguments for `var_labels()` with [!!!](https://www.rdocumentation.org/packages/rlang/versions/0.1/topics/quasiquotation). `!!!variable_labels` is equivalent to `var1 = label1, var2 = label2, …`

{{% codeblock %}}

```R
df_processed |>
  var_labels(!!!variable_labels) |>
  get_label()
```

{{% /codeblock %}}

Analogously, we can re-assign the value labels:

{{% codeblock %}}

```R
df_processed |>
  val_labels(!!!value_labels) |>
  get_labels()
```

{{% /codeblock %}}

Now let's fully re-label the "processed" dataframe. As you saw before, both `var_labels()` and `val_labels()` can be used with `dplyr` syntax. Note that with this syntax, the order of columns doesn't matter, and we can even reorder them before re-assigning the labels.

{{% codeblock %}}

```R
df_proc_relabelled <- df_processed |>
  select(order(colnames(df_processed))) |> # order the columns alphabetically
  var_labels(!!!variable_labels) |>
  val_labels(!!!value_labels)
```

{{% /codeblock %}}

Both `var_labels()` and `val_labels()` automatically skip variables that are given in the arguments that aren't present in the dataframe. However, this will produce a warning:

{{% codeblock %}}

```R
df_processed |>
  select(!e15relat) |> # removes the `e15relat` variable
  var_labels(!!!(variable_labels)) |>
  get_label()

# Warning: Following elements are no valid column names in `x`: e15relat
```

{{% /codeblock %}}

If you don't want the warning, you can create a makeshift version of `any_of()` for this case that only considers variables that exist in the dataframe. This blows up the syntax quite a bit, though.

{{% codeblock %}}

```R
df_processed |>
  select(!e15relat) |>
  var_labels(!!!(variable_labels[names(variable_labels) %in% colnames(.data)]))
```

{{% /codeblock %}}

To make things more concise, we can use a convenience function:

{{% codeblock %}}

```R
which_exist <- function(variable_labels) {
  variable_labels[names(variable_labels) %in% colnames(.data)]
}

df_processed |>
  select(!e15relat) |>
  var_labels(!!!(which_exist(variable_labels)))
```

{{% /codeblock %}}

If you happen to find a better way to only consider variables that exist in the dataframe, please [let us know](https://tilburgsciencehub.com/topics/collaborate-share/project-management/engage-open-science/contribute-to-tilburg-science-hub/contribute/)!

### Labeling data

Another operation you might want to do is to label previously unlabeled data. Let's use `mtcars` as an example:

{{% codeblock %}}

```R
# verify that this dataset does not have labels
get_label(mtcars) |> head()
```

{{% /codeblock %}}

Let's assign the variable labels that are given in the documentation in `?mtcars`

{{% codeblock %}}

```R
mtcars_var_labels <- c(
  mpg = "Miles/(US) gallon",
  cyl = "Number of cylinders",
  disp = "Displacement (cu.in.)",
  hp = "Gross horsepower",
  drat = "Rear axle ratio",
  wt = "Weight (1000 lbs)",
  qsec = "1/4 mile time",
  vs = "Engine (0 = V-shaped, 1 = straight)",
  am = "Transmission (0 = automatic, 1 = manual)",
  gear = "Number of forward gears",
  carb = "Number of carburetors"
)
mtcars_labelled <- mtcars |>
  var_labels(!!!(mtcars_var_labels))
```

{{% /codeblock %}}

We could also assign value labels to `vs` and `am`, but let's leave that for now.

## Nominal and ordinal measures

### Converting between nominal and ordinal data

SPSS knows two types of categorical measures, nominal and ordinal. In R, this distinction is made with a flag which indicates whether the data is ordered or not. Note that `sjlabelled::read_spss()` reads all factor columns with this flag set to `FALSE`, which means you'll have to retag ordinal variables yourself. To do that, you can use `as.ordered()`

{{% codeblock %}}

```R
df$c82cop1 <- as.ordered(df$e42dep)
```

{{% /codeblock %}}

`as.ordered` only works on vectors though. To use it on a dataframe, we can define a convenience function that works on selected columns of a dataframe. With the `{{ cols }}` syntax, we ensure the function supports tidyselect syntax.

{{% codeblock %}}

```R
as_ordered_cols <- function(df, cols) {
  df |> mutate(across({{ cols }}, as.ordered))
}
```

{{% /codeblock %}}

We can then perform conditional operations based on the `ordered` flag:

{{% codeblock %}}

```R
# flag all variables related to coping ("cop") are ordinal data
df_processed_ordered <- df_processed |>
  as_ordered_cols(contains("cop"))

df_processed_ordered |>
  select(where(is.ordered))
```

{{% /codeblock %}}

To convert factors back to unordered (i.e. nominal) ones, you can use:

{{% codeblock %}}

```r
df$c82cop1 <- factor(df$c82cop1, ordered = FALSE)
```

{{% /codeblock %}}

### Quantitative statistics on ordinal data

Sometimes ordinal data is interpreted as numerical data. One example for this is questionnaire data, several related questions are grouped together and the numerical levels are used to perform quantitative statistics. To do this, we need to replace the values of factors with their corresponding numeric level identifier. In `sjlabelled`, we can do that with the `as_numeric()` function.

{{% codeblock %}}

```R
df_processed |> print() # text levels
df_processed_numeric <- df_processed |>
  as_numeric() |>
  print() # numeric levels, the text levels are stored in the value labels
```

{{% /codeblock %}}

If you want to have the numbers start from 0 or a different value, you can provide `as_numeric()` with the `start.at =` argument.

We can now perform statistical operations. By calling `rowwise()`, we can ensure that the functions are applied per observation/participant and not on the whole column. Let's compute a custom score that summarizes all positive measures of the care for the elderly:

{{% codeblock %}}

```R
df_processed_numeric |>
  select(c(c82cop1, c89cop8, c90cop9)) |> # positive measures
  rowwise() |>
  mutate(
    positive_score = mean(c(c82cop1, c89cop8, c90cop9))
  )
```

{{% /codeblock %}}

## Export data back to SPSS

After we imported the SPSS file, we can clean and analyze the data as we normally would. Afterwards, we can save it either as a `.csv` or we can go back to a `.sav` file. In the latter case we need to go back to the SPSS standard, i.e. keep the _variable labels_ and replace factors with numerical IDs plus corresponding value labels. Conveniently, both can be done automatically in R! This is the only time that we will be using a function that is not part of `sjlabelled`, but the `haven` package. We don't recommend attaching `haven` with `library()`, though. Instead we will be calling it with the `::` notation. Factor columns will be treated as nominal measures by default, so make sure to flag ordered variables (e.g. with our custom function `as_ordered_cols()`) before exporting.

{{% codeblock %}}

```R
df_factor |>
  as_ordered_cols(contains("cop")) |>
  haven::write_sav("data/df_processed.sav")
```

{{% /codeblock %}}

`sjlabelled` has is own function to export `.sav` files which is a wrapper for `haven`'s `write_sav()`. It is, however, less flexible in practice, so `haven`'s version is recommended.

If you want to export the numeric version of the dataframe, make sure to convert it to factors first with `as_label()`. `write_sav()` actually ignores the value labels, so the corresponding text needs to be in the factor levels.

{{% codeblock %}}

```R
df_processed_numeric |>
  as_ordered_cols(contains("cop")) |>
  as_label() |>
  haven::write_sav("data/df_processed_num.sav")
```

{{% /codeblock %}}

## Summary

Here are the key takeaways from this building block:

- You can seamlessly work with both SPSS and R for your labelled data
- We recommend the `sjlabelled` package to handle SPSS (and labelled data in general) in R.
- Labelled data can have **variable** and **value** labels (aka levels).
  - Use `get_label()` to inspect the **variable** labels.
  - Use `get_labels()` to inspect the **value** labels.
- Use `as_label()` to replace the numerical level IDs with the text levels.
- To assign labels to the data with `dplyr`-syntax use
  - `var_labels(!!!variable_labels)`
  - `val_lables(!!!value_labels)`
  - `variable_labels` and `value_labels` are (nested) named lists with column name-label pairs
- Use `as.ordered()` to transfer categorical data to ordinal data.
- Use `as_numeric()` on ordinal data to before applying quantitative statistics.
- Use `haven::write_sav()` to export the data as SPSS files.
