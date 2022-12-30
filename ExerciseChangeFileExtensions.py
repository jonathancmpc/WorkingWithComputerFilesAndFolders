from pathlib import Path

root_dir = Path('files/ChangeExtension')

#Criando os arquivos vazios
"""for i in range(1,10):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch() """

for path in root_dir.rglob('*.txt'):
    if path.is_file():
        new_filepath = path.with_suffix('.csv')
        path.rename(new_filepath)