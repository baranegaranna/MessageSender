# MessageSender

## Usage
Have you ever had a channel in telegram? and you wanted to send users a message or they send you a message but you didn't want to give them your username?

This bot helps you to transfer messages. You make a group give the bot group chat id or your own chat id and host the bot. Bot will forward messages for you and you can answer them. 

## Settings
You have to place your own things in ``settings.py``. open it with a text editor like notepad or something else. 
* Get a token from [BotFather](https://t.me/BotFather). You have to make a bot to do this. Replace ``Token`` with your token but DO NOT REMOVE ' '. <br>
Don't share your token with others and keep it safe. In case someone got your token you can revoke the token <br>
* Make an account in [Python Anywhere](https://www.pythonanywhere.com/). If you don't confirm your email address you won't be able to reset password later. Replace your python anywhere username with ``Username``.  <br>
* Create a group and add bot. Find chat id or use your own chat id. change ``-123456`` to chat id you want. <br>
You can use [Show Json Bot](https://t.me/ShowJsonBot) to find group chat id. Just add it to group and you can remove it later.
<br>Remember if you upgrade group to supergroup chat id will change. 
* You can simply change other varibles execpt port. <br>

## Start Webhook
* Open **Web** tab. <br>
* Click **Add a new web app**. It's a big blue button. <br>
* Press **Next**. <br>
* Select **Flask**. <br>
* Select **Python 3.9**. (Now it's the latest version of python in python anywhere.) <br>
* replace ``flask_app.py`` with ``app.py`` <br>
* Open **Files** in a new tab. <br>
* From left column (Directories) find **mysite** and open it. <br>
* Upload your files. (All of them though you can skip ``startwebhook.py`` but if you don't have python installed in your machine you can run it in python anywhere.) <br>
* Click on **Open Bash console here**. <br>
* Write ``pip3 install python-telegram-bot --user`` <br>
* When it's done type ``exit``. <br> When you do this python anywhere closes the bash console and if you just close the tab it doesn't mean you have closed the bash console. You can find your consoles in **console** tab. <br>
* Run ``startwebhook.py`` and type ``exit`` if you are in python anywhere. <br>
* Go back to **Web app setup** tab or press **Web** again. <br>
* Press big green button with text **Reload YOUR_USERNAME.pythonanywhere.com** and wait for it.<br>
if you just changed anything in files you have to press this button again.
* Done!

Thanks [Tamerlan Tabolov](https://github.com/The0nix) for [PythonAnywhere bot template](https://github.com/The0nix/pythonanywhere-tg-bot)!
