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
*Run hbnb(interactively): ./console and enter

Example Usage book
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $

Interative Mode:
Run hbnb(non-interactively): echo "<command>" | ./console.py

File Descriptions

console.py - Contains the entry point of command interpreter. Commands that this console accepts:

    EOF - exits console
    quit - exits console
    emptyline - overwrites default emptyline method and does nothing
    create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
    destroy - Deletes and instance base on the class name and id
    show - Prints all string representation of all instances based or not on the class name.
    all - Prints all string representation of all instances based or not on the class name.
    update - Updates an instance based on the class name and id by adding or updating attribute

    models - Directory that contains main classes:

    base_model.py - The BaseModel class is main class where where other classes will be derived. This class gives the main attributes like id, created and updated time when a instance occurs.

    Methods inside this class:

    def __init__(self, *args, **kwargs) - Initialization of the BaseModel class
    def __str__(self) - String representation of the BaseModel class
    def save(self) - Updates the attribute updated_at with the current datetime
    def to_dict(self) - returns a dictionary containing all keys and values of the instance

Public Instance Attributes:
    id
    created_at
    updated_at

Classes inherited from Base Model:

    amenity.py
    city.py
    place.py
    review.py
    state.py
    user.py

/models/engine - Directory that contains File Storage class that manages JSON serialization and deserialization :

file_storage.py - serializes instances to a JSON file & deserializes back to instances

Public Instance Methods:
    def all(self) - returns the dictionary __objects
    def new(self, obj) - sets in __objects the obj with key .id
    def save(self) - serializes __objects to the JSON file (path: __file_path)
    def reload(self) - deserializes the JSON file to __objects

Examples of use

    vagrantAirBnB_clone$./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb) all MyModel
    ** class doesn't exist **
    (hbnb) create BaseModel
    7da56403-cc45-4f1c-ad32-bfafeb2bb050
    (hbnb) all BaseModel
    [[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
    (hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
    [BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
    (hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
    (hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
    ** no instance found **
    (hbnb) quit


Web static:
        what?

    Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

    Before developing a big and complex web application, we will build the front end step-by-step.

    The first step is to “design” / “sketch” / “prototype” each element:

        Create simple HTML static pages
        Style guide
        Fake contents
        No Javascript
        No data loaded from anything

    During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

    Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.
