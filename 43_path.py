from pathlib import Path

directory = Path('files')

if not directory.exists():
    directory.mkdir()

file_1 = directory / '1st.txt'
file_2 = directory / '2nd.txt'

with open(file_1, 'w') as f:
    lines = [
        'bmw',
        'chevrolet',
        'ferrari',
        'cadillac'
    ]
    for line in lines:
        f.write(line + '\n')

with open(file_2, 'w') as f:
    lines = [
        'python',
        'c#',
        'javascript'
    ]
    for line in lines:
        f.write(line + '\n')

with open(file_1) as f:
    print(f.read())

with open(file_2) as f:
    for line in f:
        print(line.strip())

file_1.unlink()
file_2.unlink()
if directory.exists:
    directory.rmdir()
