---
title: "Documenting Your Data"
teaching: 25
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can I remember what my data is and where it came from?
- What information should I document about a project?
- Where should documentation be stored?
- What is a README file?
- How can I create project documentation using a graphical file browser?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

By the end of this episode, learners will be able to:

- Explain the purpose of research data documentation.
- Identify information that should be captured about a dataset.
- Create a README file using a graphical file browser.
- Document project structure, provenance, and data sources.
- Identify situations where additional documentation is needed.
- Improve the reusability of a dataset through documentation.
- Use file headers to store key metadata.

::::::::::::::::::::::::::::::::::::::::::::::::

## How Do I Remember and Share Where My Data Is Stored?

In the previous two episodes, we improved our folder structure and renamed our files.

The project now looks considerably better than it did when we inherited it.

However, several important questions remain unanswered:

- What does this dataset contain?
- Who collected it?
- When was it collected?
- How was it collected?
- What do the variables mean?
- What units were used?
- Which files are raw data?
- Which files were generated during analysis?
- What changes do different versions capture?
- Which version should be used?
- Which files relate to which other files?
- When was the data downloaded?
- Where was the data downloaded from?
- What software and versions of software were used to analyse the data?

Imagine returning to this project six months from now. Would you still remember all of these details? What about three years from now? What if somebody else joins or takes over the project?

Good folder structures and filenames help people **navigate** data. Documentation helps people **understand** data.

------------------------------

:::::::::::::::: challenge

## What Makes Data Easy to Understand?


Think about a dataset, project, software package, or repository that you found particularly easy to use.

 - What made it easy to understand?
 - What information was available?
 - How was that information presented?
 - Was there a README file?
 - Was documentation easy to find?

Conversely:

 - Have you ever received poorly documented data?
 - What information was missing?

Discuss responses with your neighbour.

::::::::::: solution

Helpful documentation practices include

- Clear explanations
- Consistent organisation
- Readily available information
- Definitions of terms and variables
- Information about data collection
- Contact details

:::::::::::
:::::::::::

::::::::::::::::: instructor

Many learners will have experienced poorly documented datasets.

Encourage them to connect their frustrations as data users with their responsibilities as data creators.

:::::::::::::::::::::::::::::::::::::

------------------------------

## Documentation Is For Humans

When discussing data management, people often focus on technology:

- Storage
- File formats
- Software
- Analysis tools

However, one of the biggest barriers to reusing data is simply understanding it. Good documentation reduces the number of assumptions that somebody must make when using a dataset.

::::::::::::: callout

The most important collaborator you will ever have is often **future you**.

:::::::::::::

Documentation helps future you understand decisions that seem obvious today, but may be forgotten later.

---

## What Is Metadata?

::::::::::::: callout

Metadata is **data about data**.

:::::::::::::


Metadata provides context that helps us understand a dataset.

For example, consider the file:

```text
incidence_data.csv
```

The filename tells us very little.

Useful metadata might include:

- What the dataset contains.
- Who collected it.
- When it was collected.
- How it was collected.
- Units of measurement.
- Data quality or collection issues.
- Licensing information.
- Contact details.
- Link to the original source of the data if using an external source of data.

Metadata helps transform a collection of numbers into something meaningful.

Some software autogenerates some metadata for you. 

For example, Microsoft Word produces

- Author
- Company
- Template
- Date Created
- Date Modified
- Last Saved By
- Revision number
- Total editing time
- etc...

by default. Other software will store different metadata. 

:::::::::::::: caution

Automated metadata may add information you do not wish to share to the file. Ensure you do not inadvertently share sensitive or private metadata when distributing data. 

Office provides tools for removing automated metadata if required. 

::::::::::::::

---

## What Should We Document?

Given the huge variety of research and data, there is no universal documentation standard suitable for every project. However, most project-level documentation should include

- Project description
- Dataset descriptions
- Data origins
- Data use and analysis
- Contact details
- README file(s)

Some projects may also include
- Data dictionaries
- Standard operating procedures
- Project logs
- Parameter files
- Funding agency

These elements will be expanded on below. 

::::::::::::: callout

Research should be reproducible. Given the information in the documentation and an accompanying paper or thesis, would someone else be able to repeat your research?

Would **future you** be able to repeat your research?

:::::::::::::

### Project Description

Provide a short description that summarises the project's goal; for example,


```text
This project investigates disease incidence in marine mammals
along the Scottish west coast between 2020 and 2025.
```

A new collaborator should understand the purpose of the project within a few seconds.

