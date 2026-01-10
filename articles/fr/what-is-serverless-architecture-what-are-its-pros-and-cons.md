---
title: Qu'est-ce que l'architecture Serverless ? Quels sont ses avantages et inconvénients
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T18:43:27.000Z'
originalURL: https://freecodecamp.org/news/what-is-serverless-architecture-what-are-its-pros-and-cons
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_16x1_xEclXT4MB0FN_xr2g.jpeg
tags:
- name: architecture
  slug: architecture
- name: lambda
  slug: lambda
- name: serverless
  slug: serverless
seo_title: Qu'est-ce que l'architecture Serverless ? Quels sont ses avantages et inconvénients
  ?
seo_desc: 'By Faizan Bashir


  Serverless, the new buzzword in town has been gaining a lot of attention from the
  pros and the rookies in the tech industry. Partly due to the manner in which cloud
  vendors like AWS have hyped the architecture, from conferences to m...'
---

Par Faizan Bashir

![Image](https://cdn-media-1.freecodecamp.org/images/1*16x1_xEclXT4MB0FN_xr2g.jpeg align="left")

Serverless, le nouveau mot à la mode, attire beaucoup l'attention des professionnels et des débutants dans l'industrie technologique. En partie grâce à la manière dont les fournisseurs de cloud comme AWS ont mis en avant cette architecture, des conférences aux meetups en passant par les articles de blog et bien plus encore. Mais le serverless ne se résume pas à du battage médiatique, il promet la possibilité de mises en œuvre commerciales idéales, ce qui semble plutôt agréable à entendre et probablement plus léger pour le budget.

> *"Concentrez-vous sur votre* ***application***, pas sur l'**infrastructure**"*

Cela semble rassurant, sachant que beaucoup de vos heures de jour sont consacrées à la mise en œuvre, la maintenance, le débogage et la surveillance de l'infrastructure. Avec toute cette gestion lourde de l'infrastructure écartée, nous pouvons vraiment nous concentrer sur les objectifs commerciaux que servent nos applications. Beaucoup d'efforts productifs pourraient être canalisés dans la bonne direction, là où ils étaient censés être idéalement. Peut-être que cela semble trop beau pour être vrai, mais c'est ainsi que les choses auraient dû être. Au moins pour ceux d'entre vous qui ne peuvent pas se permettre de passer beaucoup de temps pris dans la toile des intricacies de l'infrastructure complexe moderne.

Mis à part les attentes, le Serverless brise vraiment le terrain sur son chemin pour perturber votre infrastructure serveur. Le Serverless est déjà utilisé en production par des entreprises comme Netflix, Reuters, AOL et Telenor. L'adoption à l'échelle de l'industrie est en constante augmentation. Le Serverless est prêt à prendre sa propre place, mais ne vous attendez pas à ce que le Serverless conquière votre infrastructure complètement. Il y aura des cas d'utilisation où le serverless pourrait s'avérer être le mauvais choix.

---

### Alors, qu'est-ce que le Serverless ?

Le Serverless est un modèle d'exécution de cloud computing où le fournisseur de cloud gère dynamiquement l'allocation et la provision des serveurs. Une application serverless s'exécute dans des conteneurs de calcul sans état qui sont déclenchés par des événements, éphémères (peuvent durer pour une seule invocation) et entièrement gérés par le fournisseur de cloud. La tarification est basée sur le nombre d'exécutions plutôt que sur une capacité de calcul pré-achetée, n'est-ce pas le cadre idéal pour ce projet que vous planifiez depuis longtemps ? Eh bien, allez-y, faites-le.

> *Les applications serverless sont des systèmes basés sur le cloud et pilotés par événements où le développement d'applications repose uniquement sur une combinaison de* ***services tiers, de logique côté client*** *et d'appels de procédure à distance hébergés dans le cloud (**Functions as a Service**).*

La plupart des fournisseurs de cloud ont investi massivement dans le serverless, et c'est beaucoup d'argent ; avec la promotion massive et l'offre réaliste donnée, vous pouvez supposer en toute sécurité que le serverless sera l'un des services cloud les plus utilisés dans les années à venir. Voici quelques-uns des services cloud actuellement disponibles :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t4O4UXpdG68MQboNKC6bBw.jpeg align="left")

