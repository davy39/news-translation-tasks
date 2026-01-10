---
title: How to Download a Kaggle Dataset Directly to a Google Colab Notebook
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-02-08T19:39:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-kaggle-dataset-to-google-colab
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Kaggle-to-Colab.png
tags:
- name: Data Science
  slug: data-science
- name: Google Colab
  slug: google-colab
- name: kaggle
  slug: kaggle
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: 'Kaggle is a popular data science-based competition platform that has a
  large online community of data scientists and machine learning engineers.

  The platform contains a ton of datasets and notebooks that you can use to learn
  and practice your data sc...'
---

[Kaggle](https://www.kaggle.com/) is a popular data science-based competition platform that has a large online community of data scientists and machine learning engineers.

The platform contains a ton of datasets and notebooks that you can use to learn and practice your data science and machine learning skills. They even have competitions you can participate in.

Kaggle offers a 100% free platform for all users – but there are some restrictions depending on the resources you're using. 

For example, you can use their CPU system for an unlimited amount of time. But there are strict limitations on GPU and TPU usage. You can use their GPU for 30 hours and TPU for 20 hours in a week. It gets resets each week, and then you get a fresh 30 hours GPU usage and 20 hours TPU usage at the start of the new week.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_14-21.png)
_Kaggle Website_

