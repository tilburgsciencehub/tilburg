---
tutorialtitle: "Guide to GitHub Copilot in RStudio"
type: "guide-to-github-copilot-in-rstudio"
title: "Guide to GitHub Copilot in RStudio"
description: "Learning what GitHub Copilot is, how and why it can be used"
keywords: "setup, RStudio, R, GitHub, GitHub Copilot, AI"
weight: 1
draft: false
aliases:
- /tutorials/more-tutorials/github-copilot
 
---
## Overview 

In this tutorial you will learn what GitHub Copilot is and how it can be used for you research in RStudio. 

## What is GitHub Copilot

[GitHub Copilot](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-for-individuals) is an AI pair programmer that offers autocomplete-style suggestions as you code. The tool can give you suggestions based on the code you want to use or by just simply inquiring what you want the code to do. 

It is developed by GitHub in partnership with OpenAI and it is designated to best assist developers in writing code more efficiently. 

Some of it's features include: 
- Code autocompletion: generating suggestions while you are typing the code. 
- Code generation: Copilot will use the context of the active document to generate suggestions for code that might be useful.
- Answering questions: It can also be used to ask simple questions while you are coding (e.g. "what is the definition of mean?").
- Language support: supports multiple programming languages including R, Python, SQL, HTML, JavaScript. In this tutorial we will be focusing on R. 

{{% warning %}}

Verified students, teachers, and maintainers of popular open source projects on GitHub are eligible to use Copilot for Individuals for free. Otherwise, a paid subscription is needed to use the tool.

{{% /warning %}}

## Set up GitHub and Copilot 

1. To start using the Copilot in RStudio, you first need to install R and RStudio on your computer. 
If you haven't checked it out yet, Tilburg Science Hub has a building block on this: [Installing R & RStudio](https://tilburgsciencehub.com/building-blocks/configure-your-computer/statistics-and-computation/r/)!

