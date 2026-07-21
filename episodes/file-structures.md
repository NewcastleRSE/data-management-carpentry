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

## File Structures

In the previous episode we located the dataset that was handed over by our departed collaborator. Unfortunately, finding the data is only the first challenge.

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

For most people, the answer is "probably not". Even if details are stored in lab notes, these can easily be misplaced. 

Before we worry about individual files, we need to make sure the overall project structure makes sense.

---

## Why Folder Structures Matter

Most research projects start small with only a few files:

```text
project/
├── data.csv
├── notes.docx
└── report.docx
```

At this stage organisation may seem unnecessary. However, projects rarely stay this simple. More data is added or revised, code is written, plots are generated, and papers/reports/theses are written... and revised.

::::::::::::::::::::::: callout
As projects grow we often accumulate:

- Raw data
- Processed data
- Analysis outputs
- Figures
- Documentation
- Draft manuscripts
- Collaborator comments
- Software scripts
- Temporary files
- Meeting minutes
- Downloaded software
- Software or equipment manuals
- Various notes
- Talks and presentations
:::::::::::::::::::::::

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



:::::::::::::::::::::::::::::::::::::::::::::::::::: callout

The best practice is to plan for expansion rather than reorganising files later, which can lead to incorrect file paths and references in files such as software scripts or lab notes. 

Establish a possible file structure early in the project, while being flexible if new folders or files need to be added or moved. 

Some of this organisation depends on personal preference. For example,

- Do you want to store a seminar or conference presentation with the project, or with other talks elsewhere? 
- Should a paper, along with generated figures, be kept together with the rest of the project? 

If these files are stored elsewhere, can you to find the origin of figures and other results when you write a paper in six months time? If you move a folder, will your file references still work?
::::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::::::::::::::: challenge
## What's Wrong With This Structure?

 Working in groups of 2–3:

 Spend 5 minutes exploring the inherited dataset.

 Identify as many problems as you can.

 Consider:

 - Folder names
 - Folder organisation
 - Folder depth
 - Duplication
 - Clarity
 - Consistency

 Write down your observations.

After 5 minutes, bring the class back together and discuss.

:::::::::::::::::::::::::::::::::::::::::::::::::::: solution

Common observations often include:

- Default names such as `New Folder`
- Unclear names such as `miscellaneous`
- Use of special characters (`RAW_DATA_!!!`)
- Hidden data locations
- Mixed file types within the same folder
- Folders whose purpose is unclear
- Temporary files mixed with project files

:::::::::::::::::::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::::::::::::::::::: 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

 Encourage learners to identify problems rather than immediately propose solutions.

 The goal here is to help learners recognise why poor organisation causes difficulties before introducing best practices.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

---

## Principles of Good Folder Structures

There is no single correct folder structure because different projects have different requirements.

However, most successful structures share common characteristics.

- Meaningful
- Consistent
- Shallow
- Categorical
- Able to archive old files

:::::::::::::::::::::::::::::: challenge

After looking at the Poor examples in each subsection below, try and come up with some good examples before clicking the Good tab.

:::::::::::::::::::::::::::::::

### Meaningful 

Folder names should communicate purpose.  For example, 

:::::::::::::::::::::::::::::::::::::::: tab
### Poor

```text
stuff
miscellaneous
new_folder
files
things
```

### Good

```text
raw_data
processed_data
analysis
documentation
figures
```
:::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::: callout

If somebody joined the project tomorrow, would they understand what belongs in this folder?

:::::::::::::::::::


### Consistent

Consistency is more important than perfection. Choose a particular style and use it throughout the project. This approach makes the structure easier to understand because all folders follow the same convention. For example,

:::::::::::::::::::::::::::::::::::::::: tab
### Poor

```text
RawData
processed-data
Analysis Files
documents_and_notes
```

### Good

```text
raw_data
processed_data
analysis
documentation
```
::::::::::::::::::::::::::::::::::::::::


---

### Shallow

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

Avoid using the folder hierarchy to encode too much information. For example

```text
Project/
└── Data/
    └── Raw/
        └── 2025/
            └── 05/
                └── 06/
                    └── 01/
                        └── Newcastle/
                            └── A_roads/
                                └── UserID12345/
                                └── UserID53546/
                            └── Minor_roads/ 
                                └── UserID35790/
                                └── UserID53546/                       
                        └── Gateshead/                    
                    └── 02/
                        └── Sunderland/ 
                    └── 03/
                        └── Results/                    
```

