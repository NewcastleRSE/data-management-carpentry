---
title: "Naming Files Well"
teaching: 25
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions 

## Questions

- What makes a good filename?
- How much information should be included in a filename?
- Why are naming conventions important?
- How can filenames support batch processing and automation?
- How can I rename one file or many files using a graphical file browser?

::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

## Objectives

By the end of this episode, learners will be able to:

- Identify problems with poorly named files.
- Explain the characteristics of a good filename.
- Choose an appropriate file naming convention.
- Use filenames to support sorting and batch processing.
- Rename an individual file using a graphical file browser.
- Rename multiple files using bulk rename tools.
- Apply a consistent naming convention to an existing dataset.

:::::::::::::::::::::::::::::::::::::

## From Folder Names to File Names

In the previous episode, we improved the folder structure of the inherited project. However, fixing the folders has not solved all of our problems. 

Consider the files we have been given:

```text
Data!@#$.csv
Untitled.csv
copy of DSCO1023.png
03_04_26_results.csv
results-new.csv
data_final.xlsx
data_final_v2.xlsx
data_final_v3_LAST_ONE.xlsx
```

At best, these names are unhelpful. At worst, they actively prevent us from understanding the project or keeping track of progress, particularly when looking back on the work done months later.  

::::::::::::::::::::::::::::::::::::::: callout
Imagine receiving an email that says:

> "Can you update the analysis using the latest data?"

Which file would you use?

```text
data_final.xlsx
data_final_v2.xlsx
data_final_v3_LAST_ONE.xlsx
```
The answer is not obvious. 

One can imagine that the latest results are in `data_final_v3_LAST_ONE.xlsx`, but maybe there was an error in this file and it was never deleted, meaning that `data_final_v2.xlsx` contains the latest data. How would you know?

You do not want to resort to sorting the files by date and hoping that the last *created or modified* file was the last *good* file! 

:::::::::::::::::::::::::::::::

Good filenames should give us insight into what a file contains without needing to open it. Your choice of filenames should make subsequent analysis steps as frictionless as possible. If you find you are fighting your files in order to make progress in your work, there is probably something that can be improved. *You have to be able to find your data in order to use it!*

Your choice of filenames becomes increasingly important as projects grow larger, data is shared between collaborators, or data needs revisiting at a later date. 

::::::::::::::::::::::::::::::: discussion

 Working in pairs, look through the files in the inherited project. What problems can you identify?

 Consider:

 - Can you tell what the file contains?
 - Can you identify the newest version?
 - Are dates presented consistently?
 - Would the names be easy to process automatically?
 - Are there any confusing abbreviations?

Write down as many issues as you can find.

After a few minutes, discuss observations as a group.

:::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::: callout

Common issues with file names include

- Meaningless names (`data.csv`)
- Overly long names (`1Nov16_polymer_test1_heating_123degree_measure14_userabc_id12345.txt`)
- Special characters (`image#1.png`)
- Multiple date formats (`23-Nov2024.csv`, `2024-15-07.txt`)
- Ambiguous version information (`data1bfinalfinal2reallyfinalusethis.txt`)
- Inconsistent separators (`10-12_2019-data_ver1.img.csv`) - although different separators can be used to split different types of information (e.g., `10-12-2019_data_ver1_img.csv` consistently uses `-` to separate the date elements and `_` to separate other text)
- Difficult to parse names due to lack of separators (`test1userabsnovember17.h5`)
- Duplicate information (`24Nov_image01_241117.dat`)

:::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::: instructor

 Encourage learners to focus on whether filenames communicate useful information.

 Avoid discussing "perfect" filenames. The goal is consistency and clarity.

:::::::::::::::::::::::::::::::


## Why Filenames Matter

::::::::::::::::::::::::::::::: callout

A filename serves several purposes simultaneously.

It helps answer

- What is this file?
- When was it created?
- Which sample or dataset does it belong to?
- Which version is this?
- Can it be grouped with related files?

Good filenames support

- Human understanding
- Sharing and collaboration
- Automated processing
- Reproducibility


:::::::::::::::::::::::::::::::

A filename should be easily useable by both a human reader and a computer. Keep in mind that humans and computers are good at different things and that different software and operating systems (Windows, macOS, Linux) have different conventions. Your filenames should be as portable as possible.  

