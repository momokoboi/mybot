
def discord():
  import os
  import discord
  from discord.ext import commands
  import time
  client = commands.Bot(command_prefix="!", help_command=None)



  @client.event
  async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=discord.Game(name="!help - by KillerdeathBr"))
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
      inicial = "**U get it? :hear_no_evil: :**\n" + "```" + name3 + "```" 
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

  @client.group(name='help', aliases=['HELP', 'Help'], invoke_without_command=True)
  async def help(ctx):
      embedVar = discord.Embed(title="                       __**Help Section**__", description="The available command list follows below:", color=0x00FFFF)
      embedVar.add_field(name="Command  **!help**", value='Displays the Help Section :page_facing_up:\nyou can also use !help <command>' + "\u200b", inline=False)
      embedVar.add_field(name="Command **!purge**", value='Deletes messages for you :x:\n_Use !purge amount-to-be-deleted_\n_You need to have permission to use this command._', inline=False)
      embedVar.add_field(name="Command **!joke**", value='Displays a joke for you :zany_face:')
      embedVar.add_field(name="Command **!hash**", value= "Generates a Hash or Enconding for you :chains:\nUse _!hash hash-type your-message_\nUse _!supported_ to see supported hash types and encondings", inline=False)
      await ctx.channel.send(embed=embedVar)
  @help.command(name='joke', aliases=['Joke', 'JOKE'])
  async def joke_help(ctx):
    embedVar = discord.Embed(title="                       __**Jokes**__", description="Displays a joke for you :zany_face:\n_Use !joke to spawn a joke._", color=0x00FFFF)
    await ctx.channel.send(embed=embedVar)
  @help.command(name='hash', aliases=['Hash', 'HASH'])
  async def hash_help(ctx):
    embedVar = discord.Embed(title="                       __**Hash**__", description="Generates a hash or enconding for you :chains:\n_Use !hash hash-type your-message._\nTo se supported hashes use !supported", color=0x00FFFF)
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

  @client.command(name='purge', aliases=['Purge', 'PURGE'])
  @commands.has_any_role('Moderators', 'Support_Team')
  async def purge(ctx, arg1):
    try:
      print('test1')
      amount = int(arg1)
      def not_pinned(msg):
        return not msg.pinned
      purged = await ctx.channel.purge(limit=amount + 1, check=not_pinned)
      await ctx.channel.send(f'{len(purged)-1} messages deleted by ***{ctx.author.name}***.')
      time.sleep(2)
      await ctx.channel.purge(limit=1)
      print('test2')
    except:
      await ctx.channel.send("The amount of messages to be deleted needs to an integer")

  client.run(os.getenv('mama123'))
  
if __name__ == '__main__':
  discord()
  