---
title: "Getting Started with Research Cloud"
description: "A free cloud solution for conducting research."
keywords: "cloud, virtual computers, SURF, infrastructure, parallel, research cloud, service desk"
weight: 5
#date: 2021-01-06T22:01:14+05:30
draft: false
author: "Shrabastee Banerjee"
authorlink: "https://sites.google.com/view/shrabastee"
aliases:
  - /configure/research-cloud
  - /get/chromedriver
---

## What is Research Cloud

Research Cloud is a highly customizable cloud solution for conducting your research. Think of it as a “free” version of Amazon EC2 or Microsoft Azure machine, but then brought to you under the Dutch National e-Infrastructure. SURF services are only available for researchers affiliated with Dutch institutions (though collaborators from any institution can be added to a project by the primary researcher).

- **What can you do with it?**
  Start virtual computers that run R or Python, attach some storage space, and share these computers with co-authors.

- **The benefits?** As a project leader:

  - You are in charge of the IT infrastructure.

  - Decide what packages are installed. Make sure that your coauthors can focus on doing their research, rather than installing packages or coping with memory problems on their laptops.

  - Research Cloud is also beneficial if you just want to work on a project on your own, by the way…

At present, SURF offers year-long “start-up” grants, which can then be renewed based on usage and feedback. For longer-term projects, they also offer the option to apply to [NWO grants](https://www.nwo.nl/en/news/call-computing-time-national-computer-facilities-2021-open-submission) that focus on computing resources.

## How to get started

{{% warning %}}

Make sure that you’re affiliated with a Dutch research institution to set up the work space for yourself.

{{% /warning %}}

1. Fill in the project [application form](https://www.surf.nl/en/access-to-compute-services). Click on "go to request portal" and login with SURFconext, selecting Tilburg University and using your TiU credentials. You will be transferred to the SURF servicedesk. On the SURF servicedesk look for "apply for access" and select "small NWO request (EINF)."

2. Once your wallet is approved, you will receive an email from SURF to set up your initial workspace. This will look like this:

![surf mail](../images/surf_mail.png)

Still waiting for your wallet to be approved? You can check the [status of your application at SurfSara's service desk](https://servicedesk.surfsara.nl).

3. Upon project approval, Surf will create a workspace and invite you to "join" that workspace via email.

4. You can access the [workspace via this portal](https://portal.live.surfresearchcloud.nl/). In the case that you cannot login via SSO, you can [create a so-called EduID yourself](https://www.surf.nl/diensten/eduid) and use this as your identity provider for logging in to the Research Cloud Portal.

5. All set up and want to learn more? Then check these detailed instructions on [how to use Research Cloud (including adding data sources)](https://servicedesk.surfsara.nl/wiki/display/WIKI/How+to+get+on+board).

## Advanced use cases

### Adding collaborators

To give students/collaborators access to a VM you have already created, you can [invite into your CO](https://wiki.surfnet.nl/display/SRAM/Invite+admins+and+members+to+a+collaboration) (collaborative organization) in [SRAM](https://sbs.sram.surf.nl/):

Once they become a member of your CO they can:

- Log in to the Research Cloud portal.
- Set up TOTP.
- See the workspaces that you have started for the CO.

### Usage of Research Drive in combination with Research Cloud

The Dutch foundation SURF offers login via SurfConext, which is an easy way to keep things consistent. While this works for Research Drive which is operated by LIS <link here>, it is not yet enabled for Research Cloud. Therefore, one would need to create a separate account through eduID (step 4 under “logging in” [here](https://servicedesk.surfsara.nl/wiki/display/WIKI/How+to+get+on+board)).

{{% warning %}}
Make sure to check your workspace from time to time using df -h to prevent memory overload. You will get an alert from SURF if the root disk is at 80% capacity. If this happens, do the following:

- Install ncdu command:
  `sudo apt-get install ncdu`

- Then run `ncdu` and it will show you the disk space usage stats and you click enter to dig deeper into each directory. Then look for cache files or other unnecessary files manually and press `d` to delete that file or directory.
- Run df -h again to check status of the disk space storage

{{% /warning %}}
