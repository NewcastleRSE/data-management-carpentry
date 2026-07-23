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

Files can be plain text (human readable) or binary (readable only by the computer). Plain text files have the advantage that s user can look inside them and see the data, while binary files are more compact and faster for the computer to read and write. 

### Common Formats and Trade-Offs

Some examples of the many types of file formats are

* **CSV (Comma-Separated Values - `.csv`):** A plain-text format where data fields are separated by commas. It is highly portable, open-source, and readable by almost any programming language or spreadsheet tool. However, it cannot store multiple sheets, cell formatting, or formula logic.
* **Excel Workbook (`.xlsx`):** A proprietary, compressed binary format owned by Microsoft. It is excellent for multi-sheet organization, complex formulas, and built-in plotting. The trade-off is that it requires specific software to parse cleanly, can introduce automated corruption (such as converting gene names into dates), and is less suitable for long-term data archiving.
* **FWF (Fixed-Width Format, - usually `.txt`):** A plain-text format where each column has a fixed width. Because it is portable and open source it is easily readable, like `.csv` files. However, it can waste space and be hard to edit if values vary in length. If the size of a given column can vary significantly (e.g. have value `12` or `124535643245667` then shorter entries need considerable padding or risk truncating longer entries).
* **JSON (Javascript Object Notation - `.json`):** A plain-text format that organises data into sets of key-value pairs, such as {"first_name": "John", "last_name": "Smith"}, where "first_name" and "last_name" are the keys and "John" and "Smith" are the corresponding values. This flexible format allows JSON to store very complex data structures, but it can be verbose and difficult to follow. Many programming languages have libraries for reading and manipulating JSON. Unlike the other formats listed above JSON files are not limited to tables and not every field needs to be the same for every entry, making it highly flexible. 

CSV, Excel Workbook, and FWF files are for storing tables. They are good for data which have a certain number of items (rows) each with a number of values, or noted missing values, for a consistent set of variables (columns). 

---

:::::::::::::::: discussion

## What to Consider When Choosing a File Format?

Before looking at complex formats, let's establish a set of requirements for evaluating how we store data.

Working in pairs or small groups:

Imagine you are starting a new 3-year research project that will generate thousands of files. What factors should you consider when deciding what file format to use?

Take 5 minutes to think about compatibility, long-term access, and data complexity.

:::::::::::::::::::::::::::

---

## Domain-Specific vs. Cross-Discipline Formats

Different types of research demand different types of file architectures. Some formats are highly specialized, while others cross scientific boundaries.

### 1. Discipline-Specific Formats

Many fields have developed unique file formats tailored to their specific instrumentation and data scale requirements:

* **Neuroscience / Medical Imaging:** `.nii` (NIfTI - Neuroimaging Informatics Technology Initiative). Used to store 3D and 4D brain scans from MRI machines, embedding spatial orientation metadata directly into the file header.
* **Genomics / Bioinformatics:** `.fastq` (FASTQ format). A text-based format for storing both a biological sequence (like DNA/RNA reads) and its corresponding quality scores, tightly packed for fast programmatic querying.
* **Geophysics / Seismology:** `.asdf` (ASDF - Adaptable Seismic Data Format). Used to store seismic data. 
* **Astronomy:** `.fits` (FITS - Flexible Image Transport System). A binary format for astronomical images and tables. Stores flexible header information. 
* **Machine learning:** `.pmml`. A file format for storing some types of machine learning models. 


### 2. Language specific formats (e.g. Pickle)
Some formats are designed to store data for specific programming languages.

* **Python** `.pkl` (Pickle format)
* **R** `.rda` (RData format)
* **Matlab** `.mat` (Mat format)
* **Julia** `.jld2` (Julia Data Format 2)

These formats allow the given programming language to save data and even their current state to disc. This storage approach can be convenient, but introduces security risks. For example, Python pickle files can contain instructions that execute arbitrary Python code when loaded. They are not recommended for data exchange or long-term storage.  

### 3. Cross-Discipline Formats (e.g., HDF5)

Some formats are designed to solve the problem of multi-dimensional data across multiple fields with different types of data.

* **HDF5 (Hierarchical Data Format v5 - `.h5` or `.hdf5`):** This open format behaves like a "file system within a single file." It allows you to store large, multi-dimensional arrays of numbers alongside rich, custom metadata attributes. If is fast, flexible and compact. It is not human readable. 
* **Parquet:** This open format preserves metadata, data types, and file headers. It is fast for reading but slower of writing. Excellent for Big Data which will be written once and rad many times. Like HDF5 it is not human readable. 

#### Who uses these file formats?

Common users of HDF5 include climate scientists for satellite weather models, physicists for electron microscopy data, machine learning researchers for deep neural network models, and neuroscientists for brain activity (e.g., EEG) data.

### 4. Other

Some software has their own files formats for designed for specific needs - for example, Microsoft PowerPoint uses `.pptx` files and Adobe Photoshop stores image data in `.psd` files. Other formats may be based on common formats, such as binary or HDF5, but require a certain structure for the header or metadata. These formats will have software tools for reading them and/or provide descriptions of the file format to allow writing bespoke software to read it.

