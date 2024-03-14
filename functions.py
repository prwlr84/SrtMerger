import pathlib
import time

def parse_file_name(string):
    first= string.split('und')
    name = first[0]
    second = first[1].split('date')[1].split('company')
    date = second[0]
    comp = second[1]
    anyad = {
        'Name': name.strip(),
        'Date': date.strip('_'),
        'Company': comp.strip()
    }
    print(list(anyad))
    return anyad

def clean_and_merge(data_list, dest='', name=''):
    file_name = f'{name or time.strftime("%d-%m-%Y-%H-%M")}.txt'
    text = []
    for data in data_list:
        for d in list(parse_file_name(data.name.strip('.srt')).items()):
            text.append(f'{d[0]}: {d[1]}' + ', ')
        if dest:
            data = pathlib.Path(data)
            with open(data, 'r') as srt:
                for line in srt.readlines():
                    if line[0].isalpha():
                        text.append(line + '\n')
        else:
            for line in data.readlines():
                line = str(line.decode('utf-8'))
                if line[0].isalpha():
                    text.append(line + '\n')

        text.append('\n\n')

    dest_path = pathlib.Path(dest, file_name)
    with open(dest_path, 'w') as file:
        file.writelines(text)

    return file_name
