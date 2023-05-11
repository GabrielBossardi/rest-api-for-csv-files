import os

CSV_UPLOAD_DIR = os.environ.get('CSV_UPLOAD_DIR')


def get_file_paths(valid_files):
    file_paths = {}
    for root_folder, subfolders, files in os.walk(CSV_UPLOAD_DIR):
        for file in files:
            file = os.path.splitext(file)[0]
            if file in valid_files:
                file_path = os.path.join(root_folder, file)
                file_paths[file] = file_path

    return file_paths
