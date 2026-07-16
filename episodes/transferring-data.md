---
title: "Storing and Transferring Data Efficiently"
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions

- Why do some datasets take up more storage than others?
- How can I measure the size of my data?
- What is file compression and when should I use it?
- When is changing file format an appropriate solution?
- What are the best ways to transfer data between collaborators?
- How can I reduce storage requirements without losing important information?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

By the end of this episode, learners will be able to:

- Determine the size of files and folders using a graphical file browser.
- Explain what file compression is and how it works.
- Compress files and folders using common desktop operating systems.
- Identify situations where compression is useful and where it is not.
- Recognise that file formats can affect storage requirements.
- Evaluate different methods for transferring data.
- Choose an appropriate transfer method based on data size and project requirements.

::::::::::::::::::::::::::::::::::::::::::::::::

# The Problem: The Data Is Too Big

Over the last few episodes we have:

- Organised the folder structure
- Improved file names
- Added documentation
- Chosen an appropriate storage location

The project is now much easier to understand.

Unfortunately, a new problem has appeared.

Your supervisor asks:

> "Can you send the cleaned dataset to our collaborator?"

The collaborator has an older lab computer that:

- Has very little free storage space
- Has a slow internet connection
- Cannot easily accept very large files by email

You need to make the dataset as small and transferable as possible without damaging the data.

This situation is common in research.

As projects grow, researchers often encounter:

- Storage quotas
- Slow file transfers
- Limited network bandwidth
- Data archives that are too large to share easily

Before we can solve these problems, we need to understand how data size is measured.

---

::::::::::::::::::::::::::::::::::::: discussion
How Could We Make The Data Smaller?


 Working in pairs:

 What options can you think of for reducing the amount of storage used by a dataset?

 Consider:

 - Temporary files
 - File formats
 - Compression
 - Duplicate data
 - Images and media

 Write down as many ideas as possible.

After a few minutes, discuss responses as a group.

::::::::::::::::::::::::::::::::::::::::: 

Common answers may include:

- Compressing files
- Deleting duplicates
- Removing temporary files
- Choosing more efficient file formats
- Archiving old outputs
- Resizing images
- Removing unnecessary intermediate results

::::::::::::::::::::::::::::::::::::: instructor
>
> Learners often jump immediately to deleting files.
>
> Emphasise that deletion is usually the last option.
>
> Compression and improved organisation often reduce storage requirements significantly without losing information.

:::::::::::::::::::::::::::::::::::::::: 

---

# Understanding File Size

Before making data smaller, we need to know:

> How large is it now?

In data management we often measure storage using units such as:

```text
KB  (Kilobyte)
MB  (Megabyte)
GB  (Gigabyte)
TB  (Terabyte)
```

Each step represents a large increase in storage requirements.

For example:

```text
1,000 MB ≈ 1 GB
1,000 GB ≈ 1 TB
```

As datasets grow, even small improvements can translate into large storage savings.

---

# What Does File Size Represent?

Every file occupies space on a storage device.

Files are ultimately stored as binary data on:

- Hard drives
- Solid state drives (SSDs)
- Network storage
- Cloud storage

When File Explorer reports that a file is:

```text
250 MB
```

it is telling us approximately how much storage capacity that file occupies.

Larger files:

- Require more storage
- Take longer to transfer
- Take longer to back up
- May exceed attachment limits

Understanding file sizes helps us make informed decisions.

---

# Demonstration: Viewing File Sizes

## Individual Files

Using File Explorer:

1. Navigate to the dataset.
2. Right-click a file.
3. Select **Properties**.
4. Observe the reported file size.

---

## Folders

To view the size of a folder:

1. Right-click the folder.
2. Select **Properties**.
3. Wait while the operating system calculates the total size.

This may take a few moments for large datasets.

---

## Alternative: File Explorer Columns

Switch File Explorer to **Details View**.

The size column can be displayed for many file types.

This can make large files easier to identify.

> ## Instructor Note
>
> Demonstrate both approaches.
>
> Learners often find folder-size properties particularly useful because they rarely realise the information is available.

---

# File Compression

One of the most common ways to reduce storage requirements is compression.

## What Is Compression?

Compression reduces the amount of storage required by a file without changing its contents.

It works by storing information more efficiently.

For example:

```text
AAAAAAABBBBBBBBBCCCCCCCC
```

contains repeated patterns.

A compression tool can represent these patterns more efficiently than storing every character individually.

The result is a smaller file.

---

## Lossless and Lossy Compression

There are two broad forms of compression.

### Lossless Compression

Lossless compression preserves all information.

After decompression:

```text
Original File == Restored File
```

Examples:

- ZIP
- GZIP
- 7Z

These are commonly used for research data.

---

### Lossy Compression

Lossy compression achieves greater size reduction by discarding information.

Examples:

- JPEG images
- MP3 audio
- Some video formats

The resulting file may be smaller, but some original information has been lost.

For research data, lossy compression should be used with care.

---

# Demonstration: Compressing A Folder

:::::::::: tab

### Windows

1. Right-click the folder.
2. Select:

```text
Send To → Compressed (zipped) Folder
```

3. A ZIP file will be created.

For example:

```text
clean_data.zip
```

### macOS

1. Right-click the folder.
2. Choose:

```text
Compress
```

A ZIP archive will be created.


### Linux

Most desktop file managers provide a similar option:

```text
Right-click → Compress
```

The exact wording varies between desktop environments.

:::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::: instructor
>
> Demonstrate compression on the cleaned project directory.
>
> Show both the original folder size and the compressed archive size.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# When Should You Compress Data?

Compression is often useful when:

- Archiving data
- Transferring data
- Emailing files
- Backing up projects

Examples:

```text
project.zip
results.zip
archive.zip
```

