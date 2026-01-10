---
title: How to make an ML Armada and run tens of billions of ML predictions on a budget
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T02:03:50.000Z'
originalURL: https://freecodecamp.org/news/ml-armada-running-tens-of-billions-of-ml-predictions-on-a-budget-f9505c820203
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q0NBrOiL1bfHO5NekJzQLA.jpeg
tags:
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Marcelo Lotif

  In this guide, we will go through a step-by-step process on how to set up AWS’s
  SpotFleet with Docker containers configured to run Tensorflow and Keras applications.

  Docker makes it very easy to install Tensorflow and Keras and to re...'
---

By Marcelo Lotif

In this guide, we will go through a step-by-step process on how to set up [AWS’s SpotFleet](https://aws.amazon.com/blogs/compute/powering-your-amazon-ecs-clusters-with-spot-fleet/) with Docker containers configured to run Tensorflow and Keras applications.

Docker makes it very easy to install Tensorflow and Keras and to reliably reproduce that installation many times over on different machines. At the same time, SpotFleet is a great tool to start up a number of machines while also leveraging the savings you get from [AWS’s spot instances](https://aws.amazon.com/ec2/spot/). Put those together and you have a winning combination of powerful and cheap processing capacity.

The set up described here was designed to be done from scratch and to get you up to speed from zero without fancy configurations — just the bare minimum to get you started without falling into common pitfalls.

So this will be a detailed but simple explanation on how to put all the pieces together. I expect you to know basic AWS configuration and be comfortable with the command line. However, if any of the sections below are already familiar to you, you can skip them using these links:

1. [Building a Tensorflow+Keras-enabled Docker image](#7246)
2. [Pushing your docker image to AWS and creating task definitions](#1ca7)
3. [Requesting a SpotFleet](#e9a7)
4. [Setting up your ECS Cluster to run Docker containers into SpotFleet machines](#0fff)
5. [Real life application and results](#07fc)

The last section explains how this setup is helping us running billions of predictions required for one of our backfills at the company I work for (undisclosed for the time being)— and saving us money compared to other ready-made solutions on the market.

### 1. Building a Tensorflow+Keras-enabled Docker image

We’re going to start by [leveraging the work done by the tensorflow team](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/README.md) using one of the [tensorflow/tensorflow public Docker images](https://hub.docker.com/r/tensorflow/tensorflow/) to build our own image.

First, clone the [Keras/Docker hello world project](https://github.com/lotif/keras-docker-hello-world) I made to get us started:

```
$ git clone https://github.com/lotif/keras-docker-hello-world.git
```

**Note:** I tried to do the bare minimum you will need in order to build a Docker image that trains a sample model. To make the `hello_world.py` file, I used [this tutorial](https://elitedatascience.com/keras-tutorial-deep-learning-in-python) with a few minor modifications to make it work with Keras 2.

I’m not going into detail on how to set that all up, but if you have any questions, don’t hesitate to ask — either here or in the Github repo.

Second, [install Docker on your local machine](https://docs.docker.com/install/) if you haven't already, and build the image locally:

```
$ docker build -t hello-world .
```

Once it finishes, you should see logs like these at the end:

```
[...]Successfully built 3841f29fa5b9Successfully tagged hello-world:latest
```

Now it’s time to test-run it:

```
$ docker run hello-world:latest
```

All the fun is now going to start — the model will be built and it should start training. It will run for a few minutes, and when it’s finished it will produce log messages like these:

```
[...]Epoch 9/1060000/60000 [===============] - 12s - loss: 0.1022 - acc: 0.9679     Epoch 10/1060000/60000 [===============] - 12s - loss: 0.0991 - acc: 0.9695#############################Score: [0.06286391887611244, 0.9799]Training Finished! Exiting...
```

Great! Now we have a working Docker image that trains a model. Time to put that in the cloud :)

### 2. Pushing your docker image to AWS and creating task definitions

You should [install the AWS command line on your local machine](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) and basically follow [this AWS guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#use-ecr) with one important change:

* On the [next steps](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#docker_next_steps) part, I simplified the JSON to be like the code below. Make sure to replace the `<aws-account-`id> with your AWS account id before running it.

Also, do not worry about the “**To run a task with the `hello-world` task definition”** step right now. We’re going to set up ECS later.

There are two main modifications First, there’s the removal of certain configurations that we won’t need right now. Second, we’re going to use `memoryReservation` attribute instead of `memory` . That way your container will not crash if it goes over the memory limit. Third, there is the `command` attribute which was borrowed from the _Dockerfile_. You may modify this as you seem fit regarding your project.

You can check how your task definition is looking like by going to [ECS’s task definitions section](https://console.aws.amazon.com/ecs/home?region=us-east-1#/taskDefinitions) on AWS.

Now we’re ready to set up our fleet!

### 3. Requesting a SpotFleet

I crafted a simplified JSON to get you started, but the UI for Spot Requests is not bad if you prefer to use it. Quick instructions for it are at the end of this section.

I personally prefer the JSON approach, because it’s easily documentable and versionable, as well as faster and more flexible. There are also things you can’t do using the UI, like [instance weighting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-instance-weighting). You can check the [AWS reference docs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html) for full specs on its scheme.

The fleet configurations can be changed as you please. However, there are a few things you need to do in order for it to work properly with ECS clusters:

1. **AMI:** it has to be one of the ECS-optimized AMI id’s in [this list](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html). Choose the one in the zone you’re creating the fleet in.
2. **Key pair:** the name of an AWS key pair you own so you can _ssh_ into the instances if you need to check Docker logs or debug anything. If you don’t have one yet, you can go to [Key Pairs on EC2](https://console.aws.amazon.com/ec2/v2/home#KeyPairs) and click on **Create Key Pair**.
3. **IAM fleet role:** Assign an IAM Role for EC2 service with `AmazonEC2SpotFleetRole` policy. You might have to create a new one for that.
4. **IAM instance profile:** Assign an IAM Role for EC2 service with `AmazonEC2ContainerServiceforEC2Role` policy. You might have to create a new one for that.

Place those values into the placeholders of the file below to get the final spot fleet request in JSON:

With the final file in hand, you can now run the `request-spot-fleet` command below (full specs [here](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-fleet.html)) and it will request the fleet for you:

> **Be careful:** this command will actually request EC2 instances if it finds machines cheaper than the spot bid price, which it likely will given the configurations.

```
$ aws ec2 request-spot-fleet --spot-fleet-request-config file:///path/to/spot-fleet-config.json
```

You’re done! Now you should be able to go to the [EC2 Spot Requests](https://console.aws.amazon.com/ec2sp/v1/spot/home) page and see your fleet there. It is also possible to check the status and shut down the fleet from there as well.

You can add as many instance types as you want in the `LaunchSpecifications` list. Since we have set the allocation strategy to `lowestPrice`, SpotFleet is going to request instances for whatever is the cheapest type depending on current spot prices.

To do this through the UI, [go to the Spot Requests page](https://console.aws.amazon.com/ec2sp/v1/spot/home) and click on the **Request Spot Instances** button. Then click **Request and Maintain**, and you should be able to request a spot fleet. Don’t forget to change the same four items I mentioned above, otherwise it won’t be able to join an ECS cluster.

### 4. Setting up your ECS Cluster to run Docker containers into SpotFleet machines

By creating a fleet with the configurations above, you will also allow it to create a default cluster for you on ECS and assign the fleet instances to it. You can now go to the [ECS Clusters page](https://console.aws.amazon.com/ecs/home?#/clusters), and you should be able to see this default cluster and manage it.

In the default cluster page, there is a tab called **ECS Instances** where you should be able to see the instances of the fleet you just started. They are currently running empty.

Now it’s time to make the machines do the work! For that, an ECS Service needs to be created so it can automatically assign Docker tasks to those machines and start executing.

To do that, use the `create-service` command (full specs [here](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html)):

```
aws ecs create-service --service-name hello-world-service --cluster default --task-definition hello-world-task-def --desired-count 4
```

Now you should be able to go to the **Services** tab of your cluster and see your newly created service there.

You may have noticed that I’ve set the desired count on the command above to 4. You may have also noticed that I’ve set the target capacity of the fleet to 2. If you give it a few minutes, this service will automatically spread those tasks across the instances, starting 2 Docker containers in each one of them. Awesome, isn’t it?

You can customize that behaviour by changing the `--placement-strategy` parameter on the `create-service` command.

The Docker containers are going to start up and execute the command on the task definition. When it’s finished, the task will stop and the service will start another one to do it all over again, always trying to maintain its count of 4 tasks running.

To see the logs and check if the Docker containers are running properly, you should _ssh_ into the machines, do a `docker container ls` , grab your container’s hash number, and do a `docker logs <container-ha`sh>. But this is not scalable for a large number of machines. Consolidating all the logs we need might take another post for itself :)

There are a lot of other configurations you can make on the services, including allocation strategy, health checks, and autoscaling. You should tune those according to your needs.

### 5. Real life application and results

Now I’m going to present our rationale for this solution, and how it’s helping to solve my company’s most pressing problems for adopting Machine Learning on a large scale in our app.

#### Why SpotFleet?

[AWS’s spot instances](https://aws.amazon.com/ec2/spot/) are a wonderful tool. They are boxes that are just sitting idle, and AWS offers them for just a [fraction of the full price](https://aws.amazon.com/ec2/spot/pricing/).

If you’re working with Machine Learning, you’ve probably come to the realization that some things just take too long to run. Training Machine Learning models is a very resource-intensive process for real life datasets composed of anything from hundreds of thousands to millions of training samples.

Another well-known pain point is backfilling. When you have a very large dataset, even trying to run a few predictions for each one of the data points becomes a major undertaking.

To finish all that in a reasonable amount of time (read: while you’re still alive) and without making a huge hole in your company’s finances, you need a lot of cheap processing power. SpotFleet offers a way to spin up many spot instances and Docker containers seamlessly to make them do all you need to do with maximum parallelization for a fraction of the full cost.

#### Real life improvements

After running some benchmarks for our backfill, we decided to go with a machine that is capable of doing a little over 1000 predictions per minute for cost-benefit reasons. It would cost us $1.42 to run a million predictions on that machine if we use regular AWS prices.

Seems ok, but using spot pricing, that same number of predictions would cost us $0.50! Pretty awesome savings.

Another problem is time. We need to perform tens of billions of predictions, and a single one of those machines would take decades to finish everything. Not good.

But with SpotFleet, we can start a large number of those machines at a time, scaling that number up and down easily according to our needs.

In one of our tests, we were able to start a fleet of 650 machines and reached a peak of 35 million predictions per hour at a cost of $19/h. At that rate, we could backfill all of our data in just a few months. Now that seems doable :)

In another test with more powerful but still affordable machines, we were able to reach peaks of 25k predictions per second, or over 2 billion a day!

#### Price comparison with other on-demand image processing solutions

Let’s compare these numbers to a few of the largest pre-built ML solutions for image processing on the market. Our baseline cost with spot instances is **$0.50 per million images**.

[**Google Vision - $600 per million images**](https://cloud.google.com/vision/pricing)**:** There are different tiers depending on the demand. The price goes down by almost a third if you break the 5M images per month barrier, and we definitely will. To simplify the calculations, I’ll consider only the cheapest option, and that would still cost us a whopping $600 to analyze a million images.

[**Amazon Rekognition - $400 per million images**](https://aws.amazon.com/rekognition/pricing/): Their cheapest tier only starts kicking in after 100M images per month. If we consider the lowest price again to simplify the calculation, it would cost us $400 to analyze a million images.

[**Amazon SageMaker - $3.97 per million images**](https://aws.amazon.com/sagemaker/pricing/)**:** This is a more general ML solution like the one on this guide, and it’s easier to draw a comparison here because they offer the same machines we benchmarked our backfill on. The one capable of doing 1000 predictions per minute would cost us $3.97 for a million images. That’s more than double the regular price for this machine, and almost 8x the cost of the spot price.

Let me know in the comments section how this set up works for you. Any suggestions and improvements are welcome, and please comment if you know how to make this better. Have fun!

