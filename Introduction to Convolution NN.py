import pandas as pd
import numpy as np

MNIST = pd.read_csv("MNIST.csv")

Y = MNIST[["label"]]
MNIST = MNIST.drop(['label'], axis = 1)
X = MNIST / 255.0
X = X.values.reshape(-1,28,28,1)

from keras.utils.np_utils import to_categorical
Y = to_categorical(Y, num_classes=10)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3),padding='same', activation= 'relu'))
model.add(MaxPool2D(pool_size=(3,3)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation = 'softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

Performance = model.fit(X, Y,epochs= 1)

print('Model Accuracy: {}'.format(Performance.history['acc']))
print('Model Loss: {}'.format(Performance.history['loss']))