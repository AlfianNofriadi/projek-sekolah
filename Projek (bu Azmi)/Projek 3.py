class game:
    def __init__(game, genre, ukuranFile, rating, developer):
        game.genre = genre
        game.ukuranFile = ukuranFile
        game.rating = rating
        game.developer = developer

MobileLegends = game("MOBA", "±6GB", "4.3/5", "Moonton")
FreeFire = game("Battle Royale", "±1.5GB", "4.2/5", "Garena")
Minecraft = game("Sandbox/Adventure", "±1GB", "4.6/5", "Mojang Studios")
Roblox = game("Sandbox/Multiplayer", "±200MB", "4.4/5", "Roblox Corporation")
StardewValley = game("Simulation/RPG", "±500MB", "4.8/5", "ConcernedApe")

print("===== Class Games =====")
print("")

print("----- Mobile Legends -----")
print(MobileLegends.genre, MobileLegends.ukuranFile, MobileLegends.rating, MobileLegends.developer)

print("")
print("----- FreeFire -----")
print(FreeFire.genre, FreeFire.ukuranFile, FreeFire.rating, FreeFire.developer)

print("")
print("----- Minecraft -----")
print(Minecraft.genre, Minecraft.ukuranFile, Minecraft.rating, Minecraft.developer)

print("")
print("----- Roblox -----")
print(Roblox.genre, Roblox.ukuranFile, Roblox.rating, Roblox.developer)

print("")
print("----- Stardew Valley -----")
print(StardewValley.genre, StardewValley.ukuranFile, StardewValley.rating, StardewValley.developer)