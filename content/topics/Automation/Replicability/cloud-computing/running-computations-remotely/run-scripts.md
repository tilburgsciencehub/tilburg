---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
title: "Run Scripts"
indexexclude: "true"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 104
draft: false
aliases:
  - /learn/cloud/run-scripts
  - /topics/more-tutorials/running-computations-remotely/run-scripts
---

# Run Scripts

If you opted for the default Amazon Linux 2 AMI, you probably need to install some additional software to be able to execute your code files. To install Python 3 and any other packages on your EC2 instance, run the following commands:

{{% codeblock %}}

```bash
# install Python
sudo yum install python3

# install a single package
sudo python3 -m pip install <PACKAGE_NAME>

# install multiple packages from txt file
sudo python3 -m pip install -r requirements.txt
```

{{% /codeblock %}}

Next, you can run your scripts from the command line like you're used to with `python3 <SCRIPT_NAME>.py`.

{{% tip %}}
One of the key advantages of using a VM is that you can leave it running indefinitely (even if you shut down your laptop!). Take a look at the [task scheduling](../../../automation-tools/task-automation/task-scheduling.md) building block to learn how to use crontab to schedule recurring tasks (e.g., run a Python script that scrapes a website every day at 3 AM). Keep in mind that the time at your VM may differ from your local time because the data center that hosts the VM is located in another time zone (tip: run `date` to find out the UTC time).
{{% /tip %}}

{{% tip %}}
Check out [this building block](../rstudio-aws.md) to learn how to use [Docker](../../Docker/docker.md) to launch R on the instance to run your R scripts.
{{% /tip %}}
