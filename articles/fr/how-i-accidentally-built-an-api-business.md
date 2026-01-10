---
title: Comment j'ai accidentellement construit une entreprise d'API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-09T22:02:15.000Z'
originalURL: https://freecodecamp.org/news/how-i-accidentally-built-an-api-business
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/3c36ff70b8ab4d25aa85bfa567007087.png
tags:
- name: api
  slug: api
- name: Entrepreneurship
  slug: entrepreneurship
- name: SaaS
  slug: saas
seo_title: Comment j'ai accidentellement construit une entreprise d'API
seo_desc: 'By Wenbin Fang

  In this article, I’ll share my journey of building an API business, the technology
  behind it, and how to build your own API business in the future.

  First, a little bit about the business I''ve built: Listen Notes is a podcast search
  eng...'
---

Par Wenbin Fang

Dans cet article, je vais partager mon parcours de construction d'une entreprise d'API, la technologie derrière celle-ci, et comment construire votre propre entreprise d'API à l'avenir.

Tout d'abord, un peu plus sur l'entreprise que j'ai construite : [Listen Notes](https://www.listennotes.com/) est un moteur de recherche de podcasts qui permet aux gens de rechercher [près de deux millions de podcasts et plus de 89 millions d'épisodes](https://www.listennotes.com/podcast-stats/) par personne ou par sujet. Nous fournissons également une [API de podcast](https://www.listennotes.com/api/) pour les développeurs, appelée Listen API. Elle est devenue une partie centrale de notre entreprise.

## **Une entreprise d'API accidentelle**

J'ai quitté ma précédente startup ratée en septembre 2017. Après quelques jours de bricolage, j'ai repris l'un de mes projets secondaires naissants pour polir un peu l'UI.

Ce projet secondaire était [Listen Notes](https://www.listennotes.com/), un site web de moteur de recherche de podcasts, qui n'était qu'une application React JS sur une seule page fonctionnant sur trois droplets DigitalOcean à 10 $/mois.

Je ne savais pas il y a quelques années que mon petit projet secondaire négligé se transformerait en l'entreprise utile qu'il est devenu.

![Image](https://production.listennotes.com/web/image/37454d6afb7b458ca58ae4e5873ddbbd.png)
_Une version précoce de Listen Notes_

J'ai continué à travailler sur Listen Notes à temps plein et j'ai incorporé Listen Notes en tant que Delaware C-Corp en octobre 2017. L'un de mes objectifs était de vivre autant de facettes de l'entreprise que possible, plutôt que de simplement écrire du code en coulisses.

Mon plan initial était le suivant : (Ne riez pas de moi !)

* Construire un site web de moteur de recherche de podcasts et gagner un peu d'argent grâce à la publicité, tout comme Google. Simple !
* Si ce projet Listen Notes ne fonctionne pas en deux ou trois mois, alors je serai à court d'argent, et je devrai m'endetter sur ma carte de crédit pour continuer pendant un mois de plus ou moins. Si cela ne fonctionne toujours pas, alors je devrai trouver un emploi à temps plein. Bien que les parents de Jeff Bezos aient investi 300 000 $ dans le jeune Amazon et que les parents de Mark Zuckerberg aient prêté 100 000 $ au jeune Facebook, toutes les familles ne peuvent pas se permettre de lancer des dizaines de milliers de dollars dans des projets web.

Puis quelque chose s'est produit.

Le 20 novembre 2017, j'ai reçu un email d'un développeur d'une nouvelle application de podcast, qui m'a demandé si Listen Notes fournissait une API. Il voulait pouvoir rechercher des épisodes dans son application, mais il ne voulait pas construire tout le backend.

J'ai posé quelques questions (par exemple, à quoi ressembleraient les endpoints, quels champs de données avait-il besoin, combien était-il prêt à payer...). J'ai obtenu ses réponses. Tout était dans un fil de discussion par email en quelques jours.

Le 30 novembre 2017, j'ai rapidement implémenté trois endpoints (_GET /search, GET /podcasts/{id}, et GET /episodes/{id}_), qui étaient essentiellement trois [vues Django](https://docs.djangoproject.com/en/3.1/topics/http/views/).

J'ai googlé "API gateway" ou quelque chose comme ça et j'ai trouvé un service appelé [Mashape](https://konghq.com/blog/mashape-has-a-new-homepage/), qui était un marché d'API qui gérait les paiements, la gestion des utilisateurs et la documentation de l'API.

J'ai donc mis mes trois endpoints sur Mashape et j'ai créé deux plans là-bas : GRATUIT et PRO. J'ai envoyé un email au développeur pour lui dire que l'API était prête à être utilisée.

![Image](https://production.listennotes.com/web/image/125d913b8ad14bbd99fbc7c1cfe49e04.png)
_Le fil de discussion par email qui m'a incité à construire Listen API_

Puis rien ne s'est passé. Le développeur de l'application de podcast n'a pas utilisé notre API et a plutôt abandonné son projet.

Finalement, je me suis concentré principalement sur le développement de listennotes.com. L'API était essentiellement en mode autonome sur le web ouvert. Toute personne qui découvrait notre API pouvait s'inscrire, sans parler à aucun être humain.

Le 14 janvier 2018, j'ai eu mon premier utilisateur payant. Quelques autres utilisateurs payants sont arrivés la même année.

![Image](https://production.listennotes.com/web/image/1cf8ad68f0c345318c9c64b3f370764b.png)
_La notification par email que j'ai reçue pour mon premier utilisateur payant_

Attendez, qu'est-ce que RapidAPI ? Eh bien, Mashape a été acquis par une startup nommée RapidAPI. Ils n'ont pas rebaptisé Mashape en RapidAPI complètement avant le milieu de 2018. Les startups ne font généralement pas les choses de manière propre et méthodique, ce qui est tout à fait compréhensible.

Puis quelque chose s'est produit.

Il y a eu une panne du côté de RapidAPI le 29 novembre 2018.

![Image](https://production.listennotes.com/web/image/4d1a713f41dd465b9e57fa4e34be4208.png)
_L'email que j'ai envoyé aux gens de RapidAPI lorsque la panne s'est produite_

RapidAPI avait effectué une grande mise à niveau du backend à cette époque. En tant qu'ingénieur, je comprends tout à fait que les pannes arrivent, surtout lors de changements majeurs dans le backend. Mais je me sentais impuissant parce que leur support client ne répondait pas à mon email. L'appel téléphonique n'a pas fonctionné, comme prévu.

Habituellement, leur support client était très réactif. Peut-être était-ce la saison des vacances et les gens étaient en vacances.

J'ai donc utilisé hunter.io pour trouver les emails professionnels des employés individuels de RapidAPI, du PDG ainsi que du CTO. Le problème a finalement été résolu, de nombreuses heures plus tard. En d'autres termes, notre API était complètement inutilisable pendant ces heures d'indisponibilité. Je me sentais très désolé pour nos utilisateurs payants.

Puis, vers la mi-février 2019, RapidAPI a eu des problèmes de facturation et n'a pas pu nous payer quelques milliers de dollars. Nos utilisateurs payants payaient d'abord RapidAPI. RapidAPI prenait une commission de 20 %. Ensuite, ils nous payaient les 80 % restants (moins les frais PayPal).

Après plusieurs échanges d'emails et d'appels téléphoniques, nous avons finalement obtenu notre paiement. C'est compréhensible. Encore une fois, les startups font des erreurs.

Fin février 2019, j'ai décidé de construire notre propre remplacement de RapidAPI, pour plusieurs raisons :

* Nos revenus d'API sont devenus non négligeables. La commission de 20 % de RapidAPI était un peu trop élevée pour nous.
* Nous voulions que les requêtes API atteignent directement nos propres serveurs, réduisant ainsi la latence pour nos utilisateurs.
* Je ne voulais pas me sentir impuissant lorsque RapidAPI avait des pannes. Globalement, ils faisaient du bon travail en gérant le service. Mais je voulais contrôler mon propre destin.
* Je voulais contacter mes utilisateurs d'API directement. En utilisant RapidAPI, les fournisseurs d'API comme moi n'avions pas accès aux adresses email de nos utilisateurs. C'est compréhensible. C'est comme les entreprises "Uber pour X" qui ne veulent pas que les travailleurs et les clients les contournent et fassent des affaires sous la table. Les places de marché ne veulent pas que les utilisateurs sautent les frais de commission de l'intermédiaire.

De plus, j'ai juré de faire deux choses vraiment bien pour notre nouveau système d'API :

* Nous devons fournir un excellent service client à nos utilisateurs payants.
* Nous offrirons aux clients un service backend très stable et fiable.

Après 30 jours de travail acharné, [nous avons lancé Listen API v2](https://www.listennotes.com/blog/listen-api-v2-simple-pricing-same-endpoints-39/) le 27 mars 2019. L'API héritée hébergée sur RapidAPI est devenue Listen API v1, une version à laquelle nous n'ajouterons pas de nouvelles fonctionnalités mais que nous ne voulons pas fermer car certaines applications l'utilisent encore en décembre 2020 !

Nous continuons à améliorer notre nouvelle Listen API v2 en ajoutant de nouveaux endpoints, de nouveaux champs de données, en améliorant l'efficacité opérationnelle, ainsi qu'en améliorant le tableau de bord utilisateur et nos outils internes.

Les choses accélèrent progressivement. Je suis heureux depuis lors.

Donc, voici le parcours de Listen API jusqu'à présent.

_Note : Bien que nous ayons décidé de passer à autre chose que RapidAPI, je pense toujours que c'est un excellent service. Les startups font toutes des erreurs au début. Elles corrigent les choses et continuent à améliorer leur service, ce qui est génial !_

## **La technologie derrière Listen API**

Les développeurs peuvent utiliser notre API pour rechercher des podcasts et récupérer des métadonnées détaillées sur les épisodes de podcasts. Pour que tout cela fonctionne, nous devons nous assurer que quelques composants principaux sont en place.

![Image](https://production.listennotes.com/academy/image/3c36ff70b8ab4d25aa85bfa567007087.png)
_Les principaux composants de Listen API et les technologies utilisées_

### **Datastore et moteur de recherche**

Il s'agit d'un composant partagé avec notre site web. Par conséquent, je n'ai pas eu besoin de changer quoi que ce soit dans le datastore et le moteur de recherche lors de la construction de notre infrastructure API.

Nous utilisons Postgres comme notre principal stockage de données (par exemple, pour les métadonnées de podcasts, les comptes utilisateurs, etc.), et Elasticsearch comme moteur de recherche.

J'ai écrit un ancien article de blog avec les [détails de l'ensemble de la stack technique](https://www.listennotes.com/blog/the-boring-technology-behind-a-one-person-23/).

### **Outils et processus internes**

Si vous avez travaillé dans des entreprises web, vous savez probablement de quoi je parle ici.

Il est rare qu'une entreprise Internet soit 100 % automatique. Une entreprise doit toujours construire des tonnes d'outils internes et mettre en place des processus manuels pour maintenir le service fonctionnel. C'est pourquoi des entreprises comme [Retool ont une valorisation si élevée](https://www.bloomberg.com/news/articles/2020-10-20/retool-nears-1-billion-valuation-with-funding-from-sequoia) de nos jours.

Les entreprises investissent beaucoup d'argent dans des outils internes invisibles pour les utilisateurs finaux :

![Image](https://production.listennotes.com/web/image/e448df5503934491b251a2a85b815686.png)
_Pourcentage du temps de l'équipe passé sur les outils internes. Crédits : [Retool](https://retool.com/blog/state-of-internal-tools-2020/)_

Pour démarrer notre entreprise d'API, nous devions construire (au moins) deux types d'outils internes :

* **Pour les opérations de données** : Nous avions besoin de la capacité de maintenir les métadonnées des podcasts à jour, de corriger les métadonnées corrompues, ainsi que de passer en revue et d'approuver les modifications apportées par les utilisateurs.
  De plus, nous avions besoin d'un cadre qui gère les nouveaux cas rares de données de podcast corrompues au fur et à mesure. Dans une certaine mesure, construire un produit logiciel signifie gérer des tonnes de cas particuliers pendant une très longue période (comme des années), plutôt que de lancer de nouvelles fonctionnalités chaque jour.
* **Pour les opérations utilisateurs** : Nous avions besoin de la capacité de suspendre le compte d'un mauvais utilisateur, ainsi que de rechercher immédiatement toutes les informations liées à un utilisateur spécifique qui nous a contactés pour un problème particulier.
  De plus, nous devions pouvoir évaluer rapidement si "c'est de notre faute" (erreurs côté serveur) ou "c'est de leur faute" (erreurs côté client) lorsque les utilisateurs se plaignaient.

Les outils internes sont utilisés par les employés de l'entreprise. Certains de ces outils sont entièrement automatisés, comme les tâches cron qui effectuent des tâches planifiées. Mais de nombreux outils doivent être utilisés manuellement par des employés humains, par exemple lors de la saisie du numéro d'identification d'un utilisateur et du clic sur un bouton.

La plupart de nos outils internes ont des interfaces web laides, avec un style [Bootstrap](https://getbootstrap.com/) par défaut :)

![Image](https://production.listennotes.com/web/image/f5c69dcc39a041bdbb230bcc25b3a36c.png)
_Une partie de l'interface utilisateur de notre outil interne qui nous permet de suspendre le compte d'un utilisateur de l'API._

Heureusement, notre API partage de nombreux outils internes avec le site web. Nous n'avons donc pas eu besoin de construire trop de nouvelles choses ici.

### **Le système d'analyse et de facturation**

Le modèle de tarification d'une API est généralement basé sur l'utilisation. Consultez quelques exemples concrets :

* [https://www.twilio.com/pricing](https://www.twilio.com/pricing)
* [https://sendgrid.com/pricing/](https://sendgrid.com/pricing/)
* [https://cloud.google.com/maps-platform/pricing/](https://cloud.google.com/maps-platform/pricing/)
* [https://www.microsoft.com/en-us/bing/apis/pricing](https://www.microsoft.com/en-us/bing/apis/pricing)

Il est essentiel de suivre en temps réel le nombre de requêtes qu'un utilisateur utilise. Nous utilisons Redis pour suivre ces statistiques et les sauvegardons périodiquement dans Postgres pour un stockage persistant.

Que se passe-t-il si notre Redis tombe en panne ? Nous pourrions perdre temporairement certaines statistiques de suivi. Dans ce cas, nous avons un outil interne pour synchroniser les statistiques à partir des logs bruts de Nginx.

Nous devons changer les plans de facturation sans affecter les utilisateurs existants. Par exemple, si nous augmentons les prix, les utilisateurs existants doivent toujours profiter des avantages des anciens plans. Si ce n'est pas fait correctement, il est facile d'avoir des états incohérents et des utilisateurs mécontents facturés avec le mauvais plan de facturation !

Les échecs de paiement, un phénomène très courant, doivent être gérés avec élégance. Nous ne pouvons pas simplement suspendre les utilisateurs immédiatement. Nous devons être en mesure de nous notifier que "cet utilisateur n'a pas pu payer" et de notifier l'utilisateur que "vous n'avez pas pu payer".

Après quelques tentatives, nous suspendons les utilisateurs manuellement — eh bien, nous aurions pu automatiser cette dernière étape. Mais nous ne suspendons pas souvent les utilisateurs de nos jours, donc il est acceptable de le faire manuellement. Il n'est pas nécessaire de tout rendre parfait (du moins pour l'instant).

Nous avons un tableau de bord (vue de Dieu) pour voir combien de requêtes chaque utilisateur utilise dans le cycle de facturation actuel. Et nous sommes en mesure de consulter les logs bruts pour chaque utilisateur à partir d'une interface web, sans avoir à extraire manuellement les fichiers de logs depuis S3.

Stripe et PayPal (via Braintree) sont nos processeurs de paiement. La plupart de nos utilisateurs internationaux utilisent PayPal.

Enfin, en mettant tous ces facteurs ensemble, nous pouvons calculer le montant réel d'argent qu'un utilisateur doit nous payer en temps réel, en fonction de son utilisation. Nous exécutons des tâches asynchrones via [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) pour facturer les factures dues.

Que se passe-t-il si un utilisateur se désabonne en milieu de cycle de facturation ? Nous leur facturons des tarifs au prorata, basés sur le temps et l'utilisation. Les utilisateurs n'ont pas besoin de payer les frais d'un mois complet dans ces cas.

### **Serveurs API**

Nous exécutons des applications Django pour servir les requêtes API. Chaque endpoint est une vue Django simple. Un middleware Django vérifie si une requête est légitime, puis génère un log ou rejette la requête immédiatement.

Nous mettons en cache les données de réponse par clé API + URL unique dans Redis. En général, [les performances de notre API sont assez bonnes](https://www.listennotesstatus.com/).

Nous utilisons Nginx comme équilibreur de charge et provisionnons plusieurs serveurs API. Il est simple de faire un déploiement progressif ici, avec une série de vérifications de cohérence pour s'assurer que l'API fonctionne.

En général, le processus de déploiement facile et robuste augmente ma confiance pour apporter souvent des modifications incrémentielles au code et pour déployer fréquemment.

Un endpoint API est RESTful et retourne une réponse JSON, ce qui est assez standard de nos jours.

### **Tableau de bord utilisateur et documentation de l'API**

Chaque utilisateur de l'API peut accéder à un [tableau de bord](https://www.listennotes.com/api/dashboard/) sur notre site web pour connaître le nombre de requêtes qu'il a utilisées dans le cycle de facturation actuel et consulter les logs bruts récents. Ils peuvent également mettre à jour les méthodes de paiement, créer ou réinitialiser de nouvelles clés API, configurer des webhooks et ajouter des collègues au même compte API.

![Image](https://production.listennotes.com/web/image/77749e815d7741a4a66980282870e25f.png)
_Tableau de bord utilisateur de Listen API_

La [documentation de l'API](https://www.listennotes.com/api/docs/) est probablement l'interface utilisateur la plus importante pour une entreprise d'API. Par conséquent, de nombreuses entreprises d'API emploient une équipe entière d'ingénieurs à temps plein pour construire et maintenir "simplement" la ou les pages de documentation de l'API.

Une page de documentation de l'API n'est pas simplement une page complète de mots en anglais. Elle doit montrer des extraits de code pour différents langages de programmation.

Les utilisateurs doivent pouvoir exécuter directement votre exemple de code depuis la page. Vous devez concevoir un processus reproductible (qu'il soit automatique ou manuel) pour garder la documentation synchronisée avec votre code. Il y a beaucoup de nuances.

Nous avons passé beaucoup de temps et d'énergie à construire et à itérer plusieurs versions de [notre page de documentation de l'API](https://www.listennotes.com/api/docs/). Voici le résultat final :

![Image](https://production.listennotes.com/web/image/0170ea52dec748038632db1bd3444812.png)
_[Page de documentation de Listen API](https://www.listennotes.com/api/docs/)_

Initialement, nous avons essayé quelques solutions open source pour la documentation de l'API. Il est assez chronophage de comprendre un projet open source suffisamment bien pour le personnaliser. Finalement, nous avons décidé qu'il serait plus rapide de construire la page à partir de zéro plutôt que de personnaliser une solution open source construite par d'autres.

Notre page de documentation de l'API est essentiellement une application React JS sur une seule page.

Nous codifions tous les endpoints, le schéma des données de réponse et l'exemple de réponse dans une [spécification OpenAPI](https://listen-api.listennotes.com/api/v2/openapi.yaml). L'application React JS de la page de documentation de l'API lit directement notre spécification OpenAPI.

L'effet secondaire de l'utilisation d'OpenAPI est que nous pouvons facilement nous intégrer avec des outils comme [Postman](https://www.postman.com/), car [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification) est une norme (relativement) largement adoptée pour la documentation des API de nos jours.

## **Pourquoi Listen API fonctionne**

Listen API a été une belle entreprise pour moi jusqu'à présent.

Mais ne vous attendez pas à ce que je partage publiquement les chiffres de revenus :)

Certaines entreprises font cette chose de [startup ouverte](https://www.google.com/search?q=open+startup), partageant chaque métrique commerciale avec le public, ce qui est génial.

Mais nous ne devrions pas blâmer la majorité des entreprises (y compris ma petite entreprise Listen Notes, Inc.) qui ne veulent pas partager publiquement les métriques commerciales.

Tout le monde n'est pas à l'aise d'être nu en public, littéralement ou figurativement.

De même, il y a beaucoup de conseils commerciaux (ou de clichés) que vous n'avez pas à suivre.

* Vous n'avez pas à trouver un cofondateur - avoir un cofondateur horrible est bien pire que de ne pas en avoir.
* Vous n'avez pas à révéler votre chiffre d'affaires au public ou à faire quoi que ce soit de "startup ouverte". Pas de pression. Ne vous sentez pas coupable si vous ne faites pas ce que font les autres enfants cool. Vous gérez votre propre entreprise. Vous prenez vos propres décisions.
* Vous n'avez pas à faire XYZ qu'un philosophe VC de Twitter vous urge de faire dans un tweet du genre fortune cookie.
* Vous n'avez pas à être 100 % bootstrap ni 100 % soutenu par des VC. Beaucoup de choses ne sont pas complètement d'un côté ou de l'autre. Habituellement, il y a un terrain d'entente.
* ... et la liste continue.

En fin de compte, rien n'est absolument faux ou absolument correct. La vision/connaissance de chaque individu est limitée. Les préférences de chaque personne peuvent être très différentes.

Une entreprise d'API peut être trop obscure pour la plupart des gens dans le monde, mais j'aime beaucoup mon entreprise d'API. Les gens de grandes entreprises (comme Apple, Amazon ou Microsoft) peuvent examiner mon entreprise et la juger "mignonne". Mais je la considérerais comme un succès pour moi personnellement.

Et le succès est relatif. La clé est d'apporter du bonheur aux clients (en leur faisant gagner du temps et de l'argent et en les aidant à résoudre des problèmes), à moi-même (une réalisation professionnelle) et à ma famille (en gardant le réfrigérateur plein).

Alors pourquoi Listen API fonctionne-t-il ?

### **Demande et MVP**

Je n'ai pas construit une solution pour trouver des problèmes. C'est le problème (une application de podcast qui voulait ajouter une fonctionnalité de recherche) qui nous a trouvés — et nous avons construit une solution très simple au début.

Nous n'avons pas passé des mois à lancer l'API. Nous avons passé quelques heures. Il en coûte au moins 100 $ de l'heure pour embaucher un ingénieur pas trop mauvais à San Francisco, donc le coût de lancement de ce MVP d'API était d'environ 200 $. Même si c'était 2 000 $, je penserais toujours que cela en valait la peine.

Deux raisons pour lesquelles nous avons pu lancer un MVP rapidement :

* La partie lourde de la construction d'une base de données de podcasts, d'un moteur de recherche et d'un outil d'opérations de données était déjà faite, grâce à notre site web de moteur de recherche de podcasts.
* Mashape / RapidAPI existait pour fournir une solution plug-and-play pour nous afin de gérer les utilisateurs et de créer des plans payants sans écrire de code de notre côté.

Cependant, avec le recul, il est en fait très courant pour un moteur de recherche commercial de licencier leur technologie (via API ou d'autres moyens). Quelques exemples :

* Yahoo Search était alimenté par Google vers 2000, et est alimenté par Bing aujourd'hui.
* Dans les premiers jours, le seul modèle économique de Baidu était de mettre une recherche web sur certains sites portails chinois.
* Aujourd'hui, Bing fournit [une série d'API de recherche](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api).

En lançant un MVP rapidement, nous avons pu obtenir des retours tôt, surtout après avoir obtenu le premier utilisateur payant seulement un mois ou plus après le lancement.

### **Bonne documentation**

Les retours des utilisateurs prouvent que notre [page de documentation de l'API](https://www.listennotes.com/api/docs/) joue un rôle important dans les décisions des clients d'utiliser notre API. Il doit y avoir une raison pour que les entreprises d'API emploient une équipe entière d'ingénieurs "uniquement" pour maintenir leurs pages de documentation.

Une excellente documentation inspire confiance.

### **Service backend stable**

La stabilité est la base essentielle des besoins de la [hiérarchie des besoins de Maslow](https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs) pour une entreprise d'API. Si une API n'est pas stable du tout (par exemple, elle a des pannes fréquentes ou fonctionne très lentement), elle ne peut pas être utilisée.

Cependant, il est ennuyeux de réaliser des travaux pour améliorer la stabilité du backend. La plupart des tâches pour stabiliser les services backend sont préventives, y compris la surveillance et les alertes extensives, le processus de déploiement de code avec confiance, les tests de régression de bout en bout, et ainsi de suite.

Pas de nouvelles, bonnes nouvelles.

Pas de pannes, excellentes nouvelles.

Nous utilisons <ins>Statuspage.io</ins> pour connecter nos métriques Datadog afin de construire une page de statut : <ins>listennotesstatus.com</ins>.

![Image](https://production.listennotes.com/web/image/8928e10cdf454a25b7b2c13ff513fbfe.png)
_[Page de statut du système de Listen Notes](https://www.listennotesstatus.com/)_

Espérons que la page de statut convaincra nos utilisateurs potentiels d'essayer notre API :)

### **Excellent service client**

Nous sommes tous clients des produits et services de quelqu'un d'autre. Nous avons tous été frustrés par un mauvais service client à un moment donné de notre vie. Il est évident qu'un excellent service client va loin — [RIP, Tony](https://en.wikipedia.org/wiki/Tony_Hsieh).

Beaucoup de gens ne savent probablement pas que [vous devez payer AWS beaucoup d'argent pour accéder à un meilleur service client](https://aws.amazon.com/premiumsupport/pricing/) !

Nos clients ne nous paient pas seulement pour utiliser notre API, un service en ligne. Ils paient aussi pour pouvoir obtenir une assistance client de haute qualité de la part de vrais êtres humains. Dans notre cas, c'est moi, la personne qui a construit cette chose.

J'utilise [Superhuman](https://superhuman.com/) pour traiter les emails rapidement et efficacement. Et j'ai une tonne de modèles d'emails préécrits pour gérer les tickets de support client les plus populaires. Souvent, je peux répondre à un email en 5 secondes, en utilisant CMD + K pour sélectionner un modèle d'email.

### **Investir dans les outils et processus internes**

Pour le travail de connaissance, il est possible qu'une seule personne (ou une petite équipe) puisse créer 10x, 100x, ou même 1 000x plus de valeur qu'une grande équipe.

Regardons un exemple extrême : l'édition de livres. Il est (presque) impossible d'embaucher 10 000 bons écrivains pour collaborer sur un livre ensemble et espérer qu'il soit "meilleur" de manière cohésive que Harry Potter, écrit par un seul auteur.

JK Rowling, une seule personne, a créé bien plus de valeur (en termes de montant en dollars mesurable et de bonheur et de bons moments immesurables) que la plupart des entreprises avec des centaines d'employés dans le monde.

Finalement, l'entreprise de logiciels se développerait de manière similaire.

[Nous avons déjà vu Instagram, avec 13 employés, être racheté pour 1 milliard de dollars en 2012](https://www.dailymail.co.uk/news/article-2127343/Facebook-buys-Instagram-13-employees-share-100m-CEO-Kevin-Systrom-set-make-400m.html). Quand verrons-nous une entreprise de logiciels/internet de 1 milliard de dollars ou plus avec 5 employés ou moins réaliser le même exploit ?

De grands outils et processus internes fournissent un levier pour permettre à une petite équipe d'être super-efficace. Cela est facile à comprendre. Nous, les êtres humains, avons déjà construit beaucoup d'outils pour étendre considérablement nos limites physiques/mentales, par exemple les vélos et les voitures (par rapport à la marche), les ordinateurs (par rapport au calcul manuel), et ainsi de suite.

Étant donné qu'il est (presque) impossible d'automatiser à 100 % une entreprise Internet, nous devons améliorer l'efficacité des opérations manuelles. C'est un excellent investissement que d'augmenter la productivité des opérateurs humains.

## **Anecdotes sur la gestion de Listen API en tant qu'entreprise**

Voici quelques choses que je ne savais pas avant...

### **Tout le monde peut s'inscrire => Soumettez d'abord votre candidature**

Il y a quelques années, j'ai remarqué que certaines API exigeaient que je soumette d'abord une candidature, décrivant mon cas d'utilisation, avant de me donner une clé API.

Je ne comprenais pas la logique à l'époque.

Après avoir géré ma propre entreprise d'API, je comprends maintenant.

Internet est immense. Le monde est gargantuesque. Il y a des bonnes et des mauvaises personnes. Si l'API que vous fournissez est utile, certaines personnes essaieront d'abuser de votre API.

C'est ce qui s'est passé lorsque nous avons initialement permis à n'importe qui de créer un compte API. Nous avons vu des utilisateurs créer des dizaines de comptes afin de contourner la limite de quota gratuit.

Aujourd'hui, nous exigeons que les gens soumettent d'abord une candidature. Nous recevons une notification via Slack. Ensuite, nous utilisons notre outil interne pour examiner et approuver ou rejeter la candidature. Le candidat reçoit un email automatique. De notre côté, il faut deux ou trois clics pour terminer toutes ces opérations.

Pour aider notre processus d'examen, nous utilisons une série d'heuristiques :

Cet utilisateur a-t-il précédemment créé plusieurs comptes ?

Cette adresse IP est-elle un spammer bien connu découvrable via <ins>stopforumspam.com</ins> ? (indice : il y a une API pour cela)

Et ainsi de suite...

Encore une fois, nous voyons de nouveaux cas particuliers de temps en temps. Pourtant, nous apprenons aussi à gérer ces cas uniques.

### **Clients idéaux et clients intéressants**

Nos meilleurs clients sont principalement des fondateurs de startups qui sont en affaires depuis un certain temps.

Ils peuvent prendre des décisions par eux-mêmes. Ils comprennent la valeur que nous apportons. Ils ont le pouvoir de finaliser les décisions d'achat. Et ils sont suffisamment compétents pour lire notre documentation de manière autonome et poser très peu de questions — ou ils ne nous parlent même pas du tout.

D'autre part, les personnes issues de startups bien financées par des fonds de capital-risque ou de grandes entreprises (certaines des plus grandes entreprises du monde) demandent souvent une réduction ou un essai gratuit, ce que nous n'avons pas. Pourquoi ? Je n'ai pas de bonne réponse ici.

Bien sûr, il y a toujours des exceptions.

### **Boutiques de développement et bootcamps de codage**

Beaucoup de nos utilisateurs engagent des freelances ou des boutiques de développement à l'étranger pour construire des applications et des sites web.

En général, les développeurs des boutiques de développement ne sont pas aussi bons que les développeurs internes. Bien que ce ne soit pas vrai à 100 %, la probabilité est assez élevée.

En essence, une partie de mes réponses au support client consiste à enseigner l'informatique 101. Parfois, ils envoyaient des extraits de code en PHP (ou dans un langage que je ne connais pas) pour nous demander de le déboguer par email.

Je comprends que certains de ces développeurs des boutiques de développement sortent tout juste des bootcamps de codage (ou que la boutique de développement elle-même est un bootcamp de codage). La plupart du temps, je vais googler pour eux et leur envoyer un lien StackOverflow ou quelque chose de similaire. Mais occasionnellement, si j'étais de mauvaise humeur, je ne répondrais pas aux emails "aidez-moi à déboguer mon code PHP" des utilisateurs GRATUITS qui ne nous paient pas.

De plus, de nombreux bootcamps de codage utilisent notre API pour enseigner aux étudiants comment écrire du code, ce qui est génial. Dans les projets web du monde réel, vous ne pouvez pas éviter d'utiliser des API REST tierces. Enseigner aux nouveaux programmeurs comment communiquer avec une API REST est nécessaire.

### **L'API est une entreprise lente**

Habituellement, il faudra quelques mois à un utilisateur pour commencer à nous payer.

Ils doivent ajouter une grande fonctionnalité de produit ou même construire une application entière d'abord. Ensuite, ils doivent faire un peu de marketing et obtenir un peu de traction. Enfin, ils paient, ou ils abandonnent et ferment l'application.

Nous devons définitivement réfléchir à la manière d'aider nos utilisateurs à construire des fonctionnalités de produit rapidement.

[Stripe](https://stripe.com/) fait un excellent travail dans ce domaine. Ils ont construit beaucoup de beaux composants d'interface utilisateur que les développeurs peuvent utiliser directement sans écrire des tonnes de code, comme [Checkout](https://stripe.com/payments/checkout).

### **L'API est une entreprise stable**

Notre taux de désabonnement est assez faible. Les gens passent de nombreux mois à construire une application utilisant notre API, il est donc peu probable qu'ils passent à autre chose du jour au lendemain.

Je suis heureux de ce fait.

En même temps, je suis également très optimiste quant à toutes les autres entreprises d'API, comme Stripe, Plaid et Twilio. (Ce n'est pas un conseil en investissement, mais regardez l'action [TWLO](https://finance.yahoo.com/quote/TWLO/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAD_FoGY9a1EMiBkUZnYb_ByV8xNHfzcUKtujgYNthliWl55I0UWnIhIDivMvPxpFu5Fzuuyn1fh9lCU4p3tRZmjFFIJIxEKdx4Jlnp5U1Bb_HD4AZRMH3pri07JrBsKu6LqPk4M1ruR5QQefUPmS0Mg9-3R54fpr7AzYBnutkxbK).)

### **Commencez avec les baleines, puis diversifiez**

Au stade précoce, il peut y avoir quelques utilisateurs "baleines" qui représentent une grande partie, voire la majorité des revenus.

Ne paniquez pas.

Avoir des revenus est toujours mieux que de n'en avoir aucun du tout.

Nous ne sommes pas en position de faire les difficiles au stade précoce. Nous pouvons diversifier en cours de route.

J'aime lire les [S-1](http://www.investopedia.com/terms/s/sec-form-s-1.asp).

Il n'est pas rare de voir certaines entreprises SaaS ou API avec quelques baleines lorsqu'elles sont devenues publiques. Si elles perdaient une ou deux de ces baleines, leurs revenus chuteraient de 10 %, voire de 20 % ou plus immédiatement ! Eh bien, elles sont déjà une entreprise publique. Pas besoin de s'inquiéter pour elles. Elles savent quoi faire ensuite.

### **La tarification est un travail en cours**

Nous expérimentons toujours de nouveaux tarifs. Comme pour la construction de projets logiciels en général, la tarification est toujours un travail en cours.

Nous permettons aux anciens utilisateurs de rester aux tarifs inférieurs qu'ils ont obtenus lors de leur inscription. Tout changement de prix futur n'affectera pas les utilisateurs payants existants.

Je sais que certains experts en tarification me mettraient en garde que je laisse de l'argent sur la table avec cette pratique. Mais je suis reconnaissant envers les clients qui nous soutiennent depuis si longtemps. Je veux qu'ils profitent des tarifs bas comme un avantage.

Au fait, [ProfitWell](https://www.profitwell.com/) dispose de grandes ressources concernant la tarification.

### **Haters / critiques non pertinentes**

Vous avez peut-être vu cette théorie : [Quand vous avez des haters, vous faites quelque chose de bien](https://www.google.com/search?q=When+you+have+haters%2C+you%27re+doing+something+right).

Il y a une citation similaire de [Zeng Guofan](https://en.wikipedia.org/wiki/Zeng_Guofan) (l'un des plus importants chefs militaires et politiciens de la Chine du 19e siècle) :

不招人妒忌隆庚才. "Si personne ne vous envie, alors vous êtes incompétent."

Note de bas de page : Vous pouvez trouver la sagesse de Zeng Guofan dans de nombreuses librairies d'aéroport en Chine. Il aurait été un grand utilisateur de Twitter et aurait battu ces philosophes VC de Twitter s'il était né à notre époque - il est difficile de battre une figure historique chinoise dans le jeu des fortune cookies :)

Si votre projet est visible sur Internet et obtient un peu de traction, certaines personnes vous détesteront sans raison particulière.

Une fois que vous offrez un service payant, vous ne proposerez jamais un prix suffisamment bas pour rendre tout le monde dans le monde heureux. Non, 1,00 USD n'est pas bon marché du tout dans de nombreux endroits du monde. Les personnes qui ne sont pas vos utilisateurs cibles se plaindront de vos tarifs.

D'après mon expérience, il est sûr d'ignorer la plupart des critiques, des donneurs de conseils et des suggestions des non-utilisateurs. Parfois, les gens essaient de comparer deux choses avec des noms similaires.

Par exemple, si vous recherchez "podcast API" sur Google, vous trouverez quelques autres API avec "podcast API" dans leurs noms. Cependant, si vous passez quelques minutes à parcourir la documentation, vous trouverez des différences évidentes. C'est comme comparer deux personnes avec le même prénom et le même nom de famille qui sont deux individus complètement différents après tout.

Les seules critiques ou suggestions qui m'intéressent proviennent principalement de nos utilisateurs. Je peux voir leur utilisation de l'API. Je sais qu'ils expriment des faits significatifs. Donc je les écoute.

## **Alors, êtes-vous intéressé par la construction d'une entreprise d'API ?**

De nos jours, l'économie de la passion ou l'économie des créateurs est à la mode.

Qui sont les créateurs ? Écrivains, podcasteurs, streamers...

N'oubliez pas que les développeurs de logiciels sont aussi des créateurs !

Si vous gérez déjà un site web ou avez des données intéressantes, vous pouvez également démarrer une entreprise d'API.

Merci d'avoir lu cet long article :) Faites-moi savoir ce que vous en pensez : wenbin@listennotes.com. Et vous pouvez [lire plus de mes articles sur mon blog](https://www.listennotes.com/blog/how-i-accidentally-built-an-api-business-46/)_.