---
title: "Cloud Computing with SURFsara's LISA Cluster"
description: "A free cloud solution from SURFsara for heavy computation tasks."
keywords: "cloud, virtual computers, HPC TiU, SURFsara, research clusters,infrastructure, parallel, research cloud"
weight: 8
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /configure/research-cloud
---

## SURFsara's LISA Cluster: Overview

The LISA cluster is a good alternative to [HPC TiU computing](https://tilburgsciencehub.com/topics/automation/replicability/cloud-computing/hpc_tiu/) where hundreds of servers can be accessed via a so-called queue system. The execution of a calculation task can be assigned to multiple servers. As soon as the number of required servers is available, the assignment is executed.

Some of the servers are linked to each other via a so-called high-speed link (infiniband). This part of the LISA Cluster is a good choice for executing an assignment that requires a great deal of communication between servers.
The support desk of SurfSARA can support in use. The support desk has templates and sample applications and offers workshops for beginners.

### Pros

- Hundreds of servers are available (cluster).
- Access to a huge amount of software.
- Users do not have to share the resources but have exclusive access.

### Cons

- Steep learning curve. Knowledge is required to be able to build an efficient job.
- No direct access to the joint network of Tilburg University.
- There may be a queue and thus waiting time.
- Less interactive because of the queue principle.

### How to Access LISA Cluster?

You can [request access via a 'small compute grant' at SURF](https://www.surf.nl/en/small-compute-applications-nwo). Applications are light-weight, and are handled within 2 weeks. Contrary to the name, the grant will award a decent amount of hours on either the HPC Cloud, a linux cluster, or the supercomputer. Larger grants are available via a more involved procedure. Support at TiU is available at digital research support, reachable via the self service portal.

Once your request is approved, you can connect to LISA:

**Windows**

- There is more than one way to make a connection, we take PuTTY. If that program is not present on your system, you should install it now: go to the [PuTTY download page](https://www.putty.org/) and download putty.exe. Start PuTTY and fill in under 'Host Name (or IP address)': lisa.surfsara.nl

- Check the 'Connection type' radio button labelled 'SSH', and click the 'Open' button.

**Linux**

Open a terminal window (for Ubuntu users: you find that here: 'Accessories - Terminal'). In that terminal window, type:
{{% codeblock %}}```bash
$ ssh <your_username>@lisa.surfsara.nl

````{{% /codeblock %}}

If the ssh command cannot be found, install the ssh-client. For Ubuntu users:

{{% codeblock %}}
``` bash

$ sudo apt-get install OpenSSH-client
````

{{% /codeblock %}}

**MacOS**

Open a terminal window (You find that here: 'Applications - Utilities - Terminal'). In that terminal window, type:

{{% codeblock %}}

```bash

$ ssh <your_username>@lisa.surfsara.nl

```

{{% /codeblock %}}
