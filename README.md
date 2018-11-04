# Tigger TheBot
A friendly discord bot written in Python using discord.py. With this bot you will be able to play puzzle games like tic-tac-toe!

**WARNING:** This is an on going project, may have some bugs and the code sure needs a big refactor.

### Contents
- [Setup](#setup)
- [How to play](#how-to-play)
- [Useful information](#useful-information)

## Setup

Before you can use the bot you need to have installed the [DiscordPy](https://github.com/Rapptz/discord.py/tree/rewrite) library (v1.0.0a) and _python 3.6_. To do so you need to clone the repo or download it. Then run this to install the requirements:
```
pip install -r requirements.txt
```
and then just install it:
```
python3.6 setup.py
```

After everything is installed and running in the proper version you simply run:
```
python3.6 main_bot.py
```

## How to play

To initiate the game just call the command mentioning your enemy:

```
!3lines @player2
```

After that you can make a move by sending the command `!00`, this for example would place your move at the top left corner, like this.
```
|-----------------|
|  X  |     |     |
|-----|-----|-----|
|     |     |     |
|-----|-----|-----|
|     |     |     |
|-----------------|
```

### Useful Information

This was made using [DiscordPy](https://github.com/Rapptz/discord.py/tree/rewrite) library. <br>
The API documentation for DiscordPy v1.0.0a is [here](https://discordpy.readthedocs.io/en/rewrite/api.html). <br>
To get around on how to use the library you can see this [tutorial](https://pythonprogramming.net/discordpy-basic-bot-tutorial-introduction/) from Sendtex.
