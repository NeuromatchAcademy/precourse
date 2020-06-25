
## A first course / refresher course in python

Our recommendation is to work through this set of [python programming lessons](https://swcarpentry.github.io/python-novice-inflammation/) from [Software Carpentries](http://software-carpentry.org/).  It's a great introduction to python specifically designed for people working with data in research domains.  It will quickly get you using python for analyzing data.

During NMA we're going to be relying [Google Colab](https://colab.research.google.com/) to do our python programming, so we'd like you to try to use that when you do these python tutorials. One of our Neuromatch Academy TAs put together a [short video on Getting started with Python: Google Colab](https://www.youtube.com/watch?v=iFroq4SuSPM&feature=youtu.be) to get you started with all of this.  She'll walk you through opening up Google Colab, show you how to get data files imported into Colab, and get you started on the first set of exercises. *NOTE: If you don't have access to Google Colab (e.g., it's blocked in your region), you can follow the directions in 02-getting-ready-python-without-colab.md to get set up on your local machine with jupyter notebooks.*

Once you're done with that, we highly recommend checking out sections 6-9 of this [other software carpentries python course](http://swcarpentry.github.io/python-novice-gapminder/).  It will introduce you to important python libraries for data analysis and plotting. *Remember to import the data files into Google Colab. See video linked above for an example.*

## Written instructions for getting started on the python tutorials with google co-lab
This [video](https://www.youtube.com/watch?v=iFroq4SuSPM&feature=youtu.be) also walks you through the following steps.  Please check out the video if you get stuck.

### Step 1: Create a Google account / Sign-in to your google (gmail) account
You will need a google account (gmail account) to use Google Colab.  Note that some university emails are also google accounts and Google colab can be accessed through those as well.

### Step 2: Open a Google Colab notebook
Go to [https://colab.research.google.com/](https://colab.research.google.com/). Click new notebook.  If you want a tour of the basics of Google colab go to 1:09 in [video](https://www.youtube.com/watch?v=iFroq4SuSPM&feature=youtu.be).

### Step 3: Open the Software Carpentries Python course
Go to [https://swcarpentry.github.io/python-novice-inflammation/](https://swcarpentry.github.io/python-novice-inflammation/).  You can follow along with the course and work your way through the lessons using Google colab as your python programming environment.  But before you get started you will need to download and the data and load it into Google colab (see next step).

### Step 4: Load the data into Google Colab
Go to [https://swcarpentry.github.io/python-novice-inflammation/setup/index.html](https://swcarpentry.github.io/python-novice-inflammation/setup/index.html).  You will need to download python-novice-inflammation-data.zip from the section entitled obtaining course materials. Unzip the file.

In order to upload it to Google colab you will need to put the following two lines into a code cell:
```
from google.colab import files
files.upload() 
```
Run the cell.  Select ALL of the data files you just downloaded and upload those into Google Colab.  Any time you restart Google Colab you will need to reload this data.

### Step 5: Have fun programming!!!
See you at Neuromatch Academy :)
