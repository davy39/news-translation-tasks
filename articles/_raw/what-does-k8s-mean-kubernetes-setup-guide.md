---
title: What Does K8s Mean? How to Set Up Kubernetes and Manage Clusters
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T19:46:37.000Z'
originalURL: https://freecodecamp.org/news/what-does-k8s-mean-kubernetes-setup-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/what-does-k8s-mean.png
tags:
- name: containers
  slug: containers
- name: Docker Containers
  slug: docker-containers
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "By Sebastian Sigl\nYou might've seen the term k8s in different sources,\
  \ and wondered what it means. Well, it means Kubernetes. The abbreviation consists\
  \ of:    \n\n\"k\" which is the first letter of Kubernetes,\n\"8\" which is the\
  \ number of letters between t..."
---

By Sebastian Sigl

You might've seen the term k8s in different sources, and wondered what it means. Well, it means Kubernetes. The abbreviation consists of:	

* "**k**" which is the first letter of Kubernetes,
* "**8**" which is the number of letters between the first and the last in the word, and
* "**s**" which is the last letter.

Now, let’s look into what Kubernetes is used for to understand its core strength and fields of usage.

Containers are everywhere. Using container technologies like [Docker](https://www.docker.com/), you can start applications in a completely isolated environment in a single command. Kubernetes is used for container orchestration, combining multiple machines into a cluster and distributing stateful containers.

In this blog post, you'll learn:

* How to play with Kubernetes on your local device,
* How to launch applications in a Kubernetes cluster,
* The most popular managed Kubernetes providers to run your applications at scale.

This tutorial will mainly focus on using the shell rather than the UI because it allows you to use all examples in a local and remote Kubernetes cluster.

## How to Set Up Kubernetes on your Local Device

The easiest way to get started is to [install Docker.](https://www.docker.com/get-started/) After starting, you can open Docker, go to `Settings -> Kubernetes`, and enable Kubernetes locally. After confirming, your Kubernetes cluster will start up.

The easiest way to communicate with a Kubernetes cluster is by using [kubectl](https://github.com/kubernetes/kubectl). So if you haven't done it already, [install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl). 

Additionally, I recommend that you [setup kubectx](https://github.com/ahmetb/kubectx), which allows you to switch between different clusters. To make Kubernetes deployments easy, you should also [install Helm](https://helm.sh/docs/intro/install/), which enables you to deploy more complex applications, which consist of multiple parts, with a single command.

Now, Docker shows that the Kubernetes cluster is ready in your settings, then you can start some applications. Let’s look at all available Kubernetes contexts:

```sh
# Show all available contexts
kubectx

> development
> docker-desktop

# Select local docker desktop context
kubectx docker-desktop
```

## How to Launch Applications in a Kubernetes Cluster

Let’s set up a [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) that allows a team to use Jupyter Notebooks, one of the most popular platforms for machine learning and Python.

```sh
# add helm repository
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/

# start containers
helm install my-jupyterhub jupyterhub/jupyterhub --version 1.2.0

# after a few minutes, get information about the Kubernetes service
kubectl --namespace=default get svc proxy-public

NAME           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
proxy-public   LoadBalancer   10.109.132.29   localhost     80:31480/TCP   31m
```

As printed, the external IP is localhost and exposed on port 80. Once the containers are started, you can open [http://localhost](http://localhost) and log in with the username “admin” and no password.

As you can see, it’s effortless to run a more comprehensive application with a few command lines. If you want to try more examples, check out [my blog post about Helm](https://www.freecodecamp.org/news/helm-charts-tutorial-the-kubernetes-package-manager-explained/).

To clean up resources, you should remove the running application:

```sh
helm uninstall my-jupyterhub

release "my-jupyterhub" uninstalled
```

## Most Popular Managed Kubernetes Clusters

Once you want to run an application and make it available to others, you must run a publicly available Kubernetes cluster. You should not run your cluster from scratch if you are not an expert.

Instead, you can use a managed version of a Kubernetes cluster, which means most of the maintenance of the cluster itself is done by an external provider. You can simply deploy containers, and things should just work. 

My recommendation is to use the [Google Kubernetes Cluster](https://cloud.google.com/kubernetes-engine/) (GKE), the managed cluster from Google. Google is the original designer of Kubernetes and is known to provide a solid Kubernetes experience. They also offer a more extreme managed version of it called GKE Autopilot, which allows you to pay by container hour and memory. 

Still, in reality, teams use the standard Kubernetes cluster that comes with more integrations of other managed services, which are not available yet if you use Autopilot. For example, you can create Service Accounts, DNS Records, or Managed Certificates using Kubernetes resources by using [Config Connector](https://cloud.google.com/config-connector/docs/overview).

You can follow a [simple Google tutorial to set up a GCP Kubernetes cluster and deploy an example application](https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) in a few minutes.

There are many more managed Kubernetes clusters like [Elastic Kubernetes Service](https://aws.amazon.com/de/eks/) (EKS) from Amazon and [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/) (AKS) from Microsoft. Whatever cloud you prefer, it’s usually a good idea to use the managed Kubernetes cluster from your current cloud vendor.

I [compared the interest of Kubernetes for three popular vendors by using Google Trends](https://trends.google.com/trends/explore?date=today%205-y&q=Google%20Kubernetes,AWS%20Kubernetes,Azure%20Kubernetes), which shows that Azure and AWS (Amazon) are the most popular. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-05-at-11.01.31.png)

These numbers do not show which vendor provides the best experience. But, they show a significant interest in Kubernetes run on Azure. Interestingly, Azure took the lead within the last months.

## Summary

In this blog post, you learned what k8s means – it's just an abbreviation for Kubernetes. It's a popular container orchestration system for automating applications' deployment, scaling, and management. You can run Kubernetes locally and on scale in different clouds.

I hope you enjoyed the article.

If you liked it and felt the need to give me a round of applause or just want to get in touch, [follow me on Twitter](https://twitter.com/sesigl).

I work at eBay Kleinanzeigen, one of the world’s biggest classified companies. By the way, [we are hiring](https://www.ebay-kleinanzeigen.de/careers)!

## References

* [JupyterHub Helm Chart](https://artifacthub.io/packages/helm/jupyterhub/jupyterhub?modal=values)
* [Top Managed Kubernetes Service](https://techgenix.com/top-managed-kubernetes-services/)
* [Azure vs Google vs Amazon Kubernetes](https://www.linkedin.com/pulse/aks-vs-eks-gke-managed-kubernetes-services-compared-yarden-fayer/?trk=public_profile_article_view)

  