Alongside Kaggle, there are another popular platforms for machine learning engineers and data scientists – like [Google Colaboratory](https://colab.google/), or Google Colab for short.

In Google Colab, you can also use their CPU and GPU, but the free versions have more limitations than the free Kaggle account. In Google Colab, you can not get any GPU computational power until they allocate it from their free units. You don't know how many hours you can use, and you don't even know if you have any chance to get units over the next few days. 

In order to get all the features, you need to subscribe to their pro plans which are quite expensive.

But sometimes you still may want to use Colab, in most cases for short tasks. In Colab, you can directly connect your Google Drive and use your datasets from there. You can also store your output from the notebook to Google Drive if you want.

When you're working on a project, though, sometimes you'll want to use datasets from Kaggle in Google Colab. So you'll need to download the dataset from Kaggle and upload that to Colab's temporary storage or your Google Drive. 

You can probably guess that this is a very time-consuming process. 

But there is a way that you can directly download a Kaggle dataset using an API call in the Google Colab's notebook! In this article, I am going to show you how you can do that.

## Table of Contents

I've broken this tutorial down into separate parts for better understanding. You can get a clear overview of the entire article here:

* [Types of Kaggle datasets](#heading-types-of-kaggle-datasets)
* [Prerequisites](#heading-prerequisites)
* [Setup Google Colab for using Kaggle API](#setup-google-colab-for-using-kaggle-api)
* [Install Kaggle library](#install-kaggle-library)
* [Mount Google Drive to Colab](#heading-mount-google-drive-to-colab)
* [Add the Kaggle API Token to Colab Notebook](#add-the-kaggle-api-token-to-colab-notebook)
* [Download Kaggle dataset](#download-kaggle-dataset)
* [Download Kaggle Competition dataset](#download-kaggle-competition-dataset)
* [Download Specifc file from Kaggle Competition dataset](https://www.freecodecamp.org/news/p/906afd5c-ae59-4f19-9fe3-662d110d63a7/download-specifc-file-from-kaggle-competition-dataset)
* [Conclusion](#heading-conclusion)

## Video

If you would like to watch all of the steps from a video, you're in luck – I made this video just for you:

%[https://www.youtube.com/watch?v=7Z0s-XDXR1E]

## Types of Kaggle Datasets

Normally Kaggle provides two types of datasets: typical datasets that anyone can upload, and competition datasets. In the competition datasets, the competition organizers typically add/upload the datasets. 

Even though you can download a Kaggle dataset easily, you can't download a competition dataset if you don't participate in that competition. But some competitions remain open, and you can access their datasets via "Late Submission". So just make sure to check.

## Prerequisites

To go through this tutorial and get the most ouf of it, you'll need a Kaggle account, and that is completely free. Simply head over to the official website of [Kaggle](https://www.kaggle.com/), and create an account if you don't have one already.

You'll also need Kaggle's API. Head over to the [settings](https://www.kaggle.com/settings) of your Kaggle account. Go to the API section, and click "Create New Token". Keep in mind that Kaggle does not allow you to keep multiple tokens. You can use only one active token for your Kaggle account.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_14-52.png)
_Kaggle API Token_

This will give you a `kaggle.json` file. Keep it safe, as you'll need to use it later.

You also need a Google account if you want to use Google Colab. You may already have one, but if you don't, go ahead and create a new account in Google.

Now, you can store your Kaggle JSON in your Google drive. I prefer to create a new folder and keep my JSON file there so that I can call that in Colab whenever I want.

## How to Setup Google Colab to Use the Kaggle API

You can simply open any Colab notebook where you want to use the Kaggle API to download the dataset.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-45.png)
_Google Colab_

### Install the Kaggle library

You need to install the Kaggle Python library before you start working with Kaggle. You can simply install it in the colab notebook using the command `! pip install kaggle`.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-46.png)
_Install Kaggle library in colab_

### Mount Google Drive to Colab

Now you need to mount your Google Drive to the Colab notebook, since you've uploaded your `kaggle.json` file inside your Google drive.

You can simply do that by using the two lines of code given below:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Make sure to give it permission to access your Google Drive:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-48.png)
_Give access to Google Drive_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-49.png)
_Mount Google Drive_

If you refresh the mounted folder icon, you will see your Google Drive and all of the content in the notebook.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-49_1.png)
_Find MyDrive in Notebook_

### Add the Kaggle API Token to the Colab Notebook

Now you need to add the Kaggle API token to the notebook. But before that, you can simply create a temporary directory for Kaggle at the temporary instance location on the Colab drive by using the command `! mkdir ~/.kaggle`.

Now you need to copy your uploaded JSON file to that temporary Kaggle directory. You need the URL where you uploaded your JSON file earlier. You can grab that link directly from the drive folder in the notebook.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-08-155504.png)
_Copy JSON file location_

You can get the path directly like this. 

Then you can use the copy command like below:

```bash
! cp kaggle_json_path ~/.kaggle/
```

For example, my JSON file is located at "/content/drive/MyDrive/Kaggle_API/kaggle.json", so my command would be:

```bash
! cp /content/drive/MyDrive/Kaggle_API/kaggle.json ~/.kaggle/
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-58_1.png)
_Copy JSON file_

Now you need to change the file permissions to read/write to the owner only for safety.

You can use the command below to achive that:

```bash
! chmod 600 ~/.kaggle/kaggle.json
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-59.png)
_Change file permission of kaggle.json file_

## How to Download the Kaggle Dataset

For downloading a typical Kaggle dataset, you have to find the dataset on Kaggle first.

Let's say I want to download the following dataset from Kaggle:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-01.png)
_Sample dataset_

Check the complete URL of the dataset, which in this case is:

[https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni](https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni)

%[https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni]

We need the "account_name_of_the_dataset_owner/dataset_path" string. From the URL, the account name of the dataset owner is mdfahimbinamin. The dataset path is fastsurfer-processed-3d-brain-mri-from-adni.

So to download this exact dataset from Kaggle to your Google colab, your command would be:

```bash
! kaggle datasets download mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-06.png)
_Downloading the Kaggle dataset to your Colab notebook_

The entire process happens on Google's Cloud PC. So the downloading speed should be quite fast.

By default, the datasets come as `.zip` file. So if you need to unzip that, you can simply use the command below:

```bash
! unzip dataset-path.zip
```

For example, my dataset name/path was "fastsurfer-processed-3d-brain-mri-from-adni". So I will use the following command:

```bash
! unzip fastsurfer-processed-3d-brain-mri-from-adni.zip
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-09.png)
_Unzip Kaggle Dataset_

That's it! 😊

## How to Download a Kaggle Competition Dataset

Before downloading a Competition dataset, you need to make sure that either you have joined that competition or that you've selected "Late Submission" using the same Kaggle account that you're using for Kaggle API token.

Suppose I'm joining the ConnectX competition on Kaggle.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-15.png)
_Connect X competition_

I need to click "Join Competition" to get access to their dataset.

But if I want to download a dataset from a past competition, I need to join their "Late Submission" to gain their dataset.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-16.png)
_Join a past competition_

After clicking on "Late Submission", I need to grab the URL. This time, I'm using the Binary Classification with a Bank Churn Dataset. The complete URL is: [https://www.kaggle.com/competitions/playground-series-s4e1/overview](https://www.kaggle.com/competitions/playground-series-s4e1/overview)

From the URL, I can see that the dataset is located at "playground-series-s4e1". So I will use the following command to download the dataset to my Google Colab notebook:

```bash
! kaggle competitions download playground-series-s4e1
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-19.png)
_Download dataset_

That's it! 😊

## How to Download a Specific File from a Kaggle Competition Dataset

Let's say, I want to download a specific file from a Kaggle competition dataset. I can also do that.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-21.png)
_dataset_

In the dataset used above, you can see that there are 3 files. Let's say I want to download the `test.csv` file only. 

To do this, the command would be strucutred like this: `! kaggle competitions download dataset-path -f file_name_with_extension`.

So my command would be:

```bash
! kaggle competitions download playground-series-s4e1 -f test.csv
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-23.png)
_Download specific file_

That's it! 😊

## Conclusion

I hope you have gained some valuable insights from the article.

If you have enjoyed the procedures step-by-step, then don't forget to let me know on [Twitter/X](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can follow me on [GitHub](https://github.com/FahimFBA) as well if you are interested in open source. Make sure to check [my website](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) as well!

If you like to watch programming and technology-related videos, then you can check my [YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1), too. You can also check my other writings on [Dev.to](https://dev.to/fahimfba).

All the best for your programming and development journey. 😊

You can do it! Don't give up, never! ❤️

