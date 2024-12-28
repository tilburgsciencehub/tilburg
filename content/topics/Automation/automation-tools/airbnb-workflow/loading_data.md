---
title: "Loading the Data"
type: "airbnb-workflow"
indexexclude: "true"
weight: 20
date: 2021-01-06T22:01:14+05:30
draft: false
---

# Loading the Data
## Data Exploration
The [data](http://insideairbnb.com/get-the-data.html) underlying Inside Airbnb have been analyzed, cleansed, and aggregated where appropriate to facilitate public discussion. In this data challenge, we focus on the `listings.csv` and `reviews.csv` files which contain the following information:

*Listings*  
Information about the host, location, room type, price, reviews, and availability.

*Reviews*  
The listing ID and the date of the review. More details about the review such as the comment and author can be seen in the `reviews.csv.gz` file, but it is beyond the scope of this tutorial.

**Exercise**     
Before we fully automate our workflows, it is imperative to have a close look at the data.

1. Set up a directory structure in accordance with this [template](https://github.com/rgreminger/example-make-workflow). It should have a `data`, `gen`, and `src` directory and a `data-preparation` subdirectory in `src` and `gen`.
2. Manually download the most recent version of `listings.csv` and `reviews.csv` listed on [Inside Airbnb](http://insideairbnb.com/get-the-data.html) for Amsterdam and store them in the `data` folder.
3. Create a data report:  
  * Read the data into R and generate an overview of the data (e.g., summary statistics, report on missingness, number of observations, etc.).
  * Explore interesting relationships in the data.


{{% tip %}}   
An answer that includes the following elements:

* The number of listings is (+/- 18K) is somewhat lower than the figure reported in the dashboard.
* Most hosts have only one listing but some may account for 84 listings.
* Some listings received their last review in 2012 which indicates that not all listings may be in use anymore (for 2375 records this field is empty (`NA`) which suggests that they did not receive a review at all. This is confirmed by the number of reviews column (`0`)).
* Most listings receive less than a review per month (mean: 0.63, median: 0.30).
* The neighborhoods with the most listings are located in De Baarsjes - Oud-West, De Pijp - Rivierenbuurt, and Centrum-West. The `neighborhood_group` column does not contain any information and could therefore be removed.
* For half of the listings, the daily rate falls somewhere in between €94 and €180  (1st and 3rd quantile).
* The reviews file includes all historic reviews (not just the new ones since the last data release).
* Reviews are written between March 2009 and December 2020.
* The total number of reviews (+/- 452K) are grouped by listing (16K). Given the total number of listings on Airbnb, it implies that not all listings have been reviewed (see comment above).

Note that the figures and years mentioned above are based on the dataset from December 2020 and thus may deviate from more recent versions of the dataset.


{{% /tip %}}

## Download Data
Say that you want to share your work with others, you could essentially give them access to both the R file (`src` folder) and the two csv-files (`data` folder). Yet if you work with big data sets, you may run into problems: the data becomes too large to share through email, Github, or Google Drive. For that reason, it's recommended to create a script that pulls in the data directly from the source itself which is what you're going to do in this exercise.

1. Create a new file `download.R` and save it in the `src/data-preparation` folder.
2. Look up the URL of the download links of the most recent version of the `listings.csv` and `reviews.csv` datasets.
3. Download these two files from the aforementioned `urls` using the R code below and store them in the `data` folder.  `destfile` in `download.file()` refers to the (relative) filepath and filename (e.g., `../../data/listings.csv`).

```
download.file(url = url, destfile = filename)
```
4. Run the R script from the command line and test whether it works as expected. Make sure to open the command line in the folder with the script.  First, type `R` in the command line (e.g., Terminal on Mac or Command Prompt on Windows) and see whether it opens the R command line. If not, you may need to configure a path to the R library as described [here](/topics/configure-your-computer/statistics-and-computation/r/). Next, run the command below to run the download.R script from the terminal. It downloads the data from Inside Airbnb and stores it into the `data` directory.

```
R < download.R --save
```

![](../images/download_data.gif)
