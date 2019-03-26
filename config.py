# -*- coding: utf-8 -*-

__author__ = "Rahul Bhalley"

# Data
DATASET_DIR = "Dataset"
DATASET_NAME = "Dataset"
STYLES = ["fw", "mo", "uk", "vg"]
# Set up `TRAIN_STYLE`
if DATASET_NAME == "Dataset":
    TRAIN_STYLE = "fw"
elif DATASET_NAME == "monet2photo":
    TRAIN_STYLE = "mo"
elif DATASET_NAME == "ukiyoe2photo":
    TRAIN_STYLE = "uk"
elif DATASET_NAME == "vangogh2photo":
    TRAIN_STYLE = "vg"
DATASET_PATH = {
    "trainA": f"./{DATASET_DIR}/flower/trainA",
    "trainB": f"./{DATASET_DIR}/watercolor/trainB",
    "testA": f"./{DATASET_DIR}/flower/testA",
    "testB": f"./{DATASET_DIR}/watercolor/testB"
}
LOAD_DIM = 286
CROP_DIM = 256
CKPT_DIR = "checkpoints"
SAMPLE_DIR = "samples"

# Quadratic Potential
LAMBDA = 10.0
NORM = "l1"

# CycleGAN++
CYC_WEIGHT = 10.0
ID_WEIGHT = 0.5

# Network
N_CHANNELS = 3
UPSAMPLE = True

# Training
RANDOM_SEED = 12345
BATCH_SIZE = 4
LR = 2e-4
BETA1 = 0.5
BETA2 = 0.999
BEGIN_ITER = 0
END_ITER = 15000
TRAIN = False  # `False` runs `infer` function & `True` runs `train` function

# Inference
INFER_ITER = 2000
INFER_STYLE = "fw"
IMG_NAME = "y_rose.jpg"
IN_IMG_DIR = "content"
OUT_STY_DIR = "sty"
OUT_REC_DIR = "rec"
IMG_SIZE = None  # If `None` then stylizes original size `IMG_NAME`

# Logs
ITERS_PER_LOG = 100
ITERS_PER_CKPT = 1000
