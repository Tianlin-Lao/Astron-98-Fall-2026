# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a version control system, github is its web platform to host git repositories, and git bash is its terminal

# 2) What’s the difference between the terminal and the command line?
# Terminal is where you interact with your computer with commands, and command line is its text-based interface like >>>

# 3) How does Windows PowerShell differ from Git Bash?
# In case of git we can use both ones, but Windows PowerShell is the terminal native to windows while git bash is native to git, so there could be some differences

# 4) What’s the difference between Anaconda, conda, and Python?
# Python is a programming language, conda mangaes python packages, and Anaconda is a packege distribution pack that allows you to install a lot of packeges at once

# 5) What is VS Code? 
# A developing environment (a.k.a text editor) that makes it convenient to edit code in Python

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# An environment like VS code but is browser-based and uses many code cells, while Jupyter Lab adds onto it like you can use multiple notebooks, files and terminals

# 7) What does ~/ mean?
# current home directory in unix

# 8) What’s the difference between an absolute path and a relative path?
# Relative path depends on the current working directory, while absolute path can be used regardless the current working directory.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute: :/d/python_decal_fa26/course_assignments/homework2  Relative: ../course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# remove the current directory (but can a directory be removed like this?)

# 12) What do the following commands do?
# git add   state files that will be added in the next commit
# git commit    save the specified files as a new commit in local Git with a message
# git push  uploads local commits to a remote one

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . adds all the file in the current directory, while git add <file> only adds in one file

# 14) What do "git status" and "git log -1" do?
# git status shows the current working directory status like which file changed, which branch are we on. git log -1 only shows the most recent (1) commit

# 15) What’s the difference between cloning a repository and pulling from it?
# cloning allows you to copy a new repository to get everything from it, while pull only pulls the new commits changed since last pull and requires repository existing

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# unlike python many commands on the terminal are very hard to memorize...

# 17) What’s a question you still have? What’s something you’re confused about?
# Appearently the working directory format changes between windows and unix? 

# 18) Tell me a fun fact!
# rm do not use recycle bin so be careful!

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
x = 5
x = x + 5
print(x == x + 5) # False, but these lines frustrates a mathematican!
