class Insect:
    def __init__(self, name, scientific_name, habitat, diet, behavior, predators=None):
        self.name = name
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.predators = predators if predators is not None else []
# sample insect data
insects = [
    Insect("Emperor Scorpion", "Pandinus imperator", "West Africa", "Insectavore", "Docile", ["Birds", "Bats", "Lizards", "Frogs", "Spiders", "Wasps", "Praying mantises", "Beetles", "Ants", "Dragonflies", "Centipedes", "Scorpions", "Turtles", "Fish", "Small mammals", "Carnivorous plants", "Larger insects", "Hedgehogs", "Shrews", "Moles", "Squirrels", "Foxes", "Snakes", "Mice", "Raccoons", "Skunks", "Weasels", "Owls", "Hawks", "Vultures"]),
    Insect("American Burying Beetle", "Nicrophorus americanus", "Central United States", "Insects and Carrion", "Nocturnal", ["Carnivorous plants", "Larger insects", "Small mammals", "Raccoons", "Skunks", "Weasels"]),
    Insect("Bat Cave Cockroach", "Eublaberus distanti", "Trinidad", "Organic Debris", "Nocturnal", ["Bats", "Spiders", "Small mammals"]),
    Insect("Blue Death Feigning Beetle", "Asbolus verrucosus", "Southern United States", "Decaying plant life", "Death feigning", ["Predator", "Centipedes", "Scorpions"]),
    Insect("Domino Roach", "Polyphaga", "Various", "Scavenger", "Nocturnal", ["Larger insects", "Small mammals"]),
    Insect("Eastern Lubber Grasshopper", "Romalea microptera", "Southeastern United States", "Plants", "Slow-moving", ["Birds", "Lizards", "Small mammals"]),
    Insect("Emerald Beetle", "Chrysina spp.", "Central America", "Decaying wood", "Nocturnal", ["Bats", "Spiders"]),
    Insect("Giant Jumping Stick", "Leptynia attenuata", "North America", "Plants", "Jumping", ["Birds", "Lizards"]),
    Insect("Giant Spiney Leaf Insect", "Extatosoma tiaratum", "Australia", "Leaves", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Giant Walking Stick", "Phobaeticus kirbyi", "Borneo", "Leaves", "Long legs", ["Birds", "Lizards"]),
    Insect("Giant Water Bug", "Lethocerus americanus", "North America", "Insects and Fish", "Aquatic", ["Fish", "Turtles"]),
    Insect("Green Leaf Cockroach", "Panchlora nivea", "Central and South America", "Decaying vegetation", "Flies", ["Birds", "Lizards", "Praying mantises", "Ants"]),
    Insect("Grey Bird Grasshopper", "Schistocerca nitens", "Central and South America", "Plants", "Invasive", ["Birds", "Lizards"]),
    Insect("Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing", ["Lizards", "Small mammals"]),
    Insect("Leaf Cutting Ant", "Atta spp.", "Central and South America", "Fungus", "Colony builders", ["Ants"]),
    Insect("Magnificent Flower Beetle", "Eudicella gralli", "Africa", "Fruits and sap", "Colorful", ["Birds", "Lizards"]),
    Insect("Red Eyed Assassin Bug", "Pselliopus barberi", "Central and South America", "Insects", "Ambush predator", ["Birds", "Lizards", "Praying mantises", "Beetles", "Dragonflies"]),
    Insect("Rhinoceros Katydid", "Panacanthus cuspidatus", "Central and South America", "Leaves", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Sunburst Diving Beetle", "Thermonectus marmoratus", "North America", "Insects and small fish", "Aquatic", ["Fish", "Turtles"]),
    Insect("Taxicab Beetle", "Palembus dermestoides", "South America", "Decaying matter", "Bright colors", ["Birds", "Lizards"]),
    Insect("Thorny Devil", "Moloch horridus", "Australia", "Ants", "Spiky", ["Birds", "Lizards"]),
    Insect("Water Scorpion", "Nepidae", "Worldwide", "Insects and small fish", "Aquatic", ["Fish", "Turtles"]),
    Insect("Water Strider", "Gerridae", "Worldwide", "Small insects", "Water walking", ["Fish", "Turtles"]),
    Insect("White Eyed Assassin Bug", "Platymeris biguttatus", "Africa", "Insects", "Predator", ["Birds", "Lizards", "Spiders", "Wasps"]),
    Insect("Yellow Bellied Beetle", "Cotinis nitida", "North America", "Fruit and sap", "Shiny", ["Birds", "Lizards"]),
    Insect("Zebra Bug", "Oecophylla smaragdina", "Australia and Asia", "Decaying Matter", "Colony builders", ["Birds", "Lizards"]),
    Insect("Orchid Mantis", "Hymenopus coronatus", "Southeast Asia", "Insects", "Mimicry", ["Birds", "Lizards", "Praying mantises"]),
    Insect("Carolina Mantis", "Stagmomantis carolina", "North America", "Insects", "Ambush predator", ["Birds", "Lizards", "Praying mantises"]),
    Insect("Dead Leaf Mantis", "Deroplatys lobata", "Southeast Asia", "Insects", "Leaf mimic", ["Birds", "Lizards", "Praying mantises"]),
    Insect("Zophobas Darkling Beetle", "Zophobas morio", "South America", "Decaying organic matter", "Burrowing", ["Birds", "Lizards"]),
    Insect("Giant African Millipede", "Archispirostreptus gigas", "Africa", "Decaying organic matter", "Millipede", ["Birds", "Lizards"]),
    Insect("Jade Headed Buffalo Beetle", "Eupatorus gracilicornis", "Southeast Asia", "Decaying wood", "Colorful", ["Birds", "Lizards"]),
    Insect("Texas Bullet Ant", "Paraponera clavata", "South America", "Insects and nectar", "Painful sting", ["Birds", "Lizards"]),
    Insect("Giant Cockroach", "Megacephala batesi", "Central and South America", "Decaying matter", "Nocturnal", ["Birds", "Lizards"]),
    Insect("Dragon Headed Katydid", "Ephippiger ephippiger", "Europe", "Leaves", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Madagascar Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing", ["Lizards", "Small mammals"]),
    Insect("Giant Dead Leaf Mantis", "Deroplatys dessicata", "Southeast Asia", "Insects", "Leaf mimic", ["Birds", "Lizards", "Praying mantises"]),
    Insect("Peruvian Firestick", "Oreophoetes peruana", "South America", "Decaying vegetation", "Bioluminescent", ["Birds", "Lizards"]),
    Insect("Peppered Roach", "Archimandrita tesselata", "Central America", "Decaying matter", "Nocturnal", ["Birds", "Lizards"]),
    Insect("African Goliath Beetle", "Goliathus spp.", "Africa", "Decaying wood", "Colorful", ["Birds", "Lizards"]),
    Insect("Amazon Rainforest Giant Centipede", "Scolopendra gigantea", "Amazon Rainforest", "Insects and small animals", "Predator", ["Birds", "Lizards"]),
    Insect("Golden Tortoise Beetle", "Charidotella sexpunctata", "North America", "Plants", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Firefly", "Lampyridae", "Worldwide", "Nectar", "Bioluminescent", ["Birds", "Bats", "Lizards", "Frogs", "Spiders", "Wasps", "Praying mantises", "Beetles", "Dragonflies", "Centipedes", "Scorpions", "Turtles", "Fish", "Small mammals", "Carnivorous plants", "Larger insects", "Hedgehogs", "Shrews", "Moles", "Squirrels", "Foxes", "Snakes", "Mice", "Raccoons", "Skunks", "Weasels", "Owls", "Hawks", "Vultures"]),
    Insect("Harlequin Flower Beetle", "Acrocinus longimanus", "South America", "Decaying wood", "Colorful", ["Birds", "Lizards"]),
    Insect("Vietnamese Centipede", "Scolopendra subspinipes", "Vietnam", "Insects and small animals", "Predator", ["Birds", "Lizards"]),
    Insect("Metallic Jewel Beetle", "Buprestidae", "Worldwide", "Tree sap", "Shiny", ["Birds", "Lizards"]),
    Insect("Luna Moth", "Actias luna", "North America", "Nectar", "Nocturnal", ["Birds", "Bats"]),
    Insect("Giant Isopod", "Bathynomus giganteus", "Deep sea", "Scavenger", "Aquatic", ["Fish"]),
    Insect("Leafcutter Bee", "Megachile spp.", "Worldwide", "Leaves", "Pollinator", ["Birds", "Lizards"]),
    Insect("Glowworm", "Arachnocampa spp.", "New Zealand", "Small insects", "Bioluminescent", ["Birds"]),
    Insect("Rainbow Shield Bug", "Calidea dregii", "Australia", "Plants", "Colorful", ["Birds"]),
    Insect("Titan Beetle", "Titanus giganteus", "South America", "Decaying wood", "Massive", ["Birds", "Lizards"]),
    Insect("Velvet Ant", "Mutillidae", "Worldwide", "Nectar", "Nocturnal", ["Birds", "Lizards"]),
    Insect("Atlas Moth", "Attacus atlas", "Southeast Asia", "Nectar", "Nocturnal", ["Birds", "Bats"]),
    Insect("Hercules Beetle", "Dynastes hercules", "Central and South America", "Tree sap", "Strong", ["Birds", "Lizards"]),
    Insect("Thorn Bug", "Umbonia crassicornis", "Central and South America", "Plants", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Regal Moth", "Citheronia regalis", "North America", "Nectar", "Nocturnal", ["Birds", "Bats"]),
    Insect("Mantis Shrimp", "Stomatopoda", "Tropical oceans", "Small animals", "Aquatic", ["Fish"]),
    Insect("Morpho Butterfly", "Morpho spp.", "Central and South America", "Nectar", "Colorful", ["Birds", "Lizards"]),
    Insect("Ladybug", "Coccinellidae", "Worldwide", "Aphids", "Beneficial", ["Birds"]),
    Insect("Leafhopper", "Cicadellidae", "Worldwide", "Plants", "Jumping", ["Birds", "Lizards"]),
    Insect("Fire Ant", "Solenopsis spp.", "Worldwide", "Insects and plants", "Aggressive", ["Birds"]),
    Insect("Katydid", "Tettigoniidae", "Worldwide", "Leaves", "Camouflaged", ["Birds", "Lizards"]),
    Insect("Honey Bee", "Apis mellifera", "Worldwide", "Nectar", "Pollinator", ["Birds"]),
    Insect("Webspinner", "Embioptera", "Tropical and temperate regions", "Decaying plant material", "Silk-producing", ["Birds", "Lizards"]),
]

#Insect details dictionary
insect_details = {
    insect.name: {
        "scientific_name": insect.scientific_name, 
        "habitat": insect.habitat,
        "diet": insect.diet, 
        "behavior": insect.behavior
    }
    for insect in insects
}