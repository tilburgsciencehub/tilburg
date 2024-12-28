---
tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
indexexclude: "true"
weight: 9
title: "Wrap-Up"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /wrap-up/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/finish/
---

## You did it!

**Congrats!!!** You've finished our tutorial, and are now officially
hooked to `make`.

![Congrats](https://media.giphy.com/media/D0EjguuQzYr9m/giphy.gif)

Well, all fun aside, we hope you found this tutorial useful.

Of course, this is just one way in which to increase your research productivity. Here on tilburgsciencehub.com, we have more stuff available, so take your time to browse the page.

Oh, and to be complete, here's a summary of what you've learnt.

**Thanks for following through! Good job!**

{{% summary %}}

Can you believe you all did this? See below for the (long list)

- You've cloned [our GitHub template for a reproducible textmining workflow](https://github.com/hannesdatta/textmining-workflow)
- You've verified your software setup (and probably spent a lot of
  time fixing it!)
- You've downloaded our template and ran your first workflow,
simply by typing `make` (or previewing it with `make -n`)
- Now the serious business started: you modified our scripts. Among others, you
    - removed the prototyping condition and parsed the entire data set
    - parsed more attributes (`.get('user').get('screen_name')`), and added more text mining
    metrics (e.g., word count - for a great overview about
      using text mining for research, see [here](https://journals.sagepub.com/doi/abs/10.1177/0022242919873106)[^1])
    - you even changed the URL of the actual data set to use and
    reproduced your analysis on that different dataset
    - modified R scripts and an RMarkdown document.
{{% /summary %}}

## Curious for more?

  - Revise our [workflow procedures](/topics/project-management/principles-of-project-setup-and-workflow-management/overview/)
  - Check out more [example projects and templates](/examples)
  - Getting deeper into `make`? Then use [this fantastic (open-source) book](https://www.oreilly.com/openbook/make3/book/index.csp)[^2].

[^1]:
    Berger, J., Humphreys, A., Ludwig, S., Moe, W. W., Netzer, O., & Schweidel, D. A. (2020). Uniting the Tribes: Using Text for Marketing Insight. *Journal of Marketing*, 84(1), 1–25. https://doi.org/10.1177/0022242919873106
[^2]:
    Mecklenburg, R. (2004). *Managing Projects with GNU Make: The Power of GNU Make for Building Anything.* O'Reilly Media, Inc. https://www.oreilly.com/openbook/make3/book/index.csp
