---
title: Abstractions du Cloud Computing – IaaS, PaaS, FaaS et SaaS expliqués
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-05-16T16:31:36.000Z'
originalURL: https://freecodecamp.org/news/cloud-computing-abstractions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pictures-2.001-2.jpeg
tags:
- name: abstraction
  slug: abstraction
- name: Cloud Computing
  slug: cloud-computing
seo_title: Abstractions du Cloud Computing – IaaS, PaaS, FaaS et SaaS expliqués
seo_desc: 'Abstracting is the process of reducing something to its most basic form.
  It is the hiding away of the inessential.

  For a drawing, this could be reducing it to its basic lines and shapes. Naturally,
  there are many levels of an abstraction, since what ...'
---

L'abstraction est le processus de réduction de quelque chose à sa forme la plus basique. C'est le fait de cacher ce qui n'est pas essentiel.

Pour un dessin, cela pourrait consister à le réduire à ses lignes et formes de base. Naturellement, il existe de nombreux niveaux d'abstraction, car ce qui est non essentiel est subjectif.

Cela est illustré dans l'image ci-dessous montrant un temple grec et deux dessins à différents niveaux d'abstraction.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8cf1dcb-27a4-42fb-babb-b58fb8c659b3_1628x882.png align="left")

*Exemple d'abstraction*

Plus vous abstraiez de détails du temple, plus il vous reste quelque chose de très simple. Sous sa forme la plus basique, un temple grec peut être considéré comme un triangle posé sur un rectangle avec des lignes verticales traversant le rectangle.

Les abstractions sont partout autour de nous. Google Maps en est un bon exemple. Vous pouvez avoir une vue satellite, un plan routier, un terrain, le trafic, le vélo, les transports en commun ou la vue rue, parmi d'autres. Chacune de ces options abstrait certains détails, vous permettant de vous concentrer sur ce que vous voulez voir.

Même une carte satellite est une abstraction, car c'est un instantané à un moment donné et ne peut pas capturer chaque nouvelle maison, arbre ou brin d'herbe.

Le point clé est qu'une abstraction simplifie quelque chose en **cachant les détails sous-jacents**. C'est un moyen de gérer la complexité.

Mais il y a toujours un prix à payer. En échange de la dissimulation de la complexité, vous perdez certains détails de bas niveau, ce qui signifie souvent une perte de contrôle si les choses tournent mal.

# Abstractions dans le Cloud

Dans le cloud computing, les abstractions sont partout. Lorsque vous choisissez une technologie particulière pour résoudre un problème, vous choisissez implicitement un niveau d'abstraction.

Il existe quatre niveaux d'abstraction dans le cloud computing. Ceux-ci sont appelés les modèles de service :

* IaaS (Infrastructure as a Service)

* PaaS (Platform as a Service)

* FaaS (Function as a Service)

* SaaS (Software as a Service).

Ces quatre modèles de service ne sont qu'un guide pour diviser les différents niveaux d'abstraction dans le cloud computing. Vous pouvez les considérer davantage comme des opinions bien réfléchies, plutôt que comme une règle immuable de la physique.

Certaines personnes ne considèrent que l'IaaS, le PaaS et le SaaS comme les modèles de service, ignorant le FaaS. D'autres incluront Container as a Service, Security as a Service, Database as a Service, et ainsi de suite.

Les exemples peuvent se multiplier en ajoutant simplement "as a service" à différentes technologies. Cela a du sens puisque vous pouvez abstraire à différents niveaux, ce qui fait de toute abstraction du cloud un spectre de possibilités.

Tout comme le temple grec montré ci-dessus, il peut y avoir de nombreux niveaux intermédiaires d'abstraction entre un dessin réaliste du temple et un dessin avec un triangle posé sur un rectangle.

Lorsque vous choisissez d'utiliser le cloud computing au lieu d'une solution sur site, vous choisissez effectivement d'abstraire certaines des tâches sous-jacentes et des éléments d'infrastructure que vous devriez autrement gérer.

