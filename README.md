# Data Management Best Practices

A Carpentries-style lesson introducing practical research data management skills for postgraduate students and researchers.

## Overview

Good data management is essential for efficient, reproducible, and collaborative research. This lesson helps learners develop practical skills for organising, documenting, storing, sharing, and preserving research data.

The lesson is structured around a realistic scenario:

> A researcher inherits a collection of poorly organised files from a collaborator who has left a project and must work out what the data is, how it is organised, and how best to manage it moving forward.

Working from the filesystem level down to the contents of data files, learners will progressively improve a deliberately messy dataset while discussing real-world research data management challenges.

Topics covered include:

- Organising folder structures
- Choosing effective file names
- Creating documentation and metadata
- Selecting appropriate storage locations
- Managing storage and file transfers
- Data retention and archival decisions
- Best practices for tabular data
- Choosing appropriate data formats
- Publishing and sharing research outputs

This lesson is aimed at:

- Postgraduate students
- Early career researchers
- Research support staff
- Anyone responsible for managing research data

No programming experience is required.

---

## Lesson Structure

1. Introduction
2. File Structures
3. File Names
4. Documentation
5. Where to Store Things
6. Storage and Transfer
7. Data Retention and Removal
8. Best Practices for Tabular Data
9. Choosing Data Formats
10. Capstone Exercise

---

## Building the Lesson

This lesson uses the standard **Carpentries Workbench** infrastructure.

See: https://carpentries.github.io/workbench/#installation 

To build and preview the lesson locally you need to have installed R and the Workbench materials (see the above link).
Then you can run:

```bash
R -e 'sandpaper::serve(quiet = FALSE, port = "3435")'
```

---

## Contributing

Contributions are welcome.

Examples of useful contributions include:

- Typographical corrections
- Clarifications and improved explanations
- New exercises or discussion questions
- Additional instructor notes
- Updates to institutional guidance
- Accessibility improvements
- Bug reports

### Reporting Issues

If you spot an error or have a suggestion, please open a GitHub Issue describing:

- The page or episode affected
- The problem identified
- Suggested improvements (if applicable)

### Submitting Changes

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit with a clear commit message.
5. Submit a Pull Request.

For example:

```bash
git checkout -b improve-readme-exercise
```

Please provide a short description of:

- What changed
- Why it was changed
- Any relevant context for reviewers

---

## Style Guidelines

When contributing to the lesson:

- Follow Carpentries lesson design principles.
- Use inclusive and accessible language.
- Prefer practical, research-focused examples.
- Keep exercises relevant to the lesson narrative.
- Include clear learning objectives and key points.
- Use UK English spelling where possible.

---

## Instructor Notes

This lesson is intended to be taught interactively.

Where possible:

- Encourage discussion between learners.
- Use examples from participants' own research workflows.
- Emphasise that consistency is often more important than finding a single "perfect" solution.
- Adapt storage recommendations to local institutional infrastructure where necessary.

---

## Licence

Unless otherwise stated, this lesson is released under the terms of the licence specified by The Carpentries Workbench template used by this repository.

See the repository licence file for details.

---

## Acknowledgements

This lesson was developed using the Carpentries Workbench and draws upon common data management challenges encountered by researchers across disciplines.

Special thanks to all contributors, instructors, helpers, and learners who help improve the lesson over time.

Contibutors:
- Frances Turner, frances.hutchings@ncl.ac.uk
- Carol Booth
- Jannetta Steyn
- Robin Wardle
- Tiago Sousa Garcia
- Kate Court
- David Herbert
- Rebecca Osselton
- Michelle Gilbride
- Owain Snaith



[cff-home]: https://citation-file-format.github.io/
[cff-sandpaper-docs]:  https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable
[cffinit]: https://citation-file-format.github.io/cff-initializer-javascript/
[workbench]: https://carpentries.github.io/sandpaper-docs/
