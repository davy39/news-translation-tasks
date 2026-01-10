---
title: How to build a convolutional neural network that recognizes sign language gestures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T14:45:22.000Z'
originalURL: https://freecodecamp.org/news/asl-using-alexnet-training-from-scratch-cfec9a8acf84
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vrcZTOV9qoL_pmjAXC-WsQ.png
tags:
- name: Alexnet
  slug: alexnet
- name: American Sign Language
  slug: american-sign-language
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Vagdevi Kommineni

  Sign language has been a major boon for people who are hearing- and speech-impaired.
  But it can serve its purpose only when the other person can understand sign language.
  Thus it would be really nice to have a system which could ...'
---

By Vagdevi Kommineni

Sign language has been a major boon for people who are hearing- and speech-impaired. But it can serve its purpose only when the other person can understand sign language. Thus it would be really nice to have a system which could convert the hand gesture image to the corresponding English letter. And so the aim of this post is to build such an American Sign Language Recognition System.

![Image](https://cdn-media-1.freecodecamp.org/images/SkR0qk59Nc-jKggp41TAHT8TQFairUfB5oKH)

Wikipedia has defined ASL as the following:

> **American Sign Language** (**ASL**) is a [natural language](https://en.wikipedia.org/wiki/Natural_language) that serves as the predominant [sign language](https://en.wikipedia.org/wiki/Sign_language) of [Deaf communities](https://en.wikipedia.org/wiki/Deaf_communities) in the United States and most of Anglophone Canada.

First, the data: it is really important to remember the diversity of image classes with respect to influential factors like lighting conditions, zooming conditions etc. [Kaggle data on ASL](https://www.kaggle.com/grassknoted/asl-alphabet) has all such different variants. Training on such data makes sure our model has pretty good knowledge of each class. So, let's work on the K[aggle data](https://www.kaggle.com/grassknoted/asl-alphabet).

The dataset consists of the images of hand gestures for each letter in the English alphabet. The images of a single class are of different variants — that is, zoomed versions, dim and bright light conditions, etc. For each class, there are as many as 3000 images. Let us consider classifying “A”, “B” and “C” images in our work for simplicity. Here are links for the full code for [training](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/2_AlexNet/asl_full.py) and [testing](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/2_AlexNet/predict_full.py).

![Image](https://cdn-media-1.freecodecamp.org/images/2Ja-bVTS-nR0ToERP8duawXQ2fFxG8RsH7GS)
_An image for the letter ‘A’ from the dataset_

We are going to build an [AlexNet](https://www.learnopencv.com/understanding-alexnet/) to achieve this classification task. Since we are training the CNN, make sure that there is the support of computational resources like GPU.

We start by importing the necessary modules.

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning) 
```

```
import osimport cv2import randomimport numpy as npimport kerasfrom random import shufflefrom keras.utils import np_utilsfrom shutil import unpack_archive
```

```
print("Imported Modules...")
```

Download the data zip file from K[aggle data](https://www.kaggle.com/grassknoted/asl-alphabet). Now, let us select the gesture images for A, B, and C and split the obtained data into training data, validation data, and test data.

```
# data folder pathdata_folder_path = "asl_data/new" files = os.listdir(data_folder_path) 
```

```
# shuffling the images in the folderfor i in range(10):   shuffle(files)
```

```
print("Shuffled Data Files")
```

```
# dictionary to maintain numerical labelsclass_dic = {"A":0,"B":1,"C":2}
```

```
# dictionary to maintain countsclass_count = {'A':0,'B':0,'C':0}
```

```
# training listsX = []Y = []
```

```
# validation listsX_val = []Y_val = []
```

```
# testing listsX_test = []Y_test = []
```

```
for file_name in files:  label = file_name[0]  if label in class_dict:    path = data_folder_path+'/'+file_name    image = cv2.imread(path)    resized_image = cv2.resize(image,(224,224))    if class_count[label]<2000:      class_count[label]+=1      X.append(resized_image)      Y.append(class_dic[label])    elif class_count[label]>=2000 and class_count[label]<2750:      class_count[label]+=1      X_val.append(resized_image)      Y_val.append(class_dic[label])    else:      X_test.append(resized_image)      Y_test.append(class_dic[label])
```

Each image in the dataset is named according to a naming convention. The 34th image of class A is named as “A_34.jpg”. Hence, we consider only the first element of the name of the file string and check if it is of the desired class.

Also, we are splitting the images based on counts and storing those images in the X and Y lists — X for image, and Y for the corresponding classes. Here, counts refer to the number of images we wish to put in the training, validation, and test sets respectively. So here, out of 3000 images for each class, I have put 2000 images in the training set, 750 images in the validation set, and the remaining in the test set.

Some people also prefer to split based on the total dataset (not for each class as we did here), but this doesn’t promise that all classes are learned properly. The images are read and are stored in the form of Numpy arrays in the lists.

Now the label lists (the Y’s) are encoded to form numerical one-hot vectors. This is done by the np_utils.to_categorical.

```
# one-hot encodings of the classesY = np_utils.to_categorical(Y)Y_val = np_utils.to_categorical(Y_val)Y_test = np_utils.to_categorical(Y_test)
```

Now, let us store these images in the form of .npy files. Basically, we create separate .npy files to store the images belonging to each set.

```
if not os.path.exists('Numpy_folder'):    os.makedirs('Numpy_folder')
```

```
np.save(npy_data_path+'/train_set.npy',X)np.save(npy_data_path+'/train_classes.npy',Y)
```

```
np.save(npy_data_path+'/validation_set.npy',X_val)np.save(npy_data_path+'/validation_classes.npy',Y_val)
```

```
np.save(npy_data_path+'/test_set.npy',X_test)np.save(npy_data_path+'/test_classes.npy',Y_test)
```

```
print("Data pre-processing Success!")
```

Now that we have completed the data preprocessing part, let us take a look at the full data preprocessing code here:

```
# preprocess.py
```

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning)
```

```
import osimport cv2import randomimport numpy as npimport kerasfrom random import shufflefrom keras.utils import np_utilsfrom shutil import unpack_archive
```

```
print("Imported Modules...")
```

```
# data folder pathdata_folder_path = "asl_data/new" files = os.listdir(data_folder_path)
```

```
# shuffling the images in the folderfor i in range(10):   shuffle(files)
```

```
print("Shuffled Data Files")
```

```
# dictionary to maintain numerical labelsclass_dic = {"A":0,"B":1,"C":2}
```

```
# dictionary to maintain countsclass_count = {'A':0,'B':0,'C':0}
```

```
# training listsX = []Y = []
```

```
# validation listsX_val = []Y_val = []
```

```
# testing listsX_test = []Y_test = []
```

```
for file_name in files:  label = file_name[0]  if label in class_dict:    path = data_folder_path+'/'+file_name    image = cv2.imread(path)    resized_image = cv2.resize(image,(224,224))    if class_count[label]<2000:      class_count[label]+=1      X.append(resized_image)      Y.append(class_dic[label])    elif class_count[label]>=2000 and class_count[label]<2750:      class_count[label]+=1      X_val.append(resized_image)      Y_val.append(class_dic[label])    else:      X_test.append(resized_image)      Y_test.append(class_dic[label])
```

```
# one-hot encodings of the classesY = np_utils.to_categorical(Y)Y_val = np_utils.to_categorical(Y_val)Y_test = np_utils.to_categorical(Y_test)
```

```
if not os.path.exists('Numpy_folder'):    os.makedirs('Numpy_folder')
```

```
np.save(npy_data_path+'/train_set.npy',X)np.save(npy_data_path+'/train_classes.npy',Y)
```

```
np.save(npy_data_path+'/validation_set.npy',X_val)np.save(npy_data_path+'/validation_classes.npy',Y_val)
```

```
np.save(npy_data_path+'/test_set.npy',X_test)np.save(npy_data_path+'/test_classes.npy',Y_test)
```

```
print("Data pre-processing Success!")
```

Now comes the training part! Let us start by importing the essential modules so we can construct and train the CNN AlexNet. Here it is primarily done using Keras.

```
# importing from keras.optimizers import SGDfrom keras.models import Sequentialfrom keras.preprocessing import imagefrom keras.layers.normalization import BatchNormalizationfrom keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D
```

```
print("Imported Network Essentials")
```

We next go for loading the images stored in the form of .npy:

```
X_train=np.load(npy_data_path+"/train_set.npy")Y_train=np.load(npy_data_path+"/train_classes.npy")
```

```
X_valid=np.load(npy_data_path+"/validation_set.npy")Y_valid=np.load(npy_data_path+"/validation_classes.npy")
```

```
X_test=np.load(npy_data_path+"/test_set.npy")Y_test=np.load(npy_data_path+"/test_classes.npy")
```

We then head towards defining the structure of our CNN. Assuming prior knowledge of the [AlexNet](https://www.learnopencv.com/understanding-alexnet/) architecture, here is the Keras code for that.

```
model = Sequential()
```

```
# 1st Convolutional Layermodel.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11),strides=(4,4), padding='valid'))model.add(Activation('relu'))
```

```
# Max Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Batch Normalisation before passing it to the next layermodel.add(BatchNormalization())
```

```
# 2nd Convolutional Layermodel.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Max Poolingmodel.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 3rd Convolutional Layermodel.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 4th Convolutional Layermodel.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 5th Convolutional Layermodel.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Max Poolingmodel.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# Passing it to a dense layermodel.add(Flatten())
```

```
# 1st Dense Layermodel.add(Dense(4096, input_shape=(224*224*3,)))model.add(Activation('relu'))
```

```
# Add Dropout to prevent overfittingmodel.add(Dropout(0.4))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 2nd Dense Layermodel.add(Dense(4096))model.add(Activation('relu'))
```

```
# Add Dropoutmodel.add(Dropout(0.6))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 3rd Dense Layermodel.add(Dense(1000))model.add(Activation('relu'))
```

```
# Add Dropoutmodel.add(Dropout(0.5))
```

```
# Batch Normalisationmodel.add(BatchNormalization())
```

```
# Output Layermodel.add(Dense(24))model.add(Activation('softmax'))
```

```
model.summary()
```

The `Sequential` model is a linear stack of layers. We add the convolutional layers (applying filters), activation layers (for non-linearity), max-pooling layers (for computational efficiency) and batch normalization layers (to standardize the input values from the previous layer to the next layer) and the pattern is repeated five times.

The Batch Normalization layer was introduced in 2014 by Ioffe and Szegedy. It addresses the vanishing gradient problem by standardizing the output of the previous layer, it speeds up the training by reducing the number of required iterations, and it enables the training of deeper neural networks.

At last, 3 fully-connected dense layers along with dropouts (to avoid over-fitting) are added.

To get the summarized description of the model, use model.summary().

The following is the code for the compilation part of the model. We define the optimization method to follow as SGD and set the parameters.

```
# Compile sgd = SGD(lr=0.001)
```

```
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
```

```
checkpoint = keras.callbacks.ModelCheckpoint("Checkpoint/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, 
```

```
save_best_only=False, save_weights_only=False, mode='auto', period=1)
```

`lr` in SGD is the learning rate. Since this is a categorical classification, we use categorical_crossentropy as the loss function in `model.compile`. We set the optimizer to be `sgd`_,_ the SGD object we have defined and set the evaluation metric to be accuracy.

While using GPU, sometimes it may happen to interrupt its running. Using checkpoints is the best way to store the weights we had gotten up to the point of interruption, so that we may use them later. The first parameter is to set the place to store: save it as `weights.{epoch:02d}-{val_loss:.2f}.hdf5` in the Checkpoints folder.

Finally, we save the model in the json format and weights in .h5 format. These are thus saved locally in the specified folders.

```
# serialize model to JSONmodel_json = model.to_json()with open("Weights_Full/model.json", "w") as json_file:    json_file.write(model_json)
```

```
# serialize weights to HDF5model.save_weights("Weights_Full/model_weights.h5")print("Saved model to disk")
```

Let’s look at the whole code of defining and training the network. Consider this as a separate file ‘training.py’.

```
# training.py
```

```
from keras.optimizers import SGDfrom keras.models import Sequentialfrom keras.preprocessing import imagefrom keras.layers.normalization import BatchNormalizationfrom keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D
```

```
print("Imported Network Essentials")
```

```
# loading .npy datasetX_train=np.load(npy_data_path+"/train_set.npy")Y_train=np.load(npy_data_path+"/train_classes.npy")
```

```
X_valid=np.load(npy_data_path+"/validation_set.npy")Y_valid=np.load(npy_data_path+"/validation_classes.npy")
```

```
X_test=np.load(npy_data_path+"/test_set.npy")Y_test=np.load(npy_data_path+"/test_classes.npy")
```

```
X_test.shape
```

```
model = Sequential()# 1st Convolutional Layermodel.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11),strides=(4,4), padding='valid'))model.add(Activation('relu'))# Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Batch Normalisation before passing it to the next layermodel.add(BatchNormalization())
```

```
# 2nd Convolutional Layermodel.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Poolingmodel.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 3rd Convolutional Layermodel.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 4th Convolutional Layermodel.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 5th Convolutional Layermodel.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Poolingmodel.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# Passing it to a dense layermodel.add(Flatten())# 1st Dense Layermodel.add(Dense(4096, input_shape=(224*224*3,)))model.add(Activation('relu'))# Add Dropout to prevent overfittingmodel.add(Dropout(0.4))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 2nd Dense Layermodel.add(Dense(4096))model.add(Activation('relu'))# Add Dropoutmodel.add(Dropout(0.6))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# 3rd Dense Layermodel.add(Dense(1000))model.add(Activation('relu'))# Add Dropoutmodel.add(Dropout(0.5))# Batch Normalisationmodel.add(BatchNormalization())
```

```
# Output Layermodel.add(Dense(24))model.add(Activation('softmax'))
```

```
model.summary()
```

```
# (4) Compile sgd = SGD(lr=0.001)model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])checkpoint = keras.callbacks.ModelCheckpoint("Checkpoint/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)# (5) Trainmodel.fit(X_train/255.0, Y_train, batch_size=32, epochs=50, verbose=1,validation_data=(X_valid/255.0,Y_valid/255.0), shuffle=True,callbacks=[checkpoint])
```

```
# serialize model to JSONmodel_json = model.to_json()with open("Weights_Full/model.json", "w") as json_file:    json_file.write(model_json)# serialize weights to HDF5model.save_weights("Weights_Full/model_weights.h5")print("Saved model to disk")
```

When we run the training.py file, we get to see something as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/QPaPyUKNcBciGmQDLii7chrt-EMmvZ3lDs7T)

For example, considering the first epoch of 12(Epoch 1/12):

* it took 1852s to complete that epoch
* the training loss was 0.2441
* accuracy was 0.9098 on the validation data
* 0.0069 was the validation loss, and
* 0.9969 was the validation accuracy.

So based on these values, we know the parameters of which epochs are performing better, where to stop training, and how to tune the hyperparameter values.

Now it’s time for testing!

```
# test.py
```

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning) from keras.preprocessing import imageimport numpy as npfrom keras.models import model_from_jsonfrom sklearn.metrics import accuracy_score 
```

```
# dimensions of our imagesimage_size = 224 
```

```
# load the model in json formatwith open('Model/model.json', 'r') as f:    model = model_from_json(f.read())    model.summary()model.load_weights('Model/model_weights.h5')model.load_weights('Weights/weights.250-0.00.hdf5') 
```

```
X_test=np.load("Numpy/test_set.npy")Y_test=np.load("Numpy/test_classes.npy")
```

```
Y_predict = model.predict(X_test)Y_predict = [np.argmax(r) for r in Y_predict]
```

```
Y_test = [np.argmax(r) for r in Y_test] 
```

```
print("##################")acc_score = accuracy_score(Y_test, Y_predict)print("Accuracy: " + str(acc_score))print("##################")
```

From the above code, we load the saved model architecture and the best weights. Also, we load the .npy files (the Numpy form of the test set) and go for the prediction of these test set of images. In short, we just load the saved model architecture and assign it the learned weights.

Now the approximator function along with the learned coefficients (weights) is ready. We just need to test it by feeding the model with the test set images and evaluating its performance on this test set. One of the famous evaluation metrics is accuracy. The accuracy is given by `_accuracy_score_` of `sklearn.metrics`.

Thank you for reading! Happy learning! :)

