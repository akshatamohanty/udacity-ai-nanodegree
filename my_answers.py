import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    ## numpy strides to extract X
    nrows = len(series) - window_size
    n = series.strides[0]
    X = np.lib.stride_tricks.as_strided(series, shape=(nrows, window_size), strides=(n,n) )
    
    ## get all observations starting window_size + 1
    y = np.reshape(series[window_size:], (nrows, 1))

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size, b_inp_shape):
    hidden_units = 5
    model = Sequential()
    model.add(LSTM(hidden_units, batch_input_shape=b_inp_shape))
    model.add(Dense(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    special_characters = ['é', 'è', '*','%', '@', '/', 'â', 'à', '$']
    str_without_punc = text.replace("".join(punctuation), "")
    cleaned_text = str_without_punc.replace("".join(special_characters), "")
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    pass
