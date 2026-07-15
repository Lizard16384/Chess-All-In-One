file = open("transformation.txt")
file_lines = file.readlines()
file.close()

summon_line = "execute"
match = "transformation"
for i in range(len(file_lines)):
    if file_lines[i][0:len(summon_line)] == summon_line:
        offset_start = file_lines[i].find("summon block_display ~ ~") + len("summon block_display ~ ~")
        offset_end = file_lines[i].find(" ",offset_start)
        offset = float(file_lines[i][offset_start:offset_end]) + ((1/16) * (1/4) * (1/2))
        new_line = file_lines[i][0:file_lines[i].find("positioned")] + "run summon block_display ~ ~-.03125 ~ " + file_lines[i][file_lines[i].find("{",offset_start):]
        file_lines[i] = new_line
    if file_lines[i][0:len(match)] == match:
        start_data = file_lines[i].find("[")
        end_data = file_lines[i].find("]")
        value_str = file_lines[i][start_data+1:end_data]
        values = value_str.split(",")
        values[7] = str(float(values[7]) + offset).replace("0.",".")
        new_transform = "[" + ",".join(values).strip(" ") + "]"
        new_data = "data:{final_transformation:[" + value_str + "]}"
        new_line = "interpolation_duration:20," + file_lines[i][0:start_data] + new_transform + "," + new_data + file_lines[i][end_data + 1:]
        file_lines[i] = new_line

file = open("transform_out.txt","w")
for line in file_lines:
    file.write(line)
file.close()
