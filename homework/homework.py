import re


def extract_data(pattern: str, file_path: str, output_file: str) -> None:
    with open(file=file_path, mode='r') as file:
        content = file.readlines()

    compiled_pattern = re.compile(pattern)

    data = []

    for line in content:
        matches = compiled_pattern.findall(line)
        data.extend(matches)

    with open(file=output_file, mode='w') as file:
        for item in data:
            file.write(item + '\n')


def main():
    input_file = 'MOCK_DATA.txt'

    while True:
        print(
            'Меню:',
            '1 - Считать имена и фамилии',
            '2 - Считать все емайлы',
            '3 - Считать названия файлов',
            '4 - Считать цвета',
            '5 - Выход',
            sep='\n'
        )

        try:
            choise = int(input('Выберите опцию: '))
            if choise < 1 or choise > 5:
                raise ValueError
        except ValueError:
            print('\nВыберите корректную опцию!\n')
            continue

        regex_patterns = {
            1: r'\b[A-Z][a-zA-Z\'’-]+\s[A-Z][a-zA-Z\'’-]+\b',
            2: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            3: r'\b[a-zA-Z0-9._-]+\.(ppt|avi|mp4|mp3|png|jpeg|mov|gif|xls|doc|tiff|pdf|mpeg|txt)\b',
            4: r'\b[0-9A-Fa-f]{6}\b',
        }

        output_files = {
            1: 'names.txt',
            2: 'emails.txt',
            3: 'files.txt',
            4: 'colors.txt',
        }

        if choise == 5:
            print('Выход из программы.')
            break

        extract_data(
            pattern=regex_patterns[choise],
            output_file=output_files[choise],
            file_path=input_file,
        )


if __name__ == '__main__':
    main()
