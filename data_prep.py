from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

AUTOTUNE = tf.data.experimental.AUTOTUNE

import IPython.display as display
from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


images_folder = Path("data/stanford_ds/Images")
annotations_folder = Path("data/stanford_ds/Annotation")

list_ds = tf.data.Dataset.list_files(str(images_folder/'*/*'))

for f in list_ds.take(5):
  print(f)
