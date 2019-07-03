import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("La foncton a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention!")
logging.error("Une erreur est survenue")
logging.critical('Erreur critique')