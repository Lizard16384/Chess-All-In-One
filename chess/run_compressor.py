#!/usr/bin/env python3

import json

from pathlib import Path

from payload.parser import parse
from payload import finish
from payload.positioner import calculate_positions

import position_requirements
import themes

def main():
    command_path = "chess/chess.mcfunction"
    positions_path = Path("chess/chess_positions.json")
    theme_data = themes.get_theme_commands()
    command_lines = finish.read_file_lines(command_path)
    requirements = position_requirements.return_data()
    #position_data = calculate_positions.calculate(requirements, positions_path)
    with open(positions_path,"r") as file:
        position_data = json.load(file)
    final_command_lines = parse.parse_command(command_lines, [parse.get_parse_positions(position_data), parse.get_parse_raw_data(theme_data)])
    finish.finish("".join(final_command_lines), ("clipboard","write"), "chess/chess_payload.txt")

if __name__ == "__main__":
    main()
