---
# tutorialtitle: "Practicing Pipeline Automation using Make"
type: "practicing-pipeline-automation-make"
indexexclude: "true"
weight: 6
title: "Dry-run of Make and First Modifications"
date: 2021-01-06T22:01:14+05:30
draft: false
keywords: "modifications, data preparation"
aliases:
  - /dry-run/pipeline-automation
  - /topics/reproducible-research/practicing-pipeline-automation-make/wipe-rerun
---

## Dry-run of Make and first modifications to the data preparation scripts

Sometimes, running a workflow may take hours, or even days. That's why `make`
supports so-called "dry-runs", which you can initiate by typing `make -n` (for NOT run).

**Watch our video to understand the intuition of dry-runs.**

{{< youtube h7f9bHnOLm0 iframe-video-margins >}}

Next, you will start to modify the scripts in this template. After all, you're working on a *template* that you're ultimately interested in *modifying* (e.g., putting in your own data). For each (major) modification, you need to test whether your changes to the source code were done correctly (i.e., that they didn't break the template). Read how in the box below.

{{% tip %}}
**Does the workflow still run? Test whether your changes to the code were correct!**

- Typically, after every (major) modification to the source code, you should test whether changes to the code were done correctly.
- In the past, we've seen many students trying to change the entire template at once, only to find out later that even the first modification wasn't correct. The key really is to take it slowly, step-by-step.
- We advocate two ways how you could test your changes ("does the project still work?"):
    - **If you're really unsure about your changes to the code**, it's best to open the relevant source file in Spyder first (or any other Python interface), and try running (parts of) it there. The benefit is that you can start playing around with bits of the code, and also have a way to access objects directly for debugging.
    - **If you have a certain level of confidence that your modifications were successful**, you can directly try running `make` in your project directory. That way, you're running the entire workflow again, and you can check how far `make` gets (e.g., whether it completes, or whether it crashes).
{{% /tip %}}

Now, you're ready to work on the practice questions. Enjoy!

### Practice questions and answers

1) Let's start modifying our workflow a little bit! For example,
instead of parsing only the first 1000 lines (which we did
to prototype our scripts - a useful thing you should try to remember!),
let's now parse the first 2000 lines, and then remove the prototyping
condition altogether! When done, run `make` to check whether your workflow works as intended. Hint: check `parse.py` for the code!

{{% tip %}}
**Using counters**
- In `parse.py`, we make use of a "counting variable", called `cnt`. We set this variable to 0 at the beginning of the script, and then increment it with 1 every time we parse a JSON object (`cnt+=1` is the same as `cnt = cnt + 1`).
- That way, for each iteration of our loop, we exactly know how many objects we have already parsed!
- Ultimately, we are using this variable to abort the loop when we have parsed 1000 objects (we consider this a reasonable amount of tweets to parse for a "prototype").
- Next to prototyping, counters are very useful for diagnosing errors. For example, your parsing script may crash while parsing, and then the value of `cnt` will show you at which object this error happened. That way, you directly know with which data you need to start debugging your code.
{{% /tip %}}

2) Let's now also add the username of the Twitter user to the parsed
CSV file. Again, check `parse.py` for the code on how to
extract attributes form the JSON Twitter data. When done, run `make` to check whether your workflow works as intended. Hint: use the
attribute `.get('user').get('screen_name')`.

## Watch the solutions here

{{< youtube EgiLBt1njo4 iframe-video-margins >}}
