---
title: "Choosing Where to Store Your Data"
teaching: 30
exercises: 15
---

:::::::::::::::::::::::::::::::::::::: questions 

- Where should I store my research data?
- What are the advantages and disadvantages of different storage options?
- How can I make data accessible to collaborators?
- How can I ensure research data is backed up and secure?
- What additional considerations apply to sensitive or restricted data?
- How can I make data accessible when publishing research?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

By the end of this episode, learners will be able to:

- Identify different storage options available for research data.
- Explain the difference between local, network, and cloud storage.
- Evaluate storage locations based on accessibility, backup, security, and sustainability.
- Choose an appropriate storage location for different types of research data.
- Explain why storing research data in personal accounts can create risks.
- Recognise situations where specialist storage solutions may be required.
- Identify options for publishing research outputs and datasets.

::::::::::::::::::::::::::::::::::::::::::::::::

## Where Should I Store My Data?

At this point in the lesson we have:

- Organised our folder structure
- Improved file names
- Added documentation

However, another important question remains:

> Where should this data actually live?

Many researchers begin a project by storing files wherever is most convenient, such as their work laptop, a USB drive, or personal cloud storage. This approach often works initially, but many research projects involve

- Collaborators
- Large datasets
- Sensitive information
- Long-term storage requirements

A storage decision that works for a single person may not scale as the project and team grows. Choosing an appropriate storage location is therefore an important part of good data management.

---

:::::::::::::::::::: challenge

## Where Do You Store Your Data?

 Spend a few minutes discussing your current storage set-up with a partner:

 - Where do you currently store your research data?
 - Why did you choose that location?
 - How do collaborators access it?
 - Are the data backed up?
 - What would happen if your laptop stopped working tomorrow?
 - What would happen if you suddenly left your current project?

Share some of your current solutions and any concerns with the group.

::::::::::::::::::::::::: solution

Researchers often store data on

- Laptop hard drives
- USB drives
- OneDrive
- Google Drive
- Shared network drives
- Institutional storage systems
- HPC storage
- External hard drives

:::::::::::::::::::::::
:::::::::::::::::::::::

:::::::::::::: instructor

 This discussion helps reveal existing practices within the room.

 Learners often have good reasons for their current choices, but may not have considered backup, sharing, governance, or long-term access implications.

::::::::::::::::::::::

---

## What Makes a Good Storage Location?

When deciding where to store data, consider

- Accessibility: the ability of different users to retrieve and use data
- Recoverability: the ability to restore damaged or lost data
- Security: the ability to protect data from unauthorised access or misuse
- Sustainability: the ability to store and access data for long time periods

### Can Other People Access the Data?

Collaborators must be able to find and open the data.

To evaluate data accessibility, consider

- Can all project members access the data?
- Can external collaborators access it?
- Can access be limited to specific people?
- Can access be easily added for new project members and removed for past members?
- When you leave the project, will other people have difficulty accessing the data?

---

### Is the Data Recoverable?

Data storage and data backup require different solutions. Many researchers assume that files on a computer are safe. However -  

 - Computers fail
 - Laptops are stolen
 - Hard drives stop working
 - USB drives are lost
 - Data can be accidentally deleted or incorrectly modified

Good storage solutions should have reliable backup solutions so that lost data is **recoverable**.

:::::::::::: challenge

## Making data recoverable

Discuss features of a good backup system in your groups. 

:::::::::::: solution

Possible features of a good backup system:

- Has regular, automated backups: automation ensures backup versions stay up-to-date; for e.g., backups may be scheduled every night or triggered when you connect to the internet.
- Off-site storage: stores data off-site (e.g., on the cloud or in a different building) to protect against theft or physical damage due to, e.g., fires or floods.
- Accessibility: allows you to easily restore lost data from the backups and find your files.
- Redundancy: maintains multiple copies of your data to protect against accidental deletion.


:::::::::::::
:::::::::::::

---

### Is the Data Secure?

Not all data can be shared openly; data that needs to be kept secure includes

- Personal information (particularly special category data)
- Commercially sensitive information, such as trade secrets
- Confidential research

Storage locations must be appropriate for the sensitivity of the data. We'll discuss these considerations further in the [Personal and Confidential Data](https://newcastlerse.github.io/data-management-carpentry/storing-data.html#personal-and-confidential-data) section.

:::::::::: caution

You have a legal requirement to keep certain types of data safe; failure to do so can have consequences for yourself and your institution. 

In the event of a data breach you are required to take certain actions, such as reporting to your institution. Make sure you know the requirements for your data. 

:::::::::::

---

