---
title: "Enhance Reproducibility and Automation with GitHub Actions"
description: "Explore GitHub Actions, a platform offering tools for custom workflows that boost project automation and reproducibility"
keywords: "GitHub Actions, Data Science, Project, Project Structure, Reproducibility, Automation, Testing, Formatting, Workflows, Runners, Jobs, Events"
weight: 2
author: "Diego Sanchez Perez"
authorlink: "https://www.linkedin.com/in/diego-s%C3%A1nchez-p%C3%A9rez-0097551b8/"
draft: false
date: 2023-05-23T22:01:14+05:30 #updated 2023-08-30
aliases:
  - /github_actions/introduction
---

## Overview

This building block introduces the fundamentals of GitHub Actions and how to integrate it into your project. It complements our previous guide on [data management and directory structure](https://tilburgsciencehub.com/topics/automation/workflows/starting/principles-of-project-setup-and-workflow-management/directories/#), which we strongly recommend you to check out if you haven't already!

As a result, you will:

- Understand the core concepts of GitHub Actions within a data science project.
- Familiarize yourself with its components, like events, jobs, runners, and workflows.

## Introducing GitHub Actions

[GitHub Actions](https://docs.github.com/en/actions) is GitHub's native platform for workflow automation. If your project is hosted in a GitHub repository, you can take advantage of it to define customized workflows that are automatically triggered when certain pre-specified conditions are met.

Some use case examples could include a workflow in charge of re-training your model and updating its results whenever you add new data to your project, running an automated code testing pipeline each time you push new code to your repository, or formatting and checking that your code structure adheres to certain desired standards. The great flexibility of GitHub Actions allows you to define your own customized workflows that can assist or automate most of your project's pipeline segments.

Moreover, GitHub Actions also offers many interesting advantages in terms of reproducibility. You can easily share your workflows, defined as `yaml` or `yml` files (file format employed by GitHub Actions), with anyone interested in reproducing your project's pipeline. Furthermore, GitHub Actions also generates logs every time a workflow is executed which can be very useful when it comes to reproducing and comparing your results.

{{% tip %}}
**Not familiar with Git/GitHub yet?**

Feel free to check out our building blocks on the topic [here](https://tilburgsciencehub.com/search/?q=GitHub). They contain all the information you need to get started!

{{% /tip %}}

## Understanding the main concepts

With GitHub Actions, workflows are defined through `yaml` files. These files contain the recipe for GitHub Actions to execute your workflow correctly. There are several key elements to a GitHub Actions workflow:

- **Events**: These are triggers for the workflow. Typically related to repository activity (like pull requests or commits), there are various other ways to start a workflow such as defining a periodical schedule or manual activation. More information on events can be found [here](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).

- **Jobs**: Once a workflow starts, it runs jobs, essentially, sets of steps. Each step involves an action or script directing the tasks for the workflow. Although jobs run independently and in parallel by default, the steps within a job run in sequence, depending on each other. Dive deeper into jobs with [GitHub's documentation on the topic](https://docs.github.com/en/actions/using-jobs).

- **Runners**: The runners are the servers where the jobs are executed once a workflow is triggered. GitHub offers runners based on Linux, Windows, or macOS. For intensive computational tasks not suited to GitHub’s runners, consider using your own high-capacity, self-hosted runner. If you want to learn further about it, keep an eye out for our future building block on the topic!

- **Actions**: Actions are probably one of the most interesting features of the GitHub Actions platform. They are custom applications that automatically perform certain relatively complex tasks within your workflow without you having to worry about the details of their implementation. These actions are run within the steps of your workflow's jobs and can take care of things such as automatically exporting your project's code to the runner to operate over it, setting up dependencies within the runner or automatically committing changes made in your project during the workflow.

  Typically, they are developed by GitHub's community and there is a large number of them available for you to use according to your needs, you can explore available actions by visiting [GitHub's marketplace](https://github.com/marketplace?type=actions).

<p align = "center">
<img src = "../images/wf_concept.png" width="700">
<figcaption> From left to right: Conceptual structure of a workflow file and its approximate appearance as an .yml file. </figcaption>
</p>

In the image above on the left you can see the conceptual structure of a GitHub Actions workflow, while on the right there is an example of how an actual workflow, a `yml` file, with the same proposed structure looks like approximately. This example workflow consists of two jobs, each one with three steps. Note how the workflow starts with the events that will trigger it (line 3 of the right-side image) right after the name given to the workflow.

After that the different jobs are defined, first, a runner is assigned to each of these (lines 7 and 21 from the right-side image) and then the corresponding steps are listed. You can include as many jobs within a workflow and steps within a job as you want as long as the runner can handle it, however, in this example things are kept simple so it is easier for you to familiarize yourself with the structure of a GitHub Actions workflow.

For that reason, this example workflow will not be explored in detail here. To learn more about how to build your own workflows and the details of how to do so we recommend you to check out our upcoming building block on the topic. There you will see how to design workflows using as a reference a popular implementation for these: a pipeline for code formatting and testing.

## Adapting your project structure

The first elementary pre-requisite to take advantage of GitHub Actions is that your project must be hosted in a GitHub repository. If this is the case, you should create a directory named `.github` at the root level of your project's repository, which in turn must contain another sub-directory called `workflows`.

This subdirectory is where you will place your workflow YAML files so GitHub can recognize them. You can give your workflows any name you want as long as the files containing these have the appropriate extension `.yml`.

<p align = "center">
<img src = "../images/wf_dir_structure.png" width="450">
<figcaption> Example of a project directory structure including GitHub Actions workflows. </figcaption>
</p>

In the displayed structure above, you can see the essential `.github/workflows/` directory for storing workflow `yml` files. This sits alongside standard directories like `data`, `gen`, and `src` that you might typically find in many research projects.

{{% summary %}}

**GitHub Actions** is GitHub's built-in platform designed for workflow automation. Within this system, the core components are defined using `yaml` or `yml` files which guide the automation process. These components include:

- **Events**, which serve as the catalysts, setting workflows into motion.
- **Jobs**, sequences of tasks that the workflow should undertake.
- **Runners**, which are the servers orchestrating the execution of these jobs.
- **Actions**, tailored automation tasks crafted for specific purposes.

To implement GitHub Actions into a project, one needs to integrate a special directory called `.github/workflows/` into the project's repository. Here, the workflow `yml` files are stored, allowing GitHub to detect and utilize them.

{{% /summary %}}

## Additional resources

- Github Actions [Documentation](https://docs.github.com/en/actions)
- [Workflow example](https://github.com/snpe-reputation-systems/snpe-reputation-systems/blob/master/.github/workflows/formatting-testing.yml) for code formatting and testing
