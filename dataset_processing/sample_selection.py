from Processor import Processor

ANNOT_PATH = "newdata-20230809T180348Z-001/newdata/train/ID2TR.json"

NEW_ANNOT_PATH = "datasets/COCO/annotations/"

IMAGE_DIR = "newdata-20230809T180348Z-001/newdata/test"

NEW_IMAGE_DIR = "datasets/COCO/train2017"

FILE_NAME = "ID2TR.json"


processor = Processor()

processor.sample_selection(ANNOT_PATH, NEW_ANNOT_PATH, IMAGE_DIR, NEW_IMAGE_DIR, FILE_NAME)

