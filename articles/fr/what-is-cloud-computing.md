---
title: Qu'est-ce que le Cloud Computing ? Introduction au Cloud pour les débutants
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2024-01-03T21:40:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-cloud-computing
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/cloud-sky.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
seo_title: Qu'est-ce que le Cloud Computing ? Introduction au Cloud pour les débutants
seo_desc: 'As the digital landscape continues to evolve and technology marches forward,
  cloud computing has remained an important topic for developers to learn.

  You''ve probably encountered cloud requirements in job listings, heard people talk
  about it in conver...'
---

Alors que le paysage numérique continue d'évoluer et que la technologie avance, le cloud computing reste un sujet important pour les développeurs à apprendre.

Vous avez probablement rencontré des exigences en matière de cloud dans les offres d'emploi, entendu des gens en parler dans des conversations, ou vu des publicités de sociétés proposant des services cloud – et maintenant vous êtes intéressé à en apprendre davantage.

Dans cet article, je vais démystifier le cloud pour vous, en décomposant des concepts complexes en morceaux faciles à comprendre.

Voici ce que nous allons couvrir dans cet article :

* [Le monde avant le Cloud Computing](#heading-le-monde-avant-le-cloud-computing)
* [Qu'est-ce que le Cloud Computing ?](#heading-quest-ce-que-le-cloud-computing)
* [Fournisseurs de services Cloud](#heading-fournisseurs-de-services-cloud)
* [Différents services Cloud](#heading-differents-services-cloud)
* [Défis que le Cloud Computing aide à résoudre](#heading-defis-que-le-cloud-computing-aide-a-resoudre)
* [Comment le Cloud Computing peut-il vous aider ?](#heading-comment-le-cloud-computing-peut-il-vous-aider)
* [Modèles de déploiement Cloud](#heading-modeles-de-deploiement-cloud)

Alors, plongeons-nous et apprenons les bases du cloud computing pour que vous puissiez commencer votre voyage dans ce domaine en croissance.

## Le monde avant le Cloud Computing

Pour comprendre le cloud computing, il est important de comprendre le problème que le cloud computing essaie de résoudre. Cela vous aidera à comprendre son histoire et à apprécier la commodité qu'il apporte dans le monde de la technologie.

Avant le cloud, le déploiement de services web était un processus très coûteux. Pour déployer une application web, vous deviez acheter des serveurs avec la bonne quantité de stockage et de mémoire, les garder sur site, configurer ces serveurs et les utiliser pour héberger votre application.

Cela entraîne de nombreux coûts supplémentaires, autres que les coûts initiaux des serveurs, comme l'électricité et les données nécessaires pour maintenir votre serveur en ligne à tout moment. Il y a aussi des préoccupations de sécurité, car vous devrez empêcher votre serveur d'être endommagé ou volé par des acteurs malveillants.

Au-delà de tout cela, de nombreux développeurs ne sont pas exactement des spécialistes des serveurs. Vous devriez donc soit former vos développeurs pour qu'ils deviennent administrateurs système, soit embaucher des administrateurs système pour configurer et configurer les serveurs pour qu'ils fonctionnent avec vos applications. Ensuite, pour déployer une nouvelle application, vous devriez répéter tout le processus avec de nouveaux coûts.

La mise à l'échelle des applications n'était pas facile avant le cloud. Si vous essayiez de gérer les coûts et de ne pas acheter trop de serveurs, ou d'embaucher de nombreux ingénieurs système, vous pourriez vous retrouver avec une puissance de calcul insuffisante et vous devriez mettre à l'échelle. La mise à l'échelle signifie acheter plus de serveurs (ou remplacer les existants par de meilleurs), les configurer pour qu'ils correspondent aux configurations existantes et déployer vos applications sur eux.

Ce sont quelques-uns des problèmes auxquels nous étions confrontés avant le cloud computing. Maintenant, vous vous demandez peut-être, "comment le cloud computing résout-il ces problèmes ?". Découvrons-le.

## Qu'est-ce que le Cloud Computing ?

> **Le cloud computing** est la disponibilité à la demande des ressources du système informatique, en particulier le stockage de données (stockage cloud) et la puissance de calcul, sans gestion active directe par l'utilisateur.
>
> Le cloud computing repose sur le partage des ressources pour atteindre la cohérence et utilise généralement un modèle de paiement à l'usage, ce qui peut aider à réduire les dépenses en capital mais peut également entraîner des dépenses d'exploitation imprévues pour les utilisateurs. – [Wikipedia](https://en.wikipedia.org/wiki/Cloud_computing)

Pensez au Cloud Computing comme à la location d'un ordinateur dans un cybercafé. Dans un cybercafé, ils ont les ordinateurs prêts à l'emploi – vous entrez simplement, payez pour le temps souhaité et utilisez l'ordinateur pendant cette période.

Dans le cas du cloud computing, vous n'avez pas à vous soucier d'acheter l'ordinateur, de le protéger ou de couvrir les coûts de fonctionnement. Le fournisseur de cloud couvre toutes ces préoccupations. Vous n'avez rarement à vous soucier des problèmes logiciels ou de l'absence de logiciels spécifiques sur ces ordinateurs. Et le meilleur ? Vous ne payez que pour l'ordinateur que vous utilisez, et seulement pour le temps que vous l'utilisez.

Donc, en termes plus relatables, disons que vous avez une application web à déployer. Vous allez chez un fournisseur de services cloud, sélectionnez les exigences spécifiques du serveur dont votre application a besoin, sélectionnez les dépendances logicielles et déployez votre application, sans aucun souci.

Le cloud computing expliqué à un enfant de cinq ans est _"laisser quelqu'un d'autre gérer vos besoins informatiques"_. Vous avez un site web que vous devez mettre en ligne, ou peut-être une application mobile, ou une autre pièce de technologie, et au lieu d'avoir à acheter des serveurs pour la déployer, quelqu'un d'autre achète et configure les serveurs. Vous téléchargez simplement vos fichiers. C'est presque la même chose que de louer un appartement, mais maintenant vous louez de l'espace de calcul sur un autre ordinateur.

## Fournisseurs de services Cloud

Les entreprises qui fournissent ces services cloud sont appelées fournisseurs de services cloud. Ces entreprises ont déjà de nombreux serveurs et ingénieurs système. Elles s'occupent de toutes les choses dont vous n'avez pas à vous soucier, comme les coûts des serveurs et les coûts de fonctionnement. Elles fournissent une interface web où vous pouvez accéder à leurs serveurs et les utiliser lorsque vous en avez besoin.

Actuellement, les fournisseurs de services cloud les plus populaires sont Google (Google Cloud Platform), Amazon AWS (Amazon Web Services) et Microsoft (Azure). Ces entreprises offrent des services similaires, mais avec divers modèles de prix, fonctionnalités, etc.

Voici un résumé de ce que chacune d'entre elles offre :

### Google

Ils offrent des services IaaS (Compute Engine), Containers As A Service, CaaS, (Kubernetes Engine), et PaaS (App Engine). Ils offrent également des services de stockage de données, avec des outils comme Google Cloud Storage, Cloud SQL et Cloud Bigtable.

### AWS

Il s'agit du premier fournisseur de services cloud. Ils offrent des services IaaS (Elastic Compute, EC2), CaaS (Elastic Kubernetes Service, EKS) et PaaS (Elastic Beanstalk). Ils offrent également des services de stockage de données, avec des outils comme Amazon S3 et DynamoDb.

### Microsoft

Ils offrent des services IaaS (Virtual Machine), CaaS (Kubernetes Service, AKS) et PaaS (App Service). Ils offrent également des services de stockage de données, avec des outils comme Cosmos DB.

Pour maximiser les ressources, les fournisseurs de services cloud font partager des serveurs à leurs clients. Les clients n'ont pas à connaître ou à se soucier de cette allocation.

Maintenant, comprenons ce que signifient certains des acronymes/termes ci-dessus afin que vous ayez une meilleure idée de ce que sont ces services cloud.

## Différents services Cloud

Les fournisseurs de services cloud offrent de nombreux services informatiques différents. Voici les services les plus courants :

### SaaS (Software As A Service)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/saas-778x445.jpeg)
_[Geek Super](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fgeeksuper.com%2Fadvantages-of-saas-platforms-for-online-courses%2F&amp;psig=AOvVaw0J54lC0WsxXAoS0L2czE27&amp;ust=1652833369985000&amp;source=images&amp;cd=vfe&amp;ved=0CA0QjhxqFwoTCIDvwOio5fcCFQAAAAAdAAAAABAO)_

Ce service consiste simplement à utiliser un logiciel sans aucune connaissance de son code source, de son environnement d'hébergement ou des détails de développement. Vous l'utilisez simplement et faites confiance à ce qu'il est géré et mis à jour correctement.

### PaaS (Platform As A Service)

Ici, vous vous concentrez uniquement sur le développement de votre application, car tout a été géré (le matériel, les environnements informatiques et les logiciels requis).

### IaaS (Infrastructure As A Service)

Il s'agit du service cloud le plus flexible. Ici, vous avez le plus de contrôle sur les choses. Vous pouvez personnaliser et modifier les choses comme vous le souhaitez.

Mais vous ne possédez pas les serveurs. Le fournisseur de services cloud vous fournit uniquement l'infrastructure dont vous avez besoin, et vous êtes responsable de la création de vos propres environnements informatiques et de l'installation des logiciels requis pour que votre application fonctionne.

L'idée ici est similaire à l'achat de matériel. La seule différence est que maintenant, vous le louez et il est virtuel (pour vous).

## Défis que le Cloud Computing aide à résoudre

Le cloud computing élimine le besoin d'acheter et de configurer des serveurs sur site chaque fois qu'une nouvelle application devait être développée. C'est un grand avantage car cela permet aux entreprises d'économiser beaucoup d'argent – à la fois sur les serveurs, ainsi que sur les ingénieurs qui configurerait et configurerait les serveurs pour qu'ils fonctionnent avec vos applications.

La mise à l'échelle n'est généralement pas facile car elle implique souvent beaucoup de configuration et de configuration. Par exemple, pour fournir plus de stockage à une application, vous pourriez obtenir un stockage de données externe et le connecter au serveur actuel. Cela a définitivement ses limites, cependant.

Un moment viendra probablement où vous aurez besoin d'un meilleur serveur, ou d'un serveur supplémentaire. Dans les deux cas, chaque logiciel que vous avez installé pour le faire fonctionner sur l'ancien serveur devrait être réinstallé sur le nouveau serveur. Les fichiers de l'application devraient être déplacés, et ainsi de suite.

De plus, ces applications sous-utilisent souvent ces ressources matérielles. Du point de vue de l'entreprise, c'est une perte. Une solution initiale à cela était la virtualisation. Cela signifiait essentiellement créer des environnements virtuels (contenus) où l'application dispose de tous ses logiciels requis et peut fonctionner correctement sur les serveurs. Cela a conduit à une meilleure utilisation des ressources. Mais ce n'était définitivement pas la solution parfaite.

## Comment le Cloud Computing peut-il vous aider ?

Le cloud computing offre de nombreux avantages, dont certains sont mis en évidence ici :

* Il est moins cher de payer un abonnement que de construire un centre de données entier. Vous avez des plans qui vous permettent d'utiliser uniquement ce que vous utilisez.
* La mise à l'échelle et la gestion sont des responsabilités du fournisseur de services cloud.
* Configuration facile. Les développeurs peuvent se concentrer uniquement sur le code, car toute la configuration réelle du serveur et du matériel peut être effectuée à l'aide d'une interface utilisateur fournie par le fournisseur de services cloud. Cela conduit à un temps de développement plus rapide et les applications sont livrées plus rapidement.
* Accessibilité. Les fournisseurs de services cloud ont tendance à avoir plusieurs centres de données dans le monde, garantissant que vos utilisateurs ont toujours accès à vos services aussi rapidement que possible.
* Sécurité des données. Parce que vos données ne sont plus stockées dans votre espace physique, il est plus difficile pour les acteurs malveillants d'entrer et d'endommager ou de voler vos serveurs.

## Modèles de déploiement Cloud

Un modèle de déploiement cloud détermine où vos données (et applications) sont stockées et comment vos clients interagissent avec elles.

### Cloud public

Ici, tout est géré par le fournisseur de services cloud. C'est le modèle le plus populaire. Lorsque vous utilisez un cloud public, vous ne vous souciez pas de la maintenance des serveurs, et vous êtes sûr de la haute fiabilité et de la possibilité de scalabilité illimitée. Cela signifie généralement que vous partagez des serveurs avec d'autres personnes.

C'est le modèle le moins cher, et les entreprises utilisent généralement un modèle de paiement à l'usage (vous n'avez donc jamais à vous engager trop financièrement à l'avance).

Un problème potentiel avec cela est que, avoir tout géré par le fournisseur de services cloud signifie que vous avez peu ou pas de contrôle sur les services.

### Cloud privé

Cela est similaire aux méthodes traditionnelles d'hébergement d'applications. Ici, vous avez vos propres centres de données. Cela signifie que vous seul utilisez les serveurs et avez un contrôle illimité sur eux.

Maintenant, la différence est que vous fournissez une interface en libre-service aux utilisateurs de vos serveurs, généralement des développeurs dans votre entreprise. Vous devez toujours gérer les serveurs physiques et vous êtes responsable de leur maintenance et de leur mise à l'échelle.

Cette méthode peut être plus sécurisée que le cloud public, car vous avez le contrôle et pouvez configurer autant de sécurité que possible. Elle est également très utile si vous avez des données qui ne doivent pas sortir en raison des exigences de conformité.

Mais cette méthode est beaucoup plus coûteuse, bien que avec un modèle de tarification plus prévisible ou fixe. Ces serveurs et matériels sont chers. Les avoir signifie avoir quelqu'un pour les gérer, ce qui signifie plus de dépenses. La mise à l'échelle signifie également acheter de nouveaux appareils à chaque fois.

### Cloud hybride

![Image](https://www.freecodecamp.org/news/content/images/2022/05/What-is-Hybrid-Cloud.jpeg)
_Cloud Hybride | [W3Codemasters](https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fw3codemasters.in%2Fwhat-is-hybrid-cloud-benefits-of-a-unified-hybrid-cloud-platform%2F&amp;psig=AOvVaw3ekfLv5gwNG2kjXGoFfWA4&amp;ust=1652833178148000&amp;source=images&amp;cd=vfe&amp;ved=0CA0QjhxqFwoTCPj5qKKp5fcCFQAAAAAdAAAAABAI)_

Cette approche fusionne les méthodes publiques et cloud. Elle vous permet essentiellement plus de flexibilité. Vous pouvez utiliser des services publics et également configurer les vôtres lorsque vous en avez besoin. Ici, vous êtes en mesure de vous conformer aux réglementations, via vos serveurs, et également offrir une haute accessibilité, via un fournisseur de services cloud. Cette méthode est parfaite pour les organisations qui tentent de migrer d'un modèle à un autre, en maintenant l'opération commerciale pendant la transition.

Un exemple d'application de cela serait d'héberger une application sur un cloud public et de la connecter à une base de données sur un cloud privé sécurisé.

Cette méthode est également plus chère que le cloud public, car vous devez prendre en charge certains des serveurs. Elle pourrait également devenir compliquée lorsque les données sont distribuées entre plusieurs serveurs et applications.

### Comment choisir un modèle de déploiement

Le choix entre les modèles de déploiement cloud public, privé ou hybride dépend des exigences uniques d'une organisation.

* Les clouds publics offrent une efficacité des coûts et une portée mondiale
* Les clouds privés offrent une sécurité et un contrôle améliorés
* Les clouds hybrides offrent de la flexibilité et un équilibre stratégique entre les deux.

La décision dépend en fin de compte de facteurs tels que les besoins en sécurité, les exigences de conformité, la scalabilité et le niveau de contrôle souhaité sur l'infrastructure informatique.

## **Conclusion**

Maintenant, vous devriez avoir suffisamment d'informations pour lancer votre carrière dans le cloud computing.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me connecter sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !