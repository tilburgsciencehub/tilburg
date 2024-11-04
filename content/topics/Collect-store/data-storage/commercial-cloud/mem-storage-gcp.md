---
title: "Handle storage within your Google Cloud instance"
description: "After configuring a Google Cloud instance with GPUs, learn to import heavy files from Google Drive"
keywords: "Docker, Environment, Python, Jupyter notebook, Google cloud, Cloud computing, Cloud storage, GPU, Virtual Machine, Instance, Bucket, Storage"
weight: 2
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2023-09-16
aliases:
  - /manage/storage
---

## Overview

In this article, we build upon the foundational steps outlined in [Configure a VM with GPUs in Google Cloud](https://tilburgsciencehub.com/topics/automation/replicability/cloud-computing/config-vm-gcp/).

After configuring our instance, we may find the necessity to manage large files proficiently.

In this guide, you will learn how to:

- Connect our Docker container with Google Cloud Storage using GCSFuse.
- Use Google Colab for seamless file transfers between Google Drive and Google Cloud Storage.

## Connect the Docker container to a GCS bucket

[Storage buckets](https://cloud.google.com/storage/docs/buckets) are the native storage units of the Google Cloud platform. Linking them to your virtual machine offers integrated and efficient data management, simplifying scaling, backup, and access from anywhere in the Google Cloud infrastructure, eliminating, for example, the need to perform manual uploads/downloads via the Google Cloud's browser interface.

To do this, first of all, you will need to install [GCSFuse](https://github.com/GoogleCloudPlatform/gcsfuse) in your instance by running the following code:

{{% codeblock %}}

```bash
#1
$ export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

#2
$ sudo apt-get update

#3
$ sudo apt-get install gcsfuse
```

{{% /codeblock %}}

Now, create a new directory in your virtual machine, which will be the one connected to your bucket. After that, you can run the following, substituting 'YOUR_BUCKET' with the name of the storage bucket you wish to connect with your instance, and 'PATH_TO/NEW_DIRECTORY' to the path of the newly created directory that will host that connection:

{{% codeblock %}}

```bash
$ sudo gcsfuse -o allow_other YOUR_BUCKET PATH_TO/NEW_DIRECTORY
```

{{% /codeblock %}}

This code will tell GCSFuse to synchronize your new directory with your bucket. Then, you would be able to store any output produced in your projects in this new directory that you just created in your instance and it will be immediately at your disposal within your GCS bucket, and vice versa.

## Import large files: Use Google Colab as a bridge

The transfer and management of large files can be challenging due to extended upload/download durations. Yet, having connected your Google Cloud virtual machine to your storage buckets, you can swiftly transfer files that you already have hosted on **Google Drive** and **GCS Buckets** (And in turn to your virtual machine as well) using **Google Colab** as a bridge.

This bypasses the need to manually Download/Upload files from Drive to your local machine and then to your cloud instance, potentially saving you significant amounts of time in the process.

It is suggested to utilize the same account for all Google tools. Doing so simplifies the authentication process and prevents potential permission issues, fostering a more seamless workflow.

{{% tip %}}
**Copy all directories you need**

When synchronizing the bucket with your directory inside the container, if your bucket contains other directories as well, the command `$ sudo gcsfuse -o allow_other your-bucket volume_path/new_dir/` might not copy those directories.

Try `$ sudo gcsfuse --implicit-dirs -o allow_other your-bucket volume_path/new_dir/` to make sure the implicit directories are also included if you want them to.

{{% /tip %}}

To start with, make sure your bucket is created. To do so, you can follow [these](https://cloud.google.com/storage/docs/creating-buckets) short guidelines.

To continue, launch a notebook in **Google Colab**, preferably the one you plan to run on your instance later. This approach helps you maintain a record of the code you've used.

Subsequently, to mount your **Google Drive** to this notebook, use the following code:

{{% codeblock %}}

```python
from google.colab import drive
drive.mount('/content/gdrive')

```

{{% /codeblock %}}

Next, we authenticate our user:

{{% codeblock %}}

```python
from google.colab import auth
auth.authenticate_user()

```

{{% /codeblock %}}

After, we set our **project ID**. This is the identifier corresponding to your **GCS bucket** that you intend to populate with files:

{{% codeblock %}}

```python
project_id = 'your_project_id'
!gcloud config set project {project_id}

```

{{% /codeblock %}}

The `gcloud config set project {project_id}` command configures the gcloud command-line tool to use the specified **project ID** by default.

Finally, we define our bucket's name and use the `gsutil -m cp -r` command to recursively copy the directory you're interested in sending from our mounted **Google Drive** to our specified **GCS bucket**:

{{% codeblock %}}

```python
bucket_name = 'your_bucket_name'
!gsutil -m cp -r <copy your directory path here>/* gs://{bucket_name}/
```

{{% /codeblock %}}

The output of this last cell will say at the end _"Operation completed..."_.

Now your data should be available in your **GCS bucket** and can be accessed from your Google Cloud instance. Refresh your bucket webpage and confirm it.

After following the steps outlined so far, you will be able to import your files and execute your code within the Docker container.

{{% summary %}}

**Efficiently handle large files in Google Cloud:**

- **1.** Integrate Docker with GCS bucket.
- **2.** Utilize Google Colab for seamless file transitions from Drive to bucket.

{{% /summary %}}

## Additional Resources

- [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs)
- [GCSFuse GitHub Repository](https://github.com/GoogleCloudPlatform/gcsfuse)