La figure ci-dessous montre les différences entre une solution sur site et l'IaaS, le PaaS, le FaaS et le SaaS.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f24811c-1b7f-4c93-b696-b42c5d41d576_1224x1080.png align="left")

*Figure illustrant les différences entre une solution sur site et l'IaaS, le PaaS, le FaaS et le SaaS.*

Plus vous vous déplacez vers la droite dans l'illustration ci-dessus, plus vous abstraiez de la pile d'infrastructure sous-jacente. Cela réduit la complexité de ce que vous essayez de construire, car il y a moins de choses à construire et à gérer.

Mais le prix à payer pour cette réduction de complexité est une perte de contrôle. Parfois, c'est un prix digne d'être payé, et parfois non.

## Solutions sur site

Vous êtes responsable de la gestion de tout dans la pile d'infrastructure, de la sécurité physique du centre de données à l'application elle-même.

Dans ce cas, presque rien n'est abstrait. Cela vous donne un contrôle et une flexibilité accrus pour personnaliser ce que vous voulez. En échange, vous payez le prix de la gestion de toute la pile et supportez les risques associés.

Cela est analogue à l'ouverture d'un restaurant de pizza, mais au lieu de simplement louer un espace, vous construisez le restaurant à partir de zéro.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a01e351-835d-4431-8298-de50ef3666d5_1886x1008.png align="left")

*Construire un restaurant de pizza à partir de zéro est comme gérer des solutions sur site*

L'avantage est que vous avez un contrôle total sur l'apparence du restaurant. L'inconvénient est la dépense initiale importante que vous devrez engager pour la plomberie, la ventilation, le câblage électrique, la climatisation, le chauffage, et ainsi de suite.

Vous serez également confronté à des questions comme "Le restaurant est-il assez grand, ou est-il trop grand ?" ou "Comment puis-je m'agrandir ou réduire en fonction de la demande croissante ou décroissante ?". Les coûts initiaux élevés et les niveaux d'incertitude plus élevés sont le prix à payer pour un contrôle total.

## **IaaS (Infrastructure as a Service)**

La sécurité physique, l'infrastructure du centre de données, la mise en réseau, les serveurs et la virtualisation (le processus de création de plusieurs machines virtuelles à partir d'un serveur physique) sont abstraits et gérés par le fournisseur de cloud.

Vous êtes responsable de la gestion du système d'exploitation et de tout ce qui se trouve au-dessus dans la pile d'infrastructure. Vous pouvez toujours personnaliser la machine virtuelle que vous souhaitez, en fonction des choix proposés par le fournisseur de cloud, et vous paierez pour utiliser la machine virtuelle sur une base pay-as-you-go.

Vous n'avez pas à vous soucier de l'achat de plus de serveurs ou des besoins de refroidissement pour vos serveurs. Tout cela est abstrait et géré pour vous.

Les machines virtuelles/instances sont un bon exemple d'IaaS – EC2 d'AWS, Compute Engine de GCP et VMs d'Azure.

L'IaaS est analogue à la simple location d'un espace pour votre restaurant de pizza. Le câblage électrique, la plomberie, le chauffage, etc., sont abstraits car ils sont gérés par le propriétaire du bâtiment.

Vous êtes responsable du paiement du loyer pour utiliser l'espace, de l'embauche de chefs, d'un manager, de serveurs et de nettoyeurs, de l'achat d'équipements et de meubles, du choix de la décoration, de la création d'un menu, du marketing et de l'attraction de clients.

Toujours beaucoup de travail, mais toutes les activités non liées à la fabrication de pizzas sont cachées, vous permettant de vous concentrer sur ce que vous faites de mieux – fabriquer des pizzas.

## **PaaS (Platform as a Service)**