2. Once you have installed it, proceed to configure your GitHub account. To be able to use Copilot in R you need an active GiHub account. 
A useful source is [Set up Git and GitHub](https://tilburgsciencehub.com/building-blocks/configure-your-computer/statistics-and-computation/git/). 

3. As a student, you need to request specific access to use the service. Follow this [link](https://education.github.com/), you will need to provide proof of enrollment.

4. Once your application has been approved, you will receive a notification via email (be careful, it could also be in the spam folder). 

5. To activate GitHub Copilot, go to the [website](https://github.com/features/copilot), make sure you are signed in with your GitHub account (the same with which you have requested the student access). Click on "Get GitHub Copilot" then "Start free trial", after that a messagge should appear saying you are eligible to use Copilot for free. Proceed with installation, and there you go, you have now access to this feature. 

6. The process does not end here, to enable Copilot in RStudio follow these steps. Open the app, click Tools -> Global Options -> Copilot -> tic the box saying "Enable GitHub Copilot" -> sign in your GitHub account and ther you go, you are ready to start!


## Applications

In this tutorial, we will see the application of Copilot in RStudio in the following contexts: 

- Exploratory analysis of a dataset 
- Data visualization 
- Data manipulation 
- Questions & answers 

### Exploratory data analysis 

For this tutorial, we will demonstrate the use of Copilot with the built-in R dataset called "swiss", containing different socio-economic variables for different cantones in Switzerland. 

First library the package ggplot2, needed for visualization ans load the dataset. 

{{% codeblock %}}

```R
#Load packages
library(ggplot2)

# Load swiss dataset 
data("swiss")

```
{{% /codeblock %}}

Notice how Copilot will already suggest to start your notebook with "load packages". 
Now let's proceed with exploring the dataset with some summary statistics. Again noice that just by typing "Exploratory data analysis" in the R script, ghost suggestions will appear for the following steps. Such examples are the commands summary and head. 

{{% codeblock %}}

```R
#Exploratory data analysis 

#summary statistics
summary(swiss)
head(swiss)

#summary statistics on one variable (e.g.fertitlity)
mean(swiss$Fertility)
sd(swiss$Fertility)

hist(swiss$Fertility)

```
{{% /codeblock %}}

Copilot in this case suggested me to plot a histogram of the variable fertility.

Another useful way to use Copilot is simply writing what you want to do, and suggestions will appear accordingly. For example, if we want to know the summary statistics for two variables (e.g. fertility and education) and their correlation, simply write it in a comment format (using #) and Copilot will provide the code as shown below.  

{{% tip %}}

The simpler the instructions the better for your output as Copilot is a new introduction in RStudio and it is constatly being trained. 

{{% /tip %}}

{{% codeblock %}}

```R
#summary statistics on two variables (e.g. fertility and education)
mean(swiss$Education)
sd(swiss$Education)

cor(swiss$Fertility, swiss$Education)
plot(swiss$Fertility, swiss$Education)
```
{{% /codeblock %}}

### Data visualization 

A great adavantage of using Copilot in RStudio is data visualization. With a simple request to Copilot, you can change the apperance of your visualization and implement small changes to quickly elevate your graphs. An example is the following code: 

{{% codeblock %}}

```R
#create a scatterplot between Fertility and Agriculture using ggplot2
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point()

#improve the visualization, add a title, impose minimal setting and change the color of the point to a more neutral one
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "grey") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland")

#I want the dots to be blue
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland")

#add the regression line to the plot
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland") + geom_smooth(method = "lm", se = FALSE)

#make the line dashed 
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland") + geom_smooth(method = "lm", se = FALSE, linetype = "dashed")

```
{{% /codeblock %}}

For your reference, a comparison between the starting and the final scatterplot: 

<p align = "center">
<img src = "../img/Rplot.png" width="400">
</p>

<p align = "center">
<img src = "../img/Rplot01.png" width="400">
</p>

### Data manipulation 

In this case, the data manipulation consists of adding the cantons names as the first column instead of having them as indexes. This can be useful in case you want to perform a cluster analysis grouping cantons with similar socio-economic features. 

In case you do not know how to proceed, you can simply ask Copilot how to do it and it will give you an input. 
The following code block represents Copilot's suggestion. 

{{% codeblock %}}

```R
#I want to remove the index and add it as a column in the dataset, suggest me a way to do it 
swiss$Cantones <- rownames(swiss) 
head(swiss)
```
{{% /codeblock %}}

After running this command, visualize the dataset. Notice that the cantons names were not removed as row names and were added as the last column. Although in principle this is not wrong, it looks confusing and it would be better to have them in the first column for a clearer and more structured dataset. 

After some research, one of the possible ways to do this is the following: 

{{% codeblock %}}

```R
data("swiss")
library(tibble)
swiss <- as_tibble(swiss, rownames = "Cantons")
```
{{% /codeblock %}}

{{% tip %}}

Re-load the swiss dataset to work on the original version, othwerwise you would be running the above code on the modified one. 

{{% /tip %}}

This last step was to show that Copilot, as every AI powered tool, is not to be followed blindly as it is constantly learning and hence can cause mistakes or simply not execute what yo have in mind. 

### Questions & answers

A nice feature of Copilot is the possibility to ask questions adn receive a response on the RStudio script. A simple example is the following: 

{{% codeblock %}}

```R
#You can also ask questions to Copilot. 

# q: What is the definition of mean of a variable?
# a: The mean is the average of the numbers. It is easy to calculate: add up all the numbers, then divide by how many numbers there are. In other words it is the sum divided by the count.

```
{{% /codeblock %}}

{{% tip %}}

To ensure accuracy, ask relatively clear and simple questions. 

{{% /tip %}}


{{% summary %}}
This tutorial provides an overview of GitHub Copilot and its application in RStudio for research purposes. 
It comprises three blocks: 

1. Explaining what GitHub Copilot is, its main features and applications. 
2. The setup process to enure a smooth start with this new tool in RStudio. 
3. Demonstrations on how to use Copilot in RStudio. 
{{% /summary %}}

*Sources: [RStudio GitHub Copilot](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html); [GitHub Copilot](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-for-individuals)*