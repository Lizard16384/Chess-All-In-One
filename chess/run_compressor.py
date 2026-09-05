#!/usr/bin/env python3

from pathlib import Path

from payload.parser import parse
from payload import finish
from payload.positioner import calculate_positions

import position_requirements
import themes

def main():
    command_path = "chess/chess.mcfunction"
    positions_path = Path("chess/chess_positions.txt")
    theme_data = themes.get_theme_commands()
    command_lines = finish.read_file_lines(command_path)
    requirements = position_requirements.return_data()
    positions_lines = calculate_positions.calculate(requirements, positions_path)
    final_command_lines = parse.parse_command(command_lines, [parse.get_parse_positions(positions_lines), parse.get_parse_raw_data(theme_data)])
    finish.finish("".join(final_command_lines), ("clipboard","write"), "chess/chess_payload.txt")

if __name__ == "__main__":
    main()
