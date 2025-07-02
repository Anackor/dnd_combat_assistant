from app.infrastructure.db.database import init_db
from app.core.logging_config import setup_logging
import logging

def main():
    setup_logging()
    logging.info("D&D Assistant started")
    init_db()

if __name__ == "__main__":
    main()
