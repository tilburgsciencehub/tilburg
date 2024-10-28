---
title: "Use this Checklist to Improve Your Project's Structure and Efficiency"
description: "Audit data, create and organize efficient projects."
weight: 1
keywords: "make, makefile, automation, recipes, checklist, project, plan, workflow, project organization, code structure, project checklist"
date: 2021-01-06T22:01:14+05:30 #updated 2023-08-12
aliases:
  - "/audit/workflow-checklist"
  - "/audit/organize-your-projects"
---

## Learning Goals

- Understand the essential guidelines to structure and maintain a well-organized project.
- Learn best practices for efficient and reproducible project workflows.

## Overview

As projects progress, they can become disorganized and difficult to navigate. A structured approach not only facilitates collaboration and understanding but also ensures that the project remains efficient and reproducible.

This building block offers a comprehensive checklist to guide you towards achieving this goal.

## Checklist

### Project level

Foundational guidelines that are essential for setting up any project, ensuring clarity and effective organization from the outset:

- Implement a consistent [directory structure](/topics/project-management/principles-of-project-setup-and-workflow-management/directories/#working-example): `data/src/gen`.
- Include [readme](/topics/project-management/principles-of-project-setup-and-workflow-management/documenting-code/#main-project-documentation) with project description and technical instructions on how to run/build the project.
- Store any authentication credentials outside of the repository (e.g., in a JSON file), and **not** in clear-text within the source code.
- Mirror your `/data` folder to a secure backup location. Alternatively, store all raw data on a secure server and download the relevant files to `/data`.

### Throughout the Pipeline

#### File/directory structure

Ensuring that your data, code, and results are systematically arranged, makes it easier to track changes and debug issues.

- Create subdirectory for source code: `/src/[pipeline-stage-name]/`.
- Establish subdirectories within `/gen/[pipeline-stage-name]/` for generated files: `temp`, `output`, and `audit`.
- Ensure file names are relative and not absolute. For instance, avoid references like `C:/mydata/myproject`, and opt for relative paths such as `../output`.
- Structure directories using your source code or use [.gitkeep](https://www.freecodecamp.org/news/what-is-gitkeep/).

#### Automation & documentation

Ensuring smooth automation alongside clear documentation streamlines project workflows and aids clarity.

- Make sure to have a [`makefile`](/automate/project-setup) to allow for automation.
- Alternatively, include a [readme](/topics/project-management/principles-of-project-setup-and-workflow-management/documenting-code/#main-project-documentation) with running instructions.
- Delineate dependencies between the source code and files-to-be-built explicitly. This allows `make` to automatically recognize when a rule is redundant, ensuring you define targets and source files properly.
- Include a function to delete `temp`, `output` files, and `audit` files in makefile when necessary.

#### Versioning

Versioning guarantees that changes in your project are trackable, providing a foundation for collaboration and recovery of previous work states.

- Track and version all source code stored in `/src` (e.g., add to Git/GitHub).
- Do not version any files in `/data` and `/gen`. They should **not** be added to Git/GitHub.
- If there are specific files or directories you wish to exclude, especially those unintentionally written to `/src`, utilize [.gitignore](https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/) to keep them unversioned.

{{% warning %}}
**Do not version sesitive data**

Before making a GitHub repository public, we recommend you check that you have not stored any sensitive information in it, such as any passwords.
You can use [GitHub credentials scanner](https://geekflare.com/github-credentials-scanner/) if you want to make sure.
{{% /warning %}}

#### Housekeeping

A tidy codebase is instrumental for collaborations and future adjustments. Proper housekeeping practices ensure code readability, maintainability, and efficient debugging.

- Opt for concise and descriptive variable names.
- Wherever possible, employ loops to reduce redundancy.
- Break down extensive source code into subprograms, functions, or divide them into smaller focused scripts.
- Prune unnecessary components such as redundant comments, outdated library calls, and unused variables.
- Implement asserts to stop program execution when encountering unhandled errors, ensuring robustness.

#### Testing for portability

Ensuring your project works across different environments and systems is crucial for consistent results and wider usability.

- On Your Computer:

  - Rebuild Test: Clear `/gen` and rebuild using `make`.
  - Clone & Build: Clone to a new directory, then rebuild using `make`.

- Different Systems:
  - Confirm functionality on Windows OS, Mac setup and Linux.

#### Example of a well-organized project

[This tutorial](/topics/project-management/principles-of-project-setup-and-workflow-management/overview/) covers the fundamental principles of project setup and workflows underlying this checklist. Under the _Summary_ section, you will find a visual example of a well-structure project display.

{{% tip %}}
To quickly visualize the structure of your project directories in a tree-like format, you can utilize the `tree` command in your terminal or command prompt.
{{% /tip %}}

## Additional Resources

- Tutorial about [Pipeline Automation using Make](../../../Automation/automation-tools/Makefiles/practicing-pipeline-automation-make/pipeline-automation-overview.md).
- Free open-source Master level course on [Data Preparation and Workflow Management](https://dprep.hannesdatta.com/).
- Reading about an example of a [Digital Project Folder Structure](https://medium.com/@dcbryan/staying-organized-a-project-folder-structure-7764651ff89f).
