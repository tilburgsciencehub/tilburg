---
title: "Create Your First Interactive Document With Quarto"
description: "Learn how create and publish interactive documents, such as presentations, websites, blogs, books, etc. with Quarto"
keywords: "Quarto, quarto, interactive, dashboard, presentation, document, markdown, set-up, install, guide, command line, interface, tool, command line interface, CLI"
draft: false
author: "Valerie Vossen"
weight: 5
aliases:
  - /quarto
  - /use/quarto
  - /quarto-use
---

## Overview

[Quarto](https://quarto.org/) is an open-source scientific and technical publishing system that enables you to create and share interactive documents, presentations, dashboards, and reports. It doesn't provide a standalone graphical user interface but is built to integrate with tools like [Visual Studio Code](/topics/computer-setup/software-installation/ide/vscode/), [Jupyter](https://jupyter.org/), [RStudio](/topics/computer-setup/software-installation/rstudio/r/). It supports Markdown alongside executable code blocks in multiple programming languages, such as [R](/topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/), [Python](/topics/computer-setup/software-installation/python/python/), and [Julia](/topics/computer-setup/software-installation/matlab/julia/). This guide will walk you through creating your first document. 

{{% tip %}}

Refer to [our Quarto Set-up Guide](/topics/computer-setup/software-installation/document-creation/quarto-setup/) for detailed instructions on installing Quarto.

{{% /tip %}}

## What is Quarto

Quarto is a powerful publishing system that uses Markdown to author content. It allows you to seamlessly blend narrative text and executable code chunks within a single file. This makes it ideal for creating interactive tutorials, sharing reproducible research results, and delivering impactful communication.

Key advantages of Quarto are:

- *Integrated code and text:* Combine text, code snippets, and visualizations in a single document.

- *Versatile data science tool:* Quarto supports multiple programming languages, including R, Python, and Julia, and integrates smoothly with environments like VS Code, RStudio, and Jupyter Notebooks. 

- *Various output formats*: Generate documents in formats like HTML, PDF, Word, and PowerPoint, all without needing to adjust the document's syntax for each format. 

- *Interactive features*: Incorporate interactive elements like [Shiny apps](/topics/Visualization/data-visualization/dashboarding/introduction-to-r-shiny/) and widgets directly into your documents. 


## Use Quarto with VS Code

1. Install the Quarto VS Code Extension
  - Open the Extensions Marketplace in VS Code, using the shortcut `Ctrl+Shift+X` (`CMD+Shift+X` on Mac), or click the Extensions icon on the left sidebar:

  <p align = "center">
<img src = "../images/VSCodeExtensions_icon.png" width="200">
</p>

- Search for "Quarto" in the search bar.
- Click the blue "Install" button. 

2. Create a `.qmd` (Quarto Markdown) file. 

- Navigate to the File menu and select "New File" 
- Type "Quarto", then choose "Quarto Document" from the available options.


3. Adding content:

*Metadata*

Start by setting up your document's metadata in the YAML block at the top of your Quarto file, for example: 

{{% codeblock %}}
```yaml
---
title: "My First Quarto Document"
author: "Your Name"
date: "2024-08-15"
format: 
  html:
    code-fold: true
---
```
{{% /codeblock %}}

This section defines key information, including the title, author, date, and output format. Setting `code-fold: true` collapses the code into a clickable tab. 

*Markdown text*

You can add text using Markdown syntax, for example to introduce your content and explain your code.

{{% tip %}}

Common Markdown features:

- **Bold text**: Use double asterisks (`**`)
- *Italic text*: Use single asterisks (`*`)
- Create headers with `##`
- Create lists by using `-` or `*`

{{% /tip %}}

*Code blocks*

Code blocks are enclosed in three backticks (`` ``` ``) with the language specified in curly braces (`{}`).

### Examples

*Create a plot in Python* 

To create a Quarto document with Python code, follow these steps:

- Add `jupyter: python3` to the metadata section to specify the kernel. 
- Ensure you have `matplotlib` installed. If not, use the following command in the terminal:
  - For Windows: `py -m pip install matplotlib`
  - For Mac: `python3 -m pip install matplotlib`

- Insert the following content into your Quarto document, replacing the escaped backticks around the Python code block (`` \`\`\` ``) with normal backticks (`` ``` ``).

{{% codeblock %}}
```markdown

## Creating a line plot in Python

We demonstrate how to create a simple line plot in Python, in the following steps:

- We import the `matplotlib` library
- We create data, saved in `x` and `y`
- We create the plot with the `plt.plot` function.

\`\`\`{python}
import matplotlib.pyplot as plt

# Data for plotting
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Create the plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
\`\`\`

```
{{% /codeblock %}}


{{% tip %}}

You can execute a code cell without rendering the entire document. Simply click "Run Cell", and the plot will appear in a new tab.

{{% /tip %}}


*Create a plot in R:*

As an example, the following steps create a Quarto document with R code creating a plot:

- Install the R extension in VS Code, by navigating to the Extensions tab, selecting the R extension, and clicking "Install"

- Install the required R packages (e.g., `ggplot2`). It's best practice to avoid installing packages directly within a Quarto document, as this would cause the installation to be repeated every time the document is rendered. Instead, install the packages in your terminal or within RStudio to keep your Quarto document clean. 


- Add the following Markdown and R code block to your Quarto file, replacing the escaped backticks around the R code block (`` \`\`\` ``) with normal backticks (`` ``` ``).

{{% codeblock %}}
```markdown

## Creating a scatter plot in R

\`\`\`{r}
#| echo: true
#| message: false
#| warning: false

# Load ggplot2 for plotting
library(ggplot2)

# Create a simple scatter plot
data <- data.frame(x = 1:10, y = (1:10)^2)

ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  geom_line() +
  ggtitle("Simple Scatter Plot with ggplot2") +
  xlab("X-axis") +
  ylab("Y-axis")
\`\`\`

```
{{% /codeblock %}}

{{% tip %}}

Code block options are added using `#|`. For example, you can label the code chunk, or control how code, messages, and warnings are handled:

- Use `label: ` to give the code chunk a descriptive name.
- Use `echo: true` to display the code in the output. 
- Use `message: false` to hide any messages generated by the code.
- Use `warning: false` to hide warnings in the output.

{{% /tip %}}


4. Render and preview

To preview your document with a plot created in either R or Python:

- Click on the three dots in the upper-right corner of the file, then click "Preview" (Shortcut: `Ctrl+Shift+K` for Windows, or `cmd+Shift+K` for Mac).
- The document will open in a new tab in VSCode, or you can `Ctrl+Click` the `http://localhost` link to preview the HTML version in a web browser.

Here's the output in HTML format from the example (the code is hidden under the Code tabs):

<table>
<tr>
<td style = "padding:10px">
<img src = "../images/quarto-python.png"/>
<figcaption> HTML document with plot in R</figcaption>

</td>
<td style = "padding:10px">
<img src = "../images/quarto-r.png"/>
<figcaption> HTML document with plot in Python</figcaption>
</tr>
</table>


{{% tip %}}

You can render your document in various formats by adjusting the `format:` section in the metadata. Some common options include:
- `pdf`
- `docx`: Word document
- `revealjs`: slide deck

{{% /tip %}}


### Combining R and Python in the same Quarto document

You can combine R and Python in the same Quarto document with just a few extra steps. 

For example, if your document primarily uses R code blocks, the engine will default to `knitr`. To run Python code in this environment, you can use the `reticulate` R package, which allows you to execute Python code directly from the R console.

{{% warning %}}

If your document contains mostly Python code, it's best to use the Jupyter engine instead. If you need to run R code from a Jupyter engine, you can do so [using the `rpy2` package in Python](https://rviews.rstudio.com/2022/05/25/calling-r-from-python-with-rpy2/).

{{% /warning %}}

Here's an example of a Quarto file that combines R and Python: 

{{% codeblock %}}
````markdown
---
title: "Combining R and Python"
author: "Your Name"
date: "2024-08-15"
format: 
  html:
    code-fold: true
---

# Cleaning Data in R

```{r}
#| echo: true
#| message: false
#| warning: false

## load reticulate package
library(reticulate)


# Load dplyr for data cleaning
library(dplyr)

# Load data (built-in dataset: airquality)
data("airquality")

# Data Cleaning: Remove rows with missing values
cleaned_data <- airquality %>%
  filter(!is.na(Ozone), !is.na(Solar.R), !is.na(Temp))

# Inspect cleaned data
head(cleaned_data)
```

# Visualizing data in Python 

```{python}
import pandas as pd
import matplotlib.pyplot as plt

# Convert R cleaned data to a pandas DataFrame
cleaned_data = r.cleaned_data

# Inspect the DataFrame in Python
cleaned_data.head()

# Create scatter plot of Ozone vs Temperature
plt.figure(figsize=(8, 6))
plt.scatter(cleaned_data['Temp'], cleaned_data['Ozone'], color='blue', alpha=0.7)
plt.title("Ozone Concentration vs Temperature")
plt.xlabel("Temperature (Fahrenheit)")
plt.ylabel("Ozone (ppb)")
plt.grid(True)
plt.show()
```

````
{{% /codeblock %}}

In this example, the `r.` prefix in the Python code block allows you to access the R object `cleaned_data` for use in Python. 

*The rendered HTML output:*

<p align = "center">
<img src = "../images/quarto-combine-r-python.png" width="400">
</p>

## Use Quarto with JupyterLab

Quarto can be used within JupyterLab to work with `.ipynb` files (Python notebooks). To get started, refer to [this guide](https://quarto.org/docs/get-started/hello/jupyter.html).

The process is very similar to using Quarto with VS Code. You can render notebooks from the Jupyter terminal using commands like `quarto preview example-file.ipynb`, which will open the output in a new tab. You can also define the desired output format and other options in the YAML metadata section at the top of the notebook.


## Use Quarto with RStudio

To set up Quarto with RStudio, refer to [this page](https://quarto.org/docs/get-started/hello/rstudio.html). The basic workflow is simple:

- Open a `.qmd` file in RStudio by selecting "File" -> "New File" -> "Quarto Document".
- Preview the file by clicking the "Render" button, which you can find either in the toolbar above the document (button with a blue arrow) or under the "File" tab.
- The output will open in a new tab in your web browser, or copy the `http://localhost` link to view the preview.


{{% summary %}}

Quarto is a powerful tool that blends Markdown with executable code blocks. This guide helps you get started with your first Quarto document. As you become more skilled with Quarto, learn how to [automate a report with streaming data](/topics/Collaborate-share/Share-your-work/content-creation/quarto-reports/) next!

{{% /summary %}}