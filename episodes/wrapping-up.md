---
title: "Wrapping up"
teaching: 10
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

* What are FAIR principles regarding data management.
* How can I track changes and apply version control to data files?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

* Learn FAIR principles for the management and publication of data.
* Evaluate strategies for tracking versions of data files and identify appropriate version control tools.

::::::::::::::::::::::::::::::::::::::::::::::::

## Summary and Discussion

We have discussed how to structure your project folders and systematically name files as well as how to store metadata in documentation. We have also discussed the transfer, deletion and storage of data as well as the types of file formats available. 

In general,

- data should be stored in clearly defined folders, each with a particular type of file, including notes, papers, raw data, processed data etc. with systematic file names that are easy for both humans and computers to use. 
- the documentation should allow a newcomer to the project to quickly understand which data are stored where without asking you.
- private and special data should be treated with care, following GDPR rules. 
- data can be stored and transferred using a number of tools including physical media or the cloud but each methods has pros and cons
- data can be archived instead of deleted outright, and different funders and domains will have different rules on data retention. 
- there is no-one-size-fits-all for all research projects and domains but using a system and adequate documentation is essential

There are various principles for storing and publishing data, but one popular set of guidelines are the FAIR principles.


## FAIR Principles 

FAIR principles are a set of principles for data management and publication by [Wilkinson et al., 2016][wilk]. 

"Wilkinson, M. D. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci. Data 3:160018 doi: 10.1038/sdata.2016.18 (2016)"

The FAIR acronym stands for:

- Findable
- Accessible
- Interoperable
- Reusable

These principles apply to humans and computers, and to both data and metadata. 

### Findable

Data can be located by others.

1. Data are assigned a globally unique/persistent ID (DOI)
2. Data include metadata
3. Metadata clearly identify the data
4. Data are registered, indexable and searchable. 

paraphrased slightly from [Wilkinson et al., 2016][wilk]


Examples are:


#### Poor

Data is located on my computer, external disk, personal OneDrive, or the Research Data Warehouse for your project. The data cannot be accessed but anyone out side of the group. Few people even know the data exists at all. 

#### Good

Data is available on a (reputable) online data repository, as discussed in the "Choosing Where to Store Your Data" lesson. These repositories are indexable by search engines so others can locate your data, and provide permanent DOIs so others can cite your work. 



### Accessible

It is simple to access the data. 

1. Data are retrievable by their unique identifier 
2. The protocol for retrieving the data is open, free and universal
3. The protocol allows for authentication and authorisation where appropriate
4. Metadata are accessible, even when the data is not available

paraphrased slightly from [Wilkinson et al., 2016][wilk]

Metadata should be available, even if the data cannot be. 

:::::::::::::::: caution

FAIR principles do not require the data to be open access. 

::::::::::::::::

### Interoperable

Data needs to be combined with other data sources. 

It needs to operate with other applications and workflows. Make sure that data is stated in a widely adopted data format in your research area. This will reduce friction for others trying to use your data with their existing tools.

1. Data use a formal, accessible, shared language
2. Data and metadata use FAIR vocabularies
3. Data and metadata include references to other sources of data

paraphrased slightly from [Wilkinson et al., 2016][wilk]

### Reusable

Data is well documented and well laid out. The data is licensed in such a way that others can use, modify and distribute it. 

1. Data are fully described
2. Data is clearly and accessibly licensed
3. Data have detailed providence recorded
4. Data meet community standards.

paraphrased slightly from [Wilkinson et al., 2016][wilk]

::::::::::::::: caution

If there is no license the default is for maximum protection e.g. others cannot modify or distribute it.  

:::::::::::::::

## Version Control for Data Files

Version control keeps track of the history of files instead of overwriting them. This can be via file naming and/or version control software. 

### The Problem with File-Naming "Version Control"

It is common to see project folders filled with files like:

```text
Incidence-Data_clean.csv
Incidence-Data_clean_v2.csv
Incidence-Data_clean_v2_final.csv
Incidence-Data_clean_v2_final_FINAL_corrected.csv
```

