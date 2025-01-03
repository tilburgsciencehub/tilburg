---
title: "Git Branching Strategies"
description: "Explore three popular Git branching strategies: Trunk-Based Development, Feature Branching, and Git Flow. Learn their workflow, strengths, weaknesses and suitable projects and teams."
keywords: "git, github, branching, strategies, trunk-based development, feature branching, git flow, branch, branches"
date: 2023-03-11
weight: 3
author: "Paulina Ambroziak"
authorlink: "https://www.linkedin.com/in/ambroziakp/"
aliases:
  - /git/branching/strategies
  - /learn/workflow
  - /trunk-based/development
  - /feature/branching
  - /git/flow
  - /advantages/disadvantages
  - /suitable/projects/teams
---

## Overview
A **Git branching strategy** allows developers to collaborate on a project while also tracking changes and maintaining multiple versions of the codebase. There are several Git branching strategies available, each with its own set of advantages and disadvantages. The best strategy is determined by the project's and team's unique requirements. In this building block, we'll go over three popular Git branching strategies: 
1. **Trunk-Based Development**
2. **Feature Branching**
3. **Git Flow**

## Strategy 1: Trunk-Based Development

### What is Trunk-Based Development?
**Trunk-based development (TBD)** is a branching strategy in which all developers make changes directly on the `main` branch, commonly referred to as the `trunk`, which holds the project's deployable code. Developers are encouraged to commit frequently and use feature toggles* and other techniques to manage changes that are not yet ready for release. Testing is typically automated, with a focus on continuous integration (CI) and continuous delivery (CD) to ensure that code changes are thoroughly tested before they are deployed.

If a coding task requires an extended duration, possibly spanning over several days, the developer may create a branch from the `main` codebase, implement the necessary changes, and then merge it back into the `main` codebase once development is complete. However, the goal of trunk-based development is to minimize the use of feature branches and encourage developers to work collaboratively on the `main` codebase as much as possible.

#### *Feature toggle
**Feature toggles**, also known as feature flags, can be used in software development to manage features that are not yet ready for release or that need to be shown only to specific users or groups. They function like a switch that can be turned on or off to enable or disable a particular feature in the codebase.

