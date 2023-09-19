import os
import subprocess
import time
import streamlit as st
import requests
import re


def start():
    while True and os.path.exists("/proc/" + open("pid.txt").read().strip()):
        call()
        pattern = '\\[(\\d+:\\d+:\\d+)\\] \\[Server thread/INFO\\]: (\\w+) (joined|left) the game'
        online_players = set()
        with open('log.txt', 'r') as log_file:
            for line in log_file:
                match = re.search(pattern, line)
                if match:
                    _, player, action = match.groups()
                    if action == 'joined':
                        online_players.add(player)
                    elif action == 'left':
                        online_players.discard(player)
        if len(online_players) > 0:
            players.text("Online Players:\n" + "\n".join(online_players))
        else:
            players.text("No Online Players")
        time.sleep(5)


def call():
    if os.path.exists("/proc/" + open("pid.txt").read().strip()):
        response = requests.get('http://localhost:5000/log')
        if response.status_code == 200:
            log_text = response.content.decode("utf-8").splitlines()
            full_log = open("log.txt", "w")
            full_log.write(response.content.decode("utf-8"))
            full_log.close()
            while len(log_text) > 15:
                log_text.pop(0)
            log_text = "\n".join(log_text)
            log.text(log_text)

if os.path.exists("/proc/" + open("pid.txt").read().strip()):
    data = st.columns(2)
    if data[0].button("Stop Server"):
        try:
            requests.post('http://localhost:5000/command', json={'command': "stop"})
        except:
            pass
        os.kill(int(open("pid.txt").read().strip()), os.WSTOPPED)
        time.sleep(0.4)
        st.experimental_rerun()
    players = data[1].empty()
    log = st.empty()
    cmd = st.text_input("Command")
    if st.button("Send Command"):
        requests.post('http://localhost:5000/command', json={'command': cmd})
        time.sleep(0.4)
        call()
    start()
else:
    data = st.columns(2)
    if data[0].button("Start Server"):
        subprocess.Popen("python3 runtime.py", shell=True)
        time.sleep(0.5)
        st.experimental_rerun()
    players = data[1].empty()
    log = st.empty()
    st.text_input("Command", disabled=True)
    st.button("Send Command", disabled=True)
    log.text("Awaiting Server Start...")