### Is the Data Storage Sustainable?

To ensure your data storage is sustainable over the lifetime of the project, consider

- Will the storage still exist in five years?
- What happens to the data if a team member leaves?
- Can file ownership be transferred? This ability is particularly important for cloud services.
- Is there enough storage capacity for data growth?
- Is the file format accessible? If the company which makes your software shuts down, will you still be able to access your data?
- Are any ongoing costs for data storage affordable?

---

## Types of Storage

There are many different types of data storage: 

- Local storage
- Personal cloud storage
- Shared network or cloud storage
- Institution storage (e.g., the Research Data Warehouse)

We'll discuss the advantages and disadvantages of each one below.

---

### Local Storage

Local storage refers to files stored directly on a device such as a

- Laptop
- Desktop computer
- External hard drive
- USB drive

:::::::::::::::::: challenge

## Local storage pros and cons

Discuss the advantages and disadvantages of local storage with a partner or group.

:::::::::::::::::: solution

**Advantages**

- Fast access
- Convenient
- Works without internet access
- Good for active work

**Disadvantages**

- Data may only exist in one location
    - Difficult to access off site
    - Difficult to share with colleagues
- Vulnerable to device failure or loss
- Difficult to collaborate
- Difficult to manage project-wide access
- Security issues, e.g., 'left laptop with personal data on a train'

:::::::::::::::::::::::::
:::::::::::::::::::::::::

::::::::::::: callout

Local storage is often useful for temporary working files.

It is not a good long-term storage solution for important project data since it lacks all four desired storage features: accessibility, recoverability, security, and sustainability.

::::::::::::: 

---

### Personal Cloud Storage

Many institutions provide services such as

- OneDrive
- Sharepoint
- Google Drive
- Dropbox

These services can synchronise files between devices and provide data backups.

Newcastle University has guides for using OneDrive and Sharepoint storage: [Link][one_ncl]. As does [Cambridge University][one_cam] or [University of Warwick][one_war].

:::::::::::::::::::: challenge

## Personal cloud storage pros and cons

Discuss the advantages and disadvantages of cloud storage with a partner or group.

:::::::::::::::::::: solution

**Advantages**

- Accessible from multiple devices
- Easy and rapid syncing. OneDrive often works in the background.
- Simple sharing
- Automatic backup in many cases
- Stronger security compared to email
- Version history 
- Easier to share large datasets using links to the data

**Disadvantages**

- Usually linked to an individual account
- Access often disappears when somebody leaves
- Shared permissions must be managed carefully
- Storage may be limited
- Security/Privacy issues
- Data sovereignty issues
- Potentially harder to provide access to external collaborators
- Understanding University policy 
- Knowing which service to use can be challenging
- May fail silently

::::::::::::::::::::
::::::::::::::::::::

::::::::::: caution

Various institutions will have different arrangements and recommendations regarding the use of personal or sensitive data.

For example, Newcastle University recommends against uploading personal or sensitive data to Google Drive and DropBox, see the cloud storage tab at the following [link][dst_ncl]. It suggests OneDrive.

Cambridge University defines four classes of data with different storage recommendations for each [link][dst_cam].

:::::::::::::::

:::::::::::::::::::: callout
#### A Common Research Problem

Many researchers store project data in their personal OneDrive. This approach seems convenient until

- A researcher leaves the project
- A researcher leaves the institution and their institution OneDrive account is removed
- You need to transfer ownership of files

These situations can also result in loss of access to important project data.

In some organisations, governance policies may prevent administrators from accessing a past team member's OneDrive because personal storage is treated as individual, rather than project-owned, data. For this reason, avoid using personal cloud storage as the primary home of important shared project data.

Depending on the cloud service, it can also be challenging to transfer file ownership to another team member.

::::::::::::::::::::

::::::::::::::::: instructor

Adapt this section to local institutional policies.

Learners often assume that "being in the cloud" automatically means data is accessible to everyone who needs it.

::::::::::::::::::::::::

---

### Shared Network or Cloud Storage

Shared storage is designed specifically for collaboration.

Examples include:

- Shared network drives
- Shared project folders
- SharePoint sites
- Departmental storage

:::::::::::::::::::: challenge

## Shared storage pros and cons

Discuss the advantages and disadvantages of shared storage with a partner or group.

::::::::::::::::::::: solution

**Advantages**

- Multiple users can access data
- Permissions can be managed centrally
- Better suited to collaboration
- Less dependent on a single individual

**Disadvantages**

- May require administration
- May have storage limits
- Large datasets can become difficult to manage
- May not have permission to access off-site
- Can be more difficult to understand backup policy (e.g., is something deleted locally also deleted in the shared folder?)