Future-you is one of the most important users of your naming convention, but it should also be easily understandable by colleagues.

## Characteristics of Good Filenames

::::::::::::::::::::::::::::::: callout

There is no universal naming convention. 

:::::::::::::::::::::::::::::::

It is impossible to build an understandable, concise, informative template that accounts for all possible scenarios. Different projects require different information. However, successful file naming schemes usually share several characteristics.

Filenames should be

- Meaningful
- Consistent
- Machine-friendly
- Sortable
- Clear


### Meaningful

A filename should describe the contents of the file, for example:

::: tab
### Poor
```text
data.csv
```
### Good
```text
2026-04-03_water_quality_siteA.csv
```
:::

The 'good' example immediately communicates useful information about the data: it measures the water quality at siteA on the 3rd April 2026. This name can be used by a human to easily find the desired data in a folder containing many files and reference it in code or documentation. For a computer, this filename information can help software load and sort the data without opening the document and reading its content. The 'poor' filename communicates almost nothing.

### Consistent

Choose a convention and use it across all files.

::::::::::::::::::::::::::::::::: tab

### Poor
```text
Apr1.csv
sample_2.csv
Results03April.csv
```

### Good
```text
2026-04-01_sample01.csv
2026-04-02_sample02.csv
2026-04-02_sample03.csv
```

::::::::::::::::::::::::::::::::::::

Even if the files contain the same information, inconsistent naming makes them harder to understand and automatically analyse. If the folder contains many files, how would you be able to find a specific piece of data? For automation, the good filenames each contain the data's date and sample id, allowing a script to easily loop through and find each file.  

### Machine-Friendly

Computers prefer predictable patterns.

::: tab
### Poor
```text
my data.csv
results & notes.csv
```

### Good
```text
my_data.csv
results_and_notes.csv
```
:::

Recommended characters:

- letters
- numbers
- hyphens (`-`)
- underscores (`_`)

Avoid:

```text
- special characters: \ / : * ? " < > |
- spaces
```

These characters can have special meanings on different operating systems. Hyphens can cause issues because different word processors can substitute different characters which look almost the same. Similarly, word processors can autocorrect lower case letters into uppercase characters at the start of lines. 

:::::::::::::::::::::::::::::: caution

Windows file names are case insensitive. Linux and macOS filenames are case sensitive. This difference can cause data loss when copying files from Linux or macOS to Windows file systems.

:::::::::::::::::::::::::::::::


### Sortable

Since files are usually displayed alphanumerically, choose file names that logically order your files. 


::: tab
### Poor
```text
03-04-2026_recording.csv
12-01-2025_recording.csv
25-12-2025_recording.csv
```

### Good
```text
2025-01-12_recording.csv
2025-12-25_recording.csv
2026-04-03_recording.csv
```
:::