It may be tempting to skip this description and instead rely on a long project folder name such as

```text
marine_mammals_disease_scotland_westcoast_2020_to_2025
```

but this name is long and still ambiguous. Additionally, a project's scope and goals over change over time; what if your focus narrows to investigating seals or dolphins? It is easier to change the documentation than update folder names and references. 

---

## Data descriptions

Describe the available datasets and folders.

For example:

```text
raw_data/
Contains original incidence records obtained from collaborators.

processed_data/
Contains cleaned datasets used in analysis.

analysis/
Contains scripts and outputs generated during analysis.
```

This documentation helps people understand how to navigate your files and the relationships between different files. 

---

## Data origins

Data **provenance** - the full record of a dataset's origins and modifications - becomes increasingly important as projects grow, and certain projects may have strict rules for tracking providence. Some data sources include provenance information in file headers, while others store provenance in other locations. 

If data sources are updated, for example to correct collection errors or accidental changes, it is important to keep track of the new and old files. 

::::::::::::::: challenge

What things do you need to document to track the origin of the data for one of your projects?

Think about details you may need to 
- report in a paper or other publication
- reproduce the work in future
- assess or fix a data error that is discovered during the project

::::::::::::::: solution

Possible information to document:

- Was the data collected by your team? When? Where? Include links to other notes, such as lab manuals.
- Was it obtained from a collaborator? When?
- Was it downloaded from a repository? When?
- Was it generated by software? Which version?
- Were any corrections or other modifications made? Why, when, and by whom?

::::::::::::::::::
::::::::::::::::::

---

## Data use and analysis

Many projects involve extensive data analysis. This analysis needs to be well-documented to ensure anyone with the same data can reproduce your results.

If you share your data, you also need to include any access conditions, such as restrictions for publishing or storing the data.

:::::::::::::: challenge

Consider what information you should document on how you used and analysed the data during one of your project.

:::::::::::::: solution

Useful documentation might include

- Required software and their versions
- Processing steps and settings
- Important assumptions
- Known limitations of your analysis
- Access conditions - i.e., how to access the data and any restrictions on using it

These details can save future users significant amounts of time.

::::::::::::::
::::::::::::::


---

## Contact details

Include contact information whenever possible, including for a primary contact, so that collaborators and other researchers can ask questions or raise concerns.

For example:

```text
Project Lead (Primary Contact):
Dr Jane Smith

Email:
j.smith@example.ac.uk

Data Collection Lead:
Dr John Doe

johndoe@biguniversity.ac.uk
```

---

## README File(s)

One of the simplest and most effective forms of documentation is a README file.

A README is usually placed at the top level of a project:

```text
project/
│
├── README.txt
├── data/
├── analysis/
└── results/
```

It explains the project and helps people navigate it.

A good README provides enough information for someone to understand the project at a high level without opening any other files. 

::::::::::::: callout

A README does not need to be perfect. A simple README containing a few useful paragraphs is significantly better than no README at all!

Try to keep README files up to date. 

Keep files together with their READMEs if you exchange data with colleagues. 

:::::::::::::::::

---

### Example README Structure

Example template:

```text
Project Name

Project Description

Project Structure

Data Sources

File Naming Convention

Software Requirements

Contact Information

Last Updated
```

For example:

```text
Project Name:
    Marine Mammal Incidence Study

Project Description:
    Investigation of marine mammal health records collected
    between 2020 and 2025.

Project Structure:
    data/raw - original data
    data/processed - cleaned datasets
    analysis - analysis scripts
    results - generated outputs

Software Requirements:
    Data was analysed using Python 3.13
    See analysis/pyproject.toml file for Python package dependencies and versions

Contact:
    bob.badgerton@example.ac.uk

Last Updated:
    2026-07-01
```

