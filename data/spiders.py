class Spider: 
    def __init__ (self, name, scientific_name, habitat, diet, behavior, venomous, facts):
        self.name = name 
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.venomous = venomous
        self.facts = facts


spider_facts = [
    "Spiders are arachnids, not insects, and have eight legs.",
    "Spiders produce silk from special glands, which they use to build webs.",
    "Most spiders are venomous, using their venom to paralyze or kill their prey.",
    "Spiders are found worldwide and occupy various habitats.",
    "Some spiders are known for their unique behaviors, such as mimicry and jumping."
]

Spiders = [
    Spider("Black Widow", "Latrodectus spp.", "Worldwide", "Insects", "Nonaggressive", True, spider_facts),
    Spider("Wolf Spider", "Lycosidae", "Worldwide", "Insects and small vertebrates", "Hunting", False,spider_facts),
    Spider("Golden Silk Orb Weaver", "Nephila spp.", "Tropical regions", "Flying insects", "Orb-weaver", False,spider_facts),
    Spider("Brown Widow", "Latrodectus geometricus", "Worldwide", "Insects", "Venomous", True,spider_facts),
    Spider("Brazilian Wandering Spider", "Phoneutria spp.", "South America", "Insects and small vertebrates", "Active hunter", True,spider_facts),
    Spider("Trapdoor Spider", "Ctenizidae", "Worldwide", "Insects and small vertebrates", "Ambush predator", False,spider_facts),
    Spider("Fishing Spider", "Dolomedes spp.", "North and South America", "Aquatic insects and small fish", "Semi-aquatic", False,spider_facts),
    Spider("Goliath Birdeater", "Theraphosa blondi", "South America", "Insects and small vertebrates", "Burrowing", False,spider_facts),
    Spider("Redback Spider", "Latrodectus hasselti", "Australia", "Insects", "Venomous", True,spider_facts),
    Spider("Camel Spider", "Solifugae", "Arid regions", "Insects and small vertebrates", "Fast runner", False,spider_facts),
    Spider("Green Lynx Spider", "Peucetia viridans", "North and Central America", "Insects", "Ambush predator", False,spider_facts),
    Spider("Six-Eyed Sand Spider", "Sicarius spp.", "Desert regions", "Insects and small arthropods", "Burrowing", True,spider_facts),
    Spider("Spiny Orb Weaver", "Gasteracantha spp.", "Tropical and subtropical regions", "Flying insects", "Orb-weaver", False,spider_facts),
    Spider("Bird-Dropping Spider", "Celaenia spp.", "Australia", "Flying insects", "Camouflage", False,spider_facts),
    Spider("Mouse Spider", "Missulena spp.", "Australia", "Insects", "Venomous", True,spider_facts),
    Spider("Net-Casting Spider", "Deinopidae", "Tropical and subtropical regions", "Small insects", "Web casting", False,spider_facts),
    Spider("Tarantula Hawk Spider", "Pompilidae", "South Africa", "Hunts tarantulas", "Parasitic", False,spider_facts),
    Spider("Woodlouse Hunter", "Dysdera crocata", "Europe and North America", "Woodlice", "Hunting", False,spider_facts),
    Spider("Jumping Spider", "Salticidae", "Worldwide", "Small insects", "Jumping", False,spider_facts),
    Spider("Crab Spider", "Thomisidae", "Worldwide", "Insects", "Ambush predator", False,spider_facts),
    Spider("Tube Web Spider", "Segestriidae", "Worldwide", "Insects", "Web-dwelling", False,spider_facts),
    Spider("Huntsman Spider", "Sparassidae", "Worldwide", "Insects and small vertebrates", "Hunting", False,spider_facts),
    Spider("Australian Funnel-Web Spider", "Atracidae", "Australia", "Insects and small vertebrates", "Venomous", True,spider_facts),
    Spider("Spitting Spider", "Scytodidae", "Worldwide", "Small insects", "Web-spitting", False,spider_facts),
    Spider("Socotra Island Blue Baboon Spider", "Monocentropus balfouri", "Socotra Island", "Insects", "Burrowing", False,spider_facts),
    Spider("Red Trapdoor Spider", "Stasimopus robertsoni", "South Africa", "Insects and small vertebrates", "Ambush predator", False,spider_facts),
    Spider("Ghost Spider", "Anyphaenidae", "Worldwide", "Insects", "Camouflage", False,spider_facts),
]


spider_details = {
    spider.name: {
        "scientific_name": spider.scientific_name, 
        "habitat": spider.habitat, 
        "diet": spider.diet,
        "behavior": spider.behavior,
        "venomous": spider.venomous

    }
    for spider in Spiders
}