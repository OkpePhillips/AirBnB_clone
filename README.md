## 0x00. AirBnB clone - The console


This is the first step towards building a full web application: the AirBnB clone. 
This first because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

The tasks herein provide the basics for creating the Airbnb clone:

HOW?
 1. Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
 2. Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> 
 file.
 3. Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 4. Create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine.


#### The Console

This is the interface that allows testing the mainpulation of data held and processed by the clone system.

##### 1. HOW TO START IT.
The console entry point is initiated by entering:
> ` ./console.py  `
from the root folder of the project folder.


#### 2. HOW TO USE IT. 

There are a few commands accepted by the console to create, read, update and destroy objects being managed by the program.

Typical syntax looks as follows:
> ` <command> <arguements if present>`

Example:
` (hbnb) help <topic> ` - Provides extra information on the uses for different functions.(Lists all documented commands if topic is not provided.)

` (hbnb) create <class name> ` - Generates a new instance of ` <class name> ` and returns its UUID

*** Further information on functions can be retrieved via the console ` help ` function. ***
