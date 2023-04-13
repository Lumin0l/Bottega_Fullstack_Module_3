# Pipenv allows you to wrap your entire project dependencies into a single environment.

'''

The libraries (requests, numpy...) are most often open source and they evolve.
So, You can use a library for a project, then after a time use it for a nother project, have it upgraded and then start having bugs in the first one.

Pipenv brings a solution to this issue by creating isolated coding environments with the libraries:

pipenv-1
        Machine Learning Project.

    pipenv-2
        Django web API Project.

In this case, pipenv will create a virtual environment for each project and store the working versions of the libraries there instead of system-wide.

To check how it works type "pipenv -v" and it will show the commands.

Quickguide:
    pipenv --three: will create a pipenv environment inside the directory youre in.

It will create a pipfile directory with the instructions that it will follow.

Following this creationm in the directory where the virtual environment is you need to use 'pipenv install xxxx':
    pipenv install numpy

It will create a pipfile.lock file where it specifies the instructions for using a specific version of a library.

'''