Compression can significantly reduce transfer times.

---

# When Should You Avoid Compression?

Compression is not always beneficial.

For example:

- Actively edited files
- Frequently accessed files
- Files already compressed

Many formats already include compression.

Examples:

```text
jpg
png
mp4
mp3
pdf
```

Compressing these files often produces very little size reduction.

:::::::::::::::::::::::::::::::::::::::::::::::::  callout

 If a file format is already compressed, zipping it again may provide almost no additional benefit.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: challenge
 How Much Space Can We Save?

> ## Challenge
>
> Determine the size of the cleaned project folder.
>
> Then:
>
> 1. Create a ZIP archive.
> 2. Measure the size of the ZIP file.
> 3. Calculate the reduction in size.
>
> Discuss:
>
> - Was the reduction larger or smaller than expected?
> - Why do you think this happened?

:::::::::::::::::::::::: solution
>
> Results will vary depending on the data.
>
> Text files and spreadsheets often compress well.
>
> Images, video, and already-compressed formats may show little improvement.

:::::::::::::::::::::::: 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# File Formats And Storage

Compression is not the only way to reduce file size.

Sometimes the format itself matters.

Different file formats store information differently.

For example:

```text
report.docx
report.pdf
report.txt
```

all contain text but may occupy different amounts of storage.

Similarly:

```text
image.bmp
image.png
image.jpg
```

can have dramatically different sizes.

---

# An Example: Bitmap Images

Suppose we save the same image as:

```text
sample.bmp
```

A bitmap stores every pixel explicitly.

This often results in a large file.

The same image saved as:

```text
sample.png
```

may be significantly smaller because PNG uses compression internally.

The image looks the same, but storage requirements differ.

---

# Trade-Offs

Smaller files are not always better.

Changing formats may affect:

- Data quality
- Software compatibility
- Metadata support
- Long-term preservation

For example:

```text
CSV
```

is highly portable and easy to share.

However:

```text
Excel
```

supports multiple sheets and richer formatting.

Neither format is universally superior.

The best format depends on your intended use.

> ## Looking Ahead
>
> We will discuss choosing data formats in much more detail in a later episode.

---

::::::::::::::::::::::::::::::::::::::::::::::::::: discussion

 How Have You Shared Data Before?

> ## Discussion
>
> Think about the last time you shared research data.
>
> How did you do it?
>
> Examples might include:
>
> - Email attachments
> - OneDrive links
> - SharePoint
> - USB drives
> - Shared network storage
> - Cloud platforms
>
> What limitations did you encounter?

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Methods For Transferring Data

Different transfer methods are appropriate for different situations.

---

## Email Attachments

Suitable for:

- Small files
- Documents
- Individual figures

Advantages:

- Simple
- Familiar

Disadvantages:

- Attachment size limits
- Duplicate copies
- Difficult version management

Generally unsuitable for large datasets.

---

## OneDrive or SharePoint Links

Suitable for:

- Collaborative projects
- Medium-sized datasets
- Shared documents

Advantages:

- Shared access
- Version history in many cases
- No attachment limits

Disadvantages:

- Requires permission management
- Can become difficult for very large datasets

---

## Shared Project Storage

Suitable for:

- Ongoing collaborations
- Research teams
- Institutional projects

Advantages:

- Centralised location
- Controlled access
- Common source of truth

Disadvantages:

- Access may be limited to project members

---

## Globus

Globus is commonly used in research environments for transferring large datasets.

Suitable for:

- Large research datasets
- HPC environments
- Multi-gigabyte or multi-terabyte transfers

Advantages:

- Reliable
- Designed for research
- Handles interruptions well

Disadvantages:

- May require institutional access
- More complex than simple file sharing

---

# A Note On Command-Line Tools

Large-scale research computing environments often use command-line transfer tools such as:

```text
rsync
scp
sftp
```

These tools are extremely powerful and commonly used on HPC systems.

However, they are beyond the scope of this lesson.

> ## Further Learning
>
> Learners interested in transferring data to servers or HPC systems should consider attending:
>
> - Carpentries Shell/Bash workshops
> - HPC training courses
>
> These courses cover tools such as `rsync` in more detail.

---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

 Choosing A Transfer Method

> ## Challenge
>
> Match the transfer method to the scenario.
>
> 1. A 5 MB document for a colleague.
> 2. A 300 MB dataset shared among a research group.
> 3. A 2 TB dataset for HPC processing.
> 4. A published dataset accompanying a paper.
>
> Discuss your choices with a partner.

:::::::::::::::::::::::: solution
>
> Example answers:
>
> 1. Email attachment.
> 2. OneDrive, SharePoint, or shared project storage.
> 3. Globus or institutional research storage.
> 4. Repository such as Zenodo.
>
> The important consideration is matching tools to scale and purpose.

:::::::::::::::::::::::: 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# Looking Ahead

We now know how to:

- Measure storage usage
- Compress data
- Reduce transfer sizes
- Choose transfer methods

The next challenge is deciding what data should actually be kept.

In the next episode we will explore:

- Data lifecycles
- Archiving
- Retention policies
- Digital waste

and discuss how to make sensible decisions about what data should remain part of a project and what can be removed.

::::::::::::::::::::::::::::::::::::: keypoints 

- Storage space and transfer speed are important practical considerations in research.
- File size can be measured using file browser tools.
- Compression reduces file size and is particularly useful for archiving and transfer.
- Lossless compression preserves data and is generally preferred for research data.
- Some file formats are more storage-efficient than others.
- Choosing a different file format may involve trade-offs.
- Different transfer methods are appropriate for different dataset sizes.
- Large research datasets often require specialist transfer tools.
- Understanding your data helps you make informed decisions about storage and transfer.

::::::::::::::::::::::::::::::::::::::::::::::::