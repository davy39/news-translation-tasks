---
title: Sécurité Kubernetes – Vulnérabilités et expositions courantes pour les programmes
  K8s
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
seo_title: Sécurité Kubernetes – Vulnérabilités et expositions courantes pour les
  programmes K8s
seo_desc: "By Prajwal Kulkarni\nKubernetes has become the go-to tool for orchestration,\
  \ scaling, automated deployment, and management of containerized applications. \n\
  Simply put, Kubernetes is a system that maintains coordination between diverse applications\
  \ acro..."
---

Par Prajwal Kulkarni

Kubernetes est devenu l'outil de référence pour l'orchestration, la mise à l'échelle, le déploiement automatisé et la gestion d'applications conteneurisées. 

Pour faire simple, Kubernetes est un système qui assure la coordination entre diverses applications sur un groupe de machines.

Il est important de noter que ce système traite principalement des applications conteneurisées, comme les images Docker. Il s'agit essentiellement d'une forme de virtualisation où les applications s'exécutent dans des espaces utilisateurs isolés appelés **conteneurs**.

## Problèmes de sécurité avec les conteneurs

Cependant, l'utilisateur définit les règles sur la façon dont l'application doit s'exécuter et interagir avec d'autres applications et le monde extérieur. Et tout ce qui implique une intervention humaine est sujet aux failles et aux erreurs. 

La gravité de l'erreur dépend souvent des compétences de la personne qui gère les conteneurs. Parfois, la moindre erreur peut paralyser le système. Un exemple notable est la [vulnérabilité Log4j](https://theconversation.com/what-is-log4j-a-cybersecurity-expert-explains-the-latest-internet-vulnerability-how-bad-it-is-and-whats-at-stake-173896) en Java qui a causé une panne majeure sur Internet ces derniers temps. 

Il est souvent impossible pour un logiciel ou une application d'être sécurisé à 100 % contre les attaquants. Mais cela ne devrait pas signifier à tort qu'il est acceptable d'avoir des fuites et des vulnérabilités en espérant que personne ne les remarque.

Vous devriez toujours rechercher les vulnérabilités et expositions de sécurité et leur appliquer des correctifs dès qu'ils sont disponibles.

De telles failles pourraient rendre un cluster ou un conteneur vulnérable, permettant à des individus non autorisés de les exploiter. Et avec la popularité croissante de Kubernetes, nous devons examiner de plus près comment évaluer son efficacité et gérer les problèmes de sécurité des conteneurs.

Pour mieux protéger vos configurations et programmes Kubernetes, examinons quelques vulnérabilités et expositions courantes, ainsi que les meilleures pratiques de sécurité Kubernetes.

## Le dilemme de la configuration

