---
title: Choosing a Data Storage Format
teaching: 35
exercises: 25
---
:::::::::::::::::::::::::::::::::::::: questions

* How does a file extension determine how data is stored and read?
* What factors should I consider when choosing a data format for my research?
* What are the differences between discipline-specific and domain-agnostic formats?
* What are the risks of converting files between different formats?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

By the end of this episode, learners will be able to:

* Explain how filename extensions correspond to underlying data structures.
* Evaluate the trade-offs (portability, metadata support, file size) of different data formats.
* Identify common domain-specific (e.g., `.nii`, `.fastq`) and multi-discipline cross-cutting formats (e.g., HDF5).
* Demonstrate the impact of format conversion on file size and data fidelity using image files.

::::::::::::::::::::::::::::::::::::::::::::::::

## The Problem: The Wrong Format Can Break Your Data

Over the last few episodes, we have cleaned up our files, established rules for deleting digital waste, and structured our tabular data. However, a major decision remains before we wrap up our data management workflow:

> What format should we save our data in?

Often, we default to whatever software we have open—saving tables as Excel workbooks (`.xlsx`) or text as Word documents (`.docx`). But the format you choose dictates who can open your data, how large the file will be on disk, whether metadata can be embedded safely, and if your data will still be readable in 10 or 20 years.

Choosing the wrong format can cause unreadable files, missing metadata, or a permanent loss of data fidelity.

---

## Understanding File Formats and Extensions

A file format is a standardized way that information is encoded for storage in a computer file.

The suffix at the end of a filename (e.g., `.csv`, `.xlsx`, `.txt`), known as the **file extension**, tells the operating system—and you—which application is expected to read that specific layout of bits.

### Common Formats and Trade-Offs

Some examples, out of many, are:

* **CSV (Comma-Separated Values - `.csv`):** A plain-text format where data fields are separated by commas. It is highly portable, open-source, and readable by almost any programming language or spreadsheet tool. However, it cannot store multiple sheets, cell formatting, or formula logic.
* **Excel Workbook (`.xlsx`):** A proprietary, compressed binary format owned by Microsoft. It is excellent for multi-sheet organization, complex formulas, and built-in plotting. The trade-off is that it requires specific software to parse cleanly, can introduce automated corruption (such as converting gene names into dates), and is less suitable for long-term data archiving.
* **FWF (Fixed-Width Format):** A plain-text format where each column has a fixed width. Portable and open source it is easily readable, like `.csv.` files. However, it can waste space and be hard to edit is data varies in length. 
* **JSON (Javascript Object Notation - `.json`):** A plain-text format that can hold extremally complex data structures. It is human readable and many programming languages have packages and libraries to read them. However, it can be verbose and hard for a human to follow due to its flexibility. 

---

:::::::::::::::: discussion

## What to Consider When Choosing a Format?

Before looking at complex formats, let's establish a set of requirements for evaluating how we store data.

Working in pairs or small groups:

Imagine you are starting a new 3-year research project that will generate thousands of files. What factors should you consider when deciding what file format to standardize on?

Take 5 minutes to think about compatibility, long-term access, and data complexity.

:::::::::::::::::::::::::::

---

## The Format Evaluation Checklist

When choosing a format, expect to balance these core pillars:

* **Open vs. Proprietary:** Can anyone open this file using free software (like `.csv`, `.txt`, `.json`), or does it require a paid software license (like `.mat` for MATLAB, `.sas7bdat` for SAS)? Open formats are generally preferred for FAIR data sharing.
* **Self-Documentation and Metadata:** Does the format allow you to embed metadata (data about the data) directly within the file? For example, can you include system headers, timestamps, and sensor configurations at the top of the file before the raw data matrix begins?
* **Data Complexity and Structure:** Is your data flat and two-dimensional (a simple table), or is it hierarchical and multi-dimensional (such as time-series mapping across a 3D spatial grid)? 
* **Human Readable or not** Can your file format be opened in a text editor and read or is data stored in a format which requires software to view (a binary file)? Binary files can be **much smaller** and can be read and written **much faster** than human readable formats.

---

## Domain-Specific vs. Cross-Discipline Formats

Different types of research demand different types of file architectures. Some formats are highly specialized, while others cross scientific boundaries.

### 1. Discipline-Specific Formats

Many fields have developed unique file formats tailored to their specific instrumentation and data scale requirements, for example:

* **Neuroscience / Medical Imaging:** `.nii` (NIfTI - Neuroimaging Informatics Technology Initiative). Used to store 3D and 4D brain scans from MRI machines, embedding spatial orientation metadata directly into the file header.
* **Genomics / Bioinformatics:** `.fastq` (FASTQ format). A text-based format for storing both a biological sequence (like DNA/RNA reads) and its corresponding quality scores, tightly packed for fast programmatic querying.
* **Geophysics / Seismology** `.asdf` (ASDF - Adaptable Seismic Data Format). Used to store seismic data. 
* **Astronomy** `.fits` (FITS - Flexible Image Transport System). A binary format for astronomical images and tables. Stores flexible header information. 
* **Machine learning** `.pmml`. A file format based off xml for storing machine learning models. 




### 2. Language specific formats (e.g. Pickle)
Some formats are designed to store data for spesific programming languages.

