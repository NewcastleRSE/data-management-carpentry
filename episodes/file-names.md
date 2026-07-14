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

::::::::::::::::::::::::::::::::::::::::::::::::

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

::::::::::::::::::::::::::::::::::::::::::::::::

## From Folder Names to File Names
-------------------------


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

At best, these names are unhelpful. At worst, they actively prevent us from understanding the project or keeping track of progress, particularly months later.  


:::cutout
Imagine receiving an email that says:

> "Can you update the analysis using the latest data?"

Which file would you use?

```text
data_final.xlsx
data_final_v2.xlsx
data_final_v3_LAST_ONE.xlsx
```
The answer is not obvious. 

One can imagine that the latest results are in "data_final_v3_LAST_ONE.xlsx", but maybe there was an error in this file and it was never deleted, meaning that "data_final_v2.xlsx" contains the latest data.  You do not want to be in a situation where you have to sort the files by date and hope that the last *created or modified* file was the last *good* file! 
:::

Good filenames should give us insight into what a file contains without needing to open it. Your choice of filenames should make subsequent analysis steps as frictionless as possible. If you find you are fighting your files in order to make progress in your work, there is probably something that can be improved. *You have to be able to find your data in order to use it!*

Your choice of filenames becomes increasingly important as projects grow larger, data is shared between collaborators, or data needs revisiting at a later date. 

---

# Discussion: What's Wrong With These Filenames?

::::::::::::::::::::::::::: discussion
 Working in pairs, look through the files in the inherited project.

 What problems can you identify?

 Consider:

 - Can you tell what the file contains?
 - Can you identify the newest version?
 - Are dates presented consistently?
 - Would the names be easy to process automatically?
 - Are there any confusing abbreviations?

 Write down as many issues as you can find.

After a few minutes, discuss observations as a group.

:::::::::::::::::::::::::::

Common issues with file names which typically arise include:

::: callout
- Meaningless names
- Overly long names
- Special characters
- Multiple date formats
- Ambiguous version information
- Inconsistent separators
- Duplicate information
:::

> ## Instructor Note
>
> Encourage learners to focus on whether filenames communicate useful information.
>
> Avoid discussing "perfect" filenames. The goal is consistency and clarity.

---

# Why Filenames Matter

A filename serves several purposes simultaneously.

It helps answer:

- What is this file?
- When was it created?
- Which sample or dataset does it belong to?
- Which version is this?
- Can it be grouped with related files?

Good filenames support:

- Human understanding
- Sharing and collaboration
- Automated processing
- Reproducibility

A filename should be easily useable by both a human reader and a computer. Humans and computers are good at different things and different tools and operating systems (Windows, MacOS, Linux) have different conventions. Your filenames should be as portable as possible.  

Future-you is one of the most important users of your naming convention, but, should be easily understandable to collegues.

---

# Characteristics of Good Filenames

There is no universal naming convention. There are so many possible scenarios it is impossible to build an understandable, concise, informative template which accounts for them all. Different projects require different information. However, successful file naming schemes usually share several characteristics.

## Meaningful

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

The 'good' example immediately communicates useful information about the data: data about the water quality at siteA on the 3rd April 2026. This can be used by a human, to immediatly find the data in a folder containing, potentially, many files and helps transcription into code or a document. For a computer the filename contains important information which can help software load and sort the data without having to open the document and read its content. The second filename communicates almost nothing.

---

## Consistent

Choose a convention and use it everywhere.

::: tab
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
:::

Even if the files contain the same information, inconsistent naming makes them harder to understand and automate. IF the folder contains many files, how would you be able to find these files among the others? For automation, the good example contains date and order information so each file can be analysed in order without having to load each file individually. 

---

## Machine-Friendly

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

Recommended characters include:

- letters
- numbers
- hyphens (`-`)
- underscores (`_`)

Avoid:

```text
\ / : * ? " < > |
```

These characters can have special meanings on different operating systems. Hyphens can cause issues because different word processors can substitute different characters which look almost the same . Similarly, word processors can autocorrect lower case letters into uppercase characters at the start of lines. 

::: callout
Windows file names are case insensitive. Linux and Mac filenames are case sensitive. This can cause data loss when copying files from Linux or Mac to Windows
:::

---

## Sortable

Files are usually displayed alphabetically.

If dates are written as:

```text
03-04-2026
12-01-2025
25-12-2025
```

they may not sort chronologically.

Instead use:

```text
2025-01-12
2025-12-25
2026-04-03
```

:::::: callout
This is known as the ISO date format:

```text
YYYY-MM-DD
```
::::::

sorts correctly both alphabetically and chronologically.

> ## Callout
>
> This is one of the simplest improvements you can make to a dataset.
>
> Using ISO dates often eliminates many common sorting problems.

---

# What Information Should Go Into a Filename?

Many researchers face a common temptation:

> If information is useful, why not put all of it in the filename?

This can lead to names such as:

```text
2026-06-01_12-43-16_sampling_trip_siteA_temperature_sensor_03_processed_final_v2.csv
```

The filename becomes difficult to read.

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

