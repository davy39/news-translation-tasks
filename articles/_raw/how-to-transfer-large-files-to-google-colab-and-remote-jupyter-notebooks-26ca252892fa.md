---
title: How to Upload large files to Google Colab and remote Jupyter notebooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T15:37:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-large-files-to-google-colab-and-remote-jupyter-notebooks-26ca252892fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_GgmGZJnFec994dvCDpbWQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Google
  slug: google
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bharath Raj

  If you haven’t heard about it, Google Colab is a platform that is widely used for
  testing out ML prototypes on its free K80 GPU. If you have heard about it, chances
  are that you gave it shot. But you might have become exasperated becau...'
---

By Bharath Raj

If you haven’t heard about it, [Google Colab](http://g.co/colab) is a platform that is widely used for testing out ML prototypes on its **free K80 GPU**. If you have heard about it, chances are that you gave it shot. But you might have become exasperated because of the complexity involved in transferring large datasets.

This blog compiles some of the methods that I’ve found useful for **uploading** and **downloading** **large files** from your local system to **Google Colab**. I’ve also included additional methods that can useful for transferring **smaller files** with less effort. Some of the methods can be extended to other **remote Jupyter notebook services,** like Paperspace Gradient.

### Transferring Large Files

The most efficient method to transfer large files is to use a cloud storage system such as **Dropbox** or **Google Drive**.

#### 1. Dropbox

Dropbox offers upto 2GB free storage space per account. This sets an upper limit on the amount of data that you can transfer at any moment. Transferring via Dropbox is relatively **easier**. You can also follow the same steps for **other notebook services**, such as **Paperspace Gradient**.

**Step 1: Archive and Upload**

Uploading a large number of images (or files) individually will take a very long time, since Dropbox (or Google Drive) has to individually assign IDs and attributes to every image. Therefore, I recommend that you archive your dataset first.

One possible method of archiving is to convert the folder containing your dataset into a ‘.tar’ file. The code snippet below shows how to convert a folder named “Dataset” in the home directory to a “dataset.tar” file, from your Linux terminal.

```bash
tar -cvf dataset.tar ~/Dataset
```

Alternatively, you could use WinRar or 7zip, whatever is more convenient for you. Upload the archived dataset to Dropbox.

**Step 2: Clone the Repository**

Open Google Colab and start a new notebook.

Clone this [GitHub repository](https://github.com/thatbrguy/Dropbox-Uploader.git). I’ve modified the [original](https://github.com/andreafabrizi/Dropbox-Uploader) code so that it can add the Dropbox access token from the notebook. Execute the following commands **one by one**.

```bash
!git clone https://github.com/thatbrguy/Dropbox-Uploader.git
cd Dropbox-Uploader
!chmod +x dropbox_uploader.sh
```

**Step 3: Create an Access Token**

Execute the following command to see the initial setup instructions.

```
!bash dropbox_uploader.sh
```

It will display instructions on how to obtain the access token, and will ask you to execute the following command. Replace the bold letters with your access token, then execute:

```bash
!echo "INPUT_YOUR_ACCESS_TOKEN_HERE" > token.txt
```

Execute **!bash dropbox_uploader.sh** again to link your Dropbox account to Google Colab. Now you can download and upload files from the notebook.

**Step 4: Transfer Contents**

**Download to Colab from Dropbox:**

Execute the following command. The argument is the name of the file on Dropbox.

```bash
!bash dropbox_uploader.sh download YOUR_FILE.tar
```

**Upload to Dropbox from Colab:**

Execute the following command. The first argument (result_on_colab.txt) is the name of the file you want to upload. The second argument (dropbox.txt) is the name you want to save the file as on Dropbox.

```bash
!bash dropbox_uploader.sh upload result_on_colab.txt dropbox.txt
```

#### 2. Google Drive

Google Drive offers upto 15GB free storage for every Google account. This sets an upper limit on the amount of data that you can transfer at any moment. You can always expand this limit to larger amounts. Colab simplifies the authentication process for Google Drive.

That being said, I’ve also included the necessary modifications you can perform, so that you can access Google Drive from other Python notebook services as well.

**Step 1: Archive and Upload**

Just as with Dropbox, uploading a large number of images (or files) individually will take a very long time, since Google Drive has to individually assign IDs and attributes to every image. So I recommend that you archive your dataset first.

One possible method of archiving is to convert the folder containing your dataset into a ‘.tar’ file. The code snippet below shows how to convert a folder named “Dataset” in the home directory to a “dataset.tar” file, from your Linux terminal.

```bash
tar -cvf dataset.tar ~/Dataset
```

And again, you can use WinRar or 7zip if you prefer. Upload the archived dataset to Google Drive.

**Step 2: Install dependencies**

Open Google Colab and start a new notebook. Install PyDrive using the following command:

```bash
!pip install PyDrive
```

Import the necessary libraries and methods (The **bold** imports are only required for Google Colab. Do not import them if you’re not using Colab).

```py
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
```

**Step 3: Authorize Google SDK**

**For Google Colab:**

Now, you have to authorize Google SDK to access Google Drive from Colab. First, execute the following commands:

```py
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

You will get a prompt as shown below. Follow the link to obtain the key. Copy and paste it in the input box and press enter.

![Image](https://cdn-media-1.freecodecamp.org/images/hzfWkut06QN9A99io686hCuHLETczZemgM9Y)
_Prompt to authenticate user_

**For other Jupyter notebook services (Ex: Paperspace Gradient):**

Some of the following steps are obtained from PyDrive’s [quickstart guide](https://pythonhosted.org/PyDrive/quickstart.html).

Go to [APIs Console](https://console.developers.google.com/iam-admin/projects) and make your own project. Then, search for ‘Google Drive API’, select the entry, and click ‘Enable’. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’. You should see a menu such as the image shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/jP9acVWbTFaXXFctxTPZNSuw2EP2xqZZVg0R)

Set “Application Type” to “Other”. Give an appropriate name and click “Save”.

Download the OAuth 2.0 client ID you just created. **Rename** it to **client_secrets.json**

Upload this JSON file to your notebook. You can do this by clicking the “Upload” button from the homepage of the notebook (Shown Below). **(Note: Do not** use this button to upload your dataset, as it will be extremely time consuming.)

![Image](https://cdn-media-1.freecodecamp.org/images/dOEeYDLPP98VFZDSNqXTYxkzc9B6o8fsRdTn)
_Upload button shown in red_

Now, execute the following commands:

```py
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
```

The rest of the procedure is **similar** to that of Google Colab.

**Step 4: Obtain your File’s ID**

Enable link sharing for the file you want to transfer. Copy the link. You may get a link such as this:

```
https://drive.google.com/open?id=YOUR_FILE_ID
```

Copy only the bold part of the above link.

**Step 5: Transfer contents**

**Download to Colab from Google Drive:**

Execute the following commands. Here, **YOUR_FILE_ID** is obtained in the previous step, and **DOWNLOAD.tar** is the name (or path) you want to save the file as.

```py
download = drive.CreateFile({'id': 'YOUR_FILE_ID'})
download.GetContentFile('DOWNLOAD.tar')
```

**Upload to Google Drive from Colab:**

Execute the following commands. Here, **FILE_ON_COLAB.txt** is the name (or path) of the file on Colab, and **DRIVE.txt** is the name (or path) you want to save the file as (On Google Drive).

```py
upload = drive.CreateFile({'title': 'DRIVE.txt'})
upload.SetContentFile('FILE_ON_COLAB.txt')
upload.Upload()
```

### Transferring Smaller Files

Occasionally, you may want to pass just one csv file and don’t want to go through this entire hassle. No worries — there are much simpler methods for that.

#### 1. Google Colab files module

Google Colab has its inbuilt **files module**, with which you can upload or download files. You can import it by executing the following:

```
from google.colab import files
```

**To Upload:**

Use the following command to upload files to Google Colab:

```py
files.upload()
```

You will be presented with a GUI with which you can select the files you want to upload. It is **not recommended** to use this method for files of large sizes. It is very slow.

**To Download:**

Use the following command to download a file from Google Colab:

```py
files.download('example.txt')
```

This feature works best in **Google Chrome**. In my experience, it only worked once on Firefox, out of about 10 tries.

#### 2. GitHub

This is a “hack-ish” way to transfer files. You can create a GitHub repository with the small files that you want to transfer.

Once you create the repository, you can just clone it in Google Colab. You can then push your changes to the remote repository and pull the updates onto your local system.

But do note that GitHub has a hard limit of 25MB per file, and a soft limit of 1GB per repository.

> Thank you for reading this article! Leave some claps if you it interesting! If you have any questions, you could hit me up on [social media](https://thatbrguy.github.io/) or send me an email (bharathrajn98[at]gmail[dot]com).