* **Python** `.pkl` (Pickle format)
* **R** `.rda` (RData format)
* **Matlab** `.mat` (Mat format)
* **Julia** `.jld2` (Julia Data Format 2)

These formats allow the given programming language to save data and even their current state to disc. This can be convenient, but introduces security risks. They are not recommended for data exchange or long-term storage.  

### 3. Cross-Discipline Formats (e.g., HDF5)

Some formats are designed to solve the problem of multi-dimensional data across entirely different fields.

* **HDF5 (Hierarchical Data Format v5 - `.h5` or `.hdf5`):** This open format behaves like a "file system within a single file." It allows you to store massive, multi-dimensional arrays of numbers alongside rich, custom metadata attributes. HDF5 
* **Parquet:** This open format preserves metadata, data types and file headers. Fast for reading but slower on writing. Excellent for Big Data. 

#### Who uses these"
 Climate scientists use HDF5 for satellite weather modeling, physicists use it for electron microscopy data, and machine learning researchers use it to store deep neural network weights. Parquet is used in machine learning or for distributed computing. 

### 4. Other

Some software have their own files formats for specific needs. In which case there should either be software tools to read them or exact descriptions of the file format for writing bispoke software to read it. 

---

:::::::::::: discussion

## Formats in Your Research Field - Shared Experiences

 Take 3 minutes to talk with the person next to you:

 1. What are the primary file formats you generate or interact with in your specific research domain?
 2. Are these formats open and easy to share, or do they require specialized, proprietary instruments or software to read?
 3. Why are these formats used? What needs to they address?

::::::::::::::::::::: 

---

## The Dangers of Format Conversion (Data Fidelity vs. Size)

Changing a data format can be a powerful way to reduce file size or improve software compatibility, but it can also be incredibly dangerous if you do not understand how the format handles information.

This is easiest to demonstrate using **image formats**, which are widely used across sciences to capture figures, microscopy, or satellite imagery.

### Lossy vs. Lossless Formats

* **BMP (`.bmp`):** A raw bitmap format. It saves the exact color data of every single pixel explicitly. It preserves 100% fidelity but results in massive file sizes.
* **PNG (`.png`):** A compressed, **lossless** format. It reduces the file size significantly using smart patterns, but when you open it, the image is mathematically identical to the original pixel-by-pixel.
* **JPEG (`.jpg` / `.jpeg`):** A compressed, **lossy** format. It achieves tiny file sizes by permanently throwing away visual information that the human eye is less likely to notice.

---

::::::::::::::::::::::::::: challenge


Let's look at what happens when we convert a high-resolution microscopy image (`cell_sample.bmp`) into a space-saving JPEG format.

 ## Challenge: Comparing Image Conversion and Fidelity - Inspecting the Artifacts
 
 
 1. Open your operating system's File Explorer or Finder and look at the file sizes of the following three identical-looking images:
 * `cell_sample.bmp` (Size: **12.5 MB**)
 * `cell_sample.png` (Size: **2.1 MB**) 
 * `cell_sample.jpg` (Size: **350 KB**)
 
 
 2. Open `cell_sample.jpg` and zoom in closely (400% or higher) on high-contrast areas or fine edges. Compare it side-by-side with `cell_sample.bmp`.
 

  **Questions for Discussion:**
 * What happened to the file size during the JPEG conversion?
 * What visual defects (compression artifacts) do you see around the fine details in the JPEG version?
 * Why is saving raw experimental images as JPEGs potentially dangerous for automated scientific analysis?
 
 

::::::::::::::: solution
 
 
 * **File Size:** The JPEG version is a fraction of the size of the original Bitmap, saving massive storage space.
 * **Fidelity Loss:** Zooming in reveals blocky distortions and blurry halos ("artifacts") around fine structures.
 * **Scientific Danger:** Automated image processing scripts (e.g., counting cells, measuring pixel intensities) will read these compression artifacts as actual data or fail to detect faint structures entirely. **Never use lossy compression formats (like JPEG) for raw analytical images.**
 
 

:::::::::::::::::::::
:::::::::::::::::::

---

## Data storage facilities -- Recommendations

Many data facilities have suggestions for storing data. For example 

- the [UK Data Service](https://ukdataservice.ac.uk/learning-hub/research-data-management/format-your-data/recommended-formats/) has various recommendations for various types of data, including tables, metadata, qualiatative data, image/video/audio data etc. 
- the [Library of Congress](https://www.loc.gov/preservation/resources/rfs/format-pref-summary.html) has similar recommendations

but funders and other data archives will have their own preferences. 

There are also websites, such as at the [Library of Congress](https://www.loc.gov/preservation/digital/formats/fdd/browse_list.shtml) which discuss various file formats. 


::::::::::::::::::::::::::::::::::::: keypoints

* Filename extensions guide the operating system on how to parse binary data.
* Prefer open data formats over proprietary ones to guarantee long-term accessibility and transparency.
* Formats like NIfTI and FASTQ serve specialized domain requirements, while HDF5 provides cross-discipline support for hierarchical data.
* Metadata should ideally be integrated directly within the data file format headers.
* Converting between formats can lead to permanent data corruption or loss of fidelity, especially when shifting to lossy formats.

::::::::::::::::::::::::::::::::::::::::::::::::