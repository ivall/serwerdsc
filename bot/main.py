import discord
import requests

from discord.ext import commands
from discord.embeds import Embed
from discord.ext.commands.errors import MissingPermissions

from config import *
from utils import options, is_alphanumeric

bot = commands.Bot(command_prefix='s!')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("s!pomoc"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Brak permisji.")
    else:
        raise error


@bot.command()
async def pomoc(ctx):
    embed = Embed(title="Pomoc bota serwerdsc.pl", color=0xC100FF)

    embed.add_field(name='s!ustaw link <nazwa>', value='Ustawia nazwę linku', inline=False)
    embed.add_field(name='s!ustaw opis "<opis>"', value='Ustawia opis', inline=False)
    embed.add_field(name='s!ustaw css <plik_css>', value='Ustawia link do pliku css. Zalecane skorzystanie z [hosting.zxu.pl](https://hosting.zxu.pl)', inline=False)
    embed.add_field(name='s!link', value='Link do strony serwera', inline=False)

    embed.add_field(name='Linki', value='[serwer support](https://discord.gg/McGwsEsjBU)')

    embed.set_footer(text=f'Aktywny na {len(bot.guilds)} serwerach.')

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def ustaw(ctx, option=None, value=None):
    if option not in options.keys() or not value:
        await ctx.send('Niepoprawne użycie komendy.')
        return

    if option == 'name':
        if not is_alphanumeric(value):
            await ctx.send('Możesz używać tylko liter bez polskich znaków i cyfr.')
            return

    field_name = options[option]
    invite_link = await ctx.channel.create_invite(unique=False)

    payload = {
        field_name: value,
        'discord_id': ctx.guild.id,
        'discord_name': ctx.guild.name,
        'discord_avatar': str(ctx.guild.icon_url)[:-10],
        'discord_invite': str(invite_link)
    }
    headers = {"Authorization": f"Bearer {api_token}"}

    r = requests.post(base_url, data=payload, headers=headers)

    if str(r.status_code)[0] == '2':
        await ctx.send('Wszystko przebiegło poprawnie, dane zostały utworzone lub zaaktualizowane.')
        return

    elif r.status_code == 409:
        await ctx.send('Serwer z taką nazwą już istnieje.')
        return

    #  I need to validate it on backend, but I am too lazy for now to do that
    elif r.status_code == 500:
        await ctx.send('Nazwa serwera nie może zawierać emotikon.')
        return

    await ctx.send('Niestety wykonanie komendy nie przebiegło poprawnie :worried:.')


@bot.command()
async def link(ctx):
    headers = {"Authorization": f"Bearer {api_token}"}

    r = requests.get(base_url+str(ctx.guild.id), headers=headers).json()

    try:
        await ctx.send('https://serwerdsc.pl/'+r['name'])
    except KeyError:
        await ctx.send('Serwer jeszcze nie został dodany do serwerdsc.pl, użyj komendy **s!ustaw link <nazwa>** aby go dodać.')


bot.run(token)
