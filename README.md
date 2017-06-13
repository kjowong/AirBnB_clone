# AirBnB Clone (The Holberton B&B)

![Hbnb](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

This project consists of building a command line interpreter (console) to manipulate data without a visual interface, like in a Shell

### The console functionality
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)


### Environment
Our Monty interpreter has been tested on Ubuntu 14.05.5 LTS
Tests done in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)

## Files and Directories

### Directories:
* `models/` directory contains all classes used for the entire project. 
* `models/engine/` directory containing File Storage class, handling serialization and deserialization of JSON 
* `tests/` directory contain all unit tests
* `tests/test_models` directory contain all unit tests for classes Amenity, Base Model, City, Place, Review, State, User.
* `tests/test_models/test_engine/` directory containing unittest for File Storage class.

### Program Files:
* `console.py` this file is the entry point of the command interpreter.
* `models/base_model.py` is the base class of all models. It contains common elements:
    * attributes: `id`, `created_at` and `updated_at`
    * methods: `save()` and `to_json()`
* `models/amenity.py` - Class Amenity inherits from BaseModel
* `models/city.py` - class City, inherits from BaseModel
* `models/place.py` - class Place, inherits from BaseModel
* `models/review.py` - class Review, inherits from BaseModel
* `models/state.py` - class State, inherits from BaseModel
* `models/user.py` - class User, inherits from BaseModel
* `models/engine/file_storage.py` - class FileStorage, handling sorage of object - creating new, saving and reloading objects

### Test Files:
Location of test files corresponds with the location of program files.
* `tests/test_console.py` - unittest for console.py
* `tests/test_models/test_base_model.py` - unittest for base_model.py file
* `tests/test_models/test_engine/test_file_storage.py` - unittest for File Storage class
* `tests/test_amenity.py` - unittest for Amenity Class 
* `tests/test_city.py` - unittest for City Class
* `tests/test_place.py` - unittest for Place Class
* `tests/test_review.py` - unittest for Review Class
* `tests/test_state.py` - unittest for State Class
* `tests/test_user.py` - unittest for User Class

## Classes:
**Amenity** ( `models/amenity.py` ) - Amenity Class which inherits from the class BaseModel. Includes attributes:
*   `name` - string format, dafault - empty string

**BaseModel** (`models/base_model.py`) - base class that defines all common attributes/methods for other classes.
Attributes include:
* `id` - string, assigned by `uuid` when instance is created
* `create_at` - datetime format - assigned when instance is created
* `update_at` - datetime format

Methods of class BaseModel:
* `save(self)` - updates public instance attribute `updated_at` with the current datetime
* `to_json(self)` - returns a dictionary containing all keys/values of the instance and the name of the class

**City** (`models/city.py`) - class City that inherits from the BaseModel. Contains following attributes:
* `state_id` - string format
* `name` - string format

**FileStorage** (`models/engine/file_storage.py`) - class FileStorage - used for serialization of instances to a JSON file and vice versa.
Class attributes:
* `__file_path` - string format - path to JSON file
* `__objects` - dictionary - for storing all objects by `<class name>.id` format

Class methods:
* `all(self)` - method to return all objects
* `new(self, obj)` - used to set all objects in the the dictionary with the following key format - `<obj class name>.id`
* `save(self)` - used to serialize objects to JSON file
* `reload(self)` - for deserializing onjects 

**Place** (`models/place.py`) - class Place, which inherits from the BaseModel class. 
Attributes of the class:
* `city_id` - string format
* `user_id` - string format
* `name` - string format
* `description` - string format
* `number_rooms` - integer format
* `number_bathrooms` - integer format
* `max_guest` - integer format
* `price_by_night` - integer format
* `latitude` - float format
* `longitude` - float format
* `amenity_ids` - list of strings

**Review** (`models/review.py`) - Review class which inherits from BaseModel class. 
Attributes of the class:
* `place_id` - string format
* `user_id` - string format
* `text` - string format

**State** (models/state.py) - State class which inherits from the BaseModel class. 
Class attributes:
* `name` - string format

**User** (`models/user.py`) - User class that inherits from the BaseModel class.
Class attributes:
* `email` - string format
* `password` - string format
* `first_name` - string format
* `last_name` - string format



### Execution
First step is to clone the repository into your directory:
``` 
$ git clone https://github.com/halinav00/AirBnB_clone.git 
```
To run the console, type `./console.py` script. 
```
$ ./console.py
```
Type `help` for list of commands.
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

Commands include:
* `create`: creates a new instance of model (you need to specify class for the model)
* `show`: shows information about a model based on id
* `destroy`: delete model
* `all`: display information about all models
* `update`: updates instance based on name, id and attribute
* `quit`: exits

**Examples of use:**
```
(hbnb) create User
3db5637d-5df4-44cf-a250-ef2b523946e9
(hbnb) show User 3db5637d-5df4-44cf-a250-ef2b523946e9
[User] (3db5637d-5df4-44cf-a250-ef2b523946e9) {'id': '3db5637d-5df4-44cf-a250-ef2b523946e9', 'updated_at': datetime.datetime(2017, 6, 13, 4, 18, 50, 138053), 'created_at': datetime.datetime(2017, 6, 13, 4, 18, 50, 138027)}
(hbnb) destroy User 3db5637d-5df4-44cf-a250-ef2b523946e9
(hbnb) show User 3db5637d-5df4-44cf-a250-ef2b523946e9
** no instance found **
(hbnb)
```

### Known Bugs
If found - call exterminator

### Concepts learned:
* [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python packages](https://intranet.hbtn.io/concepts/66)
* Serialization/Deserialization
* `*args, **kwargs`
* `datetime`

### Authors
*Kimberly Wong* - [Github](https://github.com/kjowong) || [Twitter](https://twitter.com/kjowong) || [email](kimberly.wong@holbertonschool.com)
*Halina Veratsennik* - [Github](https://github.com/halinav00) || [Twitter](https://twitter.com/halinav) || [email](contact.halinav@gmail.com)


*Feedback and contributors are welcomed. Reach out to either authors*