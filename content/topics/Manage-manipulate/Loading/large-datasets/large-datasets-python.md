---
title: "Handle Large Datasets In Python"
description: "Dask is a Python library for parallel computing, which is able to perform computations on larger-than-memory datasets."
keywords: "Python, pandas, Dask, parallel computing, partitions, data preparation, big data, large datasets, memory, RAM, dataframe, numpy, array"
date: 2022-10-10T22:01:14+05:30
draft: false
weight: 1
author: "Paulina Ambroziak"
authorlink: "https://www.linkedin.com/in/ambroziakp/"
aliases:
  - /import/large-datsets-python
---

## Overview

Discover Dask, a valuable solution to handle large datasets in Python that provides parallel computing functionalities to popular libraries such as Pandas and Numpy. In this building block, you will be introduced to the package Dask. Moreover, you will learn some of Dask's fundamental operations that will allow you to handle and work with large datasets in Python in a much more effective and efficient manner.

## Memory Errors when working with large datasets

When trying to import a large dataset to dataframe format with `pandas` (for example, using the `read_csv` function), you are likely to run into `MemoryError`. This error indicates that you have run out of memory in your RAM. `Pandas` uses in-memory analytics, so larger-than-memory datasets won't load. Additionally, any operations performed on the dataframe require memory as well.

Wes McKinney - the creator of the Python `pandas` project, noted in his [2017 blog post](https://wesmckinney.com/blog/apache-arrow-pandas-internals/):
{{% tip %}}
`pandas` rule of thumb: have 5 to 10 times as much RAM as the size of your dataset
{{% /tip %}}

You can check the [memory usage](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html) of each column of the `pandas` DataFrame (including the dataframe's index) with the following line of code:
{{% codeblock %}}

```python
DataFrame.memory_usage(deep=True)
```

{{% /codeblock %}}

Moreover, `pandas` only uses a single CPU core to perform computations, so it is relatively slow, especially when working with larger datasets.

## Dask library

One of the solutions to memory errors is to use another library. Here `Dask` comes in handy. `Dask` is a Python library for parallel computing, which can perform computations on large datasets while scaling well-known Python libraries such as `pandas`, `NumPy`, and `scikit-learn`.

`Dask` splits the dataset into a number of partitions. Unlike `pandas`, each `Dask` partition is sent to a separate CPU core. This feature allows us to work on a larger-than-memory dataset but also speeds up the computations on that dataset.

### Installation

`Dask` is included by default in the Anaconda distribution. Otherwise, you can also use pip to install everything required for the most common uses of `Dask` or choose to only install the `Dask` library:

{{% codeblock %}}

```shell
python -m pip install "dask[complete]"    # Install everything
python -m pip install dask                # Install only core parts of Dask
```

{{% /codeblock %}}

Alternatively, see other installing options [here](https://docs.dask.org/en/stable/install.html).

### Dask DataFrame

`Dask` DataFrame is a collection of smaller `pandas` DataFrames, split along the index.

The following are the fundamental operations on the `Dask` DataFrame:

{{% codeblock %}}

````python
# import the Dask DataFrame module
import dask.dataframe as dd

# read a single CSV file
df = dd.read_csv('/path/example-01.csv')
# read multiple CSV files at once
df = dd.read_csv('/path/example-*.csv')

# check the number of partitions
df.npartitions
# change the number of partitions
df = df.repartition(npartitions=10)

# save the Dask DataFrame to CSV files (one file per partition)
df.to_csv('/path/example-*.csv')
# save the Dask DataFrame to a single CSV file (by converting it to pandas DataFrame first)
df.compute().to_csv('/path/example.csv')
{{% /codeblock %}}

`Dask` DataFrame utilizes a great portion of the `pandas` API; therefore, there are a lot of similarities in use. However, `Dask` DataFrame doesn't support all `pandas'` features.

For the full list of operations, see the [Dask Dataframe documentation](https://docs.dask.org/en/stable/dataframe-api.html).

### Dask vs pandas
The main difference between `Dask` and `pandas` is that in `Dask`, each computation requires you to call the `compute()` function. This is because `Dask` uses so-called lazy evaluation, meaning that the evaluation of an expression will not be executed unless explicitly requested to do so.

For example, this is how you would get column mean in `pandas` and `Dask`:

{{% codeblock %}}
```python
# get column mean in pandas
df['column1'].mean()

# get column mean in Dask
df['column1'].mean().compute()
````

{{% /codeblock %}}

To convert a `Dask` DataFrame to a `pandas` DataFrame, you call the `compute()` function on that dataframe:
{{% codeblock %}}

```python
df = df.compute()
{{% /codeblock %}}

After that, you continue working with `pandas`. You usually want to do this after reducing the large dataset with `Dask` (for example, by selecting a subsection) to a manageable level.
{{% warning %}}
The entire dataset must fit in the memory before applying the `compute()` function.
{{% /warning %}}

### Dask Array
[Dask Array](https://docs.dask.org/en/stable/array.html) implements a large subset of `NumPy` API, breaking up the large array into many small arrays. You can use `Dask` Array instead of `NumPy` if you are out of RAM or experiencing performance issues.

You can see the list of functionalities [here](https://docs.dask.org/en/stable/array-api.html).


{{% summary %}}

- With `Dask` you can handle and manage efficiently large datasets in Python.

- `Dask` divides datasets into partitions and distributes the work across multiple CPU cores.

-Working with `Dask` DataFrames is user-friendly for `pandas` users due to extensive use of the `pandas` API.

- However, `Dask` DataFrame doesn't support all pandas functionalities. This makes it an interesting option to Reduce datasets with Dask first, and then switch to pandas for detailed analysis.

{{% /summary %}}

### See Also

[Practical Example Using Dask](dask-in-action.md)
```
