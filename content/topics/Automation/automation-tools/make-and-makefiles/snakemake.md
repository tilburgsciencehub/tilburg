---
title: "Set up Snakemake"
description: "Snakemake is an easy to use workflow management system. Learn how to install it."
keywords: "snakemake, build, build tool, workflow"
weight: 3
date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /get/snakemake
  - /install/snakemake
---

## What is Snakemake

[Snakemake](https://snakemake.readthedocs.io/en/stable/) is an easy to use workflow management system. Contrary to *make*, which was designed by computer scientists to build software, *snakemake* was designed for academic/professional research in Bioinformatics, so it may feel more intuitive for academic users.

Snakemake is a python package - so we can install using the default python installer, pip.

## Installing Snakemake

### Mac & Linux Users

In a terminal window enter the command:

```bash
pip install snakemake
```
followed by pressing the `Return` key.

Verify that your installation worked correctly by entering

```bash
snakemake --version
```
into a terminal and pressing `Return.`

The expected output is the current version on the software, which should be greater than

```bash
5.2.2
```

### Windows users

We need one extra step here. In a cygwin window enter the command:

```bash
conda install datrie
```

followed by pressing `Return`.

If you get an access denied error, you may have not clicked on single user install in the Anaconda installation. De- and re-install Anaconda and try again.

If the above command works, your terminal will look something like this:

```bash
The following NEW packages will be INSTALLED:
datrie: 0.7.1
proceed ([y]/n)
```

Type `y` and hit enter. Once this is done, type:

```bash
pip install snakemake
```

followed by pressing the `Return` key.

The expected output is the current version on the software, which should be greater than

```bash
5.2.2
```
