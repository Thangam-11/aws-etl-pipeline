import os
import yaml
from utils.logger import logger


def load_config(config_path="config/config.yaml"):

    try:

        if not os.path.exists(config_path):

            logger.error(f"Config file not found at {config_path}")

            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, "r") as f:

            config = yaml.safe_load(f)

        logger.info("Configuration loaded successfully")

        return config

    except Exception as e:

        logger.exception(f"Failed to load configuration: {str(e)}")

        raise