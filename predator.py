class Predator: 
    def __init__ (self, name):
        self.name = name 

Predators = [
    Predator("Birds"),
    Predator("Bats"),
    Predator("Lizards"),
    Predator("Frogs"),
    Predator("Spiders"),
    Predator("Wasps"),
    Predator("Praying mantises"),
    Predator("Beetles"),
    Predator("Ants"),
    Predator("Dragonflies"),
    Predator("Centipedes"),
    Predator("Scorpions"),
    Predator("Turtles"),
    Predator("Fish"),
    Predator("Small mammals"),
    Predator("Carnivorous plants"),
    Predator("Larger insects"),
    Predator("Hedgehogs"),
    Predator("Shrews"),
    Predator("Moles"),
    Predator("Squirrels"),
    Predator("Foxes"),
    Predator("Snakes"),
    Predator("Mice"),
    Predator("Raccoons"),
    Predator("Skunks"),
    Predator("Weasels"),
    Predator("Owls"),
    Predator("Hawks"),
    Predator("Vultures")
]

predator_details = {
    predator.name: {

    }
    for predator in Predators
}
