---
tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
indexexclude: "true"
weight: 5
title: "Inspecting the Data-preparation Pipeline"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /makefile/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/pipeline-make/
---

## Makefile of the data-preparation pipeline

Up to now, we've learnt how to run `make` in our template. But we haven't really
learnt yet how the files in each of the particular pipeline stages are *actually*
run. So, let's now navigate to the `data-preparation` source code folder,
and explore the `makefile` a bit.

Please first try to answer our questions below, and then watch our solutions.

### Practice questions and answers

1) Inspect the syntax of the `makefile` in `src/data-preparation/`. At this stage,
only look at the *file names*, not at the *directory names*. Can you explain the structure of the syntax? Think about what has been "built" in `gen/data-preparation`, what files may have been necessary to build what is there, and last, how was the build actually made (e.g., executed on your system)?

2) Now let's inspect the full file names (i.e., file name *and* directory names). Mostly,
the directories start with `../..`. Can you explain why that is? What is really happening here?

## Watch the solutions here

{{< youtube PyoJ7RUfwds iframe-video-margins >}}
