# ---
# jupyter:
#   jekyll:
#     display_name: Git miscellany
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Git Stash

# %% [markdown]
# Before you can `git pull`, you need to have committed any changes you have made. If you find you want to pull, but you're not ready to commit, you have to temporarily "put aside" your uncommitted changes.
# For this, you can use the `git stash` command, like in the following example:

# %% jupyter={"outputs_hidden": true}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon
* Glyder Fawr
* Fan y Big
* Cadair Idris

# %% jupyter={"outputs_hidden": false} language="bash"
# git stash
# git pull

# %% [markdown]
# By stashing your work first, your repository becomes clean, allowing you to pull. To restore your changes, use `git stash apply`.

# %% jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git stash apply

# %% [markdown]
# The "Stash" is a way of temporarily saving your working area, and can help out in a pinch.

# %% [markdown]
# ## Tagging
#
# Tags are easy to read labels for revisions, and can be used anywhere we would name a commit.
#
# Produce real results *only* with tagged revisions

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git tag -a v1.0 -m "Release 1.0"
# git push origin --delete v1.0  # clear the tag if it already exists on the remote origin
# git push --tags

# %% jupyter={"outputs_hidden": false}
# %%writefile Pennines.md

Mountains In the Pennines
========================

* Cross Fell
* Ingleborough

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Pennines.md
# git commit -m "Add Pennines"

# %% [markdown]
# You can also use tag names in the place of commmit hashes, such as to list the history between particular commits:

# %% jupyter={"outputs_hidden": false} language="bash"
# git log v1.0.. --graph --oneline

# %% [markdown]
# If .. is used without a following commit name, HEAD is assumed.

# %% [markdown]
# ## Working with generated files: gitignore

# %% [markdown]
# We often end up with files that are generated by our program. It is bad practice to keep these in Git; just keep the sources.

# %% [markdown]
# Examples include `.o` and `.x` files for compiled languages, `.pyc` files in Python.

# %% [markdown]
# In our example, we might want to make our .md files into a PDF with pandoc:

# %% jupyter={"outputs_hidden": false}
# %%writefile Makefile

MDS=$(wildcard *.md)
PDFS=$(MDS:.md=.pdf)

default: $(PDFS)

%.pdf: %.md
	pandoc $< -o $@

# %% jupyter={"outputs_hidden": false} language="bash"
# make

# %% [markdown]
# We now have a bunch of output .pdf files corresponding to each Markdown file.

# %% [markdown]
# But we don't want those to show up in git:

# %% jupyter={"outputs_hidden": false} language="bash"
# git status

# %% [markdown]
# Use .gitignore files to tell Git not to pay attention to files with certain paths:

# %% jupyter={"outputs_hidden": false}
# %%writefile .gitignore
*.pdf

# %% jupyter={"outputs_hidden": false} language="bash"
# git status

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Makefile
# git add .gitignore
# git commit -m "Add a makefile and ignore generated files"
# git push

# %% [markdown]
# ## Git clean

# %% [markdown]
# Sometimes you end up creating various files that you do not want to include in version control. An easy way of deleting them (if that is what you want) is the `git clean` command, which will remove the files that git is not tracking.

# %% jupyter={"outputs_hidden": false} language="bash"
# git clean -fX

# %% jupyter={"outputs_hidden": false} language="bash"
# ls

# %% [markdown]
# * With -f: don't prompt
# * with -d: remove directories
# * with -x: Also remote .gitignored files
# * with -X: Only remove .gitignore files

# %% [markdown]
# ## Hunks
#
# ### Git Hunks
#
# A "Hunk" is one git change. This changeset has three hunks:

# %% [markdown] attributes={"classes": [" diff"], "id": ""}
# ```diff
# +import matplotlib
# +import numpy as np
#
#  from matplotlib import pylab
#  from matplotlib.backends.backend_pdf import PdfPages
#
# +def increment_or_add(key,hash,weight=1):
# +       if key not in hash:
# +               hash[key]=0
# +       hash[key]+=weight
# +
#  data_path=os.path.join(os.path.dirname(
#                         os.path.abspath(__file__)),
# -regenerate=False
# +regenerate=True
# ```

# %% [markdown]
# ### Interactive add
#
# `git add` and `git reset` can be used to stage/unstage a whole file,
# but you can use interactive mode to stage by hunk, choosing
# yes or no for each hunk.

# %% [markdown]
# ``` bash
# git add -p myfile.py
# ```

# %% [markdown] attributes={"classes": [" diff"], "id": ""}
# ``` diff
# +import matplotlib
# +import numpy as np
# #Stage this hunk [y,n,a,d,/,j,J,g,e,?]?
# ```

# %% [markdown]
# ## GitHub pages
#
# ### Yaml Frontmatter
#
# GitHub will publish repositories containing markdown as web pages, automatically. 
#
# You'll need to add this content:
#
# > ```
# >    ---
# >    ---
# > ```
#
# A pair of lines with three dashes, to the top of each markdown file. This is how GitHub knows which markdown files to make into web pages.
# [Here's why](https://jekyllrb.com/docs/front-matter/) for the curious. 

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
---
title: Github Pages Example
---
Mountains and Lakes in the UK
===================

Engerland is not very mountainous.
But has some tall hills, and maybe a mountain or two depending on your definition.

# %% jupyter={"outputs_hidden": false} language="bash"
# git add index.md
# git commit -m "Add github pages YAML frontmatter"

# %% [markdown]
# ### The gh-pages branch
#
# GitHub creates github pages when you use a special named branch.
#
# This is best used to create documentation for a program you write, but you can use it for anything.

# %% jupyter={"outputs_hidden": false}
os.chdir(working_dir)

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
#
# git switch -c gh-pages
# git push -uf origin gh-pages

# %% [markdown]
# The first time you do this, GitHub takes a few minutes to generate your pages. 
#
# The website will appear at `http://username.github.io/repositoryname`, for example:
#
# http://UCL.github.io/github-example/

# %% [markdown]
# ### UCL layout for GitHub pages
#
# You can use GitHub pages to make HTML layouts, here's an [example of how to do it](http://github.com/UCL/ucl-github-pages-example), 
# and [how it looks](http://github-pages.ucl.ac.uk/ucl-github-pages-example). We won't go into the detail of this now,
# but after the class, you might want to try this.
