---
title: 'Preprocessing for deep learning: from covariance matrix to image whitening'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-16T22:44:23.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-hadrienj-preprocessing-for-deep-learning-9e2b9c75165c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ehXogigFyLpyy2q2sz80HA.png
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By hadrienj

  The goal of this post is to go from the basics of data preprocessing to modern techniques
  used in deep learning. My point is that we can use code (such as Python/NumPy) to
  better understand abstract mathematical notions. Thinking by codin...'
---

By hadrienj

The goal of this post is to go from the basics of data preprocessing to modern techniques used in deep learning. My point is that we can use code (such as Python/NumPy) to better understand abstract mathematical notions. Thinking by coding! ?

We will start with basic but very useful concepts in data science and machine learning/deep learning, like variance and covariance matrices. We will go further to some preprocessing techniques used to feed images into neural networks. We will try to get more concrete insights using code to actually see what each equation is doing.

**Preprocessing** refers to all the transformations on the raw data before it is fed to the machine learning or deep learning algorithm. For instance, training a convolutional neural network on raw images will probably lead to bad classification performances ([Pal & Sudeep, 2016](https://ieeexplore.ieee.org/document/7808140/)). The preprocessing is also important to speed up training (for instance, centering and scaling techniques, see [Lecun et al., 2012; see 4.3](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)).

Here is the syllabus of this tutorial:

**1. Background:** In the first part, we will get some reminders about variance and covariance. We will see how to generate and plot fake data to get a better understanding of these concepts.

**2. Preprocessing:** In the second part we will see the basics of some preprocessing techniques that can be applied to any kind of data — **mean normalization**, **standardization**, and **whitening**.

**3. Whitening images:** In the third part, we will use the tools and concepts gained in **1.** and **2.** to do a special kind of whitening called **Zero Component Analysis** (ZCA). It can be used to preprocess images for deep learning. This part will be very practical and fun ☃️!

Feel free to fork [the notebook associated with this post](https://github.com/hadrienj/Preprocessing-for-deep-learning)! For instance, check the shapes of the matrices each time you have a doubt.

### 1. Background

#### A. Variance and covariance

The variance of a variable describes how much the values are spread. The covariance is a measure that tells the amount of dependency between two variables.

A positive covariance means that the values of the first variable are large when values of the second variables are also large. A negative covariance means the opposite: large values from one variable are associated with small values of the other.

The covariance value depends on the scale of the variable so it is hard to analyze it. It is possible to use the correlation coefficient that is easier to interpret. The correlation coefficient is just the normalized covariance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GH0ou22oJEwAw89GkrS8-w.png)
_A positive covariance means that large values of one variable are associated with big values from the other (left). A negative covariance means that large values of one variable are associated with small values of the other one (right)._

The covariance matrix is a matrix that summarises the variances and covariances of a set of vectors and it can tell a lot of things about your variables. The diagonal corresponds to the variance of each vector:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5V2y7dyc7YclTRqdVjoOrQ.png)
_A matrix **A** and its matrix of covariance. The diagonal corresponds to the variance of each column vector._

Let’s just check with the formula of the variance:

![Image](https://cdn-media-1.freecodecamp.org/images/1*EpBVFBmFboZeAxANYe6PEg.png)

with **n** the length of the vector, and **x̄** the mean of the vector. For instance, the variance of the first column vector of **A** is:

![Image](https://cdn-media-1.freecodecamp.org/images/1*nIpi1287Raa-n9NKwVHrsA.png)

This is the first cell of our covariance matrix. The second element on the diagonal corresponds of the variance of the second column vector from **A** and so on.

**Note**: the vectors extracted from the matrix **A** correspond to the columns of **A**.

The other cells correspond to the covariance between two column vectors from **_A_**. For instance, the covariance between the first and the third column is located in the covariance matrix as the column 1 and the row 3 (or the column 3 and the row 1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ce3wTRBXCJUG7fFf95CQ9Q.png)
_The position in the covariance matrix. Column corresponds to the first variable and row to the second (or the opposite). The covariance between the first and the third column vector of **A** is the element in column 1 and row 3 (or the opposite = same value)._

Let’s check that the covariance between the first and the third column vector of **A** is equal to -2.67. The formula of the covariance between two variables **_X_** and **Y** is:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y1kVDzXPCxhRRsk8snmzTQ.png)

The variables **X** and **Y** are the first and the third column vectors in the last example. Let’s split this formula to be sure that it is crystal clear:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWZDmC8GrNL-xNqGG1CjyA.png)

1. The sum symbol (**Σ**) means that we will iterate on the elements of the vectors. We will start with the first element (**i=1**) and calculate the first element of **X** minus the mean of the vector **X**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aFL3dzKMDXf9vj2_J5tNPQ.png)

