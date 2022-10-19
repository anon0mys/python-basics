# Python Basics

This is a collection of exercises to practice various aspects of Python.

Practicing in this manner (small, bite-sized problems that you can do repeatedly) is a _fantastic_ way to solidify programming concepts.

Each folder in this repository is a set of related exercises. Open up the folder and read the README to learn more about them.

## Structure of this repository
- Each folder contains a `README.md` file that provides a summary of what skills you will develop with these exercises
- Each exercise file within the folder will begin with comments providing more detail on:
  1. How you need to manipulate or work with this file to complete the exercise.
  2. Some exercises will require you to manipulate the "current" file and run it. Other exercises will require you to create _new_ files and then reference those files for the "current" file to work.

## Setup

### 1. Clone this repository

You don't need to fork this repository; clone it to your laptop by running:

```
// using ssh keys
git clone git@github.com:turingschool/ruby-exercises.git
// using https, if the above doesn't work:
git clone https://github.com/turingschool/ruby-exercises.git
```

Once this command runs, you'll now have a "local" copy of this entire repository, living right on your laptop.

### 2. From the command line, `cd` into the `python-basics` directory.

### 3. From the command line, run `pip install -r requirements.txt`

You _should_ see something like this:

```
$ pip install -r requirements.txt
Requirement already satisfied: pytest in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (6.2.4)
Requirement already satisfied: pluggy<1.0.0a1,>=0.12 in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (0.13.1)
Requirement already satisfied: py>=1.8.2 in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (1.10.0)
Requirement already satisfied: iniconfig in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (1.1.1)
Requirement already satisfied: packaging in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (20.9)
Requirement already satisfied: attrs>=19.2.0 in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (21.2.0)
Requirement already satisfied: toml in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pytest->-r requirements.txt (line 1)) (0.10.2)
Requirement already satisfied: pyparsing>=2.0.2 in /Users/evan.wheeler/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from packaging->pytest->-r requirements.txt (line 1)) (2.4.7)
```
If you see that, great!

If you get an error like:

```

```

> Hey, hold up. What is this `pip` thing, and what does it do? what does `pip install -r requirements.txt` do?

Great question!

`pip` is Ptyhons's [package manager](https://pip.pypa.io/en/stable/). If you want to install extra code that works with Python, you'll use `pip` to do it.

It is used in conjunction with the `requirement.txt` file you see in this repository, to manage Python libraries.

Here's an exhaustive amount of information about python libraries, if you're so inclined: [https://packaging.python.org/en/latest/overview/](https://packaging.python.org/en/latest/overview/)

-------------------

Once `pip install` has run successfully, open up the first exercise!

```
$ cd data-types/strings
$ charm .
```

And read through the `README.md` for further instructions!

----------------------------------