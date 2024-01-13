# AirBnB clone - The console 🏠🏠

![65f4a1dd9c51265f49d0](https://github.com/Ronnie5562/alu-AirBnB_clone/assets/110787129/9f3f3ede-75d4-44fc-a1b3-7a71152e9633)


# Description of the project

This project is a simple clone of the AirBnB website. The first stage implements a backend interface or console to manage program data(like shell). Console commands allow users to create, update, destroy objects, and manage file storage. 

# The console - tasks
-  Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of  future instances <br>
-  Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-  Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-  Create the first abstracted storage engine of the project: File storage.
-  Create all unittests to validate all our classes and storage engine


# Description of the command interpreter

The command interpreter helps us to manage the objects of our project by:

- Creating a new object (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object

## How to start the interpreter

```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  delete  destroy  exit  help  q  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit

```

## How to use the interpreter

## Tests
To run all the tests execute the following command:

```bash
$ python3 -m unittest discover tests
```
You can also run a single test by specifying the test file:

```bash
$ python3 -m unittest tests/test_models/test_city.py

```


# Authors

## [`Abimbola Ronald`](https://www.linkedin.com/in/abimbola-ronald-977299224/)
## [`Bernice Uwituze`](https://www.linkedin.com/in/bernice-uwituze)
