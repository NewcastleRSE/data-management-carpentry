---
title: "Storing your data well"
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


# Where to store things (some ideas - pretty unstructured as I think of them)

## Filesystems and permissions

Unless your data is something you will be working on exclusively (e.g. on your own laptop), it is worth spending some time deciding where on your data will be stored.  The chances are that you will be
working with colleagues, either within your own institution or externally.  

In such cases where you need to share data, it's essential to ensure:

* You choose a place within your available filesystems that is visible to all partners internal and external.
* That all partners have the correct filesystem permissions to do what they need to do (at least read the data, for example).
* Decide which colleagues should be granted permission to write/update data, and potentially delete it.
* You stick to what you originally decided; if you need to change data locations, be aware of who will need to know about the updates - any code or scripts relying on particular locations within a 
filesystem will break and may result in data loss.
* You communicate your conventions clearly to collaborators, and write code/scripts flexibly (so don't for example hard-code filesystem paths in several places within code - this can lead to poor 
maintainability when you miss or mistype one occurrence).


