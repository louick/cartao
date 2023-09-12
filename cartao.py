import discord
from discord.ext import commands
import random
import os

TOKEN = os.getenv('DISCORD_TOKEN')



TOKEN = 'MTE1MDg2NTg2MzEyNjI5MDU2NQ.GvWKIB.SjdN-UZ3QT-B07LUqZSbdQpHh0TLfJxACwdKio'  
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

entry_greetings = [
    "Eu sei, eu sei... Cheguei na hora certa. Não se acostumem ",
    "Eis que faço minha entrada pontual. Não se desesperem, ainda sou o mesmo. ",
    "Estou aqui para duas coisas: beber café e evitar reuniões. E parece que o café acabou...",
    "Quem precisa de café quando se tem o dom de chegar atrasado e ainda fazer uma entrada triunfal?",
    "Espero que todos estejam prontos para outra performance épica de 'Eu fingindo saber o que estou fazendo'"
]

break_messages = [
    "Vou dar um intervalo. Se algo pegar fogo, vocês sabem... esperem até eu voltar.",
    "Não se preocupem, vou só recarregar as baterias. E com isso, quero dizer café.",
    "Hora de um encontro secreto com meu verdadeiro amor: a máquina de café.",
    "Estou indo para aquele lugar mágico onde os emails não podem me alcançar. Também conhecido como 'fora daqui'.",
    "Vou dar um tempo da tela do computador e olhar para a tela do meu celular. Mudança de cenário, sabe?",
    "Intervalo: aquele momento em que finjo que vou me exercitar, mas na verdade só quero um pedaço de bolo.",
    "Vou dar um intervalo para fazer algo muito importante. E com 'importante' quero dizer decidir entre uma coxinha ou duas.",
]

return_messages = [
    "Estou de volta! Não porque eu queria, mas porque aparentemente precisamos trabalhar para receber o salário.",
    "E como mágica, reapareci! E por 'mágica', quero dizer a sensação crescente de responsabilidade.",
    "Pensei em não voltar, mas lembrei que tenho contas a pagar.",
    "Retornei da minha viagem de 15 minutos para um lugar chamado 'lá fora'. Altamente recomendado.",
    "Quem sabia que 15 minutos poderiam passar tão rápido? Ah, sim, todos nós.",
    "Estou de volta e, acredite ou não, ainda não ganhei na loteria durante o meu intervalo.",
    "Retornei! E trouxe comigo a mesma energia de 'vamos fazer isso'... ou algo assim.",
    "Voltando ao palco principal após um breve intervalo. Espero que tenham sentido minha falta.",
]

exit_messages = [
    "E assim, após incontáveis minutos de trabalho árduo (e procrastinação), encerro meu dia. Que proeza!",
    "Desligando agora. Se eu esqueci de algo, com certeza foi intencional.",
    "Feito por hoje! E por 'feito', quero dizer 'deixando para amanhã o que eu claramente não queria fazer hoje'.",
    "Encerrando o dia antes que alguém me peça para fazer algo extra.",
    "E assim, com um suspiro de alívio e um clique no mouse, eu escapo da minha prisão de 9 às 5.",
    "Hora de encerrar! Se alguém precisar de mim, estarei muito ocupado... evitando meus emails.",
    "Jornada concluída. E, para ser honesto, estou surpreso por ter durado tanto tempo.",
    ]
entry_titles = ["Entrada!", "Online!", "Começando!", "Estou aqui!", "Início!"]
break_titles = ["Intervalo!", "Descanso!", "Pausa!"]
return_titles = ["Voltei!", "Retorno!", "De volta!"]
exit_titles = ["Saída!", "Encerrando!", "Finalizado!"]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

def create_embed(title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="Notification System")
    return embed

def updated_create_embed(title, description, color, author_mention):
    embed = discord.Embed(title=title, description=f"{author_mention} {description}", color=color)
    embed.set_footer(text="Notification System")
    return embed

@bot.command(name='entrada')
async def entrada(ctx):
    embed = updated_create_embed(random.choice(entry_titles), random.choice(entry_greetings), discord.Color.green(), ctx.author.mention)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='intervalo')
async def intervalo(ctx):
    embed = updated_create_embed(random.choice(break_titles), random.choice(break_messages), discord.Color.orange(), ctx.author.mention)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='voltei')
async def voltei(ctx):
    embed = updated_create_embed(random.choice(return_titles), random.choice(return_messages), discord.Color.blue(), ctx.author.mention)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='saida')
async def saida(ctx):
    embed = updated_create_embed(random.choice(exit_titles), random.choice(exit_messages), discord.Color.red(), ctx.author.mention)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

bot.run(TOKEN)
