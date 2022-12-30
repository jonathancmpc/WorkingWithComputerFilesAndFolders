from pathlib import Path

root_dir = Path('files')
#file_paths_iterdir = root_dir.iterdir()
file_paths_glob = root_dir.glob("*/*")

""" for path in file_paths_iterdir:
    print(path) """

for path in file_paths_glob:
    if path.is_file():
      new_filename = path.parts[-2] + '-' + path.name
      new_filepath = path.with_name(new_filename)
      path.rename(new_filepath)