:::::::::::::::::::::
:::::::::::::::::::::

---

### Institution storage

Many institutions provide dedicated research storage services.

At Newcastle University, research projects can use the [Research Data Warehouse (RDW)](https://services.ncl.ac.uk/itservice/core-services/filestore/researchdatawarehouse/).

The RDW is

- Backed up
- Designed for research data
- Accessible to project members
- Shared at the project level
- Suitable for large datasets
- Connected to institutional computing infrastructure

Unlike personal storage, access is linked to the project rather than an individual, which allows

- New collaborators to be added
- Departing collaborators to be removed
- Data to remain available to the project

For most research data, RDW is the recommended storage location.


:::::::::::::::::::::::::::: instructor 

Replace this section with your own institutional storage recommendations if delivering the lesson elsewhere.

::::::::::::::::::::::::::::

---


:::::::::::::: discussion

## Accessing Different Storage Locations

Follow along with the instructor who will demonstrate how to navigate to

- Local storage
- OneDrive (or equivalent cloud storage)
- Shared project storage
- Research Data Warehouse (or institutional research storage)

For each example:

1. Open File Explorer.
2. Navigate to the storage location.
3. Show where files appear.
4. Discuss who can access the data.
5. Discuss backup arrangements.
6. Discuss limitations.

::::::::::::::


---

## Permissions and Collaboration

Choosing a storage location is only the first step for storing research data.

You also need to decide

- Who can read data?
- Who can upload data?
- Who can edit data?
- Who can delete data?

For example, you may need permissions such as

| Role | Permissions |
|--------|--------|
| Project members | Read and write |
| External collaborators | Read only |
| Project lead | Full control |

but the appropriate permissions depend on the project. We recommend creating an access plan so all project members know who can access which data and how to provide access to external or new collaborators. 

::::::::::::::::: callout

Grant the minimum access necessary to reduce the risk of accidentally deleting, leaking, or modifying important data.

Permissions should be regularly reviewed to update access as needed (e.g., to remove access after team members or collaborators leave the project).

::::::::::::::::::::::::::::::::::::::::::::

---

## Personal and Confidential Data

Some projects require additional controls to protect [**personal data**](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/), such as names and and contact information, as well as **confidential data**, such as trade secrets or intellectual property. 

[**Special category data**](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data/), or sensitive data, is personal data that requires additional protection due to its sensitivity - for example, race and ethnic origin, political opinions, religious beliefs, biometric data, and health data.

When working with these types of data, consider

- Is the storage location approved for personal or confidential data?
- Who should have access to the data?
- Does the data need to be encrypted?
- Are there legal or ethical restrictions for using or distributing the data?

Personal and confidential data should never be collected or stored solely because it is convenient. Always follow institutional policies and governance requirements; for example, Newcastle University requires researchers to complete a [Data Protection Impact Assessment](https://www.ncl.ac.uk/research/research-governance/ethics/toolkit/data/) if their research project may involve personal data.

:::::::::::::::::::::: caution

There are strict legal requirements for using and storing certain types of data:

- People can request access to data held on them, via [Subject Access Requests](https://www.gov.uk/government/publications/subject-access-request-procedure/subject-access-request-procedure) 
- People can request erroneous data about them be corrected
- People can request data about them be deleted
- Personal data must be used only for the reasons it was provided
- Data breaches must be reported to the University in line with its policies
- and many others

For more information, see

- [GDPR Information for Research][gdpr]
- [Data Protection][dapr]
- [Access your personal data][aypd]

Ensure you understand your obligations for managing your data.

::::::::::::::::::::::

### Encryption

One way to protect personal and confidential data is **encryption**, which "scrambles" data so that only people with the correct key can access and read the data.

Your institutional laptop may already be running whole disk encryption, which protects all the files on the computer. Without encryption, anyone can access the files, even if you have set a password. However, data on your laptop is only fully protected when the laptop is shut down; different modes of standby have different levels of protection. For example, Hibernate provides more protection than Sleep mode in Windows.  

External hard-drives (often used for backups or data transfer) need to be explicitly encrypted, even if your laptop is encrypted. External disks can be encrypted using Bitlocker in Windows, Finder in macOS, or Disk Utility in Linux. 


:::::::::::::::::::: caution

If you forget your password and encryption key you have lost your data! It cannot be recovered. 

::::::::::::::::::::

The different tools on Windows, macOS, and Linux can make an encrypted external disk or USB key unusable on a different operating system. You can often encrypt individual files and folders if required.

---

:::::::::::::::::: discussion

## Where Should You Store Your Data?

 Consider a current or future research project.

 - Where are you storing data now?
 - Is that the most appropriate location?
 - How is the data backed up?
 - Could collaborators access it?
 - What would happen if you left the institution?

 Would you change your storage solution after today's discussion?

::::::::::::::::::::::::::

---

## Changing Data Storage Location

Storage locations may need to change as projects evolve.

When moving project data

- Inform collaborators
- Update documentation
- Update links, references, and shortcuts
- Update analysis workflows if required

Changing locations can have unintended consequences.

For example:

:::::::::::::::::: tab

## Windows

```text
D:\ProjectData\
```

becoming:

```text
R:\Projects\ProjectData\
```

## macOS

```text
/Users/Claire/ProjectData/
```

becoming:

```text
/data/Projects/ProjectData/
```

## Linux

```text
/home/Claire/ProjectData/
```

becoming:

```text
/data/Projects/ProjectData/
```

::::::::::::::::::::

may break scripts that reference the previous location.

---

## A Brief Note on Version Control

Sometimes researchers use multiple files with descriptive filenames to keep track of changes:

```text
report_v01.docx
report_v02.docx
report_v03.docx
```

For documents and data, this approach can be useful.

However, software projects often use dedicated version control systems such as [Git](https://git-scm.com/).

Version control provides

- History tracking
- Collaboration tools
- Change management
- Recovery of previous versions

Note that some services, such as OneDrive, also retain version histories. 

::::: callout
 We will not cover version control and Git in this workshop, but you can learn more about them by attending a [Carpentries Git and Version Control](https://swcarpentry.github.io/git-novice/) workshop.
:::::

---

## Sharing Research Outputs

Eventually many research projects produce outputs that should be publicly available, such as

- Supporting datasets
- Processed data
- Code
- Supplementary materials

Rather than emailing files or placing them on personal websites, researchers often store these outputs in repositories that are publicly available, such as

- [Zenodo](https://zenodo.org/)
- [Figshare](https://figshare.com/)
- [GitHub](https://github.com/) (particularly for code/software)
- Institutional repositories
- Subject-specific repositories

More repositories can be found at [re3data.org](https://www.re3data.org) and in Newcastle University's [Find Data](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/find/) resource. Note that individual funders may have their own requirements on how research outputs are shared. 

Repositories can provide

- Long-term preservation
- Stable links
- Metadata
- Citations
- [Digital Object Identifiers (DOIs)](https://www.doi.org/)

A DOI allows any type of digital object to be cited in publications, making research outputs such as datasets easier to find, cite, and reuse. Journals create DOIs for research articles as well to provide a stable citation and metadata for each article.

:::::::::::::::::: challenge

## Finding digital objects using DOIs

DOIs can be mapped to their digital objects using a DOI resolver. The resolver looks up the DOI in the DOI registry to find the corresponding record and send you to the location of the digital object.

Use the DOI Foundation's [DOI resolver](https://dx.doi.org/) to find the digital object that corresponds to each of these DOIs:

- 10.5281/zenodo.3960218
- 10.1371/journal.pone.0090081

For each DOI, answer

1) Where is the object stored? 
2) What type of object is it? (e.g., publication, dataset, software)
3) What is the name of the object?
4) Who created/authored the object?
5) When was the object published?
6) How would you cite the object?

:::::::::::::::::: solution

**10.5281/zenodo.3960218**

1) Location: Zenodo (repository)
2) Type: Software (with dataset)
3) Name: allisonhorst/palmerpenguins: v0.1.0
4) Creators: Allison M Horst, Alison Presmanes, Kristen B Gorman
5) Publication date: July 25, 2020
6) Citation: Allison M Horst, Alison Presmanes Hill& Kristen B Gorman. (2020). allisonhorst/palmerpenguins: v0.1.0 (Version v0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.3960218

**10.1371/journal.pone.0090081**

1) Location: PLOS One (journal)
2) Type: Research article
3) Name: Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis)
4) Creators: Kristen B. Gorman, Tony D. Williams, William R. Fraser
5) Publication date: March 5, 2014
6) Citation: Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. https://doi.org/10.1371/journal.pone.0090081

