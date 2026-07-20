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

:::::::::::::::::: callout

Various research funding organisations have data management and sharing policies, and they can request detailed plans in funding applications:

- [UKRI](https://www.ukri.org/who-we-are/mrc/our-policies-and-standards/research/data-management-and-sharing/) (UK)
- [Wellcome Trust](https://wellcome.org/research-funding/guidance/policies-grant-conditions/data-software-materials-management-and-sharing-policy) (UK)
- [NSF](https://www.nsf.gov/funding/data-management-plan) (US)
- [CIHR](https://cihr-irsc.gc.ca/e/54270.html) (Canada)

Guidelines for more funders are included in Newcastle University's [overview of Data Management Expectations](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/expectations/).

Newcastle University has its own policies for [postgraduates](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/pgr/) and [all research](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm).


::::::::::::::::::

::::::::::::::::::: discussion

 Have you ever inherited files from another researcher or returned to an old project after several months?

 What was the most difficult part of understanding the data?

::::::::::::::::::::


::::::::::::::::::: caution

### Legal issues with personal data

- Personal data can be requested by members of the public on mandated timescales. Would you be able to find someone's data if they requested it?
- Members of the public can request that their data be deleted. Would you be able to do so with confidence?
- Personal data can only be retained for specific purposes.

Clear data management is essential to ensure you comply with the law and keep track of important data.

:::::::::::::::::::


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

A file system provides:

- Structure
- Organisation
- Navigation
- Storage

Without folders, every file on your computer would exist in one enormous list.


## Storage Locations

Files ultimately live on some form of digital storage.
Examples include:

- Internal hard drives
- Solid-state drives (SSDs)
- USB drives
- Network storage
- Cloud storage

Regardless of where files are stored physically, they are typically presented to users through the same folder-and-file structure. As a result, learning to navigate folders is a transferable skill regardless of the storage system being used.


## Introducing the File Explorer

Most people interact with files through a graphical interface known as a **file explorer** or **file manager**.

Examples include:

| Operating System | File Manager |
|-----------------|-------------|
| Windows | File Explorer |
| macOS | Finder |
| Linux | Files / Nautilus / Dolphin (varies by distribution) |

In this lesson we will demonstrate using **Windows File Explorer**, but the same concepts apply to other operating systems.

::::::::::::::::::: discussion
## Opening File Explorer

The instructor should demonstrate how to open File Explorer in Windows.

:::::::::::::: tab

Depending on the operating system, you can use any of these options to open a file explorer: 

### Windows

- Click the Folder icon on the taskbar.
- Use the keyboard shortcut ```Windows Key + E```
- Open the Start Menu and search for ```File Explorer```

### MacOS

- Click the Finder icon (a blue and white smiling face) on the dock.

::::::::::::::::
::::::::::::::::


::::::::::::: callout
Further instructions for various file navigation tools:

:::::::::::: tab


### Windows 11

- [File Explorer](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)

### MacOS

- [Finder](https://support.apple.com/en-gb/guide/mac-help/mchlp2605/mac)

Select your particular MacOS version at the top of the page under "Mac User Guide".

### Linux

- [GNOME Files ("Nautilus")](https://apps.gnome.org/en-GB/Nautilus/) (default for Ubuntu and Debian)
- [Dolphin](https://userbase.kde.org/Dolphin/File_Management#Discover_Dolphin)
- [Thunar](https://docs.xfce.org/xfce/thunar/the-file-manager-window)


::::::::::::
:::::::::::::


## Anatomy of File Explorer
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
### Navigation Pane
Usually found on the left-hand side.
This shows:

- Desktop
- Documents
- Downloads
- Pictures
- Shared drives
- Other folders

You can use it to jump quickly between locations.

### File List

The central area of the window.
This displays the contents of the currently selected folder.

### Address Bar

Located near the top.
Shows your current location within the file system.
For example:```Downloads > legacy_dataset > RAW_DATA_!!!```
This helps you understand where you are and allows you to move back to previous folders.

### Search Box
Many file managers provide a search box.
Search can be useful, but it should not be your primary strategy for finding files.
A well-organised folder structure makes data easier to locate without relying on search.


## Looking Ahead

In the next episode we will examine the inherited dataset and begin improving its folder structure.
Before we can organise the files, however, we first need to locate them.




::::::::::::: discussion

### Navigating the file explorer

You should make sure that you know where to find:

- Navigation pane
- File listing area
- Address bar
- Search box
- Moving between folders
- Expanding and collapsing folders

on your particular computer, whether it is Windows, MacOS or Linux. 

::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor
Do not assume learners regularly use desktop file systems.

Some participants may primarily use mobile devices and may have little experience navigating folders directly.

Spend a few minutes explicitly demonstrating how files and folders are organised.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Resources

The University library has a number of training courses available for data management.

This is linked to at [Research Data Management Training](https://www.ncl.ac.uk/library/academics-and-researchers/training-and-development/research-data-management-training/)

On this website there are subsections on:

- [Data Management Planning](https://www.ncl.ac.uk/library/academics-and-researchers/training-and-development/research-data-management-training/data-management-planning/)
- [Online Training via Mantra](https://mantra.ed.ac.uk)
- [Data Analysis](https://services.ncl.ac.uk/itservice/research/dataanalysis/)

The general Research Data Management Policy and Code of Good Practice can be found: [here](https://www.ncl.ac.uk/mediav8/our-research/research-governance-policies/ResearchDataManagementPolicyandCoGP.pdf)

::::::::::::: challenge

## Finding the Dataset

Download the lesson dataset.

Using File Explorer:

1. Open the Downloads folder.
2. Locate the downloaded dataset.
3. Open the dataset folder.
4. Explore the contents without modifying anything.
5. Identify at least three things that seem confusing or poorly organised.

:::::::::::::::::


::::::::::::: discussion

Was it immediately obvious where the important data was?

What information would have helped you understand the project more quickly?
:::::::::::::::

::::::::::::::::::::::::::::::::::::: keypoints 

- Data management is an essential part of research practice.
- Many common research frustrations arise from poor organisation and documentation.
- Computers organise information using files and folders within a file system.
- File explorers provide a graphical way to navigate stored data.
- Understanding how files are organised is a foundation for good data management.
- A well-organised project should be understandable to collaborators and to your future self.

::::::::::::::::::::::::::::::::::::::::::::::::
