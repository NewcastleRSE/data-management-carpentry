---
title: "Naming files well"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- 

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- 

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

This is a lesson created via The Carpentries Workbench. It is written in
[Pandoc-flavored Markdown](https://pandoc.org/MANUAL.txt) for static files and
[R Markdown][r-markdown] for dynamic files that can render code into output. 
Please refer to the [Introduction to The Carpentries 
Workbench](https://carpentries.github.io/sandpaper-docs/) for full documentation.

...

::::::::::::::::::::::::::::::::::::: keypoints 

- 

::::::::::::::::::::::::::::::::::::::::::::::::

### How to name your files?

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

