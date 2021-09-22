---
title: "Principles for Good Coding"
description: "Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong."
keywords: "style, optimize, definition, human"
weight: 1
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code
---

## Write programs for people, not computers

Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong.

- Organization
    - Define functions that do one mayor step each, instead of one giant script doing everything
    - Write short scripts that do one task each
    - Document only what your code **doesn't** say, but nothing else
- Style
    - Use meaningful and short variable names
    - Use consistent code and formatting styles (oneExample, one_example, example-one)
    - Make use of indents in your code

## Define things once and only once

Let computers repeat and execute tasks.,

- Rule of 3: if you copy-paste code 3 times or more, write a function instead.
- If you do things often, automate them
    - e.g., by using scripts, macros, aliases/variables
    - write a dictionary with definitions
- Use build tools to [automate workflows](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/automation/)

## Use a version control system

- Add all inputs, but no outputs/generated files
    - DO: everything created by humans, small data inputs
    - DON'T: things created by the computer from your inputs (generated files; those will be [reproduced via a workflow](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/automation/)). Also [do not version large data inputs](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/directories/).
- Work in small changes
    - Create [snapshots/commits](/building-blocks/share-your-results-and-project/use-github/versioning-using-git/) in small and logical steps. This will allow you to go back in time if necessary, and to understand progression.
-  Use an issue tracking tool to document problems (e.g., such as the *Issue* tab on GitHub; email is not an issue tracker!)

## Optimize software only after it works correctly

Even experts find it hard to predict performance bottlenecks.

- Get it right, then make it fast
- Small changes can have dramatic impact on performance
- Use a profile to report how much time is spent on each line of code

