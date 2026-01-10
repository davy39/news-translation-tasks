---
title: How to Deploy your NLP Model to Production as an API with Algorithmia
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-17T21:02:19.000Z'
originalURL: https://freecodecamp.org/news/deploy-ml-model-to-production-as-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/pexels-cottonbro-5053740.jpg
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: null
seo_desc: 'By Davis David

  Did you know that 90% of machine learning models never actually make it into production?

  This means that the topic of machine learning deployment is rarely discussed when
  people learn machine learning. As a result, many AI practitioner...'
---

By Davis David

Did you know that 90% of machine learning models never actually make it into production?

This means that the topic of machine learning deployment is rarely discussed when people learn machine learning. As a result, many AI practitioners know how to create useful ML models, but they find it difficult to deploy them into production. 

Needless to say, machine learning deployment is one of the more important skills you should have if you're going to work with ML models.

![Image](https://developers.decoded.africa/content/images/2020/10/1_jBjJw7jq71pw4iZkqyp2Uw.jpeg)

Model deployment is the process of integrating your model into an existing production environment. The model will receive input and predict an output for decision making for a specific use case. 

For example, a model can be deployed in an e-commerce site and it can predict if a review about a specific product is **positive** or **negative**.

> Only when a model is fully integrated with the business systems, we can extract real value from its predictions. - Christopher Samiullah

There are different ways you can deploy your machine learning model into production. But in today's article, you will learn how to deploy your NLP model into production as an API with Algorithmia.

In this article, you will learn:

* How to create an NLP model that detects spam SMS text messages
* How to use Algorithmia, a MLOps platform.
* How to deploy your model into the Algorithmia platform
* How to use your deployed NLP model in any Python application.

Our first step is to create a machine learning model that can detect spam SMS text messages. So let't get started!

## How to Build the ML Model

First, we need to build our model. Here are the steps you should follow to do that.

### Import Python Packages 

We first import all the importance python packages that we will use to load the data, preprocess the data, and create a text classification model.

```python
# import important modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from string import punctuation 

# sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    plot_confusion_matrix,
    f1_score,
    roc_auc_score,
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score, RandomizedSearchCV

# text preprocessing modules
from nltk.tokenize import word_tokenize
from cleantext import clean

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import re #regular expression


from wordcloud import WordCloud, STOPWORDS

# Download dependency
for dependency in (
    "brown",
    "names",
    "wordnet",
    "averaged_perceptron_tagger",
    "universal_tagset",
    "stopwords"
):
    nltk.download(dependency)

#nltk.download('stopwords')

import warnings
warnings.filterwarnings("ignore")
# seeding
np.random.seed(123)
```

### Load the Spam Dataset

Then we load the spam dataset from the data directory, like this:

```python
# load data
data = pd.read_csv("../data/spam.tsv", sep="\t")
```

Let's look at the first five rows of the dataset.

```python
# show top five rows
data.head()
```

![Image](https://developers.decoded.africa/content/images/2020/10/head.PNG)

The dataset has four columns, but we will focus only on the message and label columns.

Let’s check out the shape of the dataset:

```python
# check the shape
data.shape
```

output: (5572, 4)  
  
We have 5572 rows and 4 columns.

### How to Handle Missing Values

Sometimes data can have missing values. We can use the **isnull()** method from pandas to check if our dataset has any missing values.

```python
# check missing values
data.isnull().sum()
```

![Image](https://developers.decoded.africa/content/images/2020/10/check-missing.PNG)

The output shows that our dataset does not have any missing values.

### How to Evaluate Class Distribution

We can use the **value_counts()** method from the pandas package to evaluate the class distribution form our dataset.

```python
# evalute class distribution
data["label"].value_counts()
```

![Image](https://developers.decoded.africa/content/images/2020/10/class-distribution.PNG)

In this dataset we have more legitimate messages (ham) than spam messages.

### Exploratory Data Analysis

This is very important steps in creating your machine learning project. It helps you understand more about your dataset. 

In this step we are going to find frequent words that are used in both legitimate and spam messages. 

```python
# collect words from the dataset
def collect_words(data, label):
    collected_words = " "

    # iterate through the csv file
    for val in data.message[data["label"] == label]:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
            collected_words = collected_words + words + " "

    return collected_words
```

The above function called **collect_words()** will collect all words from the dataset according to their labels (ham or spam). 

Then we can visualize frequent words by using the **wordcloud** Python package. We will start with messages labeled as ham (legitimate).

```python
# visualize ham labeled sms
cloud_stopwords = set(STOPWORDS)
ham_words = collect_words(data, label="ham")

print("Total words {}".format(len(ham_words)))

wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=cloud_stopwords,
    min_font_size=10,
).generate(ham_words)

# plot the WordCloud image
plt.figure(figsize=(15, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
```

Total words: 349132

![Image](https://developers.decoded.africa/content/images/2020/10/first-cloud.png)

As you can see in the legit messages, the most frequent words are _will, gt, now, ok, call, want, got,_ and so on.

Now we can visualize the most frequent words in messages labeled as spam. 

```python
# visualize spam labeled sms
cloud_stopwords = set(STOPWORDS)
spam_words = collect_words(data, label="spam")

print("Total words {}".format(len(spam_words)))

wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=cloud_stopwords,
    min_font_size=10,
).generate(spam_words)

# plot the WordCloud image
plt.figure(figsize=(10, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
```

Total words: 104304

![Image](https://developers.decoded.africa/content/images/2020/10/second-cloud.png)

In the above figure it shows that the most frequent words are those like _call, claim, free, txt, mobile, reply, offer_ and so on.

### How to Process the Data

After exploring and analyzing the dataset, the next step is to preprocess the dataset into the right format before creating our machine learning model.

We first replace the ham and spam classes with numerical values. The ham class will be labeled as 0 and spam class will be labeled as 1.

```python
# replace ham to 0 and spam to 1
new_data = data.replace({"ham": 0, "spam": 1})
new_data.head()
```

![Image](https://developers.decoded.africa/content/images/2020/10/new-labeled.PNG)

The messages in this dataset contain a lot of unnecessary words and characters that we don't need when creating machine learning models. 

We will clean the messages by removing stopwords, numbers, and punctuation. Then we will change words into lower case, and finally convert each word into its base form by using the lemmatization process in the NLTK package.

The **text_cleaning()** function will handle all necessary steps to clean our dataset.

```
stop_words =  stopwords.words('english')

def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Clean the text, with the option to remove stop_words and to lemmatize word

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"ur", " your ", text)
    text = re.sub(r" nd "," and ",text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r" tkts "," tickets ",text)
    text = re.sub(r" c "," can ",text)
    text = re.sub(r" e g ", " eg ", text)
    text =  re.sub(r'http\S+',' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text) # remove numbers
    text = re.sub(r" u "," you ",text)
    text = text.lower()  # set in lowercase 
        
    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])
    
    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer() 
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    
    # Return a list of words
    return(text)
```

Now we can clean our dataset by using the **text_cleaning()** function.

```python
#clean the dataset 
new_data["clean_message"] = new_data["message"].apply(text_cleaning)
```

We then split our dataset into train and test data. The test size is 15% of the entire dataset.

```python
# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    new_data["clean_message"],
    new_data["label"],
    test_size=0.15,
    random_state=0,
    shuffle=True,
    stratify=data["label"],
)
```

The CountVectorizer method from scikit-learn will help us transform our cleaned dataset into numerical values. The method converts a collection of text documents to a matrix of token counts.

```python
# Transform text data 
vectorizer = CountVectorizer(lowercase=False)
vectorizer.fit(X_train)

#transform train data 
X_train_trans = vectorizer.transform(X_train)

#transform test data
X_text_trans = vectorizer.transform(X_test)
```

### How to Actually Create Our Model

We will train the Multinomial Naive Bayes algorithm to classify if a message is legitimate or spam. This is one of the most common algorithms used for text classification.

```python
# Create a classifier

spam_classifier = MultinomialNB()
    
```

Then we train our classifier by using cross validation to avoid overfitting.

```python
# Train the model with cross validation
scores = cross_val_score(spam_classifier,X_train_trans,y_train,cv=10,verbose=3,n_jobs=-1)
```

![Image](https://developers.decoded.africa/content/images/2020/10/first-cross-validation.PNG)

Let's see the mean score.

```python
# find the mean of the all scores
scores.mean()
```

output: 0.9767713936539371  
  
The mean of the scores is around 97.68%. Our model performs well, but we can improve its performance by optimizing its hyperparameter values with the Randomized Search method from scikit-learn.

```python
# fine turning model parameters

distribution = {"alpha": [1, 0.1, 0.01, 0.001, 0.0001, 0, 0.2, 0.3]}

grid = RandomizedSearchCV(
    spam_classifier,
    param_distributions=distribution,
    n_jobs=-1,
    cv=10,
    n_iter=20,
    random_state=42,
    return_train_score=True,
    verbose=2,
)
```

We will optimize the **alpha** hyparameter from our model to get the best value that will increase our model's performance. 

```python
# training with randomized search
grid.fit(X_train_trans, y_train)
```

![Image](https://developers.decoded.africa/content/images/2020/10/random-search.PNG)

To show the hyperparameter optimization results:

```python
# summarize the results of the random parameter search
print(grid.best_score_)
print(grid.best_estimator_)
print(grid.best_params_)
```

0.9767713936539371  
 MultinomialNB(alpha=1)  
 {'alpha': 1}

The best score is the same as the previous one. Now let's test our model with the test data.

```python
# predict on the test data
y_pred = spam_classifier.predict(X_text_trans)
```

The model's performance will be evaluated by using the **accuracy_score** evaluation metric.

```python
# check accuracy score
accuracy_score(y_test, y_pred)
```

output: 0.9760765550239234  
  
The accuracy of our model is around **97.6%**, which is good performance.

Another useful evaluation metric to use is **f1_score** when you have a class imbalance in your dataset.

```python
# check f1_ score
f1_score(y_test, y_pred)
```

output: 0.908256880733945  
  
The score is **0.91** which is closer to **1**. This means that our model has good performance and we can now deploy it to production.

The model will be saved in models directory.

```python
#save model 
import joblib 

joblib.dump(spam_classifier, '../models/spam-detection-model.pkl')
```

['../models/spam-detection-model.pkl']  
  
Our  Count Vectorizer will also be saved in the preprocessing directory.

```ptython
#save Vectorizer
joblib.dump(vectorizer,'../preprocessing/count_vectorizer.pkl')
```

['../preprocessing/count_vectorizer.pkl']

After creating our spam detection model, it's time to deploy it on the Algorithmia platform.

## What is Algorithmia?

[Algorithmia](https://algorithmia.com/) is a MLOps tool that provides a simple and faster way to deploy your machine learning model into production. 

Algorithmia specializes in **"algorithms as a service"**. It allows users to create code snippets that run the ML model and host them on Algorithmia. Then you can call your code as an API. 

Now your model can be used for different applications of your choice, such as web apps, mobile apps, or e-commerce with a simple API call from Algorithmia.

![Image](https://developers.decoded.africa/content/images/2020/11/190.png)

Algorithmia supports machine learning models developed by different programming languages such as R, Python, Java, and Scala. It also support popular machine and deep learning frameworks such as Pytorch, Tensorflow, scikit-learn, XGBoost, and Keras. 

Algorithmia uses both CPUs and GPUs on its serverless Artificial Intelligence layer to optimize cost and maximize its performance to match your needs.  
Currently, this platform has over 60,000 developers with 4,500 algorithms.

Here are six steps you need to follow to deploy your machine learning model on Algorithmia.

### Step 1: Create an Account on Algorithmia

The first step is to create an account in Algorithmia by visiting this page: [https://algorithmia.com/signup](https://algorithmia.com/signup).

### Step 2: Create a New Algorithm

After creating and confirming your account and email, the next step is to create a new algorithm by clicking the dropdown menu button named **"Create New"**. Then you just select **Algorithm** at the top right corner of the page.

![Image](https://developers.decoded.africa/content/images/2020/11/create--new-algorithm.PNG)

Then enter the algorithm's name, for example SMS SPAM DETECTION. In the **source code** section you can determines where your algorithm's source code will live. 

By default source code will be on the Algorithmia platform. You can choose to keep it on GitHub, but for this article we will use the default option.  
  
The next section specifies the environment. Algorithmia gives you different options to select different environment such as Python, R, JavaScript, Java and Scala. The default option is Python 3.X, and here we will continue with this option. Finally, click the "**Create new Algorithm**" button.

### Step 3: Upload the pre-trained Model & CountVectorizer to Algorithmia

You can upload your selected model to the data section by clicking **Data Sources** on the left panel of the Algorithmia platform. Then click the **My hosted data** directory where you can create a new folder to keep all your uploaded pkl files for this specific algorithm.  
  
Inside the "My hosted data" directory I created a new folder called **sms_spam_detection**. Then I uploaded our pre-trained model and trained CountVectorizer to convert text messages (sms) to a vector of term/token counts.

![Image](https://developers.decoded.africa/content/images/2020/11/data-source.PNG)

### Step 4: Add the source code

After uploading our pre-trained model, click on the **Source Code** tab. It will open an IDE where you add the source code to run the machine learning model we created. Here's how you add the source code:  
  
**(a) Import the packages**   
We first import important Python packages including Algorithmia that will call the algorithm we created.

```python
import sys
import joblib
import pickle
import numpy as np
import Algorithmia
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from string import punctuation
import re 
import nltk
#download dependency
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
```

NB: Algorithmia's platform will automatically import the Algorithmia Python package in the file.

**(b) Create the Client**   
We then create a client from the Algorithmia package which provides a standardized way of calling any Algorithm.

```python

# we are creating the variable in global scope to use throughout our algorithm.
client = Algorithmia.client()
```

**(c) Add functions to load the pre-trained model and countvectorizer pkl files**  
The **load_model()** function will load our pre-trained model from the data source directory and the **load_preprocessing()** function will load the countvectorizer file.

```python
def load_preprocessing():
    # Get file by name
    # Open file and load model
    file_path = 'data://Davis/sms_spam_detection/count-vectorizer.pkl'
    object_path = client.file(file_path).getFile().name
    # Open file and preprocessin object
    with open(object_path, 'rb') as f:
        object = joblib.load(f)
        return object    

def load_model():
    # Get file by name
    # Open file and load model
    file_path = 'data://Davis/sms_spam_detection/spam-detection-model.pkl'
    model_path = client.file(file_path).getFile().name
    # Open file and load model
    with open(model_path, 'rb') as f:
        model = joblib.load(f)
        return model

# Load model outside of the apply function so it only gets loaded once

model = load_model()
vectorizer = load_preprocessing()
```

**(d) Add the function to clean the text input**  
Here we will use the same **text_clean()** function to clean the sms messages.

```python
#set stopwords
stop_words = stopwords.words('english')

def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Clean the text, with the option to remove stop_words and to lemmatize word

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"ur", " your ", text)
    text = re.sub(r" nd ", " and ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r" tkts ", " tickets ", text)
    text = re.sub(r" c ", " can ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r'http\S+', ' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text)  # remove numbers
    text = re.sub(r" u ", " you ", text)
    text = text.lower()  # set in lowercase

    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])

    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)

    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)

    # Return a list of words
    return (text)
```

**(e) Add the function to pre-process the input**  
The **process_input()** method will preprocess the input sms before making a prediction.

```python
def process_input(input):
    # Preprocess and Create numpy array from the input
    
    message = str(input)
    clean_message = text_cleaning(message)
    
    #vectorize the message 
    vect_message = vectorizer.transform([clean_message])
    
    print(vect_message)
    
    return vect_message
```

**(f) Add the function to apply the model for prediction**  
The last function called **apply()** will be responsible for performing predictions from the pre-processed text sms. It will return _"normal message_" if the message is legitimate and _"spam message"_ if the message is spam.

```python
def apply(input):
    # pefrom prediction from the input. 
   
    message = process_input(input)
    prediction = model.predict(message)
    if prediction[0] == 0:
        return "normal message"
    else:
        return "spam message"

```

  
Finally we save the source code added in the file.

![Image](https://developers.decoded.africa/content/images/2020/11/ide.PNG)

### Step 5: Add Dependencies to Algorithmia

Click the **dependencies tab** from the UI and add the following packages that our model relies on:

* numpy
* joblib
* scikit-learn == 0.22.2.post1
* unidecode
*  nltk == 3.5

Then  click **save dependencies** in the bottom right corner:

![Image](https://developers.decoded.africa/content/images/2020/11/dependencies.PNG)

NB: The dependency file in Algorithmia is the same as a requirements.txt file which pulls the dependencies listed from PyPi.  
  
On the editor page click **build tab** at the top right to install all dependencies listed in the dependency file. If all dependencies are successfully installed, you will see that a specific version of your algorithm is now online and ready to be published.

![Image](https://developers.decoded.africa/content/images/2020/11/specific-version.PNG)

### Step 6: Publish the Algorithm

Our last step is to publish the algorithm. There are 3 steps to publishing an algorithm: documenting all changes, adding example input and output, and configuring the algorithm settings.

**(a) Document Changes**  
You will see your commit history and you'll be able to add a release note.

![Image](https://developers.decoded.africa/content/images/2020/11/document-changes.PNG)

**(b) Add an Example**  
In this section you create your sample input and output so that users can try your algorithm.

![Image](https://developers.decoded.africa/content/images/2020/11/input-and-output-example.PNG)

**(c) Configure Algorithm settings**   
Lastly, you select if your algorithm will be **public** (which means anyone can call it) or **private** (which means only owners can call it). You also need to set the royalty and then click the **publish** button at the bottom of the page.

![Image](https://developers.decoded.africa/content/images/2020/11/configure-settings.PNG)

Our NLP model has successfully been deployed on the Algorithmia platform. Let's see how we can use our deployed model in a Python application such as Flask or Django.

## How to Install the Algorithmia Python Client

We first install the Algorithmia Python Client by using PIP. This will help us call our code that runs the NLP model.

```command
pip install algorithmia
```

### Collect the API Key

Click the "API Key" tab on your algorithm panel to collect the API key that will help you call the code that runs the NLP model.

### Create the Algorithmia Client 

We first import the Algorithmia Python package and then create the algorithm client object

```python
import Algorithmia

# Authenticate with your API key
apiKey = "YOUR_API_KEY"

# Create the Algorithmia client object
client = Algorithmia.client(apiKey)
```

### Call the Algorithm 

To call the algorithm, we need to add the name of the algorithm with its version to the client object we have created. 

The name is **"Davis/spam_detection/0.2.0",** which includes the name of your account on Algorithmia followed by the name of the algorithm we created. The final bit is the version of the algorithm (0.2.0).

```
# Create the algorithm object using the Summarizer algorithm
algo = client.algo('Davis/spam_detection/0.2.0')

# Pass in input required by algorithm
input_sms = "Win a Â£1000 cash prize or a prize worth Â£5000"

try:
    # Get the result
    print(algo.pipe(input_sms).result)
except Exception as error:
    # Algorithm error if, for example, the input is not correctly formatted
    print(error)
```

For this example the model predicts that the sms is a **"spam message"**. Cool, it's working!

## Wrapping Up

Congratulations, you have made it to the end of this article!

You can download the dataset and notebook used in this article here: [https://github.com/Davisy/SMS-Spam-Text-Classification](https://github.com/Davisy/SMS-Spam-Text-Classification)

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post! I can also be reached on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).