---

## The Format Evaluation Checklist

When choosing a format, expect to balance these core pillars:

* **Open vs. Proprietary:** Open file formats are data structures that are publicly documented, free for anyone to use, and maintained by an independent, non-profit standards organisation. Meanwhile, proprietary file formats are owned by a private company or individual that imposes legal restrictions on their use. While some proprietary formats, such as `.mat` files (created by MATLAB), have open documentation and can be read using free software, the free readers may not support all of the format's features. Additionally, the owner retains control over its use and definition, potentially leading to restrictions or changed formats in future versions. As such, open formats are generally preferred for FAIR data sharing.
* **Self-Documentation and Metadata:** Does the format allow you to embed metadata (data about the data) directly within the file? For example, can you include system headers, timestamps, and sensor configurations at the top of the file?
* **Data Complexity and Structure:** Is your data flat and two-dimensional (a simple table), or is it hierarchical and multi-dimensional (such as time-series mapping across a 3D spatial grid)? 
* **Human Readable or Binary:** Can your file format be opened in a text editor and read (e.g., `.csv`, `.json`), or is data stored in a format which requires software to view (e.g., a binary file)? Human-readable files can be easier to manually review, but many machine-readable file formats are smaller and can be read/written much faster than human-readable formats.

---

:::::::::::: discussion

## Formats in Your Research Field - Shared Experiences

 Take 3 minutes to talk with the person next to you:

 1. What are the primary file formats you generate or interact with in your specific research domain?
 2. Are these formats open and easy to share, or do they require specialised, proprietary instruments or software to read?
 3. Why are these formats used? What needs do they address?

::::::::::::::::::::: 

---

## The Dangers of Format Conversion (Data Fidelity vs. Size)

Changing a data format can be a powerful way to reduce file size or improve software compatibility, but it can also be incredibly dangerous if you do not understand how the format handles information.

This is easiest to demonstrate using **image formats**, which are widely used across sciences to capture figures, microscopy, or satellite imagery.

### Lossy vs. Lossless Formats

* **BMP (`.bmp`):** A raw bitmap format. It saves the exact color data of every single pixel explicitly. It preserves 100% fidelity but results in large file sizes.
* **PNG (`.png`):** A compressed, **lossless** format. It reduces the file size significantly using smart patterns, but when you open it, the image is mathematically identical to the original pixel-by-pixel.
* **JPEG (`.jpg` / `.jpeg`):** A compressed, **lossy** format. It achieves tiny file sizes by permanently throwing away visual information that the human eye is less likely to notice.
* **SVG (`.svg`):** A vector graphics format which scales freely and defines graphics using vertices and lines. They are easily edited. However, they are not suitable for pixel-based images.  

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
 * What happens to the file size when the BMP file is converted to JPEG format?
 * What visual defects (compression artifacts) do you see around the fine details in the JPEG version?
 * Why is saving raw experimental images as JPEGs potentially dangerous for automated scientific analysis?
 
 

::::::::::::::: solution
 
 
 * **File Size:** The JPEG version is a fraction of the size of the original Bitmap, saving a large amount of storage space.
 * **Fidelity Loss:** Zooming in reveals blocky distortions and blurry halos ("artifacts") around fine structures.
 * **Scientific Danger:** Automated image processing scripts (e.g., counting cells, measuring pixel intensities) will read these compression artifacts as actual data or fail to detect faint structures entirely. **Never use lossy compression formats (like JPEG) for raw analytical images.**
 
 See [Image Processing in Matlab](https://blogs.mathworks.com/steve/2022/12/19/avoid-jpeg-for-image-analysis/) and Section 6.8 of [Cromey D. W. (2013). Digital images are data: and should be treated as such. Methods in molecular biology (Clifton, N.J.), 931, 1–27. https://doi.org/10.1007/978-1-62703-056-4_1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4210356/) 

 > 

:::::::::::::::::::::
:::::::::::::::::::

---

## Data storage facilities -- Recommendations

Many data facilities have suggestions for storing data. For example 

- the [UK Data Service](https://ukdataservice.ac.uk/learning-hub/research-data-management/format-your-data/recommended-formats/) has recommendations for various types of data, including tables, image, video, audio, and text, as well as their associated metadata.
- the [Library of Congress](https://www.loc.gov/preservation/resources/rfs/format-pref-summary.html) has similar recommendations

but funders and other data archives will have their own preferences. 

The [Library of Congress](https://www.loc.gov/preservation/digital/formats/fdd/browse_list.shtml) also provides an overview of various file formats. 


::::::::::::::::::::::::::::::::::::: keypoints

* Filename extensions guide the operating system on how to parse binary data.
* Prefer open data formats over proprietary ones to guarantee long-term accessibility and transparency.
* Formats like NIfTI and FASTQ serve specialized domain requirements, while HDF5 provides cross-discipline support for hierarchical data.
* Metadata should ideally be integrated directly within the data file format headers.
* Converting between formats can lead to permanent data corruption or loss of fidelity, especially when shifting to lossy formats.

::::::::::::::::::::::::::::::::::::::::::::::::