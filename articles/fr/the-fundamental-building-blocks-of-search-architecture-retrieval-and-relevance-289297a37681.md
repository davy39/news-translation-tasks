---
title: 'Les éléments fondamentaux de l''architecture de recherche : récupération et
  pertinence'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-06T21:45:07.000Z'
originalURL: https://freecodecamp.org/news/the-fundamental-building-blocks-of-search-architecture-retrieval-and-relevance-289297a37681
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ueNi9IASz_PbxmuiVjXjUA.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Les éléments fondamentaux de l''architecture de recherche : récupération
  et pertinence'
seo_desc: 'By Faizan Ahmed

  Search isn’t only about finding stuff.

  Rather, search is always the start of a larger journey. Search can be the start
  of reconnecting with someone, the beginning of a purchase, or discovering crucial
  information and new opportunities...'
---

Par Faizan Ahmed

La recherche ne consiste pas **uniquement** à trouver des choses.

En réalité, la recherche est toujours le début d'un parcours plus large. Elle peut marquer le début d'une reconnexion avec quelqu'un, le commencement d'un achat, ou la découverte d'informations cruciales et de nouvelles opportunités.

Nos attentes envers la recherche sont de plus en plus élevées à mesure que Google s'améliore. De nos jours, très peu de gens cherchent au-delà de la première page. Si les résultats de recherche ne sont pas satisfaisants, ils essaieront à nouveau ou abandonneront. Selon [Search Engine Watch](https://searchenginewatch.com/sew/study/2276184/no-1-position-in-google-gets-33-of-search-traffic-study), « Les résultats de la page 1 captent 92 % du trafic total d'une recherche moyenne, avec une baisse de 95 % pour la page 2. »

La recherche devient un problème pour les logiciels lorsqu'il y a une énorme quantité de données. Au moment où votre base de données est suffisamment grande pour nécessiter une fonction de recherche, votre entreprise sera probablement tout aussi grande. Ce n'est pas un problème particulièrement urgent pour les entreprises ou les plateformes en phase de démarrage. Mais cela deviendra une difficulté croissante. Préparez-vous et intégrez cela à votre feuille de route produit.

Pour les entreprises qui développent ou maintiennent une fonctionnalité de recherche, vous comprenez déjà pourquoi il est important de rendre la recherche immédiate, utile et robuste pour les utilisateurs. Dans de nombreux cas, la recherche peut être considérée comme le début d'une conversation que l'utilisateur entame avec le logiciel. Chez Flipp, notre recherche permet aux utilisateurs de rechercher des articles de commerce électronique et des prospectus numériques. La plupart du temps, c'est littéralement la première chose que la plupart des gens utilisent...

### La recherche fait la première impression

