from keras.models import load_model
from keras import backend as K

K.clear_session()

model = load_model('md_ctc/model/classifier_model.h5')

model._make_predict_function()