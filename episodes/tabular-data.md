---
title: "Best Practices for Tabular Data"
teaching: 35
exercises: 25
---

:::::::::::::::::::::::::::::::::::::: questions

* What makes a tabular dataset "bad" or difficult to work with?
* How do inconsistent column names, missing values, and stacked sub-tables cause errors in research?
* How can I clean and standardise messy spreadsheet data using standard tools like Excel?
* How can I track changes and apply version control to data files?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

By the end of this episode, learners will be able to:

* Identify common pitfalls in tabular datasets (inconsistent naming, stacked tables, implicit missing values, omitted units).
* Explain the core principles of tidy, machine-readable data.
* Apply standard spreadsheet tools (including Find and Replace) to clean and bulk-fix data errors.
* Evaluate strategies for tracking versions of data files and identify appropriate version control tools.

::::::::::::::::::::::::::::::::::::::::::::::::

# The Problem: Tabular Data Is Everywhere, But Often a Mess

Tabular data—data organised in rows and columns such as CSV files and Excel spreadsheets—is the most common format used across research disciplines. Whether you collect sensor output, clinical trial data, or survey responses, chances are high that your data lives in a table.

Unfortunately, spreadsheets are designed to be flexible for human eyes, which often leads to habits that make the data nearly impossible for computers (and collaborators) to process cleanly.

Consider a typical research scenario: you open a dataset shared by a predecessor or collaborator, and you want to plot trends or run a statistical script. However:

* Columns have slightly different names for the same measurement.
* Units are missing or buried in cell comments.
* Blank rows divide different sub-tables within the same file.
* Category names change midway down the sheet.

Before writing analysis scripts or generating figures, we must learn how to spot these issues and transform messy tables into structured, standardized data.

---

# Discussion: Spotting the Pitfalls in Bad Data

Let's start by inspecting a real-world example of a problematic dataset: `Incidence-Data(bad).csv`.

```text
ID,table,diagnosis Year,Age Specific Incidence Age0_49,age Specific Incidence  Age 0-54,ageSpecificIncidenceAge 55-59,age SpecificIncidence Age60-64,ageSpecificIncidenceAge65_69,age Spes IncidenceAge70-74,Age_Specific_IncidenceAge75_79,Age80_84,Age85_89,Age 90
1,All Oral Cavity,All Years,,,,,,,,,,
2,All Oral Cavity,2016,1.0226257,7.1519032,11.546455,14.977962,15.698924,,18.930473,18.508072,20.708221,20.908237
3,All Oral Cavity,2017,1.1054269,7.7797451,10.903189,13.126522,16.235617,16.384249,14.734702,17.668417,16.770851,18.774832
4,All Oral Cavity,2018,0.97927344,7.1045599,10.339744,13.697983,15.216359,16.599554,17.230083,16.623766,18.70484,22.232193
5,All Oral,,0.8994543,6.5189319,9.9068785,12.557129,18.081358,17.912762,18.943886,19.327847,20.068048,23.00526
6,All Oral,2020,0.80034059,6.8461018,9.9605932,12.894961,15.298739,16.424881,16.835621,17.944742,18.093088,20.342873
...

```

> ## Discussion
> 
> 
> Working in pairs:
> Open `Incidence-Data(bad).csv` in Excel or your preferred spreadsheet viewer. Look closely at the header row, the values, and the overall layout.
> List as many data management issues as you can find.
> Consider:
> * Header names and formatting
> * Category values in rows
> * Blank cells and missing data
> * Units of measurement
> * Table structure and layout
> 
> 

*After 5 minutes, gather responses as a group.*

---

# Why These Issues Matter: Human-Readable vs. Machine-Readable

Human eyes are remarkably forgiving. When a human reads a spreadsheet, they can instantly guess that `"All Oral"` and `"All Oral Cavity"` mean the same thing, or that a blank cell under the year `2018` probably means `2019`.

Computers, however, are strictly literal. To an automated script or statistical package (like R, Python, or SPSS):

* `"All Oral"` and `"All Oral Cavity"` are two completely unrelated experimental groups.
* `age Specific Incidence  Age 0-54` (with two spaces) is a different variable name from `age Specific Incidence Age 0-54` (with one space).
* A blank year cell is treated as null or `NaN`, causing data to be silently dropped from time-series plots.

