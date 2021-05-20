import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
CONFIG_PATH = os.path.join(PROJECT_PATH, 'config', 'config.json')
TERMS_EXTRACTOR_PATH = os.path.join(PROJECT_PATH, 'terms_extractor')
DICT_EXTRACTOR_PATH = os.path.join(TERMS_EXTRACTOR_PATH, 'dict_extractor')
TERMS_EXTRACTOR_WEIGHTS_PATH = os.path.join(TERMS_EXTRACTOR_PATH, 'weights', 'weights.h5')
