import os
from pathlib import Path

days = [f'day{i}' for i in range(1,32)]
files = ['input.txt', 'sample.txt']

for day in days:
     path = Path('inputs') / day
     os.mkdir(path)
     for filename in files:
         filepath = path / filename
         print(filepath)
         filepath.touch()
