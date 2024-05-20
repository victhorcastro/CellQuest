import os
import time
import mysql.connector

from core.logger import logger


def estabilish_connection() -> mysql.connector.connection.MySQLConnection:
    logger.info("Estabilishing connection with database")

    connection_config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    }

    try:
        return mysql.connector.connect(**connection_config, raise_on_warnings=True)  # type: ignore
    except (mysql.connector.Error, mysql.connector.Warning) as error:
        logger.error(f"Error while estabilishing connection with database: {error}")

    return None
