# How to get started on python tutorials without google co-lab

We recognize that some of our students will not be able to access google colab. So this set of instructions is to help you get an alternative environment up and running. You're going to be using a tool that's very similar to google colab called jupyter notebooks (in fact google colab is just google's evolution of a jupyter notebook). We have provided written instructions for macOS / Windows / Linux operating systems below.

### VIDEO INSTRUCTIONS
- macOS -- [Precourse Getting started with Python: Jupyter Notebooks Mac OS](https://www.youtube.com/watch?v=ex3W0QVQioU&feature=youtu.be)
- Windows -- UNDER CONSTRUCTION
- Linux -- UNDER CONSTRUCTION

## macOS / Linux / Windows

## Step 1: Install Anaconda package manager

You'll need to [download and install anaconda](https://www.anaconda.com/products/individual) for your operating system [Mac / PC / Linux].

The rest of the steps will be somewhat specific to your operating system, so navigate to the operating system you are using.

### Step 2: Download the tutorials
First clone the github repo of the precourse material using the terminal (on Windows you have to use an anaconda prompt)

```git clone https://github.com/NeuromatchAcademy/precourse.git --depth=1```

You'll need to open a terminal. Open the application named Terminal and navigate to the folder you just created using the 'cd' command. [cd stands for change directory] You will have to adjust this file directory location according to where you have placed your folder. 

```cd precourse/```

### Step 3: Create the python programming environment for these tutorials

Now we need to create the conda environment. [This blog post](https://heartbeat.fritz.ai/creating-python-virtual-environments-with-conda-why-and-how-180ebd02d1db) by [Okoh Anita](https://heartbeat.fritz.ai/@anitaokoh) is helpful for describing why we need environments when we program and how you create them.

We can create the environment. Run the following command to create the environment. 
	
```conda env create -f environment.yml```

Then follow the instructions that print out in the terminal. It may take a few minutes to complete the installation.

Now activate the environment!

```conda activate nma-precourse```

You can also install the requirements.txt. Run the following command.

```pip install -r requirements.txt```

### Step 4 - Opening a jupyter notebook
Run the following command:

```jupyter-notebook```

This should open up your default browser. In the upper right-hand corner, click the button labelled new. This will bring up a drop-down menu. Click on the option labelled: Python [conda env:nma-precourse]. This will open a new tab. You have successfully opened a jupyter notebook! You can now use this programming environment to start working on the python tutorials.
