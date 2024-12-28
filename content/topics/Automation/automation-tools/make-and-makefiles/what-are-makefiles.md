---
title: "Use Makefiles to Manage, Automate, and Reproduce Projects"
description: "Learn how to use makefiles to establish defined protocols and strategies for your computational workflows."
weight: 1
keywords: "make, makefile, automation, recipes, workflow, pipeline, dependencies, targets, reproducible research"
date: 2021-01-06T22:01:14+05:30 
updated: 2023-08-18
aliases:
  - /learn/makefiles
  - /use/makefiles
---

## Learning goals

- Understand the fundamental elements of a makefile: targets, prerequisites, and instructions.
- Dive into advanced use cases, including directory naming, phony targets, variable utilization, and executing make through `.bat` files.
- Recognize the significance and functionality of make for automating tasks in reproducible research.

## Overview

Makefiles provide a set of structured rules directing a computer on how to compile or build projects. Think of makefiles as a recipe you may know from cooking ("Baking a cake: First, take some flour, then add milk [...]"), but then, for computers.

Makefiles originate in software development, where they have been used to convert source code into software programs that can then be distributed to users.

Researchers can use makefiles to establish rules detailing how individual components (e.g., cleaning the data, running an analysis, producing tables) are executed. When dependencies (e.g., to run the analysis, the data set first has to be cleaned) are well-defined, projects can be fully automated. When making changes to code, researchers can then easily "re-run" the entire project, facilitating immediate identification of any changes in the final results.

{{% tip %}}

- If you don't have `make` installed yet, follow [this guide](https://tilburgsciencehub.com/topics/automation/automation-tools/makefiles/make/)
- For a step-by-step introduction, refer to our [make cheatsheet](../images/tsh_make_cheatsheet.pdf).
  {{% /tip %}}

## Code

### Rules

A rule in a makefile generally looks like this:

{{% codeblock %}}

```bash
targets: prerequisites [separated by spaces]
   commands to build
```

{{% /codeblock %}}

- The **targets** are things that you want to build - for example, data sets, outputs of analyses, a PDF file, etc. You can define multiple targets for one rule. Typically, though, there is only one per rule. Think of this as the "dish" (or part of it) that you want to create with your recipe.

- The **prerequisites** are the things that you need before you can build the target. It's also a list of file names, separated by spaces. These files need to exist before the commands for the target are run. They are also called dependencies.

  The cool thing is that `make` automatically checks whether any of the dependencies has changed (e.g., a change in the source code) - so it can figure out which rules to be run, and which ones not, saving you a lot of computation time. You can view these as the "ingredients" of the recipe.

- The **commands** are a series of steps to go through to build the target(s). These need to be indented with a tab, **not** spaces. The commands can be seen as the recipe "instructions".

Here you have an easy example:
{{% codeblock %}}

```bash
dataset.csv: rawdata1.csv clean.R
  R --vanilla < clean.R
```

{{% /codeblock %}}

- `dataset.csv`: the final and cleaned dataset.
- `rawdata1.csv clean.R`: before building `dataset.csv`, the raw data and a specific script to clean the raw data need to exist.
- The command `R --vanilla < clean.R` opens R, and runs the script `clean.R`.

### Multiple rules

A makefile typically consist of multiple rules, which can depend on each other:

{{% codeblock %}}

```bash
# rule to build target2
target2: target1
  commands to build

# rule to build target1
target1: prerequisite1
  commands to build
```

{{% /codeblock %}}

## Advanced Use Cases

### Use directory names

You can easily use directory names in makefiles, e.g., to specify that a prerequisite is in one directory, and the target in another. For instance:

{{% codeblock %}}

```bash
gen/data-preparation/aggregated_df.csv: data/listings.csv data/reviews.csv
	Rscript src/data-preparation/clean.R
```

{{% /codeblock %}}

### "Phony" targets

Targets typically refer to output - such as files. Sometimes, it's not practical to generate outputs. We call these targets "phony targets".

- Creating a target `all` and `clean` is a convention of makefiles that many people follow.
- The phony target `all` serves as a comprehensive rule encompassing all individual targets.
- The target `clean` is typically used to remove generated temporary files, so you can start with a clean copy of your directory for testing.

The structure could look like this:
{{% codeblock %}}

```bash
all: one two

one:
    touch one.txt
two:
    touch two.txt

clean:
    rm -f one.txt two.txt
```

{{% /codeblock %}}

### Use variables

Variables in a make script prevent you from writing the same directory names (or command to execute a program) over and over again. They are typically defined at the top of the file and can be accessed with the `$` command. Note that variables can only be strings. Check out the following example:

{{% codeblock %}}

```bash
INPUT_DIR = src/data-preparation
GEN_DATA = gen/data-preparation

$(GEN_DATA)/aggregated_df.csv: data/listings.csv data/reviews.csv
  $(INPUT_DIR)/clean.R
```

{{% /codeblock %}}

### Run make using `.bat` files

Running a pipeline with `make` usually requires you to work from the command line (i.e., type `make` to start the workflow). In some circumstances, it may be more convenient to start the workflow from a batch file (e.g., on Windows, you would just have to double-click on such a file).

Here's a small code snippet to achieve that. You just need to create a `.bat` file in your project's directory (i.e., the one where you would usually run `make` in). This snippet writes any output from `make` in a `make.log` file, which you can use to verify `make` was executed properly.

{{% codeblock %}}

```bash
make -k > make.log 2>&1
pause
```

{{% /codeblock %}}

{{% warning %}}
**Is your makefile structured properly?**

Commands within the makefile must be preceded by a tab character. Ensure you use an editor that retains the tab structure. Some editors automatically convert tabs to spaces, which will lead to errors such as **\*\*\* missing separator.!**.
{{% /warning %}}

## Additional Resources

- [The Turing Way's Guide to Reproducible Research using `make`](https://the-turing-way.netlify.app/reproducible-research/make.html)
- [Software Carpentry's Lesson on Automation and Make](http://swcarpentry.github.io/make-novice)
- [Example makefile](https://github.com/hannesdatta/brand-equity-journal-of-marketing/blob/c8c9ff7a6904b4f6a7ad718932f21c6b87d4d881/analysis/code/makefile) for an analysis
- [Example makefile](https://github.com/hannesdatta/brand-equity-journal-of-marketing/blob/c8c9ff7a6904b4f6a7ad718932f21c6b87d4d881/derived/code/makefile) for a data preparation pipeline
