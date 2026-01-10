---
title: Machine Learning as a Service with TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T03:25:09.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-as-a-service-with-tensorflow-9929e9ce3801
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bhqON7cBLFo-TIrOyoDc1g.jpeg
tags:
- name: Docker
  slug: docker
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Kirill Dubovikov

  Imagine this: you’ve gotten aboard the AI Hype Train and decided to develop an app
  which will analyze the effectiveness of different chopstick types. To monetize this
  mind-blowing AI application and impress VC’s, we’ll need to ope...'
---

By Kirill Dubovikov

Imagine this: you’ve gotten aboard the AI Hype Train and decided to develop an app which will analyze the effectiveness of different chopstick types. To monetize this mind-blowing AI application and impress VC’s, we’ll need to open it to the world. And it’d better be scalable as everyone will want to use it.

As a starting point, we will use this dataset, which contains measurements of food pinching efficiency of various individuals with chopsticks of different length.

#### Architecture

As we are not only data scientists but also responsible software engineers, we’ll first draft out our architecture. First, we’ll need to decide on how we will access our deployed model to make predictions. For TensorFlow, a naive choice would be to use [TensorFlow Serving](https://www.tensorflow.org/serving/). This framework allows you to deploy trained TensorFlow models, supports model versioning, and uses g[RPC](https://grpc.io) under the hood.

The main caveat about gRPC is that it’s not very public-friendly compared to, for example, REST services. Anyone with minimal tooling can call a REST service and quickly get a result back. But when you are using gRPC, you must first generate client code from proto files using special utilities and then write the client in your favorite programming language.

TensorFlow Serving simplifies a lot of things in this pipeline, but still, it’s not the easiest framework for consuming API on the client side. Consider TF Serving if you need lightning-fast, reliable, strictly typed API that will be used inside your application (for example as a backend service for a web or mobile app).

We will also need to satisfy non-functional requirements for our system. If lots of users might want to know their chopstick effectiveness level, we’ll need the system to be fault tolerant and scalable. Also, the UI team will need to deploy their chopstick’o’meter web app somewhere too. And we’ll need resources to prototype new machine learning models, possibly in a Jupyter Lab with lots of computing power behind it. One of the best answers to those questions is to use [Kubernetes](https://kubernetes.io).

> [Kubernetes](https://kubernetes.io/) is an open-source system for automating deployment, scaling, and management of containerized applications.

With Kubernetes in place, given knowledge and some time, we can create a scalable in-house cloud PaaS solution that gives infrastructure and software for full-cycle data science project development. If you are unfamiliar with Kubernetes, I suggest you watch this:

Kubernetes runs on top of [Docker](http://docker.com) technology, so if you are unfamiliar with it, it may be good to read the [official tutorial](https://docs.docker.com/get-started/) first.

All in all, this is a very rich topic that deserves several books to cover completely, so here we will focus on a single part: moving machine learning models to production.

#### Considerations

Yes, this dataset is small. And yes, applying deep learning might not be the best idea here. Just keep in mind that we are here to learn, and this dataset is certainly fun. The modeling part of this tutorial will be lacking in quality, as the main focus is on the model deployment process.

Also, we need to impress our VC’s, so deep learning is a must! :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gejeBAG1aRDFWOL8Uxz3dg.png)
_Image [source](https://xkcd.com/1838/" rel="noopener" target="_blank" title=")._

#### Code

All code and configuration files used in this post are available in a [companion GitHub repositor](https://github.com/kdubovikov/chopstick-serving)y.

#### Training Deep Chopstick classifier

First, we must choose a machine learning framework to use. As this article is intended to demonstrate TensorFlow serving capabilities, we’ll choose TensorFlow.

As you may know, there are two ways we can train our classifier: using TensorFlow and using TensorFlow [Estimator API](https://www.tensorflow.org/versions/master/programmers_guide/estimators). Estimator API is an attempt to present a unified interface for deep learning models in a way scikit-learn does it for a set of classical ML models. For this task, we can use `tf.estimator.LinearClassifier` to quickly implement Logistic Regression and export the model after training has completed.

The other way we can do it is to use plain TensorFlow to train and export a classifier:

#### Setting up TensorFlow Serving

![Image](https://cdn-media-1.freecodecamp.org/images/1*nTik7YnlL8avMLiRm2iQBQ.jpeg)
_Serving, huh?_

So, you have an awesome deep learning model with TensorFlow and are eager to put it into production? Now it’s time to get our hands on TensorFlow Serving.

TensorFlow Serving is based on gRPC — a fast remote procedure call library which uses another Google project under the hood — Protocol Buffers.

Protocol Buffers is a serialization framework that allows you to transform objects from memory to an efficient binary format suitable for transmission over the network.

To recap, gRPC is a framework that enables remote function calls over the network. It uses Protocol Buffers to serialize and deserialize data.

The main components of TensorFlow Serving are:

* **Servable** — this is basically a version of your trained model exported in a format suitable for TF Serving to load
* **Loader** — TF Serving component that, by coincidence, loads servables into memory
* **Manager** — implements servable’s lifecycle operations. It controls servable’s birth (loading), long living (serving), and death (unloading)
* **Core** — makes all components work together (the official documentation is a little vague on what the core actually is, but you can always [look at the source code](https://github.com/tensorflow/serving/blob/f34e79a1ef0315d0f2d86eb0751a4c3700f8a433/tensorflow_serving/model_servers/server_core.h) to get a hang of what it does)

You can read a more in-depth overview of TF Serving architecture at the [official documentation](https://www.tensorflow.org/serving/architecture_overview).

To get a TF Serving-based service up and running, you will need to:

1. Export the model to a format compatible with TensorFlow Serving. In other words, create a Servable.
2. Install or compile TensorFlow Serving
3. Run TensorFlow Serving and load the latest version of the exported model (servable)

[Setting up TernsorFlow Serving](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/setup.md) can be done in several ways:

* Building from source. This requires you to install Bazel and complete a lengthy compilation process
* Using a pre-built binary package. TF Serving is available as a deb package.

To automate this process and simplify subsequent installation to Kubernetes, we created a simple Dockerfile for you. [Please clone the article’s repository and follow the instructions in the README.md](https://github.com/kdubovikov/chopstick-serving) file to build TensorFlow Serving Docker image:

```
➜ make build_image
```

This image has TensorFlow Serving and all dependencies preinstalled. By default, it loads models from the `/models` directory inside the docker container.

#### Running a prediction service

To run our service inside the freshly built and ready to use TF Serving image, be sure to first train and export the model (or if you’re using a companion repository, just run the `make train_classifier` command).

After the classifier is trained and exported, you can run the serving container by using the shortcut `make run_server` or by using the following command:

```
➜ docker run -p8500:8500 -d --rm -v /path/to/exported/model:/models tfserve_bin
```

* `-p` maps ports from the container to the local machine
* `-d` runs the container in daemon (background) mode
* `--rm` removes the container after it has stopped
* `-v` maps the local directory to a directory inside the running container. This way we pass our exported models to the TF Serving instance running inside the container

#### Calling model services from the client side

To call our services, we will use `grpc` `tensorflow-serving-api` Python packages. Please notice that this package is currently only available for Python 2, so you should have a separate virtual environment for the TF Serving client.

To use this API with Python 3, you’ll either need to use an unofficial package from [here](https://github.com/illagrenan/tensorflow-serving-api-python3) then download and unzip the package manually, or build TensorFlow Serving from the source (see the [documentation](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/setup.md#tensorflow-serving-python-api-pip-package)). Example clients for both Estimator API and plain TensorFlow are below:

#### Going into production with Kubernetes

If you have no Kubernetes cluster available, you may create one for local experiments using [minikube](https://github.com/kubernetes/minikube), or you can easily deploy a real cluster using [kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/).

We’ll go with the minikube option in this post. Once you have installed it (`brew cask install minikube` on Mac) we may start a local cluster and share its Docker environment with our machine:

```
➜ minikube start...➜ eval $(minikube docker-env)
```

After that, we’ll be able to build our image and put it inside the cluster using

```
➜ make build_image
```

A more mature option would be to use the internal docker registry and push the locally built image there, but we’ll leave this out of scope to be more concise.

After having our image built and available to the Minikube instance, we need to deploy our model server. To leverage Kubernetes’ load balancing and high-availability features, we will create a Deployment that will auto-scale our model server to three instances and will also keep them monitored and running. You can read more about Kubernetes deployments [here](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

All Kubernetes objects can be configured in various text formats and then passed to `kubectl apply -f file_name` command to (meh) apply our configuration to the cluster. Here is our chopstick server deployment config:

Let’s apply this deployment using the `kubectl apply -f chopstick_deployment.yml` command. After a while, you’ll see all components running:

```
➜ kubectl get allNAME                          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGEdeploy/chopstick-classifier   3         3         3            3           1d
```

```
NAME                                 DESIRED   CURRENT   READY     AGErs/chopstick-classifier-745cbdf8cd   3         3         3         1d
```

```
NAME                          AGEdeploy/chopstick-classifier   1d
```

```
NAME                                 AGErs/chopstick-classifier-745cbdf8cd   1d
```

```
NAME                                       READY     STATUS    RESTARTS   AGEpo/chopstick-classifier-745cbdf8cd-5gx2g   1/1       Running   0          1dpo/chopstick-classifier-745cbdf8cd-dxq7g   1/1       Running   0          1dpo/chopstick-classifier-745cbdf8cd-pktzr   1/1       Running   0          1d
```

Notice that based on the Deployment config, Kubernetes created for us:

* Deployment
* [Replica Set](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
* Three pods running our chopstick-classifier image

Now we want to call our new shiny service. To make this happen, first we need to expose it to the outside world. In Kubernetes, this can be done by defining [Services](https://kubernetes.io/docs/concepts/services-networking/service/). Here is the Service definition for our model:

As always, we can install it using `kubectl apply -f chopstick_service.yml`. Kubernetes will assign an external port to our LoadBalancer, and we can see it by running

```
➜ kubectl get svcNAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGEchopstick-classifier   LoadBalancer   10.104.213.253   <pending>     8500:32372/TCP   1dkubernetes             ClusterIP      10.96.0.1        <none>        443/TCP          1d
```

As you can see, our `chopstick-classifier` is available via port `32372` in my case. It may be different in your machine, so don’t forget to check it out. A convenient way to get the IP and port for any Service when using Minikube is running the following command:

```
➜ minikube service chopstick-classifier --urlhttp://192.168.99.100:32372
```

#### Inference

Finally, we are able to call our service!

```
python tf_api/client.py 192.168.99.100:32372 1010.0Sending requestoutputs {  key: "classes_prob"  value {    dtype: DT_FLOAT    tensor_shape {      dim {        size: 1      }      dim {        size: 3      }    }    float_val: 3.98174306027e-11    float_val: 1.0    float_val: 1.83699980923e-18  }}
```

#### Before going to real production

![Image](https://cdn-media-1.freecodecamp.org/images/1*qYsGyocCbVbbrbWY15CULA.jpeg)

As this post is meant mainly for educational purposes and has some simplifications for the sake of clarity, there are several important points to consider before going to production:

* Use a service mesh like [linkerd.io](https://linkerd.io). Accessing services from randomly generated node ports is not recommended in production. As a plus, linkerd will add much more value to your production infrastructure: monitoring, service discovery, high speed load balancing, and more
* Use Python 3 everywhere, as there is really no reason to use Python 2 now
* Apply Deep Learning wisely. Even though it is a very general, spectacular, and widely applicable framework, deep learning is not the only tool at the disposal of a data scientist. It’s also not a silver bullet that solves any problem. Machine learning has much more to offer. If you have relational/table data, small datasets, strict restrictions on computation resources, or training time or model interpretability, consider using other algorithms and approaches.
* Reach out to us if you need any help in solving machine learning challenges: datalab@cinimex.ru