or as a header in the file itself.

We will discuss documentation in the next episode.

---

# Naming Files for Batch Processing

One advantage of consistent filenames is that they can easily be processed together.

Consider:

```text
01-June_image_01.png
01-June_image_02.png
03-June_image_03.png
```

These can be processed as a collection.

However:

```text
Image One.png
June second image.png
IMG_final.png
```

are much harder to work with systematically.

When files are expected to belong to a sequence, use consistent numbering:

```text
image_01.png
image_02.png
image_03.png
```

rather than:

```text
image_1.png
image_2.png
image_10.png
```
Note there is a leading zero in this example. This improves sorting. For example, when sorting files we get:

```text
image_08.png
image_09.png
image_80.png
image_81.png
image_93.png
```

rather than

```text
image_8.png
image_80.png
image_81.png
image_9.png
image_93.png
```

Remember to pad with sufficient zeros for the expected total number of files. If you expect less than 100 files you can pad with 1 zero, less than 1000 pad with 2 zeros etc. 
---

# Using Hierarchies Effectively

Remember that folders already provide information.

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

because the location information is already present in the folder structure.

Good folder structures and good filenames should work together.

---

# Versioning Files

Many researchers create filenames such as:

```text
final.docx
final_final.docx
final_final_v2.docx
FINAL_ACTUALLY_FINAL.docx
```

This usually indicates that a versioning strategy is missing.

A better approach uses explicit versions:

```text
report_v01.docx
report_v02.docx
report_v03.docx
```

or:

```text
report_v1.0.0.docx
report_v1.1.0.docx
report_v2.0.0.docx
```

Avoid:

- latest
- final
- newest
- final_final

Eventually these labels become inaccurate.

---

# Renaming a Single File

Now that we understand good naming principles, we need practical ways to apply them.

## Demonstration

Suppose we have:

```text
Data!@#$.csv
```

A more descriptive name might be:

```text
2026-04-03_incidence_data_v01.csv
```

:::::::::::::::::::::::::: group-tab

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

### MacOS
To rename a file in Finder:
1. Select the file.
2. Left-click on the filename
3. Enter the new filename.
4. Press Enter.

:::::::::::::::::::::::::: 

Learners should follow along.

> ## Instructor Note
>
> Demonstrate both Windows methods.
>
> The keyboard shortcut is often significantly faster once learners become confident.

---

# The Problem with Large Datasets

Renaming one file is easy.

Renaming hundreds is not.

Imagine receiving:

```text
IMG0001.JPG
IMG0002.JPG
IMG0003.JPG
...
IMG1250.JPG
```

Renaming each file individually would be extremely time consuming.

Fortunately, many tools support bulk renaming.

---

# Bulk Renaming Files

Many operating systems provide ways to rename multiple files simultaneously.

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

Several graphical tools support this:

Windows
- Microsoft PowerToys PowerRename
- Bulk Rename Utility
- Advanced Renamer

MacOS
- Built-in Finder rename tools

Ubuntu
- Built-in File Manager tools
- Thunar

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
:::::::::::::::::::: output

Before:

```text
IMG_0001.png
IMG_0002.png
IMG_0003.png
IMG_0004.png
IMG_0005.png
```
After:
```text
siteA_image_0001.png
siteA_image_0002.png
siteA_image_0003.png
siteA_image_0004.png
siteA_image_0005.png
```
::::::::::::::::::::

::::::: challenge
>
> What could go wrong if a bulk rename operation is performed incorrectly?
>
> How could you reduce risk?

::::::: solution

- Test on copies first.
- Rename a small sample initially.
- Keep backups.
- Check the preview before applying changes.

::::::: 


# Exercise: Improve the File Names

> ## Challenge
>
> Working individually or in pairs:
>
> Review the filenames in the inherited dataset.
>
> Apply the principles discussed in this episode.
>
> Consider:
>
> - Meaningful descriptions
> - Consistent formatting
> - ISO dates where appropriate
> - Explicit version numbers
> - Removal of unnecessary special characters
>
> Rename the files using File Explorer.
>
> If a bulk rename tool is available, use it where appropriate.

> ## Solution
>
> There is no single correct answer.
>
> A reasonable outcome might:
>
> ```text
> Data!@#$.csv
> ```
>
> become:
>
> ```text
> incidence_data_v01.csv
> ```
>
> and:
>
> ```text
> data_final_v3_LAST_ONE.xlsx
> ```
>
> become:
>
> ```text
> project_results_v03.xlsx
> ```
>
> provided the convention is applied consistently throughout the project.

---

# Looking Ahead

We have improved both the folder structure and the filenames.

However, many questions remain unanswered:

- Where did the data come from?
- How was it collected?
- What do variables mean?
- Which files should be used?

This information belongs in documentation.

In the next episode we will explore how README files, metadata, and provenance information make datasets understandable and reusable.

::::::::::::::::::::::::::::::::::::: keypoints 

## Key Points

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

<!-- ### How to name your files?

**There is no perfect solution!**

It depends on: 
1. if you have a simple dataset or series of files which should be read at once by external model/software

