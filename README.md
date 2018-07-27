# Intro-to-Convolution-Neural-Networks
The goal of this repository is to discuss convolutional neural networks (CNNs) and how they can be applied towards the MNIST dataset. MNIST is an introductory computer vision dataset where the goal is to predict hand written digits. Each line of code will be broken down in this README in order for transparancy. The goal of this README is also to be a brief introduction into CNNs so there will be links to articles that go into some of the concepts here in more depth. This README will go over Normalization/Reshaping techniques, working with categorical targets, building and compiling each layer of the CNN, and finally fitting the CNN to the data.

## Normalization/Reshaping
The first normalization technique is to divide each value in the dataset by 255. This normalization technique works because of how computers read color; each value in the dataset will be between 0 and 255 and be in Red, Green, Blue (RGB) format with Red being (255,0,0) and Green being (0,255,0) for example. Dividing each value by 255 will allow for the range of numbers in the dataset to be between 0 and 1, depending on which colors are in the dataset. 

More information on Normalization can be found here: https://stackoverflow.com/questions/20486700/why-we-always-divide-rgb-values-by-255

Reshaping is necessary in order to turn each number from a 784 X 1 row into a 28 x 28 square array. 
Reshaping: https://stackoverflow.com/questions/41848660/why-the-negative-reshape-1-in-mnist-tutorial

## Working with categorical targets
In order to work with the categorical targets in this dataset, we must do what known is known as "one-hot" encoding, meaning that each number is represented with a 1 in the dataset. For example a number 0 would be represent with [1,0,0,0,0,0,0,0,0,0] and the number 4 would be represented with [0,0,0,0,1,0,0,0,0,0]. This allows us to train the model by assigning classes instead of having a model that assumes that a number with the class of 4 is greater than a number with the class of 0.

Working with Categorical Data: https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/

## Building and compiling each layer of the CNN
Convolutional Layer (Conv2d) and Pooling Layer (MaxPool2d) - The convolutional layer uses matrix multiplication in order to reduce the features down into what is known as a kernel. The MaxPool layer works very similar to the convolutional layer but for this case takes the max value in each window; more information can be found here:  https://hackernoon.com/visualizing-parts-of-convolutional-neural-networks-using-keras-and-cats-5cc01b214e59

Flattening - In order to perform classification on the data, we must flatten the dataset: https://www.tensorflow.org/tutorials/estimators/cnn

Output Layer - The output layer will be a dense layer that has 10 units (one to represent each class in the dataset 0-9). The output layer will also use the "softmax" activation function which will return the probability that a row belongs to a specific class: https://www.tensorflow.org/tutorials/estimators/cnn

Compiling of the model - Helps to configure the learning process, the compiling methods used in this example can be found here: https://keras.io/getting-started/sequential-model-guide/. Since this is a multi-class clasification problem, this example uses the compilation methods that are listed on the keras website under "multi-class clasification"

## Fitting and evaluating model
Fitting the model requires X and Y inputs along with the number of "epochs" that the model will train for. Epochs in this case are the amount of times that the model will pass through the training data. After fitting the model, it finished with and Accuracy of 87.9% and a Loss of 0.39. Descriptions of accuracy and loss can be found here:

Accuracy - https://stackoverflow.com/questions/34518656/how-to-interpret-loss-and-accuracy-for-a-machine-learning-model

Loss - https://www.quora.com/What-does-loss-mean-in-deep-neural-networks

## Discussion
To further improve this model in the future, two improvments could be to 1) train the model for more epochs and 2) add more convolution/ pooling layers to the model. Thank you to all of the people/websites linked above who aided me with learning a little bit more about CNNs, if you have any questions or comments about anything you see above or how to get started, feel free to reach out to me at kendallasmith140@gmail.com.
