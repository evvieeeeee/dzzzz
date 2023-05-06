import logging

def word_count(the_sims):
    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    try:
        # считаем слова, логируем результат.
        with open(the_sims, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            num_words = len(words)
            logging.debug("this file has %d words", num_words)
            return num_words
    except OSError as e:
        logging.error("error reading the file")