---
title: "The GitHub Workflow"
description: "GitHub flow is a lightweight, branch-based workflow. The GitHub flow is useful for everyone, not just developers."
keywords: "github, workflow tutorial, branch, pull, push, fork, share, commit, merge, peer review, git"
weight: 4
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /learn/github
  - /learn/workflow
  - /github/workflow
---

# Overview

As a project grows, managing the numerous code changes can become unwieldy. This is where **version control** comes into play as a fundamental aspect of a streamlined workflow.

This topic aims to make you familiar with the GitHub workflow by covering the following key areas:

- Introduction to Git and GitHub
- The GitHub workflow
  - Branching
  - Commits
  - Pull requests
  - Peer reviews
  - Merging
- Exceptions to the standard workflow

## Introduction to Git and GitHub

**Git** is an open-source version control system that tracks changes made to a project's codebase. This facilitates efficient collaboration by allowing all team members to work simultaneously on the latest project version or access previous versions to make changes.

[**GitHub**](https://www.github.com) is an online hosting service that not only provides version control but also offers tools for code backup, synchronization, and collaboration. It acts as a centralized hub for collaborative development.

This table provides a quick comparison of Git and GitHub:
{{%table%}}
| | Git | GitHub |
| --- | --- | --- |
| Environment | Installed locally | Entirely cloud-based |
| Functionality | Exclusively Source Code <br> Management (SCM) tasks, <br> like push, pull, commit, <br> fetch and merge | Serves as a centralised <br> location for uploading copies <br> of a Git repository. The GitHub <br> GUI also offers one access <br> control, collaboration <br> features, and other <br> project-management tools. |
| Ownership | Linux | Microsoft |
{{%/table%}}
Use this [topic](/learn/github) to get started with Git and GitHub.

## The GitHub workflow

In a nutshell, a standard GitHub workflow follows the **Branch-Commit-Push-Pull request-Merge (BCPPM)** pattern:

- All work on an issue happens in a separate repository _branch_.
- When work is done, the assigned contributor _commits_ the changes.
- The assignee creates a _pull request_, often involving peer review.
- Once review (if any) is complete, the changes are _merged_ into the main branch.

The default approach we follow is the [GitHub Flow](https://guides.github.com/introduction/flow/). This workflow model is explained in the rest of this topic.

{{% tip %}}
The [GitHub Cheatsheet](../images/github_cheatsheet_tsh.pdf) also summarizes this approach, so you can easily follow along or refresh your memory in case you ever forget a step in the workflow!
{{% /tip %}}

### Branching

- The assignee should create a new branch. This can be done in three ways: Use `git branch` or `git checkout -b` on the command line, click the "Add branch" icon on the GitHub desktop, or create the branch on the repository's GitHub page.

- If you are resolving an issue, you can use the "Create a branch" option under Development on the issue page. This will automatically link the branch to the issue.

  ![Create a branch for an issue.](../images/create-issue-branch.png)

- The issue branch should be named `issueXXX-description`, where `XX` is the GitHub issue number and `description` is a version of the issue title (e.g., `issue123-update-appx-figures`). The description can be more compact than the issue title itself, but should be comprehensive enough that other team members can understand what is being worked on in the branch.

{{% tip %}}
For complex issues, additional branches can be made off of the main issue branch. These should be named `issueXXX-description/sub-branch-description` (e.g., `issue123-update-appx-figures/refactor`) These sub-issue branches should be merged into the main issue branch before the main issue branch is merged back to the master branch.
{{% /tip %}}

### Commit

- All commits related to an issue should be made in its dedicated branch.

- Each commit should have a message in the format `#X Description of commit` where `X` is the GitHub issue number (e.g., "#123 Add first appendix figure").

- Any commit to master, that is merged to master, or that defines an issue deliverable should follow a complete run of the relevant build scripts (e.g., `make.py`).

{{% tip %}}
**Best commit message practices**

Crafting good commit messages is crucial to the history of work on a project being clear and readable.
A good commit message:

- should describe the purpose of the commit.
- should not be redundant with what Git is already recording ("Update code" or "Modify slides.lyx" are redundant; "Refactor estimate() function" and "Add robustness figure to slides" are better).
- should be written in sentence caps, use the imperative mood, and not end in a period ("#123 Revise abstract") not ("#123 abstract.").

[This post](https://chris.beams.io/posts/git-commit/) by Chris Beams has an excellent discussion of what makes a good commit message.
{{% /tip %}}

### Pull Requests

- When work on an issue is complete, the assignee should create a pull request by clicking `New Pull Request` on the page of the right branch.

- The title of the pull request should be `PR for #X: original_issue_title` where `X` is the Github issue number (e.g., "PR for #123: Update appendix figures").

- The description / first comment of the pull request should begin with a line that says `Closes #X` where `X` is the number the Github issue number (e.g., "Closes #123"). This will close the original Github issue and create a link in that issue to the pull request. Subsequent lines of the description can be used to provide instructions (if any) to the peer reviewer.

- The pull request should be assigned to the assignee of the original issue.

### Peer Reviews

If an issue requires **peer review**, the assignee should assign the reviewer(s) in the pull request. In this case the description / first comment of the pull request should provide instructions that define the scope of the peer review along with any information the reviewer will need to execute it efficiently.

Any issue that involves substantial changes to code should be peer reviewed by at least one other lab member, though it is ultimately up to the assignee's discretion whether or not to send the issue for peer review.

{{% tip %}}
The job of the peer reviewer **IS** to verify that:

- The deliverable is clear, complete, and conforms to the standards from the deliverables section [here](write-good-issues.md)
- Files committed to the repository conform to our organizational and code style rules
- Empirical and theoretical results are clear and appear correct

It is **NOT** typically the job of the peer reviewer to:

- go over every detail of the output and every line of code.

While for example commenting on fine points of code style from time to time is fine, this should not be the primary content of the peer review. When requesting peer review the assignee can request feedback in addition to the above: e.g., particular code or results that need a careful check.
{{% /tip %}}

{{% warning %}}

- All peer review comments should be made on the pull request itself, not on the original issue.

- Revision to the code and other files in the repository as part of the peer review process should be made in the original issue branch (`issueXXX_description`) since the pull request will automatically track changes made in the branch.
  {{% /warning %}}

### Merging

When peer review is complete, the output is finalized, and issue-specific content like the `/issue/` subdirectory has been deleted, the issue branch should be merged back to `master` using a [**squash** merge](https://help.github.com/articles/about-pull-request-merge-squashing/). You can normally perform this merge automatically from the pull request page on GitHub.

Once the merge is complete, you should delete the issue branch.

## Exceptions to the Standard Workflow

In some cases, we may use simpler workflows, for example by skipping the branch/merge steps and just committing directly to `master`. Here are a few exceptions:

1. **No issue branch:** It is permissible to skip the step of creating an issue branch and commit changes directly to `master` when all of the following are true:

- The issue is small in scope and will involve no more than a few commits
- No one else is likely to be working on the same content at the same time
- All commits follow complete runs of relevant build scripts (e.g., `make.py`)

{{% warning %}}
Separately, for some projects or repositories, we may decide to use a simplified workflow where we commit everything to `master` by default. This could happen, for example, if some co-authors are unfamiliar with `git` and prefer the simpler workflow. In such cases, we need to pay attention to avoid cases where many people will be working on the same content at the same time. We also impose a strict rule that all commits follow complete runs of `make.py`.
{{% /warning %}}

2. **No pull request:** It is permissible to skip the step of creating a pull request if an issue does not require pull review and no changes will be merged back to the master branch.

3. **No peer review:** It is permissible to skip the peer review step when the assignee is confident the output is correct and the issue involves no changes or only minor changes to the code that is being merged back to the repository.

{{% summary %}}
Mastering the GitHub workflow empowers effective collaboration and version control in your project journey. Follow the **Branch-Commit-Push-Pull Request-Merge (BCPPM)** pattern for organized collaboration. Branch for each issue, commit with meaningful messages, initiate pull requests, conduct peer reviews, and merge changes systematically.
{{% /summary %}}
