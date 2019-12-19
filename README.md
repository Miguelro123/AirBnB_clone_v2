<p>
<img width="260" height="90" src="https://uploads-ssl.webflow.com/5b0fe6b5acd20859e6fbac66/5b1641a1e46275621a2b436d_Holberton-Logo-final.png" align="right" >
</p>

# AirBnB clone - MySQL
```
This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.
```
### Supported classes:
```
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review
```
### Commands:
```
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.
```
#### Create
```
create <class name>
Ex:
create BaseModel
```
#### Show
```
show <class name> <object id>
Ex:
show User my_id
```
#### Destroy
```
destroy <class name> <object id>
Ex:
destroy Place my_place_id
```
#### All
```
all or all <class name>
Ex:
all or all State
```
#### Quit
```
quit or EOF
```
#### Help
```
help or help <command>
Ex:
help or help quit

Additionally, the console supports <class name>.<command>(<parameters>) syntax.
Ex:
City.show(my_city_id)
```
![Holberton logo](https://www.holbertonschool.com/holberton-logo.png)


## Authors
* **Julian David Gaitan S** - [JulianDavidG07](https://github.com/JulianDavidG07)
* **Edgar Miguel Rodriguez G** - [Miguelro123](https://github.com/Miguelro123)
