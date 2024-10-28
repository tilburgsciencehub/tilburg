---
title: "HPC TiU for Cloud Computing"
description: "A free cloud solution from Tilburg University for heavy computation tasks."
keywords: "cloud, virtual computers, HPC TiU, infrastructure, parallel, research cloud"
weight: 1
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /configure/research-cloud
---

# HPC TiU: Overview

HPC TiU Computing is a service by Tilburg University's Library and IT Services (LIS).

The environment consists of powerful servers on which researchers can interactively work on data and run statistical computations. This is a Windows-based environment, which looks and feels like a regular Windows desktop. It's accessible through this [web portal](https://rdweb.campus.uvt.nl/RDWeb/webclient/).

<p align = "center">
<img src = "../images/blade.png" width="500">
<figcaption> Pros and Cons of Using HPC TiU </figcaption>
</p>

### How to Access HPC TiU?

You can [request access to HPC TiU](https://servicedesk.uvt.nl/tas/public/ssp/content/detail/knowledgeitem?unid=db72c119bf344fb78a196d5b6c669ecc) via the IT Service Desk and filling in a form. Access for external researchers is possible. The guest researcher needs to have a Tilburg University username, and a so-called PNIL-account (staff-not-on-payroll).
These accounts can be requested at the HRM department.

Once your request is approved, you can access HPC TiU:

- On a **Windows, macOS, ChromeOS or Linux** computer enter the following [URL](https://rdweb.campus.uvt.nl/RDWeb/webclient/) in a recent version of your web browser and sign in with your TiU credentials.

**If this doesn't work**, proceed with the following:

- On a **Windows** computer use the following [URL](https://rdweb.campus.uvt.nl/RDWeb/webclient/) in web browser and sign in with your TiU credentials (campus\TiU username)

- On a **macOS** computer use Microsoft Remote Desktop Client for Mac (install from App Store), use this web feed [URL](https://rdweb.campus.uvt.nl/RDWeb/feed/webfeed.aspx) and sign in with your TiU credentials (campus\TiU username)

{{% warning %}}
**Scheduled maintenance**

Every **Friday after the 2nd Tuesday of the month** the TiU HPC servers will be put offline for maintenance. You will receive an email reminder each month.

Do **NOT** run your analyses when maintenance is performed, because unsaved work will be lost.

Moreover, each month during the maintenance period, **all personal data stored locally on HPC TiU on scratch drives (D:) will be erased!** Therefore, you should back up your files before.
{{% /warning %}}

### Where to Save your Files?

**M / S / T drive**

- Use M / S / T disc for storing data that must be retained.

**D drive (Scratch)**

- Use only the D-disk (Scratch) for temporary data storage.
  During standard (monthly) maintenance, the D drive is deleted.

**C drive**

- The C drive is only intended for the Operating System and Applications.

**E drive**

- The E-disk has been used since 12-10-2018 to store the local user profiles. (This is because of possible filling up of the C-drive and thus undermining the entire server).
- The E-disk contains the user profiles (with, for example, python packages). This E-disk is automatically deleted on restart.

{{% tip %}}
Here are some additional cloud computing solutions you might want to check out to level up your research infrastructure: [SURFsara's LISA Cluster](lisa_cluster.md) and [SURFsara's Cartesius Cluster](cartesius_cluster.md)
{{% /tip %}}
