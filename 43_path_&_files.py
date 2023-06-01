from pathlib import Path

directory = Path('G:/') / 'Программирование' / \
    'stashchuk-python' / 'files'

if not directory.exists():
    directory.mkdir()

with open('1st.txt', 'w') as file_1:
    file_1.write('python is nice\n')
    file_1.write('pycharm\n')
    file_1.write('vs code\n')

with open('2nd.txt', 'w') as file_2:
    file_2.write('python\n')
    file_2.write('c#\n')
    file_2.write('javascript\n')

with open('1st.txt') as file_1:
    print(file_1.read())

with open('2nd.txt') as file_2:
    print(file_2.readline())
    print(file_2.readline())
