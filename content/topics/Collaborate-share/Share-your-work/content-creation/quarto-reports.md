---
title: "Automating Dynamic Reports With Quarto"
description: "Learn how to generate a Quarto report that updates automatically with streaming data from an API"
keywords: "Quarto, quarto, interactive, dashboard, report, automating, presentation, document, markdown, set-up, install, guide, command line, interface, tool, command line interface, CLI"
draft: false
author: "Valerie Vossen"
weight: 5
aliases:
  - /quarto-reports
---

## Overview

[Quarto](https://quarto.org/) is an open-source scientific and technical publishing system that enables you to create and share interactive documents, presentations, dashboards and reports. This topic demonstrates how to create a report using streaming data directly extracted from an API, automating the process to keep the report up-to-date.

As an example, we will generate a Quarto report using data collected from the API of the [music-to-scrape website](https://music-to-scrape.org/). The report is designed to automatically pudate weekly with the latest data.


{{% tip %}}

Before diving into this example, ensure you have Quarto set up by following these guides:

- [Quarto Setup Guide](/topics/computer-setup/software-installation/document-creation/quarto-setup/) for detailed instructions on installing Quarto.
- [Create Your First Document with Quarto](/topics/Collaborate-share/Share-your-work/content-creation/quarto-use/) to get familiar with its basic functionalities.

{{% /tip %}}


## Example: Generating a report with Quarto

In this example, we'll create a Quarto report that provides a summary of the top 5 streamed artists for the week, along with the number of plays. The data and visualization will update automatically with each new week's data.

{{% tip %}}

To follow along with this example, download [the Quarto file](https://github.com/valerievossen/quarto-example/blob/main/music-automated-report.qmd) yourself.

{{% /tip %}}


### Extracting the data

First, we'll extract streaming data from the API and store it in a [Pandas](/topics/Manage-manipulate/manipulate-clean/numerical/pandas/) DataFrame. This DataFrame will be displayed in the report, showing the top 5 artists and their total plays for the specific week.


{{% codeblock %}}
```python
# Import the required libraries
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 
import plotly.express as px

# Function to get top 5 artists with total plays

def get_top_artists_dataframe():
    # Specify the URL of the API
    api_url = "https://api.music-to-scrape.org"
    
    # Send an HTTP GET request to the API
    response = requests.get(api_url+'/charts/top-artists')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the chart data and timestamps
        artists_data = data.get('chart', [])
        unix_start = data.get('unix_start')

               # Convert the unix_start timestamp to a datetime object
        start_date = datetime.utcfromtimestamp(unix_start)
        week_number = start_date.isocalendar().week
        
        # Create lists to hold artist names and plays
        artist_names = []
        total_plays = []
        
        # Populate the lists with data
        for item in artists_data:
            artist_names.append(item['name'])
            total_plays.append(item['plays'])
        
        # Create a DataFrame from the lists
        df = pd.DataFrame({
            'Artist': artist_names,
            'Total Plays': total_plays,
            'Week Number': week_number
        })
        return df
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

# Get the dataset 
get_top_artists_dataframe()

```
{{% /codeblock %}}

The code creates the following DataFrame:

{{% table %}}

| Artist                      | Total Plays | Week Number |
| The Jackson Southernaires    | 51          | 34          |
| Stevie Ray Vaughan           | 49          | 34          |
| SNOWPATROL                   | 45          | 34          |
| Sugar Minott                 | 44          | 34          |
| Nick Cave & The Bad Seeds    | 37          | 34          |

{{% /table %}}

### Visualizing the data

Next, we'll visualize the data using an interactive bar plot, created with the `plotly` library in Python. This visuallization will also be included in the Quarto report.

{{% codeblock %}}
```python
def interactive_bar_plot(df):
    if df is not None:

        # Get week number from the DataFrame (to include in dynamic title)
        week_number = get_top_artists_dataframe()["Week Number"].iloc[0]

        # Sort the DataFrame by 'Total Plays' in descending order 
        df = df.sort_values(by='Total Plays', ascending=False)

        # Create an interactive bar chart with Plotly
        fig = px.bar(get_top_artists_dataframe(), x='Total Plays', y='Artist', 
                 title=f'Total Plays for Top 5 Artists - Week {week_number}',
                 labels={'Total Plays':'Total Plays'},
                 hover_data={'Artist':True, 'Total Plays':True, 'Week Number':False})

        fig.update_layout(xaxis_title='Artist', yaxis_title='Total Plays',
                      xaxis_tickangle=-45, template='plotly_white')
        fig.show()

# Create plot with recent data extracted from API
interactive_bar_plot(get_top_artists_dataframe())

```
{{% /codeblock %}}

The bar plot automatically updates, reflecting the top artists of the current week and dynamically adjusting the title to display the current week number.

To view the created report, including the interactive bar plot, preview the Quarto file yourself, or download the [HTML output file](https://github.com/valerievossen/quarto-example/blob/main/music-automated-report.html) to open it in your browser.

## Automating the workflow

To keep your Quarto report up-to-date automatically, you can schedule the execution of the Quarto report [using a task scheduler](/topics/Automation/automation-tools/task-automation/task-scheduling/). This section will show you how to apply common automation methods to a Quarto (`.qmd`) file.

In our example, we will automate the report to update weekly, specifically on Mondays at 9:00 AM. The updated report will generate a summary of the top 5 artists and their total number of plays for the current week!

### Task Scheduler (Windows)

For Windows users, Task Scheduler is a built-in tool that allows you to automate your Quarto script. Follow these steps:

1. *Open Task Scheduler* from the Start menu.
2. *Create a new task*

    - Click on "Create Basic Task" in the right-hand pane.
    - Name your task (e.g., "Weekly Music Report").
4. *Set the trigger*

    - Choose "Weekly" as the trigger 
    - Set the task to run every Monday at 9:00 AM.
5. *Set the action*

    - Select "Start a Program" as the action.
    - In the Program/Script field, add the path to the Quarto executable, typically `C:\Program Files\Quarto\bin\quarto.exe`. If unsure of the path, you can find it by typing `where quarto` in the command prompt.
6. In the "Add arguments" field, add the following:

{{% codeblock %}}
```bash
render "C:\Users\Pieter\Desktop\weekly-music-report.qmd"
```
{{% /codeblock %}}

Replace the file path in quotes with the correct path to your Quarto file. 

7. *Complete the wizard* and your task will run according to the schedule. Adjust the task settings to ensure the task will run even if your laptop is not plugged in.

### Cron job (Mac/Linux)

For Mac and Linux users, you can schedule your Quarto script to run weekly using a cron job. Follow these steps:

1. Open the terminal and type `crontab -e` to edit  your cron jobs.
2. *Edit the Crontab*
    - Press `I` to enter insert mode.
    - Add the following line to schedule your Quarto script to run every Monday at 9:00 AM:

{{% codeblock %}}
```bash
0 9 * * 1 <PATH OF YOUR QUARTO INSTALLATION> render <PATH TO QUARTO FILE>

```
{{% /codeblock %}}

- Replace `<PATH OF YOUR QUARTO INSTALLATION>` with the path to the Quarto executable. Typically, it's installed in `/usr/local/bin/quarto`, but you can find it by running `which quarto` in the terminal.
- Replace `<PATH TO QUARTO FILE>` with the path to your Quarto file. E.g. `/Users/pieter/Desktop/weekly-music-report.qmd`. 

4. *Save and exit:* Press `Esc`, type `:wq` and hit Enter to save your changes (if a window pops up choose OK).

5. *Verify the job:* Run `crontab -l` to confirm that your newly scheduled task is listed.


{{% summary %}}

We demonstrated how to create and automate a Quarto report that updates with streaming data from an API. Specifically, we covered:

- *Generating a Quarto report with streaming data*: An example is provided that summarizes this week's top 5 streamed artists and visualizes the data with an interactive bar plot in Python.

- *Automating the report*: How to use Task Scheduler on Windows and cron jobs on macOS/Linux to ensure your report remains up-to-date every week. 

{{% /summary %}}