Ici, vous gérez le runtime et tout ce qui se trouve au-dessus. Le runtime est un environnement logiciel qui fournit les ressources et services nécessaires pour qu'une application s'exécute. Les exemples incluent la machine virtuelle Java pour les applications Java, le runtime Python pour les applications Python et Node.js pour les applications JavaScript.

Avec le PaaS, vous avez abstrait toute l'infrastructure physique. Tout ce dont vous devez vous soucier est votre runtime.

De bons exemples de PaaS sont AWS Beanstalk et GCP App Engine. De plus, les services de base de données gérés comme AWS RDS et GCP Cloud SQL relèvent du PaaS.

Le PaaS est analogue à l'ouverture d'un restaurant de pizza en franchise. Lorsque vous ouvrez une franchise, vous bénéficiez d'un espace de restaurant pré-construit, d'équipements, d'une marque et d'un ensemble de processus à suivre. Vous êtes responsable des activités principales de gestion du restaurant, telles que l'embauche du personnel, la gestion des stocks et la création de menus.

Le PaaS fonctionne de manière similaire, fournissant aux développeurs une plateforme pré-construite qui abstrait l'infrastructure sous-jacente, leur permettant de se concentrer sur la construction et le déploiement d'applications.

## **FaaS (Function as a Service)**

Ici, vous gérez les fonctions et l'application tandis que le fournisseur de cloud gère le reste.

Qu'est-ce qu'une fonction exactement et en quoi est-elle différente d'un runtime ? Une fonction est un bloc de code qui effectue une tâche spécifique, tandis qu'un runtime est l'environnement dans lequel ce code est exécuté.

Les fonctions sont généralement déclenchées par des événements tels que des requêtes HTTP, des mises à jour de base de données ou des messages d'une file d'attente. Lorsqu'un événement se produit, la fonction est automatiquement exécutée et le résultat est renvoyé à l'application appelante.

Cela est analogue à l'embauche d'un chef de pizza freelance pour cuisiner pour vous à la demande. Lorsque vous embauchez ce chef freelance, vous ne payez que pour le temps qu'il passe à cuisiner. Le chef commence à être payé en réaction à un événement, c'est-à-dire au moment où une commande arrive, et cesse d'être payé une fois la pizza prête. Le reste du temps, le chef est simplement inactif, attendant la prochaine commande sans vous coûter d'argent.

En ignorant la malhonnêteté corporative et la potentiel illégalité d'une telle pratique, faire quelque chose comme cela vous fera économiser de l'argent puisque vous ne payez que pour la durée de fabrication d'une pizza.

## **SaaS (Software as a Service)**

Ici, vous ne gérez rien, mais vous consommez simplement le service offert. Prime Video, Gmail et Outlook sont de bons exemples de SaaS. Lorsque vous les utilisez, vous ne vous souciez pas de la manière dont l'application fonctionne. Tout cela est abstrait. Vous accédez simplement au logiciel via un navigateur web ou une application mobile et l'utilisez selon vos besoins.

En utilisant l'analogie du restaurant, cela peut être comparé à simplement commander une pizza auprès du restaurant. Le restaurant abstrait toutes les étapes nécessaires pour faire la pizza.

# Exemples d'IaaS, PaaS, FaaS et SaaS

Le tableau ci-dessous montre des exemples d'offres IaaS, PaaS, FaaS et SaaS des principaux fournisseurs de cloud – AWS, GCP et Azure.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6ce9fab-512a-4d23-b7f7-0608e3042ec6_1524x970.png align="left")

# Mettre tout cela ensemble avec un exemple

Si vous construisez un site de commerce électronique comme Amazon.com, vous aurez besoin d'une base de données transactionnelle pour stocker des détails sur les clients comme leurs noms, détails de paiement, adresse, commandes, inventaires, et ainsi de suite. Comment choisir le bon niveau d'abstraction pour votre base de données ?

Vous avez quatre options à choisir pour votre base de données. En commençant par l'option qui abstrait le plus de la pile d'infrastructure :

