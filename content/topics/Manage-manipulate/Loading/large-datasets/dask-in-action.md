---
title: "Practical Example with Dask"
description: "Dask in action, a practical example for how to use Dask in a simple analytics task: how is it different from Pandas, how to do descriptive statistics, create new variables, perform grouping, filtering and plotting."
keywords: "dask, pandas, python, data, statistics, descriptive statistics, grouping, filtering, large datasets, lazy evaluation"
date: 2023-04-06
weight: 3
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /learn/dask
  - /analytics/task
  - /real/example
---

## Using Dask to Describe Data

We learned how to [Handle Large Datasets in Python](../large-datasets/large-datasets-python.md) in a general way, but now let's dive deeper into it by implementing a practical example. To illustrate how to use Dask, we perform simple descriptive and analytics operations on a large dataset. We use a flight dataset, available at [Kaggle.com](https://www.kaggle.com/datasets/usdot/flight-delays), containing over 5M flight delays and cancellations from 2015. When loaded with `pandas`, the dataframe occupies more than 1.3GB of memory, which would make operations rather slow. Let's load the data with `dask`. For all operations we also provide the equivalent `pandas` code for comparison.

### Loading the data

The first thing we need to do is import the `dask` library and load the data. Make sure that the downloaded data is in the same working directory as the Python file of the code. In Dask, we do this as follows:

{{% codeblock %}}

```python
# import the Dask DataFrame module
import dask.dataframe as dd

#read the downloaded csv file
flights = dd.read_csv('flights.csv', assume_missing=True, dtype={'CANCELLATION_REASON': 'object'})
```

{{% /codeblock %}}

The equivalent `pandas` code would be:

{{% codeblock %}}

```python
# import the pandas module
import pandas as pd

#read the downloaded csv file
flights = pd.read_csv('flights.csv')

```

{{% /codeblock %}}

{{% tip %}}
The arguments `assume_missing` and `dtype` are added because it is likely that `dask` will raise a _ValueError_ due to its attempts to infer the types of all columns by reading a sample of the data from the start of the file. This attempt is sometimes incorrect, thus it may require manually specifying the type each column should have (with `dtype`) or assuming all integer columns have missing values and request their conversion to float (with `assume_missing`).

If you don't mention these arguments when reading the data and it raises the error, Python will suggest a possible solution to fixing it.

{{% /tip %}}

### Inspecting the data

Now that we loaded the data, let's see what it looks like and find some basic info about it.
We can check to see how many partitions the data has been divided in and display the data using the following commands:

{{% codeblock %}}

```python
#check number of partitions
flights.npartitions

#display dataframe
flights.compute()
```

{{% /codeblock %}}

Since `pandas` does not partition a dataset there are no equivalent commands.

We can see the column names and shape of the dataframe too. In `dask`:

{{% codeblock %}}

```python
#display dataframe columns
flights.columns

#check the shape of dataframe
flights.shape  #outputs delayed object
flights.shape[0].compute() #calculates the number of rows
```

{{% /codeblock %}}

Note that the output of the `.shape()` method in `dask` doesn't immediately return output.
Instead, it gives this: `(Delayed('int-4b01ce40-f552-432c-b591-da8955b3ea9c'), 31)`.
This is because `dask` uses lazy evaluation - it delays the evaluation of an expression until its value is needed.
We use `.compute()` to evaluate the expression.
Why the delay? It's because to count the number of rows, `dask` needs to work through each partition and sum the number of the rows in each one.
More information on lazy evaluation is available in our building block [Handle Large Datasets in Python](../large-datasets/large-datasets-python.md).

If we wanted the column names and shape via `pandas`:

{{% codeblock %}}

```python
#display dataframe columns
flights.columns

#check the shape of dataframe
flights.shape
```

{{% /codeblock %}}

In `dask` the `info()` function doesn't give us the output we know from `pandas`, but instead only gives the number of columns, the first and last column name and dtype counts. Alternatively, we can do the following to get each dtype and non-null/null counts:

{{% codeblock %}}

```python
#show types of columns
flights.dtypes

#count non-null
flights.notnull().sum().compute()

#alternatively, count null
flights.isna().sum().compute()
```

{{% /codeblock %}}

To achieve the same thing in `pandas` we'd write the following:

{{% codeblock %}}

```python
#show types of columns
flights.dtypes

#dataframe info
flights.info()

```

{{% /codeblock %}}

### Descriptive statistics, Grouping, Filtering

