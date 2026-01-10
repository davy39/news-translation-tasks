---
title: Une introduction aux architectures orientées services et microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-22T14:02:25.000Z'
originalURL: https://freecodecamp.org/news/service-and-micro-service-oriented-architectures-explained-2f8d5da0ecdd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2myWvKpboVAA2sSZ
tags:
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction aux architectures orientées services et microservices
seo_desc: 'By Pulkit Kumar

  We’ve come a long way from the traditional three-tier monolith architecture. In
  order to achieve a fast, robust and scalable model of development, you might try
  to align your application architecture with certain philosophies and deve...'
---

Par Pulkit Kumar

Nous avons parcouru un long chemin depuis l'architecture monolithique traditionnelle à trois niveaux. Afin d'atteindre un modèle de développement rapide, robuste et évolutif, vous pourriez essayer d'aligner votre architecture d'application avec certaines philosophies et modèles de développement, espérant que cela pourrait faciliter la gestion de l'équipe et des délais de développement.

Mais lorsque vous réalisez qu'il existe tellement de modèles de développement que vous ne pouvez pas vous décider pour un en particulier parce que chaque autre semble meilleur, vous pourriez vouloir lire cet article.

Commençons par les bases et clarifions le jargon.

### Qu'est-ce que l'Architecture Orientée Microservices ?

En dehors du fait que le microservice soit un mot à la mode, selon les principes de conception des microservices, il peut être simplement défini comme :

> Un service hautement cohésif, à but unique et décentralisé.

C'est-à-dire un service qui a un et un seul but et qui est autosuffisant.

Tout service qui correspond aux propriétés mentionnées dans la définition peut être qualifié de microservice. Les principes de conception mentionnés sont :

1. _But unique_ : Le service doit être axé sur un et un seul but. Le service doit être axé sur le domaine et l'objectif. Par exemple, un microservice peut être axé uniquement sur un mécanisme de connexion.
2. _Haute cohésion_ : Le service doit être autosuffisant en termes d'exigences de domaine et d'infrastructure de domaine. Le service doit avoir toutes les fonctionnalités dont il a besoin pour servir le but unique. Par exemple, un microservice de connexion peut avoir sa propre base de données.
3. _Décentralisé_ : Le service doit être décentralisé des autres services et de l'infrastructure d'un point de vue logique, de sorte que toute modification requise dans le microservice ne doive pas impliquer de modifications dans un autre microservice. Par exemple, un microservice de connexion doit avoir son propre ensemble de composants d'infrastructure et les modifications requises dans le microservice de connexion ne doivent pas impliquer de modifications dans un autre microservice.

![Image](https://cdn-media-1.freecodecamp.org/images/tqdyaeQCiW1OZR1Sy9ag0SBELh8aj9SPH6p-)

En utilisant le modèle d'architecture de microservices, vous pouvez diviser votre équipe d'application en plusieurs équipes _axées sur le microservice_. Par exemple, un microservice de recherche peut avoir sa propre équipe et un microservice de connexion peut avoir sa propre équipe. Les deux équipes peuvent inclure des personnes ayant une expertise dans les mêmes domaines tels que la base de données, le frontend et le backend, étant donné que les deux microservices peuvent avoir leur propre base de données, frontend et backend.

Les avantages de l'utilisation de l'architecture orientée microservices incluent :

* Les équipes peuvent être organisées autour des fonctionnalités/composants du produit.

Les changements dans une fonctionnalité/composant nécessitent un changement uniquement dans cet ensemble particulier.

* Le pointage et la localisation des bugs sont faciles.
* La symphonie des domaines peut apporter des solutions innovantes.
* La gestion de la fonctionnalité devient facile.
* Plus de ressources sur une fonctionnalité particulière peuvent être ajoutées s'il y a besoin d'ajouter une poussée.

Les inconvénients de l'utilisation de l'architecture orientée microservices incluent :

* Le maillage de microservices peut être un surcoût à gérer.
* Les ressources en termes de développeurs peuvent être coûteuses.
* Les équipes peuvent croître au fur et à mesure que les composants/fonctionnalités de l'application le font.
* La localisation des solutions peut se produire si les connaissances ne sont pas partagées fréquemment entre les équipes.
* La qualité du code est différente selon les microservices.

### Qu'est-ce que l'Architecture Orientée Services ?

> Dans une architecture orientée services, les services sont divisés en fonction de leur rôle dans la couche d'application.

Par exemple, le service de base de données, le service frontend, le service backend, etc., sont des ségrégations logiques des services. Ces services sont utilisés par divers composants de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/3UCYoQ9-Cvgq8-umTYfsCCnScRPrJIfTTwQL)

