---
title: Pourquoi j'ai eu du mal à fixer le prix de ma startup, et comment j'ai finalement
  lancé Tueri.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-14T16:36:05.000Z'
originalURL: https://freecodecamp.org/news/the-struggle-to-price-my-startup-and-how-i-finally-launched-tueri-io
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/photo-1543286386-2e659306cd6c.jpg
tags:
- name: Business development
  slug: business-development
- name: pricing
  slug: pricing
- name: startup
  slug: startup
- name: ' Startup Lessons'
  slug: startup-lessons
- name: Startups
  slug: startups
seo_title: Pourquoi j'ai eu du mal à fixer le prix de ma startup, et comment j'ai
  finalement lancé Tueri.io
seo_desc: 'By Dane Stevens

  Pricing can be the life or death of a bootstrapped startup.

  When I started the process of trying to price my startup I became overwhelmed with
  questions and doubts. Should we have usage-based or a tiered pricing model? How
  much storag...'
---

Par Dane Stevens

## La tarification peut être la vie ou la mort d'une startup bootstrappée.

Lorsque j'ai commencé le processus d'essayer de fixer le prix de ma startup, j'ai été submergé de questions et de doutes. Devrions-nous avoir un modèle de tarification basé sur l'utilisation ou par paliers ? Combien de stockage pouvons-nous offrir à chaque palier ? Devrions-nous offrir un plan gratuit ? Quel devrait être le prix de base ? Et si personne ne veut payer pour cela ? Et si Tueri est un échec ?

