import gc
import pickle
from hashlib import md5
from multiprocessing import Pool

import numpy as np

FILE_NAME_PREFIX = 'FILE_NAME_PREFIX'


def split_by_user_id(target_dir_path, save_dir_path, pp_num, key_group_list):
    tasks = [(key, target_dir_path, save_dir_path) for key in key_group_list]

    with Pool(processes=pp_num) as pool:
        results = list(pool.imap_unordered(_split_parallel, tasks))

    return sum(results)


def _split_parallel(args):
    key, target_dir_path, save_dir_path = args

    file_path = target_dir_path / f'{FILE_NAME_PREFIX}_{key}.pkl'

    total_record_count = 0
    for df in _load_pickle(file_path):
        if df is None or df.empty:
            continue

        vectorized_get_key1024_group = np.vectorize(_get_key1024_group)
        group_keys = vectorized_get_key1024_group(df['user_id'])

        for split_no, split_df in df.groupby(group_keys, as_index=False):
            save_file_path = save_dir_path / f'{file_path.stem}_{split_no}.pkl'

            with open(save_file_path, mode='wb') as wf:
                pickle.dump(split_df, wf)

            del split_df

        total_record_count += df.shape[0]
        gc.collect()

    return total_record_count


def _load_pickle(file_path):
    with open(file_path, mode='rb') as rf:
        while True:
            try:
                yield pickle.load(rf)
            except EOFError:
                break


def _get_key1024_group(key_str):
    key4096_group = md5(key_str.encode()).hexdigest()[:3]
    key1024_suffix = str(int(key4096_group[2], 16) // 4)

    return key4096_group[:2] + key1024_suffix
