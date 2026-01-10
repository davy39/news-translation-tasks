---
title: Apprendre Google Analytics avec le Père Noël et ses lutins
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-20T18:41:46.000Z'
originalURL: https://freecodecamp.org/news/learn-google-analytics-from-santa-and-his-elves-59ea82fbd99a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ejm2tkSklF3ReBlktCIzIw.jpeg
tags:
- name: Christmas
  slug: christmas
- name: Google Analytics
  slug: google-analytics
- name: marketing
  slug: marketing
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Apprendre Google Analytics avec le Père Noël et ses lutins
seo_desc: 'By Christian-Peter Heimbach

  The holidays are here! It’s time to grab some egg nog, kick back by a fire place,
  and toast to all the coding you crammed into 2016.

  But wait! Before you sink into a carbohydrate-induced hibernation, let me tell you
  about ...'
---

Par Christian-Peter Heimbach

Les fêtes sont arrivées ! Il est temps de prendre un peu de lait de poule, de se détendre près d'une cheminée et de trinquer à tout le codage que vous avez fait en 2016.

Mais attendez ! Avant de sombrer dans une hibernation induite par les glucides, laissez-moi vous parler d'un projet qui fait fureur au Pôle Nord.

On dit que le Père Noël a passé ses vacances d'été à lire sur les données et l'analyse. Vous ne pensiez pas que son empire de distribution mondial fonctionnait uniquement grâce à la magie, n'est-ce pas ?

Certains lutins technophiles satisfont le Père Noël en mettant en place Google Analytics à temps pour la grande nuit.

Vous voyez, le Père Noël, ses lutins et les enfants du monde entier ont un site web secret partagé qu'ils utilisent tous pour s'inscrire et passer en revue leurs souhaits. Je suis tenu de ne pas révéler l'URL réelle, alors nous l'appellerons simplement www.wish.io.

Sur ce site, les enfants peuvent :

1. Voir les avantages de wish.io
2. Avoir l'opportunité de s'inscrire en tant qu'enfant sage
3. Choisir un cadeau qu'ils souhaitent recevoir
4. Passer en revue leur choix
5. Soumettre leur souhait

Comme vous pouvez l'imaginer, le Père Noël et les lutins peuvent apprendre beaucoup de Google Analytics sur la manière d'améliorer davantage wish.io. Voici comment ils l'utilisent.

### Installation de Google Analytics pour le Père Noël

Pour préparer la page secrète du Père Noël pour le suivi, les lutins ont besoin d'un code de suivi Google Analytics. Il s'agit d'un extrait de code JavaScript (souvent appelé "pixel" ou "extrait de suivi") que vous obtenez après vous être inscrit à [Google Analytics](https://www.google.com/analytics/analytics/).

Vous pouvez configurer jusqu'à 100 **comptes**, qui peuvent tous contenir plusieurs **propriétés**. Ces propriétés peuvent à leur tour contenir plusieurs **vues**. Cela peut sembler confus au début (surtout si vous êtes un lutin), mais ce n'est pas si grave si on le prend étape par étape.

Les lutins vont accomplir cela dans la zone d'administration de Google Analytics. Jetons un coup d'œil.

