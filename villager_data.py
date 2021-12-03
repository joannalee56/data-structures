"""Functions to parse a file containing villager data."""
#name|species|personality|hobby|motto

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    # Result = ('bear','anteater', ...)
    
    species = set()

    file = open(filename)

    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')
      species.add(villager_info[1])

    file.close()

    return species

# print(all_species("villagers.csv"))

def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []

    file = open(filename)

    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')
      
      if species == villager_info[1] or species == 'All':
        villagers.append(villager_info[0])#name

    file.close()

    # TODO: replace this with your code

    return sorted(villagers)

print(get_villagers_by_species("villagers.csv", 'Bear'))

def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    # TODO: replace this with your code
    fitness, nature, education, music, fashion, play = [], [], [], [], [], []
    
    file = open(filename)

    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')

      if villager_info[3] == 'Fitness':
        fitness.append(villager_info[0])
      elif villager_info[3] == 'Nature':
        nature.append(villager_info[0])
      elif villager_info[3] == 'Education':
        education.append(villager_info[0])
      elif villager_info[3] == 'Music':
        music.append(villager_info[0])
      elif villager_info[3] == 'Fashion':
        fashion.append(villager_info[0])
      elif villager_info[3] == 'Play':
        play.append(villager_info[0])

    file.close()

    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]

print(all_names_by_hobby('villagers.csv'))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    
    file = open(filename)

    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')
      
      villager_tuple = (villager_info[0], villager_info[1], villager_info[2], villager_info[3], villager_info[4])
      
      all_data.append(villager_tuple)
      
    file.close()
    return all_data

print(all_data("villagers.csv"))

def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    villager_motto = None

    file = open(filename)

    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')

      if name == villager_info[0]:
        villager_motto = villager_info[4]
    
    file.close()

    return villager_motto

print(find_motto('villagers.csv', 'Joanna'))


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    villager_personality = set()
    file_data = []
    file = open(filename)

    # Find name's personality
    for line in file:
      line = line.rstrip()
      villager_info = line.split('|')
      file_data.append(villager_info)

      if name in villager_info:
        personality = villager_info[2]
    
    file.close()
    
    # Search for all the other villagers with the same personality
    # file = open(filename)
    # for line in file:
    #     line = line.rstrip()
    #     villager_info = line.split('|')
        # if personality == villager_info[2]:
        #   villager_personality.add(villager_info[0])
    
    for data in file_data:
      if personality == data[2]:
          villager_personality.add(data[0])

    

    return villager_personality

print(find_likeminded_villagers('villagers.csv', 'Audie'))