---
title: Kubernetes Security – How to Use Dynamic Admission Control to Secure Your Container
  Supply Chain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-05T16:37:56.000Z'
originalURL: https://freecodecamp.org/news/kubernetes-security-dynamic-admission-control
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-39624.jpg
tags:
- name: Application Security
  slug: application-security
- name: container
  slug: container
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: cybersecurity
  slug: cybersecurity
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "By Nahla Davies\nContainers have exploded in popularity in recent years.\
  \ And as more developers are using these containers, they need more tools to manage\
  \ them and their interactions with them effectively. \nTo help manage all this,\
  \ many devs use Kuber..."
---

By Nahla Davies

Containers have exploded in popularity in recent years. And as more developers are using these containers, they need more tools to manage them and their interactions with them effectively. 

To help manage all this, many devs use Kubernetes. And it has [become the de facto standard](https://www.freecodecamp.org/news/the-kubernetes-handbook/) for container orchestration.

While containers help make the software development and deployment lifecycle more efficient, they can also expand the possible ways hackers can attack your organization. 

And while Kubernetes definitely simplifies the process of managing containers, it too has security vulnerabilities. 

Given the popularity of Kubernetes, cybercriminals have put a great deal of effort into exploiting those vulnerabilities. As a result, attacks on the supply chain [have risen significantly](https://www.darkreading.com/cloud/software-container-supply-chain-sees-spike-in-attacks/d/d-id/1341353) over the last year.

And so securing the Kubernetes supply chain is a high priority for many organizations. 

One important security feature that you should pay close attention to if you're a Kubernetes user is dynamic admission control. 

In this article, we'll discuss Kubernetes supply chain vulnerabilities and how to address them with dynamic admission control.

## Vulnerabilities in the Kubernetes Supply Chain

Recently, nearly all Kubernetes users [experienced a security incident](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en.pdf) caused by various vulnerabilities, ranging from misconfiguration to failed audits. Because of this, security concerns have started to take their toll on deployment practices. 

More than half of organizations that use Kubernetes have delayed deploying an application solely based on security issues.

If you want to secure your Kubernetes supply chain, you should have an understanding of the supply chain components for containerized applications and their associated vulnerabilities. 

The supply chain extends well beyond Kubernetes itself and [includes the contents of the containers](https://www.freecodecamp.org/news/a-simple-introduction-to-kubernetes-container-orchestration/) that Kubernetes manages as well as the container host. 

Within the container, you'll typically have a bunch of code from a variety of sources (both internal and external). This gives attackers numerous opportunities to get creative. 

To protect against these threats, you need to properly secure all code sets regardless of their source – and this can be challenging. 

For example, securing code sourced from Linux distributions such as openssl libraries or glibc may only require you to apply the most recent patch. 

But code from other external sources, such as upstream open-source libraries or internal development processes, can be more difficult to secure.

Internal development is perhaps the biggest organizational threat, particularly when developers prioritize speed of release over security.  

Many organizations have decentralized responsibility for container security, with everyone from developers to DevOps getting involved. But more organizations [are building DevSecOps units](https://devops.com/from-agile-to-devops-to-devsecops-the-next-evolution/) and placing Kubernetes security in their hands.

## How to Secure the Kubernetes Supply Chain with Dynamic Admission Control

In Kubernetes, dynamic admission control involves user-defined or configured admission controllers rather than standard built-in controllers.

### What are admission controllers?

Admission controllers take over after the Kubernetes API server receives an authentication and authorization of a request. These pieces of code intercept the request before a container gets initialized and is added as a pod to the Kubernetes cluster. 

Essentially, the admission controller attempts to verify that the image is safe. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-12.png)
_[Image Source](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)_

Admission controllers [implement a variety of functions](https://www.openpolicyagent.org/docs/v0.11.0/kubernetes-admission-control/), from enforcing resource quotas to running cluster-critical tasks. You'll need to have properly configured admission controllers to properly operate many of Kubernetes' advanced features.

### What are admission webhooks?

Dynamic admission controllers rely on admission webhooks, which are user-defined HTTP callbacks that process admission requests. 

In Kubernetes, there are two types of admission webhooks: validating admission webhooks and mutating admission webhooks. 

In the admission control process, mutating admission controls run before validating controls. Both types of webhooks are essentially self-explanatory in principle, although their specific operation requires some explanation. 

#### Validating admission webhooks

Validating admission webhooks intercept and validate requests to the Kubernetes API using an external webhook. Importantly, though, they can not mutate requests. 

All validating webhooks matching a request run in parallel (because no potential modification can occur), and the controller rejects the request on the failure of any matching webhook. 

Validation admission webhooks are all-or-nothing – if the request fails to match precisely, the control rejects it.

#### Mutating admission webhooks

In contrast, mutating admission webhooks are able to modify requests, allowing requests that are only slightly non-compliant with the rule to process. 

If multiple webhooks match a request, they run serially, and each may modify the request. Because mutating controllers run first, mutated requests can still be rejected by validating webhooks.

The joint operation of mutating and validating admission webhooks allows Kubernetes developers to [ensure that requests are compliant](https://www.freecodecamp.org/news/how-to-become-a-certified-kubernetes-application-developer/) and valid before instantiation of containers.

## Kubernetes Pod Security Policies

Pod security policies (or PSPs) are a Kubernetes security feature that relies on the implementation of admission controls. 

PSPs set conditions and defaults that Kubernetes pods must meet in order to be accepted into the container system. 

PSPs can enforce such policies as disabling privileged containers, preventing privilege escalation, and preventing containers from running as root. 

PSPs allow admins to enforce organizational security policies across an entire namespace easily. While PSPs require enabling admission controllers, they must be separately enabled.

Under the Kubernetes Pod Security Standards, there are three types of policies:

* The Baseline Policy has minimal restrictions, although it does not allow privilege escalation. 
* For the lowest trust users, there is the Restricted Policy which disables certain functions in accordance with pod hardening best practices. 
* At the highest level is the Privileged Policy, which is the broadest, allowing the most permissions and privilege escalation. 

Kubernetes started deprecating PSPs with the release of version 1.21. PSPs will be [removed entirely in 2022](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/) with the release of version 1.25. As a result, if you use Kubernetes you should carefully consider alternative security options for all future container applications.

## Don’t Neglect Standard Kubernetes Security Tools

If you use containers, you should be aware of common vulnerabilities throughout your Kubernetes environment. 

To achieve maximum security, both developers and users must apply Kubernetes-specific security features such as dynamic admission control and standard network security features [like VPNs](https://www.freecodecamp.org/news/what-does-a-vpn-do-and-how-does-it-work-a-guide-to-virtual-private-networks/).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-13.png)
_[Image Source](https://securityboulevard.com/2020/03/vpn-a-key-to-securing-an-online-work-environment/)_

A recent Kubernetes vulnerability involved attackers who had access to the API and who could obtain complete administrator access to a Kubernetes cluster and all associated resources. 

A VPN can help avoid this and other similar vulnerabilities where the API server is exposed. But it's important to select the right VPN for your needs.

### How to Choose a VPN

According to cybersecurity expert Ludovic Rembert of Privacy Canada, encryption protocols [are the most important factor](https://privacycanada.net/best-vpn/#:~:text=a%20vpn%20protocol) to look for in a VPN. 

> “A VPN protocol determines how your data gets routed between your machine and the server. Different protocols have different costs and benefits depending on what you need. For example, some prioritize privacy and security, while others prioritize speed….a PE Provider Edge device is a single device, or multiple devices, at the edge of the provider’s network. This device then connects through Consumer Edge devices. In this setup, users can view a website, while the provider device is only aware of the VPN device.” – Rembert

## Conclusion

Containerized applications will continue to become more widely used in coming years, as will container management resources [such as Kubernetes](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/). 

As the popularity of these tools increases, the number of attacks at all points in the supply chain will also increase. 

So if you work with Kubernetes, you need to take advantage of every security resource available to ensure maximum application security and reliability. 

And applying dynamic application controls to verify that the requests are compliant with security policies is one important step in this process.  
  

