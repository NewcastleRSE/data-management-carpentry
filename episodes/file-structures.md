---
title: "Choosing the Right File Structures"
teaching: 25
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions 

## Questions

- Why does folder organisation matter?
- What makes a good folder structure?
- How can I identify problems in an existing file structure?
- How can I move, rename, and delete folders using a file browser?
- How can I organise a project so that it is easier to understand and maintain?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

## Objectives

By the end of this episode, learners will be able to:

- Navigate the file browser using a mouse.
- Identify issues with folder names in a poorly organised project.
- Rename folders using a graphical file browser.
- Identify issues with folder organisation.
- Move folders using a graphical file browser.
- Delete unnecessary folders using a graphical file browser.
- Design a folder structure that supports collaboration and reproducibility.

::::::::::::::::::::::::::::::::::::::::::::::::

# File Structures

In the previous episode we located the dataset that was handed over by our departed collaborator.

Unfortunately, finding the data is only the first challenge.

The project structure itself is difficult to understand:

```text
legacy_dataset/
├── New Folder/
│   ├── Untitled 1.csv
│   └── New Folder (2)/
│       └── backup_copy.txt
│
├── RAW_DATA_!!!
│   ├── Data!@#$.csv
│   ├── 03_04_26_results.csv
│   └── raw_images_TEMP/
│
├── miscellaneous/
│   ├── cat_pic.jpg
│   ├── important_note.txt
│   └── Untitled.csv
│
└── project_data_2025/
    ├── data_final_v3_LAST_ONE.xlsx
    ├── script.py
    └── analysis_12-05-24.txt
```

Imagine joining this project six months from now.

Could you quickly answer:

- Where is the raw data?
- Which files should be analysed?
- Which files are temporary?
- Which files should be preserved?
- Which files can be deleted?

For most people, the answer is "probably not".

Before we worry about individual files, we need to make sure the overall project structure makes sense.

---

# Why Folder Structures Matter

Most research projects start small.

Initially a project might contain only a few files:

```text
project/
├── data.csv
├── notes.docx
└── report.docx
```

At this stage organisation seems unnecessary.

However, projects rarely stay this simple.

As projects grow we often accumulate:

- Raw data
- Processed data
- Analysis outputs
- Figures
- Documentation
- Draft manuscripts
- Software scripts
- Temporary files

A project that starts with three files may eventually contain hundreds or thousands.

Without a clear structure, researchers often experience:

- Time wasted searching for files
- Duplicate work
- Confusion over what files contain
- Difficulty onboarding collaborators
- Difficulty reproducing previous work

Good folder structures make projects easier to:

- Navigate
- Understand
- Collaborate on
- Maintain over time

A useful rule of thumb is:

> A collaborator should be able to understand where files belong without asking you.

---

# Discussion: What's Wrong With This Structure?

> ## Discussion
>
> Working in groups of 2–3:
>
> Spend 5 minutes exploring the inherited dataset.
>
> Identify as many problems as you can.
>
> Consider:
>
> - Folder names
> - Folder organisation
> - Folder depth
> - Duplication
> - Clarity
> - Consistency
>
> Write down your observations.

After 5 minutes, bring the class back together and discuss.

Common observations often include:

- Generic names such as `New Folder`
- Unclear names such as `miscellaneous`
- Use of special characters (`RAW_DATA_!!!`)
- Hidden data locations
- Mixed file types within the same folder
- Folders whose purpose is unclear
- Temporary files mixed with project files


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor
> ## Instructor Note
>
> Encourage learners to identify problems rather than immediately propose solutions.
>
> The goal here is to help learners recognise why poor organisation causes difficulties before introducing best practices.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

---

# Principles of Good Folder Structures

There is no single correct folder structure.

Different projects have different requirements.

However, most successful structures share common characteristics.

## Use Meaningful Names

Folder names should communicate purpose.

Good examples:

```text
raw_data
processed_data
analysis
documentation
figures
```

Poor examples:

```text
stuff
miscellaneous
new_folder
files
things
```

Ask yourself:

> If somebody joined the project tomorrow, would they understand what belongs in this folder?

---

## Be Consistent

Consistency is more important than perfection.

Choose a style and use it throughout the project.

For example:

```text
raw_data
processed_data
analysis
documentation
```

is easier to understand than:

```text
RawData
processed-data
Analysis Files
documents_and_notes
```

because all folders follow the same convention.

---

## Keep Structures Relatively Shallow

Deeply nested structures can become difficult to navigate.

Avoid situations like:

```text
Project/
└── Data/
    └── NewData/
        └── New Folder/
            └── Updated/
                └── Updated Again/
                    └── Results/
```

Having to click through many layers increases the chance of losing track of files.

As a general guideline:

- 3–4 levels deep is often sufficient
- Create more folders horizontally before creating more levels vertically

---

## Separate Different Types of Content