::::::::::::::::::
::::::::::::::::::

---

:::::::::::::::::::::::: challenge

## Matching Data to Storage


For each scenario, identify the most appropriate storage location and explain your reasoning.

 1. Active analysis files that only you are currently editing.
 2. A shared project involving five collaborators.
 3. Large datasets processed on the HPC.
 4. Personal identifiable information.
 5. Published research outputs accompanying a journal article.

 Discuss your answers with a partner.

:::::::::::::::::: solution

 Example answers:

 1. Local working copy with institutional backup.
 2. Shared project storage or Research Data Warehouse.
 3. Research Data Warehouse connected to HPC resources.
 4. Approved secure institutional storage.
 5. Public repository such as Zenodo or an institutional repository.

 The key consideration is matching storage decisions to requirements around access, backup, scale, and security.

::::::::::::::::::
::::::::::::::::::


---

## University Data Management Plan

Newcastle University has various templates for planning your data management aimed at PGRs. These can be found [here](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/pgr/). There are slightly different templates for the Faculty of Science, Agriculture and Engineering, the Faculty of Humanities and Social Sciences and the Faculty of Medical Sciences, but all follow the same general form .e.g. 

- Type of study (3 lines).
- Existing data study.
- Data types.
- Format and scale of your data.
- Data collection/production methodology.
- Data quality and standards.
- Data management, storage and curation.
- Metadata and documentation.
- Data security risks.

