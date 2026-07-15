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

For most people, the answer is "probably not". Even if details are stored in lab notes these can be easily misplaced. 

Before we worry about individual files, we need to make sure the overall project structure makes sense.

---

## Why Folder Structures Matter

Most research projects start small, containing only a few files:

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
- Software scripts
- Temporary files
- Minutes from meetings
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

Keep in mind that it is good to plan for expansion at the beginning of a project rather than have to reorganise things later, which can break things, such as software scripts or lab notes. 

It is good to think about a possible file structure early in the project, while being flexible if new folders or files needed to be added or moved. 

For example,

- Do you want to keep a seminar or conference presentation with the project, or with other talks elsewhere? 
- Should a paper, along with generated figures, be kept together with the rest of the project? 

If not, will your file system enable you to find the origin of figures etc. used in a seminar in the future or when you write a paper in six months time? If you move a folder in future will this break things?
::::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::::::::::::::: challenge
## Discussion: What's Wrong With This Structure?
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

:::::::::::::::::::::::::::::::::::::::::::::::::::: solution
Common observations often include:

- Generic names such as `New Folder`
- Unclear names such as `miscellaneous`
- Use of special characters (`RAW_DATA_!!!`)
- Hidden data locations
- Mixed file types within the same folder
- Folders whose purpose is unclear
- Temporary files mixed with project files
:::::::::::::::::::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::::::::::::::::::: 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor
> ## Instructor Note
>
> Encourage learners to identify problems rather than immediately propose solutions.
>
> The goal here is to help learners recognise why poor organisation causes difficulties before introducing best practices.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

---

## Principles of Good Folder Structures

There is no single correct folder structure.

Different projects have different requirements.

However, most successful structures share common characteristics.

- Meaningful
- Consistent
- Shallow
- Catagorical
- Able to archive old files

:::::::::::::::::::::::::::::: challenge

After looking at the Poor examples in each subsection, below, try and come up with some good examples before clicking the Goood tab. 

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

> If somebody joined the project tomorrow, would they understand what belongs in this folder?

:::::::::::::::::::


### Consistent

Consistency is more important than perfection. Choose a particular style and use it throughout the project. This makes things easier to understand because all folders follow the same convention. For example,

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

Try not to use the folder hierarchy to encode too much information. For example

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

At best this results in a lot of additional clicks in File Explorer (Win11) or Finder (MacOS), or typing in the terminal/analysis code. 


### Catagorical

A common source of confusion is mixing everything together. So plots, data, reports, analysis, code all end up in the same folder. Instead, group related materials in the same folder. 

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

This makes it easier to know where new files belong.

---

### Archive Rather Than Hoard

Many researchers hesitate to delete anything. As a result they accumulate folders full of obsolete material. Instead, consider creating an archive folder:

```text
archive/
```

This allows old material to be retained without cluttering the active project structure.

We will discuss data retention and archiving in a later episode.

---

## Moving Files and Folders

Now that we know what good structures look like, we need the practical skills required to improve them.

The first operation is moving content.

::::::::::::::::::::::::::::: challenge

### Renaming a folder

:::::::::::::::: tab


### All

In File Explorer/Finder:

1. Open the dataset folder.
2. Locate the folder:

```text
raw_images_TEMP
```

3. Click and hold the folder.
4. Drag it to a more appropriate parent folder.
5. Release the mouse button.

### Windows II

1. Right-click the folder.
2. Select **Cut**.
3. Navigate to the destination.
4. Right-click.
5. Select **Paste**.

### MacOS II

1. Right-click the folder.
2. Select **Copy**.
3. Navigate to the destination.
4. Right-click and press **option**
5. Select **Move item here**.

### Windows/Linux III

1. Left-click the folder.
2. Press **ctrl+x**
3. Navigate to the destination.
4. Press **ctrl+v**

### MacOs III

1. Left-click the folder.
2. Press **cmd+x**
3. Navigate to the destination.
4. Press **cmd+v**

::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::


:::::::::::::::::::::::: instructor

 Learners often find drag-and-drop easier initially.

 However, introducing Cut and Paste provides a useful alternative when folders are not visible on screen simultaneously.
:::::::::::::::::::::::: 


---

## Renaming Files and Folders

Renaming is one of the simplest improvements we can make to the files. This allows us to select new names for the folders. This can have consequences is any code relies on the folder names already in place, however. 

::::::::::: challenge
In the below example, chose a better name for the folder in the Poor example to a better folder name, and check your answer using the Good tab. It doesn't need to be identical, but should show similar features. 
:::::::::::

Consider:

:::::::::::::: tab

### Poor
```text
RAW_DATA_!!!
```
The name communicates intent, but the punctuation is unnecessary.

### Good
A clearer alternative might be:

```text
raw_data
```
::::::::::::::::::



:::::::::::::::::::::::::: discussion
### How do I rename a folder:

:::::::::::::: tab

### Windows/Mac/Linux
1. Right-click the folder.
2. Select **Rename**.
3. Enter the new name.
4. Press Enter.

### Windows II

1. Select the folder.
2. Press **F2**.
3. Enter the new name.

### MacOS II

1. Select the folder.
2. Click on the file name
3. Enter the new name.

::::::::::::::::
:::::::::::::





::::::::::::::::: caution

Be careful when renaming folders that are used by software or analysis scripts.

Changing a folder name may break references elsewhere in a project.

:::::::::::::::::::

---

## Deleting Unnecessary Folders

Sometimes the simplest improvement is removing unused material.

Consider:

```text
New Folder (2)
```

If this folder is empty or no longer required, it may be reasonable to remove it.

:::::::::: discussion 

### How do I delete a Folder


:::::::::::::::::: tab

### Windows

1. Select the folder.
2. Right-click.
3. Choose **Delete**.
4. Confirm deletion if prompted.

### Windows II

1. Select the folder.
2. Press the Delete key.

### MacOS

1. Select the folder.
2. Choose **Move to bin** or **Move to trash**

### Windows/MacOS

1. Select the folder.
2. Drag into recycle bin (on desktop for Windows, bottom right of screen for MacOS)


::::::::::::::::::
:::::::::::

Data deleted using the above methods are not fully removed from the system. They are moved to the recycle bin. To permanently  remove the file you have to empty the bin. Alternatively, files in the recycle bin can be restored and put back where they were. On some systems there is a certain about of time a document will stay in the recycle bin before it is deleted. 

::::::::::: caution

Check your data policies on data deletion, particularly if handling private data and your files are not encrypted. We will discuss data security in a later lesson. 

:::::::::::

:::::::::::::::: instructor

 Emphasise caution.

 Deletion should only occur when learners are confident a folder is unnecessary.
 For real research projects, archiving is often safer than immediate deletion.


::::::::::::::::::


## Designing a Better Structure

At this stage we know:

- What good folder names look like
- How to move folders
- How to rename folders
- How to remove unnecessary folders

The next step is deciding how the project should look.

::::::::::::::::: challenge

### Consider possible useful folders and how you would arrange them. 

What folder structures would be good for your projects? How would you divide up files? Think about a folder hierarchy for several minutes and discuss. 

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