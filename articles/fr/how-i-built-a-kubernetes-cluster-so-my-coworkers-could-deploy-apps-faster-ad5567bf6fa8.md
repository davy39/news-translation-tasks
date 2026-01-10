---
title: Comment j'ai construit un cluster Kubernetes pour que mes collègues puissent
  déployer des applications plus rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-26T15:50:56.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-kubernetes-cluster-so-my-coworkers-could-deploy-apps-faster-ad5567bf6fa8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tTK6pwJc63dSpVzGImKEvQ.png
tags:
- name: Devops
  slug: devops
- name: GitHub
  slug: github
- name: Kubernetes
  slug: kubernetes
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit un cluster Kubernetes pour que mes collègues puissent
  déployer des applications plus rapidement
seo_desc: 'By cheungpat

  How do you encourage your development team to build more projects without being
  bogged down with deployment? As a company that builds mobile and web products, it’s
  a priority that we create an environment where our team members focus on ...'
---

Par cheungpat

Comment encourager votre équipe de développement à construire plus de projets sans être ralentie par le déploiement ? En tant qu'entreprise qui construit des produits mobiles et web, il est primordial que nous créions un environnement où nos membres d'équipe se concentrent sur la construction plutôt que sur le déploiement.

Mais même si nous avons une plateforme de déploiement, nous aurons toujours besoin de quelqu'un pour gérer l'administration. En tant qu'ingénieurs, tout ce que nous devons répéter, nous voulons l'automatiser.

Quelle serait une manière sécurisée de donner à nos développeurs l'accès à notre plateforme de déploiement ?

1. Nous voulons permettre à nos développeurs de construire leurs propres projets (peut-être personnels) sans avoir besoin de demander à un administrateur la permission ou les ressources pour déployer une nouvelle application pour des tests ou des expériences
2. Nos développeurs peuvent déployer leur propre application, la mettre à jour ou la supprimer
3. Réduire les barrières pour essayer de nouvelles choses (pour ainsi dire)

### Notre solution : Kubernetes

Notre solution a été d'utiliser l'authentification GitHub pour notre cluster Kubernetes.   
   
Pour ceux d'entre vous qui ne savent pas, [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) est un moteur d'orchestration de conteneurs prêt pour la production développé par Google. C'est une plateforme open-source qui permet l'automatisation des opérations de conteneurs. Des choses comme le déploiement et la mise à l'échelle sur un cluster d'hôtes (ou de nœuds).

Avec Kubernetes, nous sommes en mesure de soutenir nos développeurs en tant que clients qui doivent déployer des applications et déployer de nouvelles fonctionnalités de manière transparente sans une lourde charge administrative. Les technologies de conteneurs sont une bonne pratique pour l'emballage des applications backend et leur exécution sur un serveur.  
  
Nous exécutons des conteneurs de différents projets dans le même cluster. Kubernetes nous permet de nous concentrer moins sur les serveurs individuels. Nous pouvons penser à Kubernetes comme à un "grand ordinateur" sur lequel nos membres d'équipe peuvent exécuter des conteneurs.

### Donner à notre équipe l'accès au cluster

Nous voulons que les collègues aient leurs propres identifiants pour accéder au cluster. Cela économise du temps d'administration puisqu'ils n'ont pas besoin d'ouvrir un nouveau compte pour chaque utilisateur. Les nouveaux utilisateurs peuvent générer eux-mêmes les identifiants, ou de nouveaux s'ils perdent leurs identifiants.  
   
Nous cherchions une solution d'authentification qui pourrait répondre à toutes les exigences ci-dessous :

1. Le temps d'administration doit être économisé (puisqu'ils sont aussi nos développeurs)
2. Les nouveaux utilisateurs peuvent générer leurs propres identifiants sans avoir besoin de l'administrateur
3. Les identifiants de l'utilisateur sont toujours privés pour des raisons de sécurité
4. Les développeurs ont leur propre espace pour expérimenter
5. Les espaces de projet peuvent être accessibles et modifiés par plusieurs utilisateurs
6. À l'avenir, nous pourrions vouloir activer l'audit pour suivre les changements

### Tentatives — la plupart des stratégies d'authentification existantes ne conviennent pas

Tout d'abord, de nombreuses méthodes d'authentification existantes nécessitent toujours qu'un administrateur génère ou gère des comptes. C'est la principale raison pour laquelle nous avons écarté la plupart d'entre elles.  
   
Ci-dessous, je vais lister quelques-unes des plus courantes pour référence, mais n'hésitez pas à passer à la section suivante si vous voulez simplement comprendre pourquoi nous avons choisi l'authentification GitHub.

#### **Basé sur les certificats**

Chaque utilisateur a son propre certificat SSL privé pour accéder au cluster, ce qui peut être compliqué à configurer. Cela signifie qu'un administrateur doit gérer une infrastructure à clé publique (c'est-à-dire une autorité de certification) pour signer le certificat de l'utilisateur. De plus, l'administrateur doit le faire lorsque 1) il y a un nouvel utilisateur, 2) le certificat expire, ou 3) l'utilisateur a perdu le certificat/clé privée. Enfin, l'utilisateur doit gérer ses propres matériaux de clé privée lorsqu'il veut utiliser les mêmes certificats SSL sur plusieurs ordinateurs — une faiblesse potentielle de sécurité.

