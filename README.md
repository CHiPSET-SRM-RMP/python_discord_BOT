# python_discord_BOT
This is very biggner friendly Discord Bot based on Python 3.
This Bot is Made to Be used in single or multiple servers.


# Changes You Have TO Do Before Deployment

You have to create a Seprate json file in which Bot will store all the Server Id and Server prefixes.

Here "prefixes.json" is the file that is being used to store infor for you can use this name of different.

# Important Points

1. The module 'logging' is used for logging the data if you are deploying the bot on your PC, but if you're deploying the bot on cloud platform you will not be requred this file because you can see the runtime status of the bot every second. This is why here log code is commented.

2. You have to give the bot certain permissions "administrator, BOT, Guild". *Guild is not necessary because you have given the administrator permission.*

3. Intents are important because *intent are the previlage esclation for the bot so that it can access the member list or the the gluid* so you will be able to use "Ban, Unbann and Kick".

4. You can print the member join and leave in discord channel instead of console just by adding "channel client.get.channel(channel id)".
*Client can be anything but you have to define it in (client = commands.Bot(command_prefix = get_prefix, intents = intents))*
 
 5. So now adding the feature after the update of 1.0.2, You can make the bot play any any kind of song from video. this may effect the quality of the file but it is possible that te fole get affetcet.
 

# Setting The Bot

when the bot join the default prefix is going to be ". " (dot with space).

Use command ". help" to see all commands.
For changing the prefix You can use ". change_prefix (your prefix)"

# ALL SET
 
