---
title: "Set up Make"
description: "Learn how to install make on windows, mac, and Linux. Use make to automate the execution of projects, and see how to check if make is installed correctly"
keywords: "make, build, build tool, install, set up, windows"
weight: 2
date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /get/make
  - /install/make
---

## What is Make

[`Make`](https://www.gnu.org/software/make/) is a "build tool", allowing us to control the execution of a set of command line statements to assemble pipelines that define what gets executed when. Using `make`,
our entire workflow becomes transparent and reproducible.

{{% tip %}}

**Why Build Tools?**

Imagine you have built a complex project, consisting of dozens of datafiles and scripts.
Also imagine you haven't worked on the project for a few weeks, and now wish to continue
your work where you left off.

The big questions then become:

- In which order do the files need to be executed?
- Which files are up-to-date and do not have to be executed again?

For this purpose, we use a *workflow management system* - or, in technical terms - "build tool".
Build tools will allow us to control the execution of a set scripts by running them from the command line.

Some reasons we push this topic are:

* Your workflow / order of execution is explicitly documented.
* Each time you run `make`, it only executes each script if the output is expected to be different from the last time your ran it. That is, it runs 'partial builds.'
* If multiple users work on the project, they can easily execute code that others have written.

{{% /tip %}}
<!--    #* Its written in Python, which minimizes the learning curve needed to pick up the essentials relatively small
#    #* It was designed for academic/professional research (in Bioformatics) so it feels more intuitive than most alternatives for our desired audience.
-->

## Installation

We will use `make` to automate the execution of our projects with a "single click", so that our entire work flow is reproducible.

### For Windows Users

We will install `make` so that it plays nicely with your Anaconda/Python distribution and the Windows command line.

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube 8bqH8AOPT3U iframe-video-margins >}}

#### Download make
Please [download `make` here](http://gnuwin32.sourceforge.net/downlinks/make.php).

{{% warning %}}
**Making `make` available via the PATH settings on Windows.**

We need to update our PATH settings; these settings are a set of directories that Windows uses to "look up" software to startup.
{{% /warning %}}

    - Open the settings for environment variables
        - Right-click on Computer.
      	- Go to "Properties" and select the tab "Advanced System settings".
      	- Choose "Environment Variables"
    - Alternatively, type "environment variable" (Dutch: omgevingsvariabelen) in your Windows 10 search menu, and press Enter.

	-  Select `Path` from the list of user variables. Choose `Edit`.
		- **Windows 7 and 8 machines:**
			If you chose your installation directory to be `C:\Program Files\GnuWin32\bin` during your installation (i.e., you did use the default directory), copy and paste the following string without spaces at the start or end:

            `;C:\Program Files (x86)\GnuWin32\bin`

		- **Windows 10 machines:**
			- Click `New` and paste the following string:

            `C:\Program Files (x86)\GnuWin32\bin`

			- Click on `OK` as often as needed.

<!---

within CygWin.
Its time to go back to the **setup-x86_64.exe** we [told you not to delete](commandLine.md). We will use it to install make.
Proceed as follows:

* Click through the installation until you arrive at the page "Select packages."
* Type make into the search function and wait for the results to be filtered.
* Click the '+' next to "Devel" and then find the following lines:
    * make
    * gcc-tools-epoch1-automake
    * gcc-tools-epoch2-automake
 and then click on the word 'Skip' located next to each of these. 'Skip' should then be replaced with some numbers (the version which we will install).
 * Now click on "Next" in the bottom right corner and continue accepting all options until the installation is complete.

-->

### For Mac Users

* Please install X-code command line tools, which includes `make`.

Open a terminal by searching for it with spotlight, `cmd + spacebar` then type terminal and press `Return` when it appears. Then, copy and paste the following:

```bash
xcode-select --install
```

### For Linux Users

`Make` is pre-installed on Linux operating systems so there is nothing to be done.


## Verifying Your Installation

To check that `Make` is installed and working correctly, open a terminal session and type (then hit the return key):

```bash
make
```

If everything is working correctly, you should get the following output:

```bash
make: *** No targets specified or no makefile found. Stop.
```
