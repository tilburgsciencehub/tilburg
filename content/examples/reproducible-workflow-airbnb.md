---
title: "A Reproducible Research Workflow with AirBnB Data"
date: 2020-11-11T22:01:14+05:30
draft: false
description: "A platform-independent, reproducible research workflow with AirBnB data, using Stata, Python and R."
keywords: "tisem, airbnb, template, workflow, example"
weight: 1
aliases:
  - /try/airbnb-workflow
---

## Overview

Using publicly available data from AirBnB (available via [Kaggle.com](https://www.kaggle.com/airbnb/boston)), we illustrate how a reproducible workflow may look like in practice.

{{% cta-primary-center "Check out the GitHub Repository" "https://github.com/tilburgsciencehub/airbnb-workflow" %}}

We've crafted this project to run:

- platform-independent (Mac, Linux, Windows)
- across a diverse set of software programs (Stata, Python, R)
- producing an entire (mock) paper, including modules that
  - download data from Kaggle,
  - prepare data for analysis,
  - run a simple analysis,
  - produce a paper with output tables and figures.

## How to run it

### Dependencies

- Install [Python](/get/python/).
  - Anaconda is recommended. [Download Anaconda](https://www.anaconda.com/download).
  - check availability: type `anaconda --version` in the command line.
- Install Kaggle package.
  - [Kaggle API](https://github.com/Kaggle/kaggle-api) instruction for installation and setup.
- Install [Automation tools](/get/make/).
  - GNU make: already installed in Mac and Linux OS. [Download Make](http://gnuwin32.sourceforge.net/packages/make.htm) for Windows OS and install.
  - Windows OS users only: make `Make` available via the command line.
    - Right Click on `Computer`
    - Go to `Property`, and click `Advanced System Settings `
    - Choose `Environment Variables`, and choose `Path` under the system variables, click `edit`
    - Add the bin of `Make`
  - check availability: type `make --version` in the command line.
- Install [Stata](/get/stata/).
  - making Stata available via the command line. [Instruction](/get/stata/) for adding Stata to path.
  - check availability: type `$STATA_BIN --version` in the command line.
- Install [Perl](/get/perl/).
  - Perl is already installed in Mac and Linux OS. [Download Perl](https://www.perl.org/get.html) for Windows OS.
  - Make sure Perl available via the command line.
  - check availability: type `perl -v` in the command line.
- Install [LyX](/get/latex/).
  - LyX is an open source document processor based on the LaTeX. [Download LyX](https://www.lyx.org/Download).
  - make sure LyX available via the command line.
  - check availability: type `$LYX_BIN` in the command line.

### Run it

Open your command line tool:

- Check whether your present working directory is `airbnb-workflow` by typing `pwd` in terminal
  - if not, type `cd yourpath/airbnb-workflow` to change your directory to `airbnb-workflow`
- Type `make` in the command line.

### Directory structure

Make sure `makefile` is put in the present working directory. The directory structure for the Airbnb project is shown below.

```text
├── data
├── gen
│   ├── analysis
│   │   ├── input
│   │   ├── output
│   │   │   ├── figure
│   │   │   ├── log
│   │   │   └── table
│   │   └── temp
│   ├── data_preparation
│   │   ├── audit
│   │   │   ├── figure
│   │   │   ├── log
│   │   │   └── table
│   │   ├── input
│   │   ├── output
│   │   │   ├── figure
│   │   │   ├── log
│   │   │   └── table
│   │   └── temp
│   └── paper
│       ├── input
│       ├── output
│       └── temp
└── src
    ├── analysis
    ├── data_preparation
    └── paper
```

- **gen**: all generated files such as tables, figures, logs.
  - Three parts: **data_preparation**, **analysis**, and **paper**.
  - **audit**: put the resulting log/tables/figures of audit program. It has three sub-folders: **figure**, **log**, and **table**.
  - **temp** : put the temporary files, such as some intermediate datasets. We may delete these filed in the end.
  - **output**: put results, including the generated figures in sub-folder **figure**, log files in sub-folder **log**, and tables in sub-folder **table**.
  - **input**: put all temporary input files
- **data**: all raw data.
- **src**: all source codes.
  - Three parts: **data_preparation**, **analysis**, and **paper** (including TeX files).

<!-- {{% codeblock %}}

[js-link](code.js)


```js
// some js code
var name = "Arvind Singh";

if (name == "arvind") {
	console.log("testing out coding blck");
}
```

```bash
# some bash code
# make-files.txt
touch test/john.txt
touch test/mike.txt
touch test/jenna.txt
```

{{% /codeblock %}} -->
