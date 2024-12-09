import pickle

import pandas as pd


def pkl_to_csv(pkl_file: str, output_csv: str):
    """
    PKL 파일을 CSV 파일로 변환하는 메서드

    Args:
        pkl_file: 변환할 pkl 파일 경로
        output_csv: 생성할 csv 파일 경로
    """
    try:
        # PKL 파일에서 데이터를 불러오기
        with open(pkl_file, 'rb') as file:
            chunk_dfs = []

            while True:
                try:
                    chunk_dfs.append(pickle.load(file))
                except EOFError:
                    break

            combined_df = pd.concat(chunk_dfs, ignore_index=True)
            combined_df.to_csv(output_csv, index=False)

    except (FileNotFoundError, EOFError):
        print(f"\n파일 {pkl_file}을(를) 읽을 수 없습니다.")