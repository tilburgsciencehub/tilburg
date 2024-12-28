---
# tutorialtitle: "Inside AirBnB - Workflow Walkthrough"
type: "airbnb-workflow"
title: "Overview"
description: "Set up an end-to-end workflow to investigate the impact of COVID-19 on AirBnB bookings"
keywords: "airbnb, make, R, workflow, inside airbnb, walkthrough"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 10
---

# Overview

## Inside AirBnB
[Inside Airbnb](http://insideairbnb.com/index.html) is an independent open-source data tool developed by community activist Murray Cox who aims to shed light on how Airbnb is being used and affecting neighborhoods in large cities. The tool provides a visual overview of the amount, availability, and spread of rooms across a city, an approximation of the number of bookings and occupancy rate, and the number of listings per host.

For example, [here](http://insideairbnb.com/amsterdam/) is the dashboard for the city of Amsterdam. The animation below illustrates how the number of listings have been growing rapidly throughout the years:

![title](../images/airbnb_expansion.gif)




## Research Question  
The overarching research question that we aim to investigate is:    
**How did the Airbnb market in Amsterdam respond to the COVID-19 pandemic in terms of bookings per neighborhood?**

To get to an answer, we need a multitude of input, transformation, and output steps. We'll use `make` to automate our workflows and make them reproducible. As data on Inside Airbnb is updated monthly, our program should still work once new data becomes available or if we change the city from Amsterdam to, for example, New York.
