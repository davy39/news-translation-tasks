---
title: Sécurité Kubernetes – Comment utiliser le contrôle d'admission dynamique pour
  sécuriser votre chaîne d'approvisionnement de conteneurs
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
seo_title: Sécurité Kubernetes – Comment utiliser le contrôle d'admission dynamique
  pour sécuriser votre chaîne d'approvisionnement de conteneurs
seo_desc: "By Nahla Davies\nContainers have exploded in popularity in recent years.\
  \ And as more developers are using these containers, they need more tools to manage\
  \ them and their interactions with them effectively. \nTo help manage all this,\
  \ many devs use Kuber..."
---

Par Nahla Davies

Les conteneurs ont connu une explosion de popularité ces dernières années. Et comme de plus en plus de développeurs utilisent ces conteneurs, ils ont besoin de plus d'outils pour les gérer et interagir avec eux efficacement. 

Pour aider à gérer tout cela, de nombreux développeurs utilisent Kubernetes. Et il est [devenu la norme de facto](https://www.freecodecamp.org/news/the-kubernetes-handbook/) pour l'orchestration de conteneurs.

Bien que les conteneurs aident à rendre le cycle de vie du développement et du déploiement logiciel plus efficace, ils peuvent également multiplier les façons dont les pirates peuvent attaquer votre organisation. 

Et bien que Kubernetes simplifie définitivement le processus de gestion des conteneurs, il présente également des vulnérabilités de sécurité. 

Étant donné la popularité de Kubernetes, les cybercriminels ont mis beaucoup d'efforts à exploiter ces vulnérabilités. Par conséquent, les attaques sur la chaîne d'approvisionnement [ont considérablement augmenté](https://www.darkreading.com/cloud/software-container-supply-chain-sees-spike-in-attacks/d/d-id/1341353) au cours de l'année dernière.

Ainsi, la sécurisation de la chaîne d'approvisionnement Kubernetes est une priorité élevée pour de nombreuses organisations. 

Une fonctionnalité de sécurité importante à laquelle vous devez prêter une attention particulière si vous êtes un utilisateur de Kubernetes est le contrôle d'admission dynamique. 

Dans cet article, nous discuterons des vulnérabilités de la chaîne d'approvisionnement Kubernetes et de la manière de les traiter avec le contrôle d'admission dynamique.

## Vulnérabilités dans la chaîne d'approvisionnement Kubernetes

Récemment, presque tous les utilisateurs de Kubernetes [ont subi un incident de sécurité](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en.pdf) causé par diverses vulnérabilités, allant de la mauvaise configuration aux audits échoués. En raison de cela, les préoccupations de sécurité ont commencé à avoir un impact sur les pratiques de déploiement. 

Plus de la moitié des organisations qui utilisent Kubernetes ont retardé le déploiement d'une application uniquement en raison de problèmes de sécurité.

Si vous souhaitez sécuriser votre chaîne d'approvisionnement Kubernetes, vous devez comprendre les composants de la chaîne d'approvisionnement pour les applications conteneurisées et leurs vulnérabilités associées. 

La chaîne d'approvisionnement s'étend bien au-delà de Kubernetes lui-même et [inclut le contenu des conteneurs](https://www.freecodecamp.org/news/a-simple-introduction-to-kubernetes-container-orchestration/) que Kubernetes gère ainsi que l'hôte du conteneur. 

À l'intérieur du conteneur, vous aurez généralement un ensemble de code provenant de diverses sources (internes et externes). Cela donne aux attaquants de nombreuses opportunités de faire preuve de créativité. 

Pour se protéger contre ces menaces, vous devez sécuriser correctement tous les ensembles de code, quelle que soit leur source – et cela peut être difficile. 

Par exemple, la sécurisation du code provenant de distributions Linux telles que les bibliothèques openssl ou glibc peut nécessiter uniquement l'application du dernier patch. 

Mais le code provenant d'autres sources externes, telles que les bibliothèques open-source en amont ou les processus de développement internes, peut être plus difficile à sécuriser.

Le développement interne est peut-être la plus grande menace organisationnelle, en particulier lorsque les développeurs privilégient la rapidité de publication à la sécurité.  

De nombreuses organisations ont décentralisé la responsabilité de la sécurité des conteneurs, avec la participation de tous, des développeurs à DevOps. Mais de plus en plus d'organisations [créent des unités DevSecOps](https://devops.com/from-agile-to-devops-to-devsecops-the-next-evolution/) et placent la sécurité Kubernetes entre leurs mains.

## Comment sécuriser la chaîne d'approvisionnement Kubernetes avec le contrôle d'admission dynamique

Dans Kubernetes, le contrôle d'admission dynamique implique des contrôleurs d'admission définis ou configurés par l'utilisateur plutôt que des contrôleurs intégrés standard.

### Qu'est-ce que les contrôleurs d'admission ?

Les contrôleurs d'admission prennent le relais après que le serveur API Kubernetes a reçu une authentification et une autorisation d'une demande. Ces morceaux de code interceptent la demande avant qu'un conteneur ne soit initialisé et ajouté en tant que pod au cluster Kubernetes. 

Essentiellement, le contrôleur d'admission tente de vérifier que l'image est sûre. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-12.png)
_[Source de l'image](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)_

Les contrôleurs d'admission [implémentent une variété de fonctions](https://www.openpolicyagent.org/docs/v0.11.0/kubernetes-admission-control/), de l'application de quotas de ressources à l'exécution de tâches critiques pour le cluster. Vous devrez avoir des contrôleurs d'admission correctement configurés pour faire fonctionner correctement de nombreuses fonctionnalités avancées de Kubernetes.

### Qu'est-ce que les webhooks d'admission ?

Les contrôleurs d'admission dynamiques reposent sur des webhooks d'admission, qui sont des rappels HTTP définis par l'utilisateur qui traitent les demandes d'admission. 

Dans Kubernetes, il existe deux types de webhooks d'admission : les webhooks d'admission de validation et les webhooks d'admission de mutation. 

Dans le processus de contrôle d'admission, les contrôles d'admission de mutation s'exécutent avant les contrôles de validation. Les deux types de webhooks sont essentiellement auto-explicatifs en principe, bien que leur fonctionnement spécifique nécessite quelques explications. 

#### Webhooks d'admission de validation

Les webhooks d'admission de validation interceptent et valident les demandes adressées à l'API Kubernetes à l'aide d'un webhook externe. Il est important de noter, cependant, qu'ils ne peuvent pas modifier les demandes. 

Tous les webhooks de validation correspondant à une demande s'exécutent en parallèle (car aucune modification potentielle ne peut se produire), et le contrôleur rejette la demande en cas d'échec de tout webhook correspondant. 

Les webhooks d'admission de validation sont du type tout ou rien – si la demande ne correspond pas précisément, le contrôle la rejette.

#### Webhooks d'admission de mutation

En revanche, les webhooks d'admission de mutation sont capables de modifier les demandes, permettant ainsi de traiter les demandes qui ne sont que légèrement non conformes à la règle. 

Si plusieurs webhooks correspondent à une demande, ils s'exécutent en série, et chacun peut modifier la demande. Comme les contrôleurs de mutation s'exécutent en premier, les demandes modifiées peuvent encore être rejetées par les webhooks de validation.

Le fonctionnement conjoint des webhooks d'admission de mutation et de validation permet aux développeurs Kubernetes de [s'assurer que les demandes sont conformes](https://www.freecodecamp.org/news/how-to-become-a-certified-kubernetes-application-developer/) et valides avant l'instantiation des conteneurs.

## Politiques de sécurité des pods Kubernetes

Les politiques de sécurité des pods (ou PSP) sont une fonctionnalité de sécurité Kubernetes qui repose sur la mise en œuvre de contrôles d'admission. 

Les PSP définissent des conditions et des valeurs par défaut que les pods Kubernetes doivent respecter pour être acceptés dans le système de conteneurs. 

Les PSP peuvent imposer des politiques telles que la désactivation des conteneurs privilégiés, la prévention de l'escalade de privilèges et l'empêchement des conteneurs de s'exécuter en tant que root. 

Les PSP permettent aux administrateurs d'appliquer facilement les politiques de sécurité organisationnelles à l'ensemble d'un espace de noms. Bien que les PSP nécessitent l'activation des contrôleurs d'admission, ils doivent être activés séparément.

Selon les normes de sécurité des pods Kubernetes, il existe trois types de politiques :

* La politique de base a des restrictions minimales, bien qu'elle n'autorise pas l'escalade de privilèges. 
* Pour les utilisateurs les moins dignes de confiance, il existe la politique restreinte qui désactive certaines fonctions conformément aux meilleures pratiques de durcissement des pods. 
* Au niveau le plus élevé se trouve la politique privilégiée, qui est la plus large, permettant le plus de permissions et d'escalade de privilèges. 

Kubernetes a commencé à déprécier les PSP avec la sortie de la version 1.21. Les PSP seront [supprimés entièrement en 2022](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/) avec la sortie de la version 1.25. Par conséquent, si vous utilisez Kubernetes, vous devriez envisager soigneusement des options de sécurité alternatives pour toutes les applications conteneurisées futures.

## Ne négligez pas les outils de sécurité standard de Kubernetes

Si vous utilisez des conteneurs, vous devez être conscient des vulnérabilités courantes dans tout votre environnement Kubernetes. 

Pour atteindre une sécurité maximale, les développeurs et les utilisateurs doivent appliquer des fonctionnalités de sécurité spécifiques à Kubernetes telles que le contrôle d'admission dynamique et des fonctionnalités de sécurité réseau standard [comme les VPN](https://www.freecodecamp.org/news/what-does-a-vpn-do-and-how-does-it-work-a-guide-to-virtual-private-networks/).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-13.png)
_[Source de l'image](https://securityboulevard.com/2020/03/vpn-a-key-to-securing-an-online-work-environment/)_

Une vulnérabilité récente de Kubernetes impliquait des attaquants qui avaient accès à l'API et qui pouvaient obtenir un accès administrateur complet à un cluster Kubernetes et à toutes les ressources associées. 

Un VPN peut aider à éviter cela et d'autres vulnérabilités similaires où le serveur API est exposé. Mais il est important de sélectionner le bon VPN pour vos besoins.

### Comment choisir un VPN

Selon l'expert en cybersécurité Ludovic Rembert de Privacy Canada, les protocoles de chiffrement [sont le facteur le plus important](https://privacycanada.net/best-vpn/#:~:text=a%20vpn%20protocol) à rechercher dans un VPN. 

> « Un protocole VPN détermine comment vos données sont acheminées entre votre machine et le serveur. Différents protocoles ont différents coûts et avantages en fonction de vos besoins. Par exemple, certains privilégient la confidentialité et la sécurité, tandis que d'autres privilégient la vitesse... un appareil PE Provider Edge est un appareil unique, ou plusieurs appareils, à la périphérie du réseau du fournisseur. Cet appareil se connecte ensuite via des appareils Consumer Edge. Dans cette configuration, les utilisateurs peuvent consulter un site web, tandis que l'appareil du fournisseur n'est conscient que de l'appareil VPN. » – Rembert

## Conclusion

Les applications conteneurisées continueront à être de plus en plus utilisées dans les années à venir, tout comme les ressources de gestion de conteneurs [telles que Kubernetes](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/). 

À mesure que la popularité de ces outils augmente, le nombre d'attaques à tous les points de la chaîne d'approvisionnement augmentera également. 

Ainsi, si vous travaillez avec Kubernetes, vous devez tirer parti de toutes les ressources de sécurité disponibles pour garantir une sécurité et une fiabilité maximales des applications. 

Et l'application de contrôles d'application dynamiques pour vérifier que les demandes sont conformes aux politiques de sécurité est une étape importante dans ce processus.