A common source of confusion is mixing everything together.

For example:

```text
project/
├── raw_data.csv
├── final_figure.png
├── manuscript.docx
├── script.py
└── notes.txt
```

Instead, group related materials:

```text
project/
├── data/
│   ├── raw/
│   └── processed/
│
├── analysis/
│
├── figures/
│
└── documentation/
```

This makes it easier to know where new files belong.

---

## Archive Rather Than Hoard

Many researchers hesitate to delete anything.

As a result they accumulate folders full of obsolete material.

Instead, consider creating an archive folder:

```text
archive/
```

This allows old material to be retained without cluttering the active project structure.

We will discuss retention and archiving in a later episode.

---

# Moving Files and Folders

Now that we know what good structures look like, we need the practical skills required to improve them.

The first operation is moving content.

## Demonstration: Moving a Folder

In File Explorer:

1. Open the dataset folder.
2. Locate the folder:

```text
raw_images_TEMP
```

3. Click and hold the folder.
4. Drag it to a more appropriate parent folder.
5. Release the mouse button.

Alternatively:

1. Right-click the folder.
2. Select **Cut**.
3. Navigate to the destination.
4. Right-click.
5. Select **Paste**.

The instructor should demonstrate both methods.

> ## Instructor Note
>
> Learners often find drag-and-drop easier initially.
>
> However, introducing Cut and Paste provides a useful alternative when folders are not visible on screen simultaneously.

---

# Renaming Files and Folders

Naming is one of the simplest improvements we can make.

## Demonstration: Renaming a Folder

Consider:

```text
RAW_DATA_!!!
```

The name communicates intent, but the punctuation is unnecessary.

A clearer alternative might be:

```text
raw_data
```

To rename a folder:

1. Right-click the folder.
2. Select **Rename**.
3. Enter the new name.
4. Press Enter.

Alternatively:

1. Select the folder.
2. Press **F2**.
3. Enter the new name.

Demonstrate both methods.

> ## Callout
>
> Be careful when renaming folders that are used by software or analysis scripts.
>
> Changing a folder name may break references elsewhere in a project.

---

# Deleting Unnecessary Folders

Sometimes the simplest improvement is removing unused material.

Consider:

```text
New Folder (2)
```

If this folder is empty or no longer required, it may be reasonable to remove it.

## Demonstration: Deleting a Folder

1. Select the folder.
2. Right-click.
3. Choose **Delete**.
4. Confirm deletion if prompted.

Alternatively:

1. Select the folder.
2. Press the Delete key.

Explain that deleted content is often moved to the Recycle Bin first.

> ## Instructor Note
>
> Emphasise caution.
>
> Deletion should only occur when learners are confident a folder is unnecessary.
>
> For real research projects, archiving is often safer than immediate deletion.

---

# Designing a Better Structure

At this stage we know:

- What good folder names look like
- How to move folders
- How to rename folders
- How to remove unnecessary folders

The next step is deciding how the project should look.

One possible structure might be:

```text
project/
├── data/
│   ├── raw/
│   └── processed/
│
├── analysis/
│
├── documentation/
│
├── outputs/
│
└── archive/
```

This is not the only correct answer.

The important point is that each folder has a clear purpose.

---

# Discussion: What Else Would You Change?

> ## Discussion
>
> Looking at the inherited dataset:
>
> - Which folders would you rename?
> - Which folders would you move?
> - Which folders would you remove?
> - Are there any new folders you would create?
>
> Compare ideas with a neighbour.

---

# Exercise: Repair the Project Structure

> ## Challenge
>
> Working individually or in pairs:
>
> 1. Rename unclear folders.
> 2. Move folders into more logical locations.
> 3. Remove any unnecessary empty folders.
> 4. Create a structure that clearly separates:
>     - Data
>     - Documentation
>     - Analysis
>     - Outputs
>
> You do not need to create a perfect structure.
>
> Focus on making the project easier to understand.

> ## Solution
>
> There is no single correct solution.
>
> A reasonable result might:
>
> - Rename `RAW_DATA_!!!` to `raw_data`
> - Replace `miscellaneous` with more specific folders
> - Remove unnecessary empty folders
> - Create dedicated locations for documentation and analysis
> - Reduce unnecessary nesting

---

# Looking Ahead

We have improved the folder structure, but many files still have confusing names.

In the next episode we will focus on file naming conventions and explore how good file names make datasets easier to understand and process.

::::::::::::::::::::::::::::::::::::: keypoints 

## Key Points

- Folder structures should help people find and understand data.
- Use meaningful, consistent folder names.
- Separate different types of project content into dedicated folders.
- Avoid excessive nesting.
- File Explorer allows folders to be moved, renamed, and deleted without using the command line.
- Consistency is usually more important than any specific organisational scheme.
- A good folder structure should be understandable by collaborators and by your future self.

::::::::::::::::::::::::::::::::::::::::::::::::