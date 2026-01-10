---
title: How to Build Machine Learning Models with Reliable Validation Scores
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-05T17:15:59.000Z'
originalURL: https://freecodecamp.org/news/build-machine-learning-models-with-reliable-validation-scores
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Untitled-presentation.jpg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "By Saheed Azeez\nImagine that you took a test in school, and you expected\
  \ to score 80-90% based on how you thought you performed. But when the results came\
  \ out, you learned that you scored 50-60% in the test. You'd be shocked, right?\
  \ \nWell sometimes t..."
---

By Saheed Azeez

Imagine that you took a test in school, and you expected to score 80-90% based on how you thought you performed. But when the results came out, you learned that you scored 50-60% in the test. You'd be shocked, right? 

Well sometimes these same scenarios play out in machine learning problems. You might build a machine learning model with very good validation performance, but in the real world, the model's performance is worse. 

A practical example is being ranked high in the public leaderboard of a machine learning contest on [Kaggle](https://www.kaggle.com/) and when the private (final) leaderboard is released, your ranking drops.

In this article, I'll be discussing how to build models that have validation scores that are closer to real world performance. I'll also talk about reasons why validation scores are often widely different from real world performance or leaderboard performance (for machine learning competitions). Finally, I'll give some tips to help you reduce this difference in performance.

### Here's what we'll cover:

1. [Prerequisites](#heading-prerequisites)
2. [What are Validation Scores in Machine Learning?](#heading-what-are-validation-scores-in-machine-learning)
3. [How to Build a Model with Good Validation Scores](#heading-how-to-build-a-model-with-good-validation-scores)
* [Select the right evaluation metrics](#select-the-right-evaluation-metrics)
* [Select the right train-validation split](#select-the-right-train-validation-split)
* [Handle train and test data of different distributions](#handle-train-and-test-data-of-different-distributions)
* [Manage data leakage](#manage-data-leakage)
* [Drop duplicate data points](#drop-duplicate-date-points)
* [Properly deal with outliers](#properly-deal-with-any-outliers)
* [Try cross validation](#try-cross-validation)
4. [Wrapping Up](#heading-wrapping-up)

## Prerequisites

If you have built a machine learning model before, then you should be able to understand and learn from this article.

## What Are Validation Scores in Machine Learning?

To learn what a validation score is, you have to first understand the different types of datasets used in model training and evaluation.

First, a **train dataset** is the initial data you want to build your model on. Your model will learn its parameters from the training data. This is usually represented with _X_ or _x_ or _train_ in most notebooks.

After building your model on the training data, you'll want to see how your model performs on data it hasn't seen before. That's where the **validation data** come in. Like the name implies, you use it to validate your model's performance. 

But most of the time, you won't have separate validation data to use – so you'll have to extract a percentage of your training data to validate the model. The performance of your model on the validation data is what is called the **validation score** or **validation performance**.

This is important because you are (or will eventually be) building a model to solve a business or real world problem. The model will be used to predict instances that you wouldn't have answers to (target), and that prediction is what matters the most. 

In a machine learning competition setting, you can call this real world problem the **test data.** The performance your model exhibits on this data is what is called the **real world performance**.

Note: What I call validation data could also be referred to as test data by other engineers, and what I call test data could be called real world performance data. I gave this description based on my Machine Learning contest experience.

## How to Build a Model with Good Validation Scores

### 1) Select the right evaluation metrics

One of the first steps before building a model based on your data is to identify what makes a good model. You should ask yourself the question "Why should model A be better than model B"? You have to use some sort of score that rates one model's performance over another. 

There are many metrics for both **classification** (f1-score, accuracy, roc auc score and a lot more) and **regression** (mean squared error, mean absolute error, mean Absolute Percentage Error and co) problems.

The evaluation metrics should also translate to the real world application of the model. 

For example, the evaluation metric for a regression model that is open to outliers **should be mean squared error** and not **mean absolute error**. For classification problems which involve imbalanced data, the preferred evaluation metrics should be **f1_score** over **accuracy** because it takes account of the data imbalance in its calculation. And so on.

Here's an example of applying evaluation metrics on a simple regression problem:

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Generate a sample dataset for demonstration purposes, with 1000 data points and 10 features
X, y = make_regression(n_samples=1000, n_features=10, noise=0.5, random_state=42)

# Split the dataset into training and valdation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a regression model (Linear Regression in this example)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_val)

# Calculate regression metrics
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

# Print the results
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/regression-metrics-1.png)
_Result from the metrics_

And here's an example of applying evaluation metrics on a simple classification problem:

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Generate a sample dataset for demonstration purposes
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the dataset into training and valdation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier (Random Forest in this example)
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Make predictions on the val set
y_pred = classifier.predict(X_val)
y_proba = classifier.predict_proba(X_val)[:, 1]  # Probability estimates for ROC-AUC and log_loss

# Calculate classification metrics
accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)
roc_auc = roc_auc_score(y_val, y_proba)
logloss = log_loss(y_val, y_proba)

# Print the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC-AUC Score: {roc_auc:.4f}")
print(f"Log Loss: {logloss:.4f}")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/classification-metrics.png)
_The result_

### 2) Select the right train-validation split

As I mentioned earlier, many times you'll have to split out a percentage of your train data to use as validation data. 

You might be familiar with the line of code below which helps split out the data:

```python
# Split the dataset into training and valdation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
```

So how do you know what percentage split to use?

Well, a simple answer is to find a balance between a percentage split that isn't too large – after all, you don't want to extract too much out of your train data and lose information – and one that isn't too small – so that your validation data isn't too small and you can trust the validation scores you'll be getting.

For tabular machine learning problems, a percentage split between **10% (0.1)** to **25% (0.25)** should be good enough.

### 3) Handle train and test data of different distributions

There are instances where the train data and test data (or the location where the model will be applied) are of different distributions. 

For example, let's say we're building a model to predict loan defaults. But while the train data available is from London, the model is targeted at users in Lagos. Although to some extent user behaviors are universal, there'll be some lifestyle or income differences between the locations that'll be reflected in the data and could also impact the model's performance. 

Since your validation data is extracted from train data (London location), the validation score might not be very reliable, as the model (trained on London users) might give, say, a 75% accuracy on the validation data (London users) – but it might have poorer accuracy on the real world, Lagos, because the **data distribution is different!**

The solution here will be to **drop some features** that might relate to London lifestyle and not Lagos. You might have to do some data exploration to identify those features – or better still, get some Lagos data to train the model on if it's available.

This is just an example showing how data distribution differences based on location can affect your model's results. There are many other factors that can cause data distribution differences like cultural, economic, or demographic variations.

You can drop features with the line of code below:

```python
dropped_features = ["feature1", "feature2", "feature3"]  # A list of features you want to drop
data.drop(dropped_features, axis=1, inplace=True)

```

### 4) Manage data leakage

You'd be very happy if your model scored a 99% f1_score or a mean squared error close to 0, in your validation performance. Well, such models are mostly impractical in the real world, and mostly occur due to **data leakage.**

Data leakage occurs when your model learns patterns or information during training that won't be available during the actual deployment or real-world use of the model.

A common cause of data leakage is when you forget to remove your target column or other columns that won't be available in the real world when you are applying your model from your train data before training the model. Since your validation data will also have this same information (since its extracted from your train data), it will thus give **an unrealistic score** that will not be attainable in the real world.

Another cause is when you have columns that indicate future values. Suppose you are predicting stock prices, and your dataset includes a feature that represents the average future stock prices of that week. This might cause future leakage because in the real world, you won't have the average stock price of that week (which includes value from the future) beforehand.

To prevent data leakage, it's essential to carefully preprocess and clean the data to ensure that only information available at the time of prediction is used during training.

You can also split the data into training and validation sets before any data preprocessing steps to simulate a real-world scenario for your validation set. Be cautious about using temporal data, and ensure that future information is not included when training the model.

### 5) Drop duplicate data points

There are many instances where the train data you'd be given will have duplicate data points (data instances where all the columns have the same values). In these cases, when you split the data into train and validation, there is a high chance that some data points in the train will also fall in the validation set. 

You'll want to avoid this, because the validation score you'll get won't tell the actual story of your model's performance in the real world, because your model has seen some of the data points you are using to validate it during training. It's like seeing your exam questions beforehand.

So, it's important to **drop duplicate data points** before splitting the data into train and validation.

Dropping duplicates in dataframes can easily be done with [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) like this:

```python
#where df is your dataframe
df.drop_duplicates(subset=None
                   keep='first',
                   inplace=False, 
                   ignore_index=False)
```

### 6) Avoid overfitting

Overfitting occurs when your model learns from the training data too well, capturing noise and specific patterns that are not generalizable to new data. 

Since your validation data is a subset extracted from your training data, the validation score might be **high** but the performance in the real world will be **poor**.

You can reduce the effect of regularization by applying techniques on your model such as dropout (for neural networks), pruning (for decision trees), or adding regularization terms to linear models.

Also, carefully tune hyperparameters to find the right balance between model complexity and generalization.

### 7) Properly deal with outliers

Outliers are data points that deviate significantly from the rest of the dataset. They can have a substantial impact on the performance of your model, especially if they are present in the **target** columns of regression problems. Presence of outliers can make the validation scores for regression problems very unreliable.

Let's see an example:

**Without outliers:**

```python
from sklearn.metrics import mean_squared_error,mean_absolute_error

#example target output
actual_val_target=[10,5,6,7,8,10,2,8,12,13]
#example prediction from a model
predicted_val_target=[9.5,5.2,5.8,7.3,7.5,10.4,0.5,8.1,12.5,12.8]

print(f"Root mean square error without outliers {mean_squared_error(actual_val_target,predicted_val_target,squared=False)}")
print(f"Mean absolute error without outliers {mean_absolute_error(actual_val_target,predicted_val_target)}")
```

The result can be seen below:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1703858169667/8e2156bc-4abe-4820-9d10-5bc91562af8d.png)

**With an outlier (50):**

```python

#13 has been replaced with 50 to be an outlier
actual_val_target=[10,5,6,7,8,10,2,8,12,50]
predicted_val_target=[9.5,5.2,5.8,7.3,7.5,10.4,0.5,8.1,12.5,12.8]

print(f"Root mean square error with outliers {mean_squared_error(actual_val_target,predicted_val_target,squared=False)}")
print(f"Mean absolute error with outliers {mean_absolute_error(actual_val_target,predicted_val_target)}")
```

Result:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1703858201531/73eb5b50-b7e4-4770-9e0f-457fbdcfd24b.png)

You can see that just one outlier can affect the validation score and make it unreliable. So, it's crucial to address outliers appropriately.

Some tips to handle outliers:

* **Identify and Understand Outliers:** Use statistical methods or visualization techniques to identify outliers in your data. Understand whether these outliers are genuine data points or errors in data collection.
* **Treatment Strategies:** Depending on the nature of the outliers, you can choose to remove them, transform them, or use robust models that are less sensitive to extreme values.
* **Consistent Handling:** Ensure that the same outlier-handling techniques are applied consistently to both the training and validation datasets to maintain consistency in data preprocessing.

### 8) Try cross validation

When building models, you typically split the data into two (train and validation). But by training the model on train alone, you've lost all the patterns that can be learned from the validation data.

What if you split your data into multiple folds?

You can validate the model on one fold and build the model on the others. Do this until you've used all the folds as validations. So, if your data was split into 10 folds, you can build models on 10 subsamples of the data. That's what cross validation is about.

You can find the average of the validation scores on each fold and this helps provide a more robust estimate of how well your model generalizes to unseen data. 

```python
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Generate a synthetic dataset for demonstration purposes
X, y = make_regression(n_samples=1000, n_features=10, noise=0.5, random_state=42)

# Create a linear regression model
regressor = LinearRegression()

# Example using cross_val_score
cv_scores = cross_val_score(regressor, X, y, cv=5, scoring='neg_mean_squared_error')
rmse_scores = np.sqrt(-cv_scores)  # Taking the square root to get RMSE

print("Cross-validated RMSE scores:", rmse_scores)
print("Mean RMSE:", np.mean(rmse_scores))

# Example using cross_val_predict
predicted_values = cross_val_predict(regressor, X, y, cv=5)
```

For more details on cross validation, you can check out sklearn's [_cross_val_score_](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html) and [_cross_val_predict_](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate).

## Wrapping Up

The most important takeaway from this article is that you should try as much as possible to simulate a real-world scenario for your validation set so your validation score can be as reliable as possible.

I wish you the best in your future models.

Thank you!

