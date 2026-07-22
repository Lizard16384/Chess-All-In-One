#!/usr/bin/env python3

from payload.parser import parse
from payload import finish

import themes

def main():
    in_command = "chess/chess.mcfunction"
    in_positions = "chess/chess_positions.txt"
    theme_data = themes.get_theme_commands()
    command_lines = finish.read_file_lines(in_command)
    positions_lines = finish.read_file_lines(in_positions)
    final_command = parse.parse_command(command_lines, [parse.get_parse_positions(positions_lines), parse.get_parse_raw_data(theme_data)])
    finish.finish(final_command, ("clipboard","write"), "chess/chess_payload.txt")

if __name__ == "__main__":
    main()
