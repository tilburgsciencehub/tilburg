---
title: "Contribute to Open Source Projects"
description: "Learn how to contribute to open source projects published on GitHub."
weight: 4
keywords: "github, open source, pull request, collaborate, contribute, git, repository, forking, cloning, science, project, contribution"
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /learn/git-collaborate
  - /learn/git-pr
  - /learn/pullrequest
  - /pullrequests
  - /pullrequest
---

# Overview

Ever wondered how to contribute to open source projects on GitHub? This building block will go through this process step-by-step to prepare you for your first meaningful open source contribution!

1.  Get familiar with the repository
2.  Run the code
3.  Make changes
4.  Submit your contribution

## Step 1: Get familiar with the repository

Familiarize yourself with the repository to which you want to contribute.

- Typically, each repository has a README with general instructions on what the repository is about (and how to run the code).
- Also, new features and bugs are discussed at the repository’s _Issues_ page.
- Finally, many repositories contain a discussion forum and project board (called _Projects_) in which you can learn about the roadmap of the project.

{{% example %}}
For example, visit the [repository of Tilburg Science Hub](https://github.com/tilburgsciencehub/tsh-website).

- Browse through the repository’s README (the first file you see when you click on the link above)
- Head over to the issue page: click on the _Issues_ tab.
- View the project/discussion boards: you can find this through the _Projects_ tab.

Can you identify ways in which to contribute to the project?

{{% /example %}}

## Step 2: Run the code

After installing the required software, you need to run the code to see whether you can test your changes to the project later.

- Open the repository on GitHub, and fork it (click on the _fork_ button in the upper right corner on GitHub). This creates a copy of the code in your GitHub account.

- Clone your own forked repository to the disk. You can do this with `git clone`. The example code below shows how to clone a fork of the Tilburg Science Hub website. (Replace your user name.)

{{% codeblock %}}

```bash
 git clone https://github.com/[your-user-name]/tsh-website
```

{{% /codeblock %}}

- Enter the directory of the cloned repository, and run the code.

## Step 3: Make changes

Find something that you want to add to the project, or fix! Each new feature that you introduce needs to be developed in a separate branch. This allows the repository owner to carefully screen which parts of the project to add to the public version of the main project. The websites are written in Markdown, and you can easily add or change the content.

1. Create a new branch

{{% codeblock %}}

```bash
git branch name-of-a-new-feature
```

{{% /codeblock %}}

2. Work on your new feature. Throughout, apply the Git workflow: `git status`, `git add`, `git commit -m "commit message"`. For more information on Git Commands, read this [building block](/topics/contribute-and-share-your-work/most-important-git-commands/).

3. When you’re done with all of your changes, push your changes to your GitHub repository.

{{% codeblock %}}

```bash
git push -u origin name-of-a-new-feature
```

{{% /codeblock %}}

At this stage, your changes are visible in your forked copy of the repository. The repository owner of the main project doesn't know about these changes yet.

{{% tip %}}
**Preview the Tilburg Science Hub website**

When contributing to Tilburg Science Hub, it is very useful to preview changes and see how they will look on the website.

- First, install Hugo. If you don't have Hugo installed, follow the tutorial [Get Hugo](https://tilburgsciencehub.com/topics/collaborate-share/share-your-work/content-creation/hugo-website/get-hugo/).

- Navigate to the repository cloned on your local machine. You can do this in two ways: navigate to this repository first and then open the Command Prompt here, or open the Command Prompt first and type `cd` followed by the Path to this repository. (The example uses the first option.)

- Type `hugo server` in the Command Prompt.

- The website can now be run locally. Paste the localhost link (http://localhost:xxxx/) in your browser to view the website with your changes.

<p align = "center">
<img src = "../images/hugoserver.png" width="400">
</p>

{{% /tip %}}

## Step 4: Submit your contribution

Fully done and happy with your changes? Then let the project owner know about your new, amazing feature by making a pull request (PR)!

1. Open your forked repository on GitHub, select the branch you've just edited, and click on "Pull request".

2. Carefully describe your changes. For example, describe the new feature you developed, why it is useful, how you've tested it, etcetera. Then submit your pull request.

3. The owner of the main repository will now review your changes, maybe request changes, and potentially integrate your new feature with the main project. Congrats on your first open source contribution!

{{% summary %}}
This guide takes you on a step-by-step explanation journey into open source contribution on GitHub:

1. **Get familiar**: Explore the repository, read the README page, and explore the _Issues_ and _Projects_ pages. You can find out how you can contribute.
2. **Run the code**: Fork the repository, clone it, and run the code. This sets the stage for your changes.
3. **Make changes**: Create a new branch, and make your changes by adding new content or changing existing content. You can use Git commands to manage these changes.
4. **Submit your contribution**: When satisfied, initiate a pull request from your fork. Explain your changes, and the project owner might merge your work into the main project.

With these steps, you're set to make your first meaningful open source contribution!
{{% /summary %}}