> La première impression n'est pas la dernière impression, mais une impression durable.
> — [Anonyme](https://en.wikiquote.org/wiki/Anonymous)

La plupart du temps, lorsqu'une personne télécharge l'application Flipp, la première chose qu'elle fait est **rechercher**. Avant même de regarder le menu des détaillants, elle recherche le nom de son magasin préféré. Par exemple, « Wal-Mart ».

![Image](https://cdn-media-1.freecodecamp.org/images/3NQI3VjOIUPG7UgZRHf6SpbPt7pQczVQT--8)

Si cette personne n'est pas satisfaite de la fonctionnalité de recherche, elle cessera d'utiliser l'application **immédiatement**. Cet utilisateur abandonnera peu après son inscription.

Cette tendance à utiliser d'abord la recherche est totalement organique pour notre application, comme je suis sûr qu'elle l'est pour beaucoup d'autres. Nous n'avions même pas mentionné la recherche dans notre processus d'onboarding ! Une fois que nous avons remarqué cette tendance, nous avons décidé d'ajouter une superposition dans le processus d'onboarding. Les nouveaux utilisateurs peuvent mieux comprendre et utiliser la recherche. Nous développons cette fonctionnalité en ce moment même !

La recherche est également très importante pour **fidéliser** les utilisateurs. Si je n'arrivais pas régulièrement à trouver des détaillants ou des articles spécifiques que je cherchais, **je** serais frustré.

La pire chose que votre recherche puisse faire est de produire une page blanche. Et la chose la plus facile à faire avec une application est de la supprimer.

**Vous voulez afficher des résultats.** Pouvez-vous imaginer Google ne retournant aucun résultat pour la majorité de ses mots-clés ? Vous remarquerez que même si vous ne trouvez pas quelque chose qui **correspond exactement** à votre recherche Google, ils trouveront quelque chose à vous montrer. Et leur système est si bien conçu que vous trouverez probablement ce que vous cherchiez après quelques liens ou recherches.

Il y a quelques clés pour éviter les pages blanches :

* Vous pourriez commencer par corriger les fautes d'orthographe ou les erreurs de l'utilisateur pour lui (« Voulez-vous dire... ? »). Vous pourriez également les autocorriger en son nom.
* Assurez-vous d'identifier leur intention. Que voulaient-ils rechercher ? Quel est le problème qu'ils essaient de résoudre avec cette requête ? Y a-t-il une autre façon de le formuler ou un autre chemin vers la solution ?

Au minimum, vous devez leur montrer **quelque chose** que vous pensez qu'ils pourraient trouver intéressant.

Les clés pour remplir la page de recherche, et finalement trouver ce que la personne cherche dans la base de données de recherche, nécessitent de lier deux éléments ensemble : la **récupération** et la **pertinence**.

### Qu'est-ce que la récupération ?

Le processus de récupération signifie trier toute la base de données de recherche et réduire la recherche à un ensemble plus spécifique d'articles.

Chez Flipp, cela signifie passer de milliers d'articles à 100 articles les plus susceptibles de correspondre à la recherche de la personne. Nous utilisons [Apache Solr](https://lucene.apache.org/solr/), qui indexe tous les articles et les commerçants dans une couche de cache.

Solr nécessite que l'équipe Flipp saisisse le nom de l'article et ses attributs. Par exemple, cela pourrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/qploW7Uh9aQ6XqIAOtapu3Nsoxp4J1j8IgxP)

Solr indexe chaque article et leurs champs respectifs, et recherche dans tous ces champs pour trouver l'article qui correspond le plus à votre requête. Dans cet exemple particulier, nous avons utilisé le « nom de l'article », le « nom de la marque » et le « commerçant ». Mais cela pourrait être la « catégorie », la « description », et bien d'autres attributs différents.

Cela semble assez simple, n'est-ce pas ?

La recherche se complique très rapidement.

Par exemple, si quelqu'un tape « TV » dans la recherche, il s'attend à voir un véritable écran de télévision. Le problème est qu'il existe de nombreux accessoires pour les téléviseurs — tables, étagères, supports, etc.

L'utilisateur veut voir un écran de télévision, donc ces accessoires ne seraient pas pertinents. Nous devons nous assurer que Solr comprend l'intention de recherche lors de la récupération des articles pour l'utilisateur. À cette fin, Solr utilise les mécanismes suivants :

* **Boosting.** Il s'agit du processus de pondération de chaque attribut des articles afin qu'un attribut ait la préséance sur l'autre. Par exemple, le nom d'un produit est plus pondéré que sa description.
* **Synonymes.** Ce sont des mots qui désignent le même produit mais qui sont orthographiés ou référencés différemment. Un bon exemple serait « tv » et « télévision ». Lors d'une requête, Solr doit renvoyer les mêmes résultats pour les deux termes.
* **Tokenization.** Cela fait référence à la tokenisation d'un mot et à la génération de parties de mots basées sur divers délimiteurs. Par exemple, il ne devrait y avoir aucune différence dans les résultats renvoyés pour des requêtes comme « X-box », « X box » ou « XBox ».

### Qu'est-ce que la pertinence ?

Après que le processus de récupération a extrait 100 articles parmi des milliers, le processus de pertinence suit. Le processus de pertinence décide comment trier ces 100 articles de la base de données. Il détermine l'ordre.

#### _Lequel affichons-nous en premier ?_

Gardez à l'esprit la statistique dont nous avons parlé au début de l'article. Elle indique que **la plupart des gens ne regardent pas au-delà des dix premiers articles**.

Bien que l'application Flipp n'ait pas de pagination, nous avons remarqué que la plupart des gens ne regardent pas au-delà des premiers articles. Nous organisons cet ordre d'articles selon les préférences de l'utilisateur ou les signaux reçus pour le comportement de l'utilisateur. Pour ce faire, nous utilisons quatre algorithmes différents :

#### **Curation par la foule**

Il s'agit d'un facteur qui trie les articles par popularité à ce moment-là. Les articles qui ont le plus de clics par les utilisateurs au cours des 30 derniers jours sont placés en haut. Nous attribuons un poids plus important à la récence. Mon collègue Thanesh [écrit plus sur la curation par la foule ici](https://medium.freecodecamp.com/how-crowd-curation-improved-our-search-quality-by-27-84d500e751bc).

#### **Curation par catégorie**

Il s'agit d'un facteur qui trie les articles par catégorie. Par exemple, hypothétiquement, « TV » correspond à « électronique » et « systèmes de divertissement à domicile ». Il y aura des moments où l'utilisateur voudra voir des articles connexes, et d'autres moments où il ne le voudra pas, donc nous ne voulons pas disqualifier complètement ce facteur. Les catégories d'articles qui correspondent à la catégorie de la requête de recherche sont mises en avant.

Par exemple, une recherche pour « TV » afficherait les articles dans « TV/systèmes de divertissement à domicile » plus haut, et les articles étiquetés comme « accessoires » plus bas. Sans la curation par catégorie, les accessoires de TV seraient regroupés avec les écrans de TV, et nous devrions limiter la récupération de ces articles, ce qui exclurait les utilisateurs intéressés à la fois par les accessoires et les écrans.

Les deux premières images ci-dessous montrent l'effet de la curation par catégorie où une requête pour « oranges » afficherait également des jus d'orange comme résultat, cependant après avoir appliqué la curation par catégorie (3ème image), nous voyons que seules les oranges sont mises en avant comme résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/q80-1SJxhbErbD-xsvuqIpcJLdBqranVyvSc)

**Le score Solr** considère la pertinence comme un problème de probabilité. Un score de pertinence devrait refléter la probabilité qu'un utilisateur considère le résultat pertinent, la récupération d'informations probabiliste. Pour ceux qui s'intéressent à la manière dont ce score est calculé, ils peuvent se référer aux détails [ici](https://en.wikipedia.org/wiki/Okapi_BM25).

Le score cumulatif d'un article est calculé en mettant à l'échelle et en accumulant les scores individuels de curation par la foule et par catégorie, plus le score Solr.

**Le traitement postérieur des termes négatifs** fait référence à la rétrogradation des termes négatifs associés aux requêtes de recherche. Les résultats de recherche qui contiennent ces termes négatifs ne sont soit pas récupérés, soit affichés à la toute fin des résultats de recherche classés.

Par exemple, « Coffee » est un terme de recherche populaire. Par défaut, une recherche pour « coffee » obtiendrait également certaines tables à café populaires. Nous définirions le mot « table » dans « coffee table » comme un terme négatif. Parce que les personnes cherchant du café ne cherchent probablement pas de la décoration de salon. Cela rétrograde toutes les tables à café dans les résultats de recherche.

### Réflexions finales

C'est drôle de voir comment quelque chose d'aussi simple que la recherche peut rapidement devenir si compliqué. Ce n'est qu'un petit aperçu de la réflexion qui entre dans notre recherche et notre produit. Merci d'avoir lu ! Espérons que vous pourrez utiliser certaines des idées des processus de récupération et de pertinence pour améliorer la recherche de votre logiciel.

Sur une note connexe, cela pourrait vous donner une idée de pourquoi des choses comme les [bulles de filtres](https://www.ted.com/talks/eli_pariser_beware_online_filter_bubbles) émergent lorsqu'il s'agit de moteurs de recherche. Nous essayons de vous aider à trouver ce que vous voulez. Et en raison de l'attention limitée de la plupart des gens, nous n'avons pas le temps de vous montrer des choses que vous ne voulez peut-être pas.

Je suis Faizan, un ingénieur de données chez [Flipp](https://flipp.com/). Si vous êtes intéressé à réinventer la façon dont les gens achètent des choses, jetez un coup d'œil à [notre blog d'ingénierie](http://eng.flipp.com/) et à nos [offres d'emploi actuelles](https://corp.flipp.com/jobs).