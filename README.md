# pands-weekly-tasks

##### Welcome to my Programming and Scripting Weekly Tasks repository. This project contains tasks completed as part of the weekly assignments for the PANDS module in the Postgraduate Diploma in Data Analytics in ATU.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Tasks Overview](#tasks-overview)

## Installation
#### To get started with the project, clone the repository to your local machine:
```bash

git clone https://github.com/zoeharlowe/pands-weekly-tasks.git

```
#### Navigate into the project directory:
```bash

cd pands-weekly-tasks

```
#### You can then set up a virtual environment to manage the dependencies:
```bash

python3 -m venv venv

```

#### Activate the virtual environment:
- **On Windows:**
```bash

venv\Scripts\activate

```
- **On Mac/OS/Linux:**
```bash

source venv/bin/activate

```
## Usage
#### Once the repository is set up, you can run the individual Python scripts for each weekly task. Each task is located in its respective file. To run a specific script, use the following command:
```bash

python script_name.py

```
#### Replace script_name.py with the filename of the task you wish to run.

## Tasks Overview
##### This repository includes the following weekly tasks:

### Week 1: helloWorld.py
##### This program prints "Hello World" to the screen.

##### **Key Concepts:** Using the print() function

### Week 2: bank.py
##### This program reads in two money amounts, adds them and prints the result in a readable format. 
##### **Key Concepts:** Casting strings to floats
##### *https://bobbyhadz.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str#typeerror-can-only-concatenate-str-not-float-to-str*

### Week 3: accounts.py
##### This program reads in a bank account number of any length and output the number where only the last 4 digits are shown. All the other digits are replaced with 'X's

##### **Key Concepts:** Indexing, using the len() function

### Week 4: collatz.py
##### Implements the Collatz conjecture algorithm. This program reads in a positive integer. If the integer is even, it divides it by two. If it is odd, it multiplies it by three and adds one. The program stops once it outputs the number 1.

##### **Key Concepts:** While loops, if statements
##### *https://www.youtube.com/watch?v=094y1Z2wpJg&t=855s*

### Week 5: weekday.py
##### This program determines the day of the week and outputs whether today is a weekday or not. There is no user input.

##### **Key Concepts:** Date handling, datetime module

### Week 6: squareroot.py
##### This program takes a positive float as input and outputs it's approximate square root.

##### **Key Concepts:** Functions
##### *Galaxy Code AI Generator*

### Week 7: es.py
##### This program will output how many times it counts the letter 'e' in a text file. The file will be passed in as an argument on the command line.

##### **Key Concepts:** File management/creation, sys.argv(), FileNotFoundError

### Week 8: plottask.py & plot-task.png
##### Generates plots based on data and visualizes the results. This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 and a plot of the function  h(x)=x3 in the range 0 to 10 - on the same set of axes.

##### **Key Concepts:** Data visualization, matplotlib library, setting parameters on plots.
##### *https://stackoverflow.com/questions/45699759 how-do-you-limit-the-y-axis-height-in-matplotlib*

