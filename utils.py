def read_commands():
    commands = {}
    current_command = None

    with open("amber-commands.txt", "r") as cmd_file:
        for line in cmd_file:
            line = line.strip()
            if line.startswith("///"):
                current_command = line[3:].strip()
                commands[current_command] = []
            elif current_command is not None:
                commands[current_command].append(line)

    for command, code_lines in commands.items():
        commands[command] = "\n".join(code_lines)

    return commands