## Be a good code citizen
Team members should take the time to improve code they are modifying or extending even if they did not write it themselves. A core of good code plus a long series of edits and accretions equals bad code. The problem is that the logical structure that made sense for the program when it was small no longer makes sense as it grows. It is critical to regularly look at the program as a whole and improve the logical structure through reorganization and abstraction. Programmers call this “refactoring.” Even if your immediate task only requires modifying a small part of a program, we encourage you to take the time to improve the program more broadly. At a minimum, you should guarantee that the code quality of the program overall is at least as good as it was when you started. A resource on how to implement refactoring can be found [here](https://refactoring.guru/refactoring/).

## Keep it short
- No line of code should be more than 100 characters long.
  - All languages we work in allow you to break a logical line across multiple lines on the page (e.g, using `///` in Stata or `...` in Matlab).

{{% tip %}}
   Set your editor to show a “margin” at 100 characters.
{{% /tip %}}
- Functions should not typically be longer than 200 lines.

## Language-specific style guides
### Python
We follow Python's style guide [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations). Also we:

* Use docstrings for functions whose purpose may be unclear or that will be used outside of their own modules

Supplemental resources:

* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/), especially the sections on [coding style](http://docs.python-guide.org/en/latest/writing/style/) and [packaging conventions](http://docs.python-guide.org/en/latest/writing/structure/).

* [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html), especially recommendations concerning [string formatting](https://google.github.io/styleguide/pyguide.html#Strings) and the rule to always explicitly close [files and sockets](https://google.github.io/styleguide/pyguide.html?showone=Files_and_Sockets#Files_and_Sockets).

Additional notes:

* When opening text files for writing or appending text, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "wb"` or `mode  =  "ab"` respectively to  write in binary mode. This improves portability across operating systems.

* When opening text files for reading, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "rU"` to enable universal newline support.

### R
We follow the general guidelines in [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml).

Exceptions:
* We do not follow their naming conventions (don't use dots, and underscores or camel-case are fine).
* See [conventions for line length](https://github.com/tilburgsciencehub/onboard/wiki/Code#keep-it-short)
* We do not require that all functions have a comment block describing their uses, though these are encouraged when the purpose of a function would not be clear or where it will be used outside of the file in which it is defined.

### Stata
We use two coding styles in Stata: a linear format for very short or simple scripts, and a functional style for longer or more complex scripts.

The linear format looks something like this:

```{stata}
*****************************
* Prepare data
*****************************
* Format X variables
... 
* Format Y variables
... 
*****************************
* Run regressions
*****************************
... 
*****************************
* Output tables
*****************************
 ...
```

If you include a comment as a header like this for one major block of code, you should include a similar header for every block of code at the same logical place in the hierarchy. This is a case where redundant comments are allowed. The comments are not there to provide information, but to make the code easy to scan.

In the functional style in Stata, we enclose code within program... end blocks. The first program is always called “main,” and the .do file always ends with an “Execute” step.

The functional style looks like this:

```{stata}
* PROGRAMS

program main
    prepare_data
    run_regressions
    output_tables
end

program prepare_data
    X = format_x_vars
    Y = format_y_vars
    ...
end

program format_x_vars
    ...
end

program format_y_vars
    ...
end

program run_regressions
    ...
end

program output_tables
    ...
end

* EXECUTE
main
```

The `main` command must come at the end of the script is because Stata (like Python) reads in programs in order of appearance.

In this example, these “functions” are really just blocks of code: they do not accept any inputs and outputs. But within this structure it is easy to add “syntax” commands to individual programs to define inputs and use “return” calls to pass back outputs. Functions in Stata should follow all the usual rules discussed in the *Code and Data* manual for clear, logical abstraction. You should pay special attention to the input/output structure, making sure your functions increase rather than decrease the readability of code. (Because Stata’s way of passing inputs and outputs is so clunky, it is very easy to end up with lots of long argument lists and local variables that are actually harder to read than a simple linear version of the code.)

In *Code and Data*, we discuss the principle that functions should be “shy.” Stata poses a special problem in this respect, because the data in memory is by definition a global variable. From the following code

```{stata}
use x y z using autodata.xls, clear
prepare_data
update_variables
merge_new_data 
regress productivity y_average z_average
```

there is no way to tell what are the inputs and outputs to the `prepare_data`, `update_variables`, and `merge_new_data` functions and no way to tell where the `productivity`, `y_average`, and `z_average` variables came from. When possible, write functions that only operate on variables that are explicitly passed to the function and do not otherwise touch the data in memory; if a function creates new variable(s), the names of these variables can be specified as part of the function call. This should always be true of ado files; for programs only defined and used within a given .do file, it’s a matter of judgment.


#### Merging

  *  By default, we should use Stata’s built-in merge command

  *  In older versions of Stata, the merge command was not robust, and we therefore used the add-on command `mmerge` instead. Much of our old code uses mmerge. The only cases we should use mmerge in new code is when we require functionality like the `urename()` option that does not exist in the built-in merge command.

  *  Guidelines for using `merge`

      *  Always specify the type of merge (`1:1`, `m:1`, or `1:m`). Failing to specify the merge type calls the old, non-robust version of merge.

      *  Never do many to many (`m:m`) merges, or at least, only do them when you have a very good reason.

      *  Always include the `assert()` option to indicate what pattern of matched observations you expect.

      *  Always include the `keep()` option to indicate which observations are to be kept from the merged data set.

      *   Whenever possible, include the `keepusing()` option and enumerate explicitly what variables you intend to be adding to the dataset; you can include this option even when you are keeping all the variables from the using data.

      *   Use the `nogen` option except when you plan to explicitly use the `_merge` variable later. You should never save a dataset that has `_merge` in it; if you need this variable later, give it a more informative name.

      *  You should follow analogous rules for `mmerge`. E.g., you should always specify the type() option.


#### Miscellaneous

  *  Always use forward slashes (`/`) in file paths. (Stata allows backslashes (`\`) in file paths on Windows, but these cause trouble on non-Windows OS’s.)

  *  Use `preserve`/`restore` sparingly. Excessive use can make code hard to follow; explicitly saving and opening data files is often better.

  *  We should always use `save_data`, our custom version of Stata’s save command when saving datasets to /output/. The ado file and its help file can be found in the `/gslab_misc/ado/` directory of our `gslab_stata`
GitHub repository. `save_data` replaces both `save` and `outsheet`, the standard Stata commands and requires the user to specify a key for the file. The command confirms that the key(s) are valid, places the keys at the top of the variable list, and sort the file by its key(s). File manifest information is stored in a log file if there is an output folder.

  *  When the number of variables needed from a dataset is not too large, list the variables explicitly in the `use` command.

*Content based on Ulrich Bergmann, Matteo Courthoud, Lachlan Deer (2020), [Introduction and Motivation, Programming Practices for Research in Economics](https://github.com/pp4rs/2020-uzh-course-material/blob/master/00-intro/intro.pdf), University of Zurich.*

*The main principles we follow in writing code are summarized in [this Building Block](https://tilburgsciencehub.com/write/good-code) and the document [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf). See especially the Code Style appendix and chapters 1, 2, 6, and 7.*
