class Spider: 
    def __init__ (self, name, sceintific_name, habitat, diet, behavior, venomous):
        self.name = name 
        self.sceitific_name = sceintific_name
        self.habitat = habitat
        self.diet = diet
        self.behavior = behavior
        self.venomous = venomous

spiders = [
        Spider("Black Widow", "Latrodectuss spp.", "Worldwide", "Insects", "Venomous", True),
        Spider("Wolf Spider", "Lycosidae", "Worldwide", "Insects and small vertebrates", "Hunting", False),
        Spider("Golden Silk Orb Weaver", "Nephila spp.", "Tropical regions", "Flying insects", "Orb-weaver", False),
        Spider("Brown Widow", "Latrodectus geometricus", "Worldwide", "Insects", "Venomous", True),
        Spider("Brazilian Wandering Spider", "Phoneutria spp.", "South America", "Insects and small vertebrates", "Active hunter", True),
        Spider("Trapdoor Spider", "Ctenizidae", "Worldwide", "Insects and small vertebrates", "Ambush predator", False),
        Spider("Fishing Spider", "Dolomedes spp.", "North and South America", "Aquatic insects and small fish", "Semi-aquatic", False),
        Spider("Goliath Birdeater", "Theraphosa blondi", "South America", "Insects and small vertebrates", "Burrowing", False),
        Spider("Redback Spider", "Latrodectus hasselti", "Australia", "Insects", "Venomous", True),
        Spider("Camel Spider", "Solifugae", "Arid regions", "Insects and small vertebrates", "Fast runner", False),
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