2. Multiply the result with the first element of **Y** minus the mean of the vector **_Y_**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AKo4naYravnW3-3NrwSXTg.png)

3. Reiterate the process for each element of the vectors and calculate the sum of all results.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lk6JZa0lHqswjKwD5wKziQ.png)

4. Divide by the number of elements in the vector.

**Example 1.**

Let’s start with the matrix **A**:

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6NqwIfr6XlHSL_NIXtXsA.png)

We will calculate the covariance between the first and the third column vectors:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BvbRAxHeb40LU5goEDsoLg.png)

and

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jx4vbnRDKW95fF2nYSygZg.png)

**x̄=3**, **ȳ=4**, and **n=3** so we have:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PcvOUuCgOCY_qQhLb5AimA.png)

Ok, great! That’s the value of the covariance matrix.

**Now the easy way**. With NumPy, the covariance matrix can be calculated with the function `np.cov`.

**It is worth noting** that if you want NumPy to use the columns as vectors, the parameter `rowvar=False` has to be used. Also, `bias=True` divides by **n** and not by **n-1**.

Let’s create the array first:

```
array([[1, 3, 5],       [5, 4, 1],       [3, 8, 6]])
```

Now we will calculate the covariance with the NumPy function:

```
array([[ 2.66666667, 0.66666667, -2.66666667],       [ 0.66666667, 4.66666667, 2.33333333],       [-2.66666667, 2.33333333, 4.66666667]])
```

Looks good!

**Finding the covariance matrix with the dot product**

There is another way to compute the covariance matrix of **A**. You can center **A** around 0. The mean of the vector is subtracted from each element of the vector to have a vector with mean equal to 0. It is multiplied with its own transpose, and divided by the number of observations.

Let’s start with an implementation and then we’ll try to understand the link with the previous equation:

Let’s test it on our matrix **A**:

```
array([[ 2.66666667, 0.66666667, -2.66666667],       [ 0.66666667, 4.66666667, 2.33333333],       [-2.66666667, 2.33333333, 4.66666667]])
```

We end up with the same result as before.

The explanation is simple. The dot product between two vectors can be expressed:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hdHYlHiK3s0IDwwWytJO0A.png)

That’s right, it is the sum of the products of each element of the vectors:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6zDuuYJtL6yiuE1CatrYDQ.png)
_The dot product corresponds to the sum of the products of each element of the vectors._

If **n** is the number of elements in our vectors and that we divide by **n**:

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNMJtFhQF2v56K1OLE0_Yw.png)

You can note that this is not too far from the formula of the covariance we have seen earlier:

![Image](https://cdn-media-1.freecodecamp.org/images/1*RYVpFx0lrkTEl_R92ocGgQ.png)

The only difference is that, in the covariance formula, we subtract the mean of a vector from each of its elements. This is why we need to center the data before doing the dot product.

Now, if we have a matrix **A**, the dot product between **A** and its transpose will give you a new matrix:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Qw42RtGhHQWXD4rkA-MTQ.png)
_If you start with a zero-centered matrix, the dot product between this matrix and its transpose will give you the variance of each vector and covariance between them, that is to say the covariance matrix._

This is the covariance matrix!

#### B. Visualize data and covariance matrices

In order to get more insights about the covariance matrix and how it can be useful, we will create a function to visualize it along with 2D data. You will be able to see the link between the covariance matrix and the data.

