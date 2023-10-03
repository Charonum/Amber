# Amber
Amber is a lightweight self-hosting application written in python. It allows you to access your server to remotely shut down, start, and send commands.
# Setup
1. Either use Installer.py or paste your server files into Amber's main directory, renaming your jar file to server.jar
2. Run `pip3 install -r requirements.txt` in a terminal
3. Run Amber.py
4. You should be prompted to enter an email address, type nothing and just hit enter.
5. The UI should be live at localhost:8501. If that doesn't work, the terminal should say
# Webhooks
**WEBHOOKS ONLY WORK IF THE MC SERVER IS ONLINE**
1. Log: localhost:5000/log
2. Command: localhost:5000/command `to send a command, post {"command": "your command here"}`