*Source :* [*https://www.slideshare.net/loige/building-a-serverless-company-with-nodejs-react-and-the-serverless-framework-jsday-2017-verona*](https://www.slideshare.net/loige/building-a-serverless-company-with-nodejs-react-and-the-serverless-framework-jsday-2017-verona)

* [**AWS Lambda**](https://aws.amazon.com/lambda/)

* [**Google Cloud Functions**](https://cloud.google.com/functions/)

* [**Azure Functions**](https://azure.microsoft.com/en-us/services/functions/)

* [**IBM OpenWhisk**](https://www.ibm.com/cloud-computing/bluemix/openwhisk)

* [**Alibaba Function Compute**](https://www.alibabacloud.com/product/function-compute)

* [**Iron Functions**](http://open.iron.io/)

* [**Auth0 Webtask**](https://webtask.io/)

* [**Oracle Fn Project**](https://fnproject.io/)

* [**Kubeless**](https://kubeless.io/)

---

### Architecture Traditionnelle vs. Serverless

![Image](https://cdn-media-1.freecodecamp.org/images/1*x_v5NRC3TTMt1MaYl1gMUg.jpeg align="left")

*Source :* [*https://www.gocd.org/2017/06/26/serverless-architecture-continuous-delivery/*](https://www.gocd.org/2017/06/26/serverless-architecture-continuous-delivery/)

Pendant des années, vos applications ont fonctionné sur des serveurs que vous deviez corriger, mettre à jour et surveiller en continu, tard le soir et tôt le matin, en raison de toutes les erreurs inimaginables qui ont rompu votre production. Tant que vous les gériez, toute la responsabilité de leur bon fonctionnement vous incombait. Le Serverless tend à être différent de ce qui précède, vous n'avez plus besoin de vous soucier des serveurs sous-jacents. La raison en est qu'ils ne sont plus gérés par vous et, avec la gestion hors de l'équation, la responsabilité incombe aux fournisseurs de cloud. Mais malgré les fonctionnalités cool du Serverless dans certains cas, l'architecture traditionnelle le surpasse.

#### Tarification

L'un des principaux avantages de l'utilisation du Serverless est la réduction des coûts, pendant des années, le coût de la provision des serveurs et de la maintenance de cette équipe de serveurs 24x7 qui a creusé un trou dans votre poche a disparu. Le modèle de coût du Serverless est basé sur l'exécution : vous êtes facturé pour le nombre d'exécutions. Vous disposez d'un certain nombre de secondes d'utilisation qui varie en fonction de la quantité de mémoire dont vous avez besoin. De même, le prix par MS (milliseconde) varie en fonction de la quantité de mémoire dont vous avez besoin. Évidemment, les fonctions de durée plus courte sont plus adaptables à ce modèle avec un temps d'exécution maximal de 300 secondes à 15 minutes pour la plupart des fournisseurs de cloud.

*Le gagnant ici est l'architecture Serverless.*

#### Réseautage

L'inconvénient est que les fonctions Serverless ne sont accessibles que sous forme d'API privées. Pour y accéder, vous devez configurer une passerelle API. Cela n'a pas d'impact sur votre tarification ou votre processus, mais cela signifie que vous ne pouvez pas y accéder directement via l'IP habituelle, dommage !

*Le gagnant ici est l'architecture traditionnelle.*

#### Dépendances tierces

La plupart, sinon la totalité, de vos projets ont des dépendances externes, ils reposent sur des bibliothèques qui ne sont pas intégrées dans le langage ou le framework que vous utilisez. Vous utilisez souvent des bibliothèques avec des fonctionnalités qui incluent la cryptographie, le traitement d'images, etc., ces bibliothèques peuvent être assez lourdes. Sans accès au niveau du système, vous devez empaqueter ces dépendances dans l'application elle-même.

> *Réinventer la roue n'est pas toujours une bonne idée.*

*Le gagnant ici dépend du contexte. Pour les applications simples avec peu de dépendances, le Serverless est le gagnant ; pour tout ce qui est plus complexe, l'architecture traditionnelle est la gagnante.*

#### Environnements

La configuration de différents environnements pour le Serverless est aussi simple que la configuration d'un seul environnement. Étant donné qu'il s'agit d'un paiement par exécution, c'est une grande amélioration par rapport aux serveurs traditionnels, vous n'avez plus besoin de configurer des machines de développement, de préproduction et de production. Finalement, vous perdriez le compte de tous les environnements, à un moment donné.

*Le gagnant ici est l'architecture Serverless.*

#### Délai d'exécution

Avec le calcul Serverless, il y a une [limite de délai d'exécution de 15 minutes pour AWS Lambda](https://aws.amazon.com/about-aws/whats-new/2018/10/aws-lambda-supports-functions-that-can-run-up-to-15-minutes/). Les fonctions trop complexes ou de longue durée ne sont pas adaptées au Serverless, mais avoir un délai d'exécution strict rend impossible l'exécution de certaines tâches. Une limite stricte sur ce temps rend le Serverless inutilisable pour les applications qui ont des temps d'exécution variables, et pour certains services qui nécessitent des informations provenant d'une source externe. Cela est susceptible de changer dans le futur.

*Le gagnant clair ici est l'architecture traditionnelle.*

#### Évolutivité

Le processus de mise à l'échelle pour le Serverless est automatique et transparent, mais il y a un manque de contrôle ou une absence totale de contrôle. Bien que la mise à l'échelle automatique soit formidable, il est difficile de ne pas pouvoir traiter et atténuer les erreurs liées aux nouvelles instances Serverless.

*C'est un match nul entre le Serverless et l'architecture traditionnelle.*

---

### Fonctions en tant que Service (FaaS)

FaaS est une implémentation des architectures Serverless où les ingénieurs peuvent déployer une fonction individuelle ou un morceau de logique métier. Elles démarrent en quelques millisecondes (~100 ms pour AWS Lambda) et traitent des requêtes individuelles dans un délai de 300 secondes à 15 minutes imposé par la plupart des fournisseurs de cloud.

#### **Principes du FaaS :**

* Gestion complète des serveurs

* Facturation basée sur l'invocation

* Évolutivité instantanée et pilotée par événements

### Propriétés clés du FaaS :

#### Fonctions logiques indépendantes, côté serveur

Les FaaS sont similaires aux fonctions que vous êtes habitué à écrire dans les langages de programmation, de petites unités séparées de logique qui prennent des arguments d'entrée, opèrent sur l'entrée et retournent le résultat.

#### Sans état

Avec le Serverless, tout est sans état, vous ne pouvez pas sauvegarder un fichier sur le disque lors d'une exécution de votre fonction et vous attendre à ce qu'il soit là à la suivante. Deux invocations de la même fonction pourraient s'exécuter sur des conteneurs complètement différents sous le capot.

#### Éphémère

Les FaaS sont conçues pour démarrer rapidement, faire leur travail et puis s'arrêter à nouveau. Elles ne restent pas inutilisées. Tant que la tâche est effectuée, les conteneurs sous-jacents sont supprimés.

#### Déclenchées par des événements

Bien que les fonctions puissent être invoquées directement, elles sont généralement déclenchées par des événements provenant d'autres services cloud tels que des requêtes HTTP, de nouvelles entrées de base de données ou des notifications de messages entrants. Les FaaS sont souvent utilisées et considérées comme le lien entre les services dans un environnement cloud.

#### Évolutives par défaut

Avec des fonctions sans état, plusieurs conteneurs peuvent être initialisés, permettant d'exécuter autant de fonctions (en parallèle, si nécessaire) que nécessaire pour continuer à servir toutes les requêtes entrantes.

#### Entièrement gérées par un fournisseur de cloud

AWS Lambda, Azure Functions, IBM OpenWhisk et Google Cloud Functions sont les solutions FaaS les plus connues disponibles. Chaque offre prend généralement en charge une gamme de langages et d'environnements d'exécution, par exemple Node.js, Python, .NET Core, Java.

---

### L'application Serverless

Une solution Serverless se compose d'un serveur web, de fonctions Lambda (FaaS), d'un service de jetons de sécurité (STS), d'une authentification utilisateur et d'une base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TIrjN7EjLUVJmJ6YvHR7Dg.png align="left")

*Source :* [*http://blog.tonyfendall.com/2015/12/serverless-architectures-using-aws-lambda/*](http://blog.tonyfendall.com/2015/12/serverless-architectures-using-aws-lambda/)

* **Application Client** — L'interface utilisateur de votre application est rendue côté client dans une application JavaScript Frontend Moderne, ce qui nous permet d'utiliser un serveur web simple et statique.

* **Serveur Web** — Amazon S3 fournit un serveur web robuste et simple. Tous les fichiers HTML, CSS et JS statiques de notre application peuvent être servis depuis S3.

* **Fonctions Lambda (FaaS)** — Elles sont les éléments clés de l'architecture Serverless. Quelques exemples populaires de FaaS sont AWS Lambda, Google Cloud Functions et Microsoft Azure Functions. AWS Lambda est utilisé dans ce framework. Les services d'application pour la connexion et l'accès aux données seront construits en tant que fonctions Lambda. Ces fonctions liront et écriront dans votre base de données et fourniront des réponses JSON.

* **Service de Jetons de Sécurité (STS)** — génère des identifiants AWS temporaires (clé API et clé secrète) pour les utilisateurs de l'application. Ces identifiants temporaires sont utilisés par l'application cliente pour invoquer l'API AWS (et ainsi invoquer Lambda).

* **Authentification Utilisateur** — AWS Cognito est un service d'identité intégré à AWS Lambda. Avec Amazon Cognito, vous pouvez facilement ajouter l'inscription et la connexion des utilisateurs à vos applications mobiles et web. Il offre également la possibilité d'authentifier les utilisateurs via des fournisseurs d'identité sociaux tels que Facebook, Twitter ou Amazon, avec des solutions d'identité SAML, ou en utilisant votre propre système d'identité.

* **Base de Données** — AWS DynamoDB fournit une base de données NoSQL entièrement gérée. DynamoDB n'est pas essentiel pour une application serverless mais est utilisé ici comme exemple.

---

### Avantages de l'Architecture Serverless

#### **Du point de vue commercial**

1. Le coût engendré par une application serverless est basé sur le nombre d'exécutions de fonctions, mesuré en millisecondes au lieu d'heures.

2. Agilité du processus : des unités déployables plus petites entraînent une livraison plus rapide des fonctionnalités sur le marché, augmentant la capacité à s'adapter au changement.

3. Le coût d'embauche d'ingénieurs en infrastructure backend diminue.

4. Réduction des coûts opérationnels

#### **Du point de vue du développeur**

1. Responsabilité réduite, pas d'infrastructure backend à gérer.

2. Administration système nulle.

3. Gestion opérationnelle plus facile.

4. Favorise l'adoption des Nanoservices, Microservices, principes SOA.

5. Configuration plus rapide.

6. Évolutivité, pas besoin de se soucier du nombre de requêtes simultanées.

7. Surveillance intégrée.

8. Favorise l'innovation.

#### **Du point de vue de l'utilisateur**

1. Si les entreprises utilisent cet avantage concurrentiel pour livrer des fonctionnalités plus rapidement, alors les clients reçoivent de nouvelles fonctionnalités plus rapidement qu'avant.

2. Il est possible que les utilisateurs puissent plus facilement fournir leur propre stockage backend (par exemple, Dropbox, Google Drive).

3. Il est plus probable que ces types d'applications puissent offrir une mise en cache côté client, ce qui fournit une meilleure expérience hors ligne.

---

### Inconvénients de l'Architecture Serverless

#### **Du point de vue commercial**

1. Contrôle global réduit.

2. Le verrouillage par le fournisseur nécessite plus de confiance pour un fournisseur tiers.

3. Une exposition supplémentaire au risque nécessite plus de confiance pour un fournisseur tiers.

4. Risque de sécurité.

5. Risque de récupération après sinistre

6. Coût imprévisible car le nombre d'exécutions n'est pas prédéfini

7. Tous ces inconvénients peuvent être atténués avec des alternatives open-source, mais au détriment des avantages de coût mentionnés précédemment

#### **Du point de vue du développeur**

1. Technologie immature entraînant une fragmentation des composants, des meilleures pratiques peu claires.

2. Complexité architecturale.

3. La discipline requise contre la prolifération des fonctions.

4. Le multi-tenancy signifie qu'il est techniquement possible que les fonctions voisines puissent accaparer les ressources système en arrière-plan.

5. Les tests locaux deviennent délicats.

6. Restrictions significatives sur l'état local.

7. La durée d'exécution est limitée.

8. Manque d'outils opérationnels

#### **Du point de vue de l'utilisateur**

1. À moins d'être correctement architecturée, une application pourrait offrir une mauvaise expérience utilisateur en raison d'une latence accrue des requêtes.

---

### Frameworks Serverless

*Source : https://serverless.com*

Les plateformes serverless nécessitent des infrastructures où elles peuvent être exécutées, les frameworks agnostiques des fournisseurs offrent un moyen agnostique de définir et de déployer du code serverless sur diverses plateformes cloud ou services commerciaux.

* [Serverless Framework](https://serverless.com/) (Javascript, Python, Golang)

* [Apex](http://apex.run/) (Javascript)

* [ClaudiaJS](https://claudiajs.com/) (Javascript)

* [Sparta](https://gosparta.io/) (Golang)

* [Gordon](https://github.com/jorgebastida/gordon) (Javascript)

* [Zappa](https://www.zappa.io/) (Python)

* [Up](https://github.com/apex/up) (Javascript, Python, Golang, Crystal)

---

### Résumé

L'architecture serverless est certainement très excitante, mais elle vient avec un ensemble de limitations. La validité et le succès des architectures dépendent des exigences commerciales et en aucun cas uniquement de la technologie. De la même manière, le serverless peut briller lorsqu'il est utilisé au bon endroit.

Jetez un coup d'œil à la formidable architecture serverless, il est temps de voir à quoi ressemble le serverless de l'intérieur. Voici quelques liens pour commencer votre voyage serverless.

[**serverless/examples**](https://github.com/serverless/examples)
[\_Serverless Examples - A collection of boilerplates and examples of serverless architectures built with the Serverless
…\_github.com](https://github.com/serverless/examples)

[**anaibol/awesome-serverless**](https://github.com/anaibol/awesome-serverless)
[\_awesome-serverless - :cloud: A curated list of awesome services, solutions and resources for serverless / nobackend
…\_github.com](https://github.com/anaibol/awesome-serverless)

[**Building Serverless Contact Form For Static Websites**](https://hackernoon.com/building-serverless-contact-form-for-static-websites-b0e622d5a035)
[\_Handling static forms with AWS serverless lambda functions\_hackernoon.com](https://hackernoon.com/building-serverless-contact-form-for-static-websites-b0e622d5a035)

J'espère que cet article a aidé à comprendre le calcul serverless. J'adorerais entendre comment vous utilisez le serverless dans vos projets. Partagez les connaissances, aidez-les à atteindre plus de personnes.