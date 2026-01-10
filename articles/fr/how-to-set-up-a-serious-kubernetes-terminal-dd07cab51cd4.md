---
title: Comment installer un terminal Kubernetes sérieux
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
seo_title: Comment installer un terminal Kubernetes sérieux
seo_desc: 'By Chris Cooney

  All the CLI tools a growing k8s nerd needs


  Kubernetes comes pre-packaged with an outstanding CLI. For basic operations, it
  works wonderfully. Alas, when one needs to do something quickly, complexity increases.

  The Kubernetes communit...'
---

Par Chris Cooney

#### Tous les outils CLI dont un passionné de k8s en croissance a besoin

![Image](https://cdn-media-1.freecodecamp.org/images/so-R6v0yNEdAxS8GfQ9pG316RLC43SSX3m8K)

Kubernetes est livré avec un CLI exceptionnel. Pour les opérations de base, il fonctionne merveilleusement. Malheureusement, lorsque l'on doit faire quelque chose rapidement, la complexité augmente.

La communauté Kubernetes a développé toutes sortes d'outils basés sur le web pour surveiller votre cluster — [kube ops view](https://github.com/hjacobs/kube-ops-view), [grafana](https://medium.com/htc-research-engineering-blog/monitoring-kubernetes-clusters-with-grafana-e2a413febefd), etc. Cependant, avoir un terminal entièrement équipé accélérera rapidement le temps nécessaire pour atteindre la racine d'un problème. Il constitue une partie fondamentale de votre couteau suisse.

Ce qui suit est une très courte liste d'outils open source que j'ai appliqués à mon terminal OSX. Lorsqu'ils sont utilisés ensemble, ils me permettent de naviguer dans mon cluster Kubernetes, de résoudre rapidement les problèmes et de surveiller le comportement. J'ai éliminé de nombreuses petites utilités et je me suis concentré sur les outils que j'utilise tous les jours.

#### Avant tout outil...

Avant de vous lancer dans ces outils, je vous recommande vivement d'installer [zsh](https://ohmyz.sh/). Il s'agit d'un wrapper open source exceptionnel autour du terminal standard OSX. Il est plus riche en fonctionnalités et intuitif, et les plugins que vous pouvez installer sont fantastiques. Certains de ces outils listés supposent que vous avez ZSH installé.

#### [k9s](https://github.com/derailed/k9s)

![Image](https://cdn-media-1.freecodecamp.org/images/x6Tesdbm6GNXgOtJFplS3VyHt8FjKe0ayWSX)
_oh oui_

Je commence fort. K9s est l'outil CLI mère pour le cluster Kubernetes. Vous pouvez vous connecter directement aux pods avec une seule touche, voir les logs, supprimer des ressources et plus encore. Il offre un accès exceptionnel pour les opérations les plus courantes que vous effectuerez. C'est un incontournable pour tout ingénieur utilisant Kubernetes.

#### [kubectx](https://github.com/ahmetb/kubectx)

Mais une chose que K9s ne supporte pas est le passage entre différents contextes dans votre configuration Kubernetes. Il est très rare que nous n'ayons qu'un seul cluster. Passer de l'un à l'autre est aussi simple que

```
kubectl config use-context my-context
```

Mais avec cela, il y a quelques prérequis :

* Vous devez connaître le nom du cluster avant de l'exécuter.
* Il y a une autre commande similaire `set-context` qui pourrait vous tromper.

`kubectx` présente une alternative plus simple à cela. Si vous exécutez `kubectx` seul, il listera tous les contextes de votre fichier `.kube/config`. Vous pouvez ensuite fournir le nom du contexte qui vous intéresse :

```bash
kubectx my-context
```

Pas besoin de se souvenir de tous les contextes, pas besoin de vérifier manuellement les fichiers et aucune possibilité de se tromper de commande. Simple et efficace. Combiné avec `k9s`, cela offre une grande navigabilité depuis votre CLI avec un minimum de touches.

#### [kubens](https://github.com/ahmetb/kubectx)

Une fois que vous naviguez entre les contextes, vous pouvez vouloir creuser dans un espace de noms spécifique. Une fois de plus, il est très courant d'avoir plus de quelques espaces de noms dans votre cluster. Eh bien, [ahmetb](https://twitter.com/ahmetb) (le gentleman qui vous a apporté `kubectx`) a également mis au point `kubens`. C'est la même chose que `kubectx`, mais pour les espaces de noms.

```bash
kubens kube-system
```

Maintenant, toutes vos commandes s'exécutent contre l'espace de noms `kube-system`, par défaut. Vous pouvez également exécuter `kubens` sans rien d'autre pour voir une liste de vos espaces de noms.

#### [kube-ps1](https://github.com/jonmosco/kube-ps1)

Donc, vous pouvez basculer entre les contextes et les espaces de noms. Mais comment savoir lequel vous visez actuellement ? C'est pénible de devoir vérifier constamment. Pour le moment, pour le savoir, vous devriez exécuter :

```bash
kubens
kubectx
kubectl <my-command>
```

Pour éviter cela, `ps1` est un plugin zsh qui vous montrera automatiquement votre contexte et espace de noms actuels :

![Image](https://cdn-media-1.freecodecamp.org/images/prQC-ZDrz2hCz5ggKEIgyL9CIiMWu-KDP2Hy)
_Je pointe vers mon contexte minikube et l'espace de noms par défaut_

Maintenant, vous pouvez voir quel espace de noms et contexte vous visez sans exécuter une seule commande. Il est également hautement configurable — vous pouvez désactiver l'espace de noms ou le contexte, si vous n'êtes intéressé que par l'un d'eux, ou vous pouvez utiliser `kubeoff` pour désactiver entièrement l'ensemble.

#### [popeye](https://github.com/derailed/popeye)

Maintenant, passons à quelque chose de légèrement différent. `popeye` exécutera des analyses automatiques des ressources dans votre dépôt et mettra en évidence des problèmes clairs et évidents. C'est un outil très nouveau et que j'ai trouvé très utile. Si vous cherchez à faire un peu de ménage de printemps dans votre cluster, commencer avec `popeye` vous donnera des indications claires sur ce qui doit être corrigé.

![Image](https://cdn-media-1.freecodecamp.org/images/RrLhd7S2q9Lrkq7i15C8FgLVgIzwgFuUh6CU)
_Ce sont les premières lignes d'un rapport très long et détaillé._

#### [Stern](https://github.com/wercker/stern)

Vous avez déjà utilisé `kubectl logs` ? Vous avez remarqué que vous ne pouvez suivre les logs que d'un seul pod à la fois ? Eh bien, ne vous inquiétez plus ! Stern est un outil qui vous permet de récupérer les logs de plusieurs pods, en fonction d'une requête très flexible.

Je parle régulièrement de Kubernetes, DevOps et bien plus sur mon [compte twitter](https://twitter.com/chris_cooney).