![Trunk-Based Development](./images/trunk-based-development.png)
*Trunk-Based Development* by [Atlassian](https://www.atlassian.com/git/topics/comparing-workflows), edited / [CC BY](https://creativecommons.org/licenses/by/2.5/au/)

### Trunk-Based Development Workflow
1. **Work on the `main` codebase:** Work directly on the `main` (`trunk`) branch, rather than creating separate branches.

2. **Make small, frequent changes:** Make small and incremental changes to the codebase, which are easier to review and less likely to cause issues.

3. **Use Continuous Integration:** Integrate and test the codebase frequently in order to detect issues early, avoid conflicts, and ensure that the codebase is always in a releasable state.

4. **Merge changes frequently:** Merged changes frequently back into the `main` codebase, keeping it up-to-date and reducing the likelihood of conflicts.

### Pros and Cons

{{%table%}}
| Advantages | Disadvantages |
| --- | --- |
| Encourages collaboration and <br> rapid feedback | Can lead to conflicts and <br> integration issues if not <br> managed properly |
| Promotes early issue detection <br> and quick resolution | Requires robust automated <br> testing and continuous <br> integration practices |
| Facilitates faster feature <br> and improvement delivery | Can be difficult to roll <br> back changes once <br> integrated into `main` |
| Simplifies codebase management <br> by keeping all developers <br> on the same branch | May not be suitable for <br> larger teams or complex <br> projects |
| Reduces overhead of <br> multiple <br> `feature` branches | Single point of failure <br> if `main` becomes unstable |
{{%/table%}}

### Teams and Projects
Trunk-based development is suitable for projects with **small teams**, **short release cycles**, and a focus on **delivering new features and improvements quickly**.

## Strategy 2: Feature Branching

### What is Feature Branching?
**Feature Branching** is a commonly used workflow that involves creating a new branch for a specific feature or change in the codebase. This allows developers to work on the feature independently without affecting the `main` branch. When the feature is complete, it can be merged back into the `main` branch through a pull request. The pull request allows other team members to review the changes and suggest modifications or improvements before merging the feature into the `main` branch.

![Feature Branching](../images/feature-branching.png "Feature Branching")
*Feature Branching* by [Atlassian](https://www.atlassian.com/git/topics/using-branches/git-merge), edited / [CC BY](https://creativecommons.org/licenses/by/2.5/au/)

### Feature Branching Workflow
1. **Create `feature` branches:** Create a new branch for each feature or task you're working on. This branch should be created from the `main` branch.
2. **Work on the feature:** After creating the `feature` branch, you can start implementing the new feature by making as many commits as necessary. The branch should only contain changes relating to that particular feature.
3. **Create a pull request:** When you're finished working on the `feature` branch, you create a pull request to merge the changes into the `main` branch.
4. **Review and approve:** Other developers review the changes in the pull request and approve them if they are satisfied with the changes. Code review can help catch issues or mistakes before they are merged into the `main` branch.
5. **Merge the `feature` branch:** Once you're done working on the feature, you can merge the `feature` branch back into the `main` branch.
6. **Clean up:** After merging, you can delete the `feature` branch, as it is no longer needed.

### Pros and Cons

{{%table%}}
| Advantages | Disadvantages |
| --- | --- |
| Allows parallel feature <br> development | Managing and updating <br> numerous branches |
| Facilitates controlled <br> code review/testing | Delays in merging changes <br> into `main` due to <br> extended review |
| Ensures consistent stability <br> of the `main` branch | Can lead to conflicts due <br> to branch dependencies |
| Enhances change tracking | Extra effort to <br> synchronize branches with <br> changes in `main` |
{{%table%}}

### Teams and Projects
Feature Branching is commonly used in **collaborative software development environments** where **multiple developers** are **working on different features or tasks concurrently**.

## Strategy 3: Git Flow

### What is Git Flow?
**Git Flow** is a branching strategy that uses two main long-lived branches - `main` and `develop` - that remain in the project during its entire lifetime. Additionally, it employs several short-lived branches - `feature`, `release`, and `hotfix` - that are created as needed to manage the development process and deleted once they have fulfilled their purpose. The `main` branch is the stable production-ready code and the `develop` branch is where all development takes place. `Feature` branches are used to develop new features or changes, `release` branches are used to prepare for a new release, and `hotfix` branches are used to quickly address critical issues in the production code.

![Git Flow](./images/git-flow.png "Git Flow")
*Git Flow* by [Atlassian](https://www.atlassian.com/git/topics/comparing-workflows/gitflow-workflow) / [CC BY](https://creativecommons.org/licenses/by/2.5/au/)

### Git Flow Workflow
1. **Create the `develop` branch:** This branch will be used for ongoing development work. A `develop` branch is created from the `main` branch.
2. **Create `feature` branches:** When starting work on a new feature or bug fix, create a new `feature` branch from the `develop` branch. 
3. **Develop and merge the `feature` branch into `develop`:** Make any necessary changes to your local code on the `feature` branch. Once the feature is complete and tested, merge the branch back into the `develop` branch. 
4. **Create the `release` branch:** When it's time to prepare a new release, create a new `release` branch from the `develop` branch with a descriptive name that includes the version number, for example, `release/1.0`. Test the release thoroughly to catch any bugs or issues to ensure it's production-ready.
5. **Merge the `release` branch into `main`:** Once the release is ready, merge the `release` branch into the `main` branch and tag it with a version number. Use a pull request to ensure code reviews and approval from other team members.
6. **Repeat the process:** Once the release is complete, switch back to the `develop` branch and start the process over again with a new `feature` branch.

If a critical issue in the `main` branch is detected:
-	**Create a `hotfix` branch from `main`:** This branch is used to quickly fix critical issues or bugs in the production code that cannot wait for the next release cycle.
-	**Merge the `hotfix` branch into both `develop` and `main`:** After the hotfix is completed and tested, it is merged into both the `develop` and `main` branches to ensure that the fix is applied to both the ongoing development work and the production code.

### Pros and Cons

{{%table%}}
| Advantages | Disadvantages |
| --- | --- |
| Provides clear structure <br> for managing code changes | Can be more complex <br> than other branching <br> strategies |
| Separates ongoing development <br> from stable releases | Potential for larger <br> number of branches |
| Encourages use of short-lived <br> `feature`, `release`, and <br> `hotfix` branches | Possibility of  <br>  merge conflicts |
| Facilitates code review  <br> and testing processes | Requires a certain level  <br> of discipline and adherence <br> to process |
| Predictable development  <br> flow | Can be seen as  <br> overly prescriptive or  <br> inflexible |
{{%/table%}}

### Teams and Projects
Git Flow is particularly well-suited for **larger development teams** that are working on **complex software applications** with **long development cycles** and **multiple releases**. Smaller teams or projects with shorter development cycles may find Git Flow to be overly complex.

## Summary
{{%table%}}
| Strategy | Project Type | Team Size | Collaboration Maturity |
| --- | --- | --- | --- |
| **Trunk-Based <br>Development** | For projects with <br> frequent code changes <br> and continuous releases | Smaller <br> teams | High collaboration and  <br> communication needed,<br> as all changes are <br> made directly to `main` |
| **Feature <br>Branching** | Projects with <br> simultaneous <br> development of <br> different features | Medium or <br>large-sized <br>teams | Moderate collaboration <br> maturity, as changes <br> occur in separate <br> branches before <br> merging into `main` |
| **Git Flow** | Projects requiring <br> a structured approach  | Larger <br>  teams | High collaboration <br> maturity, as changes <br> involve multiple <br> branches and a <br> formalized release <br> process |
{{%/table%}}

{{% summary %}}
* **Trunk-Based Development** is a Git branching strategy that emphasizes frequent integration and testing on the `main` branch to ensure a high level of collaboration and continuous delivery.
* **Feature Branching** is a Git branching strategy that involves creating separate branches for individual features or changes to allow for isolation, testing, and review before merging into the `main` branch.
* **Git Flow** is a Git branching model that builds on Feature Branching by adding additional branches for managing releases and hotfixes, providing a structured approach for managing different types of changes in larger teams or more complex projects.
{{% /summary %}}
