---
title: Facial recognition using OpenCV in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T15:29:37.000Z'
originalURL: https://freecodecamp.org/news/facial-recognition-using-opencv-in-java-92fa40c22f62
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fpDngO6lM5pDeIPOOezK1g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Java
  slug: java
- name: opencv
  slug: opencv
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Manish Bansal

  Ever since the Artificial Intelligence boom began — or the iPhone X advertisement
  featuring the face unlock feature hit TV screens — I’ve wanted to try this technology.
  However, once I started googling about it, I typically only foun...'
---

By Manish Bansal

Ever since the Artificial Intelligence boom began — or the iPhone X advertisement featuring the face unlock feature hit TV screens — I’ve wanted to try this technology. However, once I started googling about it, I typically only found code examples in Python. And being a Java enthusiast for seven years, I got demotivated seeing that. Therefore, I finally decided to hunt for Java open source libraries for this.

Currently, there are various Java libraries out there. But the most popular one I found was [OpenCV](https://github.com/opencv/opencv).

OpenCV is an open source computer vision library that has tons of modules like object detection, face recognition, and augmented reality. Although this library is written in C++, it also offers battle-tested Java bindings.

However, there is one issue. As part of its software release, it offers only a few modules (with Java bindings) out of the box — and facial recognition is not one of them. Therefore, to use it, you need to manually build it.

**Wait! What? Why?**

Yes — the reason cited by the OpenCV community is that the modules are not completely stable. Therefore, they are not bundled along with the standard release. Hence, they maintain them in a separate repository [here](https://github.com/opencv/opencv_contrib).

If you have no or very little C++ experience (like me), you must have already started to feel dizzy about building a C++ library yourself. But don’t worry, I am here to hold your hand and walk you through this tedious process. So let’s begin, shall we?

### Building OpenCV for Java from scratch

![Image](https://cdn-media-1.freecodecamp.org/images/UPSASYdL1mTRl1Y2WO8wo5ORbKIVlJ0SZ4zp)
_“Birds flying around a half-built building and construction site” by [Unsplash](https://unsplash.com/@danist07?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">贝莉儿 NG</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

You can find various resources for step by step instructions like [this](https://opencv-java-tutorials.readthedocs.io/en/latest/01-installing-opencv-for-java.html#install-opencv-3-x-under-windows), [this](https://www.learnopencv.com/install-opencv3-on-windows/), and [this](https://perso.uclouvain.be/allan.barrea/opencv/cmake_config.html). However, none of them worked perfectly for me, as one thing or another was missing. The closest I found, which helped me, is [this](https://opencv-java-tutorials.readthedocs.io/en/latest/01-installing-opencv-for-java.html#install-opencv-3-x-under-linux) one. However, you do not need to refer to it. You can follow below steps and you will be good.

First, you need to have the below software on your PC. Here, I am building a 64-bit version of the library as I own a 64 bit PC. But you can build it for 32-bit as well.

The required software is:

1. [Cmake](https://cmake.org) (I used 3.6.0 rc-4 version).
2. [Ant](https://ant.apache.org) (used internally for building JAR)
3. MinGW — W64 GCC-8.1.0
4. [64 bit JDK 1.8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

**A word about MinGW:** Here, to build this library, we need C++ compilers. You can use Visual Studio tools (VS), which is far better. However, I did not have the luxury to do that, as I built it on my office laptop and VS is licensed software unavailable to Java people here. Therefore, I had to use open source tools, and the best one is MinGW (Minimalist GNU for Windows).

Also, it is very important to use the correct version of MinGW. Download version [x86_64-posix-seh](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z), as there is thread support in this version. I have not tried all other versions. But version [x86_64-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/sjlj/x86_64-8.1.0-release-win32-sjlj-rt_v6-rev0.7z) does not work at all.

To give some more perspective, the build is done by the utility called **make** which comes as part of MinGW (bin/mingw32-make.exe). make is a task runner for C++ like “Ant” is for Java. But C++ code and make scripts are very much platform-dependent. Hence, to make the distributables platform-independent, the utility **CMake** is used. CMake generates platform-dependent make scripts.

### **Generating build configurations using CMake**

**Step 1:** Download the source code zip of both the [opencv](https://github.com/opencv/opencv/releases) and [opencv_contrib](https://github.com/opencv/opencv_contrib/releases), and extract them into a directory. Further, create a folder called “build” in the same directory (I created “build_posix” as visible in the screenshots).

**Step 2:** Open CMake. Point “where is the source code” to the opencv extracted folder. Further, point “where to build the binaries” to the “build” folder you created.

![Image](https://cdn-media-1.freecodecamp.org/images/3w-kaNsw1jy-wgJj27ivlgUpkB3nWbKhmSAg)

**Step 3:** Add the 64 bit JDK 1.8 bin folder, the MinGW bin folder, and the Ant bin folder to the “PATH” environment variables. This is important, as CMake will look in the environment variables for configuration. If this is not done, then we will have to configure CMake manually in step 5.

**In case you have multiple JDKs in your system and you already have some different JDK in “PATH” & you don’t want to add JDK 1.8 in “PATH”, you can skip this. But do configure it manually in step 5.**

**Step 4:** Press the “Configure” button and select “ MinGw Makefiles” and “finish”. After this, CMake will start configuring your project. It will take a while and, after it finishes configuring, it will show the current available configurations.

In case you are wondering if the configurations generated for you are correct, you can refer to the logs which got generated for me [here](https://pastebin.com/50rtPkt6) and compare.

![Image](https://cdn-media-1.freecodecamp.org/images/1yaCLCiHsbLeyhIyjrWmIfMJfH2VO0bXcdk9)

**Step 5:** Now comes the most important part — changing the configurations. First, click the checkboxes “Grouped” and “Advanced” to organize the configurations.

![Image](https://cdn-media-1.freecodecamp.org/images/HNOpUBXPSjKz6lJcJiTQcZxlxLPWVRSD6yKR)

* Verify that ANT_EXECUTABLE (search “ANT_EXECUTABLE” in the search box) and all five “JAVA” configurations are pointing to the 64-bit JDK 1.8. If Step 3 was done properly, then this will be correct. Otherwise, correct them.

![Image](https://cdn-media-1.freecodecamp.org/images/zKNLlpIu8mRydVeelgHNLs4CevTolRnHxTrP)

* Un-check Python (search “Python”) related check boxes under “BUILD” and “INSTALL” groups as we don’t need Python builds.

![Image](https://cdn-media-1.freecodecamp.org/images/zXNIv3AOYlE5jS7KKgBm3Gkp7rBZA2PfrGkS)

* Disable “WITH_MSMF” and “WITH_IPP & WITH_TBB”. These libs are only available for VS.
* Edit “OPENCV_EXTRA_MODULES_PATH” under “OPENCV” group and set it to the “modules” folder under the “opencv_contrib” source folder you extracted earlier.

![Image](https://cdn-media-1.freecodecamp.org/images/Vxz1vQr2-CoYNCn2HMyrkN0FjuI6pvTEZlOm)

After this, press the “Configure” button again. This will do the final configurations. You can refer to the logs which got generated for me [here](https://pastebin.com/B71iVjQT).

**Note**: Make sure to compare your “Configure” logs generated with the one I shared in pastebin above. If you find some **major** difference, then first try correcting your configurations and press “Configure” again. Otherwise, there are chances that your build will fail and that it will be more difficult to debug.

**Step 6:** After this, press “Generate”. It will take few seconds and then close CMake.

### **Compiling OpenCV**

Now, if all the configurations generated above are correct, this task will be a breeze (of 2–3 hours!). Just open the command prompt, go to the “build” folder, and execute the command below.

```
mingw32-make.exe  -j5 > buildLogs.txt
```

Here, `-j5` is added, which instructs the make utility to run five jobs in parallel. This will make your build faster, at least theoretically.

Further, do not forget to push the logs to a text file. These might get too big, in which case your command prompt window might truncate it. You need them in case compilation fails. You can refer to the compilation logs generated in my case [here](https://pastebin.com/r7RSXSDm).

**Note**: The order of log statements might not be the same for you, as the build is happening in five parallel threads.

Once the build is over, you can check the “bin” and “lib” folders inside your “build” directory. Inside “bin”, you will have all your opencv*.exe’s and libopencv*.dll’s and your compiled JAR. Further, “lib” will have your main dll (libopencv_javaxxx.dll) along with some more dependent files.

![Image](https://cdn-media-1.freecodecamp.org/images/mIygBsHnPC5flruoL8nFf3yEAF7P96QMYh6l)
_“bin” folder after successful compilation_

![Image](https://cdn-media-1.freecodecamp.org/images/ORUBTFMX5NhE0AjRxAfiLfoTAW4o3OnDR1VX)
_“lib” folder after successful compilation_

### Hands on with OpenCV face recognition API

![Image](https://cdn-media-1.freecodecamp.org/images/e3jIAxwvVbVXoR2L0sOeAUQ352nzncBolZYX)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Now that you have built the library, you first need to set up the environment variables, as well as the user library, in Eclipse.

1. Create a variable OPENCV_JAVA_BIN and point it to the “bin” folder generated inside your “build” directory.
2. Create OPENCV_JAVA_LIB and point it to the “lib” folder generated inside your “build” directory.
3. Append both the above variables to the “PATH” variable.
4. Open up your Eclipse and create a new user library which you will be using for your face recognition project. Go to “Window” > “Preferenc**es**”. From the menu, navigate under “Java” > “Build Path” > “User Libraries” and choose “New…” . Enter a name for the library — for example, opencv — and select the newly created user library. Choose “Add External JARs…” , and browse to select “opencv-3xx.jar” from your computer.

After this, there is **no need** to link the native library, as this was added to your “path” variables in Step 3.

Once you are done with this setup, you can clone my Git repository from [here](https://github.com/manishbansal8843/Opencv-facerec-java) and import the project into your Eclipse workspace. Further, you will need to add JDK 1.8 as well as the opencv user library (just created above) to this project. Once you are done, you will be ready to test your newly built OpenCV library.

As of this writing, there are three programs in this project.

* **HelloWorld**: you can run this to test if your OpenCV library setup is ok. If this does not work properly, you need to sort this out **first**. The only issues you will encounter at this point will be related to system environment variables or user library setup.
* **FaceDetection**: you can use this to test the face detection module. It is a different module from face recognition. This is a module which gets shipped along with standard release of OpenCV. As of this writing, we can provide an image as an input to the program, and it will detect all the faces inside the image. The output image has green rectangles drawn on all the detected faces.

![Image](https://cdn-media-1.freecodecamp.org/images/TzyLTh-v5ie9SpRVJH2rHyK3OPSpSHpvYWFJ)
_Input image for Face Detection program_

![Image](https://cdn-media-1.freecodecamp.org/images/csQYwDeXAiOBbv6AWCOxhlLMvqZ1wyaf0GRz)
_Output image of face detection program_

* **FaceRecognition:** the OpenCV facerec module includes three algorithms:

1. Eigenfaces
2. Fisherfaces
3. Local Binary Patterns Histograms.

For technical details on all these algorithms, you can refer [this](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html) official article. For demonstration purposes, I will show you how to use the Eigenfaces algorithm.

First, you need to [download](http://www.cl.cam.ac.uk/Research/DTG/attarchive/pub/data/att_faces.zip) training data from the face database. This data contains ten different images for each of 40 distinct subjects (400 images). For some subjects, the images were taken at different times, varying the lighting, facial expressions (open / closed eyes, smiling / not smiling), and facial details (glasses / no glasses). After extracting them on your computer, you need to prepare a .csv file containing the path of each image, along with their corresponding label.

To make it easy, I have one TrainingData.txt in my Git repository. However, you need to edit the file and alter the paths of images as per your computer directory location.

**Note**: the downloaded face database contains images in .pgm format. This format is **not supported** by Windows. To actually convert them to .jpg, I added PGMToJPGConverter to my repository. You can use to this to convert the images and have an actual look at the training data.

After this, you can run the face recognition program. Below are the steps performed in the program:

1. OpenCV library is [loaded](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L20) as usual.
2. The .csv file is read, and two ArrayList(s) are [created](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L24). One for the matrix of images and other for their corresponding labels.
3. Out of the 400 input images, the last entry in the list data structure is [removed and saved](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L26-L29) for testing the trained model later.
4. After that, the remaining 399 images are used for [training](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L34) the Eigenfaces algorithm.
5. Once training is complete, the model is asked to [predict](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L39) the label of the image we removed in step 3.

![Image](https://cdn-media-1.freecodecamp.org/images/3h2mUCWnXzKQeFfIMJpFMIGxLoAM80Bp6tP0)
_Output of Face Recognition Program_

Here, we can observe that the algorithm is able to predict the label of our test subject with a confidence value of 1807. The lower the value, the better the prediction. Similarly, you can perform this exercise with two other algorithms. The C++ code can be downloaded from [here](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#fisherfaces-in-opencv) and [here](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#local-binary-patterns-histograms-in-opencv).

> **Update (27th Dec 2018)**: In case you find building the openCV java bindings painful, then i have a good news for you. Recently, I have found an easier way to get all the openCV dependencies for java. For complete details, please refer my [another article](https://medium.com/@manishbansal8843/face-recognition-using-opencv-in-java-updated-8fc329863e52).

**Congratulations**!! ? You made it to the end. And if you liked ?this article, hit that clap button below ?. It means a lot to me and it helps other people see the story.

