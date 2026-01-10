---
title: Comment simplifier le dépannage de Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-28T22:43:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-sohel-patel-1804035.jpg
tags:
- name: containers
  slug: containers
- name: Kubernetes
  slug: kubernetes
seo_title: Comment simplifier le dépannage de Kubernetes
seo_desc: "By Andrej Kovacevic\nDiagnosing and resolving issues in Kubernetes can\
  \ be quite challenging. Kubernetes, after all, is a complex system. \nResolving\
  \ problems even in small K8s clusters, nodes, and containers can be tricky, and\
  \ it's often hard to identi..."
---

Par Andrej Kovacevic

Diagnostiquer et résoudre les problèmes dans Kubernetes peut être assez difficile. Kubernetes, après tout, [est un système complexe](https://kubernetes.io/docs/concepts/). 

Résoudre les problèmes même dans de petits clusters K8s, nœuds et conteneurs peut être délicat, et il est souvent difficile d'identifier et de traiter les problèmes. Et un problème n'est même pas toujours facile à tracer – il peut s'agir d'un problème dans un pod ou des pods, un seul conteneur, un contrôleur, un plan de contrôle, ou dans plusieurs composants. 

Comme vous pouvez vous y attendre, la complexité croît de manière exponentielle lorsque vous traitez un environnement de production à grande échelle avec de nombreux microservices impliqués. 

Ces microservices sont souvent créés par différentes équipes de développement. Il arrive également que ces microservices soient construits collaborativement par différentes équipes mais sur un cluster K8s commun. 

Dans de tels scénarios, il peut y avoir de la confusion quant à savoir qui est responsable du dépannage de quoi.

Mais ne vous inquiétez pas – vous pouvez éviter de transformer le dépannage de Kubernetes en un désordre ingérable et de gaspiller des ressources avec l'aide des conseils suivants.

## Augmenter la visibilité

L'un des points les plus [importants dans le dépannage de Kubernetes](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/) est le besoin d'une meilleure visibilité. 

Les données de l'enquête The State of Kubernetes Security 2020 montrent que 75 pour cent des utilisateurs de Kubernetes considèrent la visibilité comme essentielle, car il peut être fastidieux et difficile de déterminer et d'examiner rapidement tout ce qu'une organisation a déployé au fil du temps.

### Pourquoi la visibilité est-elle importante dans K8s ?

Une visibilité améliorée de K8s vous aide vraiment à obtenir des informations opérationnelles et de sécurité. Elle permet également de réaliser ce qui suit :

* **Assurer la conformité.** Lorsque les organisations se conforment aux normes ou directives établies, la probabilité de se retrouver dans des scénarios compliqués ou alambiqués diminue vraiment. Cela signifie également que le dépannage devient beaucoup plus facile.
* **Vérifier le trafic approprié.** Le trafic de données entre les services ou les microservices, en particulier, est comme une représentation de la santé d'un système K8s. Le trafic doit aller là où il devrait. Sinon, attendez-vous à des dysfonctionnements graves et à des problèmes critiques.
* **Savoir ce qui s'exécute dans l'environnement K8s et déterminer si ils sont correctement configurés.** Il est extrêmement difficile de mener un quelconque dépannage si vous n'êtes pas familier avec votre environnement K8s.
* **Prédire les besoins saisonniers.** Avec les connaissances et la compréhension appropriées de Kubernetes, vous pouvez voir des tendances ou des schémas dans l'utilisation des ressources. Cela vous aide à faire des projections et des prédictions qui peuvent également être utiles dans le dépannage.
* **Permettre une utilisation efficace des ressources.** Une visibilité accrue vous permet de déterminer si vous utilisez la bonne quantité de ressources par rapport à l'historique de latence et de performance.
* **Dépannage efficace.** Avoir une compréhension claire de tout ce qui se passe dans un environnement utilisant Kubernetes conduit finalement à de meilleurs résultats de dépannage, car il est plus facile de trouver la cause racine des problèmes que vous rencontrez avec les applications et les microservices.

### Comment améliorer votre visibilité K8s

Si vous souhaitez améliorer votre visibilité K8s, vous devrez collecter deux types de données : en temps réel et historiques. 

Les données en temps réel sont nécessaires pour identifier et résoudre un problème actuel. Les données historiques servent de base aux activités de référence par rapport à quelque chose qui est considéré comme régulier ou normal. 

Les deux types de données sont utiles pour le dépannage et peuvent devenir encore plus utiles lorsqu'ils améliorent votre visibilité Kubernetes.

Vous pouvez atteindre une visibilité accrue en créant un moyen d'obtenir et d'analyser efficacement les données en temps réel et historiques. Vous pouvez également augmenter la visibilité en utilisant des outils qui facilitent le déploiement et la surveillance améliorés. 

Il existe de nombreux outils Kubernetes qui permettent la surveillance, le contrôle et le traçage en direct. Ces outils peuvent vous fournir des pages de mise à jour de statut robustes, des métriques et des fonctions OpenTracing qui incluent le support pour les plateformes d'observabilité telles que LightStep et Datadog.

## Établir une gestion des pannes organisée et efficace

Il ne suffit pas de trouver les pannes. Vous avez également besoin d'une manière organisée et efficace de gérer les problèmes. Cela aide à prévenir (ou à résoudre plus rapidement) des problèmes similaires à l'avenir. 

Comme nous venons de le discuter, une visibilité améliorée de Kubernetes vous aide à utiliser vos ressources plus efficacement. Et vous devriez tirer parti de cet avantage d'efficacité en adoptant une approche organisée et efficace dans la gestion de vos pannes Kubernetes. 

Pour commencer, faites un point pour maîtriser les erreurs courantes de K8s, comme celles décrites ci-dessous. Dans de nombreux cas, les problèmes sont simplement des erreurs courantes ou simples que de nombreux développeurs K8s tendent à suranalyser.

### Erreurs courantes de Kubernetes

[**CreateContainerConfigError**.](https://datafloq.com/read/how-debug-createcontainerconfig-error/17789) Cette erreur provient généralement d'une ConfigMap ou d'un secret manquant (objets K8s qui contiennent des données sensibles telles que les identifiants de connexion). 

Le problème peut être un problème d'authentification dans le registre de conteneurs ou l'utilisation d'un nom ou d'une balise d'image incorrecte. Vous pouvez identifier ces problèmes en exécutant les commandes appropriées.

**CrashLoopBackOff.** Cette erreur se produit lorsqu'un pod ne peut pas être planifié sur un nœud. Cela peut se produire parce que vous n'avez pas assez de ressources sur un nœud pour exécuter un pod ou un pod qui n'a pas réussi à monter les volumes demandés.

**Kubernetes Node Not Ready.** Cela se produit lorsqu'un nœud de travail est terminé ou plante, ce qui entraîne l'indisponibilité de tous les pods stateful résidant sur le nœud arrêté. 

Cela se résout généralement de lui-même après un certain temps. Si le temps est de l'essence, cependant, vous devrez reprogrammer les pods stateful sur un autre nœud en cours d'exécution.

Pour d'autres problèmes, le dépannage standard implique généralement quelques étapes. Pour le dépannage des pods K8s, vous devrez généralement :

* examiner la sortie de la commande kubectl describe pod, 
* vérifier l'erreur dans la description du pod,
* vérifier une incompatibilité entre le serveur API et le manifeste de pod local (et le diagnostic d'autres problèmes de pod via les logs du pod), et
* effectuer un débogage Container Exec, un débogage Ephemeral Debug Container et une commande Debug Pod sur le nœud.

En ce qui concerne les clusters K8s, vous devrez afficher les informations de base du cluster, récupérer les logs du cluster et mettre en œuvre des solutions en fonction des problèmes que vous trouvez. 

Pour résoudre un crash ou un arrêt de la machine virtuelle du serveur API, par exemple, vous devrez redémarrer la machine virtuelle du serveur API. Cette solution s'applique également aux crashes de service du plan de contrôle et aux dysfonctionnements de Kubelet.

Vous devriez avoir des workflows prédéfinis pour guider vos réponses à divers problèmes. Encore une fois, le dépannage de Kubernetes n'est pas aussi facile qu'il y paraît. Il n'y a rien de mal à avoir des fiches de référence, surtout lorsque vous traitez des problèmes peu courants.

## Utiliser une solution de dépannage Kubernetes

Pour de nombreuses entreprises ou équipes, l'utilisation d'un service de dépannage K8s peut être le meilleur moyen de gérer les problèmes de Kubernetes. 

Toutes les équipes n'ont pas des experts de premier plan en Kubernetes qui peuvent résoudre les problèmes dès qu'ils surviennent. Et tout le monde n'a pas les bons outils et procédures systématiques en place pour traiter les problèmes de conteneur, de pod, de cluster ou de [nœud](https://developer.ibm.com/articles/6-reasons-your-node-js-apps-are-failing/).

Une solution de dépannage peut fournir une plateforme unifiée pour suivre les activités K8s, ce qui facilite la recherche de la source des problèmes. 

Un tel système peut offrir un moyen efficace d'améliorer la visibilité de K8s en fournissant une chronologie complète, par exemple. Ou il peut afficher toutes les modifications de code et de configuration, les logs de pod, les statuts de déploiement, les alertes, les diffs de code et d'autres détails de manière organisée.

De plus, les services avancés de dépannage de Kubernetes sont conçus pour fournir des informations sur les dépendances de service. Ils facilitent la compréhension des changements inter-services qui se produisent dans une organisation. 

Ils peuvent fournir des détails utiles sur les réactions en chaîne qui suivent certains changements pour vous aider à identifier et éventuellement résoudre le problème.

## En résumé

Dire que le dépannage de Kubernetes peut être simplifié peut sembler un oxymore. Et promettre une manière vraiment simplifiée de traiter les problèmes de K8s, c'est pousser l'enveloppe trop loin. 

Mais il est certainement possible d'établir des moyens de rendre le processus de dépannage moins compliqué et fastidieux qu'il ne l'est normalement.