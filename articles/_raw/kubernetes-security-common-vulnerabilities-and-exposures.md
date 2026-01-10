---
title: Kubernetes Security – Common Vulnerabilities and Exposures for K8s Programs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-23T19:06:43.000Z'
originalURL: https://freecodecamp.org/news/kubernetes-security-common-vulnerabilities-and-exposures
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/jens-rademacher-kJOj4dU76mE-unsplash-1.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "By Prajwal Kulkarni\nKubernetes has become the go-to tool for orchestration,\
  \ scaling, automated deployment, and management of containerized applications. \n\
  Simply put, Kubernetes is a system that maintains coordination between diverse applications\
  \ acro..."
---

By Prajwal Kulkarni

Kubernetes has become the go-to tool for orchestration, scaling, automated deployment, and management of containerized applications. 

Simply put, Kubernetes is a system that maintains coordination between diverse applications across a group of machines.

It is important to note that this system mostly deals with containerized applications, like Docker images. This is basically a form of virtualization where applications run in isolated user spaces called **containers**.

## Security Issues with Containers

But the user defines the rules of how the application should run and interact with other applications and the external world. And anything that involves human intervention is prone to flaws and mistakes. 

The severity of the error often depends on the skillset of the person managing the containers. Sometimes, even the slightest mistake can break the system. One notable example is the [Log4j vulnerability](https://theconversation.com/what-is-log4j-a-cybersecurity-expert-explains-the-latest-internet-vulnerability-how-bad-it-is-and-whats-at-stake-173896) in Java that caused a major breakdown over the internet in recent times. 

It is often impossible for a software/application to be 100% secure from attackers. But this shouldn't wrongly imply that it is okay to have leaks and vulnerabilities and hope nobody notices them.

You should always look for security vulnerabilities and exposures and apply patches to them as and when available.

Such flaws could leave a cluster or container vulnerable, allowing unauthorized individuals to exploit them. And with Kubernetes' increasing popularity, we need to consider more closely how to assess its efficacy and manage container security issues.

To better safeguard your Kubernetes configurations and programs, let's look at some common vulnerabilities, exposures, and Kubernetes security best practices.

## Configuration Dilemma

![Image](https://www.freecodecamp.org/news/content/images/2022/03/access-control-overview.svg)
_[Source](https://kubernetes.io/docs/concepts/security/controlling-access/)_

If you're new to the Kubernetes world and you're deploying a project by yourself, you may have a tough time figuring out the security configuration rules. This is because, unfortunately, Kubernetes does not provide secure-enough default configuration rules in such instances. 

Although security configuration is not of high importance when you're trying to get hold of the environment, it becomes critical in the later stages when deploying to production. 

A similar issue exists with how pods communicate with each other. These communication rights are defined by network policies, but no such policies are associated with pods by default. Again, this is something that you need to manually configure.

A simple workaround for tackling this is to enable role-based access control (RBAC) to define who has access to the API and what authorizations they hold. 

You can use attributes such as `allowPrivilegeEscalation` and `readOnly` to escalate security in terms of readability and privilege levels.

The following policy shows the authorization levels of the user "bob":

```
{
    "apiVersion": "abac.authorization.kubernetes.io/v1beta1",
    "kind": "Policy",
    "spec": {
    "user": "bob",
    "namespace": "projectCaribou",
    "resource": "pods",
    "readonly": true
    }
}
```

Here, the user "bob" is authorized only to read objects from the namespace "projectCaribou".

If the request were of type "write" or "update", the action would, as expected, fail.

## Malicious Code in Docker Images

Since Kubernetes often deals with containerized applications, usually [Docker images](https://docs.docker.com/engine/reference/commandline/image/), attackers often breakthrough to the cluster or Kube node by gaining access from within the containerized application. 

While there are different solutions to avoid different types of attacks, you could always limit the memory resource usage to prevent DoS attacks. 

You can do this by configuring an ingress controller that is defined to limit the number of requests in a timeframe – for example, 10 requests a second or 1000 requests a minute. 

You can implement this by limiting the requests per client IP or by limiting requests at the service host level. 

Alternatively, an access control list can also be defined to allow only an individual or selected IPs. This mitigation technique ensures that no anonymous request traffic floods the server, and also makes sure that traffic/requests only from credible sources are handled.

Scanning the applications before deploying is also a good rule of thumb to detect malicious code and act on it immediately.

## The Cluster is Secure, the Transmittance is Not

Generally, priority is given only to the cluster's security as that is what handles the applications. But one thing that is often overlooked is the fact that transmittance does not contain any kind of security measure or encryption by default. 

This is a common exposure issue, and ignoring it could open the door for intruders to gain unauthorized access into your system. This means that the [transport security layer](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) (TLS) should handle communication in the cluster between services. 

Improvements in network technology have led to the emergence of products like LinkerD that can enable TLS by default while also providing additional telemetry information on service transactions.

The same principle is also applied to "[etcd](https://www.ibm.com/cloud/learn/etcd)", which stores the state of the cluster. If left unsecured, this becomes an attractive target for attackers as it is possible for the attacker to take over the entire cluster. Even if they have read access only, they could misuse it to elevate privileges.

## Eyes on Runtime

Even if you succeed in overcoming vulnerabilities related to policy and configuration, the runtime presents a new set of obstacles. One example of a runtime security vulnerability is a breached container that runs malicious processes. 

Although crypto mining has become a popular target for malicious actors who break into container settings, attackers can carry out other hostile actions, such as network port scanning for open access to desirable resources, from a compromised container.

You can actively monitor security-critical containers' runtime activity, such as process activity and network communication, to solve these and other runtime issues.

Also, it is also strongly recommended that you incorporate the build and deploy time information to compare observed against expected activity during the runtime. This makes it easier to spot any unusual behavior.

## The Issue with Compliance

Compliance with security standards, regulatory requirements and norms, and an organization's internal regulations can be difficult in cloud-native systems.

The most common reason for failed compliance is neglecting the security aspect during the container adoption process.

The best way to mitigate such vulnerabilities is to adopt security controls early in the container life cycle. Automating necessary checks to the greatest possible extent is also a good practice for reducing your overheads.

## Conclusion

Security is important for containers, and it's something you need to take into account and manage when working with Kubernetes. 

At the end of the day, your ultimate goal should be to make it difficult for intruders to gain access to your systems. And even if they happen to make it in, the infrastructure should be good enough to detect abnormal activity and dispatch actions to prevent it from spreading. 

As Rory McCune, principal security consultant at [NCC Group](https://www.nccgroup.com/us/), says, 

> _"Kubernetes is very complicated, and it's very easy to make a mistake on how you configure it."_ 

Kubernetes and container vulnerabilities, if left unpatched, might lead to severe exposures.  

