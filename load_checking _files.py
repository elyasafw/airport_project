from pathlib import Path

def files_exiest(filename):
    file_path = Path(filename)
    if file_path.exists():
        return True
    else:
        print("error! file not found...")
        return False
    

def load_budget():
    with open('./budget.txt', 'r') as f:
        return float(f.read())