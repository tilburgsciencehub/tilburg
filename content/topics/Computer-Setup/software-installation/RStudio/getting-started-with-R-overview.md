---
title: "Get Started With R"
description: "Learn to code in R"
keywords: "learn, R, resources, R packages, installation,style, code, R, guidelines, best practices, packrat, package management system, setup, RStudio, programming, coding"
weight: 2
date: 2022-09-07T22:02:51+05:30
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /learn/r
  - /start/r
  - /topics/reproducible-research/getting-started-with-r/
  - /topics/code-like-a-pro/getting-started-with-r/
---

## Overview: Why R?

<a href= '../images/r-perks.png' target="blank"> <img src="../images/r-perks.png" alt="overview of perks R offers" width="300" style="float:right;"></a>

Whether you’re looking to start coding for a new career or just as a hobby, choosing your first programming language can be a daunting task. There is no one-size-fits-all answer—it depends on the type of project you’ll work on, what is demanded on the job, etc. However, R stands out with several appealing benefits.

Chances are, sooner or later, you'll encounter R, one of the most popular (if not _the_) statistical programming languages worldwide. R's popularity isn't just because it's free; it's also due to the global community that uses, documents, and continually improves it.

{{% warning %}}

The R interface might seem intimidating at first, especially if you're used to using Excel to do your data magic. But trust us, investing time in learning R will pay off greatly, not just in your grad school career, but also in your industry career. R, alongside Python, has become a standard skill for jobs in marketing analytics and data science.

{{% /warning %}}

One of the best things about R is the _wide range of learning resources available_. However, with so many options, it can be hard to know where to start. This guide offers the right starting point and the resources to help you learn R efficiently, including the following topics:

- Tips for learning R efficiently
- Learn advanced R
- Reproducible workflows in R
- How to manage R packages
- Analysis in R: Examples
- Communicate your insights: Publish e-books and interactive articles directly from R
- Building webpages with R

{{% tip %}}

_Set up R and RStudio_

Your first step is to set up R and RStudio on your local machine, following our [R/R Studio installation guide](/topics/computer-setup/software-installation/rstudio/r/).

{{% /tip %}}

## Tips for learning R efficiently

Here are a few tips to learn R efficiently:

- Have a project!

  "Huh - why to have a project? I first need to learn R!"

  Well, if you _really_ want to learn R, you should already have a project in mind that you would like to tackle. R is a powerful tool, and without a clear goal, you might feel overwhelmed. If you don't have a specific project, and still would like to learn R, consider finding an interesting dataset to work with, like those available on [Kaggle.com](https://www.kaggle.com).

- Enroll in R courses at [Datacamp](https://www.datacamp.com/). It is free with a Tilburg University account!

  - For _beginners_:
    - [Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r)
    - [Intermediate R](https://www.datacamp.com/courses/intermediate-r)
  - For _data management_ and _preparing your own datasets_:
    - Learn _data.table_, our preferred tool for handling large datasets. Just
      search for _data.table_ at datacamp.com. These are our favorite courses:
      - [Data manipulation with data.table](https://www.datacamp.com/courses/data-manipulation-in-r-with-datatable)
      - [Joining data with data.table](https://www.datacamp.com/courses/joining-data-in-r-with-datatable)
    - Explore _Tidyverse_, a collection of tools that simplify data tasks. Our top pick is: [Introduction to Tidyverse](https://www.datacamp.com/courses/introduction-to-the-tidyverse)

- Learning your _method_
  - Once your data is prepped, you can begin analyzing it. The method you choose will depend on your specific research question. For many students, a refresher in [regression analysis](https://www.datacamp.com/courses/intermediate-regression-in-r)— such as Ordinary Least Squares (OLS) or Logistic Regression (Logit)—may be particularly useful.

## Learn Advanced R

Want to learn more _advanced programming_ with R? Check out the [digital version](https://adv-r.hadley.nz/index.html) of the book: “Advanced R”, in Chapman & Hall’s R Series.

## Mastering Reproducible Workflows with R

Want to learn the essential skills for _reproducible research_ and open science in R? This [book](https://psyteachr.github.io/reprores-v2/index.html) covers a wide range of topics such as:

- [Reproducible Workflows](https://psyteachr.github.io/reprores-v2/repro.html)
- Data visualization, e.g. [styling plots](https://psyteachr.github.io/reprores-v2/plotstyle.html)
- [Data Wrangling](https://psyteachr.github.io/reprores-v2/dplyr.html)

Also, explore the [materials](https://github.com/debruine/msc-data-skills) from the University of Glasgow's MSc course in [Data Skills for Reproducible Science](https://psyteachr.github.io/msc-data-skills/index.html).

## Managing R Packages

Packages in R are collections of functions, data, and code bundled together and stored in a ‘library’. While R comes with a standard set of packages, you can install additional ones as needed. As your projects grow, managing packages can become complex. Use this [code snippet](/topics/automation/replicability/package-management/auto-install-r-packages/) to automatically install any packages you may need.

For effective package management, consider using _Packrat_. This tool helps avoid dependency issues by isolating R packages, making them portable, ensuring project reproducibility. This is especially useful when working on multiple projects or across different machines with different versions of packages installed. Learn more in [our comprehensive guide to Packrat](/topics/automation/replicability/package-management/packrat/)

## Analysis with R: Examples

Got a hang of the R syntax and are looking to put your R coding skills to practice with some empirical project? Here are some guides and code examples for commonly used techniques for descriptive and causal analysis.

- [Run a regression analysis](/topics/analyze/regression/linear-regression/regression-analysis/)
- [Impact evaluation with Difference-in-Differences and Regression Discontinuity](/topics/analyze/causal-inference/did/impact-evaluation/)
- [Synthetic control analysis](/topics/analyze/causal-inference/synthetic-control/synth-control/)

## Communicate insights with R

One of the most important and challenging jobs of a researcher is communicating one’s findings to non-technical stakeholders in an appealing way. R facilitates creative ways to present your insights through interactive dashboards (R Shiny), and tools like Distill, Bookdown, and Quarto for publishing content (e.g., e-books, slides, articles) directly to the web from R.

Want to try it yourself? Here are some resources to help you get started:

- [Build Interactive dashboards with R shiny](/topics/visualization/data-visualization/dashboarding/shiny-apps/)
- [Publish e-books and interactive articles directly from R](/topics/collaborate-share/share-your-work/content-creation/using-r/)

## Building Webpages with R

Interested in creating a webpage with R? Check out this [guide](https://debruine.github.io/tutorials/webpages.html).

For _interactive webpages_ with R, you can easily create them using [webexercises](https://debruine.github.io/webexercises/).

{{% summary %}}

R is a powerful statistical language with extensive resources that make it a top choice for data analysis. This guide helps you get started with R by covering setup, efficient learnign tips, advanced techniques, package management, reproducible research, and methods for communicating your insights.

Continue your journey by learning to code in R following [proper coding style guidelines](/topics/computer-setup/software-installation/rstudio/r-code-style/).

{{% /summary %}}