Another example can be found [here](https://www.ncl.ac.uk/mediav8/library/key-messages/rdm/README.txt).

---


:::::::::::::: challenge

## Creating A README File

Follow along with the demo to make a README file for the inherited project.

### Step 1: Navigate To The Top-Level Folder

Open File Explorer.

Navigate to:

```text
legacy_dataset/
```

---

### Step 2: Create A New Text File

Right-click in an empty area of the window and select

```text
New → Text Document
```

to create a new file.

---

### Step 3: Rename The File

Rename the file `README.txt`.

---

### Step 4: Open The File

Double-click the file to open it in Notepad (or a similar text editor).

---

### Step 5: Add Basic Structure

Add headings such as

```text
Project Name

Description

Folder Structure

Data Sources

Contact Information

Last Updated
```

Save the file.

:::::::::::::::: solution

::::::::::::::::
::::::::::::::::

::::::::::::::::::: instructor

 Demonstrate each step live.

 Some learners may never have manually created a text file before.

 Pause between steps to allow learners to follow along.

::::::::::::::::::::::::::

---

## Documentation Beyond The Top Level

Project-level documentation is important, but it is not always sufficient.

Sometimes subfolders require their own documentation.

For example:

```text
results/
```

may contain dozens of generated outputs and sub-folders.

Several months later, somebody might reasonably ask:

- Which software generated these files?
- When were they created?
- Which parameters were used?
- Which version of the data was analysed?
- What is the data access and retention policy of these data?

A README placed inside the results folder can answer these questions.

For example:

```text
results/
│
├── README.txt
├── figures/
└── tables/
```

The README could document:

```text
Generated:
2026-07-01

Analysis Software:
R version 4.6

Input Data:
processed_data_v03.csv

Parameters:
Significance threshold = 0.05
```

This preserves important contextual information.

Alternativly, different versons could have different folders, or be run using different software versions. 

::::::::::: discussion

Consider different projects or subjects and why different folders might need different README files to keep track of the data. 

::::::::::::

---

## Other Useful Documentation

Depending on the project, additional documentation might include:

### Data Dictionaries

These explain variables in tabular datasets.

For example:

| Variable | Description |
|-----------|-------------|
| incidence_rate | Number of cases per 100,000 |
| region | Geographic study area |
| year | Observation year |

We will revisit this when discussing tabular data.

---

### Standard Operating Procedures

These describe how data is collected or processed.

For example:

```text
sampling_protocol.txt
```
Which contains a written description of the procedures used. 

---

### Project Logs

These provide a record of major project decisions.

For example:

```text
project_log.txt
```

This can be particularly useful for long-running projects.


### Parameter files

::::::::::: callout

Parameter files will depend on for project and/or software, but provide a record of inputs into software when processing data. The goal of such documentation is to ensure that your  data processing/analysis steps can be reproduced. These should be documented and referenced where appropriate. 

:::::::::::::::::::::

---

::::::::::::::::: challenge

## Write A README

 Create a `README.txt` file for the inherited project.

 Include:

 - Project name
 - Project description
 - Folder structure
 - Data sources
 - Contact information
 - Last updated date

 You may need to make reasonable assumptions where information is missing.

 The goal is to make the project easier for a future collaborator to understand.

::::::::::::::: solution

 There is no single correct answer.

 A successful README should clearly explain:

 - What the project is
 - What data exists
 - How the folders are organised
 - Who is responsible for the project

 It should allow somebody unfamiliar with the project to begin understanding its contents.

Also, see the Newcastle University [Documentation](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/working/organise/) and Metadata page.


Additional, subject specific suggestions can be found [here](https://www.dcc.ac.uk/guidance/standards/metadata) as well as data centre policies and information produced by funding agencies. 


::::::::::::::::::::
:::::::::::::::::::

## File headers

Depending on the file, data can be stored in file headers or in metadata. A simple example would be to store basic information in the first few lines of a spreadsheet or csv file or as text and tables in other file formats. We will discuss this later in the data formats lesson. 

The advantage of storing information as headers or comments in the files is that they cannot be seperated from the folder structure, such as when communicating with a collegue. It can provide a failsafe is a file becomes seperated from the rest of the project. 

---

:::::::::::::::::: discussion

## Reflection

Imagine you are leaving your current project tomorrow.

What information would a replacement researcher need in order to continue your work?

Is all of that information currently written down somewhere?

::::::::::::::::::::

---

## Looking Ahead

Our project now has:

- A clearer folder structure
- Better file names
- Initial documentation

The next challenge is deciding where data should live.

How can we store data so it is:

- Accessible?
- Backed up?
- Secure?
- Shareable?

In the next episode we will explore how to choose appropriate storage locations for different types of research data.

::::::::::::::::::::::::::::::::::::: keypoints 

## Key Points

- Documentation makes data understandable and reusable.
- Documentation is primarily written for people, including future-you.
- Metadata provides context about a dataset.
- README files are a simple and effective way to document projects.
- A README should explain what the project is, how it is organised, and where the data came from.
- Documentation should be stored close to the data it describes.
- Additional README files can be useful within subfolders such as results or processed data.
- Good documentation reduces confusion and improves collaboration.

::::::::::::::::::::::::::::::::::::::::::::::::