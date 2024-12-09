from shutil import make_archive


def _compress_middle_data(root_dir_path, batch_result_folder_name, middle_folder_name):
    target_dir_path = root_dir_path / middle_folder_name
    zip_file_name = str(root_dir_path / batch_result_folder_name / middle_folder_name)

    if not target_dir_path.exists() or not target_dir_path.is_dir():
        return

    make_archive(zip_file_name, 'zip', target_dir_path)
