"""Example of an undirected graph."""

from queue import Queue


class PersonNode():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with cohabitants adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<PersonNode: {self.name}>"


class CohabitantGraph():
    """Graph holding people and their cohabitant relationships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<CohabitantGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def cohabitants(self, person1, person2):
        """Set two people as cohabitants"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for cohabitant in person.adjacent - seen:
                    possible_nodes.enqueue(cohabitant)
                    seen.add(cohabitant)
                    print("added to queue:", cohabitant)
        return False

    def are_connected_recursive(self, person1, person2, seen=None):
        """Were two people cohabitants? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                if self.are_connected_recursive(person, person2, seen):
                    return True

        return False

    def verbose_are_connected_recursive(self, person1, person2, seen=None):
        """Were two people cohabitants? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            print("\nreturning True - {} is {}".format(person1.name, person2.name))
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                print("calling method on {}'s cohabitant {} with {}".format(person1.name, person.name, person2.name))
                if self.verbose_are_connected_recursive(person, person2, seen):
                    print("\nreturning True from checking {}".format(person.name))
                    return True

        print("returning False from checking {}".format(person1.name))
        return False

rachel = PersonNode("Rachel Perkins")
steven = PersonNode("Steven Edouard")
jeff = PersonNode("Jeff Dean")
sara = PersonNode("Sara Ellsworth")
gabe = PersonNode("Gabe")
julie = PersonNode("Julie")
mari = PersonNode("Mari")
troy = PersonNode("Troy")
josh = PersonNode("Josh")
shigs = PersonNode("Jonathan Shigamatsu")
kim = PersonNode("Kim Shores")
sonam = PersonNode("Sonam Gill")
harman = PersonNode("Harman Nagi")
ashley = PersonNode("Ashley Youngblood")
sean = PersonNode("Sean Nichols")
sarah_p = PersonNode("Sarah Pulley")
olivia = PersonNode("Olivia Sorgman")
christie = PersonNode("Christie Bahna")
sarah_r = PersonNode("Sarah Rose")
jay = PersonNode("Jay Snow")

cohabitants = CohabitantGraph()
cohabitants.add_people([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

cohabitants.set_cohabitants(rachel, steven)
cohabitants.set_cohabitants(rachel, josh)
cohabitants.set_cohabitants(rachel, troy)
cohabitants.set_cohabitants(rachel, jeff)
cohabitants.set_cohabitants(rachel, sara)
cohabitants.set_cohabitants(rachel, gabe)
cohabitants.set_cohabitants(rachel, julie)
cohabitants.set_cohabitants(rachel, sonam)
cohabitants.set_cohabitants(sonam, harman)
cohabitants.set_cohabitants(sonam, julie)
cohabitants.set_cohabitants(sonam, gabe)
cohabitants.set_cohabitants(julie, christie)
cohabitants.set_cohabitants(julie, mari)
cohabitants.set_cohabitants(julie, gabe)
cohabitants.set_cohabitants(julie, steven)
cohabitants.set_cohabitants(julie, olivia)
cohabitants.set_cohabitants(olivia, gabe)
cohabitants.set_cohabitants(sonam, olivia)
cohabitants.set_cohabitants(gabe, steven)
cohabitants.set_cohabitants(gabe, mari)
cohabitants.set_cohabitants(gabe, christie)
cohabitants.set_cohabitants(christie, mari)
cohabitants.set_cohabitants(troy, sean)
cohabitants.set_cohabitants(sean, sarah_p)
cohabitants.set_cohabitants(troy, josh)
cohabitants.set_cohabitants(troy, jeff)
cohabitants.set_cohabitants(troy, sara)
cohabitants.set_cohabitants(josh, jeff)
cohabitants.set_cohabitants(josh, sara)
cohabitants.set_cohabitants(jeff, sara)
cohabitants.set_cohabitants(josh, ashley)
cohabitants.set_cohabitants(ashley, shigs)
cohabitants.set_cohabitants(kim, shigs)
cohabitants.set_cohabitants(troy, mari)
cohabitants.set_cohabitants(sara, sarah_r)
cohabitants.set_cohabitants(sarah_r, jay)