from Medical_CTC.__init__ import model
from Medical_CTC import settings
from keras.preprocessing import image
import numpy as np
import os

SCAN_DIR = os.path.join(settings.MEDIA_ROOT, 'ct_scans')


def check_for_contrast(img_dir=None):
    img_dir = os.path.join(SCAN_DIR, img_dir)
    img = image.load_img(img_dir)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred


