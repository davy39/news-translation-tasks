---
title: How to simplify the deployment of containerized apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T05:11:19.000Z'
originalURL: https://freecodecamp.org/news/how-can-we-simplify-deployment-of-containarized-apps-a2effd01a662
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QzKmrPtCm5SvCklDccppkQ.png
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: 'By Omer Levi Hevroni

  I asked myself this question when I started to learn Kubernetes: how can we simplify
  the deployment of containerized apps? At first look, deploying containerized apps
  seems pretty simple. All you need is a bunch of YAML files, an...'
---

By Omer Levi Hevroni

I asked myself this question when I started to learn [Kubernetes](https://kubernetes.io/): how can we simplify the deployment of containerized apps? At first look, deploying containerized apps seems pretty simple. All you need is a bunch of YAML files, and by using `[kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/)` (the Kubernetes command line utility), you’ll have your service up and running in your Kubernetes cluster.

But, Although deploying one app is an easy task, how do you deploy hundreds of apps? At [Soluto](https://www.solutotlv.com), we have more than 100 live microservices and this number keeps growing. So as we started thinking about shifting workload to our Kubernetes cluster, we faced a few challenges:

First, Kubernetes deployment is actually more complex. There are many moving parts that you need to set up correctly: pod autoscaler, pod resources, ingress, and so on. Those parts require some experience with how Kubernetes works, and not setting it up correctly might cause issues in production. Ideally we’d have a way to simplify this, so developers can focus on writing their code and worry less about deployment.

Second, security is also a challenge. All services in production should have certain things, like Transport Layer Security (TLS). These are not necessarily complex things, but need to be taken care of nonetheless. We would like to pre-configure them so that any new deployment will be secured by default.

### Finding a solution

To solve these challenges and speed up and ease the adoption process, we looked for a way to create a template for Kubernetes. Something that any developer would be able to use, and would require just a few parameters (for example, the Docker image of the service) to get the service up and running in production.

On the other hand, we needed to be careful not to hide too much — developers must be able to understand what’s going on so they can handle production issues. We had to find the right level of abstraction that makes it easier to deploy to Kubernetes, without hiding too much detail.

With that in mind, we started to look for a solution. After trying a few things, we found [Helm](https://helm.sh/). Helm is a package manager for Kubernetes.You can use it to install any app on your cluster, and Helm will take care of getting all the required configuration files and installing them on your cluster. Helm also support updating deployments, rollbacks, and many other cool features. Each Helm package is called a “Chart”, and the charts are stored in a repository. With helm, installing [Mongo](https://github.com/kubernetes/charts/tree/master/stable/mongodb), for instance, is as easy as `helm install stable/mongodb`.

Sound like an excellent solution! We can define a chart for each type of service — like one for all our web APIs, which will handle things like load balancer and TLS — and the developer simply needs to specify the required parameters using Helm’s configuration files.

![Image](https://cdn-media-1.freecodecamp.org/images/4P0D8IGfVHiObVNHgAdPTrrhcNFOZh2irhoj)
_Me and my teammate, when we found Helm_

### Helm: Let’s see how it’s done

In order to use Helm, we first need to [install](https://docs.helm.sh/using_helm/#installing-helm) it. Helm has two components: Helm client running on your computer, and Tiller, a server-side component running on your cluster. Then, we need to create the chart by using this simple Helm CLI command: `helm create web-api`

After running this command, you’ll notice the creation of a new folder named “web-api”. Within this folder, you’ll find all the familiar Kubernetes configuration files: deployment, service, ingress, and so on. Now it’s time to customize a bit: we can add a [horizontal pod autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/), define the default resources the pod requires, and of course, enable TLS by default.

Everything is highly customizable based on the [Go templating mechanism](https://docs.helm.sh/chart_template_guide/). So anything we add can be overridden later by the developer, in case the default configuration doesn’t work as needed.

So now we have a chart — but how can we consume it? The chart has to exist in a [Helm repository](https://github.com/kubernetes/helm/blob/master/docs/chart_repository.md), which is basically a server with a few Zip archives (which are all the charts in the repository) and one index file that is consumed by the CLI. You can manually set up your repo using any storage service like Azure Blob or AWS S3, but the simplest option is [Chart Museum](https://github.com/kubernetes-helm/chartmuseum).

Chart museum is a Helm repository with a CRUD API to manage your charts. It supports basic authentication so you can restrict who can push new charts to your Helm repository. Helm doesn’t supply any museum-as-a-service solution, so you’re gonna have to roll your own. But it’s dead simple — [simply use its docker image.](https://hub.docker.com/r/chartmuseum/chartmuseum/)

Now we can build a CI/CD pipeline for our web-api chart, to ease the process of modifying it:

* Run some kind of tests, to make sure that the new version is not broken. I’ll discuss how in the next paragraph.
* Pack the new chart, using Helm CLI.
* Push the new package to our Chart Museum instance, using Chart Museum’s API.

### Testing it out

Now our chart is ready to be used by developers! But wait… how can we know that the chart actually works? And how can we make sure it will continue to work? This is why we need to write tests for our chart (like we write for anything else).

![Image](https://cdn-media-1.freecodecamp.org/images/WGGYmgftYuRQOqzlognwNV8yF4IFx6etjAF2)

There are basically two things we want to test.

1. We want to test our template — for example, if an ingress is supposed to exist with a TLS and specific rules (defined by the developer), we should test the generated template and make sure the ingress was created correctly.
2. We want to test that the files are valid Kubernetes configurations and that they work as expected.

Testing the first thing is relatively simple — check out this [sample repo](https://github.com/omerlh/helm-chart-tests-demo) to see just how simple it is.

This allows us to test the generated Kubernetes files, by using `[kubetest](https://github.com/garethr/kubetest)`. This is great, but can be complex and messy, especially when having a lot of branching in your template files.

A better solution is required — one that will allow us to do unit testing for the templates, without generating Kubernetes files. This wasn’t a problem until recently when we started to have a lot of branching in our templates, and we’re now looking for options.

The second thing — testing that Kubernetes files are valid — is a bit more tricky. For now, at Soluto we’re using Helm’s version mechanism: each chart has a version, and all of our services will use the latest stable version. When a new chart version is pushed, we can test this version on a specific service. If it works correctly, update the rest of the services. Another option is to test that using `minikube`, but it was too complex for our needs.

### Finally: Deploying!

So now we have a CI/CD pipeline for our Helm charts, and we have prepared a Helm chart that the developers can use. Now, when a new developer wants to deploy a new service to production, all they have to do is:

1. Add our repository to their local Helm using `helm repo add chartmuseum http://<chart-museum-u`rl>  
2. Create a new Helm config file and specify the required parameters (for example, docker image of the service)  
3`. Run helm upgrade —install <service-name> chartmusuem/web-api -f<path_`to_config_file> and that’s it. The service is alive.

And to make it even easier to understand, I’ve created a sample [repository](https://github.com/Soluto/kubernetes-deployment-demo). The repository contains all the things that I’ve discussed in this blog post: a generic chart for a web app that can be deployed with this chart and chart museum. Check it out to better understand what’s going on — and there is even a walkthrough to help you get started.

Thank you for reading along. If you have any questions, or you need help getting started with Helm, feel free to reach out either via the comments here or via [Twitter](https://twitter.com/intent/tweet?text=.%20%40omerlh%2C%20I%20have%20a%20question%20about%20%40Helm&via=SolutoEng).

Happy Helming!

Originally posted on [Soluto’s Blog](https://blog.solutotlv.com/?utm_source=medium)

