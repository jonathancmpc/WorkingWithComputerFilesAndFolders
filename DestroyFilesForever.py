from pathlib import Path

root_dir = Path('files/destination')

for path in root_dir.glob('*.txt'):
  with open(path, 'wb') as file:
    file.write(b'') # Apaga todo o conteúdo que estiver no arquivo
  path.unlink() #deleta o arquivo para sempre