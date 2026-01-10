---
title: Comment une mauvaise configuration de TensorFlow dans Docker peut être 10 fois
  plus lente que prévu
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
seo_title: Comment une mauvaise configuration de TensorFlow dans Docker peut être
  10 fois plus lente que prévu
seo_desc: 'By Pierre Paci

  TL:DR: TensorFlow reads the number of logical CPU cores to configure itself, which
  can be all wrong when you have a container with CPU restriction.

  Let’s do a simple benchmark comparing an inference on GPU, CPU on the host, CPU
  on dock...'
---

Par Pierre Paci

TL:DR: TensorFlow lit le nombre de cœurs logiques du CPU pour se configurer, ce qui peut être complètement faux lorsque vous avez un conteneur avec des restrictions CPU.

Faisons un simple benchmark comparant une inférence sur GPU, CPU sur l'hôte, CPU sur Docker, et CPU sur Docker avec restriction.

![Image](https://cdn-media-1.freecodecamp.org/images/y4ZPOO6WxCSkO-6s2atP9DTwTLgBbVle0fFT)
_Notre micro benchmark_

Keras/TensorFlow semble effectuer certaines opérations sur GPU lors du premier appel à .predict(), nous ne chronométrerons donc pas le premier appel, mais le second.

En exécutant cela sur ma Nvidia 1080, cela donne un **temps d'inférence de ~0,01s** par image.

Cette fois, sur mon CPU, sans conteneur, **cela prend ~0,12s**. 12 fois plus lent est de l'ordre de grandeur de ce à quoi s'attendre entre CPU et GPU. Notez que mon TensorFlow n'est pas correctement compilé avec le support AVX ou MKL. Le GPU a été rendu invisible en utilisant la variable d'environnement **CUDA_VISIBLE_DEVICES**.

Ajoutons un conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/sB5ZQBmwoQiTI3y7YRonETjWAgJjbajplop5)
_Notre simple conteneur._

Note : Pillow est une bibliothèque de gestion d'images requise par Keras pour charger une image.

L'exécution de ce conteneur donne un **temps d'inférence de ~0,15s**. Peut-être un certain surcoût de Docker ou certaines versions de TF sont différentes de mon hôte, mais ce n'est pas le sujet de cet article. Le vrai point arrive maintenant.

#### La solution

J'utilise un i7 7700k avec 8 cœurs logiques, 4 physiques. Donc, si nous configurons le conteneur pour utiliser seulement 2 cœurs logiques (1 physique), cela devrait être environ 4 fois plus lent, soit environ 0,6s. Les restrictions seront faites par l'[API Docker](https://docs.docker.com/config/containers/resource_constraints/#cpu). **En réalité, cela donne un temps d'inférence de 2,5s — 4 fois plus lent que prévu !**

En fait, TensorFlow utilise le nombre de cœurs logiques pour calculer certains paramètres de performance internes. Un surcoût se produira ici puisque le nombre de cœurs rapportés diffère de ce qui est disponible. Sur votre serveur de production, cela pourrait être encore plus important. **Sur nos serveurs, c'était 10 fois plus lent puisque le Xeon a plus de cœurs.**

Alors, que pouvons-nous faire ?

Le [guide de performance de TensorFlow](https://www.tensorflow.org/performance/performance_guide#optimizing_for_cpu) a la réponse !

![Image](https://cdn-media-1.freecodecamp.org/images/U1JE2b5hFA18vqiEH6GuKsAzapkmhXt2k5eL)

En utilisant ces nouveaux paramètres, nous obtenons le code suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/4K6wPcJD74UHhF5zpitLzPiZa0XGnvPtkl3k)

**Et maintenant, cela ne prend que ~0,6s**. Et c'est exactement ce à quoi nous nous attendions !

En conclusion, même si Docker semble simplifier l'environnement de production, soyez toujours prudent ! Et n'oubliez pas d'utiliser le guide de performance dans la documentation.