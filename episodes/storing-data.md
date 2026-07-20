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

Many researchers begin a project by storing files wherever is most convenient:

- On their laptop
- In Downloads
- On a USB drive
- In personal cloud storage

This often works initially.

However, research projects usually involve:

- Collaborators
- Large datasets
- Sensitive information
- Long-term storage requirements

A storage decision that works for a single person may become problematic when a project grows or team members change.

Choosing an appropriate storage location is therefore an important part of good data management.

---

:::::::::::::::::::: challenge

## Where Do You Store Your Data?

 Spend a few minutes discussing the following questions with a partner:

 - Where do you currently store your research data?
 - Why did you choose that location?
 - How do collaborators access it?
 - Is it backed up?
 - What would happen if your laptop stopped working tomorrow?

Share some of your examples with the group.

::::::::::::::::::::::::: solution

Common answers often include:

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

When deciding where to store data, it is useful to consider four broad questions:

- Access.
- Backups.
- Security.
- Sustainability. 

### Can People Access It?

If collaborators need access, they must be able to find and open the data.

Questions to consider:

- Can project members access it?
- Can external collaborators access it?
- Can access be controlled?
- Can new project members be added easily?

---

## Is It Backed Up?

Storage and backup are not the same thing.

Many researchers assume:

> "My files exist on a computer, therefore they are safe."

Unfortunately this is not always true.

 - Computers fail.
 - Laptops get stolen.
 - Hard drives stop working.
 - Accidental data deletion.

Good storage solutions should have reliable backup arrangements.

:::::::::::: challenge

Discuss what are the good characteristics of a backup system in your groups. 

:::::::::::: solution

A good backup system might include:

- Regular backups - overnight, when connected to the internet etc.
- Offsite - cloud backups? In a different building.
- Accessible - you can easily go and get the backups and find your files
- Redundancy - Multiple copies, in case you delete data and take a while to notice
- ...

:::::::::::::
:::::::::::::

---

## Is It Secure?

Not all data can be shared openly.

Examples include:

- Participant data
- Medical records
- Personal information
- Commercially sensitive information
- Confidential research

Storage locations must be appropriate for the sensitivity of the data. 

:::::::::: caution

You have a legal requirement to keep certain types of data safe with consequences for yourself and the University. 

There are required actions that need to be taken if there is a data breach, such as reporting to the University. Make sure you know the requirements for your data. 

:::::::::::

---

## Is It Sustainable?

Consider the lifetime of the project.

Ask:

- Will the storage still exist in five years?
- What happens if a team member leaves?
- Can ownership be transferred?
- Is there enough capacity for data growth?
- Is the file format accessible? If the company which makes your software shuts down will you still be able to access your data?

---

## Local Storage

Local storage refers to files stored directly on a device such as:

- Laptop
- Desktop computer
- External hard drive
- USB drive

For example:

:::::::::: tab

### Windows

```text
C:\Users\Bob\Documents\Research\
```

### MacOS

```text
/Users/Bob/Documents/Research/
```

### Linux

```text
/home/Bob/Documents/Research/
```
::::::::::::::::::::::::

:::::::::::::::::: challenge

Discuss the advantages and disadvantages of local storage with a partner or group.

:::::::::::::::::: solution

Examples include

## Advantages

- Fast access
- Convenient
- Works without internet access
- Good for active work

## Disadvantages

- Data may only exist in one location
    - Hard to access off site
    - Hard to share with collegues
- Vulnerable to device failure or loss
- Difficult to collaborate
- Difficult to manage project-wide access
- Security issues e.g. 'left laptop on a train'

:::::::::::::::::::::::::
:::::::::::::::::::::::::

::::::::::::: callout

Local storage is often useful for temporary working files.

It is rarely an ideal long-term location for important project data.

::::::::::::: 


---

## Personal Cloud Storage

Many institutions provide services such as:

- OneDrive
- Sharepoint
- Google Drive
- Dropbox

These can synchronise files between devices and provide backup capabilities.

For example:

```text
OneDrive/
└── Research Project/
```

