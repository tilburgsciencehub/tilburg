---
title: "Set up Quarto"
description: "Learn how to install and use Quarto"
keywords: "Quarto, quarto, interactive, dashboard, presentation, document, markdown, set-up, install, guide, command line, interface, tool, command line interface, CLI"
draft: false
author: "Valerie Vossen"
weight: 5
aliases:
  - /get/quarto
  - /install/quarto
---

## Overview

[Quarto](https://quarto.org/) is an open-source scientific and technical publishing system that allows you to create and share interactive documents, presentations, dashboards, and reports. It does not provide a standalone graphical user interface, but is built to integrate with tools like [Visual Studio Code](/topics/computer-setup/software-installation/ide/vscode/), [Jupyter](https://jupyter.org/), [RStudio](/topics/computer-setup/software-installation/rstudio/r/), etc. It supports Markdown and executable code blocks in multiple programming languages, such as [R](/topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/), [Python](/topics/computer-setup/software-installation/python/python/), and [Julia](/topics/computer-setup/software-installation/matlab/julia/).

<p align = "center">
<img src = "../images/quarto-logo.png" width="300">
</p>

## Installing Quarto

#### Windows Users

- Go to the [Quarto downloads page](https://quarto.org/docs/get-started/)
- Click on the blue button `Download Quarto CLI` to download the Windows Installer for the latest Quarto release. 
- Open the installer from your download history. A set-up wizard will guide you through the installation process.
- Follow the instructions, clicking `Next` as required.
- Close the setup wizard once the installation is completed. 

#### Mac Users

- Go to the [Quarto downloads page](https://quarto.org/docs/get-started/)
- Download the macOS Installer package (`quarto-{version}-macos.pkg`).
- Navigate to your download folder and double-click the `.pkg` file to start the installer. 
- Follow the prompts in the installation wizard. 
- Once the installation is complete, click `Close`.


#### Linux/Ubuntu users

- Visit the [Quarto downloads page](https://quarto.org/docs/get-started/)
- Choose the right package for your Linux distribution. 
- Open a terminal window. Use the package manager for your distribution to install the downloaded package. For Ubuntu, this typically involves running:

{{% codeblock %}}
```bash
sudo dpkg -i quarto-{version}.deb
sudo apt-get install -f
```
{{% /codeblock %}}


{{% summary %}}

Now that Quarto is installed, you can start using it to create a wide range of documents and presentations. Continue with this [topic](/topics/collaborate-share/share-your-work/content-creation/quarto-use/) to learn how to begin working with Quarto and take advantage of its features!

{{% /summary %}}