J'ai passé d'innombrables heures à essayer de répondre à ces questions et la tarification a été la partie la plus redoutable du lancement de [Tueri](https://tueri.io). Tueri est une startup entièrement bootstrappée et, en fin de compte, la tarification peut en être la vie ou la mort. L'argent des investisseurs est inexistant, ce qui signifie que l'entreprise doit être rentable à chaque étape de sa croissance.

Cela se résume à ces deux questions essentielles :

1. Puis-je offrir une valeur et un service exceptionnels à mes clients à ce prix ?
2. À ce prix, Tueri peut-elle continuer à croître et à être à la pointe pour que je puisse continuer à offrir une valeur et un service exceptionnels ?

Ces deux questions peuvent sembler contradictoires, mais elles sont essentielles pour construire une entreprise durable et centrée sur le client.

## Qu'est-ce que Tueri ?

Le mot **Tueri** est un mot latin qui signifie : préserver. Tueri est une plateforme de gestion et d'optimisation d'images basée sur l'idée d'une image maître **immuable**.

Tueri utilise la transformation, la compression et la conversion d'images juste-à-temps pour livrer l'image parfaite à chacun de vos utilisateurs en quelques millisecondes.

L'idée de Tueri est venue pendant mon travail en tant que développeur d'applications. En tant que développeur, je construis des applications d'incitation à la clientèle pour des entreprises de pièces automobiles. Le principe de base de ces sites est le suivant : plus un client (atelier de mécanique) achète de pièces automobiles, plus il gagne de points. Les clients échangent des points en ligne pour tout, des clubs de golf aux téléviseurs en passant par les vacances.

Ces sites web reçoivent quotidiennement des flux de fichiers de la part des fournisseurs avec de nouveaux produits, des produits abandonnés et des produits mis à jour. Il y a des _milliards_ de produits et aucune standardisation des dimensions des images, des tailles de fichiers ou du protocole HTTP d'hébergement des images. J'ai construit Tueri pour résoudre ces problèmes.

La première version de Tueri était un simple serveur proxy conçu pour récupérer des images HTTP distantes et les rediffuser via HTTPS, supprimant ainsi les avertissements de contenu non sécurisé sur nos sites d'incitation à la clientèle.

La version suivante était un simple script PHP d'une page utilisant GraphicsMagick. Ce script récupérait une image distante, redimensionnait l'image si elle dépassait une largeur prédéfinie, la stockait sur le serveur et servait l'image via HTTPS.

Ces itérations ont rapidement progressé en termes de portée et de fonctionnalités et, à un moment donné, j'ai réalisé qu'elles me faisaient gagner des quantités obscènes de temps.

**Je devais partager cela avec d'autres développeurs.**

Après beaucoup de travail pour convertir un projet personnel en quelque chose que je pouvais héberger pour les autres, j'étais prêt à lancer. Le seul problème était que je n'avais aucune idée de la manière de le tarifer.

## Devrions-nous offrir un plan gratuit ?

Voici quelques raisons pour lesquelles un plan gratuit a du sens :

* Acquisition d'utilisateurs — Offrir un plan gratuit peut vous aider à acquérir un grand nombre de nouveaux utilisateurs. Cela, à son tour, devrait stimuler la croissance grâce au marketing de bouche à oreille.
* Vente incitative — Un utilisateur du plan gratuit peut être incité à passer à un plan payant.
* Soutien à la communauté — Dans mes emplois en tant que développeur, j'ai compté sur d'innombrables services gratuits et j'ai grandement bénéficié de la communauté open-source.

Ma crainte de ne pas offrir de plan gratuit était que j'aurais beaucoup de mal à acquérir de nouveaux utilisateurs. J'ai lutté avec cette question ce qui m'a semblé être des centaines de fois, alors j'ai fait quelques recherches.

J'ai étudié d'innombrables autres startups. Je voulais savoir si elles offraient un plan gratuit, quelles fonctionnalités elles incluaient, quel pourcentage d'utilisateurs l'utilisaient et si elles étaient rentables.

J'ai découvert ce qui suit :

* Les utilisateurs gratuits stimuleront la croissance grâce au bouche-à-oreille, mais ils stimuleront davantage la croissance du plan gratuit.
* Un plan gratuit vous aidera à acquérir plus d'utilisateurs, mais seulement un très faible pourcentage de ces utilisateurs passeront un jour à un plan payant.
* Un énorme pourcentage de support est dédié aux utilisateurs gratuits.
* Un produit avec plan gratuit est souvent inférieur en raison des coûts associés aux services back-end.
* Ce produit inférieur est celui par lequel les gens connaissent votre entreprise.

### La décision concernant le plan gratuit

J'ai décidé de ne pas offrir de plan gratuit afin de consacrer 100 % de nos ressources à nos clients payants. Cela garantit à la fois la qualité du produit et un service client exceptionnel.

## Devrions-nous avoir un modèle de tarification basé sur l'utilisation ou par paliers ?

#### Tarification basée sur l'utilisation

Avantages :

* Vous ne payez que pour ce que vous utilisez.
* Meilleur pour les entreprises avec des fluctuations saisonnières d'utilisation.
* Meilleur pour les développeurs individuels où une faible dépense mensuelle est une priorité.

Inconvénients :

* Difficile de comprendre quel sera votre facture mensuelle réelle.
* Fluctuations potentiellement drastiques de la facture mensuelle.
* Plus difficile pour un développeur de convaincre son entreprise.
* La mentalité du client est axée sur la limitation de l'utilisation pour réduire les coûts, diminuant ainsi la valeur perçue du produit.

#### Tarification par paliers

Avantages :

* Facile à comprendre votre facture mensuelle.
* Pas de fluctuations de la facture mensuelle.
* Un montant mensuel fixe est facile à présenter pour un développeur à son entreprise.
* La mentalité du client est axée sur l'obtention de la meilleure valeur de leur plan, augmentant ainsi la valeur perçue du produit.

Inconvénients :

* Plus difficile de répondre à tous les cas d'utilisation.
* Pas aussi idéal pour les clients à utilisation saisonnière.
* Difficile de répondre aux développeurs individuels avec un budget minimal.

J'ai examiné des centaines de pages de tarification de différentes entreprises de logiciels en tant que service (SaaS) ; certaines simples, d'autres complexes. Je me suis constamment tourné vers les modèles de tarification par paliers en raison du fait qu'ils étaient plus faciles à comprendre. De nombreuses entreprises avec une tarification basée sur l'utilisation consacrent une page entière à expliquer comment calculer votre facture mensuelle. Même après avoir suivi les exemples, je ne pouvais toujours pas dire avec certitude ce qu'elles me coûteraient.

Parlons d'un exemple de tarification basée sur l'utilisation pour Tueri. Supposons qu'elle soit tarifiée par transformation d'image. Vous avez un site web responsive simple avec 10 pages et 10 images par page pour un total de 100 images. Vous consultez Google Analytics pour l'utilisation des appareils : vous avez une résolution de bureau, une résolution de portable, deux résolutions de tablette (portrait et paysage) et deux résolutions mobiles (portrait et paysage). Si chaque image sur chaque page est vue dix fois par chaque résolution, vous avez un total de 6 000 transformations.

Facile, non ? Pas exactement.

En réalité, vous pouvez avoir 10 000, 50 000, 100 000 ou plus de vues de pages par mois. Vous pourriez avoir 20+ résolutions différentes, des écrans HiDPI, des pages avec des niveaux de vues variés, et de nouvelles images ajoutées régulièrement.

Vous pouvez voir comment cela devient compliqué.

### La décision concernant le modèle de tarification

Bien que ce n'ait pas été une décision facile à prendre, j'ai conclu que la tarification par paliers était adaptée à Tueri en raison de sa transparence et de sa simplicité.

## Quel devrait être le prix de base ?

Cela doit être la question la plus difficile à répondre, du moins pour moi. Une question que je continuerai à poser et à réévaluer tout au long de la vie de Tueri.

J'ai dû évaluer :

* Sommes-nous une entreprise premium ou une entreprise de valeur ?
* Quel type d'utilisateurs voulons-nous cibler avec notre service ?
* Voulons-nous servir des millions de clients à bas prix ou des milliers de clients à un prix plus élevé ?
* Pouvez-nous continuer à offrir un service exceptionnel à nos clients à ce prix ?
* Quelle est la valeur temporelle que nous offrons à nos clients ?
* Quelle est la valeur monétaire que nous offrons à nos clients ?
* Que facture notre concurrence, sont-ils rentables et leur entreprise est-elle durable ?

Cela se résume à définir des priorités :

* Je veux offrir un niveau de service exceptionnel à moins de clients.
* Je suis dans ce projet pour le long terme et notre tarification doit être durable.

### La décision concernant le prix de base

La tarification ne doit pas être statique, vous devez l'évaluer au fil du temps en fonction des retours des clients, de la valeur ajoutée des nouvelles fonctionnalités et des coûts d'exploitation.

Nous évaluons constamment notre tarification et [j'adorerais connaître](mailto:dane.stevens@tueri.io) votre cas d'utilisation et si notre tarification vous convient.

## Conclusion

J'ai finalement réalisé que je n'allais jamais tout comprendre, alors j'ai pris les meilleures décisions possibles avec les informations disponibles et j'ai lancé.

Il n'y a pas de réponse définitive pour tarifer votre startup, mais gardez ces choses à l'esprit et vous ne vous tromperez pas :

* Surpassez les attentes de vos clients en matière de service et de valeur.
* Tarifiez votre entreprise pour la croissance.
* Lancez votre startup.
* Réévaluez constamment votre tarification.

---

Avez-vous des conseils ou des questions sur la tarification de votre startup ? Contactez-moi à l'adresse [dane.stevens@tueri.io](mailto:dane.stevens@tueri.io).

---

*Initialement publié sur [Tueri.io](https://tueri.io/blog/2019-08-14-the-struggle-to-price-my-startup-and-how-i-finally-launched-tueri/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=Pricing)*