Newcastle University has guides for using OneDrive and Sharepoint storage: [Link](https://newcastle.sharepoint.com/sites/O365). 

:::::::::::::::::::: challenge

Discuss the advantages and disadvantages of cloud storage with a partner or group.

:::::::::::::::::::: solution

## Advantages

- Accessible from multiple devices
- Easy and rapid syncing. OneDrive often works in the background.
- Simple sharing
- Automatic backup in many cases
- Strong Security compared to email
- Version history 
- You do not need to send data, you can send a link to the data

## Disadvantages

- Usually linked to an individual account
- Access often disappears when somebody leaves
- Shared permissions must be managed carefully
- Storage quotas may be limited
- Security/Privacy issues
- Data sovereignty issues
- Access to external collaborators
- Understanding University policy 
- Knowing which service to use can be challenging

::::::::::::::::::::
::::::::::::::::::::

::::::::::: caution

The University also recommends against uploading personal or sensitive data to Google Drive and DropBox, see the cloud storage tab at the following [link](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/working/). It suggests OneDrive.

:::::::::::::::


## A Common Research Problem

Many researchers store project data in their personal OneDrive.

This seems convenient until:

- A researcher leaves the project.
- Their institutional account is removed.
- Access to project data is lost.

In some organisations, governance policies may prevent administrators from granting access because personal storage is treated as individual rather than project-owned data.

For this reason, personal cloud storage should generally not be considered the primary home of important shared project data.

Depending on the cloud service, it can be hard to transfer ownership of files to another group member. 


::::::::::::::::: instructor

Adapt this section to local institutional policies.

Learners often assume that "being in the cloud" automatically means data is accessible to everyone who needs it.

::::::::::::::::::::::::

---

## Shared Storage

Shared storage is designed specifically for collaboration.

Examples include:

- Shared network drives
- Shared project folders
- SharePoint sites
- Departmental storage

Example:
```text
Shared Projects/
└── Marine Mammal Study/
```

:::::::::::::::::::: challenge

Discuss the advantages and disadvantages of shared storage with a partner or group.

::::::::::::::::::::: solution

## Advantages

- Multiple users can access data
- Permissions can be managed centrally
- Better suited to collaboration
- Less dependent on a single individual

## Disadvantages

- May require administration
- May have storage limits
- Large datasets can become difficult to manage
- Different ways of accessing off-site
- Understanding backup policy can be hard, is something apparently deleted actually deleted?

:::::::::::::::::::::
:::::::::::::::::::::

---

## Research Data Warehouse Storage

Many institutions provide dedicated research storage services.

At our institution, research projects can use the Research Data Warehouse (RDW) [link](https://services.ncl.ac.uk/itservice/core-services/filestore/researchdatawarehouse/).

The RDW is:

- Backed up
- Designed for research data
- Accessible to project members
- Shared at the project level
- Suitable for large datasets
- Connected to institutional computing infrastructure

Unlike personal storage, access is linked to the project rather than an individual.

This means:

- New collaborators can be added
- Departing collaborators can be removed
- Data remains available to the project

For most research data, this is the recommended storage location.


:::::::::::::::::::::::::::: instructor 

Replace this section with your own institutional storage recommendations if delivering the lesson elsewhere.

::::::::::::::::::::::::::::

---


:::::::::::::: challenge

## Accessing Different Storage Locations

Follow along with the instructor who will demonstrate how to navigate to:

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

Choosing a location is only part of the problem.

You also need to decide:

- Who can read data?
- Who can upload data?
- Who can edit data?
- Who can delete data?

For example:

| Role | Permissions |
|--------|--------|
| Project members | Read and write |
| External collaborators | Read only |
| Project lead | Full control |

There is no universal solution.

The appropriate permissions depend on the project.

::::::::::::::::: callout

Grant the minimum access necessary.

This reduces the risk of accidental deletion or modification of important files.

:::::::::::::::::

---

## Sensitive Data

Some projects require additional controls.

Examples include:

- Human participant data
- Clinical data
- Personal information
- Commercially restricted data

Questions to consider:

- Is the storage location approved for sensitive data?
- Who should have access?
- Does the data need encryption?
- Are there legal or ethical restrictions?

Sensitive data should never be stored solely because it is convenient.

Always follow institutional policies and governance requirements.

:::::::::::::::::::::: caution

There are strict legal requirements for using and storing certain types of data. 

- People can request access to data held on them, via [Subject Access Requests](https://www.ncl.ac.uk/mediav8/data-protection/files/SubjectAccessRequestform_002%20(1).docx) 
- People can request erroneous data about them be corrected
- People can demand data about them be deleted
- Personal data must be used only for the reasons it was provided
- Data breaches must be reported to the Univerity in line with its policies
- and many others

See the following examples:

- [GDPR Information for Research](https://www.ncl.ac.uk/research/research-governance/ethics/gdpr/)
- [Data Protection](https://www.ncl.ac.uk/data-protection/)
- [Access your personal data](ttps://www.ncl.ac.uk/data-protection/access-personal-data/)

Be clear on what your obligations are regarding the data you use. The above links are not meant to be definative, you will need to check this yourself. 

::::::::::::::::::::::


### Protecing Your Data


#### Encryption

Your University laptop may already be running whole disk encryption. This protects all the files on the computer. Without it, anyone can access the files, even if you have set a password. However, data on your laptop is only fully protected when it is shut down. Prefer Hibernate to Sleep in Windows.  

The same does not always apply to external hard-drives used for backups or data transfer unless the disk is explicitly encrypted. If the external drive asks for a password before you can access it, it is probably encrypted, if it does not then it probably isn't. External disks can be encrypted using Bitlocker for Windows, Finder for MacOS or Disk Utility in Linux. 


:::::::::::::::::::: caution

If you forget your password and/or encryption key you have lost your data! It cannot be recovered. 

::::::::::::::::::::

The different tools on Windows, MacOS and Linux can make an encrypted external disk or USB key unusable on a different operating system. You can encrypt individual files and folders if required, depending on software and system e.g. Windows/MacOS/Linux/OneDrive.




#### Sharing data

> Maybe move this to the sharing data md. 

Sharing data is discussed in a previous lesson. However, a few additional items related to security are discussed here. 

If concerned about storing data on the cloud, or transfering it to collegues you can encrypt it before hand and sent the encrypted version, while sending the password to the file seperatly. 

The University offers a [File Transfer Service](https://dropoff.ncl.ac.uk/) which offers the chance to encrypt data before sending. It will also inform you when someone accesses the data. 

This offers additional security over email, which is **not recommended** for moving private data. Email passed from you to the destination through a number of intermediate servers. If any link in the chain is exposed, the data can leak. This is why companies rarely email you your bills, but instead offer secure websites for viewing them [1](https://www.infosec.ox.ac.uk/stay-safe-on-email#tab-457621), [2](https://hexiosec.com/blog/secure-email-attachments/). 

Using OneDrive and Sharepoint to transfer files is an alternative to sending the data as a copy. If you send data as an email or via the File Transfer Service, you are making a copy and sending that out into the world. Using University OneDrive or Sharepoint only sends a link. If an email is sent in error you need only break the link or revoke permissions and the data becomes inassessible. This is a good way of reducing errors such as sending to the wrong email address or attaching the wrong document, [for example](https://www.bbc.co.uk/news/articles/c363w8pjpklo). 





#### Sanitising your data

When moving data you need to ensure you are only sending the data you intend. This includes your data, metadata, documentation, file headers etc.  

Data security laws require the removal of personally identifiable information, such that a person is not identifiable using the data *in combination with* other data. This means that even if you cannot identify someone using your data you must also make sure that an individual cannot be identified if someone combines your data with some other data. 

This is a reason good data management is important, you need to be able to track any private data in order to make sure it is not exposed and make sure all of it is removed. 

Software auto-generates metadata, such as name of creator, date created, name of last modifier, date and time of last modification, organisation, and more depending on the software. Ensure that only the data you want is transmitted and be aware of inadvertant meta-data. 



---

## Changing Data Locations

Eventually projects evolve.

Storage locations sometimes need to change.

When moving project data:

- Inform collaborators
- Update documentation
- Update links and shortcuts
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

## MacOS

```text
/Users/Clair/ProjectData/
```

becoming:

```text
/data/Projects/ProjectData/
```

## Linux

```text
/home/Clair/ProjectData/
```

becoming:

```text
/data/Projects/ProjectData/
``

::::::::::::::::::::


may break scripts that assume the old location.

This is one reason why good documentation is important.

---

## A Brief Note on Version Control

Sometimes researchers use filenames to keep track of changes:

```text
report_v01.docx
report_v02.docx
report_v03.docx
```

For documents and data this can be useful.

However, software projects often use dedicated version control systems such as Git.

Version control provides:

- History tracking
- Collaboration tools
- Change management
- Recovery of previous versions

Version control is a large topic in its own right.

Note that some services, such as OneDrive retain their own version histories. 

### Further Learning

 If you want to learn more about version control, consider attending a Carpentries Git and Version Control workshop.

 This lesson will not cover Git in detail.

---

## Sharing Research Outputs

Eventually many research projects produce outputs that should be publicly available.

Examples include:

- Supporting datasets
- Processed data
- Code
- Supplementary materials

Rather than emailing files or placing them on personal websites, researchers often use repositories.

Examples include:

- Zenodo
- Figshare
- Institutional repositories
- Subject-specific repositories

These repositories can provide:

- Long-term preservation
- Stable links
- Metadata
- Citations
- Digital Object Identifiers (DOIs)

A DOI allows a dataset to be referenced in publications in the same way that journal articles are cited.

For example:

```text
doi.org/xxxxx
```

This makes research outputs easier to find, cite, and reuse.

The University provides the following information page [Find Data](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/find/) but individual funders may have their own requirements. [re3data.org](https://www.re3data.org) can also find data repositories. 


---

:::::::::::::::::: discussion

## Where Should You Store Your Data?

 Consider a current or future project.

 - Where are you storing data now?
 - Is that the most appropriate location?
 - How is the data backed up?
 - Could collaborators access it?
 - What would happen if you left the institution?

 Would you change anything after today's discussion?

::::::::::::::::::::::::::

---

:::::::::::::::::::::::: challenge

## Matching Data to Storage


For each scenario, identify the most appropriate storage location and explain your reasoning.

 1. Active analysis files that only you are currently editing.
 2. A shared project involving five collaborators.
 3. Large datasets processed on the HPC.
 4. Human participant data.
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

The university has guides and training spesifically to help with your data management plan [here](https://www.ncl.ac.uk/library/academics-and-researchers/lrs/rdm/planning/dmponline/). 

This is the University plan, your funding agencies may have their own standards and requirements.  

---

## Data Privacy Impact Assessment

If your research project involves personal or sensitive data, or could potentially, a Data Protection Impact Assessment should be completed and registered with the University's Information Governance Team. This is outlined [here](https://www.ncl.ac.uk/research/research-governance/ethics/toolkit/data/). The assessment documenation includes a number of screening questions to help decide which sections you need to fill in. 

---



## Looking Ahead

We now know where data should live.

The next challenge is dealing with situations where data is becoming difficult to store or share.

In the next episode we will discuss:

- Compression
- File transfer
- Storage efficiency
- Reducing duplication

and explore what to do when projects begin running out of space.

::::::::::::::::::::::::::::::::::::: keypoints 

- Storage decisions should consider accessibility, backup, security, and sustainability.
- Local storage is useful for active work but is rarely sufficient on its own.
- Personal cloud storage can create problems when researchers leave projects.
- Shared project storage is generally preferable to individual-owned storage.
- Research data should ideally be stored in project-owned, backed-up systems.
- Permissions should be managed carefully and reviewed regularly.
- Sensitive data may require additional controls and approved storage locations.
- Moving data locations can affect collaborators and workflows.
- Repositories such as Zenodo can make research outputs more discoverable and citable.
- Version control is important for managing changes and is covered in dedicated Carpentries Git workshops.

::::::::::::::::::::::::::::::::::::::::::::::::