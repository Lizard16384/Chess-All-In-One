import importlib.util
import sys
import pyperclip

"""
handling from previous management

spec = importlib.util.spec_from_file_location("parser", "../parse.py")
parse = importlib.util.module_from_spec(spec)
sys.modules["parser"] = parse
spec.loader.exec_module(parse)

spec = importlib.util.spec_from_file_location("compressor", "../compress.py")
compress = importlib.util.module_from_spec(spec)
sys.modules["compressor"] = compress
spec.loader.exec_module(compress)
"""

import themes

class CommandLengthError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(f"{self.message} (Length: {self.value})")

class CommandWireError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(f"{self.message} (Length: {self.value})")

def read_file_lines(file_name):
    file = open(file_name)
    file_lines = []
    for line in file:
        new = line.strip()
        if len(new) > 0 and new[0] != "#":
            file_lines.append(new)
    file.close()
    return file_lines

def finish(final, output, result = "result.txt"):
    if len(final) > 32500:
        raise CommandLengthError(len(final), f"Payload character length exceeds 32500! Command cannot be pasted in one command!")
    elif False:  # TODO: check byte length not to exceed 65536 and check behavior - maybe command can still be run, packet just can't be sent back to client.
        raise CommandWireError(len(final), f"Payload byte length exceeds 65536! Command cannot be sent to server in one command!")
    else:
        print(f"Payload: {((len(final)/32500) * 100):.2f}%, {len(final)} used of 32500")
    
    if "clipboard" in output:
        pyperclip.copy(final)
    if "write" in output:
        result = open(result, "w", -1, "utf-8")
        result.write(final)
        result.close()
    if "clipboard" not in output and "write" not in output:
        raise Exception('Please specify output method. Options are "clipboard" and/or "write"')

    print(f"Result {f'wrote to file {result}' if "write" in output else ""}{" and " if "clipboard" in output and "write" in output else ""}{"copied to clipboard" if "clipboard" in output else ""}.")

def main():
    raw_command = parse.parse_command(read_file_lines("chess.mcfunction"),read_file_lines("chess_positions.txt"),themes.get_theme_commands())

    snbt = compress.compress_data(raw_command)
    raw_data = {"snbt":snbt,"storage":"c","scoreboard":"c"}

    final_command = parse.parse_command(read_file_lines("../compressor.mcfunction"),read_file_lines("../positions.txt"),raw_data)
    finish(final_command, ("clipboard","write"), "result.txt")

main()
