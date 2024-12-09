import os
from pathlib import Path


def find_all_paths(input_dir_path, output_dir_path):
    results = []

    for root, _, file_names in os.walk(input_dir_path):
        root = Path(root)

        for file_name in file_names:
            results.append((root / file_name, output_dir_path / file_name))

    return results