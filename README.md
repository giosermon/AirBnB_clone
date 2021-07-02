# AirBnB_clone

<p align="center"><img src="https://i.pinimg.com/originals/b7/96/7a/b7967a5072e088986559b57b4ba53c83.jpg"/></p>

<h1>Project Description</h1>

Airbnb Clone is the main project of the second trimester at Holberton School. The aim is to develop an entire web application that simulates the behavior of the Airbnb platform. Starting from the console or command interpreter


<h1>Learning Objectives</h1>

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    How to create a Python package
    How to create a command interpreter in Python using the cmd module
    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    How to manage datetime
    What is an UUID
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7 or more)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start by test_
    Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case

<h1>Installation</h1>
*Clone this repository:https://github.com/giosermon/AirBnB_clone.git
*Run hbnb(interactively): ./console and enter commands
*Run hbnb(non-interactively): echo "<command>" | ./console.py

Example Usage book
Interative Mode:

<p>(hbnb) help</p>

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb)create BaseModel
df1ca7e3-a140-4739-b4da-96f87b4e7ee9
(hbnb)all BaseModel
["[BaseModel] (df1ca7e3-a140-4739-b4da-96f87b4e7ee9) {'updated_at': datetime.datetime(2020, 2, 19, 22, 49, 0, 939794), 'created_at': datetime.
datetime(2020, 2, 19, 22, 49, 0, 939700), 'id': 'df1ca7e3-a140-4739-b4da-96f87b4e7ee9'}"]
(hbnb)show BaseModel df1ca7e3-a140-4739-b4da-96f87b4e7ee9
[BaseModel] (df1ca7e3-a140-4739-b4da-96f87b4e7ee9) {'updated_at': datetime.datetime(2020, 2, 19, 22, 49, 0, 939794), 'created_at': datetime.datetime(2020, 2, 19, 22, 49, 0, 939700), 'id': 'df1ca7e3-a140-4739-b4da-96f87b4e7ee9'}
(hbnb) create User
8cf2405e-2837-4a7c-b824-b12a9a0d89b2
(hbnb) destroy BaseModel df1ca7e3-a140-4739-b4da-96f87b4e7ee9
(hbnb) show BaseModel df1ca7e3-a140-4739-b4da-96f87b4e7ee9
** no instance found **
(hbnb) quit
