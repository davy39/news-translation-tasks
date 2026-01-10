---
title: How to Use Google Colab with VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-09T22:24:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-google-colab-with-vs-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/1_6glvkHvmHFc9JjcExBB3-w.jpeg
tags:
- name: Google Colab
  slug: google-colab
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By Davis David

  Google Colab and VS Code are two popular editor tools that many Python developers
  use. They''re great for developing efficient tech solutions or systems especially
  in the areas of Machine Learning and Data Science.

  If you''re a Python de...'
---

By Davis David

Google Colab and VS Code are two popular editor tools that many Python developers use. They're great for developing efficient tech solutions or systems especially in the areas of Machine Learning and Data Science.

If you're a Python developer or data scientist, you might already know how to use Google Colab. But did you know that you can set up VS Code on Google Colab and use it as an editor the same way as in your local machine?

**In this article, you will learn:**

1. How to install the colabcode Python package.
2. How to start VS Code (code server).
3. How to access the online VS Code.
4. How to open the terminal.
5. How to run a Python file.

## How to Use Google Colab with VS Code

### Open Colab Notebook

The first step is to launch a new colab notebook in your Google Colab. You can rename the file as you want.

For example, `run_vscode.ipynb`.

### Install colabcode Python package.

To use Google Colab with VS Code (code server), you need to install the colabcode Python package. This is an awesome open-source Python package developed by [Abhishek Thakur](https://github.com/abhishekkrthakur).

To install the package, run the following command in your notebook cell:

```
 !pip install colabcode
```

### Import ColabCode

The next step is to import the ColabCode class from the package.

```python
from colabcode import ColabCode
```

### Create an instance of ColabCode

After importing ColabCode, you need to create an instance of ColabCode and set the following arguments:

* **port** – The port you want to run the code-server on. For example port=10000
* **password** – You can set a password to protect your code-server from unauthorized access. This is an optional argument.
* **mount_drive** – If you want to use your Google drive. This is a Boolean argument which means you can set it to True or False. This is an optional argument.

```python
ColabCode(port=10000)
```

### Start the Code Server

After running the ColabCode instance, it will start the server and show the link to access the code server.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_2j1llmzWvkrJ1QcDX4TyKw.jpeg)

You need to click the link and it will open in a new tab.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_8WOTEo4531S7KEoE9qsocA.jpeg)

Now you can take advantage of a full-fledged code editor and run different experiments on the Colab VM.

**Note:** If you check on your Colab Notebook, you will see that the cell that runs the ColabCode instance is continuously running. Don't close your Colab notebook unless you want to close the code server that runs VS Code.

## Tips to use VS Code on Google Colab

After launching the code server, use the following tips to help you start using VS Code on Google Colab.

### Step 1: Open Terminal

To open the terminal on VS Code that runs on Google Colab, use the following shortcut command:

```command
Ctrl + Shift + `
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_LdynqUTdluFY53C3DwIfdg.jpeg)

### Step 2: Change the Theme if You Want

You can change the theme of the editor by clicking the setting icon (bottom-left corner) and then click "Color Theme". It will open a popup window with different theme options you can select.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_oRbVQGlo1juU6yh4ylOIwQ.jpeg)

### Step 3: Run a Python File

You can create a Python file by clicking the **"File"** section on the sidebar and then select a **"New File"** tab.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_8YC-QStbIB9sdzh3gV5krg-1.jpeg)

In the following example, you will see how to run a simple Python file that trains a machine-learning algorithm to classify iris flowers into three species (setosa, versicolor, or virginica) and then make a prediction.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_C21tD_JDFE6dh559nCmZ0Q-1.jpeg)

## Final Thoughts on Using Google Colab with VS Code

Congratulations 👏👏, you have made it to the end of this article! I hope you have learned something new. You can set up VS Code on Google Colab and take your coding to the next level.

You can also use the colabcode Python package on the **Kaggle** platform to run VS Code. You just need to follow the same steps mentioned above.

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post!

You can also find me on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).

And you can read more articles like this [here](https://hackernoon.com/u/davisdavid).

