This repository contains some experiments using Kivy as a replacement for PySide.

# Setup
The following setup section(s) assume basic Python, Git, GitHub, and virtual environment knowledge.

## Windows
* Download and install [Python 3.4.4](https://www.python.org/downloads/release/python-344/).

* Fork this repository.

* Clone this repository:

  `git clone git@github.com:your_github_user_name/kivygui.git`
  
* Install the following Python virtual environment libraries:

  `pip install virtualenvwrapper virtualenvwrapper-win`

* In the Windows command line, create a virtual environment for Kivy:

  `mkvirtualenv kivygui`
  
* Set the project directory for your new virtual environment to the same directory where you cloned this repository into:

  `setprojectdir C:\Users\you\Projects\kivygui`
  
* Install Kivy's dependencies within your virtual environment:

  `pip install -r requirements.txt`
  
Congrats, you should now be able to `import kivy`.
