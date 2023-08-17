from insects import Insect
from sqlalchemy import sessionmaker 

def display_insect_names(session):
    insects = session.query(Insect).all()
    print("Available Insects:")
    for insect in insects:
        print(insect.name)


##list of insects common name, science name, habitat, diet, behavior
Emperor_scorpion  = Insect("Emperor Scorpion", "Pandinus imperator", "West Africa", "Insectavore", "Docile")
American_burying_beetle = Insect("American Burying Beetle", "Nicrophorus americanus", "Central United States", "Insects and Carrion", "Nocturnal")
Bat_cave_cockroach = Insect("Bat Cave Cockroach", "Eublaberus distanti", "Trinidad", "Organic Debris", "Nocturnal")
Blue_death_feigning_beetle = Insect("Blue Death Feigning Beetle", "Asbolus verrucosus", "Southern United States", "decaying plant life", "death feiging")
Domino_roach = Insect()
Eastern_lubber_grasshopper = Insect()
Emerald_beetle = Insect()
Giant_jumping_stick = Insect()
Giant_spiney_leaf_insect = Insect()
Giant_walking_stick = Insect()
Giant_water_bug = Insect()
Green_leaf_cockroach = Insect()
Grey_bird_grasshopper = Insect()
Hissing_cockroach = Insect()
Leaf_cutting_ant = Insect()
Magnificent_flower_beetle = Insect()
Red_eyed_assassin_bug = Insect()
Rhinoceros_katydid = Insect()
Sunburst_diving_beetle = Insect()
Taxicab_beetle = Insect()
Thorny_devil = Insect()
Water_scorpion = Insect()
Water_strider = Insect()
White_eyed_assassin_bug = Insect()
Yellow_bellied_beetle = Insect()
Zebra_bug = Insect()
Orchid_mantis = Insect()
Carolina_mantis = Insect()
Brown_recluse = Insect()
Cave_whip_spider = Insect()
Dead_leaf_mantis = Insect()
Zophobas_darkling_beetle = Insect()
Antilles_treespider = Insect()
Giant_african_milipede = Insect()
Jade_headed_buffalo_beetle = Insect()
Red_kneed_tarantula = Insect()
Brazilian_white_knee_tarantula = Insect()
Texas_bullet_ant = Insect()
Giant_cockroach = Insect()
Dragon_headed_katydid = Insect()
Madagascar_hissing_cockroach = Insect()
Giant_dead_leaf_mantis = Insect()
Peruvian_firestick = Insect()
Peppered_roach = Insect()
Brazilian_salmon_pink_birdeater = Insect()
Flordia_orb_weaver_spider = Insect()
