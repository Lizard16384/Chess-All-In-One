#!/usr/bin/env python3

import json
from pathlib import Path

from payload.parser import parse
from payload import finish

def main():
    command_path = "chess/live board updates/live board updates.mcfunction"
    live_positions_path = "chess/live board updates/live_positions.json"
    chess_positions_path = "chess/chess_positions.json"
    command_lines = finish.read_file_lines(command_path)
    with open(live_positions_path,"r",encoding="utf-8") as file: live_position_data = json.load(file)
    with open(chess_positions_path,"r",encoding="utf-8") as file: chess_position_data = json.load(file)
    positions_data = live_position_data | chess_position_data
    final_command_lines = parse.parse_command(command_lines, [parse.get_parse_positions(positions_data)])
    finish.finish("".join(final_command_lines), ("clipboard","write"), "chess/live board updates/result.txt")

if __name__ == "__main__":
    main()
