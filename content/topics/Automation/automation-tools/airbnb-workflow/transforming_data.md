---
# tutorialtitle: "Inside AirBnB - Workflow Walkthrough"
type: "airbnb-workflow"
indexexclude: "true"
weight: 30
title: "Transforming the Data"
date: 2021-01-06T22:01:14+05:30
draft: false
---

# Transforming Data
## Feature Definition

As the author of Inside Airbnb notes, guests may leave a review after their stay, and these can be used as an indicator for the number of bookings. Although only verified guests can review listings, it is unlikely that every guest will take the time to write one. In reality, the number of bookings will thus exceed the number of reviews.

**Exercise**  
Think of several arguments why this may or may not be a problem in the context of our research question.   

{{% tip %}}  
Some hosts will be more likely to get reviews than others for a couple of reasons:

* Guest who had a highly positive (or negative) experience may be more inclined to leave a review to inform other Airbnb visitors.
* Guests may be more likely to leave a review for listings with many other reviews.
* The hosts have given a 5-star rating to the guests first and hope that they will reciprocate.
* The hosts might have specifically asked for it.

In other words, the likelihood of getting a review may not be uniform across all hosts. Yet it is another question whether this likelihood has significantly changed since the start of the pandemic. If not, then we can still use the number of reviews as a proxy for the number of bookings and examine the relative change compared to a pre-COVID period.

{{% /tip %}}  

## Data Preprocessing

Create a file `clean.R` that loads the data from the `data` directory and reshapes the data into the following format:

---
| date | neighbourhood | num_reviews |
| :---- | :---- | :---- |
| 2015-01-01 | Bijlmer-Centrum | 43 |
| 2015-02-01 | Bijlmer-Centrum | 94 |
| ... | ... | .... |
| 2020-12-01 | Zuid | 23 |      

---

Please adhere to the step-by-step guidelines below:  

* Convert the date column of `reviews` into date/time format.
* Filter for `reviews` published since January 1st 2015.
* Filter for `listings` that have received at least 1 review.
* Merge the `reviews` and `listings` dataframes on a common column.
* Group the number of reviews by date and neighborhood (aggregated on a monthly level).
* Store the final data frames in `gen/data-preparation` as `aggregated_df.csv`.


## Reshaping Data

If we want to compare neighbourhoods side by side (e.g., Centrum-West vs De Pijp) in, for example, a plot we need to transform the data from a *long* format into a *wide* format. More specifically, we are after a data structure in which the horizontal column headers are the neighbourhoods and the rows the dates:

---
| date | Bijlmer-Centrum | Bijlmer-Oost | ... | Zuid |
| :--- | :--- |:--- |:--- | :--- |
| 2015-01-01 | ... | ... | ... | ... |
| 2015-02-01 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| 2020-12-01 | ... | ... | ... | ... |
---


Import the data from `gen/data-preparation/aggregated_df.csv`, reshape the data into wide format and store the result as `pivot_table.csv` in `gen/data-preparation`.