1. Vous pourriez choisir d'utiliser une option FaaS comme [AWS Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/). Cela démarre automatiquement la base de données lorsqu'elle est utilisée et l'arrête lorsqu'elle n'est pas utilisée, vous permettant d'économiser de l'argent en ne payant que lorsque vous l'utilisez. Cela est idéal pour une base de données peu utilisée avec des charges de travail imprévisibles

2. Vous pourriez choisir une option PaaS comme [AWS RDS](https://aws.amazon.com/rds/). Il s'agit d'une base de données gérée où AWS abstrait et gère les tâches administratives comme la correction du système d'exploitation, la mise à l'échelle, les sauvegardes de la base de données et d'autres tâches administratives qui nécessiteraient autrement un administrateur de base de données (DBA) pour les gérer

3. Vous pourriez choisir une option IaaS en installant un système de gestion de base de données relationnelle (RDBMS) comme MySQL sur une instance EC2. AWS gérera le matériel, mais vous serez responsable de la gestion du système d'exploitation et de l'application de la base de données. Ainsi, les tâches administratives comme la correction du système d'exploitation, la mise à l'échelle, les sauvegardes de la base de données, entre autres, seront de votre responsabilité

4. Vous pouvez choisir une solution sur site. Ici, vous hébergerez vous-même la base de données et gérerez le matériel vous-même, en plus de toutes les tâches administratives de la base de données comme décrit ci-dessus


Quelle est la bonne option à choisir ? Tout d'abord, cela dépend de votre cas d'utilisation et des avantages et compromis avec lesquels vous êtes à l'aise. Cela est banal mais néanmoins vrai.

Cependant, une bonne heuristique qui fonctionnera la plupart du temps pour la plupart des problèmes est de se concentrer sur ce qu'il faut éviter. Vous voulez généralement éviter une solution extrême ou aberrante, sauf si le problème que vous essayez de résoudre est effectivement extrême ou aberrant. Et la plupart des problèmes, par définition, ne peuvent pas être aberrants.

L'option FaaS utilisant Aurora, et la solution sur site ne sont pas idéales, sauf si votre cas d'utilisation demande spécifiquement les fonctionnalités que ces options possèdent.

Aurora serverless n'est pas un service très populaire, donc trouver des modèles pour l'intégration avec d'autres technologies ou obtenir de l'aide pour le dépannage de problèmes techniques peut être plus difficile. De plus, il peut y avoir certains problèmes techniques avec l'utilisation d'une base de données serverless comme Aurora.

Par exemple, la réveiller d'un état inactif en réponse à une requête peut parfois prendre quelques secondes. Et ce délai peut être suffisamment long pour perdre un client sur votre application de commerce électronique.

La solution sur site n'est pas non plus idéale, car une application de commerce électronique aura des fluctuations de demande en raison des vacances, des remises ou d'un produit devenant viral. Les solutions sur site sont mauvaises pour gérer de grandes fluctuations de demande.

Cette simple heuristique de se concentrer sur ce qu'il faut éviter donne deux solutions acceptables – l'option IaaS d'exécuter votre base de données sur une instance EC2 ou l'option PaaS d'utiliser un service de base de données géré comme RDS. L'une ou l'autre de ces solutions est adaptée au cas d'utilisation décrit.

Le point clé à retenir est qu'une abstraction simplifie quelque chose en **cachant les détails sous-jacents**. C'est un moyen de gérer la complexité.

La solution d'abstraction plus élevée consistant à utiliser RDS est la solution la moins complexe, car AWS gère toutes les complexités sous-jacentes de la correction du système d'exploitation, de la mise à l'échelle, des sauvegardes de la base de données et d'autres tâches administratives. Le prix à payer pour cette réduction de complexité est un contrôle moindre de la base de données et une facture AWS plus élevée.

J'espère que cela vous aidera à choisir la solution qui vous convient. Merci d'avoir lu !