#### **Basé sur le nom d'utilisateur/mot de passe**

Puisque tout le monde sait comment utiliser un nom d'utilisateur et un mot de passe, cela est plus facile à mettre en œuvre que l'authentification basée sur les certificats. Cependant, Kubernetes n'a pas une interface conviviale pour que nos membres d'équipe créent leur propre compte, ce qui signifie que nous avons toujours besoin d'un administrateur pour générer un ensemble de nom d'utilisateur et de mot de passe pour chaque utilisateur. De plus, cela signifie que l'administrateur doit réinitialiser le mot de passe d'un utilisateur si l'utilisateur le perd. Sans une interface utilisateur conviviale, il est également difficile pour l'utilisateur de changer le mot de passe. Kubernetes nécessite également que le serveur API soit redémarré lorsque la liste des noms d'utilisateur/mots de passe change.

#### **Basé sur un jeton pré-généré**

Similaire à l'approche basée sur le nom d'utilisateur/mot de passe, l'administrateur est toujours impliqué pour générer un jeton.  
   
[**Open ID Connect (OIDC)**](http://openid.net/connect/)** : Au moment où nous avons construit le cluster Kubernetes, la prise en charge d'OIDC n'était pas complètement au point, et nous n'étions pas sûrs de la manière d'intégrer OIDC avec les comptes Google. OIDC est une bonne option s'il est complètement implémenté par le serveur API Kubernetes et la commande client (ce qui n'était pas implémenté la dernière fois que j'ai vérifié).

### 5 raisons simples d'utiliser l'authentification GitHub

L'authentification GitHub était une solution simple parce que :

1. Tout le monde dans notre entreprise a déjà un compte GitHub
2. Cela résout notre problème de charge administrative puisque les gens gèrent leurs propres jetons
3. Les utilisateurs peuvent facilement générer un jeton d'accès sur [github.com](http://github.com)
4. C'est hautement flexible puisque les utilisateurs peuvent accéder au cluster Kubernetes sur différents ordinateurs, simplement en générant de nouveaux jetons
5. L'accès peut toujours être révoqué en supprimant le jeton d'accès sur [github.com](http://github.com) (au cas où le jeton GitHub serait divulgué)

### Mise en œuvre de l'authentification GitHub

Nous authentifions nos membres d'équipe en utilisant un jeton GitHub.  
   
Kubernetes prend en charge un [plugin d'authentification de jeton webhook](https://github.com/kubernetes/kubernetes/pull/24902) pour permettre à un service distant de s'authentifier. Donc, tout ce que nous avons à faire est de mettre en œuvre un webhook qui vérifie le jeton.  
   
Lorsque l'utilisateur essaie de s'authentifier auprès de l'API Kubernetes, le serveur API Kubernetes appelle cet authentificateur pour vérifier le jeton porteur. Cet authentificateur vérifie si le jeton d'accès est valide en utilisant l'API GitHub et retourne le nom d'utilisateur GitHub au serveur API en vérifiant si l'utilisateur demandé a accès à la ressource. Il utilise des règles de contrôle d'accès basé sur les rôles (RBAC).  
   
Notez que nous devons exécuter le webhook sur le maître Kubernetes, afin que le serveur API puisse y accéder.  
   
 Voici comment nous avons réellement [implémenté le WebHook](https://github.com/oursky/kubernetes-github-authn/blob/master/main.go) :

Nous avons utilisé [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) parce qu'il offre la plus grande flexibilité sans apporter de modifications de configuration sur le serveur API. En plus de RBAC, Kubernetes dispose de diverses stratégies d'autorisation.   
   
Pour l'instant, l'authentification GitHub ne supprime pas entièrement les responsabilités de l'administrateur. Un administrateur est toujours nécessaire dans certains scénarios :

1. Si un utilisateur veut son propre espace de noms personnel, l'administrateur doit toujours créer l'espace de noms et définir les règles RBAC pour cet utilisateur
2. S'il y a un nouveau projet, l'administrateur doit toujours créer l'espace de noms et définir les règles RBAC pour ce projet

Lors de la configuration du projet, l'administrateur peut désigner un responsable d'équipe pour contrôler les règles RBAC pour les membres de l'équipe participants et contrôler qui a accès à l'espace de noms du projet.

### Maintenant, les membres de l'équipe Oursky peuvent accéder au cluster avec GitHub

Chaque fois que nos coéquipiers ont besoin d'un nouveau déploiement pour leur projet (même pour des projets personnels), ils peuvent simplement obtenir un jeton de GitHub. Nous espérons que cela encouragera notre équipe à construire quelque chose d'intéressant sans se soucier du déploiement stable.  
   
Vous êtes les bienvenus pour jeter un coup d'œil à l'implémentation exacte dans [ce dépôt github](https://github.com/oursky/kubernetes-github-authn). Vous pouvez également mettre en œuvre cette solution dans votre propre cluster.

_Construction d'une application ? Je travaille actuellement sur un [backend open source](http://skygear.io/) chez [Oursky](https://www.freecodecamp.org/news/how-i-built-a-kubernetes-cluster-so-my-coworkers-could-deploy-apps-faster-ad5567bf6fa8/undefined) qui rendra votre travail plus facile._