At best, this approach results in a lot of additional clicks in a file explorer or typing in a terminal/scripts. It can also make analyses unwieldy if you need to collect data from many different subfolders (e.g., if you want to analyse all of Newcastle's data from the example above). 

At worst, file metadata, such as city and datetime in this example, can be irrevocably lost if files are moved from their original location. As such, metadata should ideally be stored in the files themselves or in a reference table with the filenames, rather than in the folder structure.


### Categorical

A common source of confusion is mixing different types of data and files together so that plots, data, reports, analyses, and scripts are all stored in the same folder. Instead, group related materials in the same folder. 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: tab

### Poor
```text
project/
├── raw_data.csv
├── final_figure.png
├── manuscript.docx
├── script.py
└── notes.txt
```

### Good
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

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This structure makes it easier to know where new files belong and find existing files, even if you're new to the project.

:::::::::::::: caution

Know where any private/secure data is to minimise the chance of GDPR violations. 

::::::::::::::

---

### Archive Rather Than Hoard

Many researchers hesitate to delete anything. As a result, they accumulate folders full of obsolete material. Instead, consider creating an archive folder:

```text
archive/
```

This approach allows old material to be retained without cluttering the active project structure.

We will discuss data retention in a later episode.

---

## Moving Files and Folders

Now that we know what good structures look like, we need the practical skills to improve existing structures.

The first operation is moving content.

### How to Move a Folder

:::::::::::::::: tab


### Click and Drag

**All operating systems**

In File Explorer/Finder:

1. Open the dataset folder.
2. Locate the folder:

```text
raw_images_TEMP
```

3. Click and hold the folder.
4. Drag it to a more appropriate parent folder.
5. Release the mouse button.

### Cut and Paste

**Windows**

1. Right-click the folder.
2. Select **Cut**.
3. Navigate to the destination.
4. Right-click.
5. Select **Paste**.

**macOS**

1. Right-click the folder.
2. Select **Copy**.
3. Navigate to the destination.
4. Right-click and press **option**
5. Select **Move item here**.

**Linux**

Depends on the operating system, but most use the same approach as Windows.

### Keyboard shortcuts

**Windows/Linux**

1. Left-click the folder.
2. Press **ctrl+x**
3. Navigate to the destination.
4. Press **ctrl+v**

**macOs**

1. Left-click the folder.
2. Press **cmd+x**
3. Navigate to the destination.
4. Press **cmd+v**

::::::::::::::::::::::::::::::::


:::::::::::::::::::::::: instructor

 Learners often find drag-and-drop easier initially.

 However, introducing Cut and Paste provides a useful alternative when folders are not visible on screen simultaneously.
:::::::::::::::::::::::: 


---

## Renaming Folders

Renaming is one of the simplest improvements we can make to the file organisation. However, be aware that renaming can have unintended consequences if existing files depend on those names; for example, you may need to update folder references in the project's documentation or code.

::::::::::: challenge
Choose a better name for the folder in the Poor example, then see one potential better name in the Good tab.

:::::::::::::: tab

### Poor
```text
RAW_DATA_!!!
```
The name communicates intent, but the punctuation is unnecessary and has ambiguous meaning.

### Good
A clearer alternative is

```text
raw_data
```
::::::::::::::::::
:::::::::::


### How to Rename a Folder

:::::::::::::: tab

### Right-click

**All operating systems**

1. Right-click the folder.
2. Select **Rename**.
3. Enter the new name.
4. Press Enter.

### Via folder selection

**Windows**

1. Select the folder by left-clicking on it.
2. Press **F2**.
3. Enter the new name.

**macOS**

1. Select the folder by left-clicking on it.
2. Click on the folder name
3. Enter the new name.

::::::::::::::::


::::::::::::::::: caution

Be careful when renaming folders that are used by software or analysis scripts. Changing a folder name may break links elsewhere in a project. 

Additionally, project documentation may become out-of-date and confusing if it references the original folder structure.

:::::::::::::::::::

---

## Deleting Unnecessary Folders

Sometimes the simplest improvement is removing unused material.

Consider:

```text
New Folder (2)
```

If this folder is empty or no longer required, it may be reasonable to remove it.

### How to Delete a Folder

:::::::::::::::::: tab

### Drag to Recycle Bin

**All operating systems**

1. Select the folder.
2. Drag into recycle bin (on desktop for **Windows**, bottom right of screen for **MacOS**)

### Right-click

**Windows**

1. Right-click the folder.
2. Choose **Delete**.
3. Confirm deletion if prompted.

**macOS**

1. Right-click the folder.
2. Choose **Move to Bin** or **Move to trash**.
3. Confirm deletion if prompted.

### Keyboard shortcuts
 
**Windows**
1. Select the folder.
2. Press ```Delete```.

**macOS**

1. Select the folder.
2. Press ```Command (⌘) + Delete```.


::::::::::::::::::

Data deleted using the above methods are not fully removed from the system; they are first moved to the recycle bin. You can permanently delete the file by emptying the bin. Alternatively, files in the recycle bin can be restored and "put back" to their original location. On some systems, the bin permanently deletes files after they have been in the bin a certain amount of time (e.g., 30 days).

::::::::::: caution

Check your data policies on data deletion, particularly if handling private data and your files are not encrypted. We will discuss data security in a later lesson. 

Deleting a file on your computer will not always remove the file from automated backups (e.g., files stored in Newcastle University's Microsoft OneDrive); this behaviour will depend on your syncing settings. Confirm that these settings support the backup behaviour you need for your project.

:::::::::::

:::::::::::::::: instructor

 Emphasise caution.

 Deletion should only occur when learners are confident a folder is unnecessary.
 For real research projects, moving to ``archive/`` is often safer than immediate deletion.


::::::::::::::::::


## Designing a Better Structure

At this stage we know:

- What good folder names look like
- How to move folders
- How to rename folders
- How to remove unnecessary folders

The next step is deciding what folder structure you need for your project.

::::::::::::::::: challenge

### Consider possible useful folders and how you would arrange them. 

What folder structures would be good for your projects? How would you divide up files? Try writing out three possible folder hierarchies for a project and discuss the pros/cons of the different approaches with your neighbours.

::::::::::::::::: solution

There is no one correct answer. It will vary depending on your project or personal preferences. One possible structure might be:

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

Other possible folders would be:

- `code`
- `figures` folder inside the analysis folder or outputs folder
- `temp` for temporary files you know you do not wish to keep
etc.

::::::::::::::::::
::::::::::::::::::

The important point is that each folder has a clear purpose.

---

::::::::::::::::::::: discussion

### What Else Would You Change?

 Looking at the inherited dataset:

 - Which folders would you rename?
 - Which folders would you move?
 - Which folders would you remove?
 - Are there any new folders you would create?

 Compare ideas with a neighbour.

::::::::::::::::::::::::::::::::::::::::::  

---

:::::::::::::::::::::::::::::::::::::::::: challenge

### Repair the Project Structure


 Working individually or in pairs:

 1. Rename unclear folders.
 2. Move folders into more logical locations.
 3. Remove any unnecessary empty folders.
 4. Create a structure that clearly separates:
     - Data
     - Documentation
     - Analysis
     - Outputs

 You do not need to create a perfect structure.

 Focus on making the project easier to understand.

::::::::::::::::::::::::::::::::::::::::: solution

 There is no single correct solution.

 A reasonable result might:

 - Rename `RAW_DATA_!!!` to `raw_data`
 - Replace `miscellaneous` with more specific folders
 - Remove unnecessary empty folders
 - Create dedicated locations for documentation and analysis
 - Reduce unnecessary nesting

:::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::

---

## Looking Ahead

We have improved the folder structure, but many files still have confusing names.

In the next episode we will focus on file naming conventions and explore how good file names make datasets easier to understand and process.

::::::::::::::::::::::::::::::::::::: keypoints 

- Folder structures should help people find and understand data.
- Use meaningful, consistent folder names.
- Separate different types of project content into dedicated folders.
- Avoid excessive nesting.
- File Explorer allows folders to be moved, renamed, and deleted without using the command line.
- Consistency is usually more important than any specific organisational scheme.
- A good folder structure should be understandable by collaborators and by your future self.

::::::::::::::::::::::::::::::::::::::::::::::::