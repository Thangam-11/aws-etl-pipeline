from sqlalchemy import create_engine
from utils.logger import logger

logger.info("db_utils module loaded")

def get_engine(config):

    logger.info("Creating database engine")

    engine = create_engine(
        f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    )

    logger.info("Database engine created successfully")

    return engine