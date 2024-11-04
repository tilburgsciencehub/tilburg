---
title: "Find Keywords and Sentences from Multiple PDF Files"
#date: 2020-11-11T22:01:14+05:30
draft: false
description: "Docker application based on R that finds keywords and sentences from PDF files "
keywords: "keywords, finder, PDF, R, Docker, application"
weight: 5
aliases:
  - /keywords-finder/docker/PDF
---

## Overview

This is a template for a reproducible [Dockerized](https://tilburgsciencehub.com/topics/automation/replicability/docker/docker/) application, based on [R](https://tilburgsciencehub.com/topics/computer-setup/software-installation/rstudio/learn-r/), that **finds keywords and/or sentences in multiple `PDF` files**.

{{% summary %}}

- We use `R` to first, convert the `PDF` files into plain text files (`.txt`).
- Then, a second `R` script searches the keywords and/or sentences that are previously defined in those converted text files.
- Matches are reported into an Excel file, reporting what keyword or sentence was found in which file.
  {{% /summary %}}

`Docker` is used to run the above mentioned process inside an isolated container (_see [this building block](https://tilburgsciencehub.com/topics/automation/replicability/docker/install_docker/) to learn more about containers_). By doing so, you can run this application without even having to have `R` installed in your computer plus it will also run smoothly, regardless of what operating system (OS) you're using.

## Motivating Example

In many situations, we make use of `crtl (or "Command" in Mac) + F` to find words or sentences in `PDF` files. However, this can be highly time-consuming, especially if needed to apply in multiple files and/or different keywords or sentences. For instance, we first applied this application in legal research, where we needed to check in over 10,000 court rulings, which ones made reference to a specific law.

## Get The Workflow

Need to find keywords or sentences from multiple PDF files? Clone our repository to your local machine and add your `PDF` files and keywords to get started:
{{% cta-primary-center "Go to the GitHub Repository" "https://github.com/tilburgsciencehub/keywords-finder" %}}
