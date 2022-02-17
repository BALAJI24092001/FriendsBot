
# Telegram Bot #

![MIT License](https://img.shields.io/github/license/BALAJI24092001/TelegramBot)
![Repo size](https://img.shields.io/github/repo-size/BALAJI24092001/TelegramBot)
![Lines of code](https://img.shields.io/tokei/lines/github/BALAJI24092001/TelegramBot)
![](https://img.shields.io/github/last-commit/BALAJI24092001/TelegramBot)

A telegram bot, created using python to make the series F.R.I.E.N.D.S, available to download easily.

## Create a bot ##  
<div>
<img src="./images/BotFatherLogo.jpg" width = 150 align="right"/>
<p>The first step is to create a bot from the BotFather bot, which is a official telegram bot by Telegram. Follow the below steps to create a bot, name the bot, give a usermane for the bot, change the privacy setting for the bot. 

Bot commands can also be managed from the BotFather bot manager bot itself. But for our flexibility we use python, where we can even establish a database connection for user data.</p>
</div>


<br>

<p align='center'>
<img src="./images/img1.png" width=320 /> <img src="./images/img2.png" width=320 > 
</p>

Use the command `/newbot` to start creating a new bot. Give the bot, a name, user name and the bot will give an API key.


<p align='center'>
<img src="./images/img3.png" width=320 /> <img src="./images/img4.png" width=320 /> 
</p>

Select the bot and disable the privacy settings. By default, the privacy settings are enabled. If the privacy is enabled, then bot cannot access the messages when it is added to a channel, unless the bot is mentioned by the user.


The bot is now created and can be accessable by the users from anywhere. But we didn't train the bot to reply to the commands. For this, we can directly train it from the BotFather itself, which is less efficient than training with any programming language.

Follow the code form `./src/bot.py` file to understand how the telegram api's, get and post command works.

## Authors ##
- [@BALAJI24092001](https://www.github.com/BALAJI24092001)
- [@gbgchakradhar](https://github.com/gbgchakradhar)
- [@abhiramavala](https://github.com/abhiramavala)

## License ##

<a href="https://github.com/BALAJI24092001/TelegramBot/blob/main/LICENSE"><p style="text-align:center">MIT License</p></a>
<p style="text-align:center">Copyright (c) 2021 BALAJI VARA PRASAD </p>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
