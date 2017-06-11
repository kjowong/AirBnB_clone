# AirBnB Clone (The Holberton B&B)

![Hbnb](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

This project consists of building a command interpreter to manipulate data without a visual interface, like in a Shell

## Concepts learned:
* [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python packages](https://intranet.hbtn.io/concepts/66)
* Serialization/Deserialization
* `*args, **kwargs`
* `datetime`

## The console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

### Execution
To run the console, type `./console.py` script. 
Type `help` for list of commands.

Commands include:
* `create`: creates a new instance of model (you need to specify class for the model)
* `show`: shows information about a model based on id
* `destroy`: delete model
* `all`: display information about all models
* `update`: updates instance based on name, id and attribute
quit: exits