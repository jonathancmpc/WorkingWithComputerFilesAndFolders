from pathlib import Path
import zipfile

root_dir = Path('files/ZipFiles')
destination_path = Path('files/Destination')

for path in root_dir.glob('*.zip'):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = destination_path / Path(path.stem) #nome da pasta de destino
    zf.extractall(path=final_path)