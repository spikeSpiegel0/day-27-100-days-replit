import random, os, time

def character():
  name = input("Name Your Legend: ")
  print()
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return name

def healthStats():
  six_sided_roll = random.randint(1,6)
  twelve_sided_roll = random.randint(1,12)
  healthStat = int(round((six_sided_roll*twelve_sided_roll)/2+10,0))
  return healthStat

def strenghtStats():
  six_sided_roll = random.randint(1,6)
  eight_sided_roll = random.randint(1,8)
  strenghtStat = int(round((six_sided_roll*eight_sided_roll)/2+12,0))
  return strenghtStat

healthStats()
print("🥌 Character Builder 🥌")
print()
anotherOne = "yes"
while anotherOne == "yes":
  name = character()
  time.sleep(1)
  os.system("clear")
  print(name)
  health = healthStats()
  print("HEALTH: ", health)
  strength = strenghtStats()
  print("STRENGTH: ", strength)
  print()
  print("May your name go down in Legend..")
  print()
  anotherOne = input("Again?: ")
  time.sleep(1)
  os.system("clear")