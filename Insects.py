from data.model import AnimalFact

class Insect:
    def __init__(self, name, scientific_name, habitat, diet, behavior):
        self.name = name
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.facts = []

# Facts for insects
insect_facts = [
   "Insects are the largest group of animals on Earth.",
    "Insects play a vital role in pollination of plants.",
    "Insects have three body segments: head, thorax, and abdomen.",
    "Some insects can walk on water due to surface tension.",
    "The lifespan of insects varies widely, from a few hours to several years.",
    "Insects have a hard exoskeleton that provides protection and support.",
    "Some insects, like ants, live in complex social colonies with different roles.",
    "Insects have diverse feeding habits, including herbivores, carnivores, and scavengers.",
    "Many insects go through a process called metamorphosis, changing form as they grow.",
    "Insects communicate using various methods, such as pheromones and sounds.",
    "Insects have specialized sensory organs, such as antennae and compound eyes.",
    "The praying mantis is known for its unique hunting behavior and distinctive front legs.",
    "The silk produced by silkworms is used to make fabric and other products.",
    "Honeybees are important pollinators and produce honey as a food source.",
    "Some insects, like fireflies, produce light through a process called bioluminescence.",
    "Insects have been used in medicine and scientific research for various purposes.",
    "Insects are found in nearly every habitat on Earth, from rainforests to deserts.",
    "Certain insects, like termites, are considered pests due to their damage to structures.",
    "Butterflies are known for their vibrant colors and intricate wing patterns.",
    "Insects contribute to the decomposition of organic matter, recycling nutrients in ecosystems.",
]



# Sample insect data
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
    Insect("Brown Recluse", "Loxosceles reclusa", "United States", "Insects", "Nocturnal"),
    Insect("Cave Whip Spider", "Phrynus marginemaculatus", "Caves in North and South America", "Small insects", "Camouflaged"),
    Insect("Dead Leaf Mantis", "Deroplatys lobata", "Southeast Asia", "Insects", "Leaf mimic"),
    Insect("Zophobas Darkling Beetle", "Zophobas morio", "South America", "Decaying organic matter", "Burrowing"),
    Insect("Antilles Treespider", "Ancylometes bogotensis", "Central and South America", "Insects and small vertebrates", "Ambush predator"),
    Insect("Giant African Millipede", "Archispirostreptus gigas", "Africa", "Decaying organic matter", "Millipede"),
    Insect("Jade Headed Buffalo Beetle", "Eupatorus gracilicornis", "Southeast Asia", "Decaying wood", "Colorful"),
    Insect("Red Kneed Tarantula", "Brachypelma smithi", "Mexico", "Insects and small vertebrates", "Burrowing"),
    Insect("Brazilian White Knee Tarantula", "Acanthoscurria geniculata", "South America", "Insects and small vertebrates", "Burrowing"),
    Insect("Texas Bullet Ant", "Paraponera clavata", "South America", "Insects and nectar", "Painful sting"),
    Insect("Giant Cockroach", "Megacephala batesi", "Central and South America", "Decaying matter", "Nocturnal"),
    Insect("Dragon Headed Katydid", "Ephippiger ephippiger", "Europe", "Leaves", "Camouflaged"),
    Insect("Madagascar Hissing Cockroach", "Gromphadorhina portentosa", "Madagascar", "Decaying matter", "Hissing"),
    Insect("Giant Dead Leaf Mantis", "Deroplatys dessicata", "Southeast Asia", "Insects", "Leaf mimic"),
    Insect("Peruvian Firestick", "Oreophoetes peruana", "South America", "Decaying vegetation", "Bioluminescent"),
    Insect("Peppered Roach", "Archimandrita tesselata", "Central America", "Decaying matter", "Nocturnal"),
    Insect("Brazilian Salmon Pink Birdeater", "Lasiodora parahybana", "South America", "Insects and small vertebrates", "Burrowing"),
    Insect("Flordia Orb Weaver Spider", "Eriophora ravilla", "Southeastern United States", "Insects caught in webs", "Orb-weaver"),
]
    
# Populate insect facts
for insect, facts in zip(insects, insect_facts):
    insect.facts = [AnimalFact(fact=fact, insect=insect) for fact in facts]

# Insect details dictionary
insect_details = {
    insect.name: {
        "scientific_name": insect.scientific_name, 
        "habitat": insect.habitat,
        "diet": insect.diet, 
        "behavior": insect.behavior
    }
    for insect in insects
}
