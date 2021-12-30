from pathlib import Path, PureWindowsPath
import os

print(os.getcwd())
print( os.listdir(os.getcwd()) )

h = Path('chispazo/Data_set/Chispazo.csv')

if not h.exists():
    print('nosta we')
else:
    print(h.name)
    print(h.suffix)
    print(h.stem)
    print(PureWindowsPath(h))