---
title: Python Project – How to Convert Multiple Images into a Single PDF File
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-07-19T20:13:36.000Z'
originalURL: https://freecodecamp.org/news/convert-multiple-images-into-a-single-pdf-file-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/alvaro-reyes-fSWOVc3e06w-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Creating projects is the best way to learn a programming language. It is
  fun and it''s a creative way to learn new things.

  Whenever I try to learn a new language or new technology, I try to create a project,
  whether it''s a small byte-sized or big proj...'
---

Creating projects is the best way to learn a programming language. It is fun and it's a creative way to learn new things.

Whenever I try to learn a new language or new technology, I try to create a project, whether it's a small byte-sized or big project.

In this article, I am going to show you a small but very cool project if you are a complete beginner learning Python.

You will create a project that will grab all of the image files from a particular directory and create a single PDF file that includes all of the images.

The interesting thing about Python is, you will need only 4 lines of code to achieve that! So, let's get started, shall we?

## 📦 Project Directory Structure

This is what my project directory looks like without Git.

```python
📦img2singlePDF
 ┣ 📜ImageContainingBook.pdf
 ┣ 📜jakub-neskora-A9tqu5iCFCQ-unsplash.jpg
 ┣ 📜raphael-renter-csae9W8JAsw-unsplash.jpg
 ┣ 📜README.md
 ┣ 📜sam-moghadam-khamseh-cU5TUyEaZXQ-unsplash.jpg
 ┣ 📜Script.py
 ┣ 📜sherry-christian-8Myh76_3M2U-unsplash.jpg
 ┗ 📜sunder-muthukumaran-fd6K_OFlnRA-unsplash.jpg
```