We want to investigate the delays, more specifically, what is the biggest delay? What airline has the largest amount of summed delays? Is there a difference in average arrival delay between certain periods of the year?

Let's start with descriptive statistics to get a grasp of the data.
Starting with `dask`:

{{% codeblock %}}

```python
#compute descriptive statistics for the whole dataframe
flights.describe().compute()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe().compute()
```

{{% /codeblock %}}

Which is similar to how we'd work in `pandas`.

{{% codeblock %}}

```python
#compute descriptive statistics for the whole dataframe
flights.describe()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe()
```

{{% /codeblock %}}

If we wanted to find the largest departure delay, we'd need to use the `max()` command along the horizontal axis. In `dask`:

{{% codeblock %}}

```python
#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0).compute()
```

{{% /codeblock %}}

Or, equivalently in `pandas`:

{{% codeblock %}}

```python
#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0)
```

{{% /codeblock %}}

Next, we may be interested in which airline has the largest amount of minutes delay in the data.
We can find this by computing the sum of the airline delays grouped by airlines.

{{% codeblock %}}

```python
#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum().compute()
```

{{% /codeblock %}}

Or in `pandas`:

{{% codeblock %}}

```python
#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum()
```

{{% /codeblock %}}

We might also want to know if the average delay is different across months.
For example, delays could be higher in winter due to snowstorms and inclement weather.
We start by first checking if the data contains delays for all months of the year. Then, we compute the mean arrival delays by grouping them per month.

{{% codeblock %}}

```python
#count the unique values for the "month" column to check we get 12
flights['MONTH'].nunique().compute()

#group the average arrival delay per month
flights.groupby(by = 'MONTH')['ARRIVAL_DELAY'].mean().compute()

#take the maximum average delay
flights.groupby(by = 'MONTH')['ARRIVAL_DELAY'].mean().max().compute()

```

{{% /codeblock %}}

The same operations would be executed in `pandas` as follows:

{{% codeblock %}}

```python
#count the unique values for month column to check we get 12
flights['MONTH'].nunique()

#group the average arrival delay per month
flights.groupby(by = 'MONTH')['ARRIVAL_DELAY'].mean()

#take the maximum average delay
flights.groupby(by = 'MONTH')['ARRIVAL_DELAY'].mean().max()

```

{{% /codeblock %}}

### Variable creation and plotting

When plotting large datasets, we can either use packages that can handle many data points, or bring the data that we want to plot to a smaller shape that fits the memory. For this simple example we want to plot the count of airlines per month, which is not a large dataframe, so we can just use the classic `matplotlib` to make a graph.

Thus, in our answer to the question "Is there a difference in average arrival delay between certain periods of the year?", we can visualize the average delays for each month with a plot:

{{% codeblock %}}

```python
#create new dataframe
monthly_delay = flights.groupby(by = 'MONTH')['ARRIVAL_DELAY'].mean().reset_index()

#converting the dataframe from dask to pandas
monthly_delay = monthly_delay.compute()

#convert month column to int type
monthly_delay['MONTH'] = monthly_delay['MONTH'].astype(int)

#create bar plot
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 7))

# creating the bar plot
plt.bar(monthly_delay["MONTH"], monthly_delay["ARRIVAL_DELAY"], color ='orange',
        width = 0.4)

plt.xlabel("Month")
plt.xticks(range(monthly_delay['MONTH'].nunique()+1)) #display all values on x axis
plt.ylabel("Average arrival delay")
plt.title("Average arrival delay per month")
plt.grid()    #display grid
plt.rcParams.update({'text.color': "white",
                     'axes.labelcolor': "white",
                     'xtick.color': "white",
                     'ytick.color': "white" ,
                     'font.size': 13})      #change text color and size for better readability
plt.show()
```

{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../imgages/graph_output.png" width=450">
</p>

As such, we can see that the highest average arrival delay is registered in June, with the second highest in February, while September and October register negative values, which means that on average, arrivals were ahead of schedule.

{{% summary %}}

`dask` is a Python library suitable to use when dealing with larger datasets that don't fit the memory. It uses lazy evaluation, which means it doesn't execute operations or commands until actually necessary. Most of the functions are the same as in `pandas`, but remember to add `.compute()` after them if you want `dask` to compute the result at that point in your code.

{{% /summary %}}

## See also

For more resources on `dask` check out these links:

- [Dask documentation](https://docs.dask.org/en/stable/)
- [Dask forum](https://dask.discourse.group/)
