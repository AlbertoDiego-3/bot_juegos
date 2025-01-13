import discord
from discord.ext import commands
import random



list1 = ["FANTASY STRIKE", "PHANTOM DUST", "HALO INFINITE"]
list2 = ["AGE OF EMPIRES", "TOTAL WAR", "COMPANY OF HEROES"]
list3 = ["LEAGUE OF LEYENDS", "STAR CRAFT", "O.A.D"]
list4 = ["UNCHARTED", "SATISFACTORY", "FARM SIMULATOR"]
list5 = ["CALL OF  DUTY 6", "FORZA HORIZON", "MARVEL RIVALS"]
list6 = ["WARFRAME", "SLEEPING DOGS", "WOLVERINE"]
list7 = ["DOOM", "BODERLANDS 3", "GRID LEYENDS"]
list8 = ["A WAY OUT", "SEA OF THIEVES", "STARDEW VALLEY"]
list9 = ["TRINER 4 THE NIGHTMARE PRINCE", "RISK OF RAIN", "DON'T STRAVER TOGETHER"]
list10 = ["LEAGUE OF LEYENDS", "DOTA 2", "BODY CAM"]
list11 = ["LEAGUE OF LEYENDS", "BATTLETECH", "X-COM"]
list12 = ["CALL OF DUTY 6", "GEARS OF WARS", "MARVEL'S SPIDERMAN"]
list13 = ["DRAGON BALL FIGHTERSZ", "CALL OF DUTY  6", "JOURNEY TO THE SAVAGE PLANET"]
list14 = ["DRAGON BAlL FIGHTERSZ", "LEFT 4 DEAD", "MONSTER HUNTER"]
list15 = ["SEA OF THHIEVES", "STREET FIGHTERS 6", "WORLD OF WARCRAFT"]
list16 = ["MARVEL'S SPIDERMAN", "THE WITCHER 3", "BATMAN ARKANE"]
list17 = ["DYINGHT LIGHT", "DISHONORED", "SLEEPING DOGS"]
list18 = ["DOTA 2", "AGE OF EMPIRES", "DOMINIONS"]
list19 = ["DIABLO 2", "HADES", "INVISIBLE, INC"]
list20 = ["MINDUSTRY", "HARVEST MOON", "HYDRONEER"]
list22 = ["SATISFACTORY", "ASSEMBLE WITH CARE", "FLOW"]
list24 = ["DON'T STRAVE TOGETHER", "PHASMOPHOBIA", "STARDEY VALLEY"]
list25 = ["WE WERE HERE", "TERAS", "ADIOS"]
list26 = ["RAFT", "KEEP TALKING AND NOBODY EXPLODES", "DAUNTLESS"]
list27 = ["HAARVERSTELLA", "LOS SIMS", "ATOMICROPS"]

game_lists = {
    ("Estrategico", "online", "el formato"): list3,
    ("Estrategico", "un solo jugador", "el formato"): list2,
    ("Estrategico", "cooperativo", "el formato"): list1,
    ("veloz", "online", "el formato"): list5,
    ("veloz", "un solo jugador", "el formato"): list6,
    ("veloz", "cooperativo", "el formato"): list7,
    ("casual", "online", "el formato"): list8,
    ("casual", "un solo jugador", "el formato"): list4,
    ("Estrategico", "cooperativo", "una historia"): list4,
    ("Estrategico", "online", "una historia"): list10,
    ("Estrategico", "online", "la jugabilidad"): list11,
    ("veloz", "online", "una historia"): list12,
    ("veloz", "online", "la jugabilidad"): list5,
    ("Estrategico", "cooperativo", "la jugabilidad"): list13,
    ("veloz", "cooperativo", "una historia"): list14,
    ("veloz", "cooperativo", "la jugabilidad"): list15,
    ("veloz", "un solo jugador", "una historia"): list16,
    ("veloz", "un solo jugador", "la jugabilidad"): list17,
    ("Estrategico", "un solo jugador", "la jugabilidad"): list18,
    ("Estrategico", "un solo jugador", "una historia"): list19,
    ("casual", "un solo jugador", "una historia"): list20,
    ("casual", "un solo jugador", "la jugabilidad"): list22,
    ("casual", "online", "una historia"): list9,
    ("casual", "online", "la jugabilidad"): list24,
    ("casual", "cooperativo", "una historia"): list25,
    ("casual", "cooperativo", "la jugabilidad"): list26,
    ("casual", "cooperativo", "el formato"): list27}



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="quiz")
async def start_quiz(ctx):
    await ctx.send("¡Comencemos el cuestionario de recomendación de juegos!")
    await recomendar_juego(ctx)

@bot.command()
async def recomendar_juego(ctx):
    x = []

    for question in [
        "¿Cómo eres jugando? (Estrategico, veloz, casual)",
        "¿Cómo te gusta jugar? (online, un solo jugador, cooperativo)",
        "¿Qué es lo que más te importa en un juego? (el formato, una historia, la jugabilidad)"
    ]:
        await ctx.send(question)
        response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        x.append(response.content)

    game_key = tuple(x)
    if game_key in game_lists:
        game = random.choice(game_lists[game_key])
        await ctx.send(game)
    else:
        await ctx.send("No se encontró una recomendación para tus preferencias.")


bot.run("token")
