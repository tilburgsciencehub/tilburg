---
# tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
title: "Pipeline Automation Overview"
description: "Follow our tutorial to implement a fully automated workflow to conduct sentiment analysis on tweets."
keywords: "tutorial, tweets, sentiment, analysis, workflow"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 1
aliases:
  - /practice/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/pipeline-automation-overview
  - /topics/reproducible-research-and-automation/practicing-pipeline-automation-make/_index
  - /topics/other-category/implement-an-efficient-and-reproducible-workflow/workflow/pipeline.md
---

Longing to put your knowledge from our [workflow guide](/topics/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/project-setup-overview/) into practice? Then follow this tutorial to implement a fully automated workflow to conduct sentiment analysis on tweets, using our [GitHub workflow template](https://github.com/hannesdatta/textmining-workflow).

## Objectives of this tutorial

-	Familiarize yourself with a [robust directory structure](/topics/project-management/principles-of-project-setup-and-workflow-management/directories/) for data-intensive projects
-	Experience the benefits of [automating workflows with makefiles/GNU make](/topics/project-management/principles-of-project-setup-and-workflow-management/automation/)
-	Learn to use Git templates for your own research projects
-	Adjust the workflow template to
    -	...download different datasets from the web
    - ...unzip data automatically
    -	...parse JSON objects and select relevant attributes
    - ...add new text mining metrics to the final data set using Python's `textblob`
    - ...modify the analysis in an RMarkdown/html document

## Prerequisites

-	Computer setup following our [setup instructions](/topics/computer-setup/software-installation/#software-installation-ezo/).
    - [Python](/install/python) and the `textblob` package

        ```
        pip install -U textblob
        ```

        Then, open Python in the terminal by typing `python`, and type

        ```
        import nltk
        nltk.download('punkt')
        ```

        If you receive an error message, please verify you are typing this command in python, and not *directly* in the terminal/Anaconda prompt.

    -	[R, RStudio](/install/r) and the following packages:

        ```
        install.packages(c("data.table", "knitr", "Rcpp", "ggplot2", "rmarkdown"))
        ```

        When installing the packages, R may ask you to select a "CRAN-Mirror". This is the location of the package repository from which R seeks to download the packages. Either pick `0-Cloud`, or manually choose any of the location nearest to your current geographical location.

{{% warning %}}
  **R 4.0**.
  Newer versions of R (>=R 4.0) may require you to download additional packages.

  ```
  install.packages(c("rlang", "pillar"))
  ```

  - If you're being asked whether to build these packages from source or not [options: yes/no], select NO.

  - If you're being asked to install RTools, please do follow these installation instructions.
{{% /warning %}}

  -	[GNU Make](/install/make)

- Familiarity with our [workflows](/topics/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/project-setup-overview/), in particular on [pipelines and project components](/topics/project-management/principles-of-project-setup-and-workflow-management/pipeline/), [directory structure](/topics/project-management/principles-of-project-setup-and-workflow-management/directories/) and [pipeline automation](/topics/project-management/principles-of-project-setup-and-workflow-management/automation/).

-	Nice-to-haves:
    - Basic experience with Python and R
    -	Familiarity with common data operations using `data.table` in R
    -	Familiarity with text mining using Python and TextBlob
    - If you want to learn Git on the way...
        - Have Git installed on your computer (see [here](/install/git))
    	  - Have GitHub login credentials

## Disclaimer

To keep this tutorial as accessible as possible, it will mention Git/GitHub a few times, but assume you will acquire details on these skills elsewhere. In other words, versioning and contributing to Git repositories is not part of this tutorial.

<!-- to do:

add note what to put in make, and what to put in R-->