Here is a breakdown of the issues identified in `Incidence-Data(bad).csv`:

### 1. Inconsistent Header Naming Conventions

The column headers mix title case, lowercase, camelCase, snake_case, and arbitrary spaces:

* `diagnosis Year` (contains a space and mixed case)
* `age Specific Incidence  Age 0-54` (contains double spaces)
* `ageSpecificIncidenceAge 55-59` (camelCase mixed with spaces)
* `age Spes IncidenceAge70-74` (spelling typo: "Spes")
* `Age80_84` vs `Age 90` (abruptly dropped the variable name prefix entirely)

### 2. Missing Units in Headers

What do the numbers in the data cells actually represent? Is this incidence per 1,000 people? Per 100,000 people? A percentage? Without units explicitly recorded in the header or accompanying metadata, the numbers are ambiguous.

### 3. Stacked Sub-Tables in a Single File

Rows 10 and 20 are completely blank, serving as visual dividers between sub-tables (`All Oral Cavity`, `Male`, `Female`). Furthermore, summary rows (e.g., `All Years`) are mixed directly into the same column as specific annual data.

### 4. Inconsistent Category Values

In the `table` column, the category is written as `"All Oral Cavity"` in rows 2–4, but changes to `"All Oral"` in rows 5–9.

### 5. Implicit Missing Data

In several rows, values for `diagnosis Year` or `table` are left blank because the author assumed the reader would know it "carried over" from the row above.

---

# Core Principles of Tidy Tabular Data

To make tabular data easy to analyze, archive, and share, adhere to three core rules of **Tidy Data**:

1. **Each variable forms a column:** Do not mix multiple variables into a single column, and do not drop variable names midway across headers.
2. **Each observation forms a row:** Every row should represent a single timepoint, subject, or experimental run.
3. **Each cell contains a single value:** Do not embed units, notes, or multiple values in a single cell.

```text
Good Header Example:
id, category, diagnosis_year, incidence_per_100k_age_0_49, incidence_per_100k_age_50_54

```

> ## Golden Rules for Clean Headers
> 
> 
> * Use lowercase letters.
> * Use underscores (`_`) instead of spaces.
> * Avoid special characters (`?`, `$`, `%`, `-`, `/`, `#`).
> * Keep names descriptive but concise.
> * Include units directly in the header (e.g., `weight_kg`, `temp_celsius`, `incidence_per_100k`).
> 
> 

---

# Demonstration: Cleaning Data in Excel

We will now walk through practical steps to fix these issues in Excel (or LibreOffice Calc / Google Sheets) without altering the underlying raw data.

> ## Instructor Note
> 
> 
> Emphasize preserving the original raw file! Always save your cleaned dataset under a new filename (e.g., `Incidence-Data_clean.csv`) or work on a copy.

---

## Step 1: Standardising Column Headers

1. Open `Incidence-Data(bad).csv` in Excel.
2. Select Row 1 (the header row).
3. Systematically rename headers to follow a single, consistent naming convention (e.g., lowercase with underscores):

| Old Header | New Clean Header | Reason for Change |
| --- | --- | --- |
| `diagnosis Year` | `diagnosis_year` | Replaced space with underscore, lowercase |
| `age Specific Incidence  Age 0-54` | `incidence_per_100k_age_0_54` | Fixed double spaces, added unit (`per_100k`), standardized naming |
| `age Spes IncidenceAge70-74` | `incidence_per_100k_age_70_74` | Fixed typo (`Spes`), standardized |
| `Age80_84` | `incidence_per_100k_age_80_84` | Restored missing variable prefix |

---

## Step 2: Bulk Fixes Using Find and Replace

Manually retyping mismatched category names across thousands of rows is slow and error-prone. We can use Excel's **Find and Replace** tool to perform bulk corrections.

1. Highlight the column containing category names (Column B: `table`).
2. Press **`Ctrl + H`** (Windows) or **`Cmd + H`** (macOS) to open the Find and Replace dialog.
3. In **Find what**, enter: `All Oral`
4. In **Replace with**, enter: `All Oral Cavity`
5. Click **Match entire cell contents** (if available) to avoid accidental partial matches.
6. Click **Replace All**.

Excel will report how many replacements were made, ensuring all rows now use a single category label.

