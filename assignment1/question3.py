"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

bldgs = []

class Person:
    def __init__(self, fname, lname, gender):
		if (not fname[0].isupper()):
		    raise Exception("First name must be capitalized")
		elif (not lname[0].isupper()):
		    raise Exception("Last name must be capitalized")
		elif not (gender == "M" or gender == "F"):
		    raise Exception("Not a valid gender")
		else:
		    self.fname = fname
		    self.lname = lname
		    self.gender = gender
		    self.bldg = None

class Building(object):
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.loc = (None, None)
        bldgs.append(self)
        
    def __getitem__(self, index) :
        return self.rooms[index]

    def __setitem__(self, index, value) :
        enter(value, index)
        
    def __iter__(self):
        return iter(map(lambda i: i[0], self.rooms))
    
    def enter(self, person, room_no):
        self.room_no = room_no
        for room in self.rooms:
            if room[0] == person:
                self.rooms.remove((room[0], room[1], room[2]))
                person.bldg = None
        if (person.bldg == None):
            self.rooms.append((person, self.room_no, self.name))
            person.bldg = self
           
    def where_is(self, person):
        for room in self.rooms:
            if room[0] == person:
                return room[0].fname + " " + room[0].lname + " is in room " + str(room[1]) + " of " + str(room[2])
        return "Person not in any room"
        
    def give_loc(self, x, y):
        if not (type(x) is int and type(y) is int):
            raise Exception("Please enter a location of form (int, int)")
        else:
            self.loc = (x, y)

class Office(Building):
    def __init__(self, name, employees):
        super(Office, self).__init__(name)
        self.employees = employees
        
    def enter(self, person, room_no):
        if (person in self.employees):
            super(Office, self).enter(person, room_no)
        else:
            return "Person not on employee list"
    
class House(Building):
    def __init__(self, name):
        super(House, self).__init__(name)
        
    def enter(self, person):
        super(House, self).enter(person, None)            

    def where_is(self):
        pass
        
    def at_home(self, person):
        return (person in map(lambda i: i[0], self.rooms))
        
def find(x, y):
    for b in bldgs:
        if (b.loc == (x, y)):
            return b
    return None
