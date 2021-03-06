class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.characters = []


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.armor_head = []
        self.armor_torso = []
        self.armor_legs = []
        self.flavor = "salty"

    def move(self, new_location):
        """This moves the player to a new room.

        :param new_location: The room object of which you are going to move to.
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction.

        :param direction: The direction you want to move to.
        :return: The Room object if it exists, or None if not.
        """
        return getattr(self.current_location, direction)


# Option 1 - Define as we go
StartRoom = Room("Starting Room", "You're suddenly in a strange forest, in the middle of an island. How'd you get "
                                  "here? There's paths to each cardinal direction.")
northern_path = Room("Northern Path", "There's a path to your north, a path to your east, and a path back to your "
                                      "starting point, to the south.", None, StartRoom, None, None)
southern_path = Room("Southern Path", "You find three paths to go to: one to the south, one to the west, and one to "
                                      "the north, back to your starting point.", StartRoom, None, None, None)
eastern_path = Room("Eastern Path", "You can see paths to the east and north, along with a path west, back to where "
                                    "you started.", None, None, None, StartRoom)
western_path = Room("Western Path", "You can see a path to your west, a path south, and a path back east to your "
                                    "starting point.", None, None, StartRoom, None)
ne_path = Room("Armory", "You find some abandoned armor here, along with a large number of steaks. Maybe someone was"
                         " here before you? There are also paths south and west.", None, eastern_path, None,
               northern_path)
nw_path = Room("Northwest Path", "You can barely see anything except the paths to the south and east.",
               None, western_path, northern_path, None)
se_path = Room("Southeast Path", "You can only see paths to the north and west.", eastern_path, None, None,
               southern_path)
sw_path = Room("Southwest Path", "You're surrounded by trees, but there are paths to the north and east.",
               western_path, None, southern_path, None)
northern_dog = Room("Dog Room (North)", "There's a pomeranian here, just sitting down and drawing a picture. Maybe, "
                                        "just maybe, you can befriend it...? There are also paths north and south.",
                    None, northern_path, None, None)
southern_dog = Room("Dog Room (South)", "There's a small dog jumping up and down. It seems to just be recording an "
                                        "animation. Maybe you could befriend it...?", southern_path, None, None, None)
eastern_dog = Room("Dog Room (East)", "You observe the dog that's in here. It seems to be writing code on a laptop."
                                      "It's coding a game...? And can you really befriend a dog that's so"
                                      "distracted?", None, None, None, eastern_path)
western_dog = Room("Dog Room (West)", "Are you seeing double? There are TWO dogs here. One has a scarf, and the other"
                                      "has a pilot's cap. Where do dogs even get clothes? Anyways, you should probably"
                                      "find a way to get around them.", None, None, western_path, None)
nnn_path = Room("Far Northern Path", "You're past the Dog Room, and there's a broken boat here. If you found some"
                                     "wood, you could fix it, but right now, you can't sail.", None, northern_dog, None,
                None)
sss_path = Room("Far Southern Path", "You're past the Southern Dog Room. There's a dead end here, but you can still "
                                     "go back.", southern_dog, None, None, None)
eee_path = Room("Far Eastern Path", "There's a dead end past the Eastern Dog Room, but there is some wood here you "
                                    "can take.", None, None, None, eastern_dog)
www_path = Room("Far Western Path", "There's a beach here. It might be a dead end, but you're at least past the dogs.",
                None, None, western_dog, None)
water = Room("The Ocean", "You're riding a boat on the ocean. You're escaping the island!", None, None, www_path, None)
win = Room("You Win!", "You successfully escaped the island of dogs, and you can restart by running the program "
                       "again.", None, None, None, None)


StartRoom.north = northern_path
StartRoom.south = southern_path
StartRoom.east = eastern_path
StartRoom.west = western_path
northern_path.north = northern_dog
northern_path.east = ne_path
northern_path.west = nw_path
southern_path.east = se_path
southern_path.west = sw_path
eastern_path.north = ne_path
eastern_path.south = se_path
western_path.north = nw_path
western_path.south = sw_path
southern_path.south = southern_dog
eastern_path.east = eastern_dog
western_path.west = western_dog
northern_dog.north = nnn_path
southern_dog.south = sss_path
eastern_dog.east = eee_path
western_dog.west = www_path
www_path.west = water
water.west = win

player = Player(StartRoom)
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in ['restart']:
        player.current_location = StartRoom
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            if next_room is None:
                raise AttributeError
            player.move(next_room)
        except KeyError:
            print("You can't go that way.")
        except AttributeError:
            print("This path doesn't exist.")
    elif command.lower() in ['zork']:
        print("Wrong game.")
    else:
        print("I don't know that command.")