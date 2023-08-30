class Spider: 
    def __init__ (self, name, scientific_name, habitat, diet, behavior, venomous):
        self.name = name 
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.venomous = venomous

spiders = [
    Spider("Black Widow", "Latrodectus spp.", "Worldwide", "Insects", "Nonaggressive", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Wolf Spider", "Lycosidae", "Worldwide", "Insects and small vertebrates", "Hunting", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Golden Silk Orb Weaver", "Nephila spp.", "Tropical regions", "Flying insects", "Orb-weaver", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Brown Widow", "Latrodectus geometricus", "Worldwide", "Insects", "Venomous", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Brazilian Wandering Spider", "Phoneutria spp.", "South America", "Insects and small vertebrates", "Active hunter", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Trapdoor Spider", "Ctenizidae", "Worldwide", "Insects and small vertebrates", "Ambush predator", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Fishing Spider", "Dolomedes spp.", "North and South America", "Aquatic insects and small fish", "Semi-aquatic", False, ["Birds", "Lizards", "Fish", "Aquatic insects"]),
    Spider("Goliath Birdeater", "Theraphosa blondi", "South America", "Insects and small vertebrates", "Burrowing", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Redback Spider", "Latrodectus hasselti", "Australia", "Insects", "Venomous", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Camel Spider", "Solifugae", "Arid regions", "Insects and small vertebrates", "Fast runner", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Green Lynx Spider", "Peucetia viridans", "North and Central America", "Insects", "Ambush predator", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Six-Eyed Sand Spider", "Sicarius spp.", "Desert regions", "Insects and small arthropods", "Burrowing", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Spiny Orb Weaver", "Gasteracantha spp.", "Tropical and subtropical regions", "Flying insects", "Orb-weaver", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Bird-Dropping Spider", "Celaenia spp.", "Australia", "Flying insects", "Camouflage", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Mouse Spider", "Missulena spp.", "Australia", "Insects", "Venomous", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Net-Casting Spider", "Deinopidae", "Tropical and subtropical regions", "Small insects", "Web casting", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Tarantula Hawk Spider", "Pompilidae", "South Africa", "Hunts tarantulas", "Parasitic", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Woodlouse Hunter", "Dysdera crocata", "Europe and North America", "Woodlice", "Hunting", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Jumping Spider", "Salticidae", "Worldwide", "Small insects", "Jumping", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Crab Spider", "Thomisidae", "Worldwide", "Insects", "Ambush predator", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Tube Web Spider", "Segestriidae", "Worldwide", "Insects", "Web-dwelling", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Huntsman Spider", "Sparassidae", "Worldwide", "Insects and small vertebrates", "Hunting", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Australian Funnel-Web Spider", "Atracidae", "Australia", "Insects and small vertebrates", "Venomous", True, ["Birds", "Lizards", "Other insects"]),
    Spider("Spitting Spider", "Scytodidae", "Worldwide", "Small insects", "Web-spitting", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Socotra Island Blue Baboon Spider", "Monocentropus balfouri", "Socotra Island", "Insects", "Burrowing", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Red Trapdoor Spider", "Stasimopus robertsoni", "South Africa", "Insects and small vertebrates", "Ambush predator", False, ["Birds", "Lizards", "Other insects"]),
    Spider("Ghost Spider", "Anyphaenidae", "Worldwide", "Insects", "Camouflage", False, ["Birds", "Lizards", "Other insects"]),
]


spider_details = {
    spider.name: {
        "scientific_name": spider.scientific_name, 
        "habitat": spider.habitat, 
        "diet": spider.diet,
        "behavior": spider.behavior,
        "venomous": spider.venomous

    }
    for spider in spiders
}