![Image](https://cdn-media-1.freecodecamp.org/images/X2vD7aDhtGFC2emUEYa8wgbuaJiij-R96Jp9)
_Capture d'écran de la zone d'administration de Google Analytics_

Les propriétés de compte décrivent les sites web, les applications mobiles ou d'autres systèmes, chacun représenté par un code de suivi et un identifiant unique — appelé code UA. Ici, vous pouvez configurer la propriété « wish.io du Père Noël ». Si le Père Noël décide plus tard de créer des sous-domaines ou des pages séparées mais liées — comme la liste des enfants pas sages du Père Noël — il peut configurer une propriété supplémentaire ici pour éviter de mélanger les données sur les enfants sages et ceux qui ne le sont pas.

Vous pouvez définir votre gestion des utilisateurs pour chaque niveau, mais les permissions sont héritées par détail (compte > propriété > vues).

Les lutins doivent réfléchir soigneusement à qui doit pouvoir voir et modifier quoi. Il suffit d'un petit utilisateur vert qui ne sait pas ce qu'il fait pour tout gâcher.

Alors le Père Noël s'assure que tous les lutins lisent le [guide des permissions de Google Analytics](https://support.google.com/analytics/answer/2884495?hl=en) avant de pouvoir ajouter des utilisateurs.

Google Analytics offre plusieurs vues que les lutins peuvent utiliser pour diverses fins.

Premièrement, ils peuvent appliquer des **filtres**. Cela est utile car les lutins génèrent beaucoup de trafic interne qui doit être supprimé, afin que le Père Noël puisse se concentrer sur les données de session des enfants qui visitent le site.

Deuxièmement, les lutins peuvent définir des **objectifs** et des **segments** au niveau de la vue, afin que chaque équipe puisse accéder aux données qui l'intéressent le plus. Après tout, les lutins de la logistique veulent un type d'information différent de celui des lutins du front-end.

Vous pouvez configurer beaucoup plus ici, comme des rapports automatiques et des métriques calculées personnalisées. Mais c'est un travail pour l'été prochain.

### Bonnes pratiques des lutins pour la configuration des vues

Ensuite, les lutins doivent configurer trois vues standard : www wish.io (Maître), www wish.io (Test) et www wish.io (Brute).

Ces trois vues sont essentielles en raison du fonctionnement de Google Analytics : il applique des filtres entre les étapes de collecte et de traitement des données.

Cela signifie que si les lutins ont un filtre défectueux, leurs données disparaîtront. Pour cette raison, ils doivent configurer une vue brute et ne jamais la toucher afin d'avoir une solution de secours en cas d'urgence. Chaque lutin sait que la vue de test est pour les tests, et que la vue maître est celle avec laquelle travailler au quotidien.

![Image](https://cdn-media-1.freecodecamp.org/images/s05oj4NVhw3evphxBrt4rJ-vCgWaJLn6Phs1)
_Capture d'écran de l'ajout d'une nouvelle vue avec Google Analytics_

### Comment les lutins suivent les enfants

Avec le backend de Google Analytics en place, les lutins ajoutent un extrait de suivi de wish.io.

Oui, cela constitue une violation flagrante de la [COPPA](https://en.wikipedia.org/wiki/Children's_Online_Privacy_Protection_Act). Mais le Père Noël ne se soucie pas de nos lois. En fait, il ne se soucie même pas des lois de la physique.

Ils trouvent le code de suivi dans la section des propriétés du panneau d'administration, puis le collent dans le code de mise en page de leur site web.

Les lutins prennent également la mesure vitale de s'assurer que le script est situé juste avant la balise de fermeture `</head>`. Habituellement, les développeurs ne veulent pas de scripts bloquant le rendu ici, mais c'est une exception spéciale. Le script Google Analytics est asynchrone, et finalement, les lutins veulent capturer tout le trafic. Ils ne peuvent pas risquer de manquer les informations des enfants qui pourraient quitter une page avant que tous les scripts ne soient chargés.

Le **taux de rebond** — qui suit la proportion de visiteurs qui quittent une page sans interagir avec aucun du contenu — est une métrique importante. Il pourrait montrer aux lutins QA et front-end que quelque chose ne va pas avec la page. Il aide également les lutins marketing à vérifier si une certaine activité était mal ciblée.

![Image](https://cdn-media-1.freecodecamp.org/images/u7JKtpAs0Z-z4KtZXLhQuGoMsWgLtVgDoj6v)
_Capture d'écran de la section du code de suivi de Google Analytics_

### Navigation dans Google Analytics

Avec le suivi intégré, les lutins étaient prêts à examiner les données initiales. Bien que Google Analytics commence à collecter des données en temps réel immédiatement, les lutins décident de lui donner au moins 24 heures pour qu'il puisse recueillir une quantité significative de données.

Maintenant, les lutins doivent se familiariser avec Google Analytics, ses divers menus et les données qu'il affiche.

![Image](https://cdn-media-1.freecodecamp.org/images/kLdOmNPDyFYNk08BQaAM0FMToZ3WezNjf7An)
_Capture d'écran : Vue d'ensemble des rapports Google Analytics (Wish.io renommé Compte de démonstration)_

Le menu de navigation de gauche montre les principales sections que les lutins peuvent utiliser pour examiner les données d'un site web. Les éléments les plus importants sont Audience, Acquisition, Comportement et Conversions.

Ce menu abrite également la vue Événements en temps réel et Intelligence. Les Événements d'Intelligence cesseront bientôt d'exister dans Google Analytics, donc le Père Noël et les lutins ont décidé de ne pas s'en soucier. La vue en temps réel est agréable à afficher sur les écrans plats au siège des Opérations de Souhaits et à booster le moral des lutins. Mais les décisions significatives demandent une vue à plus long terme.

Alors les lutins retournent aux sections principales de Google Analytics pour voir quels autres outils il offre.

### Vue d'ensemble de l'audience

Lorsque les lutins ouvrent la vue d'une nouvelle propriété, ils voient par défaut la Vue d'ensemble de l'audience. Heureusement, les pages de vue d'ensemble sont toutes similaires, ce qui rend le processus d'apprentissage un peu plus fluide pour les lutins et les humains.

![Image](https://cdn-media-1.freecodecamp.org/images/A-rft19qQovXYd6NToapWzMWcIMqgxP3XG5Q)

Dans la zone marquée "1" (ci-dessus), les lutins obtiennent les informations les plus importantes sur leur audience. Combien d'utilisateurs sont venus sur leur page, combien de temps ils y ont passé, et les pages qu'ils ont vues par session, etc. Tout cela est joliment présenté dans des graphiques, afin que les lutins puissent repérer les pics, les creux et les tendances générales.

En regardant l'annotation (2), vous verrez qu'il est possible de segmenter ces vues d'ensemble. Cela est vrai pour toutes les sections principales dans Analytics. Maintenant, le Père Noël peut voir si les enfants navigant sur wish.io sur les téléphones mobiles qu'ils ont reçus l'année dernière se comportent différemment des autres utilisateurs. La création de segments est un sujet avancé, mais peut être très gratifiant. Les segments peuvent révéler un contexte à partir des données qui est autrement seulement présenté en moyennes approximatives. Remarque : Vous pouvez utiliser le [guide approfondi de Google sur les segments](https://support.google.com/analytics/topic/3123779?hl=en&ref_topic=6175347) ou consulter la Galerie pour importer des segments populaires créés par la communauté.

Sous les valeurs de résumé (3), les lutins ont un accès rapide à des informations plus détaillées que chaque catégorie offre. Par exemple, ils peuvent voir plus de données démographiques par pays, ou le contexte technique des utilisateurs.

Des informations encore plus détaillées sont disponibles dans les sous-catégories de la barre de navigation de gauche (4).

Un aspect des données détaillées de l'audience a ajouté du carburant à un débat déjà houleux que les lutins avaient pendant l'été : la grande question de savoir quelle version d'Internet Explorer wish.io devrait être compatible avec.

Vous pouvez sans doute imaginer à quel point cela est devenu animé. Heureusement, Google Analytics a remplacé les querelles par des décisions basées sur les données. Il suffit d'utiliser la navigation de gauche et de consulter : Audience > Technologie > Navigateur/OS et de cliquer sur "Internet Explorer" pour les détails de la version.

![Image](https://cdn-media-1.freecodecamp.org/images/6sZ8kHvD5Z7C3BExOcwRl4gQr8myXIFoXEOB)
_Capture d'écran : Sessions et visiteurs d'Internet Explorer par version de navigateur_

Heureusement, Google Analytics enregistre les détails de la version spécifique d'un navigateur. Le Père Noël et les lutins sont ravis que 95 % des visiteurs d'Internet Explorer utilisent la version 11. Ils supposent également que les enfants sages (qui sont le public principal de wish.io, bien sûr) sont assez diligents pour soit mettre à jour Internet Explorer régulièrement, soit utiliser un meilleur navigateur. Bien sûr, la part de navigateur pour les visiteurs du site à venir naughtylist.io devra être évaluée séparément.

Il y a beaucoup d'autres choses intéressantes que les lutins peuvent apprendre ici. Par exemple, Google peut montrer les données de genre et d'intérêts des enfants (activées dans les paramètres de la propriété sous le panneau d'administration — assurez-vous de vous conformer à vos lois locales, contrairement au Père Noël). Cela leur permet également de plonger beaucoup plus profondément dans les données d'acquisition et de comparer le comportement de l'audience en fonction des différents canaux par lesquels les visiteurs sont arrivés.

### Acquisition

Pour en savoir plus sur l'origine des visiteurs de wish.io, le Père Noël peut consulter la Vue d'ensemble de l'acquisition.

![Image](https://cdn-media-1.freecodecamp.org/images/qWUntTHp5VkP6zac29-4Hin6IXaL4bbnaFu6)
_Capture d'écran : Vue d'acquisition montrant les visiteurs par source de trafic_

Cette vue se concentre sur les sources de trafic.

Google définit neuf canaux principaux dans lesquels il agrège ces sources :

**Direct** : Habituellement, les personnes tapant l'URL ou utilisant un marque-page.

**Recherche organique** : Les personnes utilisant Google ou Bing, et cliquant sur un lien de résultat de recherche organique.

**Référencement** : Quelqu'un suivant un lien sur un autre site web ou blog.

**Social** : Les visiteurs provenant de sites listés comme sociaux (cliquez sur le lien 'Social' pour voir la liste).

**Email** : Toutes les visites provenant directement des emails.

**Recherche payante** : Les personnes accédant aux pages via des liens payants sur Google et les sites partenaires.

**Display** : Les personnes ayant cliqué sur des bannières publicitaires payantes.

**Affiliés** : Le trafic reçu des partenaires affiliés qui promeuvent wish.io

**Autres** : Un résumé du trafic publicitaire classé comme "spécial". Par exemple, le trafic acheté sur un taux de coût par action.

Il est important de comprendre que ces regroupements sont le résultat d'un ensemble de règles par défaut indiquant quel média compte pour quel groupe de trafic.

Les lutins peuvent fabriquer des liens à des fins sociales ou publicitaires — les soi-disant liens UTM — qui sont également résumés dans ces groupes. De cette façon, ils peuvent juger du succès d'une annonce ou d'un article de blog.

Pour plus de commodité, ils utilisent l'outil [Google's Link Builder](https://ga-dev-tools.appspot.com/campaign-url-builder/). Pour éviter un comptage erroné, ils doivent être conscients des [règles de regroupement](https://support.google.com/analytics/answer/3297892?hl=en&ref_topic=3125765) et définir correctement 'utm_medium'.

Une fois que tout est en place, les lutins peuvent découvrir de nombreux détails intéressants sur leurs canaux. Ils peuvent voir quels canaux sociaux ont le plus contribué à wish.io, ou quelles campagnes ont été les plus réussies. Ils peuvent même optimiser leurs investissements AdWords et voir sur quelles pages de destination les enfants arrivent généralement depuis diverses sources.

La prochaine étape logique pour le Père Noël est d'acquérir — et d'agir en conséquence — une compréhension plus approfondie du comportement exact des visiteurs sur ses sites.

### Suivi du comportement des enfants sur wish.io

Pour le Père Noël et ses lutins, il a toujours été difficile de suivre les millions de souhaits différents que les enfants pourraient formuler. Il est donc important pour eux de comprendre les tendances, les choix populaires, les classiques, ainsi que les erreurs potentielles sur leurs millions de pages.

![Image](https://cdn-media-1.freecodecamp.org/images/miukLIfdpehZ0UL02qadfoj3hmzJR0ePFIik)
_Capture d'écran : Vue du comportement montrant les visiteurs par page_

Chaque département de lutins a ses propres informations d'intérêt.

Les lutins du front-end et de l'assurance qualité doivent toujours surveiller de près les taux de rebond, le temps moyen passé sur la page et le score de vitesse de leurs pages les plus importantes.

Chaque lutin du front-end déteste les longues réunions SEO déclenchées par les temps de chargement de wish.io qui deviennent incontrôlables. Il est donc utile pour eux d'explorer la sous-catégorie Vitesse du site. Google fournit des informations précieuses par navigateur, pays et page — ainsi que des suggestions sur la manière de s'améliorer.

Les lutins UX peuvent obtenir un aperçu des pages prioritaires dans la section Comportement. Ils peuvent également examiner le flux d'entrée des personnes sur la page du Père Noël, leur parcours et leur sortie.

Mais le sujet le plus passionnant pour eux est la création d'expériences de contenu. En gros, ils peuvent demander aux lutins du front-end de créer des versions alternatives de la même page, puis tester automatiquement ces versions par rapport à des objectifs mesurables.

Par exemple, il pourrait être intéressant de trouver une variante de page où les enfants restent plus longtemps ou soumettent des souhaits à un meilleur taux. Ils peuvent configurer des expériences initiales avec l'outil d'analyse, qui dispose d'un [guide simple](https://support.google.com/analytics/topic/1745146?hl=en&ref_topic=1120718). Pour des cas d'utilisation avancés, les lutins peuvent effectuer des expériences de contenu via l'[API bien documentée analytics.js](https://developers.google.com/analytics/devguides/collection/analyticsjs/experiments).

Enfin, l'onglet Comportement offre également le suivi des événements, que les lutins marketing adorent. Les événements peuvent être envoyés à Google Analytics chaque fois que les enfants initient une action importante qui ne déclenche pas une nouvelle vue de page.

Par exemple, lorsque les enfants cliquent sur des boutons de téléchargement, soumettent leurs formulaires "J'ai été un enfant sage", modifient un souhait, etc. Les événements sont des appels de fonction simples à l'API d'analyse. Les lutins les ajoutent à leurs écouteurs d'événements JavaScript et à leurs rappels qui contrôlent l'interactivité de leur page. Tout cela est décrit dans le [guide de suivi des événements de Google](https://developers.google.com/analytics/devguides/collection/analyticsjs/events).

Les lutins marketing adorent le suivi des événements car cela les met dans une meilleure position pour configurer l'élément crucial des Conversions de Google Analytics.

### Conversions

La configuration de la section Conversions dans le panneau d'administration a demandé quelques efforts de la part du Père Noël et de son équipe, mais cela en valait la peine. Les conversions aideront les lutins à comprendre les effets "commerciaux" de toutes les informations précédemment examinées. Cela boucle la boucle entre avoir beaucoup de données et comprendre comment cela conduit à l'objectif ultime : des enfants heureux.

![Image](https://cdn-media-1.freecodecamp.org/images/2UcYbZKhcwKbNjHqtnGtygqzpire7gXX6PsT)
_Capture d'écran : Conversions montrant l'achèvement des objectifs par lieu_

Les objectifs ne sont pas définis par défaut dans Google Analytics. Les utilisateurs doivent les définir dans le panneau d'administration. Les objectifs sont définis par le type d'interaction sous-jacent. Cela peut être soit la visualisation d'une certaine page (par exemple, thankyou.html), un comportement (durée minimale sur le site, nombre de pages par session), ou lorsqu'un événement est enregistré. Vous pouvez même définir une série de destinations à afficher comme un seul objectif.

![Image](https://cdn-media-1.freecodecamp.org/images/SYunT2hbndHmlnUDKvz0u4n67RMMNdNn6Kjo)

Cela est important lorsque vous souhaitez suivre combien d'enfants ont parcouru un "entonnoir" de conversion complet. Par exemple, ils entrent dans la zone des enfants inscrits, parcourent les options de souhaits et soumettent un souhait avec succès.

Avec cet objectif d'entonnoir suivi, la visualisation montre comment les enfants passent par chaque étape. Elle révèle également dans quelle mesure (et quand) ils abandonnent, et où ils vont ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/ckhQRIT29LrgdccJl-CGAyha56JjcfNnYtMj)

Il est important de noter que les objectifs doivent être définis de manière à ne pas se chevaucher. Si un événement génère le comptage de deux objectifs, vos taux de conversion peuvent être trop élevés.

En plus d'utiliser les objectifs, il est possible d'intégrer tout le système e-commerce du Père Noël dans Google Analytics. Mais c'est un travail pour la nouvelle année. Une fois cette intégration approfondie en place, le Père Noël et ses associés obtiendront des informations jusqu'au niveau "commande" par souhait, et pourront même suivre les retours de souhaits.

Une autre vue utile de Google Analytics était la sous-catégorie Entonnoirs multicanaux. Avant Google Analytics, les lutins marketing se disputaient souvent sur l'allocation du budget et sur qui contribuait le plus aux souhaits soumis.

Les lutins de la publicité de marque se plaignaient que leur travail n'impactait pas seulement le trafic direct, mais aussi la recherche et les réseaux sociaux. Ils ont pensé que certains enfants venaient initialement via leurs publications sur les réseaux sociaux, mais revenaient plus tard pour soumettre des souhaits en tapant l'URL de wish.io.

Alors pourquoi le dernier lutin impliqué devrait-il prendre tout le crédit ? Ils ne devraient pas. C'est pourquoi chaque réunion marketing au Pôle Nord inclut désormais un regard sur les Conversions assistées et les Principaux chemins de conversion. Ici, les lutins peuvent voir non seulement leur valeur de conversion directe, mais aussi la valeur des conversions qu'ils ont aidé à conclure.

![Image](https://cdn-media-1.freecodecamp.org/images/tt5MyDBzDOns6gqrfVIzmPIy62TSnoRa3t4Z)
_Capture d'écran : Conversions assistées par source de trafic_

### Un travail bien fait

Grâce à son projet Google Analytics, le Père Noël a déclaré 2016 comme "l'année des décisions basées sur les données". Il est heureux que ses lutins aient transformé des discussions autrefois houleuses en compétitions et expériences basées sur les données.

Désormais, il utilisera le pouvoir des données pour encourager l'esprit scientifique de son équipe — et pour trouver des processus toujours optimisés pour booster le bonheur.

Il ne reste plus qu'à vous souhaiter, à vous et à vos proches, de joyeuses fêtes. J'espère que ce petit conte du Pôle Nord vous a inspiré pour rendre votre 2017 encore plus réussie et basée sur les données.

Maintenant, enfilons tous nos [pulls de Noël moches](https://medium.freecodecamp.com/the-geekiest-ugly-sweater-ever-34a2e591483f) et embrassons l'esprit des fêtes.

Remerciements spéciaux à Craig Rennie de [Draft Punk](https://www.draft-punk.com) et Quincy de [Free Code Camp](https://www.freecodecamp.com/) pour tous leurs efforts d'édition. Que vos fêtes soient extra heureuses !

**Avis de non-responsabilité :** _Cette histoire est écrite dans un thème de vacances à des fins de divertissement uniquement. Malgré le rapport ci-dessus sur le Père Noël, les lutins et les enfants, il est important de noter que Google Analytics ne suit ni ne partage les informations d'audience de quiconque de moins de 18 ans._

_Toutes les données et images sont fournies par Google. Les données présentées ici sont disponibles pour chaque compte d'analyse en accédant au [Compte de démonstration de Google Analytics](https://support.google.com/analytics/answer/6367342?hl=en)_