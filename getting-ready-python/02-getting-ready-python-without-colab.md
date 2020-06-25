# How to get started on python tutorials without google co-lab

We recognize that some of our students will not be able to access google co-lab.  So this set of instructions is to help you get an alternative environment up and running.  You're going to be using a tool that's very similar to google colab called jupyter notebooks. (In fact google colab is just google's evolution of a jupyter notebook.) We have provided written instructions for macOS / Windows / Linux operating systems below.

### VIDEO INSTRUCTIONS
- macOS -- [Precourse Getting started with Python: Jupyter Notebooks Mac OS](https://www.youtube.com/watch?v=ex3W0QVQioU&feature=youtu.be)
- Windows -- UNDER CONSTRUCTION
- Linux -- UNDER CONSTRUCTION

## Step 1: Install Anaconda package manager

You'll need to [download and install anaconda](https://www.anaconda.com/products/individual) for your operating system [Mac / PC / Linux].  

The rest of the steps will be somewhat specific to your operating system, so navigate to the operating system you are using.

## macOS / Linux

### Step 2: Create a folder for your python tutorials
First make a folder where you'll keep your jupyter notebooks for the python tutorials.  I'm going to make a folder in Documents called python-tutorials-2020.

You'll need to open a terminal. Open the application named Terminal and navigate to the folder you just created using the 'cd' command. [cd stands for change directory] You will have to adjust this file directory location according to where you have placed your folder. 

`cd ~/Documents/python-tutorials-2020`

### Step 3: Create the python programming environment for these tutorials

Now we need to create the conda environment.  [This blog post](https://heartbeat.fritz.ai/creating-python-virtual-environments-with-conda-why-and-how-180ebd02d1db) by [Okoh Anita](https://heartbeat.fritz.ai/@anitaokoh) is helpful for describing why we need environments when we program and how you create them.  Below I provide instructions for the steps we'll take to create an environment for the python tutorials.

We need to create an environment.yml file that contains:

	name: nma-prep
	channels:
	  - conda-forge
	dependencies:
	  - matplotlib
	  - numpy
	  - python=3.7
	  - scipy
	  - ipywidgets
	  - jupyter
	  - nb_conda
	  - pandas



In order to create this file we are going to use a text editor called nano.  To check to see if nano is installed run the following command:

	nano --version
	
*If you are running Linux and nano is not installed, run the following command (you will have to type in your password):*

	sudo apt-get install nano


To create the file, type the command:

	nano environment.yml

This will open a file named environment.yml with a text editor called nano.  Copy and paste the contents above into that file.  To save the document, press ctrl-O followed by enter.  To close the document, press ctrl-X. 

Now we can install the environment.  Run the following command to create the environment. 
	
	conda env create
Then follow the instructions that print out in the terminal.  It may take a few minutes to complete the installation.

Now activate the environment!

	conda activate nma-prep

### Step 4 - Opening a jupyter notebook
Run the following command:

	jupyter notebook

This should open up your default browser.  In the upper right-hand corner, click the button labelled new.  This will bring up a drop-down menu.  Click on the option labelled: Python [conda env:nma-prep].  This will open a new tab.  You have successfully opened a jupyter notebook!  You can now use this programming environment to start working on the python tutorials.

## Windows

### Step 2: Create a folder for your python tutorials
First make a folder where you'll keep your jupyter notebooks for the python tutorials.  I'm going to make a folder in Documents called python-tutorials-2020.

### Step 3: Create the NMA programming environment
Now we need to create the conda environment.  [This blog post](https://heartbeat.fritz.ai/creating-python-virtual-environments-with-conda-why-and-how-180ebd02d1db) by [Okoh Anita](https://heartbeat.fritz.ai/@anitaokoh) is helpful for describing why we need environments when we program and how you create them.  Below I provide instructions for the steps we'll take to create an environment for the python tutorials.

We need to create an environment.yml file that contains:

	name: nma-prep
	channels:
	  - conda-forge
	dependencies:
	  - matplotlib
	  - numpy
	  - python=3.7
	  - scipy
	  - ipywidgets
	  - jupyter
	  - nb_conda
	  - pandas

Open Notepad. Copy and paste the contents above into that file.  Save the document in the folder you created and name it environment.yml

Now open the Anaconda Navigator and launch the CMD.exe Prompt. Navigate to the folder you just created using the 'cd' command. [cd stands for change directory] You will have to adjust this file directory location according to where you have placed your folder. 

`cd C:/Documents/python-tutorials-2020`

Now we can install the environment.  Run the following command to create the environment. 
	
	conda env create

It may take a few minutes to complete the installation.

Now activate the environment!

	conda activate nma-prep

### Step 4 - Opening a jupyter notebook
Run the following command:

	jupyter notebook

This should open up your default browser.  In the upper right-hand corner, click the button labelled new.  This will bring up a drop-down menu.  Click on the option labelled: Python [conda env:nma-prep].  This will open a new tab.  You have successfully opened a jupyter notebook!  You can now use this programming environment to start working on the python tutorials. 
