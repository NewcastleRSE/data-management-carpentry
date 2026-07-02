---
title: "Introduction to Data Management"
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions 

## Questions

- Why is data management important?
- How do computers organise files and folders?
- What is a file system?
- How can I use a graphical file explorer to navigate my data?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

## Objectives

By the end of this episode, learners will be able to:

- Describe common data management challenges.
- Explain how files and folders are organised on a computer.
- Navigate a file system using a graphical interface.
- Locate project data using a file explorer.
- Explain why data organisation matters for research.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Research increasingly depends on digital data. Whether you are collecting measurements in the field, analysing simulation outputs, recording interviews, working with images, or managing spreadsheets, the data you create must be stored, organised, documented, and maintained throughout its lifecycle.

Good data management makes research more efficient, more reproducible, and easier to share with collaborators. Poor data management can result in wasted time, duplicated effort, lost information, and difficulty reproducing results.

In this lesson we will work through a realistic scenario that many researchers encounter: inheriting a project from somebody else.

Over the course of the lesson we will begin with a chaotic collection of files and gradually improve it using practical data management techniques.

We will work from the outside in:

1. Organising folder structures
2. Creating meaningful file names
3. Documenting data and workflows
4. Choosing appropriate storage locations
5. Managing storage and file transfers
6. Deciding what data to keep and what to remove
7. Improving tabular data structure
8. Choosing appropriate data formats

The focus of this lesson is **not programming, data science, or statistics**. Instead, we will concentrate on practical skills that help people find, understand, share, and preserve research data.

## Scenario

Imagine the following situation.

You are a postgraduate researcher joining a collaborative research project.

One of the project's researchers has recently left the institution. Before leaving, they copied everything they thought might be important into a single folder and sent it to the team.

Unfortunately, the folder contains hundreds of files.

Some files have names such as:

```text
Data!@#$.csv
data_final_v3_LAST_ONE.xlsx
Untitled.csv
copy of DSCO1023.png
```

Some folders are called:

```text
New Folder
New Folder (2)
miscellaneous
RAW_DATA_!!!
```

There are multiple file versions, undocumented datasets, hidden folders, and no README file explaining what anything means.

Your supervisor asks:

> Can you work out what this data is, organise it, and make sure we can continue the project?

Throughout this lesson, you will take the role of the researcher trying to rescue this project.

Each episode focuses on solving one specific problem and introduces practical techniques that can be applied to your own research projects.

## Why Does Data Management Matter?

Many research projects begin with only a handful of files:

```text
experiment.xlsx
notes.docx
results.csv
```

Finding information is easy.

However, projects grow. As files accumulate, researchers typically encounter familiar problems:

- "I can't find the file I need."
- "Which version is current?"
- "Where did this data come from?"
- "Why am I running out of storage?"
- "How do I share this file?"
- "What does this dataset actually contain?"

Most of these problems are not technical problems.

They are organisational problems.

Good data management practices reduce time wasted searching for data, improve collaboration, and make research easier to reproduce.

> ## Discussion
>
> Have you ever inherited files from another researcher or returned to an old project after several months?
>
> What was the most difficult part of understanding the data?

## How Computers Store Data

Before we organise data effectively, it helps to understand how computers store information.

Computers store information in **files**.

Files are organised into **folders** (also called directories), which can contain both files and additional folders.

Together these form a **file system**.

### Visualising a File System

```text
Computer
│
└── Users
    │
    └── Alice
        │
        ├── Documents
        │   ├── Report.docx
        │   └── Notes.txt
        │
        ├── Downloads
        │   ├── Dataset.csv
        │   └── Image.png
        │
        └── Pictures
            ├── Figure1.jpg
            └── Figure2.jpg
```

Folders help organise related files in much the same way as folders in a filing cabinet.

Without folders, every file would exist in one enormous list.

A file system provides:
- Structure
- Organisation
- Navigation
- Storage

Without folders, every file on your computer would exist in one enormous list.


# Storage Locations
Files ultimately live on some form of digital storage.
Examples include:
- Internal hard drives
- Solid-state drives (SSDs)
- USB drives
- Network storage
- Cloud storage

Regardless of where files are stored physically, they are typically presented to users through the same folder-and-file structure.As a result, learning to navigate folders is a transferable skill regardless of the storage system being used


# Introducing the File Explorer

Most people interact with files through a graphical interface known as a **file explorer** or **file manager**.

Examples include:

| Operating System | File Manager |
|-----------------|-------------|
| Windows | File Explorer |
| macOS | Finder |
| Linux | Files / Nautilus / Dolphin (varies by distribution) |

In this lesson we will demonstrate using **Windows File Explorer**, but the same concepts apply to other operating systems.

## Demonstration: Opening File Explorer

The instructor should demonstrate how to open File Explorer.

### Method 1 
Click the folder icon on the taskbar.
### Method 2
Press:```textWindows Key + E```
### Method 3
Open the Start Menu and search for:```textFile Explorer```

### Windows

- Click the folder icon on the taskbar
- Press `Windows + E`
- Search for "File Explorer" from the Start Menu



# Anatomy of File Explorer
A typical File Explorer window contains several important components.

```text
+--------------------------------------------------+
| Address Bar                                      |
+--------------------------------------------------+
| Navigation Pane | File List                      |
|                 |                                |
| Documents       | Dataset.csv                    |
| Downloads       | README.txt                     |
| Pictures        | results.xlsx                   |
| Desktop         | raw_data                       |
|                 |                                |
+--------------------------------------------------+
```
## Navigation Pane
Usually found on the left-hand side.
This shows:
- Desktop
- Documents
- Downloads
- Pictures
- Shared drives
- Other folders

You can use it to jump quickly between locations.

## File List

The central area of the window.
This displays the contents of the currently selected folder.

## Address Bar
Located near the top.
Shows your current location within the file system.
For example:```textDownloads > legacy_dataset > RAW_DATA_!!!```
This helps you understand where you are and allows you to move back to previous folders.

## Search Box
Many file managers provide a search box.
Search can be useful, but it should not be your primary strategy for finding files.
A well-organised folder structure makes data easier to locate without relying on search.



# Looking Ahead

In the next episode we will examine the inherited dataset and begin improving its folder structure.
Before we can organise the files, however, we first need to locate them.



### What to Show

Demonstrate:

- Navigation pane
- File listing area
- Address bar
- Search box
- Moving between folders
- Expanding and collapsing folders

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor
>
> Do not assume learners regularly use desktop file systems.
>
> Some participants may primarily use mobile devices and may have little experience navigating folders directly.
>
> Spend a few minutes explicitly demonstrating how files and folders are organised.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Exercise: Finding the Dataset

Download the lesson dataset.

Using File Explorer:

1. Open the Downloads folder.
2. Locate the downloaded dataset.
3. Open the dataset folder.
4. Explore the contents without modifying anything.
5. Identify at least three things that seem confusing or poorly organised.

> ## Discussion

>
> Was it immediately obvious where the important data was?
>
> What information would have helped you understand the project more quickly?


::::::::::::::::::::::::::::::::::::: keypoints 

- Data management is an essential part of research practice.
- Many common research frustrations arise from poor organisation and documentation.
- Computers organise information using files and folders within a file system.
- File explorers provide a graphical way to navigate stored data.
- Understanding how files are organised is a foundation for good data management.
- A well-organised project should be understandable to collaborators and to your future self.

::::::::::::::::::::::::::::::::::::::::::::::::
