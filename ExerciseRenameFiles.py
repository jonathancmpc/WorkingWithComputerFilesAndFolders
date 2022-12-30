from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob('*/*/*')

for path in file_paths:
  if path.is_file():
    new_filename = '-'.join(path.parts[1:-1]) + '-' + path.name
    #print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)