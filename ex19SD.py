def allied_races(HORDE, ALLIANCE):
    print(f"\tNew race for horde: {HORDE}.")
    print(f"\tNew race for alliance: {ALLIANCE}.")
    print(f"both {HORDE} and {ALLIANCE} will launch soon!\n ")

def month_races(H, A):
    print("For the next month after that one there will be: ")
    print(f"\t{H} and {A} ")

print("For the 28th of April this are the next races that will be unlocked: ")
allied_races("Orcs", "Humans")

print("For the 29th of April this are the next races that will be unlocked: ")
race1 = "Trolls"
race2 = "Dwarves"
allied_races(race1, race2)

print("For the 30th of April this are the next races that will be unlocked: ")
allied_races("Tauren", "Gnome")

print("For the 1st of April this are the next races that will de unlocked: ")
allied_races("Blood Elf","Night elf")

print("For the 2nd of April this are the next races that will de unlocked: ")
allied_races("Forsaken", "Draenei")

month_races("Nightborne", "Void elf\n")
month_races("Highmountain Tauren", "Lightforged Draenei\n")
month_races("Mag'har Orc", "Dark Iron Dwarve\n")
month_races("Zandalari Troll", "Kul Tiran Human\n")
month_races("Vulpera (F)", "Mechagnomes\n")