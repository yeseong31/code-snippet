from shutil import rmtree


def delete_dir(dir_path):
    """
    지정된 경로 내 모든 파일 및 디렉토리를 삭제하는 메서드

    Args:
        dir_path(Path): 삭제할 디렉토리 경로

    Raises:
        PermissionError: 삭제 또는 디렉토리 생성 권한이 없을 경우 발생
        OSError: 파일 시스템 관련 오류가 발생할 경우 발생
    """
    if dir_path.exists():
        rmtree(dir_path)


def clear_dir(dir_path):
    """
    지정된 경로 내의 모든 파일 및 디렉토리를 삭제하고, 빈 디렉토리를 재생성하는 메서드

    Args:
        dir_path(Path): 삭제 및 재생성할 대상 디렉토리 경로

    Raises:
        PermissionError: 삭제 또는 디렉토리 생성 권한이 없을 경우 발생
        OSError: 파일 시스템 관련 오류가 발생할 경우 발생
    """
    delete_dir(dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)
