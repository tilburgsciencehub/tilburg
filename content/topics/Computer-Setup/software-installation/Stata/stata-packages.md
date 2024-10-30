---
title: "Install Stata Packages"
description: "Learn how to install Stata packages"
keywords: "stata, packages, ssc, ado"
#date: 2023-06-05T22:02:51+05:30
draft: false
weight: 4
aliases:
  - /get/stata-packages
  - /install/stata-packages
---

## What are Stata packages

Stata packages are user-contributed programs or commands that expand the capabilities of the Stata statistical software. They provide additional tools for tasks like data analysis, econometrics, and visualization, enhancing Stata's built-in features.

## Installing Stata packages from SSC

Installing packages from SSC is straight forward. For example if you wish to install `egenemore` package:

{{% codeblock %}}

```Stata
ssc install egenmore
```

{{% /codeblock %}}

### Installing community-contributed packages

While packages are regularly being added to SSC, in some cases you may need a package that has not been yet added but is available online. For example using `rdmulti` package for [regression discontinuity estimation](https://tilburgsciencehub.com/topics/analyze/causal-inference/did/impact-evaluation/).

{{% codeblock %}}

```Stata
net install rdmulti, from(https://raw.githubusercontent.com/rdpackages/rdmulti/master/stata) replace
```

{{% /codeblock %}}

If you are searching for the package but are unsure how to get the correct path; or alternatively if you are searching for packages that can help you in some specific application, the `search` command comes in handy.

{{% codeblock %}}

```Stata
search rdmulti
* Helps you find the installation path for rdmulti

search venn
* Lists packages that may be helpful for producing Venn diagrams
```

{{% /codeblock %}}

### Installing packages from .ado files

If you wish to manually install a package using an .ado file, for example using work from a colleague that may not be available online you should just copy the ado file into your personal ado folder. To find the path for your personal folder, use either `sysdir` or `personal`.

{{% codeblock %}}

```Stata
sysdir
* Provides different system directories, including personal ado folder

personal
* Provides path to personal ado folder
```

{{% /codeblock %}}
