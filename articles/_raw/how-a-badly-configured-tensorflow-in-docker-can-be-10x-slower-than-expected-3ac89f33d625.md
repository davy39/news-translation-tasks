---
title: How a badly configured Tensorflow in Docker can be 10x slower than expected
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T12:44:47.000Z'
originalURL: https://freecodecamp.org/news/how-a-badly-configured-tensorflow-in-docker-can-be-10x-slower-than-expected-3ac89f33d625
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0nVTVSsYDtcaFxMxc4Sr-w.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Pierre Paci

  TL:DR: TensorFlow reads the number of logical CPU cores to configure itself, which
  can be all wrong when you have a container with CPU restriction.

  Let’s do a simple benchmark comparing an inference on GPU, CPU on the host, CPU
  on dock...'
---

By Pierre Paci

TL:DR: TensorFlow reads the number of logical CPU cores to configure itself, which can be all wrong when you have a container with CPU restriction.

Let’s do a simple benchmark comparing an inference on GPU, CPU on the host, CPU on docker, and CPU on docker with restriction.

![Image](https://cdn-media-1.freecodecamp.org/images/y4ZPOO6WxCSkO-6s2atP9DTwTLgBbVle0fFT)
_Our micro benchmark_

Keras/Tensorflow seems to do some operation in GPU upon the first call to .predict(), so will not time the first call, but the second one.

Running that on my Nvidia 1080 will result in an **inference time of ~0.01s** per image.

This time, on my CPU, without a container **it takes ~0.12s**. 12x slower is in the order of magnitude of what to expect between CPU and GPU. Note that my TensorFlow is not properly compiled with AVX or MKL support. GPU was made not visible by using the environment variable **CUDA_VISIBLE_DEVICES**.

Let’s add a container.

![Image](https://cdn-media-1.freecodecamp.org/images/sB5ZQBmwoQiTI3y7YRonETjWAgJjbajplop5)
_Our simple container._

Note: Pillow is an image handling library required by Keras to load an image.

Running this container will result in an **inference time of ~0.15s**. Maybe some overhead from Docker or some TF versions are different from my host, but that’s not the point of this article. The real point will come now.

#### The solution

I’m using a i7 7700k with 8 logical cores, 4 physical. So if we set the container to use only 2 logical core (1 physical), it should be about 4 times slower, so about 0.6s. Restrictions will be made by the [Docker API](https://docs.docker.com/config/containers/resource_constraints/#cpu). **It actually results in 2.5s inference — 4 times slower than expected!**

In fact, TensorFlow uses the number of logical cores to compute some internal performance numbers. An overhead will occur here since the number of reported cores differs from what’s available. On your production server, it could be even bigger. **On our servers, it was 10 times slower since Xeon has more cores.**

So, what can we do ?

The [TensorFlow performance guide](https://www.tensorflow.org/performance/performance_guide#optimizing_for_cpu) has the answer!

![Image](https://cdn-media-1.freecodecamp.org/images/U1JE2b5hFA18vqiEH6GuKsAzapkmhXt2k5eL)

Using these new parameters, we get the following code:

![Image](https://cdn-media-1.freecodecamp.org/images/4K6wPcJD74UHhF5zpitLzPiZa0XGnvPtkl3k)

**And now, it only take ~0.6s**. And that’s exactly what was expected!

So in conclusion, even if Docker seems to simplify the production environment, always be careful! And don’t forget to use the performance guide in the documentation.

