import os
from datetime import datetime, timedelta


# ---------- DATE TRACKER ----------
def read_last_date(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r") as f:

            return f.read().strip()

    return "2025-06-30"


# ---------- UPDATE TRACKER ----------
def update_last_date(file_path, new_date):

    with open(file_path, "w") as f:

        f.write(new_date)


# ---------- NEXT DATE ----------
def get_next_date(last_date_str):

    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")

    next_date = last_date + timedelta(days=1)

    return next_date.strftime("%Y-%m-%d")