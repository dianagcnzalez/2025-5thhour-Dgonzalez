#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
EnemyCreatures = {
    "Enemy1" : {
        "Name": "Mardi",
        "Power": "Invisibility",
        "Damage": 15
    },
    "Enemy2": {
        "Name": "Morris",
        "Power": "teleportation",
        "Damage": 55
    },
    "Enemy3": {
        "Name": "Phoenix",
        "Power": "Telekinesis",
        "Damage": 100
    },
    "Enemy4": {
        "Name": "Judas",
        "Power": "shapeshifting",
        "Damage": 105
    },
    "Enemy5":{
        "Name": "Mack",
        "Power": "Time traveler",
        "Damage": 256
    },
}
EnemyCreatures["Enemy1"]["Damage"] = int(input("Enemy1 Damage: "))
print (EnemyCreatures["Enemy1"])

EnemyCreatures["Enemy2"]["Damage"] = int(input("Enemy2 Damage: "))
print (EnemyCreatures["Enemy2"])

EnemyCreatures["Enemy3"]["Damage"] = int(input("Enemy3 Damage: "))
print (EnemyCreatures["Enemy3"])

EnemyCreatures["Enemy4"]["Damage"] = int(input("Enemy4 Damage: "))
print (EnemyCreatures["Enemy4"])

EnemyCreatures["Enemy5"]["Damage"] = int(input("Enemy5 Damage: "))
print (EnemyCreatures["Enemy5"])