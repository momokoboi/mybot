
def discord():
  import os
  import discord
  from discord.ext import commands
  import time
  client = commands.Bot(command_prefix="!", help_command=None)



  @client.event
  async def on_ready():
    print(f"We have logged in as {client.user}")
  #______________________________________________________
  
  @client.command(name='joke', aliases=['JOKE', 'Joke'])
  async def daddy_joke(ctx):
    from Selenium_scrapping import getjoke

    URL ='https://edition.cnn.com/interactive/2019/06/us/dad-joke-generator-trnd/'
    await ctx.channel.send("Loading...")
    name3 = getjoke(URL)
    time.sleep(2)
    await ctx.channel.purge(limit=2)
    if len(name3) > 3:
      inicial = "**U get the Joke? :hear_no_evil: :**\n" + "```" + name3 + "```" 
    else:
      inicial = "```**ERROR PLEASE TRY AGAIN**```" 
    await ctx.channel.send(inicial)

  @client.command(name='hash', aliases=['HASH', 'Hash'])
  async def hash(ctx, agr1select,*argstext):
    hash_list = ['md2','md4', 'md5', 'sha224', 'sha256', 'sha384', 'sha512']
    test_list = ['sha512/244','sha512/256', 'base32', 'base64', 'dbase32', 'dbase64']
    if agr1select.lower() in hash_list:
      from Selenium_scrapping import gethash
      text_string = ' '.join(argstext)
      if len(text_string)> 0:
        await ctx.channel.send(f"Calculating {agr1select.lower()} Hash...")
        hashed_text = gethash(agr1select, text_string)
        await ctx.channel.purge(limit=2)
        await ctx.channel.send(f'**Requested message**: {text_string}')
        await ctx.channel.send(hashed_text)
      else:
        await ctx.channel.send("**Try again, not supported empty string.**")
    elif agr1select.lower() in test_list:
      from Selenium_scrapping import gethash_and_enconding
      text_string = ' '.join(argstext)
      if len(text_string)> 0:
        await ctx.channel.send(f"Calculating {agr1select.lower()}...")
        hashed_text = gethash_and_enconding(agr1select, text_string)
        await ctx.channel.purge(limit=2)
        await ctx.channel.send(f'**Requested message**: {text_string}')
        await ctx.channel.send('Result: ' + hashed_text)
      else:
        await ctx.channel.send("**Try again, not supported empty string.**")
    else:
       await ctx.channel.send("**Try again, not supported hash. To see supported hash use _!supported_**")

  @client.command(name='help', aliases=['HELP', 'Help'])
  async def helping_table(ctx):
      embedVar = discord.Embed(title="                       __**Help Section**__", description="The available command list follows below:", color=0x00FFFF)
      embedVar.add_field(name="Command  **!help**", value='Displays the Help Section :page_facing_up:' + "\n\u200b", inline=False)
      embedVar.add_field(name="Command **!joke**", value="Displays a random joke for you :zany_face:" + "\n\u200b", inline=False)
      embedVar.add_field(name="Command **!hash**", value= "Generates a Hash or Enconding for you :chains:\nuse _!hash_ <hashtype or enconding> <your-message>\nuse _!supported_ to see supported hash types and encondings", inline=False)
      await ctx.channel.send(embed=embedVar)

  @client.command(name='supported', aliases=['Supported', 'SUPPORTED'])
  async def supported_hash(ctx):
    embedVar2 = discord.Embed(title='**Supported hash types:**', description='_SHA-0 and SHA-1 are not supported, these algorithms have been compromised_', color=0x00FFFF)
    embedVar2.add_field(name='__MD* algorithms__(vulnerable)', value='md2, md4, md5.')
    embedVar2.add_field(name='__Secure Hash Algorithm(SHA)__', value='sha224, sha256, sha384, sha512, sha512/224, sha512/256.')
    embedVar2.add_field(name='__Secure Hash Algorithm(SHA3)__', value='3sha224, 3sha256, 3sha384, 3sha512.')
    embedVar2.add_field(name='__Encodings__', value='base32, base64')
    embedVar2.add_field(name='__Decodings__', value='dbase32, dbase64')
    await ctx.channel.send(embed=embedVar2)
  @client.event
  async def on_command_error(ctx, error):
    await ctx.channel.send("**Try again command invoked incorrectly. For help use _!help_**")
    print(error)

  client.run(os.getenv('mama123'))
  
if __name__ == '__main__':
  discord()
  