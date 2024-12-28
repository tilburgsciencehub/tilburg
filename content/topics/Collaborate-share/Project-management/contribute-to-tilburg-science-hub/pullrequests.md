---
tutorialtitle: "Contribute using Pull Requests"
type: "contribute-to-tsh"
indexexclude: "true"
title: "Contribute using Pull Requests"
description: "Tutorials teach our users how to combine individual building blocks into a final product. Learn how to write one."
keywords: "template, pull, requests, contribute, github"
weight: 1004
draft: false
aliases:
- /contribute/pullrequests
- /contribute/mode-3
- /topics/more-tutorials/contribute-to-tilburg-science-hub/mode-2/
- /topics/more-tutorials/contribute-to-tilburg-science-hub/mode-3/
---

## Contributing using Pull Requests

On this page, we provide all the necessary resources and information for you to be able to write content autonomously.

{{% tip %}}

Please, notice that Tilburg Science Hub Building Blocks, Tutorials and Examples are written as [Markdown](https://guides.github.com/features/mastering-markdown/) files. We encourage you to familiarize with the Markdown formatting before starting to write - it's very easy!

{{% /tip %}}

### If you want to revise, modify, add, or remove content from existing pages, or report a bug

#### Simple changes

The easiest method to make straightforward updates to Markdown files is to use [GitHub's web-based file editor](https://help.github.com/en/articles/editing-files-in-your-repository).

1. Click on the "**Edit this page**" button at the bottom of the page you want to edit on our website.

![Edit this page button](./images/tsh-edit-this-page-button.png)

2. You will be redirected to our GitHub repository where that file is hosted. You will need to **fork** our repository in order to propose changes.

![Click on the pencil icon to open the text editor.](../github-fork.png)

3. Edit the file and then **submit a new pull request**. That's it.

#### Elaborate changes

For more complex updates or editing more than a file, it's better to use a local Git workflow to create a pull request.

After having [set up your GitHub account](/topics/configure-your-computer/statistics-and-computation/git/), follow the following steps (required only the first time you set up a local project):

1. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

2. Within your version of the forked repository, create a **new branch for each significant change being made**.

3. Navigate to the file(s) you wish to change within the new branches and make revisions as required.

4. Commit all changed files within the appropriate branches.

5. Create individual pull requests from each of your changed branches to the `main-flask` branch within the originating repository.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.

#### Host our site local to see your changes

If you want to make changes to, for example, our templates, or you want to see how your changes will look on the site you have to run our site locally using Flask. 

1. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

2. Clone the repository using git clone https://github.com/{your_github_account}/website.git

3. Follow the installation guidelines that are in README.md file in this repository (either using Docker or running by flask command). You can find there the exact commands to type in the command prompt to start running the website.

4. Within your version of the forked repository create a **new branch for each significant change being made**. Please note that since the website fetches the content from the database, in order to see your changes on the website you need to rerun `python content_to_db.py` script.

### If you want to write new content

1. First, you'll need to prepare the content as Markdown file(s). Follow our templates [below](#contribution-templates) to get started. In case you want to feature your project in the Examples section, please [contact us](/about/#who-maintains-tsh).

2. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

3. Clone the repository using git clone https://github.com/{your_github_account}/website.git

4. Follow the installation guidelines that are in README.md file in this repository (either using Docker or running by flask command). You can find there the exact commands to type in the command prompt to start running the website.

5. Within your version of the forked repository create a **new branch for each significant change being made**. Please note that since the website fetches the content from the database, in order to see your changes on the website you need to rerun `python content_to_db.py` script.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.

{{% tip %}}

Don't know how to do this? You can follow a great tutorial about [contributing on GitHub](https://github.com/firstcontributions/first-contributions).

{{% /tip %}}

### Place new sections in a logical order.

If you have written a new section which you wish to add to the website, make sure they are where they suppose to be.
{{% example %}}
  You wish to add a Building Block on "Advanced Git Commands". Now, imagine that once your page is completed, you notice that your new section appears in the first position:

  ![](./images/advanced-git-misplaced.PNG)

  Does it make sense to have the "Advanced Git Commands" section before the "Get Started with Git and Github"? It does not.

  - Ideally you would place it for instance, just after "The Most Important Git Commands You Should Know". This way, when going through the tutorials, the new content would come in a more natural order.
{{% /example%}}


**How to choose the order of sections?**

Well, using our Markdown Templates (which can be found below) it is quite a simple task. You only need to change the value of the parameter **"weight"** in the markdown file:

  ![](../weights.PNG)

{{% tip %}}
A weight set equal to 1 will place your section in the first place, likewise the prior example. If you wish to make it appear after other sections, make sure to give it a higher weight.
{{% /tip %}}

## Contribution Templates

{{% warning %}}

First, make sure to read our [code of conduct](../code-of-conduct) as well as our [writing guidelines](../style-guide).

{{% /warning %}}

{{% cta-primary "Start with our Building Block Markdown template" "https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/topics/more-tutorials/contribute-to-tilburg-science-hub/building-block-shell.md" %}}

{{% cta-primary "Start with our Tutorial Markdown template" "https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/topics/more-tutorials/contribute-to-tilburg-science-hub/tutorial-shell.md" %}}


<!--
The design should always accommodate all users' knowledge levels and avoid confusion. For instance, on a tutorial page, there should be a quick and concise explanation (a sort of TL;DR), as well as a more in-depth exposition for those who need to educate themselves first.

The design should be attractive and easy to use for all our target groups and should strike a balance between glossiness and nerdiness. We want to avoid unnecessary clutter and stock photos. Let's keep it simple.
-->
