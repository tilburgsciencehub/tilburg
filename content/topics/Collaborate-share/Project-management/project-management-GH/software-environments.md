---
title: "Use Software Environments to Ensure Replicability"
description: "Sometimes when we scrape the web, we need to automate our computer to open a web browser to gather information from each page."
keywords: "environments, conda, software environments, virtual"
weight: 3
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /setup/software-environment
  - /setup/virtual-environment
  - /topics/automate-and-execute-your-work/automate-your-workflow/software-environments/
---

## Overview

The **main advantages** of using virtual software environments are:

1. **Ensures replicability**:
   - Environment specifies versions for each program and package used
   - Ensures that specified versions are the right ones (environment does not forget to update specified version if the version is updated in a project)
2. **Easy set-up on a different machine or the cloud**: run environment setup to install all required software/packages.

3. **Keeps projects separate**: adding or updating packages for one project does not affect others.

Here, we will explain how to use Conda to set up such virtual software environments. Conda is a package and environment manager and allows to install Python, R as well as additional software (e.g. pandoc) on Windows, Linux and MacOS.

### Why is keeping track of software/package versions important?

If software or packages are updated, code that was written for one, may not work on the updated version. An obvious example here is the difference between Python versions 2.7.x and 3.x, where code written for one will not work on the other. For example, just try the basic `print 'Hello World'` on Python 2.7.x and 3.x.

In such cases an error occurs and it will be obvious that a different software version needs to be used. However, changes across versions can also be more subtle and harder to detect. If the syntax does not change, but the underlying functions do, then code will still run through but may produce different results.

{{% example %}}
One example of a subtle change is the update of R from version 3.5.1 to 3.6.0. In this update, the way random numbers are produced by the `sample()` function was changed. This means that if the `sample()` function is used in a code, then running the same code on R 3.5.1 and 3.6.0 (or newer) will produce different results even if the seed is fixed. You can verify this easily by running this code in both R versions:

    # Fix seed
    set.seed(1)
    # Draw a random number from 1,2,...10
    r = sample(1:10,1)
    # = 9 on 3.6.3
    # = 3 on 3.5.1

{{% /example %}}

Given that such changes are bound to occur over time, it is important to keep track of which versions (of all packages!) are used for a project if it should still work and produce the same results in the future.

### Virtual environments

This is where virtual software environments come in. The environment basically is just a list specifying the full version specifications of all software and packages used. Of course, such an environment could just be a list typed by hand. But as projects develop over time with different packages being added and updated, the list would have to be kept up to date by hand, which is prone to errors and can be quite the effort.

Fortunately, there are software solutions that specify and keep track of software environments. The one we're using here is Conda, which is part of Anaconda which you will have already installed if you installed Python following the instructions [here](/topics/configure-your-computer/statistics-and-computation/python/). Of course, other solutions exist (e.g. in Python itself) to set up such environments. These are linked below.

There are multiple advantages to using Conda (or similar setups):

1. Installs software and packages directly (at least for R and Python)
2. Automatically keeps track of versions
3. Export environments and easily set them up on a different machine (or in the cloud)
4. Easy to use (both command line and graphical interface)
5. Part of Anaconda (which we used on Windows to install Python in the first place)

### General setup

For each project, create a separate software environment. This ensures that if you're updating versions for one project, it won't affect your other projects. Moreover, it creates fewer dependencies in a given project, as its environment will not also contain dependencies from other projects.

Note that now instead of using the familiar `pip install` or `install.packages()` commands in Python and R, it is necessary to install packages through Conda so that they are correctly added to the environment.

{{% tip %}}
**Activate the right environment**

Having multiple projects means having multiple environments. So when working on a project, always make sure the corresponding environment is activated.
{{% /tip %}}

## Code snippet

<!-- Provide your code in all the relevant languages and/or operating systems. -->

{{% codeblock %}}

```bash
# Create new empty environment
# (this will ask where to save the environment, default location is usually fine )
conda create --name test_env

# Activate environment
conda activate test_env

# Install R 3.6.1 and data tables package
# Note that R packages use prefix r-
conda install r-base=3.6.1
conda install r-data.table

# Close environment (switches back to base)
conda deactivate
```

{{% /codeblock %}}

## Using the code

If Conda is installed, the example can be run (line by line) in a terminal to set up a new software environment, install R and additional packages. The same structure can be used to set up environments for python, install additional packages and much more.

**Installation instructions for Conda**:

- If you've installed Python based on [these instructions](/topics/configure-your-computer/statistics-and-computation/python/), Conda should be already available
- Alternatively, detailed instructions to install Conda are provided [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Note that with the full Anaconda install environments can also be managed using a graphical interface. Here, we focus only on the command line to have clear steps. Instructions for the graphical interface are provided [here](https://docs.anaconda.com/navigator/tutorials/manage-environments/).

## Examples

1.  Add _conda-forge_ channel to get newer R version

        # Add 'conda-forge' channel (provides more recent versions,
        # and a lot of additional software)
        # Note: Sets overall config, not per environment
        conda config --add channels conda-forge

        # Install newer R version in test_env
        conda activate test_env
        conda install r-base=4.0.3

2.  Search for available packages

        # lists packages starting with r-data
        conda search r-data*

3.  Export environment into file (to be installed on a different machine)

        # Activate environment to be saved
        conda activate test_env

        # Export environment to a yml-file (in current directory)
        conda env export > test_env.yml

        # Export enviornment to a yml-file, only packages explicilty requested
        # (required if environment ported to different OS, see below)
        conda env export --from-history > test_env.yml

4.  Import and set up environment from file

        # Create environment based on yml-file (created as above, in same directory)
        conda env create -f test_env.yml

5.  Deactivate environment (gets back to base)

        conda deactivate

6.  Remove environment

        conda env remove --name test_env

    Note that there's a bug; software environments sometimes can only be removed if at least one package was installed.

7.  List installed environments

        conda info --envs

## OS dependence

Sometimes we work across different operating systems. For example, you may develop and test code on a Windows desktop, before then running it on a server that runs on Linux. As the Conda environment contains all dependencies, it will also list some low level tools that may not be available on a different OS. In this case, when trying to set up the same environment from a _.yml_ file created on a different OS it will fail.

{{% example %}}
Check the output of `conda list`, which will list various dependencies you never explicitly requested.
{{% /example %}}

In this case, it is possible to use the `--from-history` option (see Example 3 above). When creating the environment `.yml` file, this option makes it so that the generated `.yml` file will only contain the packages explicitly requested (i.e. those you at one point added through `conda install`), while the lower level dependencies (e.g. compiler, BLAS library) are not added. If the requested packages exist for the different OS, this usually should work as the low level dependencies will be automatically resolved when setting up the environment.

## Additional Resources

1. More information on Conda environments: [https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)

2. Python virtual environments: [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. Information on package environments in Julia: [https://julialang.github.io/Pkg.jl/v1/environments/](https://julialang.github.io/Pkg.jl/v1/environments/)
