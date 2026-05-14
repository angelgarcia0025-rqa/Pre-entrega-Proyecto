import logging
import os


def configurar_logger():
    os.makedirs("reports/logs", exist_ok=True)

    logging.basicConfig(
        filename="reports/logs/ejecucion.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    return logging.getLogger()