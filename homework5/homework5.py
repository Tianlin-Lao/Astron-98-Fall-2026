# 2.1
# Git and Github: Git is the version managing tool to track your code and edit history, while Github is the online platform to store Git
# Command line is the text-based interface to type commands to computer, and terminal is the software hosting command line
# Local repository is the repository based on your computer, while remote repository is based on a cloud server
# Version control lets you track your updates, work history and collaborate with other people
# Staging area is between working directory and local repository, a place to keep draft works.
# git add: move changes from working directory to staging area
# git commit: take everything from the staging area and add to local repository, and leave this as a version
# git push: upload local commits to a remote repository
# git status: show the current branch you are working on
# git pull: download new changes from the remote repository
# pwd: print working directory
# ls: display content in working directory
# cd: change working directory
# nano: create or edit a file
# touch: create new, empty file
# mv: move or rename files
# rm: remove files with no confirmation
# cat: read, display or combine files from command line

# 2.2
# pwd
# ls
# cd; git pull
# mv ../brianna_repo/homework.py ./homework
# cd homework
# nano homework.py
# git add git commit git push origin main
# there are new changes on the remote repository that is not in the local repo. 
# To fix, use git pull first, merge the change, then normal procedure for push again
# cd ~/Recent

# 3.1
def checkDataType(d):
    return str(type(d))[7:][:-1]

# 3.2
def evenOrOdd(x):
    if x%2==0:
        return 'Even'
    else:
        return 'Odd'

# 4
def sumWithLoop(l):
    ans = 0
    for i in l:
        ans += i
    return ans

# 5.1
def duplicateList(l):
    ans = []
    for i in l:
        ans.append(i)
        ans.append(i)
    return ans

#5.2 
'''
def square(num)
    return num * num

    def square(num)
                   ^
SyntaxError: expected ':'
'''
def square(num): # add a ':'
    return num * num

# 6.2
ls = [1, 2.1, 'a', True]
print(duplicateList(ls))