Using [ISO date format](https://www.iso.org/iso-8601-date-and-time-format.html) (YYYY-MM-DD) means the files will be grouped from first to last date. This organisation is more useful than sorting by day first, then month within that day, which instead sorts files by the day of the month:

```text
01-02-2025_recording.csv
01-03-2025_recording.csv
01-05-2024_recording.csv
01-05-2023_recording.csv
```
which is *usually*, but not always, less useful. 

When planning your file names, consider how alphabetical sorting will arrange your files. Place the most important metadata for grouping files (such as the date, subject, country, or sample) at the start of the file name.

### Clear

Filenames should be clear for a human and computer to read. 

:::::::::::::::::::::::::::::: tab
### Poor
```text
03042026siteAID1234.csv
```

### Good
```text
03-04-2026_site-A_ID-1234.csv
```

:::::::::::::::::::::::::::::::::::::


This provides breaks for the eye, and for software. 


## What Information Should Go Into a Filename?

Many researchers face a common temptation:


> If information is useful, why not put all of it in the filename?


This can lead to names such as:
```text
2026-06-01_12-43-16_sampling_trip_siteA_temperature_sensor_03_processed_final_v2.csv
```
which becomes difficult to read, particularly in a long list of files with similar names. 

Acronyms can help make the file name smaller but you don't want to have to have a set of definitions taped to your office wall to remember them. 

A useful guideline is:


> Include enough information to identify the file, but not so much that the filename becomes documentation.


The most useful information might include:

- date
- sample identifier
- location
- experiment identifier
- version

For example:

```text
2026-06-01_siteA_sample03_v01.csv
```

Additional details can either be stored elsewhere:

- README files
- metadata files
- data dictionaries
- laboratory notebooks

or as a header or metadata in the file itself.

We will discuss documentation in the next episode.


## Naming Files for Batch Processing

One advantage of consistent filenames is that they can easily be processed together.

::: tab
### Poor
```text
Image One.png
June second image.png
IMG_final.png
```

### Good
```text
June_01_image_01.png
June_01_image_02.png
June_03_image_03.png
```
:::

The files in the good example can be processed together, while files in the poor example are much harder to work with systematically. When files are expected to belong to a sequence, use consistent numbering with leading zeros:

::: tab
### Poor
```text
image_1.png
image_2.png
image_10.png
```

### Good
```text
image_01.png
image_02.png
image_03.png
```
:::

This improves sorting. 

For example, when sorting files we get:

::: tab

### Poor

```text
image_8.png
image_80.png
image_81.png
image_9.png
image_93.png
```

### Good

```text
image_08.png
image_09.png
image_80.png
image_81.png
image_93.png
```

:::


::: callout
Remember to pad with sufficient zeros for the expected total number of files. If you expect less than 100 files you can pad with 1 zero, less than 1000 pad with 2 zeros etc. 
:::
---

## Using Hierarchies Effectively

Remember that your folder hierarchy already provides information.

Suppose we have:

```text
project/
└── case_studies/
    ├── scotland/
    ├── england/
    └── wales/
```

Inside each folder:

```text
2026-06-01_image_01.png
```

is sufficient.

Avoid naming files:

```text
scotland_2026-06-01_image_01.png
```

For example:

::: tab
### Bad 
```text
project/
└── case_studies/
    ├── scotland/
       └── scotland_2026-06-01_image_01.png
       └── scotland_2026-06-01_image_02.png
    ├── england/
       └── england_2026-07-02_image_01.png    
    └── wales/
       └── wales_2026-05-02_image_13.png  
```

### Good
```text
project/
└── case_studies/
    ├── scotland/
       └── 2026-06-01_image_01.png
       └── 2026-06-01_image_02.png
    ├── england/
       └── 2026-07-01_image_01.png    
    └── wales/
       └── 2026-05-02_image_13.png  
```
:::

The location information is already present in the folder structure and so is reduntant in the file name. 

This can illustrate how each project has different filename requirements. If the 'country' layer of the directory structure wasn't present, it would be useful to put the country in the filename. As files move around, or are migrated from folder to folder you need to consider whether file names should change. 

For example, 


If it is decided that the country folders can be removed, then files:

```text
scotland/2026-06-01_image_01.png 
england/2026-07-01_image_01.png 
````

would have the same name. You would need to be rename them to avoid data loss. 


::: callout
Good folder structures and good filenames should work together.
:::

---

## Versioning Files

Versioning files keeps track of revisions over time. This is useful because documents evolve, and you do always not wish to overwrite previous files. This can be because of repeated experiments, fresh downloads of data, wanting non-destructive revisions to documents or an audit trail of changes.

Many researchers create filenames that making tracking revisions difficult. This usually indicates that a versioning strategy is missing. For example:

::: tab

### Bad

```text
final.docx
final_final.docx
final_final_v2.docx
FINAL_ACTUALLY_FINAL.docx
```

### Good
```text
report_v01.docx
report_v02.docx
report_v03.docx
```
or
```text
report_v1.0.0.docx
report_v1.1.0.docx
report_v2.0.0.docx
```
:::

The bad example is difficult to follow, while the good example uses explicit versions. 

Avoid:

- latest
- final
- newest
- final_final

because these labels eventually become inaccurate. As soon as you edit report_final_final.docx it is no longer final (or even final final!), and you probably won't go back to rename it. 

::::::::::::::::::::::: callout

Various software tools do exist to help with versioning. For example:

- git (for text documents or code)
- Microsoft office (version history tool)
- OneDrive

which do not rely on file names. 

::::::::::::::::::::::::::::


## Renaming files

### Renaming a Single File

Now that we understand good naming principles, we need practical ways to apply them.

::: challenge
Suppose we have

```text
Data!@#$.csv
```

A more descriptive name might be

```text
2026-04-03_incidence_data_v01.csv
```

We can rename it via:

:::::::::::::::::::::::::: tab

### Windows
To rename a file in File Explorer:

1. Select the file.
2. Right-click.
3. Choose **Rename**.
4. Enter the new filename.
5. Press Enter.

### Windows Alternative:
To rename a file in File Explorer:

1. Select the file.
2. Press **F2**.
3. Type the new name.
4. Press Enter.

### macOS
To rename a file in Finder:

1. Select the file.
2. Left-click on the filename
3. Enter the new filename.
4. Press Enter.

:::::::::::::::::::::::::: 
:::


::: instructor

Demonstrate both Windows methods.

The keyboard shortcut is often significantly faster once learners become confident.

:::



### Bulk Renaming Files

Renaming one file is easy, but renaming hundreds is not.

Imagine receiving

```text
IMG0001.JPG
IMG0002.JPG
IMG0003.JPG
...
IMG1250.JPG
```

from a collaborator.

Renaming each file individually would be extremely time consuming (and boring!).Fortunately, many operating systems provide ways to rename multiple files simultaneously.

For example:

```text
IMG0001.JPG
IMG0002.JPG
IMG0003.JPG
```

might become:

```text
siteA_image_01.jpg
siteA_image_02.jpg
siteA_image_03.jpg
```

Several graphical tools support this, for example:

::: tab

### Windows

- Microsoft PowerToys PowerRename
- Bulk Rename Utility
- Advanced Renamer

### macOS

- Built-in Finder rename tools

### Ubuntu Linux

- Built-in File Manager tools
- Thunar

:::

The exact interface differs between tools, but the concepts are similar:

- Find text
- Replace text
- Add prefixes
- Add suffixes
- Insert numbering


:::::::::::::::::::: challenge
Using a bulk rename tool:

Replace:

```text
IMG
```

with:

```text
siteA_image_
```
::: solution

::: tab
### Before

```text
IMG_0001.png
IMG_0002.png
IMG_0003.png
IMG_0004.png
IMG_0005.png
```
### After:
```text
siteA_image_0001.png
siteA_image_0002.png
siteA_image_0003.png
siteA_image_0004.png
siteA_image_0005.png
```
:::
:::
::::::::::::::::::::

::::::: challenge

What could go wrong if a bulk rename operation is performed incorrectly?

How could you reduce risk?


::::::: solution

- Test on copies first.
- Rename a small sample initially.
- Keep backups.
- Check the preview before applying changes.
:::
::::::: 



## Exercise: Improve the File Names

::: challenge

Working individually or in pairs:

Review the filenames in the inherited dataset and apply the principles discussed in this lesson.

Consider:

 - Meaningful descriptions
 - Consistent formatting
 - ISO dates where appropriate
 - Explicit version numbers
 - Removal of unnecessary special characters

 Rename the files using File Explorer/Finder.

If a bulk rename tool is available, use it where appropriate.

::: solution

 There is no single correct answer.

 A reasonable outcome might:

::: tab

### Before

 ```text
 Data!@#$.csv
 ```

### After

 ```text
 incidence_data_v01.csv
 ```
:::

or

::: tab

### Before

 ```text
 data_final_v3_LAST_ONE.xlsx
 ```

### After

 ```text
 project_results_v03.xlsx
 ```
:::

These different options are all goodm provided the convention is applied consistently throughout the project. 

:::
:::


## Looking Ahead

We have improved both the folder structure and the filenames.

However, many questions remain unanswered:

- Where did the data come from?
- How was it collected?
- What do variables mean?
- Which files should be used?

This information belongs in documentation.

In the next episode we will explore how README files, metadata, file headers, and provenance information make datasets understandable and reusable.

::::::::::::::::::::::::::::::::::::: keypoints 

### Key Points

- Good filenames help both people and computers understand data.
- Consistency is more important than choosing a particular naming convention.
- Use meaningful names that describe file contents.
- Avoid spaces and special characters where possible.
- Use ISO dates (`YYYY-MM-DD`) when dates are needed.
- Include version numbers rather than labels such as "final" or "latest".
- Folder structures and filenames should work together.
- Bulk renaming tools make large-scale renaming practical.
- A filename should help identify a file without needing to open it.

::::::::::::::::::::::::::::::::::::::::::::::::
