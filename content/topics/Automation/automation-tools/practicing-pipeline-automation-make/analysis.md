---
tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
indexexclude: "true"
weight: 8
title: "Extending the Analysis"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /analyze/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/analysis
---

## Let's modify the analysis

We're done with the `data-preparation` pipeline for now, and turn our
attention to the `analysis` part of our project.

Admittedly, there's not much here yet. Try fiddling around with the files a bit
when you proceed to our practice questions and answers below.

Now let's continue with a couple of modifications. You can directly start working on the practice questions below.

### Practice questions and answers

1) Recall the powerful `makefile` we've introduced to you a while ago? Well,
open the `makefile` in `src/analysis/` now and try to understand
the steps of this stage of the pipeline! What happens, exactly?

2) Let's open `preclean.R` (e.g., in RStudio). Try to understand
what this script does. Then, filter the data only for tweets with
`polarity>0`.

3) Last, provide some summary statistics (`summary(dt$nwords)`) of the
word count, and produce a histogram `hist(dt$nwords)` of it in the
RMarkdown document.

## Watch the solution here

{{< youtube GI3CmKFSUQk iframe-video-margins >}}
