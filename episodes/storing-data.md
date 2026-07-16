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

# The Problem: Where Should I Store My Data?

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

# Discussion: Where Do You Store Your Data?

:::::::::::::::::::::::::::::::::::::::::::::: discussion

 Spend a few minutes discussing the following questions with a partner:

 - Where do you currently store your research data?
 - Why did you choose that location?
 - How do collaborators access it?
 - Is it backed up?
 - What would happen if your laptop stopped working tomorrow?

 Be prepared to share some examples with the group.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

After a few minutes, gather responses.

Common answers often include:

- Laptop hard drives
- USB drives
- OneDrive
- Google Drive
- Shared network drives
- Institutional storage systems
- HPC storage
- External hard drives

> ## Instructor Note
>
> This discussion helps reveal existing practices within the room.
>
> Learners often have good reasons for their current choices, but may not have considered backup, sharing, governance, or long-term access implications.

---

# What Makes a Good Storage Location?

When deciding where to store data, it is useful to consider four broad questions:

## Can People Access It?

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

Computers fail.

Laptops get stolen.

Hard drives stop working.

Good storage solutions should have reliable backup arrangements.

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

---

## Is It Sustainable?

Consider the lifetime of the project.

Ask:

- Will the storage still exist in five years?
- What happens if a team member leaves?
- Can ownership be transferred?
- Is there enough capacity for data growth?

---

# Local Storage

Local storage refers to files stored directly on a device such as:

- Laptop
- Desktop computer
- External hard drive
- USB drive

For example:

```text
C:\Users\Bob\Documents\Research\
```

## Advantages

- Fast access
- Convenient
- Works without internet access
- Good for active work

## Disadvantages

- Data may only exist in one location
- Vulnerable to device failure
- Difficult to collaborate
- Difficult to manage project-wide access

:::::::::::::::::::::::::::::::::::::::: callout

Local storage is often useful for temporary working files.

It is rarely an ideal long-term location for important project data.

:::::::::::::::::::::::::::::::::::::::::::::::::

---

# Personal Cloud Storage

Many institutions provide services such as:

- OneDrive
- Google Drive
- Dropbox

These can synchronise files between devices and provide backup capabilities.

For example:

```text
OneDrive/
└── Research Project/
```

## Advantages

- Accessible from multiple devices
- Easy syncing
- Simple sharing
- Automatic backup in many cases

## Disadvantages

- Usually linked to an individual account
- Access often disappears when somebody leaves
- Shared permissions must be managed carefully
- Storage quotas may be limited

## A Common Research Problem

Many researchers store project data in their personal OneDrive.

This seems convenient until:

- A researcher leaves the project
- Their institutional account is removed
- Access to project data is lost

In some organisations, governance policies may prevent administrators from granting access because personal storage is treated as individual rather than project-owned data.

For this reason, personal cloud storage should generally not be considered the primary home of important shared project data.

> ## Instructor Note
>
> Adapt this section to local institutional policies.
>
> Learners often assume that "being in the cloud" automatically means data is accessible to everyone who needs it.

---

# Shared Storage

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

## Advantages

- Multiple users can access data
- Permissions can be managed centrally
- Better suited to collaboration
- Less dependent on a single individual

## Disadvantages

- May require administration
- May have storage limits
- Large datasets can become difficult to manage

---

# Research Data Warehouse Storage

Many institutions provide dedicated research storage services.

At our institution, research projects can use the Research Data Warehouse (RDW).

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

> ## Instructor Note
>
> Replace this section with your own institutional storage recommendations if delivering the lesson elsewhere.

---

# Demonstration: Accessing Different Storage Locations

The instructor should demonstrate navigating to:

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

Encourage learners to follow along where possible.

---

# Permissions and Collaboration

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

:::::::::::::::::::::::::::::::::: Callout
>
> Grant the minimum access necessary.
>
> This reduces the risk of accidental deletion or modification of important files.

::::::::::::::::::::::::::::::::::::::::::::

---

# Sensitive Data

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

---

# Changing Data Locations

Eventually projects evolve.

Storage locations sometimes need to change.

When moving project data:

- Inform collaborators
- Update documentation
- Update links and shortcuts
- Update analysis workflows if required

Changing locations can have unintended consequences.

For example:

```text
D:\ProjectData\
```

becoming:

```text
R:\Projects\ProjectData\
```

may break scripts that assume the old location.

This is one reason why good documentation is important.

---

# A Brief Note on Version Control

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

> ## Further Learning
>
> If you want to learn more about version control, consider attending a Carpentries Git and Version Control workshop.
>
> This lesson will not cover Git in detail.

---

# Sharing Research Outputs

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

---

# Discussion: Where Should You Store Your Data?

:::::::::::::::::::::::::::::::::::::::::: discussion
>
> Consider a current or future project.
>
> - Where are you storing data now?
> - Is that the most appropriate location?
> - How is the data backed up?
> - Could collaborators access it?
> - What would happen if you left the institution?
>
> Would you change anything after today's discussion?

::::::::::::::::::::::::::::::::::::::::::::::::::::

---

:::::::::::::::::::::::::::::::::::::::::::::: challenge
Matching Data to Storage


>
> For each scenario, identify the most appropriate storage location and explain your reasoning.
>
> 1. Active analysis files that only you are currently editing.
> 2. A shared project involving five collaborators.
> 3. Large datasets processed on the HPC.
> 4. Human participant data.
> 5. Published research outputs accompanying a journal article.
>
> Discuss your answers with a partner.

:::::::::::::::::::::::::: solution


>
> Example answers:
>
> 1. Local working copy with institutional backup.
> 2. Shared project storage or Research Data Warehouse.
> 3. Research Data Warehouse connected to HPC resources.
> 4. Approved secure institutional storage.
> 5. Public repository such as Zenodo or an institutional repository.
>
> The key consideration is matching storage decisions to requirements around access, backup, scale, and security.

:::::::::::::::::::::::: 

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

---

# Looking Ahead

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