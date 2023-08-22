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

]

spider_details = {
    spider.name: {
        "sceintific_name": spider.sceintific_name, 
        "habitat": spider.habitat, 
        "diet": spider.diet,
        "behavior": spider.behavior,
        "venomous": spider.venomous

    }
    for spider in spiders
}