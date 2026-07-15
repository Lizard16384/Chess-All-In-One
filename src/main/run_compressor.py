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

def read_file_lines(file_name):
    file = open(file_name)
    file_lines = []
    for line in file:
        new = line.strip()
        if len(new) > 0 and new[0] != "#":
            file_lines.append(new)
    file.close()
    return file_lines

def main():
    raw_command = parse.parse_command(read_file_lines("chess.mcfunction"),read_file_lines("chess_positions.txt"),themes.get_theme_commands())

    snbt= compress.compress_data(raw_command)
    raw_data = {"snbt":snbt,"storage":"c","scoreboard":"c"}

    final_command = parse.parse_command(read_file_lines("../compressor.mcfunction"),read_file_lines("../positions.txt"),raw_data)
    if len(final_command) > 32500:
        print(f"Payload of {len(final_command)} exceeds 32500! Pasting into a command block directly will not be possible!")
    else:
        print(f"Payload: {((len(final_command)/32500) * 100):.2f}%, {len(final_command)} used of 32500")
    result = open("result.txt", "w", -1, "utf-8")
    result.write(final_command)
    result.close()

    pyperclip.copy(final_command)

    print("Result wrote to file result.txt and copied to clipboard.")

def test():
    raw_command = parse.parse_command(read_file_lines("chess.mcfunction"),read_file_lines("chess_positions.txt"),themes.get_theme_commands())

    snbt = compress.compress_data(raw_command)
    raw_data = {"snbt":snbt,"storage":"c","scoreboard":"c"}

    print(raw_data["snbt"])

main()
#test()
