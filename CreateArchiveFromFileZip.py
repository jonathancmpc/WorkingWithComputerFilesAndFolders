from pathlib import Path
import zipfile

root_dir = Path('files/ZipFiles')
archive_path = root_dir / Path('archive.zip') # Concatena os diretórios

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob('*.txt'):
      zf.write(path) #Escreve dentro do arquivo zip
      path.unlink() #apaga os arquivos que foram zipados
