data = '/home/kali/example_file_to_split'
step = 25
n = 1
number_of_lines = 0
jump = step

with open(data, 'rb') as file:
    lines = file.readlines()
    file.close()

with open(data) as size:
    for number_of_line, line in enumerate(lines):
        file_of_results = f'split_{n}.txt'
        if (number_of_line + 2) <= jump:
            with open(rf"{file_of_results}", "ab") as file_results:
                #file_results.write(line.decode('utf-8'))
                file_results.write(line)
        elif (number_of_line + 2) > jump:
            n += 1
            jump = step * n
            with open(rf"{file_of_results}", "ab") as file_results:
                #file_results.write(line.decode('utf-8'))
                file_results.write(line)
