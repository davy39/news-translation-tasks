---
title: Security as Standard in the Land of Kubernetes.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T17:39:17.000Z'
originalURL: https://freecodecamp.org/news/security-as-standard-in-the-land-of-kubernetes-50bfad74ca16
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJxP2dKTiFWRnfG5p0tKGA.jpeg
tags:
- name: Docker
  slug: docker
- name: '#infosec'
  slug: infosec
- name: Kubernetes
  slug: kubernetes
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Chris Cooney

  Security in Kubernetes needs some work, but there are some clear steps a team can
  take to make sure their information is safe.

  I have been writing about Kubernetes for a while. I use it every day in my place
  of work. Our mission over ...'
---

By Chris Cooney

Security in Kubernetes needs some work, but there are some clear steps a team can take to make sure their information is safe.

I have been writing about Kubernetes for a while. I use it every day in my place of work. Our mission over the past several months has been to create the fort knox of kubernetes clusters. Should an attacker get through the layers of networking, the firewalls and the WAFs, they will find themselves with very few options. It was spawned from a single piece of advice I got from the gentlemen at [LearnK8s](https://twitter.com/learnk8s).

> Kubernetes will automatically handle high availability, deployments, configuration and secrets for you, but it won’t enforce security on its own. That takes some work.

That’s not to say that Kubernetes is _insecure_, it is simply a different way of approaching software. A way that favours continuous delivery, zero downtime deployments and high availability. Kubernetes will do these things for you, with minimal effort. Security, on the other hand, requires voluntary effort. This has been my job for the past few months and I thought I’d share the lessons I’ve learned. First, the overarching ideal we had in mind.

### Security as Standard

This is simple. It should not be the effort of every single engineer to make sure every layer of their application, deployment and configuration is secure. Think about the amount of rework involved in this.

* The sheer potential for drift, the complexity introduced for support.
* The silo this creates and the disjointed architecture you’re landed with, because everyone has a slightly different method based on their experience.

The aim is to require _minimum developer effort_ and _maximum automatic security_.

### So How Do We Achieve This?

This will form the meat of this article. I have compiled a list of tools and practices that one can use to help foster a technical ecosystem that creates a safe, secure environment for engineers to operate in.

This is by no means an exhaustive list. More of a starter kit. There are some fundamental ideas and some more experimental. The trick is to find what works for you, but keep in mind the two metrics — minimum developer effort, maximum automatic security.

### The Kubernetes NetworkPolicy

I have no doubt that the majority of people reading this article will know all about the `[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)` in Kubernetes. When you’re starting out with security in a Kubernetes cluster, this is the gold. In short, it allows the engineer to lock down which other services can talk to this pod. For example, you can create a `NetworkPolicy` like this:

```
kind: NetworkPolicyapiVersion: networking.k8s.io/v1metadata:  name: api-allowspec:  podSelector:    matchLabels:      app: my-app  ingress:  - from:      - podSelector:          matchLabels:            app: my-other-app
```

We’ve stated something very specific here. We’ve said that that there is only one thing that should be able to talk to our application. That is a pod labelled with `my-other-app`. Should a rogue container be created inside your cluster, any attempts to communicate with `my-app` will be thwarted. However, we can take this further.

Network Policies are not only linked to apps, but they can be hooked into entire namespaces, creating some basic rules that govern all of the applications in there. So one can create a `default-deny` rule. This will essentially blacklist all traffic and another `NetworkPolicy` will need to be made to whitelist communication.

We have a problem though. Not everyone is going to create and use a `NetworkPolicy`. They are inconvenient and tricky at times, people will err to the side of ease and go for an open container. So far, we’ve got high developer effort and high security. This poses a question. How do we make life easier for the engineer, while maintaining a high degree of security? The answer, is _helm_.

### Utilise Helm for Consistency

[Helm](https://helm.sh/) allows you to bundle up lots of Kubernetes resources into a single _chart_. Its most common use case is to make the deployment of 3rd party software trivial — you can peruse the huge collection of [stable helm charts](https://github.com/helm/charts/tree/master/stable) at your leisure. Everyone who’s anyone has got a chart on there and it should be your first port of call when you want to make some open source tooling available in your kubernetes cluster.

Light bulbs should be flicking on right about now. What if we can create our own helm chart and include a `NetworkPolicy` as standard? We can throw all sorts in there — `PodDisruptionBudget` or `HorizontalPodAutoscaler` for example. If you can ensure your engineers are using your helm chart for their deployments, you can also ensure that the correct resources are in place with minimal effort from their part. You’ve just drove down the developer effort and kept the same level of security. Score!

So now your apps are limiting who they can and can’t talk to, but how do you know ensure your application can’t run a bunch of destructive commands to the other applications around it?

### Role Based Access Control (RBAC) for Services

RBAC is a very common feature in Kubernetes cluster. I would strongly advise turning it on. We typically use it for third party applications and developer access, but we can also use it for our software, in the form of `ServiceAccount` resources. We can link these to a specific `Role` or `ClusterRole` and hey presto, no more risk of applications going rogue inside your cluster.

The Kubernetes documentation does a great job of taking you through the mechanics of this. [Read it and be enlightened.](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#service-account-permissions) My one bit of advice would be, once you’ve got your head around the essence of it, bake this into your helm chart. Don’t force engineers to do this because sooner or later, they’re going to avoid it. Or hate you. Or both. Remember, minimum developer effort.

### Validate Your Yaml Before Deploying using Kubescore

So you’ve got a badass helm chart for your applications, but not everything is an application. There are plenty of things, Nexus servers and CI tools, that won’t be deployed through the typical means. Often, it’ll be a cheeky `kubectl` command from an engineer’s machine that opens up the widest vulnerability.

One trick is to use a tool named [kube-score](https://github.com/zegl/kube-score) to provide an easy, consistent and objective measurement of the quality of a service. An element of trust is needed here — you could cook something up to prevent any yaml being applied that fails, but in the first instance, simply making your engineers aware of this tool is enough to get you going.

### Test your Cluster Configuration with kube-bench

There is a brilliant tool called [kube-bench](https://github.com/aquasecurity/kube-bench) that will analyse the configuration of your nodes. This will test out things like, whether you have disabled privileged containers and that your kubelet is communicating with the master nodes in HTTPS.

As with everything, it is unlikely that you’ll pass every metric — this thing is rigorous. Focus on the big ones, anything the tool highlights as critical. This is work you can do behind the scenes, without disrupting engineering, that will benefit you in the long run, should your cluster fall foul of a vulnerability elsewhere.

### Create a Standard Set of Base Docker Images

One gaping hole with all of this is the application containers themselves. Vulnerabilities creep into those all the time and this unknown quantity creates a wonderful little hiding place for difficult to diagnose bugs and vulnerabilities.

However, all is not lost. The good folks at Google have been working on [Distroless](https://github.com/GoogleContainerTools/distroless), a set of docker images that makes docker alpine look like Windows 10. These things are very, very limited and do not give an intruder much wiggle room.

That said, you don’t need to use Distroless images. You can package up your own if you’re confident in your container-fu. The aim here is to limit the scope and scale of custom docker images and bring it to a manageable set of known tooling, and making those available to everyone who needs them.

#### And look out for the latest tag

Ensure all docker images that are deployed into the cluster are _pinned to a version._ The `latest` tag is a dangerous game indeed — you have absolutely no idea what software is running after each pod recycle.

### Istio Mutual TLS

If you’ve been looking into [Istio](https://istio.io/), you’ll know that it very recently announced v1.0.0. That’s it folks, they’re ready for production. Istio offers an absolute plethora of monitoring, tracing and resilience. It also has an awesome feature for enabling mutual TLS between Istio managed applications. If your application has an envoy proxy, you’re in the money.

#### But what is Mutual TLS?

Mutual TLS is a little like HTTPS. It involves one party verifying the existence of the other and, subsequently, establishing an encrypted communications channel. However, HTTPS is predicated on the client verifying the server. In mutual TLS, _two clients will verify each other_.

#### Does it impact the applications?

This is the cool bit. Istio Mutual TLS happens outside of the application, inside the envoy proxy that is coupled with your applications. Your apps can send a request in HTTP and Istio will silently verify the source and encrypt the traffic for you. Developer effort? Absolutely nothing. Security benefits? Strong cryptographic encryption in transit within the cluster and a massive blocker to man in the middle (MITM) attacks. Not bad at all.

### Controversial: Ban the `LoadBalancer and NodePort` Service Types — Stick to ClusterIP

This one tends to split the room a little. We see the `LoadBalancer` service type crop up everywhere in services. It is often the default configuration for many helm charts that are seeking to allow ingress traffic from outside the cluster. There are some serious drawbacks to this:

* Load Balancers cost money, both for transfer costs and running time. Engineers will use whatever is easiest and you can be damn sure, at any reasonable scale, those charges are going to mount. This wouldn’t be so bad, but it’s completely avoidable.
* Each Load Balancer is going to talk to your nodes on a different port. The more ports you’ve got open, the greater the attack surface.
* Who the hell knows what configuration is going on between those load balancers and their target nodes. It is totally at the discretion of whatever controller you’ve installed.

#### So what can we do instead?

Create a single way in. One Load Balancer. For us, we use an [AWS ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), but you can use an [NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) or a classic [ELB](https://aws.amazon.com/elasticloadbalancing/) if the mood takes you. The aim of the game is to create only one route and one set of ports that traffic flows in on. This minimises your attack surface. With all of your applications running as `ClusterIP` instances, no additional port exposure is needed and the routing is done for you by Kubernetes. The only thing left to do is to pick a single ingress controller to run as a `NodePort`, perhaps [NGINX](https://github.com/nginxinc/kubernetes-ingress) or [Traefik](https://github.com/helm/charts/tree/master/stable/traefik), and hey presto! You’ve got simple networking with a tiny attack surface.

### Very Controversial: Take control of the build and deployment process

I’ve included this one as an opinion piece. It is much more controversial than the others that I have discussed. Teams often enjoy owning their own Continuous Delivery (CD) pipelines. This is something they will need to work with on a daily basis. There are classic disagreements amongst engineers about which CI/CD tool to use.

#### And this opens an attack vector, a big one.

Until you know, not think or guess, but know that your engineers are making use of the automation that has been put in place, all of this effort could be cancelled out by a single dodgy config. Your helm chart might wrap services in steel wool and spray it with holy water, but it’s no good if it isn’t being used.

By creating a unified CI/CD process, you can ensure the proper checks are being used. This has some serious benefits. If you wish to introduce a new tool, you build it in one place and everyone gets it immediately. Minimal rework, minimal effort, maximum security benefit. Topped off by consistency across teams.

The option we went for was [Global Shared Libraries](https://jenkins.io/doc/book/pipeline/shared-libraries/) in Jenkins. This allowed us to create a single code base that defined the pipelines which all services use. I have written [another article](https://hackernoon.com/simplifying-jenkinsfiles-c97cfee13f83) about this topic, if you’d like a more in depth look. (Warning, strong language.)

#### But a word of warning…

Think long and hard about this one. You’re taking on a huge maintenance and reliability burden. If that CI/CD tool that you’ve built is flakey, it impacts every developer, immediately. It is a single point of failure and your life will be spent fighting fires. Think hard before shouldering this.

#### Often trust and education is the best solution…

Short of taking over the CI/CD process, the best thing you can do is be involved in the creation of each team’s set of tools. Answer questions, talk about capabilities. Make yourself available to give advice to teams. Give people autonomy and responsibility over their own solution by letting them know what good looks like. This approach doesn’t offer guarantees, but it presents a much more manageable operational overhead.

### Okay, I’m Fresh Out.

I’ve avoided discussing specific networking techniques that we have employed and I’ve ducked around how we can write our apps in a more secure way. The trick here has been to get some quick wins that will seriously narrow the attack surface of any Kubernetes cluster while requiring very little effort from your software engineers.

Have fun on your journey. Kubernetes is a brilliant tool and with a little love and attention, it can form an amazing platform for your engineering squads.

I’m fully on the Kubernetes train and I shout about it on my [twitter](https://twitter.com/chris_cooney) all the time.

