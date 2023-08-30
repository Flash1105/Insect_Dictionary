class Insect:
    def __init__(self, name, scientific_name, habitat, diet, behavior, facts):
        self.name = name
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.facts = facts


insect_facts = [
    "Insects are the largest group of animals on Earth.",
    "Insects have a hard exoskeleton that provides protection and support.",
    "Insects play a vital role in pollinating plants.",
    "Insects can be found in a wide range of habitats, from forests to deserts.",
    "Insects go through metamorphosis, changing from egg to larva to pupa to adult."
]
# sample insect data
insects = [
    Insect("Emperor Scorpion", "Pandinus imperator", "West Africa", "Insectavore", "Docile", insect_facts),
    Insect("American Burying Beetle", "Nicrophorus americanus", "Central United States", "Insects and Carrion", "Nocturnal", insect_facts),
    Insect("Bat Cave Cockroach", "Eublaberus distanti", "Trinidad", "Organic Debris", "Nocturnal", insect_facts),
    Insect("Blue Death Feigning Beetle", "Asbolus verrucosus", "Southern United States", "Decaying plant life", "Death feigning",insect_facts),
    Insect("Domino Roach", "Polyphaga", "Various", "Scavenger", "Nocturnal",insect_facts),
    Insect("Eastern Lubber Grasshopper", "Romalea microptera", "Southeastern United States", "Plants", "Slow-moving",insect_facts),
    Insect("Emerald Beetle", "Chrysina spp.", "Central America", "Decaying wood", "Nocturnal",insect_facts),
    Insect("Giant Jumping Stick", "Leptynia attenuata", "North America", "Plants", "Jumping",insect_facts),
    Insect("Giant Spiney Leaf Insect", "Extatosoma tiaratum", "Australia", "Leaves", "Camouflaged",insect_facts),
    Insect("Giant Walking Stick", "Phobaeticus kirbyi", "Borneo", "Leaves", "Long legs",insect_facts),
    Insect("Giant Water Bug", "Lethocerus americanus", "North America", "Insects and Fish", "Aquatic",insect_facts),
    Insect("Green Leaf Cockroach", "Panchlora nivea", "Central and South America", "Decaying vegetation", "Flies",insect_facts),
    Insect("Grey Bird Grasshopper", "Schistocerca nitens", "Central and South America", "Plants", "Invasive",insect_facts),
    Insect("Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing",insect_facts),
    Insect("Leaf Cutting Ant", "Atta spp.", "Central and South America", "Fungus", "Colony builders",insect_facts),
    Insect("Magnificent Flower Beetle", "Eudicella gralli", "Africa", "Fruits and sap", "Colorful",insect_facts),
    Insect("Red Eyed Assassin Bug", "Pselliopus barberi", "Central and South America", "Insects", "Ambush predator",insect_facts),
    Insect("Rhinoceros Katydid", "Panacanthus cuspidatus", "Central and South America", "Leaves", "Camouflaged",insect_facts),
    Insect("Sunburst Diving Beetle", "Thermonectus marmoratus", "North America", "Insects and small fish", "Aquatic",insect_facts),
    Insect("Taxicab Beetle", "Palembus dermestoides", "South America", "Decaying matter", "Bright colors",insect_facts),
    Insect("Thorny Devil", "Moloch horridus", "Australia", "Plants", "Spiky",insect_facts),
    Insect("Water Scorpion", "Nepidae", "Worldwide", "Insects and small fish", "Aquatic",insect_facts),
    Insect("Water Strider", "Gerridae", "Worldwide", "Small insects", "Water walking",insect_facts),
    Insect("White Eyed Assassin Bug", "Platymeris biguttatus", "Africa", "Insects", "Predator",insect_facts),
    Insect("Yellow Bellied Beetle", "Cotinis nitida", "North America", "Fruit and Nector", "Shiny",insect_facts),
    Insect("Zebra Bug", "Oecophylla smaragdina", "Australia and Asia", "Decaying Matter", "Colony builders",insect_facts),
    Insect("Orchid Mantis", "Hymenopus coronatus", "Southeast Asia", "Insects", "Mimicry",insect_facts),
    Insect("Carolina Mantis", "Stagmomantis carolina", "North America", "Insects", "Ambush predator",insect_facts),
    Insect("Dead Leaf Mantis", "Deroplatys lobata", "Southeast Asia", "Insects", "Leaf mimic",insect_facts),
    Insect("Zophobas Darkling Beetle", "Zophobas morio", "South America", "Decaying organic matter", "Burrowing",insect_facts),
    Insect("Giant African Millipede", "Archispirostreptus gigas", "Africa", "Decaying organic matter", "Millipede",insect_facts),
    Insect("Jade Headed Buffalo Beetle", "Eupatorus gracilicornis", "Southeast Asia", "Decaying wood", "Colorful",insect_facts),
    Insect("Texas Bullet Ant", "Paraponera clavata", "South America", "Insects and nectar", "Painful sting",insect_facts),
    Insect("Giant Cockroach", "Megacephala batesi", "Central and South America", "Decaying matter", "Nocturnal",insect_facts),
    Insect("Dragon Headed Katydid", "Ephippiger ephippiger", "Europe", "Leaves", "Camouflaged",insect_facts),
    Insect("Madagascar Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing",insect_facts),
    Insect("Giant Dead Leaf Mantis", "Deroplatys dessicata", "Southeast Asia", "Insects", "Leaf mimic",insect_facts),
    Insect("Peruvian Firestick", "Oreophoetes peruana", "South America", "Decaying vegetation", "Bioluminescent",insect_facts),
    Insect("Peppered Roach", "Archimandrita tesselata", "Central America", "Decaying matter", "Nocturnal",insect_facts),
    Insect("African Goliath Beetle", "Goliathus spp.", "Africa", "Decaying wood", "Colorful",insect_facts),
    Insect("Amazon Rainforest Giant Centipede", "Scolopendra gigantea", "Amazon Rainforest", "Insects and small animals", "Predator",insect_facts),
    Insect("Golden Tortoise Beetle", "Charidotella sexpunctata", "North America", "Plants", "Camouflaged",insect_facts),
    Insect("Firefly", "Lampyridae", "Worldwide", "Nectar", "Bioluminescent",insect_facts),
    Insect("Harlequin Flower Beetle", "Acrocinus longimanus", "South America", "Decaying wood", "Colorful",insect_facts),
    Insect("Vietnamese Centipede", "Scolopendra subspinipes", "Vietnam", "Insects and small animals", "Predator",insect_facts),
    Insect("Metallic Jewel Beetle", "Buprestidae", "Worldwide", "Tree sap", "Shiny",insect_facts),
    Insect("Luna Moth", "Actias luna", "North America", "Nectar", "Nocturnal",insect_facts),
    Insect("Giant Isopod", "Bathynomus giganteus", "Deep sea", "Scavenger", "Aquatic",insect_facts),
    Insect("Leafcutter Bee", "Megachile spp.", "Worldwide", "Leaves", "Pollinator",insect_facts),
    Insect("Glowworm", "Arachnocampa spp.", "New Zealand", "Small insects", "Bioluminescent",insect_facts),
    Insect("Rainbow Shield Bug", "Calidea dregii", "Australia", "Plants", "Colorful",insect_facts),
    Insect("Titan Beetle", "Titanus giganteus", "South America", "Decaying wood", "Massive",insect_facts),
    Insect("Velvet Ant", "Mutillidae", "Worldwide", "Nectar", "Nocturnal",insect_facts),
    Insect("Atlas Moth", "Attacus atlas", "Southeast Asia", "Nectar", "Nocturnal",insect_facts),
    Insect("Hercules Beetle", "Dynastes hercules", "Central and South America", "Tree sap", "Strong",insect_facts),
    Insect("Thorn Bug", "Umbonia crassicornis", "Central and South America", "Plants", "Camouflaged",insect_facts),
    Insect("Regal Moth", "Citheronia regalis", "North America", "Nectar", "Nocturnal",insect_facts),
    Insect("Mantis Shrimp", "Stomatopoda", "Tropical oceans", "Small animals", "Aquatic",insect_facts),
    Insect("Morpho Butterfly", "Morpho spp.", "Central and South America", "Nectar", "Colorful",insect_facts),
    Insect("Ladybug", "Coccinellidae", "Worldwide", "Aphids", "Beneficial",insect_facts),
    Insect("Leafhopper", "Cicadellidae", "Worldwide", "Plants", "Jumping",insect_facts),
    Insect("Fire Ant", "Solenopsis spp.", "Worldwide", "Insects and plants", "Aggressive",insect_facts),
    Insect("Katydid", "Tettigoniidae", "Worldwide", "Leaves", "Camouflaged",insect_facts),
    Insect("Honey Bee", "Apis mellifera", "Worldwide", "Nectar", "Pollinator",insect_facts),
    Insect("Webspinner", "Embioptera", "Tropical and temperate regions", "Decaying plant material", "Silk-producing",insect_facts),
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