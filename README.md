# Intro-to-Convolution-Neural-Networks

This goal of this repository is to discuss convolutional neural networks (CNN) and how it can be applied towards the MNIST dataset. MNIST is an introductory computer vision dataset with the goal of predicting hand written digits. Each line of code will be broken down in this README in order for clarity of thought and action. This repository will go over Normalization/Reshaping techniques, working with categorical targets, building and compiling each layer of the CNN, and finally fitting the CNN to the data.

## Normalization/Reshaping
The first normalization technique is to divide each value in the dataset by 255. This normalization technique works because of how computers read color. Each value in the dataset will be between (0,255) and be in Red, Green, Blue (RGB) format with Red being (255,0,0) and Green being (0,255,0) for example. Dividing each value by 255 will allow for the range of number in the dataset to be between 0 and 1 depending on which colors are in the dataset. 

More information on Normalization can be found here: https://stackoverflow.com/questions/20486700/why-we-always-divide-rgb-values-by-255

Reshaping is necessary in order to turn each number from a 784 X 1 row into a 28 x 28 array. 
Reshaping: https://stackoverflow.com/questions/41848660/why-the-negative-reshape-1-in-mnist-tutorial

## Working with categorical targets
In order to work with the categorical targets in this dataset, we must turn each number into what known as "one-hot" meaning that each number is represented with a 1 in the dataset. For example a number 0 would be represent with [1,0,0,0,0,0,0,0,0,0] and the number 4 would be represented with [0,0,0,0,1,0,0,0,0,0]. This allows us to train the model by assigning classes instead of having a model that assumes that a number with the class of 4 is greater than a number with the class of 0.

Working with Categorical Data: https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/

## Building and compiling each layer of the CNN
Convolutional Layer (Conv2d) - https://hackernoon.com/visualizing-parts-of-convolutional-neural-networks-using-keras-and-cats-5cc01b214e59
Pooling Layer (MaxPool2d) - https://hackernoon.com/visualizing-parts-of-convolutional-neural-networks-using-keras-and-cats-5cc01b214e59
Flattening - https://www.tensorflow.org/tutorials/estimators/cnn
Dense Layer - https://www.tensorflow.org/tutorials/estimators/cnn
Output Layer - 
