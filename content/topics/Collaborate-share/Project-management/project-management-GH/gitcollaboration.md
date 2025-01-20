---
title: Use Git for LaTeX Collaboration and Version Control 
description: Learn the advantages of using Git with LaTeX for free 
collaboration, quicker compile time, and version control.
keywords: "Git, LaTeX, Overleaf, Collaboration, Document, Scientific"
date: 2025-01-20
weight: 2
author: "Ian McGettigan"
aliases:
  - /use/git
  - /collaborate/git
---

## Overview <!-- Goal of the Building Block -->

Using Git to collaborate on documents has several advantages over using
Overleaf. Overleaf's free plan is rather limited, requiring users to pay
for collaboration and larger documents. Git is free. Working on documents
locally also improves upon Overleaf's slower compilation time. Overleaf
also requires an internet connection, and is susceptible to crashes. With
Git one can work locally. Learning Git may seem difficult, but it is 
actually quite easy. Its advantages over Overleaf make it worth spending
half an hour learning. This article teaches the basics, including all
commands, so you can always refer back to it for future reference.

## Instructions

1. Create a GitHub account.
2. Create a repository. Go to your profile, and click the plus button
in the top right, and then click "New repository."
- Follow the on-screen instructions.
- Open Terminal and run the following commands:
```bash
cd ~/Documents/
mkdir NameOfRepository
cd NameOfRepository
git init
vim DocumentName.tex # Create and compile
git add .
git branch -M main
git remote add origin https://{your-username}/{repo-name}.git
git push -u origin main
```
- You can now view your updated repository at the link above. 

### General Workflow

1. Share the repository with your collaborators. They will have to 
clone the repository by running `git clone https://github.com/username/repo.git/`, replacing the username and repo.git with the actual names.
I recommend doing this in a folder you will remember, e.g., 
`~/Documents/project1/`
2. Change directory into the repository: `cd ~/path/to/repo/`
3. Pull all changes: `git pull`
5. Add all changes in your preferred editor. For working in the terminal,
I recommend using Vim with Vim-TeX and UltiSnips. For more details, please
look at [Gilles Castels' Blog](https://castel.dev/post/lecture-notes-1/)
6. After you're finished, commit your changes by running 
`git commit -m "some message describing your changes"`. The message itself
is unimportant, but can help to organize your version history, should you
wish to go back to previous versions easily.
7. Push your changes. It is not enough to commit them; you must also
push them: `git push`.
8. Your collaborators will repeat steps 1–7. It is very important
to pull all changes before adding your own.

**NOTE**: If you add a folder or dataset or any new file, it is not 
enough to run `git commit`. You must run `git add blank.rmd` and then
commit and then push. 
