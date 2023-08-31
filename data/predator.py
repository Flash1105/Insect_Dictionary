class Predator: 
    def __init__ (self, name):
        self.name = name 

Predators = {
    "Birds": {
        "insect_names": [],
        "spider_names": [
            "Black Widow", "Wolf Spider", "Golden Silk Orb Weaver", "Brown Widow",
            "Brazilian Wandering Spider", "Trapdoor Spider", "Fishing Spider",
            "Goliath Birdeater", "Redback Spider", "Camel Spider", "Green Lynx Spider",
            "Six-Eyed Sand Spider", "Spiny Orb Weaver", "Bird-Dropping Spider",
            "Mouse Spider", "Net-Casting Spider", "Tarantula Hawk Spider",
            "Woodlouse Hunter", "Jumping Spider", "Crab Spider", "Tube Web Spider",
            "Huntsman Spider", "Australian Funnel-Web Spider", "Spitting Spider",
            "Socotra Island Blue Baboon Spider", "Red Trapdoor Spider", "Ghost Spider"
        ]
    },
    "Bats": {
        "insect_names": ["Bat Cave Cockroach"],
        "spider_names": [
            "Black Widow", "Wolf Spider", "Golden Silk Orb Weaver", "Brown Widow",
            "Brazilian Wandering Spider", "Trapdoor Spider", "Fishing Spider",
            "Goliath Birdeater", "Redback Spider", "Camel Spider", "Green Lynx Spider",
            "Six-Eyed Sand Spider", "Spiny Orb Weaver", "Bird-Dropping Spider",
            "Mouse Spider", "Net-Casting Spider", "Tarantula Hawk Spider",
            "Woodlouse Hunter", "Jumping Spider", "Crab Spider", "Tube Web Spider",
            "Huntsman Spider", "Australian Funnel-Web Spider", "Spitting Spider",
            "Socotra Island Blue Baboon Spider", "Red Trapdoor Spider", "Ghost Spider"
        ]
    },
    "Lizards": {
        "insect_names": [
            "Emperor Scorpion", "Giant Jumping Stick", "Giant Spiney Leaf Insect",
            "Giant Walking Stick", "Rhinoceros Katydid", "Thorny Devil",
            "Metallic Jewel Beetle", "Hercules Beetle", "Thorn Bug"
        ],
        "spider_names": [
            "Camel Spider", "Green Lynx Spider", "Jumping Spider", "Crab Spider"
        ]
    },
    "Frogs": {
        "insect_names": ["Emperor Scorpion", "Eastern Lubber Grasshopper"],
        "spider_names": ["Camel Spider", "Jumping Spider"]
    },
    "Spiders": {
        "insect_names": [
            "Emperor Scorpion", "Bat Cave Cockroach", "Blue Death Feigning Beetle",
            "Emerald Beetle", "Giant Spiney Leaf Insect", "Giant Walking Stick",
            "Green Leaf Cockroach", "Red Eyed Assassin Bug", "White Eyed Assassin Bug"
        ],
        "spider_names": []
    },
    "Wasps": {
        "insect_names": [
            "Emperor Scorpion", "Bat Cave Cockroach", "Green Leaf Cockroach",
            "White Eyed Assassin Bug"
        ],
        "spider_names": ["Green Lynx Spider", "Jumping Spider", "Crab Spider"]
    },
    "Praying mantises": {
        "insect_names": [
            "Emperor Scorpion", "Blue Death Feigning Beetle", "Red Eyed Assassin Bug",
            "Orchid Mantis", "Carolina Mantis", "Dead Leaf Mantis", "Giant Dead Leaf Mantis"
        ],
        "spider_names": ["Jumping Spider", "Crab Spider"]
    },
    "Beetles": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Blue Death Feigning Beetle",
            "Emerald Beetle", "Red Eyed Assassin Bug", "Rhinoceros Katydid",
            "Taxicab Beetle", "Magnificent Flower Beetle", "Giant African Millipede",
            "Jade Headed Buffalo Beetle"
        ],
        "spider_names": ["Green Lynx Spider", "Jumping Spider", "Crab Spider"]
    },
    "Ants": {
        "insect_names": [
            "Emperor Scorpion", "Blue Death Feigning Beetle", "Giant Spiney Leaf Insect",
            "Giant Walking Stick", "Leaf Cutting Ant", "Thorny Devil",
            "White Eyed Assassin Bug"
        ],
        "spider_names": ["Jumping Spider", "Crab Spider"]
    },
    "Dragonflies": {
        "insect_names": [
            "Emperor Scorpion", "Blue Death Feigning Beetle", "Red Eyed Assassin Bug"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Centipedes": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle"],
        "spider_names": ["Jumping Spider"]
    },
    "Scorpions": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle"],
        "spider_names": ["Jumping Spider"]
    },
    "Turtles": {
        "insect_names": [
            "Emperor Scorpion", "Giant Water Bug", "Sunburst Diving Beetle",
            "Water Scorpion"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Fish": {
        "insect_names": [
            "Emperor Scorpion", "Giant Water Bug", "Sunburst Diving Beetle",
            "Water Scorpion", "Water Strider"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Small mammals": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Carnivorous plants": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Blue Death Feigning Beetle"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Larger insects": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Domino Roach",
            "Magnificent Flower Beetle", "Thorny Devil", "Amazon Rainforest Giant Centipede",
            "Golden Tortoise Beetle"
        ],
        "spider_names": ["Jumping Spider", "Crab Spider"]
    },
    "Hedgehogs": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Hercules Beetle"],
        "spider_names": ["Jumping Spider"]
    },
    "Shrews": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Hissing Cockroach"],
        "spider_names": ["Jumping Spider"]
    },
    "Moles": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Hissing Cockroach"],
        "spider_names": ["Jumping Spider"]
    },
    "Squirrels": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Golden Tortoise Beetle"],
        "spider_names": ["Jumping Spider"]
    },
    "Foxes": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Grey Bird Grasshopper", "Red Eyed Assassin Bug"],
        "spider_names": ["Jumping Spider"]
    },
    "Snakes": {
        "insect_names": ["Emperor Scorpion", "Blue Death Feigning Beetle", "Grey Bird Grasshopper", "Red Eyed Assassin Bug"],
        "spider_names": ["Jumping Spider"]
    },
    "Mice": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Raccoons": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Skunks": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Weasels": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Owls": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Hawks": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    },
    "Vultures": {
        "insect_names": [
            "Emperor Scorpion", "American Burying Beetle", "Bat Cave Cockroach",
            "Domino Roach", "Eastern Lubber Grasshopper", "Hissing Cockroach",
            "Golden Tortoise Beetle", "Glowworm", "Regal Moth", "Velvet Ant"
        ],
        "spider_names": ["Jumping Spider"]
    }
}