import requests
import re

from discord.ext import commands
from discord.embeds import Embed
from discord.ext.commands.errors import MissingPermissions

from config import *

bot = commands.Bot(command_prefix='s!')
options = {
    'link': 'name',
    'opis': 'description',
    'css': 'css_file'
}

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
    embed.add_field(name='s!ustaw css <plik_css>', value='Ustawia link do pliku css', inline=False)

    embed.add_field(name='Linki', value='[serwer support](https://discord.gg/McGwsEsjBU)')

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def ustaw(ctx, option=None, value=None):
    if not option or option not in options.keys() or not value:
        await ctx.send('Niepoprawne użycie komendy.')
        return

    if option == 'name':
        pattern = re.compile("[A-Za-z0-9]+")
        if not pattern.fullmatch(value):
            await ctx.send('Możesz używać tylko liter i cyfr.')
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

    #  server with that name already exists
    elif r.status_code == 409:
        await ctx.send('Serwer z taką nazwą już istnieje.')
        return

    await ctx.send('Niestety wykonanie komendy nie przebiegło poprawnie :worried:.')


bot.run(token)
