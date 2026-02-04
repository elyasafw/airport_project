from pathlib import Path

def files_exiest(filename):
    file_path = Path(filename)
    try:
        if file_path.exists():
            return True
    except Exception:
        print("error! file not found...")
        return False