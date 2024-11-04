---
title: "Coding, Workflow, and Data Management in a Research Project/Thesis"
description: "Coding, workflow and data management as the core foundation of your research."
keywords: "master, thesis, guide, marketing, economics, management, tisem, research, guidance, preparation, question, proposal, skills, resources"
date: 2023-07-10
weight: 3
author: "Valerie Vossen"
aliases:
  - /masterthesisguide/datacoding
---

## Overview

**Coding, workflow, and data management** is the core foundation of any independent research project within the quantitative social sciences (e.g. in economics, data science, or marketing). Think of any big course project or the research for your Master thesis. This is an overview of the sections covered:

- Code versioning: GitHub
- Data collection techniques
- Data import
- Inspecting raw data
- Building your project pipeline

## Code versioning: GitHub

GitHub is a powerful version control platform that allows you to manage and track changes in your code. This ensures transparency, and organization throughout the research process.

### Why use GitHub for your course project or Master Thesis?

Even if your project/thesis is not a collaborative project, keeping your work on GitHub still offers a lot of advantages:

- _Version control_: Easily track changes, view previous versions, and revert to earlier drafts if needed. No more confusion with multiple versions of the same document (e.g. saving the file as "Thesisdraft1", "Thesisdraft2" and so on).
  <br>

- _Transparent documentation:_ The commit history provides a clear record of all the edits made. Leaving clear commit messages helps in understanding what edits you made when revisiting your work after months of working on it.

- _Branching:_ You can create branches for different sections without impacting the main project draft in which you can experiment as much as you want.

- _Remote accessibility:_ Access your project from anywhere as GitHub is a cloud-based platform.

- _Backup:_ GitHub serves as a secure backup, minimizing the risk of losing your work.

- _Showcasing your work:_ After finishing the project, you can keep it on GitHub, making it accessible for others to use and showcasing your research!

Use [this topic](/share/data) to learn how to use GitHub for your project!

## Data collection techniques

Depending on your research, you might want to create your own data. Techniques for data collection include web scraping or APIs.

- The [Web scraping and API Mining tutorial](/learn/web-scraping-and-api-mining) discusses the difference between web scraping and API mining. It also shows you how to scrape static and dynamic websites and how to extract data from APIs.
- When you are new to web scraping and APIs, you can follow the open course [Online Data Collection and Management](https://odcm.hannesdatta.com/) of Tilburg University.

## Data import

You might want to analyze data sets for your project that already exist somewhere. There are several techniques to import data, dependent on your data source. Use these topics to learn about importing data and see example cases.

- [Download data directly from URLs using R and Python](/store/data)
- [Import larger datasets into R](/import/large-datsets)
- [The package `Dask` for processing large datasets in Python](/import/large-datsets-python)
- [Integrating SPSS data in R](building-blocks/prepare-your-data-for-analysis/data-preparation/spss-files-in-R): useful when your data source is an SPSS file
- [Text pre-processing in R](/building-blocks/prepare-your-data-for-analysis/data-preparation/text-preprocessing): useful when working with text data in R
- [Data sources related to areas of Economics](/research/datasources)

## Inspecting raw data

Upon importing your raw data, explore it right away to assess its quality. There are several things you can do:

- **Visually inspect your data:** Load the data into your software program (e.g. R, Excel) and visually inspect the data tables and their structure.

- **Cross-tabulate data:** Organize your data in a table format to see the frequency distribution of variables' categories in relation to each other. Do this with `table()` in R or pivot tables in Excel.

- **Plot your data** to explore trends (e.g. with `plot()` in R), or distributions (e.g. with `hist()` in R). Aggregate data by a common unit before plotting (e.g. time periods, categories like countries or brands).

### Important considerations

Key considerations when assessing your raw data quality include the following points:

- **Documentation**: study any provided ReadMe file or documentation thoroughly. Or if there is no documentation available, create your own using [this tutorial which includes a template](/document/new-data).

- **Variable names and columns**: Ensure you understand the meaning of each variable and column. Confirm if any columns are incomplete.

- **Data quality**:
  - Check for feasibility and consistency in variable values. Are there any values that seem unrealistic?
  - Detect missing values and identify if missing values truly represent NA (_Not Available_) data or if they imply zero values.
  - Verify the consistency in data definitions across the dataset, including the measurement units of your variables.
  - Pay attention to proper encoding of strings and headers.

{{% tip %}}
**GDPR compliance**
<br>
When dealing with data, ensuring compliance with your organization's data management policies is crucial. This often entails promptly anonymizing personally identifiable information during your data preparation phase.

Tilburg University has provided [specific guidelines for students](https://www.tilburguniversity.edu/sites/default/files/download/Student%20research%20and%20personal%20data%20in%20your%20research.pdf). Moreover, the legal department at Tilburg offers valuable [guidance on handling personal data with care](https://www.tilburguniversity.edu/about/conduct-and-integrity/privacy-and-security/research-data).
{{% /tip %}}

## Building your project pipeline

A project pipeline is a systematic framework that gives a structured sequence of the steps included in your research. It outlines the flow of tasks, from data collection and cleaning to analysis and visualization.

Your project pipeline might quickly become more complex, which makes a clear structure even more important. A good project pipeline ensures consistency and facilitates efficiency by breaking down the complex process into smaller manageable steps.

It also ensures transparency. For example, a project where code files are separated into multiple smaller components (e.g. one for data cleaning, one for running the model, one for producing tables and figures) is way easier for others to read and understand.

Use [this tutorial that covers the principles of project setup and workflow management](/learn/project-setup) as a guide.

{{% tip %}}
[A checklist to help you ensure you meet all the requirements when building your pipeline](/tutorials/project-management/principles-of-project-setup-and-workflow-management/checklist)
{{% /tip %}}

#### Pipeline automation

If your project is data-oriented, e.g. related to marketing analytics or data science, consider automating your pipeline. [This tutorial](/practice/pipeline-automation) is helpful to teach you how to automate your pipeline automation using `Make`.
