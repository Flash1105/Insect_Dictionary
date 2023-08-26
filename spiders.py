class Spider: 
    def __init__ (self, name, scientific_name, habitat, diet, behavior, venomous):
        self.name = name 
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.venomous = venomous

Spiders = [
    Spider("Black Widow", "Latrodectus spp.", "Worldwide", "Insects", "Venomous", True),
    Spider("Wolf Spider", "Lycosidae", "Worldwide", "Insects and small vertebrates", "Hunting", False),
    Spider("Golden Silk Orb Weaver", "Nephila spp.", "Tropical regions", "Flying insects", "Orb-weaver", False),
    Spider("Brown Widow", "Latrodectus geometricus", "Worldwide", "Insects", "Venomous", True),
    Spider("Brazilian Wandering Spider", "Phoneutria spp.", "South America", "Insects and small vertebrates", "Active hunter", True),
    Spider("Trapdoor Spider", "Ctenizidae", "Worldwide", "Insects and small vertebrates", "Ambush predator", False),
    Spider("Fishing Spider", "Dolomedes spp.", "North and South America", "Aquatic insects and small fish", "Semi-aquatic", False),
    Spider("Goliath Birdeater", "Theraphosa blondi", "South America", "Insects and small vertebrates", "Burrowing", False),
    Spider("Redback Spider", "Latrodectus hasselti", "Australia", "Insects", "Venomous", True),
    Spider("Camel Spider", "Solifugae", "Arid regions", "Insects and small vertebrates", "Fast runner", False),
    Spider("Green Lynx Spider", "Peucetia viridans", "North and Central America", "Insects", "Ambush predator", False),
    Spider("Six-Eyed Sand Spider", "Sicarius spp.", "Desert regions", "Insects and small arthropods", "Burrowing", True),
    Spider("Spiny Orb Weaver", "Gasteracantha spp.", "Tropical and subtropical regions", "Flying insects", "Orb-weaver", False),
    Spider("Bird-Dropping Spider", "Celaenia spp.", "Australia", "Flying insects", "Camouflage", False),
    Spider("Mouse Spider", "Missulena spp.", "Australia", "Insects", "Venomous", True),
    Spider("Net-Casting Spider", "Deinopidae", "Tropical and subtropical regions", "Small insects", "Web casting", False),
    Spider("Tarantula Hawk Spider", "Pompilidae", "South Africa", "Hunts tarantulas", "Parasitic", False),
    Spider("Woodlouse Hunter", "Dysdera crocata", "Europe and North America", "Woodlice", "Hunting", False),
    Spider("Jumping Spider", "Salticidae", "Worldwide", "Small insects", "Jumping", False),
    Spider("Crab Spider", "Thomisidae", "Worldwide", "Insects", "Ambush predator", False),
    Spider("Tube Web Spider", "Segestriidae", "Worldwide", "Insects", "Web-dwelling", False),
    Spider("Huntsman Spider", "Sparassidae", "Worldwide", "Insects and small vertebrates", "Hunting", False),
    Spider("Australian Funnel-Web Spider", "Atracidae", "Australia", "Insects and small vertebrates", "Venomous", True),
    Spider("Spitting Spider", "Scytodidae", "Worldwide", "Small insects", "Web-spitting", False),
    Spider("Socotra Island Blue Baboon Spider", "Monocentropus balfouri", "Socotra Island", "Insects", "Burrowing", False),
    Spider("Red Trapdoor Spider", "Stasimopus robertsoni", "South Africa", "Insects and small vertebrates", "Ambush predator", False),
    Spider("Ghost Spider", "Anyphaenidae", "Worldwide", "Insects", "Camouflage", False),
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