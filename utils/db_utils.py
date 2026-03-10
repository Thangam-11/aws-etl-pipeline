from sqlalchemy import create_engine


# ---------- DATABASE CONNECTION ----------
def get_engine(config):

    engine = create_engine(
        f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    )

    return engine
