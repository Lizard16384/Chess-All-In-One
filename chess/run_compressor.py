from payload.parser import parse
from payload.compressor import compress
from payload import finish

import themes

def main():
    in_command = "chess/chess.mcfunction"
    in_positions = "chess/chess_positions.txt"

    result = "result.txt"

    raw_command = parse.parse_command(finish.read_file_lines(in_command),finish.read_file_lines(in_positions),themes.get_theme_commands())

    snbt = compress.compress_data(raw_command)
    raw_data = {"snbt":snbt,"storage":"c","scoreboard":"c"}

    final_command = compress.compile_command(raw_data)
    finish.finish(final_command, ("clipboard","write"), result)

main()