![Image](https://www.freecodecamp.org/news/content/images/2022/03/access-control-overview.svg)
_[Source](https://kubernetes.io/docs/concepts/security/controlling-access/)_

Si vous débutez dans le monde de Kubernetes et que vous déployez un projet par vous-même, vous pourriez avoir du mal à comprendre les règles de configuration de sécurité. C'est parce que, malheureusement, Kubernetes ne fournit pas de règles de configuration par défaut suffisamment sécurisées dans de tels cas. 

Bien que la configuration de la sécurité ne soit pas d'une importance capitale lorsque vous essayez de prendre en main l'environnement, elle devient critique lors des étapes ultérieures, notamment lors du déploiement en production. 

Un problème similaire existe avec la manière dont les pods communiquent entre eux. Ces droits de communication sont définis par des politiques réseau (network policies), mais aucune politique de ce type n'est associée aux pods par défaut. Encore une fois, c'est quelque chose que vous devez configurer manuellement.

Une solution simple pour y remédier consiste à activer le contrôle d'accès basé sur les rôles (RBAC) afin de définir qui a accès à l'API et quelles autorisations ils détiennent. 

Vous pouvez utiliser des attributs tels que `allowPrivilegeEscalation` et `readOnly` pour renforcer la sécurité en termes de niveaux de lecture et de privilèges.

La politique suivante montre les niveaux d'autorisation de l'utilisateur "bob" :

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

Ici, l'utilisateur "bob" est autorisé uniquement à lire les objets de l'espace de noms (namespace) "projectCaribou".

Si la requête était de type "write" ou "update", l'action échouerait, comme prévu.

## Code malveillant dans les images Docker

Étant donné que Kubernetes traite souvent des applications conteneurisées, généralement des [images Docker](https://docs.docker.com/engine/reference/commandline/image/), les attaquants s'introduisent souvent dans le cluster ou le nœud Kube en accédant depuis l'intérieur de l'application conteneurisée. 

Bien qu'il existe différentes solutions pour éviter différents types d'attaques, vous pourriez toujours limiter l'utilisation des ressources mémoire pour prévenir les attaques DoS. 

Vous pouvez le faire en configurant un contrôleur d'ingress (ingress controller) défini pour limiter le nombre de requêtes dans un laps de temps – par exemple, 10 requêtes par seconde ou 1000 requêtes par minute. 

Vous pouvez implémenter cela en limitant les requêtes par IP client ou en limitant les requêtes au niveau de l'hôte du service. 

Alternativement, une liste de contrôle d'accès (ACL) peut également être définie pour autoriser uniquement des adresses IP individuelles ou sélectionnées. Cette technique d'atténuation garantit qu'aucun trafic de requêtes anonymes n'inonde le serveur et s'assure également que seuls les trafics/requêtes provenant de sources crédibles sont traités.

Scanner les applications avant le déploiement est également une bonne règle de base pour détecter le code malveillant et agir immédiatement.

## Le cluster est sécurisé, mais pas la transmission

En général, la priorité est donnée uniquement à la sécurité du cluster car c'est lui qui gère les applications. Mais une chose souvent négligée est le fait que la transmission ne contient aucune sorte de mesure de sécurité ou de chiffrement par défaut. 

Il s'agit d'un problème d'exposition courant, et l'ignorer pourrait ouvrir la porte à des intrus pour obtenir un accès non autorisé à votre système. Cela signifie que la [couche de sécurité de transport](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) (TLS) devrait gérer la communication dans le cluster entre les services. 

Les améliorations de la technologie réseau ont conduit à l'émergence de produits comme LinkerD qui peuvent activer TLS par défaut tout en fournissant des informations de télémétrie supplémentaires sur les transactions de service.

Le même principe s'applique également à « [etcd](https://www.ibm.com/cloud/learn/etcd) », qui stocke l'état du cluster. S'il n'est pas sécurisé, il devient une cible attrayante pour les attaquants car il leur est possible de prendre le contrôle de l'ensemble du cluster. Même s'ils n'ont qu'un accès en lecture, ils pourraient en abuser pour élever leurs privilèges.

## Garder un œil sur le runtime

Même si vous réussissez à surmonter les vulnérabilités liées aux politiques et à la configuration, le runtime présente un nouvel ensemble d'obstacles. Un exemple de vulnérabilité de sécurité au runtime est un conteneur compromis qui exécute des processus malveillants. 

Bien que le crypto-minage soit devenu une cible populaire pour les acteurs malveillants qui s'introduisent dans les paramètres des conteneurs, les attaquants peuvent mener d'autres actions hostiles, telles que le scan de ports réseau pour un accès ouvert à des ressources souhaitables, à partir d'un conteneur compromis.

Vous pouvez surveiller activement l'activité au runtime des conteneurs critiques pour la sécurité, comme l'activité des processus et la communication réseau, pour résoudre ces problèmes et d'autres problèmes liés au runtime.

De plus, il est fortement recommandé d'incorporer les informations sur les moments de build et de déploiement pour comparer l'activité observée à l'activité attendue pendant le runtime. Cela facilite la détection de tout comportement inhabituel.

## Le problème de la conformité

La conformité aux normes de sécurité, aux exigences réglementaires et aux normes, ainsi qu'aux réglementations internes d'une organisation peut être difficile dans les systèmes cloud-native.

La raison la plus courante d'un échec de conformité est le fait de négliger l'aspect sécurité lors du processus d'adoption des conteneurs.

La meilleure façon d'atténuer ces vulnérabilités est d'adopter des contrôles de sécurité tôt dans le cycle de vie des conteneurs. Automatiser les vérifications nécessaires dans la mesure du possible est également une bonne pratique pour réduire vos surcharges (overheads).

## Conclusion

La sécurité est importante pour les conteneurs, et c'est quelque chose que vous devez prendre en compte et gérer lorsque vous travaillez avec Kubernetes. 

En fin de compte, votre objectif ultime devrait être de rendre difficile l'accès des intrus à vos systèmes. Et même s'ils parviennent à entrer, l'infrastructure doit être suffisamment performante pour détecter une activité anormale et déclencher des actions pour l'empêcher de se propager. 

Comme le dit Rory McCune, consultant principal en sécurité chez [NCC Group](https://www.nccgroup.com/us/) :

> _"Kubernetes est très complexe, et il est très facile de faire une erreur dans sa configuration."_ 

Les vulnérabilités de Kubernetes et des conteneurs, si elles ne sont pas corrigées, pourraient entraîner de graves expositions.