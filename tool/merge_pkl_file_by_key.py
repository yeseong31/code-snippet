from multiprocessing import Pool

import pandas as pd

from tool.split_pkl_file_by_key import FILE_NAME_PREFIX


def merge_by_user_id(target_dir_path, save_dir_path, pp_num, key_group_list):
    tasks = [(key, target_dir_path, save_dir_path) for key in key_group_list]

    with Pool(processes=pp_num) as pool:
        results = list(pool.imap_unordered(_merge_parallel, tasks))

    return sum(results)


def _merge_parallel(args):
    key, target_dir_path, save_dir_path = args

    target_file_paths = list(target_dir_path.glob(f'*_{key}.pkl'))
    if not target_file_paths:
        return None, 0

    df = pd.concat(map(pd.read_pickle, target_file_paths), ignore_index=True)

    save_file_path = str(save_dir_path / f'{FILE_NAME_PREFIX}_{key}.pkl')
    df.to_pickle(save_file_path)

    return df.shape[0]
