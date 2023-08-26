from Processor import Processor

ANNOT_PATH = "Background_mixed/annotations/ID2TE.json"

NEW_ANNOT_PATH = "Background_mixed/annotations"

IMAGE_DIR = "Background_mixed/test"

NEW_IMAGE_DIR = "Background_mixed/valid"

FILE_NAME = "ID2TE_Mixed.json"


processor = Processor()

processor.sample_selection(ANNOT_PATH, NEW_ANNOT_PATH, IMAGE_DIR, NEW_IMAGE_DIR, FILE_NAME)

