# Git & GitHub Complete Guide

## Table of Contents

1. Introduction
2. What is Git?
3. What is GitHub?
4. Git vs GitHub
5. Git Architecture
6. Working Directory, Staging Area & Repository
7. Installing Git
8. Creating Your First Repository
9. Cloning a Repository
10. Git Status
11. Git Add
12. Git Commit
13. Git Reset
14. Git Remove (rm)
15. Viewing History
16. Branches
17. Merging
18. Merge Conflicts
19. Checkout
20. Git Diff
21. Remote Repositories
22. Push
23. Fetch
24. Pull
25. Git Restore
26. Git Stash
27. Git Revert
28. Git Rebase
29. Pull Requests
30. Git Workflow Summary
31. Command Cheat Sheet

---

# 1. Introduction

Git is a **Version Control System (VCS)**.

It records:

* What changed
* Who changed it
* When it changed
* Previous versions
* Complete project history

Git allows developers to safely experiment without losing previous work.

---

# 2. What is Git?

Git is software that tracks file changes.

It works with:

* Source code
* Text files
* Images
* Videos
* Documents
* Almost any file

Example:

```
Day 1

index.html

Hello World
```

After one month:

```
Hello World!!
```

Git still remembers the original version.

You can restore it anytime.

---

# 3. What is GitHub?

GitHub is an online platform that stores Git repositories.

Think of it like:

* Google Drive for code
* OneDrive for source code
* Cloud backup for Git repositories

GitHub enables:

* Team collaboration
* Sharing code
* Backup
* Pull Requests
* Code Reviews

---

# 4. Git vs GitHub

| Git                    | GitHub                 |
| ---------------------- | ---------------------- |
| Version Control System | Cloud Hosting Platform |
| Runs locally           | Runs online            |
| Tracks changes         | Stores repositories    |
| Free software          | Web service            |

Video analogy:

> Git is the coffee.

> GitHub is the coffee shop.

---

# 5. Git Architecture

Git has two parts.

## Local

Your computer.

Contains:

```
Working Directory

↓

Staging Area

↓

Local Repository
```

---

## Remote

Cloud server

Usually:

* GitHub
* GitLab
* Bitbucket

---

# 6. Git Workflow

```
Working Directory

↓

git add

↓

Staging Area

↓

git commit

↓

Local Repository

↓

git push

↓

Remote Repository (GitHub)
```

---

# 7. Working Directory

The folder where you write code.

Example:

```
Git-1

├── 1.txt
├── 2.txt
└── myfolder
      └── 3.txt
```

Everything happens here first.

---

# 8. Staging Area

Temporary place before saving.

Think of it as:

> "I'm ready to save these changes."

Move files here using:

```
git add
```

---

# 9. Repository

Repository stores:

* Complete history
* Commits
* Versions
* Branches

There are two types:

Local Repository

```
.git
```

Remote Repository

GitHub

---

# 10. Installing Git

Verify installation:

```bash
git --version
```

Example:

```bash
git version 2.45.1
```

---

# 11. Create First Repository

Create folder

```bash
mkdir Git-1
```

Move inside

```bash
cd Git-1
```

Initialize Git

```bash
git init
```

Output:

```
Initialized empty Git repository
```

Git creates

```
.git
```

hidden folder.

---

# 12. Create Files

Example from video

```
Git-1

1.txt
2.txt

myfolder
   3.txt
```

Contents:

```
1.txt

1

2.txt

2

3.txt

3
```

---

# 13. Clone Repository

Instead of creating locally:

```bash
git clone https://github.com/user/Git-Journey.git
```

Git downloads:

* Repository
* History
* Branches

---

# 14. Git Status

Check current changes.

```bash
git status
```

Example:

```
modified:

1.txt

2.txt
```

Git always tells you:

* Modified files
* Deleted files
* Untracked files
* Staged files

---

# 15. Git Add

Moves files to staging.

## Add everything

```bash
git add --all
```

or

```bash
git add -A
```

Stages:

* Modified files
* Deleted files
* New files

---

## Current Folder

```bash
git add .
```

Stages only current directory.

Example

Inside:

```
myfolder
```

Only

```
3.txt
```

gets staged.

---

## Specific File

```bash
git add 1.txt
```

---

## Specific Folder

```bash
git add myfolder/3.txt
```

---

## Extension

```bash
git add *.txt
```

Stages all txt files in current directory.

---

## Important Difference

| Command       | Behavior       |
| ------------- | -------------- |
| git add .     | Current folder |
| git add -A    | Entire project |
| git add --all | Entire project |
| git add *.txt | Only txt files |

---

# 16. Git Commit

Commit saves staged files permanently.

