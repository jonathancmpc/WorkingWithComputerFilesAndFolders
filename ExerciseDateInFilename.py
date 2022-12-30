from pathlib import Path
from datetime import datetime

root_dir = Path('files')
file_paths = root_dir.glob('*/*')

for path in file_paths:
  if path.is_file():
    stats = path.stat() #Pega os detalhes do arquivo, como data de modificação, criação, tamanho, etc.
    second_created = stats.st_ctime #Pega a data de criação int
    date_created = datetime.fromtimestamp(second_created) #Converte para datetime
    date_created_str = date_created.strftime("%Y-%m-%d_%H-%M-%S") #Converte para string para formatar
    
    new_filename = date_created_str + '-' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)