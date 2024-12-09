import pandas as pd


def csv_to_pkl(csv_file, output_pkl):
    """
    CSV 파일을 PKL 파일로 변환하는 메서드

    Args:
        csv_file: 변환할 csv 파일 경로
        output_pkl: 생성할 pkl 파일 경로
    """
    df = pd.read_csv(csv_file)
    df.to_pickle(output_pkl)
