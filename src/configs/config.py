import os

BASE_DIR = os.getcwd()
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
REPORTS_DIR = os.path.join(BASE_DIR, "reports", "figures")

def init_folders():
    for path in [DATA_RAW, DATA_PROCESSED, REPORTS_DIR]:
        if not os.path.exists(path):
            os.makedirs(path)