Syntax

```bash
git commit -m "Added login page"
```

Example from video

```bash
git commit -m "I have made some changes to the files"
```

---

## Configure Identity

Required once.

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

---

# 17. Git Reset

Unstage files

```bash
git reset
```

Undo latest commit

```bash
git reset HEAD~
```

Hard reset

```bash
git reset --hard
```

Restores project exactly like last commit.

---

# 18. Git Remove

Delete file

```bash
git rm file.txt
```

Delete forcefully

```bash
git rm -f file.txt
```

Keep file locally but stop tracking

```bash
git rm --cached file.txt
```

Delete folder

```bash
git rm -r myfolder
```

---

# 19. Commit History

Full history

```bash
git log
```

Compact

```bash
git log --oneline
```

Example

```
9fd4a6 Updated login

4c239f Added API

a82fd2 Initial commit
```

---

# 20. Branches

Main branch

```
main
```

Create

```bash
git branch development
```

List

```bash
git branch
```

Switch

```bash
git checkout development
```

---

# 21. Why Branches?

Video analogy

Main kitchen

↓

Test kitchen

↓

Merge successful recipe

↓

Serve customers

Branch = Safe place to experiment.

---

# 22. Merge

Merge changes into current branch.

Example

```
development

↓

main
```

Command

```bash
git merge development
```

---

# 23. Merge Conflict

Occurs when same lines are edited.

Example

Main

```
Hello
```

Development

```
Hi
```

Git cannot decide.

Conflict markers

```
<<<<<<< HEAD

Hello

=======

Hi

>>>>>>> development
```

Developer manually resolves conflict.

Commit after resolving.

---

# 24. Checkout

Switch branch

```bash
git checkout main
```

Switch commit

```bash
git checkout <commit-id>
```

Detached HEAD

```
HEAD detached
```

Return

```bash
git checkout main
```

---

# 25. Compare Changes

```bash
git diff commit1 commit2
```

Shows

* Added lines
* Removed lines
* Modified lines

---

# 26. Push

Upload local changes.

```bash
git push origin main
```

Upload branch

```bash
git push origin development
```

---

# 27. Fetch

Download updates.

```bash
git fetch
```

Downloads only.

Does NOT update files.

---

# 28. Pull

```bash
git pull
```

Equivalent

```
git fetch

+

git merge
```

Downloads and merges.

---

# 29. Restore

Undo local changes.

Single file

```bash
git restore 1.txt
```

Entire directory

```bash
git restore myfolder
```

Whole repository

```bash
git restore .
```

Unstage

```bash
git restore --staged file.txt
```

---

# 30. Git Stash

Temporarily save unfinished work.

Store

```bash
git stash
```

Restore and remove

```bash
git stash pop
```

Restore only

```bash
git stash apply
```

View

```bash
git stash list
```

Delete stash

```bash
git stash drop
```

### Pop vs Apply

| Pop           | Apply         |
| ------------- | ------------- |
| Restores work | Restores work |
| Removes stash | Keeps stash   |

---

# 31. Git Revert

Undo a commit safely.

```bash
git revert commit-id
```

Creates a NEW commit.

Original history remains.

Good for shared repositories.

---

# 32. Git Rebase

Moves feature branch onto latest main.

Instead of

```
Merge Commit
```

Produces

```
Clean Linear History
```

Command

```bash
git rebase main
```

### Behind the scenes

1. Finds common ancestor.
2. Temporarily removes feature commits.
3. Applies latest commits from `main`.
4. Reapplies feature commits on top.

⚠️ Avoid rebasing shared/public branches because it rewrites commit history.

---

# 33. Pull Request (PR)

Purpose:

Request merging one branch into another.

Example

```
development

↓

main
```

Steps

1. Push branch
2. Open GitHub
3. New Pull Request
4. Select Base = main
5. Compare = development
6. Review changes
7. Create Pull Request
8. Merge Pull Request
9. Confirm Merge

PR sections:

* Conversation
* Commits
* Files Changed

---

# 34. Complete Git Workflow

```
Create Project

↓

git init

↓

Create Files

↓

git status

↓

git add .

↓

git commit -m "message"

↓

git push origin main

↓

GitHub
```

---

# 35. Frequently Used Commands

```bash
git init
git clone URL
git status
git add .
git add -A
git commit -m "message"
git log
git log --oneline
git diff
git branch
git checkout branch
git merge branch
git push origin main
git fetch
git pull
git restore .
git restore --staged .
git stash
git stash pop
git stash apply
git stash list
git stash drop
git revert commit-id
git rebase main
git rm file.txt
git rm -f file.txt
git rm --cached file.txt
git reset
git reset --hard
```

---
