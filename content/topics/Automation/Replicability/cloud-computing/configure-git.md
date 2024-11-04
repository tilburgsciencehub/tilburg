---
title: "Setting Up a New Workspace, Configuring Git and Adding Research Drive on Research Cloud"
description: "Learn how to set up a new workspace/VM instance on Research Cloud and configure Git on the instance."
keywords: "surf, rd, rclone, large files, webdav, store, storage, git, configure"
weight: 9
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
draft: false
aliases:
  - /setup/research-drive
---

# Overview

This building block takes you through the steps to configure Git on a new virtual machine (VM) on Research Cloud once you have finished setting up your account and creating a workspace following [these steps](https://tilburgsciencehub.com/topics/automation/replicability/cloud-computing/getting-started-research-cloud/).

## Setting up SSH key authentication

### Step 1: Create your SSH keys

You can access and write data in remote repositories on Github using SSH (Secure Shell Protocol). When you connect via SSH, you authenticate using a private key file on your local machine. To create the SSH key:

- Go to the directory `~/.ssh` using `cd .ssh` command on the terminal and create a ‘config’ file using `touch config` command.
- Then, create your SSH keys with the `ssh-keygen` command. Click enter to save the key in the default directory specified or mention an alternative directory if you would like to save it elsewhere. Then you may enter a passphrase for your private key, providing an additional layer of security.
- Now, we have generated two keys that are required for SSH authentication: private key (id_rsa) and the public key (id_rsa.pub).

  <video width="500" height="300" controls>
    <source src="../images/ssh-keygen.mov" type="video/mp4">
  </video>

{{% tip %}}
You could also create additional storage drive and link it to the instance when creating one. Then make sure to save the SSH key files in this external drive. This will be helpful when for example, you delete your current VM and mount this external drive to a new VM. In this case, you need not configure git from scratch again.
{{% /tip %}}

### Step 2: Configure SSH

If you configure multiple keys for an SSH client and connect to an SSH server, the client can try the keys one at a time until the server accepts one but this process doesn’t work because of how Git SSH URLs are structured. Hence, you must configure SSH to explicitly use a specific key file. To do this, edit your `~/.ssh/config` file using the `nano` command and copy-paste the following and press F3 to save.

```
# Host github.com
#   User git
#   Hostname github.com
#   IdentityFile ~/.ssh/id_rsa
```

{{% warning %}}
Make sure to change the ‘IdentityFile’ to the directory where the id_rsa key is saved.
{{% /warning %}}

<video width="500" height="300" controls>
  <source src="../images/nano.mov" type="video/mp4">
</video>

### Step 3: Adding a New SSH key to your Github Account

- Open the public key using the `cat` command and copy the SSH public key to your clipboard.

<video width="500" height="300" controls>
  <source src="../images/copy-paste-key.mov" type="video/mp4">
</video>

- Go to your Github page and click on `Settings` > `SSH and GPG keys` > `New SSH key` and paste the key here.

<video width="500" height="300" controls>
  <source src="../images/config-key-on-git.mov" type="video/mp4">
</video>

- Lastly, to make sure the key file is readable and writable only by the owner run `chmod 600 ~/.ssh/config`
- Now, clone the repository using the SSH URL

<video width="500" height="300" controls>
  <source src="../images/git clone.mov" type="video/mp4">
</video>

### Step 4: Adding Research Drive

To use Research Drive, you should first make sure that you have an account, or a collaborator has given you access to Research Drive. If so, you can log in and view/upload files using instructions here: https://wiki.surfnet.nl/display/RDRIVE/How+to+login

You should then be able to connect research drive on your workspace following these instructions:

https://servicedesk.surf.nl/wiki/display/WIKI/Connect+Research+Drive (In most cases, you would be using the "branded" research drive instance (e.g., provided by Tilburg).

{{% tip %}}
If you do not see any files displayed in the Research Drive folder of your workspace, there is some issue with mounting. Please follow the steps above to re-link Research Drive to your collaborative organization (CO) and it should work.
{{% /tip %}}