This function will calculate the covariance matrix as we have seen above. It will create two subplots — one for the covariance matrix and one for the data. The `heatmap()` function from [Seaborn](https://seaborn.pydata.org) is used to create gradients of colour — small values will be coloured in light green and large values in dark blue. We chose one of our palette colours, but you may prefer other colours. The data is represented as a scatterplot.

#### C. Simulating data

**Uncorrelated data**

Now that we have the plot function, we will generate some random data to visualize what the covariance matrix can tell us. We will start with some data drawn from a normal distribution with the NumPy function `np.random.normal()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C5wwjainirV9mQHDlei9SQ.png)
_Drawing sample from a normal distribution with NumPy._

This function needs the mean, the standard deviation and the number of observations of the distribution as input. We will create two random variables of 300 observations with a standard deviation of 1. The first will have a mean of 1 and the second a mean of 2. If we randomly draw two sets of 300 observations from a normal distribution, both vectors will be uncorrelated.

```
(300, 2)
```

**Note 1**: We transpose the data with `.T` because the original shape is `(2, 300)` and we want the number of observations as rows (so with shape `(300, 2)`).

**Note 2**: We use `np.random.seed` function for reproducibility. The same random number will be used the next time we run the cell.

Let’s check how the data looks like:

```
array([[ 2.47143516, 1.52704645],       [ 0.80902431, 1.7111124 ],       [ 3.43270697, 0.78245452],       [ 1.6873481 , 3.63779121],       [ 1.27941127, -0.74213763],       [ 2.88716294, 0.90556519],       [ 2.85958841, 2.43118375],       [ 1.3634765 , 1.59275845],       [ 2.01569637, 1.1702969 ],       [-0.24268495, -0.75170595]])
```

Nice, we have two column vectors.

Now, we can check that the distributions are normal:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wb8r7PRje6nunmN-iMrUyQ.png)

Looks good!

We can see that the distributions have equivalent standard deviations but different means (1 and 2). So that’s exactly what we have asked for.

Now we can plot our dataset and its covariance matrix with our function:

```
Covariance matrix:[[ 0.95171641 -0.0447816 ] [-0.0447816 0.87959853]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kq4mIBv4hFGzOuhoftcFVQ.png)

We can see on the scatterplot that the two dimensions are uncorrelated. Note that we have one dimension with a mean of 1 (y-axis) and the other with the mean of 2 (x-axis).

Also, the covariance matrix shows that the variance of each variable is very large (around 1) and the covariance of columns 1 and 2 is very small (around 0). Since we ensured that the two vectors are independent this is coherent. The opposite is not necessarily true: a covariance of 0 doesn’t guarantee independence (see [here](https://stats.stackexchange.com/questions/12842/covariance-and-independence)).

**Correlated data**

Now, let’s construct dependent data by specifying one column from the other one.

```
Covariance matrix:[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*r-OmoGkWJvkWqjFO0ltV3w.png)

The correlation between the two dimensions is visible on the scatter plot. We can see that a line could be drawn and used to predict **y** from **x** and vice versa. The covariance matrix is not diagonal (there are non-zero cells outside of the diagonal). That means that the covariance between dimensions is non-zero.

That’s great! We now have all the tools to see different preprocessing techniques.

### 2. Preprocessing

#### A. Mean normalization

Mean normalization is just removing the mean from each observation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ym0P7PyUgZlML1QlGeUlvQ.png)

where **X’** is the normalized dataset, **X** is the original dataset, and **x̅** is the mean of **X**.

Mean normalization has the effect of centering the data around 0. We will create the function `center()` to do that:

Let’s give it a try with the matrix **B** we have created earlier:

```
Before:
```

```
Covariance matrix:[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*PaAR5buk8ICGSyiTKAeh_w.png)

```
After:
```

```
Covariance matrix:[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeCA2GooKYzbVqevDVG0FA.png)

The first plot shows again the original data **B** and the second plot shows the centered data (look at the scale).

#### B. Standardization or normalization

Standardization is used to put all features on the same scale. Each zero-centered dimension is divided by its standard deviation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2PX6slhDPJkjibJiecX25Q.png)

where **X’** is the standardized dataset, **X** is the original dataset, **x̅** is the mean of **X**, and **σ** is the standard deviation of **_X_**.

Let’s create another dataset with a different scale to check that it is working.

```
Covariance matrix:[[ 0.95171641 0.83976242] [ 0.83976242 6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vTAyUBAcepxHyvX449hESQ.png)

We can see that the scales of **x** and **y** are different. Note also that the correlation seems smaller because of the scale differences. Now let’s standardize it:

```
Covariance matrix:[[ 1.          0.34500274] [ 0.34500274  1.        ]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0a6gXhWnLPBv8i-L7PbYKA.png)

Looks good. You can see that the scales are the same and that the dataset is zero-centered according to both axes.

Now, have a look at the covariance matrix. You can see that the variance of each coordinate — the top-left cell and the bottom-right cell — is equal to 1.

This new covariance matrix is actually the correlation matrix. The Pearson correlation coefficient between the two variables (**c1** and **c2**) is 0.54220151.

#### C. Whitening

Whitening, or sphering, data means that we want to transform it to have a covariance matrix that is the identity matrix — 1 in the diagonal and 0 for the other cells. It is called whitening in reference to white noise.

[Here are more details on the identity matrix.](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.3-Identity-and-Inverse-Matrices/)

Whitening is a bit more complicated than the other preprocessing, but we now have all the tools that we need to do it. It involves the following steps:

* Zero-center the data
* Decorrelate the data
* Rescale the data

Let’s take again **C** and try to do these steps.

1. **Zero-centering**

This refers to mean normalization (**2. A**). Check back for details about the `center()` function.

```
Covariance matrix:[[ 0.95171641  0.83976242] [ 0.83976242  6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AXOzdgC8gjiwpg-9AsfzKw.png)

**2. Decorrelate**

At this point, we need to decorrelate our data. Intuitively, it means that we want to rotate the data until there is no correlation anymore. Look at the following image to see what I mean:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ehXogigFyLpyy2q2sz80HA.png)

The left plot shows correlated data. For instance, if you take a data point with a big **x** value, chances are that the associated **y** will also be quite big.

Now take all data points and do a rotation (maybe around 45 degrees counterclockwise. The new data, plotted on the right, is not correlated anymore. You can see that big and small **y** values are related to the same kind of **x** values.

The question is: how could we find the right rotation in order to get the uncorrelated data?

Actually, it is exactly what the eigenvectors of the covariance matrix do. They indicate the direction where the spread of the data is at its maximum:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1SAoJ_o70IygSmDnKiCkmw.png)

The eigenvectors of the covariance matrix give you the direction that maximizes the variance. The direction of the **green** line is where the variance is maximum. Just look at the smallest and largest point projected on this line — the spread is big. Compare that with the projection on the **orange** line — the spread is very small.

For more details about eigendecomposition, see [this post](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/).

So we can decorrelate the data by projecting it using the eigenvectors. This will have the effect to apply the rotation needed and remove correlations between the dimensions. Here are the steps:

* Calculate the covariance matrix
* Calculate the eigenvectors of the covariance matrix
* Apply the matrix of eigenvectors to the data — this will apply the rotation  
   
Let’s pack that into a function:

Let’s try to decorrelate our zero-centered matrix **C** to see it in action:

```
Covariance matrix:[[ 0.95171641 0.83976242] [ 0.83976242 6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ok5JSx7zN4lg9FAcZOE6Ew.png)

```
Covariance matrix:[[ 5.96126981e-01 -1.48029737e-16] [ -1.48029737e-16 3.15205774e+00]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HmJGGe0cP6X-p0W-VuRfBg.png)

Nice! This is working.

We can see that the correlation is not here anymore. The covariance matrix, now a diagonal matrix, confirms that the covariance between the two dimensions is equal to 0.

**3. Rescale the data**

The next step is to scale the uncorrelated matrix in order to obtain a covariance matrix corresponding to the identity matrix.To do that, we scale our decorrelated data by dividing each dimension by the square-root of its corresponding eigenvalue.

**Note**: we add a small value (here 10^-5) to avoid division by 0.

```
Covariance matrix:[[ 9.99983225e-01 -1.06581410e-16] [ -1.06581410e-16 9.99996827e-01]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vFleYrVKknN5zwO3SNA5hQ.png)

Hooray! We can see that with the covariance matrix that this is all good. We have something that looks like an identity matrix — 1 on the diagonal and 0 elsewhere.

### 3. Image whitening

We will see how whitening can be applied to preprocess an image dataset. To do so we will use the paper of [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) where they give some details about the process. This preprocessing technique is called Zero component analysis (ZCA).

Check out the paper, but here is the kind of result they got. The original images (left) and the images after the ZCA (right) are shown.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YyKLLSzcAMX_9cCBbjP2sg.png)
_Whitening images from the CIFAR10 dataset. Results from the paper of [Pal &amp; Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/" rel="noopener" target="_blank" title=")._

First things first. We will load images from the CIFAR dataset. This dataset is available from Keras and you can also download it [here](https://www.cs.toronto.edu/~kriz/cifar.html).

```
(50000, 32, 32, 3)
```

The training set of the CIFAR10 dataset contains 50000 images. The shape of `X_train` is `(50000, 32, 32, 3)`. Each image is 32px by 32px and each pixel contains 3 dimensions (R, G, B). Each value is the brightness of the corresponding color between 0 and 255.

We will start by selecting only a subset of the images, let’s say 1000:

```
(1000, 32, 32, 3)
```

That’s better. Now we will reshape the array to have flat image data with one image per row. Each image will be `(1, 3072)` because 32 x 32 x 3 = 3072. Thus, the array containing all images will be `(1000, 3072)`:

```
(1000, 3072)
```

The next step is to be able to see the images. The function `imshow()` from Matplotlib ([doc](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html)) can be used to show images. It needs images with the shape (M x N x 3) so let’s create a function to reshape the images and be able to visualize them from the shape `(1, 3072)`.

For instance, let’s plot one of the images we have loaded:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ylvIdrsU1GyVkJwP6cwTdA.png)

Cute!

We can now implement the whitening of the images. [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) describe the process:

**1.** The first step is to rescale the images to obtain the range [0, 1] by dividing by 255 (the maximum value of the pixels).

Recall that the formula to obtain the range [0, 1] is:

![Image](https://cdn-media-1.freecodecamp.org/images/1*g8aDx7zkR7G4GoZzLJONhA.png)

but, here, the minimum value is 0, so this leads to:

![Image](https://cdn-media-1.freecodecamp.org/images/1*QSSqNJa6rbJGOEQMk_Jp0A.png)

```
X.min() 0.0X.max() 1.0
```

**Mean subtraction: per-pixel or per-image?**

Ok cool, the range of our pixel values is between 0 and 1 now. The next step is:

**2.** Subtract the mean from all images.

**Be careful here.**

One way to do it is to take each image and remove the mean of this image from every pixel ([Jarrett et al., 2009](https://www.computer.org/csdl/proceedings/iccv/2009/4420/00/05459469.pdf)). The intuition behind this process is that it centers the pixels of each image around 0.

Another way to do it is to take each of the 3072 pixels that we have (32 by 32 pixels for R, G and B) for every image and subtract the mean of that pixel across all images. This is called per-pixel mean subtraction. This time, each pixel will be centered around 0 **according to all images**. When you will feed your network with the images, each pixel is considered as a different feature. With the per-pixel mean subtraction, we have centered each feature (pixel) around 0. This technique is commonly used (e.g [Wan et al., 2013](http://proceedings.mlr.press/v28/wan13.html)).

We will now do the per-pixel mean subtraction from our 1000 images. Our data are organized with these dimensions `(images, pixels)`. It was `(1000, 3072)` because there are 1000 images with 32 x 32 x 3 = 3072 pixels. The mean per-pixel can thus be obtained from the first axis:

```
(3072,)
```

This gives us 3072 values which is the number of means — one per pixel. Let’s see the kind of values we have:

```
array([ 0.5234 , 0.54323137, 0.5274 , …, 0.50369804, 0.50011765, 0.45227451])
```

This is near 0.5 because we already have normalized to the range [0, 1]. However, we still need to remove the mean from each pixel:

Just to convince ourselves that it worked, we will compute the mean of the first pixel. Let’s hope that it is 0.

```
array([ -5.30575583e-16, -5.98021632e-16, -4.23439062e-16, …, -1.81965554e-16, -2.49800181e-16, 3.98570066e-17])
```

This is not exactly 0 but it is small enough that we can consider that it worked!

Now we want to calculate the covariance matrix of the zero-centered data. Like we have seen above, we can calculate it with the `np.cov()` function from NumPy.

**Please note** that our variables are our different images. This implies that the variables are the rows of the matrix **X**. Just to be clear, we will tell this information to NumPy with the parameter `rowvar=TRUE` even if it is `True` by default (see the [doc](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html)):

**Now the magic part** — we will calculate the singular values and vectors of the covariance matrix and use them to rotate our dataset. Have a look at [my post](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.8-Singular-Value-Decomposition/) on the singular value decomposition (SVD)if you need more details.

**Note**: It can take a bit of time with a lot of images and that’s why we are using only 1000. In the paper, they used 10000 images. Feel free to compare the results according to how many images you are using:

In the paper, they used the following equation:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ucN3UJIcEWsuYu1EZjA3KA.png)

with **U** the left singular vectors and **S** the singular values of the covariance of the initial normalized dataset of images, and **X** the normalized dataset. **ϵ** is an hyper-parameter called the whitening coefficient. **diag(a)** corresponds to a matrix with the vector **a** as a diagonal and 0 in all other cells.

We will try to implement this equation. Let’s start by checking the dimensions of the SVD:

```
(1000, 1000) (1000,)
```

**S** is a vector containing 1000 elements (the singular values). **diag(S)** will thus be of shape `(1000, 1000)` with **S** as the diagonal:

```
[[ 8.15846654e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 4.68234845e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 2.41075267e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] …,  [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 3.92727365e-05 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 3.52614473e-05 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 1.35907202e-15]]
```

```
shape: (1000, 1000)
```

Check this part:

![Image](https://cdn-media-1.freecodecamp.org/images/1*l5DfX7eqQvIgndc4B749Gg.png)

This is also of shape `(1000, 1000)` as well as **U** and **U^T**. We have seen also that **X** has the shape `(1000, 3072)`. The shape of **X_ZCA** is thus:

![Image](https://cdn-media-1.freecodecamp.org/images/1*2aSZTPJiOgdApva29IZyUg.png)

which corresponds to the shape of the initial dataset. Nice.

We have:

![Image](https://cdn-media-1.freecodecamp.org/images/1*TdmO3dBq-ne84RqY-EtZ2Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mEVlWSSed1Ne_eQ7UiqrZQ.png)

Disappointing! If you look at the paper, this is not the kind of result they show. Actually, this is because we have not rescaled the pixels and there are negative values. To do that, we can put it back in the range [0, 1] with the same technique as above:

```
min: 0.0max: 1.0
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ylvIdrsU1GyVkJwP6cwTdA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Cd3O07GnABlmvfGflJDqg.png)

Hooray! That’s great! It looks like an image from the paper. As mentioned earlier, they used 10000 images and not 1000 like us.

To see the differences in the results according to the number of images that you use and the effect of the hyper-parameter **ϵ**, here are the results for different values:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZN5tPhzho7QCbL4VCXYKGQ.png)

The result of the whitening is different according to the number of images that we are using and the value of the hyper-parameter **ϵ**. The image on the left is the original image. In the paper, [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) used 10000 images and epsilon = 0.1. This corresponds to the bottom left image.

That’s all!

I hope that you found something interesting in this article You can read it on my [blog](https://hadrienj.github.io/posts/Preprocessing-for-deep-learning/), with LaTeX for the math, along with other articles.

You can also fork the Jupyter notebook on Github [here](https://github.com/hadrienj/Preprocessing-for-deep-learning).

#### References

[K. Jarrett, K. Kavukcuoglu, M. Ranzato, and Y. LeCun, “What is the best multi-stage architecture for object recognition?,” in 2009 IEEE 12th International Conference on Computer Vision, 2009, pp. 2146–2153.](https://www.computer.org/csdl/proceedings/iccv/2009/4420/00/05459469.pdf)

[A. Krizhevsky, “Learning Multiple Layers of Features from Tiny Images,” Master’s thesis, University of Tront, 2009.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.222.9220&rep=rep1&type=pdf)

[Y. A. LeCun, L. Bottou, G. B. Orr, and K.-R. Müller, “Efficient BackProp,” in Neural Networks: Tricks of the Trade, Springer, Berlin, Heidelberg, 2012, pp. 9–48.](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

[K. K. Pal and K. S. Sudeep, “Preprocessing for image classification by convolutional neural networks,” in 2016 IEEE International Conference on Recent Trends in Electronics, Information Communication Technology (RTEICT), 2016, pp. 1778–1781.](https://ieeexplore.ieee.org/document/7808140/)

[L. Wan, M. Zeiler, S. Zhang, Y. L. Cun, and R. Fergus, “Regularization of Neural Networks using DropConnect,” in International Conference on Machine Learning, 2013, pp. 1058–1066.](http://proceedings.mlr.press/v28/wan13.html)

**Great resources and QA**

[Wikipedia — Whitening transformation](https://en.wikipedia.org/wiki/Whitening_transformation)

[CS231 — Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/neural-networks-2/)

[Dustin Stansbury — The Clever Machine](https://theclevermachine.wordpress.com/2013/03/30/the-statistical-whitening-transform/)

[Some details about the covariance matrix](http://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/)

[SO — Image whitening in Python](https://stackoverflow.com/questions/41635737/is-this-the-correct-way-of-whitening-an-image-in-python)

[Mean normalization per image or from the entire dataset](http://ufldl.stanford.edu/wiki/index.php/Data_Preprocessing)

[Mean subtraction — all images or per image?](https://stackoverflow.com/questions/29743523/subtract-mean-from-image)

[Why centering is important — See section 4.3](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

[Kaggle kernel on ZCA](https://www.kaggle.com/nicw102168/exploring-zca-and-color-image-whitening/notebook)

[How ZCA is implemented in Keras](https://github.com/keras-team/keras-preprocessing/blob/b9d142456a64ef228475f07cb2f2d38fd05bd249/keras_preprocessing/image.py#L1254:L1257)