Les architectures orientées services peuvent être un meilleur choix lorsque l'application n'a pas un très grand écosystème de fonctionnalités/composants diversifiés et que les composants peuvent partager logiquement les services.

En utilisant le modèle d'architecture orientée services, les équipes peuvent être facilement divisées _en fonction de leur expertise de domaine_.

Par exemple, les équipes peuvent être simplement divisées en backend, devops, base de données, mobile, etc. Si un composant nécessite un service, le client (développeur du composant) contactera l'équipe de service et ainsi, toutes les informations principales sur le service restent _localisées_ avec l'équipe de service.

Les avantages de l'utilisation de l'architecture orientée services incluent :

* La qualité du code est cohérente à travers le domaine.
* Le partage des connaissances est facile au sein du domaine.
* Les erreurs ne sont pas répétées puisque l'équipe de domaine est consciente des échecs précédents.
* Plus de ressources peuvent être mises sur le service si nécessaire.

Les inconvénients de l'utilisation de l'architecture orientée services incluent :

* Un bug/une rupture dans un service peut affecter plusieurs services/couches.
* La symphonie des domaines est manquante, ce qui peut entraîner un manque d'innovation.
* Les équipes peuvent finir par travailler sur une seule couche si elles ne sont pas gérées correctement.
* La gestion de plusieurs fonctionnalités est difficile car elle peut impliquer des changements dans plusieurs services.
* Un service peut finir par changer beaucoup.

### Qu'est-ce qui est commun aux deux ?

Les deux modèles de développement diffèrent de manière significative du monolithe traditionnel.

> Mais les deux nécessitent que les équipes et les composants se concentrent sur une seule et unique chose.

Les concepts de ségrégation et de localisation sont au cœur des deux modèles. Les deux modèles sont généralement alignés avec la philosophie DevOps pour assurer une croissance rapide au sein des équipes.

### Conclusion

Puisque le monolithe ne peut pas répondre aux besoins du développement moderne et agile, vous pourriez vouloir aligner vos pratiques de développement ainsi que vos équipes avec l'une des deux approches.

Le microservice est un mot à la mode ces jours-ci, mais cela ne signifie pas que c'est la meilleure solution à vos problèmes.

Si votre application exige une ségrégation des équipes basée sur des domaines d'expertise tels que la base de données, le frontend, le backend, la science des données, etc., alors l'approche orientée services pourrait être la meilleure pour vous.

Si votre application a besoin de nombreuses fonctionnalités plug-in différentes qui nécessitent leurs propres ressources telles que leur propre base de données, frontend, backend, etc., vous pourriez vouloir opter pour une architecture orientée microservices et concentrer les équipes sur des ensembles de fonctionnalités particuliers.

Cependant, vous pouvez également opter pour l'approche hybride. L'approche hybride peut être utile lorsque vous construisez une plateforme avec plusieurs applications.

Par exemple, si vous souhaitez construire un magasin d'applications interne, l'équipe développant la plateforme (équipe du magasin d'applications/plateforme) peut être davantage divisée selon un modèle orienté services ; tandis que les équipes construisant les applications (équipes d'applications) peuvent être concentrées et divisées en microservices.

[Inscrivez-vous à ma newsletter](http://eepurl.com/gcFOaX) pour obtenir un _accès gratuit_ à des conseils en logiciels, des cours, des articles, des digestifs hebdomadaires et des offres exclusives à la liste.