---
title: "Choosing the right file structures"
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

# Episode 1: File Structures

## Where should I put this file?
The first thing to think about is what folders you are going to use. The goal here is that when you save a file you know exactly where it should logically go. When you next need to find that file, you can go striaght there instead of having to look around for it. 

Some tips:
* Aim for a shallow folder structure, you don't want to be having to click through 8 folders to get to a file. Something like 3 or 4 levels is probably deep enough.
* You might want to have a 'Inbox' and 'Archive' folder. Inbox can be used for temporary files or downloads that you delete at the end of each week. Archive can hold folders that you are not actively using, but are not ready to delete yet. This will help keep your actively used folders most accessible. 
* You can also 'favourite' your most use folders. On Mac, you can drag a folder to the Favourites section on the left hand side of the Finder window. On Windows you can right click on a folder and select 'Pin to Quick access'. On Linux you cab drag and drop a folder to the Bookmarks section. 

## What is this file?
Your goal is here is to know what a file is without having to open it. Most of these tips apply to naming folders too!

Some tips:
* Choose a format and stick to it. It's probably helpful to make a note of this somewhere, perhaps in a file called 'README' at the top level folder for a specific project. For example, `[Date]\_[sample number]\_[location]_[version]`. Keep filenames as brief as possible.
* Avoid spaces. If you start referring to files programmatically, process them through software or move them through the command line, it may cause you (or others using different operating system environments) a headache to have spaces in your filenames. Instead of spaces, you could use underscores (_), hyphens (-) or camel case (CapitaliseEachWord). Decide on what you will use and stick to it. 
* Also steer clear of special symbols as these can have other meanings in some contexts, or on other operating systems (\/:*?"<>|")
* Don't start with an asterisk (*) as this creates a hidden file that will not appear by default in your file explorer or finder window.
* Also steer clear of starting a filename with '.' as some operating systems such as Linux will interpret this as a hidden file which may puzzle others when it fails to appear.
* Choose a format for dates and, again, stick to it. Given that files are, by default, sorted alphanumerically, if you use this format `YYYY-MM-DD` your files will be organised chronologically. Be aware that files from other sources might use different date conventions, e.g. reversing month and day.

## Which files is this?
There are various approaches to version control. You might have heard of git which is universally used for code. If you are using naming conventions to distinguish between different versions of files, the permise is similar to above, choose a convention, write it, and stick to it.
In some applications, such as Geographic Information Systems, a working set of data is spread across potentially many files; in such cases it might be worth using a folder naming convention to indicate a consistent version of a set of files.

Some tips:
* Use the 'v-syntax' or semantic versioning. For example at the end of the filename at `_v1`, then `_v2` and so on (or `_v01` if you expect to have more than 9 versions). If you would like to be more granular, use semantic version, where you use 3 numbers seperated by full stops to stand for Major version, minor version and patch (small update). So, your first version might be `_1.0.0`, a small update might be `_1.0.1`. You might then do a manjor update and move to `_2.0.0`.
* Avoid using dates or initials to signify different versions as this makes it hard to see at a glance which is the most recent, and leaves you in a pickle if you want to save two versions in the same day.
* Avoid `FINAL` or `latest` in a filename. What happens when you find yourself unexpectedly editing your 'final' version?