> Note: for example, some formats MUST have a few auxiliary metadata files to be read (for example, simply `JSON` to fetch metadata or `.SHP` in geospatial analysis)

In this case, the dataset should contain a few files with the same names but different extensions.

2. Whether files should be processed in batches by another step in a processing pipeline.
   
Your filename should normally have a permanent and temporary parts:

`<permanent>_<temporary>.png`: `image_01.png`

In reality, the temporary part might include over one or more temporary subparts:

`<temporary>_<permanent>_<temporary>`: `01-June_image_01.png`

Then, both temporary parts can be intuitively used in batch processing to loop over:
- dates
- identifiers

For example:
- `01-June_image_01.png`
- `01-June_image_02.png`
- `02-June_image_01.png`
  
> NOTE: separate temporary and permanent parts with `underscore`, and use `dash` within temporary and permanent parts.

Then, it becomes simple to group files and aggregate statistics per file batches, if you need this.

3. Including meaningful content in your filename

If you need a mutable parameter for your batch processing, include it. If this parameter is not suggested to use in processing, skip it.
  
**Bad example**
- `01-Jun-2026-00:01:02_image_01.png`
- `01-Jun-2026-02:12:26_image_02.png`
- `03-Jun-2026-05:32:19_image_03.png`
  
**Good example (daily images)**
- `01-Jun-2026_image_01.png`
- `02-Jun-2026_image_02.png`
- `03-Jun-2026_image_03.png`
- `04-Jun-2026_image_04.png`
...
- `31-Aug-2026_image_92.png`

4. Hierarchy of parameters in filenames

- Do not repeat the names of your 'sub-project' items in a filename to avoid duplications

A filename example in your repo:

your-project/
├── case_studies/
│   ├── england/
│   ├── ├── `01-Jun-2026_image_01.png`
│   ├── ├── `02-Jun-2026_image_02.png`
│   ├── wales/
│   ├── ├── `01-Jun-2026_image_01.png`
│   ├── ├── `02-Jun-2026_image_02.png`
│   ├── ├── `03-Jun-2026_image_03.png`
│   ├── scotland/
│   ├── ├── `01-Jun-2026_image_01.png`
│   ├── ├── `02-Jun-2026_image_02.png`
│   ├── northern_ireland/
│   ├── ├── `01-Jun-2026_image_01.png`
│   ├── ├── `02-Jun-2026_image_02.png`

---

**Main rules:**
- it's not recommended to include `spaces` in your filenames! This might break someone's code. Or, at least use consistently `space` and `underscore`.
- Once you have chosen a naming convention, stick to it.  It is unlikely you will know the assumptions others have made regarding file names in their code.  Changing the convention midstream 
will potentially break scripts written by others, and may lead to data loss or worse!


## What is this file?
Your goal is here is to know what a file is without having to open it. Most of these tips apply to naming folders too!

Some tips:
* Choose a format and stick to it. It's probably helpful to make a note of this somewhere, perhaps in a file called 'README' at the top level folder for a specific project. For example, `[Date]\_[sample number]\_[location]_[version]`. Keep filenames as brief as possible.
* Avoid spaces. If you start referring to files programmatically, process them through software or move them through the command line, it may cause you (or others using different operating system environments) a headache to have spaces in your filenames. Instead of spaces, you could use underscores (_), hyphens (-) or camel case (CapitaliseEachWord). Decide on what you will use and stick to it. 
* Also steer clear of special symbols as these can have other meanings in some contexts, or on other operating systems (\/:*?"<>|")
* Don't start with an asterisk (*) as this creates a hidden file that will not appear by default in your file explorer or finder window.
* Also steer clear of starting a filename with '.' as some operating systems such as Linux will interpret this as a hidden file which may puzzle others when it fails to appear.
* Choose a format for dates and, again, stick to it. Given that files are, by default, sorted alphanumerically, if you use this format `YYYY-MM-DD` your files will be organised chronologically. Be aware that files from other sources might use different date conventions, e.g. reversing month and day.

## Which files is this?
There are various approaches to version control. You might have heard of git which is universally used for code. If you are using naming conventions to distinguish between different versions of files, the permise is similar to above, choose a convention, write it, and stick to it.
In some applications, such as Geographic Information Systems, a working set of data is spread across potentially many files; in such cases it might be worth using a folder naming convention to indicate a consistent version of a set of files.

Some tips:
* Use the 'v-syntax' or semantic versioning. For example at the end of the filename at `_v1`, then `_v2` and so on (or `_v01` if you expect to have more than 9 versions). If you would like to be more granular, use semantic version, where you use 3 numbers seperated by full stops to stand for Major version, minor version and patch (small update). So, your first version might be `_1.0.0`, a small update might be `_1.0.1`. You might then do a manjor update and move to `_2.0.0`.
* Avoid using dates or initials to signify different versions as this makes it hard to see at a glance which is the most recent, and leaves you in a pickle if you want to save two versions in the same day.
* Avoid `FINAL` or `latest` in a filename. What happens when you find yourself unexpectedly editing your 'final' version? -->
