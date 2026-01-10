---
title: What is Stratified Random Sampling? Definition and Python Example
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-11-15T16:33:52.000Z'
originalURL: https://freecodecamp.org/news/what-is-stratified-random-sampling-definition-and-python-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-viktorya-sergeeva--------10275085.jpg
tags:
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: null
seo_desc: 'When we wish to conduct an experiment on a population – for example, the
  entire population of a country – it is not always practical or realistic to include
  every subject (citizen) in the experiment.

  Instead, we rely on a sample, which is a subset of...'
---

When we wish to conduct an experiment on a population – for example, the entire population of a country – it is not always practical or realistic to include every subject (citizen) in the experiment.

Instead, we rely on a sample, which is a subset of the population, and then draw conclusions about the population based on the sample's results.

Now, drawing a sample from a population is known as sampling technique, and the manner in which the sample is drawn is essential to the result.

There are lot of sampling techniques out there, but in this tutorial we will look at one of them called stratified random sampling and how it works. Without further ado, let's get started.

## What is Stratified Random Sampling?

Before we go into the details of stratified random sampling, let's break the term down into bits so we can grasp it better. Let's start with stratified.

In the context of sampling, **stratified** means splitting the population into smaller groups or strata based on a characteristic. To put it another way, you divide a population into groups based on their features.

**Random** **sampling** entails randomly selecting subjects (entities) from a population. Each subject has an equal probability of being chosen from the population to form a sample (subpopulation) of the overall population.

So therefore, **stratified random sampling** is a sampling approach in which the population is separated into groups or strata depending on a particular characteristic. Then subjects from each stratum (the singular of strata) are randomly sampled.

You divide the population into groups based on a characteristic and then choose a subject or entity at random from each group.

## Types of Stratified Random Sampling

Stratified sampling is divided into two categories, which are:

* Proportionate stratified random sampling.
    
* Disproportionate stratified random sampling.
    

**Proportionate stratified random sampling** is a type of sampling in which the size of the random sample obtained from each stratum is proportionate to the size of the entire stratum's population.

In other words, the proportion of the entire stratum equals the proportion of the sample stratum. Consider the following example:

```python
students = {
    
    "Name": ["Ibrahim", "Ganiyat", "Joel", "Elijah", "Yusuf", "Nurain", 
            "Dayo", "David", "Olu", "Tobi"],
    
    "ID":  ['001', '002', '003', '004', '005', '006','007', '008', '009', '010'],
    
    "Grade": ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'B', 'A'],
    
    "Category": [1, 2, 2, 1, 3, 3, 1, 2, 3, 3]
}
df = pd.DataFrame(students)
>>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-35.png align="left")

The above dataframe contains students' names, IDs, grades, and categories. Assume we wish to stratify students based on their grade characteristics and sample 60% of students from each group. That means we will have three strata in the above dataframe, because we have three different grades.

We can sample it by typing the following:

```python
df_sample = df.groupby("Grade", group_keys=False).apply(lambda x:x.sample(frac=0.6))
```

Now what we did above is to group the dataframe into different strata using the `groupby()` method. Then we passed in the `Grade` feature. For each group (stratum) we randomly sampled out `0.6(60%)` of observation from it.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-36.png align="left")

Now if we look at the proportion for `df_sample` and `df`, we will see that the proportions for both dataframes are the same.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-37.png align="left")

**Disproportionate stratified random sampling**, on the other hand, involves randomly selecting strata without regard for proportion. In other words, sampling is done based on a specified number. Let's look at an example.

```python
df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(n=2))
```

In this code, you can see that we only specified the actual number of samples we want to achieve.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-38.png align="left")

Most of the time, you'll use proportionate stratified sampling. Disproportionate requires more expert knowledge. When performing stratified sampling you will most likely use proportionate sampling.

## Applications of Stratified Random Sampling

### 1\. Sampling Based on Shared Characteristic:

When one or more subjects in an experiment share characteristics, it suggests they are members of the same group (one subject can only be in a particular group).

For example, suppose 50 students take a test, and the grade range for the examination is merely A-E. So we can have students who are in the same grade group, for example, students who received an A (and it is impossible for a student to have two grades). As a result, they share the same characteristic or feature, which is grade.

So when you want to sample subjects based on shared characteristics, you should use stratified random sampling. This ensures that a member of a specific group will be included.

This is because stratified random sampling differs from simple random sampling, which is also a sampling technique. Stratified random sampling randomly samples out the population with no characteristics (that is, each subject of the population has equal chances of being picked).

As a result, simple random sampling cannot guarantee that a certain member of a particular group will be included in the sample.

Let's have a look at an example to see what we're talking about. Let's say we want to sample out 60% of students using both stratified and simple random sampling.

We can see the result for stratified random sampling below:

```python
df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(frac=0.6))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-39.png align="left")

And this is the result of simple random sampling:

```python
df.sample(frac= 0.6)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-40.png align="left")

We can see that students with C grades are not included in the sample. This is because in simple random sampling, every observation has an equal chance of being chosen because we are not sampling based on characteristics. This means that there is a chance that an observation will not be chosen.

In stratified random sampling, on the other hand, we consider all the groups we want to sample and then randomly sample from each group.

### 2\. Imbalanced Dataset:

An imbalanced dataset is a machine learning classification problem in which the two class labels in the target variable are not proportional to one another. In other words, one class has a higher count than the other, resulting in an imbalance.

In machine learning, stratified sampling is also used to obtain the same sample proportion for a train and test set if there is an imbalance in the dataset.

For example, a chronic disease dataset has an imbalance label as shown below. You can click [here](https://www.kaggle.com/datasets/mansoordaku/ckdisease/download?datasetVersionNumber=1) to download the dataset.

```python
df = pd.read_csv("kidney_disease.csv")
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-41.png align="left")

If we check the proportion label feature which is `classification`, we can see that it is imbalanced.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-42.png align="left")

Now let's say we want to split the train and test set using simple random sampling. We won't achieve the same proportion for the train and test set as the population proportion.

```python
from sklearn.model_selection import train_test_split
X = df.drop(columns = ["classification"])
y = df["classification"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-43.png align="left")

We can see that the label proportion for both `y_train` and `y_test` is not the same as the population proportion. To achieve the same proportion we can make use of the `stratify` parameter in `train_test_split` as shown below:

```python
from sklearn.model_selection import train_test_split
X = df.drop(columns = ["classification"])
y = df["classification"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y)
```

The above code shows that the dataset was stratified on the label. So with that we will achieve the same proportion as the population proportion.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-44.png align="left")

## Conclusion

In this tutorial, we looked at stratified sampling and how you can use it in statistics and machine learning. We also looked at the types of stratified sampling.

Thank you for your time.
