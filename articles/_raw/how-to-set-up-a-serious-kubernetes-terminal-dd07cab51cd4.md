---
title: How to set up a serious Kubernetes terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-22T22:59:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-serious-kubernetes-terminal-dd07cab51cd4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tTUoVKGzxtZYA5xp.png
tags:
- name: Devops
  slug: devops
- name: Kubernetes
  slug: kubernetes
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'By Chris Cooney

  All the CLI tools a growing k8s nerd needs


  Kubernetes comes pre-packaged with an outstanding CLI. For basic operations, it
  works wonderfully. Alas, when one needs to do something quickly, complexity increases.

  The Kubernetes communit...'
---

By Chris Cooney

#### All the CLI tools a growing k8s nerd needs

![Image](https://cdn-media-1.freecodecamp.org/images/so-R6v0yNEdAxS8GfQ9pG316RLC43SSX3m8K)

Kubernetes comes pre-packaged with an outstanding CLI. For basic operations, it works wonderfully. Alas, when one needs to do something quickly, complexity increases.

The Kubernetes community has built all sorts of web based tooling for monitoring your cluster — [kube ops view](https://github.com/hjacobs/kube-ops-view), [grafana](https://medium.com/htc-research-engineering-blog/monitoring-kubernetes-clusters-with-grafana-e2a413febefd) etc. However, having a fully kitted terminal will rapidly speed up the time it takes to get to the root of an issue. It forms a fundamental part of your Swiss army knife.

The following is a very short list of open source tools that I’ve applied to my OSX terminal. When used together, they allow me to skip around my kubernetes cluster, quickly troubleshoot issues, and monitor behaviour. I’ve cut out lots of small little utilities and stuck to the tools that I find myself using every day.

#### Before any tools…

Before you go after these tools, I’d strongly recommend installing [zsh](https://ohmyz.sh/). It is an outstanding, open source wrapper around the standard OSX terminal. It is more feature rich and intuitive and the plugins you can install are fantastic. Some of these tools listed make the assumption you have ZSH installed.

#### [k9s](https://github.com/derailed/k9s)

![Image](https://cdn-media-1.freecodecamp.org/images/x6Tesdbm6GNXgOtJFplS3VyHt8FjKe0ayWSX)
_oh yes_

I’m starting strong. K9s is the momma bear of CLI tools for kubernetes cluster. You can SSH straight into pods with a single key press, view logs, delete resources and more. It provides outstanding access for the most common operations you’ll be performing. This is a staple for any engineer using kubernetes.

#### [kubectx](https://github.com/ahmetb/kubectx)

But one thing that K9s doesn’t support is switching between various contexts in your kubernetes config. It is very rare that we’ll only have one single cluster. Switching between these is as simple as

```
kubectl config use-context my-context
```

But with this, there are some prerequisites:

* You need to know the name of the cluster before you run.
* There is another, similar `set-context` command that could trip you up.

`kubectx` presents a simpler alternative to this. If you run `kubectx` on its own, it will list out all of the contexts in your `.kube/config` file. You can then provide the name of the context you’re interested in:

```bash
kubectx my-context
```

No need to remember all the contexts, no need to manually check files and no possibility of getting the wrong command. Nice and simple. Combined with `k9s`, this offers a lot of navigability from your CLI with minimal key presses.

#### [kubens](https://github.com/ahmetb/kubectx)

Once you’re flitting around contexts, you may want to dig into a specific namespace. Once again, it’s very common to have more than a few namespaces in your cluster. Well, [ahmetb](https://twitter.com/ahmetb) (the gentleman who brought you `kubectx`) also put together `kubens`. It’s the same as `kubectx`, only for namespaces.

```bash
kubens kube-system
```

Now all of your commands run against the `kube-system` namespace, by default. You can also run `kubens` without anything else to see a list of your namespaces.

#### [kube-ps1](https://github.com/jonmosco/kube-ps1)

So, you can switch between contexts and namespaces. But how do you know which one you’re currently aimed at? It’s a pain to keep checking. At the moment, to find out you’d need to run:

```bash
kubens
kubectx
kubectl <my-command>
```

To remove this, `ps1` is a zsh plugin that will automatically show you your current context and namespace:

![Image](https://cdn-media-1.freecodecamp.org/images/prQC-ZDrz2hCz5ggKEIgyL9CIiMWu-KDP2Hy)
_I’m pointing at my minikube context and the default namespace_

Now you can see which namespace and context you’re pointing out without running a single command. It’s also highly configurable too — you can turn off namespace or context, if you’re only interested in one of them, or you can use `kubeoff` to disable the whole thing entirely.

#### [popeye](https://github.com/derailed/popeye)

Now, onto something a little different. `popeye` will run automatic scans of the resources in your repository and highlight clear, obvious problems. This is a very new tool and one that I have found very useful. If you’re looking for some spring cleaning to do in your cluster, starting with `popeye` will give you some clear indications of what needs to be fixed.

![Image](https://cdn-media-1.freecodecamp.org/images/RrLhd7S2q9Lrkq7i15C8FgLVgIzwgFuUh6CU)
_This was the first few lines of a very long, detailed report._

#### [Stern](https://github.com/wercker/stern)

Ever used `kubectl logs`? Noticed you can only follow logs from one pod at one time? Well, worry no more! Stern is a tool that allows you to pull the logs from multiple pods, based on a very flexible query.

I’m talking regularly about kubernetes, DevOps and much more on my [twitter account](https://twitter.com/chris_cooney).