This manual approach quickly leads to confusion over which file is the true "current" version, and makes it impossible to track *what* changed, *why* it changed, and *who* changed it.

Try not to use `final` as additional changes might be required. 

```text
Incidence-Data_clean_v1.csv
Incidence-Data_clean_v2.csv
Incidence-Data_clean_v3.csv
Incidence-Data_clean_v4.csv
```
And note in the folder README which is the (current) final version for future reference. 


---

### Version Control Strategies for Research Data

Depending on your data size and computational setup, several strategies exist for tracking changes:

#### 1. Separation of Raw and Processed Data

Never modify your original raw dataset. Maintain a strict directory structure:

* `data/raw/`: Read-only original files (never modified).
* `data/processed/`: Cleaned, standardized outputs generated by documented steps or scripts.

#### 2. Cloud and Storage Revision Histories

Platforms like OneDrive, SharePoint, and institutional research data repositories automatically record file version histories. If you accidentally overwrite a spreadsheet, you can restore previous versions through the cloud provider's web interface.

#### 3. Formal Version Control with Git

For researchers working with text-based tabular files (such as CSVs, TSVs) and processing scripts (Python, R, MATLAB), formal version control systems like **Git** offer the gold standard for tracking history.

Git records snapshots of your files over time, allowing you to:

* View exact line-by-line differences between file versions.
* Revert to any previous state if an error is introduced.
* Collaborate safely without overwriting a colleague's work.

### Further Learning: Version Control with Git 
 
 Demonstrating Git is beyond the scope of this introductory lesson, but learning Git is highly recommended for any researcher handling data and code.
 If you want to learn how to track changes, collaborate effectively, and manage versions using Git, consider signing up for our companion workshop:

 * **Software Carpentries: Version Control with Git**
 

## Next steps

As data becomes more complex and inter-related various other tools might be beneficial. These include

### Databases

Databases allow users to query different datasets in combinations using unique identifiers shared between databases. For example, you may have data about various penguin trackers, which include:

``Table=tracker_info``

| tracker_id | tracker frequency | date applied | tracker brand | tracker product id |
|---|---|---|---|---|
| ... |  ... |  ... |  ... |  ... | 

and another table of:

``Table=tracker_current_location``

| tracker_id | latitude | longitude | 
|---|---|---|
| ... |  ... |  ... |  

and another table with:

``Table=penguin_info``

| penguin name | penguin id | sex | species | age | tracker_id | place of birth | 
|---|---|---|---|---|---|---|
| ... |  ... |  ... |  ... |  ... | ... | ... | 

and another table with:

``Table=island_info``

| island name | latitude | longitude |
|---|---|---|
| ... |  ... |  ... |  

These tables (tracker_info, tracker_current_location, penguin_info, island_info) can be combined in various ways using a database to track penguins to different islands efficiently. This is particularly important when the data are large. Queries include: which tracker band is <penguin name> wearing and when was it applied (perhaps if there is. given battery life) or how many penguins are on a different island to which they were born etc. 

There are many types of database, including Microsoft Access, which has a graphical user interface or a number of others which are queryable using a programming language called SQL. Depending on the database type chosen the data can be structured (in tables) or unstructured (text, images etc.).

A detailed discussion of SQL is beyond the scope of this course, but there are many tutorials online, such as [W3Schools][w3_sql].

### Dataframes

These tools are often available in programming languages such as R or Python, which act like miniature Databases, with many of the same tools for combining and grouping data from different tables. For Python these include packages such as ``pandas``, the newer ``polars``, or ``dask`` for parallel computing. In R there is the built in ``data.frame`` package.



::::::::::::::::::::::::::::::::::::: keypoints 

* Formal version control tools like Git, alongside institutional cloud history, provide robust methods for tracking data changes over time.
::::::::::::::::::::::::::::::::::::::::::::::::

[wilk]: https://www.nature.com/articles/sdata201618
[w3_sql]: https://www.w3schools.com/sql/