---

## Step 3: Handling Missing Values and Stacked Tables

To convert stacked tables into a single, clean table:

1. **Fill in implicit missing values:** If rows 5 and 9 are missing the `diagnosis_year` value, consult the source documentation and enter the explicit year (e.g., `2019`, `2023`). Never leave cells blank if the value is known.
2. **Remove empty separator rows:** Delete completely blank rows (such as rows 10 and 20) that were used purely for visual padding.
3. **Separate summary rows if necessary:** Filter or remove summary rows like `All Years` if you plan to aggregate data programmatically, or move distinct sub-tables into separate CSV files if they represent fundamentally different experimental structures.

---

# Exercise: Cleaning the Incidence Dataset

> ## Challenge
> 
> 
> Working with your copy of `Incidence-Data(bad).csv`:
> 1. Use **Find and Replace** to standardise any inconsistent category names in the `table` column.
> 2. Standardize the headers for age groups `Age85_89` and `Age 90` so they match the format of the other age columns (`incidence_per_100k_age_85_89` and `incidence_per_100k_age_90_plus`).
> 3. Fill in missing values in the `diagnosis_year` column where values were implicitly omitted.
> 4. Delete the blank row dividers.
> 5. Save the modified file as `Incidence-Data_clean.csv`.
> 
> 
> Compare your cleaned file with a partner. Are all header names identical?

> ## Solution
> 
> 
> A clean version of the dataset should have:
> * Uniform headers across all columns without spaces or special characters.
> * Units (`per_100k`) included in the header metadata or documented clearly.
> * No blank separator rows.
> * Explicit values in every row (no implied carry-overs).
> * Consistent category labels (`All Oral Cavity` throughout).
> 
> 

---

# Version Control for Data Files

Once you have spent time cleaning a dataset, how do you manage changes as the project evolves?

## The Problem with File-Naming "Version Control"

It is common to see project folders filled with files like:

```text
Incidence-Data_clean.csv
Incidence-Data_clean_v2.csv
Incidence-Data_clean_v2_final.csv
Incidence-Data_clean_v2_final_FINAL_corrected.csv

```

This manual approach quickly leads to confusion over which file is the true "current" version, and makes it impossible to track *what* changed, *why* it changed, and *who* changed it.

---

## Version Control Strategies for Research Data

Depending on your data size and computational setup, several strategies exist for tracking changes:

### 1. Separation of Raw and Processed Data

Never modify your original raw dataset. Maintain a strict directory structure:

* `data/raw/`: Read-only original files (never modified).
* `data/processed/`: Cleaned, standardized outputs generated by documented steps or scripts.

### 2. Cloud and Storage Revision Histories

Platforms like OneDrive, SharePoint, and institutional research data repositories automatically record file version histories. If you accidentally overwrite a spreadsheet, you can restore previous versions through the cloud provider's web interface.

### 3. Formal Version Control with Git

For researchers working with text-based tabular files (such as CSVs, TSVs) and processing scripts (Python, R, MATLAB), formal version control systems like **Git** offer the gold standard for tracking history.

Git records snapshots of your files over time, allowing you to:

* View exact line-by-line differences between file versions.
* Revert to any previous state if an error is introduced.
* Collaborate safely without overwriting a colleague's work.

> ## Further Learning: Version Control with Git
> 
> 
> Demonstrating Git is beyond the scope of this introductory lesson, but learning Git is highly recommended for any researcher handling data and code.
> If you want to learn how to track changes, collaborate effectively, and manage versions using Git, consider signing up for our companion workshop:
> * **Software Carpentries: Version Control with Git**
> 
> 

---

::::::::::::::::::::::::::::::::::::: keypoints

* Humans and computers read tables differently; layout spreadsheet data for machine readability.
* Tidy data requires one variable per column, one observation per row, and one value per cell.
* Column headers should be consistent, lowercase, free of spaces, and explicitly state units of measurement.
* Tools like Find and Replace in spreadsheet software enable quick, bulk standardisation of inconsistent values.
* Never modify raw data directly; maintain separate raw and processed data folders.
* Formal version control tools like Git, alongside institutional cloud history, provide robust methods for tracking data changes over time.

::::::::::::::::::::::::::::::::::::::::::::::::