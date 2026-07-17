from payload.parser import parse
from payload import finish

import themes

def main():
    in_command = "chess/chess.mcfunction"
    in_positions = "chess/chess_positions.txt"
    theme_data = themes.get_theme_commands()
    command = parse.parse_command(finish.read_file_lines(in_command),finish.read_file_lines(in_positions),theme_data)

    raw_data = {"storage":"c","scoreboard":"c"}
    final_command = compress.compile_command(command, raw_data)
    finish.finish(final_command, ("clipboard","write"), "result.txt")

if __name__ == "__main__":
    main()
