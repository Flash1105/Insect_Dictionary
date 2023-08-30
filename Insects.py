class Insect:
    def __init__(self, name, scientific_name, habitat, diet, behavior):
        self.name = name
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior

# sample insect data
insects = [
    Insect("Emperor Scorpion", "Pandinus imperator", "West Africa", "Insectavore", "Docile"),
    Insect("American Burying Beetle", "Nicrophorus americanus", "Central United States", "Insects and Carrion", "Nocturnal"),
    Insect("Bat Cave Cockroach", "Eublaberus distanti", "Trinidad", "Organic Debris", "Nocturnal"),
    Insect("Blue Death Feigning Beetle", "Asbolus verrucosus", "Southern United States", "Decaying plant life", "Death feigning"),
    Insect("Domino Roach", "Polyphaga", "Various", "Scavenger", "Nocturnal"),
    Insect("Eastern Lubber Grasshopper", "Romalea microptera", "Southeastern United States", "Plants", "Slow-moving"),
    Insect("Emerald Beetle", "Chrysina spp.", "Central America", "Decaying wood", "Nocturnal"),
    Insect("Giant Jumping Stick", "Leptynia attenuata", "North America", "Plants", "Jumping"),
    Insect("Giant Spiney Leaf Insect", "Extatosoma tiaratum", "Australia", "Leaves", "Camouflaged"),
    Insect("Giant Walking Stick", "Phobaeticus kirbyi", "Borneo", "Leaves", "Long legs"),
    Insect("Giant Water Bug", "Lethocerus americanus", "North America", "Insects and Fish", "Aquatic"),
    Insect("Green Leaf Cockroach", "Panchlora nivea", "Central and South America", "Decaying vegetation", "Flies"),
    Insect("Grey Bird Grasshopper", "Schistocerca nitens", "Central and South America", "Plants", "Invasive"),
    Insect("Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing"),
    Insect("Leaf Cutting Ant", "Atta spp.", "Central and South America", "Fungus", "Colony builders"),
    Insect("Magnificent Flower Beetle", "Eudicella gralli", "Africa", "Fruits and sap", "Colorful"),
    Insect("Red Eyed Assassin Bug", "Pselliopus barberi", "Central and South America", "Insects", "Ambush predator"),
    Insect("Rhinoceros Katydid", "Panacanthus cuspidatus", "Central and South America", "Leaves", "Camouflaged"),
    Insect("Sunburst Diving Beetle", "Thermonectus marmoratus", "North America", "Insects and small fish", "Aquatic"),
    Insect("Taxicab Beetle", "Palembus dermestoides", "South America", "Decaying matter", "Bright colors"),
    Insect("Thorny Devil", "Moloch horridus", "Australia", "Ants", "Spiky"),
    Insect("Water Scorpion", "Nepidae", "Worldwide", "Insects and small fish", "Aquatic"),
    Insect("Water Strider", "Gerridae", "Worldwide", "Small insects", "Water walking"),
    Insect("White Eyed Assassin Bug", "Platymeris biguttatus", "Africa", "Insects", "Predator"),
    Insect("Yellow Bellied Beetle", "Cotinis nitida", "North America", "Fruit and sap", "Shiny"),
    Insect("Zebra Bug", "Oecophylla smaragdina", "Australia and Asia", "Decaying Matter", "Colony builders"),
    Insect("Orchid Mantis", "Hymenopus coronatus", "Southeast Asia", "Insects", "Mimicry"),
    Insect("Carolina Mantis", "Stagmomantis carolina", "North America", "Insects", "Ambush predator"),
    Insect("Dead Leaf Mantis", "Deroplatys lobata", "Southeast Asia", "Insects", "Leaf mimic"),
    Insect("Zophobas Darkling Beetle", "Zophobas morio", "South America", "Decaying organic matter", "Burrowing"),
    Insect("Giant African Millipede", "Archispirostreptus gigas", "Africa", "Decaying organic matter", "Millipede"),
    Insect("Jade Headed Buffalo Beetle", "Eupatorus gracilicornis", "Southeast Asia", "Decaying wood", "Colorful"),
    Insect("Texas Bullet Ant", "Paraponera clavata", "South America", "Insects and nectar", "Painful sting"),
    Insect("Giant Cockroach", "Megacephala batesi", "Central and South America", "Decaying matter", "Nocturnal"),
    Insect("Dragon Headed Katydid", "Ephippiger ephippiger", "Europe", "Leaves", "Camouflaged"),
    Insect("Madagascar Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing"),
    Insect("Giant Dead Leaf Mantis", "Deroplatys dessicata", "Southeast Asia", "Insects", "Leaf mimic"),
    Insect("Peruvian Firestick", "Oreophoetes peruana", "South America", "Decaying vegetation", "Bioluminescent"),
    Insect("Peppered Roach", "Archimandrita tesselata", "Central America", "Decaying matter", "Nocturnal"),
    Insect("African Goliath Beetle", "Goliathus spp.", "Africa", "Decaying wood", "Colorful"),
    Insect("Amazon Rainforest Giant Centipede", "Scolopendra gigantea", "Amazon Rainforest", "Insects and small animals", "Predator"),
    Insect("Golden Tortoise Beetle", "Charidotella sexpunctata", "North America", "Plants", "Camouflaged"),
    Insect("Firefly", "Lampyridae", "Worldwide", "Nectar", "Bioluminescent"),
    Insect("Harlequin Flower Beetle", "Acrocinus longimanus", "South America", "Decaying wood", "Colorful"),
    Insect("Vietnamese Centipede", "Scolopendra subspinipes", "Vietnam", "Insects and small animals", "Predator"),
    Insect("Metallic Jewel Beetle", "Buprestidae", "Worldwide", "Tree sap", "Shiny"),
    Insect("Luna Moth", "Actias luna", "North America", "Nectar", "Nocturnal"),
    Insect("Giant Isopod", "Bathynomus giganteus", "Deep sea", "Scavenger", "Aquatic"),
    Insect("Leafcutter Bee", "Megachile spp.", "Worldwide", "Leaves", "Pollinator"),
    Insect("Glowworm", "Arachnocampa spp.", "New Zealand", "Small insects", "Bioluminescent"),
    Insect("Rainbow Shield Bug", "Calidea dregii", "Australia", "Plants", "Colorful"),
    Insect("Titan Beetle", "Titanus giganteus", "South America", "Decaying wood", "Massive"),
    Insect("Velvet Ant", "Mutillidae", "Worldwide", "Nectar", "Nocturnal"),
    Insect("Atlas Moth", "Attacus atlas", "Southeast Asia", "Nectar", "Nocturnal"),
    Insect("Hercules Beetle", "Dynastes hercules", "Central and South America", "Tree sap", "Strong"),
    Insect("Thorn Bug", "Umbonia crassicornis", "Central and South America", "Plants", "Camouflaged"),
    Insect("Regal Moth", "Citheronia regalis", "North America", "Nectar", "Nocturnal"),
    Insect("Mantis Shrimp", "Stomatopoda", "Tropical oceans", "Small animals", "Aquatic"),
    Insect("Morpho Butterfly", "Morpho spp.", "Central and South America", "Nectar", "Colorful"),
    Insect("Ladybug", "Coccinellidae", "Worldwide", "Aphids", "Beneficial"),
    Insect("Leafhopper", "Cicadellidae", "Worldwide", "Plants", "Jumping"),
    Insect("Fire Ant", "Solenopsis spp.", "Worldwide", "Insects and plants", "Aggressive"),
    Insect("Katydid", "Tettigoniidae", "Worldwide", "Leaves", "Camouflaged"),
    Insect("Honey Bee", "Apis mellifera", "Worldwide", "Nectar", "Pollinator"),
    Insect("Webspinner", "Embioptera", "Tropical and temperate regions", "Decaying plant material", "Silk-producing"),
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