The university has guides and training specifically to help with your data management plan [here](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/dmponline/). 

This is the University plan, your funding agencies may have their own standards and requirements.  

---

## Data Privacy Impact Assessment

If your research project involves personal or sensitive data, or could potentially, a Data Protection Impact Assessment should be completed and registered with the University's Information Governance Team. This is outlined [here](https://www.ncl.ac.uk/research/research-governance/ethics/toolkit/data/). The assessment documenation includes a number of screening questions to help decide which sections you need to fill in. 


---



## Looking Ahead

We now know where research data should be stored.

The next challenge is dealing with situations where data is challenging to store or share.

In the next episode we will discuss

- Storage limits
- Compression
- File transfer
- Storage efficiency
- Reducing duplication

::::::::::::::::::::::::::::::::::::: keypoints 

- Storage decisions should consider accessibility, recoverability, security, and sustainability.
- Local storage is convenient for active work, but is rarely meets other storage requirements.
- Personal cloud storage can create access problems when researchers leave projects.
- Shared project storage is generally preferable to individual-owned storage.
- Research data should ideally be stored in project-owned, backed-up systems.
- Permissions should be managed carefully and reviewed regularly.
- Personal and confidential data may require additional controls and approved storage locations.
- Updating data locations can affect collaborators and workflows.
- Repositories such as Zenodo can make research outputs more discoverable and citable.
- Version control is important for managing changes and is covered in dedicated Carpentries Git workshops.

::::::::::::::::::::::::::::::::::::::::::::::::

[dpi_ncl]: https://www.ncl.ac.uk/research/research-governance/ethics/toolkit/data/
[dpi_imp]: https://www.ncl.ac.uk/research/research-governance/ethics/toolkit/data/
[dmp_cam]: https://www.data.cam.ac.uk/planning-support/data-management-plans
[dmp_dur]: https://libguides.durham.ac.uk/open_research/dmp
[dmp_lee]: https://students.leeds.ac.uk/postgraduate-research-practice/doc/data-management-plans 
[dmp_new]: https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/dmponline/
[dmp_sur]: https://www.surrey.ac.uk/library/open-research/data-management-plans
[dr_re3]: https://www.re3data.org
[dr_ncl]: https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/find/
[bbc]: https://www.bbc.co.uk/news/articles/c363w8pjpklo
[sec_oxf]: https://www.infosec.ox.ac.uk/stay-safe-on-email#tab-457621
[sec_hex]: https://hexiosec.com/blog/secure-email-attachments/
[ftt_gla]: https://transfer.gla.ac.uk
[fft_her]: https://exchangefile.herts.ac.uk
[ftt_ncl]: https://dropoff.ncl.ac.uk/
[fft_sur]: https://dropoff.surrey.ac.uk 
[sar_ico]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/subject-access-requests/a-guide-to-subject-access/
[dst_ncl]: https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/working/
[dst_cam]: https://www.data.cam.ac.uk/organising-storing/storage-backup
[one_ncl]: https://newcastle.sharepoint.com/sites/O365 
[one_cam]https://help.uis.cam.ac.uk/system/files/managing_and_sharing_files_in_onedrive_and_sharepoint_-_learner_-_december_2025.pdf  
[one_war]: https://warwick.ac.uk/services/idg/learning-resources/knowledge/guide-to-onedrive/
[gdpr]: https://www.ncl.ac.uk/research/research-governance/ethics/gdpr/
[dapr]: https://www.ncl.ac.uk/data-protection/
[aypd]: https://www.ncl.ac.uk/data-protection/access-personal-data/