You can see what my project looks like with Git [in this repo](https://github.com/FahimFBA/img2singlePDF/blob/main/README.md). Don't forget to star the repository to show your love.

## 🎯 Project Set Up

To get started, first create a new folder for the project. Make sure that you do not include any spaces in the folder's name.

Add some image files in that directory. For this project, I am going to use the `.jpg` image files. Therefore I would suggest you to do the same thing!

You can download the royalty free images from [Unsplash](https://unsplash.com/) or [Pexels](https://unsplash.com/).

Keep in mind that our project can't handle large image files. So try to download those image files which are smaller in file size. You can select small files when downloading them from Unsplash.

You can also find the images in the `img` folder in the GitHub repository listed earlier on.

Next, open [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code is free and a widely used code editor.

If you prefer using a different editor, you can go ahead and open the project using the editor of your choice.

Now, create a Python file named `Script.py`. Here is where you will write down the code for this project.

Lastly, install the package/library named `img2pdf`. This library is used for converting images to PDF via direct JPEG inclusion. You can check this [website](https://pypi.org/project/img2pdf/) for more details.

I am going to install it using `pip`. Open a terminal window and enter the command `pip install img2pdf` .

## 💻 Let's Write Some Code

We can work with some pre-defined libraries. If we do that, then we do not necessarily need to write everything from scratch.

Python already has a ton of libraries, and we can directly use their pre-defined functionality. But for that, we need to import those libraries before trying to work with them.

First, you need to import the relevant 2 packages/modules/libraries named `os` and `img2pdf`. If you want to work with some pre-defined libraries/modules, then it is necessary to mention them earlier as the interpreter would find them before proceeding to work on those specific libraries.

We need the `os` library. This module comes under Python's standard utility modules.

The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. As we will use the file directory from our local storage, it is necessary for our task.

For importing a library in Python, we simply use `import library_name`. In this case, we used `import os` to import the `os` library. After importing a library we can use them anytime we want in that script or Python file.

As for the other library, `img2pdf`, remember that we are going to use this library for converting our image files to PDF files.

For importing the `img2pdf` library, we use the same import command, `import img2pdf`.

After importing the necessary two libraries, we can use them in our script anytime we want, and we can also use all of the functionality of the two libraries. It makes our tasks easier and our code shorter. Before doing that, make sure that you have already installed the `img2pdf` library using `pip` or `conda`.

Now I need to specify exactly in which file format and file name I want to place my image files. I will create a specific PDF file where all of the images will be integrated. Therefore I will specify that using the file use command.

The command structure is something like `with open ("Target_Filename.extension", "mode") as file:`.

Therefore, our command would be:

```python
with open("ImageContainingBook.pdf", "wb") as file:
```

This will create a PDF file named `ImageContainingBook.pdf` and integrate all of the image files there.

If you want to have a different file name, then you can change the name, but make sure to not keep any spaces in the file name. For example, do not use any file names like `my pdf.pdf`. Instead of using any space, use underscore ( `_` ), like `my_pdf.pdf`. But I prefer to use something like `myPDF.pdf`.

And check that you have also included the file extension ( in this case, you are working with a PDF file so the file extension must need to be `.pdf`).

As we will write in that file and we will work on the binary files, we have used the formatting as the `wb`. The `wb` indicates that the file is opened for writing in binary mode.

According to a solution from [StackOverflow](https://stackoverflow.com/questions/2665866/what-does-wb-mean-in-this-code-using-python):

> "When writing in binary mode, Python makes no changes to data as it is written to the file. In text mode (when the `b` is excluded as in just `w` or when you specify text mode with `wt`), however, Python will encode the text based on the default text encoding. Additionally, Python will convert line endings (`\n`) to whatever the platform-specific line ending is, which would corrupt a binary file like an `exe` or `png` file."

Then I need to specify what I want to do with the file.

I want to write in that file and I want the conversion functionality of the `img2pdf` library.

In my directory, there might be a lot of different files and that is natural. But as I only want to convert the image files which have a `.jpeg` extension in them, I need to specify that explicitly.

Also, I definitely need to include the file directory where it will get all of the images.

Therefore the last line of our script would be:

```python
file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")])) # Change the file directory accordingly
```

Let me explain the code now.

`os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf")`: This line uses the `os` module to list all the files in the directory specified by the given path. In this case, it is the directory "C:\\Users\\fahim\\Desktop\\ImageToPdf".

`[i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")]`: This is a list comprehension that filters the files obtained from the directory listing. It iterates through each file name in the directory and only includes those that end with the extension ".jpg". This step ensures that only JPEG images will be considered for the conversion to PDF.

`img2pdf.convert(...)`: The `img2pdf` library provides the `convert` function, which takes a list of image file paths and converts them into a single PDF file. The code passed inside the parentheses is generating the list of image file paths (JPEG images ending with ".jpg") using the list comprehension.

`file.write(...)`: It seems that `file` is a file object that was opened in write mode. The `write` method is being used to write the PDF content to the file.

To use this code successfully, you need to make sure of the following:

* That the `img2pdf` library is installed in your Python environment.
    
* Replace the directory path `"C:\\Users\\fahim\\Desktop\\ImageToPdf"` with the path to the directory containing the JPEG images you want to convert to PDF.
    
* That you have appropriate write permissions for the specified directory and file.
    

It's important to note that the code converts all the JPEG images in the specified directory into a single PDF file. If there are other file types or non-image files in that directory, they will be ignored during the conversion.

In a nutshell, the entire Python script is:

```python
import os
import img2pdf
with open("ImageContainingBook.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")])) # Change the file directory accordingly
```

Make sure to include an extra backspace in the file directory. We do this because we want to notify it that it is not an escape sequence, but is part of that directory path string.

If we want, then we can modify the code more. Another example of using the same code by breaking them down into individual segments can be like below:

```python
import os
import img2pdf

# Replace the directory path with the folder containing JPEG images to be converted
directory_path = "C:\\Users\\fahim\\Desktop\\img2singlePDF"

# List all files in the directory and filter only JPEG images (ending with ".jpg")
image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]

# Convert the list of JPEG images to a single PDF file
pdf_data = img2pdf.convert(image_files)

# Write the PDF content to a file (make sure you have write permissions for the specified file)
with open("output.pdf", "wb") as file:
    file.write(pdf_data)
```

Again, let me provide the explanation for all of the lines in detail:

1. First, we import the necessary modules: `os` to interact with the file system and `img2pdf` for image-to-PDF conversion.
    
2. The `directory_path` variable should be replaced with the path to the folder containing the JPEG images that need to be converted.
    
3. Using list comprehension, we obtain a list of image files in the specified directory, filtering only those with the ".jpg" extension. These are the images that will be included in the PDF.
    
4. The `img2pdf.convert(...)` function takes the list of image files and converts them into a single PDF file, storing the PDF content in the `pdf_data` variable.
    
5. We open a new file named "output.pdf" in binary write mode (`"wb"`) using a `with` statement to ensure proper file handling and closure.
    
6. Finally, we write the `pdf_data` content to the "output.pdf" file, effectively creating the PDF with the converted images.
    

Note: Before running the code, ensure that the `img2pdf` library is installed in your Python environment. You can install it using `pip install img2pdf`. Also, make sure you have the necessary write permissions for the specified directory and file.

## 🏃‍♂️ Run the Code

If you have the [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) extension installed on your VS Code, then you can run the file using that extension.

But if you like to run the code from your terminal then the command would be `python filename.py` for Windows and `python3 filename.py` for Mac or Linux.

As my filename is `Script.py` and I am using my Windows machine, my command would be `python Script.py`.

Instantly you will receive the PDF file which contains all of the image files (where the image files have a `.jpeg` file extension).

## 📺 Video Walkthrough

I know that many of you like to watch a video instead of following a complete article. Fear not! I have also created a complete video tutorial for you:

%[https://www.youtube.com/watch?v=zBZhfzgahsk] 

## 💁‍♂️ Conclusion

I hope you have enjoyed this short article. You should now be able to convert your images into a single PDF file in your own projects. 😊

If you have any questions then please let me know by reaching out on [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can also follow me on:  
🎁GitHub: [FahimFBA](https://github.com/FahimFBA)  
🎁YouTube: [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

Have a great day! 😊

🖼️ Cover: Photo by [Alvaro Reyes](https://unsplash.com/@alvarordesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/fSWOVc3e06w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
