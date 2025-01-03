---
# tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
indexexclude: "true"
weight: 7
title: "More Modifications"
keywords: "modifications, branching"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /modify/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/modifications
---

## More modifications, branching, and replacing input files

Now let's continue with a couple of advanced modifications to our workflow. We hope these convince you about the potential efficiency gains you can expect when working on data-intensive projects!

This time, you can directly start working on the practice questions below. Also take note of our additional explanations for each question.

### Practice questions and answers

1) Please open `textmining.py`, and also provide the word count as an additional column. Tip: use `len(blob.words)` to obtain the word count of the `blob` variable.

2) Let's now swap the name of the JSON file name to `fortnite_event_1.json` (in parse.py). Re-run the workflow and compare the final output in `/gen/analysis/output`.

{{% tip %}}
**Branching.**
Working with reproducible workflows enables you to easily compare the results of one workflow with those of another (modified) one. Think about the question above: *comparing* the results of our results on `fortnite_allevent.json` with those obtained on `fortnite_event_1.json`.

In practice, we make use of the concept of "branching".

  - There's one very elegant way to do this using Git (but we don't cover that one here).
  - The more "clumsy" way of going about is to *work in a copy of your entire project directory* to see what your modifications will do.

    - Yes, you've heard correctly: just copy-paste your entire project infrastructure and then do the modifications there and run `make`.
    - You now have two main directories on your system and you can directly compare the output of the two `analysis.html` files in `my_project/gen/analysis/output` and `my_project - copy/gen/analysis/output/`.
{{% /tip %}}

3) Last, try to replace the download URL in `download.py` with a different raw data set, available at
`"https://uvt-public.s3.eu-central-1.amazonaws.com/data/trump_disinfectant.zip"`, and run the entire workflow again. Remember to adjust subsequent scripts!!!

{{% tip %}}
**Returning back to our "head revision".**

In question #2 above, we've "branched out" to understand the implications of modifying the event of interest (JSON file). In this part of the practice questions, we're returning back to our "main repository" - or, in *reproducible-science slang*, the "head revision" of our project. A head revision is always the main version of the project. Think about it as your master copy.

{{% /tip %}}

## Watch the solutions to all questions here

{{< youtube IjHKc6oOIUU iframe-video-margins >}}
