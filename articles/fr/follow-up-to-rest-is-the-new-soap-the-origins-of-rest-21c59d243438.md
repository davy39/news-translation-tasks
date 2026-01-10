---
title: 'Voici ma suite à REST est le nouveau SOAP : parlons du REST Original'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T18:59:55.000Z'
originalURL: https://freecodecamp.org/news/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a68QxzlHe3e3THOyKV9m8w.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: REST
  slug: rest
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Voici ma suite à REST est le nouveau SOAP : parlons du REST Original'
seo_desc: 'By Pakal de Bonchamp

  I’ve read the philosophical dissertations, so you don’t have to!

  I expected my recent article (or “hipsteresque drunken rant,” as some called it),
  to get a barrage of criticism, under the motto “you haven’t understood anything
  ab...'
---

Par Pakal de Bonchamp

**J'ai lu les dissertations philosophiques, pour que vous n'ayez pas à le faire !**

Je m'attendais à ce que mon [article récent](https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d) (ou « rant d'ivrogne hipster », comme certains l'ont appelé), reçoive une volée de critiques, sous la devise « vous n'avez rien compris à REST ». C'est effectivement ce qui s'est passé.

Mais cela a également déclenché des débats intéressants, notamment sur [Reddit](https://www.reddit.com/r/javascript/comments/7k2kv2/rest_is_the_new_soap_pakal_de_bonchamp_medium/?st=jb8hbpsd&sh=1a3a371e) et sur [Hacker News](https://news.ycombinator.com/item?id=15937448). Cela a également touché une corde sensible chez de nombreux développeurs, qui se sentaient comme des hérétiques pour douter de l'omnipotence de REST.

Pour citer un [résumé particulièrement perspicace](https://news.ycombinator.com/item?id=15938460) du ressentiment :

> _Une simple spécification d'API RPC prend quelques minutes à définir. « Restifier » prend beaucoup plus de temps, il y a un million de petits pièges, pas de véritable standard. Chacun a une opinion différente sur la manière de le faire._

> _Les données sont réparties entre les verbes, les URLs, les paramètres de requête, les en-têtes et les charges utiles. Tout le monde pense que tout le monde ne « comprend » pas REST. Si vous essayez de suggérer autre chose que REST au bureau, vous devenez le sujet d'une chasse aux sorcières. C'est vraiment un culte du cargo de l'inutilité._

> _Mes collègues ont passé tellement de temps à essayer de faire générer correctement la documentation par Swagger ainsi que les API côté client, et il y a d'innombrables pièges que nous traitons encore. C'est vraiment SOAP 2.0, alors qu'un simple protocole JSON/RPC aurait fait l'affaire._

> _Ne me lancez pas sur la confusion entre les erreurs du serveur HTTP et les erreurs de l'application. Et essayer de faire des requêtes de type action avec un état d'esprit optimisé pour CRUD. Combien de temps avons-nous perdu à déterminer la manière « standard » de faire simplement un appel d'API de connexion RESTful._

De l'autre côté, Phil Sturgeon, l'un des principaux défenseurs de REST, a publié un [article de réponse](https://philsturgeon.uk/api/2017/12/18/rest-confusion-explained/) (voir mes [commentaires rapides ici](http://disq.us/p/1oy9a9l)). Je suis heureux que nous ayons convenu de certains points importants, notamment que de nombreuses API devraient en réalité être RPC, au lieu de se terminer en travaux de rustine pseudo-REST.

À la lumière de tous ces retours, j'ai modifié mon essai initial à plusieurs reprises, et maintenant un nouvel article semble nécessaire pour clarifier les points restants.

Je tiens à m'excuser à l'avance si l'audace de ce post est perçue comme de la rudesse. Considérant la nocivité de la situation, je n'ai malheureusement pas pu me contenter d'un ton paisible. Aucune offense personnelle n'est intended de quelque manière que ce soit. Alors, passons à autre chose.

### Plusieurs nuances de REST

Une difficulté du sujet est qu'il existe plusieurs concepts derrière le terme « REST ».

1) Le Livre Fondateur de REST, c'est-à-dire [la dissertation de Roy Fielding](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)   
2) Les milliers de blogs/podcasts des défenseurs de REST (comme ceux de Phil Sturgeon), disséminés sur le Web, et expliquant « comment faire du REST correctement »  
3) Les milliards de services web (auto-proclamés) RESTful, exposés publiquement ou privément sur tout l'Internet

Ma tirade traitait principalement du **#3** : les API RESTish qui gaspillent le temps de tout le monde, pour des bénéfices encore à démontrer. Et même après avoir lu des centaines de commentaires, je dois maintenir ma position : ces API que j'ai rencontrées partout réinventent constamment la roue, ne tirent même pas parti des avantages que la sémantique HTTP pourrait apporter (cache côté client, négociation de contenu, verrouillage optimiste…), et sont une douleur longue à intégrer.

L'article de réponse de Phil Sturgeon a mis en lumière la principale raison de cet épitome de l'inutilité :

> « Les gens partout construisent des API RESTish qui sont essentiellement juste du RPC + des verbes HTTP + des URLs jolies. »

En chemin, nous avons évoqué **#2** à travers quelques citations de défenseurs de REST. Pour le reste, autant que j'ai vu, les blogueurs/podcasteurs REST se sont souvent contredits. Ils ont donné des instructions qui sonnaient plus comme des goûts que des leçons de sagesse, ont évité les questions les plus importantes, et ont fait une vertu de ne pas étayer, avec des exemples et des démonstrations, leurs arguments les plus audacieux : « RPC cause un travail redondant », « REST est nécessaire pour des API durables des décennies », et bien sûr le (in)fameux « Le client n'a pas besoin de connaissance préalable du service pour l'utiliser. »

Je n'ai pas encore croisé une simple page de prose résumant comment HATEOAS fonctionne _réellement_, et quels défis il résout pour nous. C'est un problème en soi.

À propos des contradictions… voici une anecdote. Lorsque j'ai présenté une API simple (et doucement orientée CRUD), c'était juste pour montrer le nombre anormal de questions qui devaient être répondus juste pour la RESTifier. Et pourtant, de nombreux commentateurs ont senti le besoin d'expliquer, avec une documentation verbeuse, comment ILS spécifieraient cette API.

Cela a abouti à de nombreux protocoles similaires mais incompatibles, certains tissant des standards ensemble, certains réinventant la pierre taillée, et certains allant jusqu'à spécifier un type MIME versionné par point de terminaison de ressource (comme « application/vnd.my-rest-api.v1.account-search-result+json »).

Phil Sturgeon a également répondu, dans son article de réponse, à ces questions semi-rhétoriques. Les recommandations livrées avaient du sens et semblaient « à jour ». Mais elles contredisaient directement les enseignements passés ou présents de nombreux autres partisans de REST (ainsi que les commentateurs cités ci-dessus) sur divers sujets : champs clairsemés, documents composés, formats PATCH, charges utiles DELETE, et ainsi de suite.

Au moins, tout cela a prouvé un point : lorsque les choses doivent être faites rapidement et consensuellement, REST n'est pas la meilleure voie à suivre. Pourtant, beaucoup ont affirmé que j'attaquais des « idées fausses » de REST, et m'ont dirigé vers cette ou cette citation de la dissertation originale. C'était une manière de dire que la « théorie » était bonne, même si la « pratique » était défectueuse. « Oui, c'est vrai, le communisme affirme la même chose », pourrait-on argumenter.

![Image](https://cdn-media-1.freecodecamp.org/images/DIOnmqtsew2du2MQ-H9Rx67Y7kny0XF6oI4y)
_Comment *certains* défenseurs de REST voient sa Thèse Fondatrice_

Le débat sur le fait qu'une pratique soit RESTful ou non est devenu un gag récurrent dans l'écosystème du développement web. Cependant, pour l'honneur intellectuel, il était en fait intéressant de revenir à la définition la plus autoritaire de REST™ telle que donnée par la dissertation **#1** et les articles connexes. C'est au moins pour comprendre comment ce battage a commencé, et ce qui peut être sauvé de tout cela.

J'espère que les résumés ci-dessous seront jugés suffisamment fidèles aux originaux. Sinon, je vous invite à me faire part de vos retours sur d'autres « idées fausses » qu'ils pourraient contenir.

### Qu'est-ce que le REST™ Original au fait ?

La [dissertation](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438) de Roy Fielding, publiée en 2000, est naturellement longue (180 pages), donc elle n'est probablement pas largement lue parmi les développeurs web.

Voici un aperçu de son contenu. En alternative, vous pouvez également lire les chapitres d'Introduction et de Conclusion de ladite dissertation.

* Le chapitre 1 définit les termes liés à l'architecture comme les éléments, les composants, les propriétés, les styles, les motifs, et ainsi de suite.
* Le chapitre 2 liste les propriétés clés pour une architecture basée sur le réseau : performance perçue par l'utilisateur, efficacité du réseau, évolutivité, modifiabilité, visibilité et fiabilité.
* Le chapitre 3 classe les styles architecturaux existants (Pipe et Filtre, Cache, Client-Serveur, Code à la Demande), et montre leurs avantages et inconvénients concernant les propriétés clés ci-dessus.
* Le chapitre 4 résume les exigences de l'architecture du World Wide Web (Barrière d'Entrée Basse, Extensibilité, Hypermédia Distribué, Évolutivité Anarchique et ainsi de suite), et explique pourquoi un style architectural dédié est nécessaire pour guider son développement, notamment pour évaluer les extensions proposées avant leur déploiement.
* Le chapitre 5 présente le style architectural REST : les styles existants dont il dérive, ses éléments architecturaux (Ressources et leurs Identifiants, Représentations, Connecteurs, Composants, et ainsi de suite), et comment tout cela fonctionne ensemble concernant les processus et les données.
* Le chapitre 6 donne un retour d'expérience sur la manière dont REST a été utilisé pour guider le développement des standards de protocoles Web (URIs, HTTP et ses nombreuses fonctionnalités et extensions), où il a échoué à être appliqué (cookies, mélange de différentes préoccupations dans les en-têtes, IDs utilisateur dans les URIs, et ainsi de suite), et les leçons architecturales à tirer de l'architecture Web moderne.

![Image](https://cdn-media-1.freecodecamp.org/images/RICSoTTSIx3hE6WbMEFyh-UHXdYMFmPLLxGe)
_Le livre « Une introduction à REST : Tome 1 »_

Que retirons-nous de cette dissertation, en dehors des habituelles [contraintes REST](http://whatisrest.com/rest_constraints/index) ?

Premièrement, comme prévu pour l'**introduction d'un « style architectural »**, elle dit presque rien sur les méthodes HTTP, les schémas, la gestion des erreurs, la versioning, et tous ces sujets concrets qui façonnent les services web du monde réel. C'est pourquoi des centaines d'opinions contradictoires ont coulé pour remplir le vide, et c'est pourquoi il est étrange d'entendre parfois que REST est « précisément spécifié » par cette dissertation.

Deuxièmement, REST a été formalisé pour donner une **colonne vertébrale théorique au développement du World Wide Web**. Il mélange de nombreux styles architecturaux existants, et hérite de leurs avantages et inconvénients, dans le but de concevoir un **système hypermédia distribué à l'échelle d'Internet**.

**Et cela fonctionne.**

* Sur le web, nous sommes heureux que toutes les pages web parlent HTTP, s'affichent avec un GET, et gèrent les formulaires avec GET ou POST [Interface Uniforme]
* Sur le web, nous sommes heureux que notre navigateur comprenne des centaines de types de contenu (HTML, images, CSS, polices, Javascript, RSS…), et les gère selon de nombreuses règles intégrées (cache, affichage, sécurité…). [Messages Auto-Descriptifs]
* Sur le web, nous sommes heureux d'avoir le cache dans le navigateur, les réseaux de diffusion de contenu, et d'autres formes de caches partagés, aidant à accélérer le temps de chargement et à absorber les pics de trafic (comme les « effets Slashdot »). Même si un rapide ctrl+F5 est parfois nécessaire pour corriger les comportements étranges des pages web. [Système en Couches & Cache]
* Sur le web, nous sommes heureux que les proxies et les pare-feux comprennent les protocoles web, et les laissent circuler, tout en bloquant les connexions TCP/UDP douteuses. [Visibilité]
* Sur le web, nous sommes heureux que les scripts puissent être livrés par le serveur pour chaque page, puisque les navigateurs, par eux-mêmes, n'ont aucune idée de la manière d'ajouter de la dynamique au HTML fourni [Code-à-la-Demande]

Un point [évoqué mais non détaillé dans la dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_5) est « **Hypermedia As The Engine Of Application State** » **(HATEOAS)**. Dans des articles complémentaires, Roy Fielding a expliqué le concept de « contrôles hypermédia », également appelés « affordances » : une sorte de liens glorifiés, annonçant au client « ce qu'il peut faire ensuite ». Et il a déclaré (un peu tard ?) que ceux-ci ne sont pas de simples options, mais que HATEOAS est au cœur même de REST.

> Lorsque je dis Hypertexte, je veux dire … La présentation simultanée d'informations et de contrôles de sorte que l'information devient l'affordance à travers laquelle l'utilisateur obtient des choix et sélectionne des actions. L'hypertexte n'a pas besoin d'être du HTML sur un navigateur : les machines peuvent suivre des liens lorsqu'elles comprennent le format de données et les types de relations ([source](http://roy.gbiv.com/talks/200711_REST_ApacheCon.pdf)).

> _Informations et actions, affichées à un utilisateur à travers un format auto-documenté d'awesomeness, avec une sélection de liens qui transforment un client bien réglé en un crawler au lieu d'être simplement un échange CRUD… eh bien, c'est tout le but de REST ([source](https://blog.apisyouwonthate.com/representing-state-in-rest-and-graphql-9194b291d127))._

> _Naturellement, c'est là que je dois expliquer pourquoi « hypermedia as the engine of application state » est une contrainte REST. Pas une option. Pas un idéal. Hypermedia est une contrainte. En d'autres termes, vous le faites ou vous ne faites pas de REST ([source](https://www.infoq.com/articles/roy-fielding-on-versioning/))._

> _Une API REST devrait être entrée sans connaissance préalable au-delà de l'URI initial (signet) et d'un ensemble de types de médias standardisés qui sont appropriés pour le public visé (c'est-à-dire, attendus pour être compris par tout client qui pourrait utiliser l'API) ([source](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven))._

Concernant cet aspect également, le Web semble RESTful. À partir de la page d'accueil d'un site web, les utilisateurs et les webspiders sont capables de le naviguer sans effort, et de gérer les médias associés (images, feuilles de style, scripts, etc.) qui sont découverts en cours de route. Bien que les URLs changent avec le temps et que des formulaires soient ajoutés et supprimés, les sites web n'ont pas besoin de numéros de version, et c'est très bien.

![Image](https://cdn-media-1.freecodecamp.org/images/8TXoDNwDHiJFQU4enox2C8z7PLnmBhzPlty8)
_Quand j'ai réalisé que le principal exemple de HATEOAS était simplement le world wide web_

Nous voyons ainsi que le REST™ original est un style architectural puissant, offrant un grand contrôle aux serveurs sur leurs clients, et proposant un écosystème explorable d'hypermédia éditable.

Maintenant, qu'en est-il de vos API ? Visent-elles également à être des « systèmes hypermédia distribués à l'échelle d'Internet » ?

### Le Saint Graal hasardeux et (souvent) inutile

Vous avez peut-être entendu parler du [Modèle de Maturité de Richardson](https://martinfowler.com/articles/richardsonMaturityModel.html). Il évalue le niveau de RESTfulness de votre API, selon qu'elle utilise des ressources appropriées (Niveau 1), des verbes (Niveau 2), et des contrôles hypermédia (Niveau 3). Ce modèle peut vous donner l'impression que certaines de vos API « RESTish » sont destinées à évoluer sur ces « étapes vers la gloire de REST » (comme le décrit Martin Fowler). Mauvaise nouvelle, cela ne se produira probablement pas.

Oui, vous pouvez simuler la RESTfulness en mappant vos fonctions serveur aux URLs des Ressources. Oui, vous pouvez la simuler davantage en mappant vos opérations aux verbes HTTP les plus proches. Mais lorsque vient le temps d'atteindre le niveau final, d'avoir vraiment une application auto-descriptive, explorable, pilotée par hypermédia, vous devrez réaliser la dure vérité : votre API n'est pas RESTful, elle ne l'a jamais été, et elle ne le sera jamais. Elle a en réalité moins de chances d'atteindre la « Vraie RESTfulness » qu'une limace d devenir un papillon.

Vous souvenez-vous des citations de Roy Fielding dans la section précédente ? Sa définition de REST est entièrement axée sur HATEOAS. Mais c'est une déclaration extrêmement ambitieuse.

Cela signifie que vous devez oublier les types MIME sans signification comme « text/xml » ou « text/json », et utiliser des types de contenu spécifiques, soutenus par des contrats, et reconnaissables par les consommateurs d'API. Cela signifie que, sauf si un protocole RESTful complet existe déjà pour votre cas d'utilisation précis, vous devrez écrire des brouillons de style RFC/IETF pour décrire la sémantique de vos types de contenu spécifiques. Vous devrez concevoir un système hypermédia activé par crawler, et spécifier la signification de ses diverses « affordances ». Et vous devrez probablement fournir des implémentations client à vos clients, dans leurs propres langages de programmation, puisqu'ils ont d'autres choses à faire que de suivre de telles entreprises herculéennes.

Tout cela représente un énorme travail de spécification et d'implémentation. Pour des bénéfices plutôt légers. Et des inconvénients préoccupants.

Oui, cela permet aux développeurs côté serveur de garder le contrôle de leur structure d'URL sans redirections (_aujourd'hui je renomme « users/ » en « accounts/ » — c'est plus fluide_), mais à quel coût ? À moins que vous ne génériez constamment de nouvelles URLs pour l'éviter, je parie que vos consommateurs d'API coderont en dur les URLs de toute façon, pour éviter cette couche supplémentaire de complexité (reconnaissance des affordances, cache de traversée d'URL, etc.)

Oui, cela permet au serveur de contrôler les actions disponibles, lorsque le consommateur final est un humain. Mais qu'en est-il de l'Expérience Utilisateur ? Le fait que le serveur montre et masque arbitrairement les affordances est un concept effrayant. Lorsque un bouton « supprimer » est manquant sur une [SPA](https://en.wikipedia.org/wiki/Single-page_application), je veux savoir pourquoi. Et si je demande à mon programme REST-crawler de créer cette ressource, je préfère qu'il échoue avec un message d'erreur distant approprié, plutôt que de dire « désolé, je n'ai pas trouvé l'affordance pour cela ». Les actions peuvent être empêchées par des règles de sécurité, des dépendances manquantes, des tâches concurrentes, et d'autres problèmes. Nous avons le droit de savoir ce qui se passe, et les « affordances », dans leur forme actuelle, manquent cette fonctionnalité cruciale.

De plus, qu'en est-il des interactions machine-à-machine ? Si l'évolutivité de l'API est clé, comment le programme consommateur comprend-il les nouveaux champs et les nouvelles affordances ? Roy Fielding [répond](https://www.infoq.com/articles/roy-fielding-on-versioning/) « C'est là que le code-à-la-demande brille ». Non. Il n'est pas question que vous injectiez dynamiquement votre code distant dans mon programme Python de sitôt.

Après avoir lu des centaines de pages sur le sujet REST/HATEOAS, je n'ai rarement été aussi peu impressionné. Atteindre le NIVEAU 3 de RESTfulness était censé être une épiphanie. J'ai plutôt le profond sentiment que le remède est pire que la maladie.

Maintenant, certaines personnes soutiennent que Roy Fielding pousse le concept trop loin, que le « **REST léger** » (c'est-à-dire « Niveau de Maturité de Richardson 2 », sans Contrôles Hypermédia) est le vrai but à atteindre.

Mais malgré tout, je parie que vous n'avez en réalité besoin d'aucun de cela.

* Vous (très probablement) ne voulez pas de code-à-la-demande. Vous voulez que vos clients lisent vos spécifications, et appellent votre API précisément comme vous (et eux) l'entendez.
* Vous (très probablement) ne voulez pas de visibilité au niveau du réseau. Au contraire, vous voulez autant de chiffrement TLS que possible.
* Vous (très probablement) ne voulez pas de caches partagés ou de cache côté client. Au contraire, les caches distants sont parmi vos pires ennemis. Et si vos consommateurs d'API ne sont pas des navigateurs, ils ignorent typiquement les en-têtes de cache de toute façon.
* Vous (très probablement) pouvez vous passer de la négociation de contenu, et d'autres fonctionnalités HTTP plus ou moins regroupées avec les meilleures pratiques REST (vous savez, pour la Représentation versus la Ressource). Chaque langage à jour peut comprendre des formats comme Xml et Json.
* Vous (très probablement) ne voulez pas exposer des Ressources pour des opérations CRUD, et utiliser ces hommes du milieu maladroits pour déclencher des opérations réelles dans vos applications.

Tout ce que vous (très probablement) voulez, c'est exposer un ensemble de vos fonctionnalités côté serveur à des navigateurs ou serveurs distants. De manière rapide, élégante, robuste.

**Votre API (très probablement) crie « RPC ». Et dans ce cas, même une chausse-pied de la taille d'un gratte-ciel ne permettra pas de l'adapter au très ambitieux, mais rarement pertinent, Style Architectural REST.**

Bien sûr, vous pourriez avoir besoin de cette ou cette propriété de HTTP. Par exemple, vous pourriez vouloir utiliser la méthode GET et différentes URIs pour vos opérations en lecture seule originaires d'Ajax afin de bénéficier du cache côté navigateur. Ou vous pourriez vouloir exposer votre base de données comme CRUD-sur-HTTP pour tirer parti des implémentations génériques (comme les clients de style Active Record pour le protocole JsonAPI).

Mais quels que soient vos besoins, _la vie est courte_. Vous n'avez pas besoin de commencer par un ensemble abstrait de « directives » comme les contraintes REST. Vous feriez mieux de chercher un **protocole clé en main**, correspondant aux besoins que vous avez vraiment.

Il existe des tonnes de telles solutions (principalement non-RESTful), pour le RPC léger, le CRUD, le pub/sub, les files d'attente de travaux, les systèmes de fichiers distants, l'interrogation/filtrage de données, le calcul haute performance, et la messagerie bidirectionnelle. Rarement, vous devrez innover — ajouter de nouvelles capacités à un protocole, ou utiliser des approches hybrides. Mais commencer à « transformer les verbes en noms » ou suivre des principes abstraits comme des dogmes est la dernière chose que vous devez faire.

Veuillez noter, au passage, que le CRUD peut également être fait comme un simple sous-ensemble de RPC. Les services web ne sont généralement plus codés en langage C, donc si vous voyez un autre errant argumenter que « c'est horrible d'avoir à coder autant de fonctions CRUD de base », veuillez les éclairer avec cette API de haute technologie.

```
create(type, **params) -> id
retrieve(type, id, **params)
update(type, id, **params)
delete(type, id, **params)
```

En chemin (très probablement) sans REST, vous rencontrerez des dizaines de discours intransigeants, affirmant que seul REST peut vous garantir l'évolutivité et la longévité. Il y a peu besoin de réfuter ce qui n'a jamais été prouvé. Tout ce que je peux juger, d'après mon expérience personnelle, c'est que :

* Une base de données bien configurée et un simple cache côté serveur suffisent pour 99 % des services web ; une vieille sagesse dit _l'optimisation prématurée est la racine de tous les maux_.
* Les services évoluent continuellement. Que cela signifie un nouveau paramètre dans une procédure distante ou un nouveau champ dans une représentation de ressource, cela n'a pas beaucoup d'importance. Et le concept de [l'Évolution de l'API](https://blog.apisyouwonthate.com/api-versioning-has-no-right-way-f3c75457c0b7#API%20Evolution) est, autant que j'ai lu, rien d'autre que la vieille sagesse du développement logiciel : ne faites pas de changements cassants jusqu'à ce que ce soit absolument nécessaire, et utilisez des couches de compatibilité pour aider tout le monde à avancer à un rythme sain.
* Même si vous concevez votre API de manière maladroite, elle sera certainement morte loooong avant d'avoir de réels problèmes de compatibilité. Peut-être pas parce que son but est devenu irrelevant, et peut-être pas à cause de concurrents écrasants, mais probablement à cause de changements d'avis dans votre département marketing.
* Avec le temps passé à intégrer correctement la plupart des API de style REST, on pourrait implémenter plusieurs versions successives de services web RPC légers correspondants. Restons pragmatiques.
* Lorsqu'une startup technologique, avec une espérance de vie inférieure à 2 ans, passe un tiers de son temps à écrire du REST(ish) de base, son CTO mérite peut-être d'être giflé avec une grosse truite. Les bonnes pratiques de programmation et les solutions de contournement peu coûteuses sont tout ce dont ils ont besoin, jusqu'à ce qu'ils atteignent l'état où l'évolutivité devient une question digne de réflexion et de dépenses.

Plus important encore, veuillez abandonner cette Quête du Saint Graal appelée « HATEOAS », sauf si vous faites partie des quelques Chevaliers dans le monde concernés par cette Mission.

REST/HATEOS est pour les API spécifiques centrées sur les données : celles qui sont naturellement CRUD, celles qui sont consommées via des motifs ActiveRecord ou DataMapper dans vos langages préférés, celles qui n'ont pas des tonnes de contraintes subtiles et d'effets secondaires entre les champs d'un modèle, et celles destinées à être explorées par des humains (actuellement les seules entités dans l'univers capables de comprendre ce que ce champ « email de contact de facturation » nouvellement apparu signifie).

Sinon, vous finirez par avoir l'inadéquation des API RESTish, mais avec une pile supplémentaire de complications.

![Image](https://cdn-media-1.freecodecamp.org/images/3hlZJG4kPDdGKmn7yyoOFW-Yq8V4AIVsueyM)
_Quand il est utilisé de manière inadéquate, REST est comme « Monty Python et le Saint Graal », mais avec des milliers de lapins_

Un cas d'utilisation pertinent pour HATEOS serait un protocole générique « Admin de Base de Données », permettant à n'importe quel serveur de piloter une même application monopage générique à travers la structure de sa base de données (SQL ou no-SQL) : navigation entre les tables et les pages d'enregistrements, formulaires autogénérés pour chaque schéma, boutons de création/édition/suppression dynamiques, et ainsi de suite.

De manière similaire, une API dédiée à la navigation et à l'édition de documentation, ou à l'exploration/tirage/poussée d'un Système de Contrôle de Version, se prêterait bien à un style architectural REST. Mais celles-ci sont loin, très loin, de ce pour quoi la plupart des services web sont construits. Et si [Github est passé de REST à GraphQL](https://githubengineering.com/the-github-graphql-api/) pour son API, c'est un indice que les bénéfices revendiqués par REST étaient juste _insuffisants_.

### **Où cela a-t-il mal tourné ?**

Nous voici donc. REST/HATEOS est certainement un style architectural bien évolué, mais (à mon avis) pertinent seulement pour une infime fraction des cas d'utilisation. Et maintenant, il s'est répandu comme un cancer sur l'écosystème des services web — principalement sous sa forme tronquée appelée « API RESTish » — apportant l'inadéquation et la complexité artificielle partout.  
   
Qui est à blâmer pour cette situation embarrassante ?

* La dissertation originale, qui n'a pas positionné REST par rapport à d'autres architectures, et est restée trop vague sur ses avantages et inconvénients ?
* Les défenseurs de REST, qui se sont souvent perdus dans des recommandations très subjectives (quand elles n'étaient pas contradictoires), au lieu de promouvoir des standards et d'expliquer quand (ne pas) utiliser REST ?
* Les innombrables articles qui ont présenté un faux dilemme entre SOAP et REST, propulsant ainsi vers les étoiles un gagnant par défaut ?
* Les trolls d'Internet qui ont proclamé, dans à peu près chaque fil de discussion StackOverflow concernant la conception de services web, « Oubliez le protocole XYZ existant, c'est une couche supplémentaire qui rend les choses non maintenables, tout ce dont vous avez besoin est du HTTP fait main » ?
* Les amateurs de buzzwords qui ont imposé REST à leurs équipes, sans discuter des impacts de ce changement architectural, sans jamais se demander « mais pourquoi donc ? »
* La masse silencieuse de développeurs, qui, comme moi, savent DEPUIS DES ANNÉES que quelque chose n'allait pas du tout, mais n'ont pas sonné l'alarme ?

![Image](https://cdn-media-1.freecodecamp.org/images/N42-nijzWSHyLEQCHFSL7nNNQops1B0Qhj2Y)

Oui. Je suppose que c'est un mélange de tout cela.

L'ironie cruelle de cette histoire est que la [dissertation originale](https://www.ics.uci.edu/~fielding/pubs/dissertation/introduction.htm) elle-même mettait en garde contre le saut sur le wagon et les choix architecturaux inappropriés :

> « Combien de fois voyons-nous des projets logiciels commencer par l'adoption de la dernière mode en matière de conception architecturale, et seulement plus tard découvrir si les exigences du système appellent à une telle architecture. La conception par buzzword est un phénomène courant. […] L'interface REST est conçue pour être efficace pour le transfert de données hypermédia à gros grains, optimisant pour le cas courant du Web, mais aboutissant à une interface qui n'est pas optimale pour d'autres formes d'interaction architecturale. »

Cependant, une bonne nouvelle est que REST a ouvert la voie à d'autres protocoles, comme GraphQL et HTTP2. Et son utilisation de fonctionnalités HTTP avancées est une inspiration pour d'autres architectures. Nous lui devons au moins cela.

### Que faire si vous *devez vraiment* RESTifier ?

Pour de nombreuses raisons (comme la hiérarchie de l'entreprise, ou avoir vraiment besoin de CRUD avec cache HTTP), vous pourriez devoir opter pour REST. Avec ou sans HATEOAS.

Dans mon article précédent, j'ai suggéré que l'industrialisation des clients et serveurs REST était un problème sans solution. **Il s'avère que je me trompais**_._

Voici une liste non exhaustive de « standards » liés à REST, tirée des contributions de divers commentateurs. Vous pouvez en trouver beaucoup plus sur la nouvelle liste [standards.rest](http://standards.rest/) de Phil Sturgeon.

* Pour spécifier la sémantique de PATCH : JSON Patch, JSON Merge Patch
* Pour spécifier les contrats d'interface : JSON Schema, API Blueprint, OpenAPI (anciennement Swagger), RAML, GraphQL Types, XML Schema
* Pour séquentialiser les résultats et/ou les erreurs dans les réponses : Format JSend, RFC7807 (Détails des Problèmes pour les API HTTP), Ensembles de champs clairsemés (restreignant les champs à retourner), Documents composés (incluant les ressources associées)
* Protocoles avec contrôles hypermédia : JSON Hyper-Schema (Brouillon IETF), JSON Hypertext Application Language ou « HAL » (Brouillon IETF), Json-API, OData, Mason, Hydra/JSON-LD, JSON SIREN

Ce sont en effet un bon nombre de possibilités. Une explosion combinatoire de possibilités, puisque beaucoup d'entre elles ne prennent en charge qu'une petite partie du protocole. Ces efforts de standardisation sont les bienvenus, bien qu'ils soient quelque peu tardifs : les plus RESTful (pour l'hypermédia) sont, près de 18 ans après la dissertation de Roy Fielding, encore des brouillons.

![Image](https://cdn-media-1.freecodecamp.org/images/i6CBAPMfBiy4qOpl5ceeYOwH3Y8EwOuBz8bc)
_Les API REST ont des standards. Comme les chargeurs de téléphone._

**Savez-vous pourquoi je n'ai cité aucun d'entre eux dans ma précédente tirade ?**

Parce que pendant toutes ces années passées à intégrer les API de grandes entreprises (pensez à Google, Microsoft, Oracle, Dropbox, Spotify, et autres), ainsi que celles de petites entreprises, **JAMAIS** je n'ai rencontré aucun de ces « standards », ni explicitement ni implicitement. Peut-être est-ce parce que j'ai eu de la malchance. Peut-être est-ce parce qu'ils sont rarement utilisés.

De mon point de vue, ce manque de standardisation visible est dû au **péché originel de REST** : pour une raison quelconque, il est venu avec un état d'esprit très anti-standards, avec une philosophie obscurantiste « tout ce dont vous avez besoin est l'amour et HTTP ». Ainsi, même les développeurs les plus talentueux ont ressenti l'urgence de spécifier leur propre protocole à moitié cuit, dans leur coin, ignorant des milliers d'autres qui avaient déjà fait de même.

Dans votre cas, naturellement, le moindre mal sera d'utiliser des standards et des bibliothèques existants. De préférence des **protocoles complets**, plutôt que des assemblages de RFCs style LEGO.

**Je dois cependant vous avertir. Ici aussi, il y a des dragons.**

Parfois, le diable est dans les détails. Une vieille sagesse en informatique stipule que les erreurs ne doivent pas passer inaperçues. C'est pourquoi il est bon de garder le format des objets cohérent : certains de leurs champs peuvent être annulés, mais ils sont présents en tout temps (sauf demande contraire du client). C'est la meilleure façon de prévenir les _faux négatifs_ (dus aux fautes de frappe), et d'éviter les ruptures aléatoires dans les clients stricts si la propriété _quantique_ de ces champs n'était pas (comme souvent) correctement documentée.

Je pensais que cette idée s'appliquait naturellement aux représentations REST, aussi. Dommage : des standards comme [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) vous obligent à supprimer les champs distants au lieu de les annuler. Ces détails minuscules mais déclencheurs d'apocalypse sont particulièrement inappropriés dans une philosophie qui prétend « aider le client et le serveur à évoluer indépendamment ».

Parfois, le diable est de la taille d'un éléphant. Vous avez déjà entendu parler de ce OpenAPI (anciennement Swagger), l'un des standards REST les plus ambitieux ? L'idée est de décrire votre API dans un fichier de spécification, avec des points de terminaison et des schémas, et d'utiliser les outils OpenAPI pour industrialiser la création à la fois du client et du serveur. Cela semble bien, n'est-ce pas ?

Voici un [exemple de spécification d'interface json](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json), pour l'API Kubernetes. Oui, les schémas Json sont par nature extrêmement verbeux.

D'accord, voici maintenant l'[implémentation cliente correspondante](https://github.com/kubernetes-incubator/client-python/tree/master/kubernetes/client) pour Python.

À ce jour, c'est plus de 90 000 lignes de code et de commentaires Python, générées automatiquement par OpenAPI. Pas seulement de minces enveloppes, pour bénéficier des outils d'auto-documentation et de l'autocomplétion de l'IDE. 90 000 lignes. Plus que leur spécification d'interface json. Qu'est-ce que c'est que ce bordel.

![Image](https://cdn-media-1.freecodecamp.org/images/WO3MynM9YLRWzKSWHvSWxHhVRoaYJCwCkjzZ)
_Quand vous demandez un catamaran à OpenAPI_

Chaque langage, chaque framework, a sa propre idée sur la manière de gérer OpenAPI. Certains choisissent des [approches hybrides (et élégamment sans cruft)](http://radar.oreilly.com/2015/09/building-apis-with-swagger.html). Certains génèrent un fichier de spécification à partir du code serveur. La plupart génèrent des tonnes de code de base à partir dudit fichier de spécification. Parfois, ils vont plus loin et génèrent des tests aussi.

Plus d'outils et plus de générateurs de code signifient plus de bugs et des courbes d'apprentissage plus difficiles… et tout cela pour quoi ? Le SDK Kubernetes est exposé à Python comme un [ensemble de méthodes](https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md#documentation-for-api-endpoints). Avec des URLs codées en dur. Encore une fois, un système RPC-sur-CRUD, considéré par beaucoup comme l'état de l'art de la RESTfulness, tout en ignorant HATEOAS. Je trouve tout cela extrêmement confus, et j'espère ne pas être le seul.

Soyez donc particulièrement prudent quant aux protocoles et frameworks liés à REST que vous pourriez choisir. Certains sont pratiques et efficaces, mais d'autres font ressembler REST de plus en plus au nouveau SOAP.

### TL;DR

Le REST™ original est comme l'ingénierie des fusées : excitant, mais très spécifique, assez complexe, et plutôt nuisible à moins de savoir précisément ce que vous faites.

Les API RESTish sont plus abordables, mais assurez-vous que vous en tirerez profit, car ce n'est rarement le cas. Pour citer une règle empirique simple de Phil Sturgeon :

> « Si une API est principalement des actions, peut-être devrait-elle être RPC. Si une API est principalement CRUD et manipule des données liées, peut-être devrait-elle être REST. »

De nombreuses normes REST(ish) existent, donc pas besoin d'en spécifier une à partir de zéro. Mais quels que soient vos besoins, méfiez-vous des buzzwords, utilisez le bon outil pour le bon travail (REST et RPC ne sont que deux parmi des centaines), et surtout, [KISS](https://en.wikipedia.org/wiki/KISS_principle). Je parie que vous auriez plus de succès en utilisant un client JsonAPI générique et en le validant contre un vrai serveur de préproduction, plutôt qu'en passant des jours à générer des tonnes de code OpenAPI de base — pour découvrir plus tard qu'il ne correspond pas réellement au côté distant à cause de bugs ou d'autres incompatibilités.

Cela vaut également pour d'autres architectures, d'ailleurs : vous économiserez probablement du temps en utilisant des protocoles simples JsonRPC ou JsonWSP, au lieu de générer du code de base avec gRPC, pour réaliser plus tard que ce protocole brillant n'a même pas spécifié comment signaler les erreurs au niveau de l'application.

### Épilogue

REST est un sujet difficile à aborder. Il y a beaucoup de trous dans la dissertation fondatrice, beaucoup de définitions conflictuelles, beaucoup d'opinions contradictoires sur la manière de faire ceci ou cela correctement, beaucoup de hypes et de disgrâces injustifiées, beaucoup de (standards sous-utilisés et partiels)… et très peu d'exemples concrets d'API HATEOAS (la plupart des liens que j'ai croisés étaient morts, alors beaucoup pour les « décennies durables »).

Mais j'espère que cette analyse a clarifié un peu les différents « RESTs » dont parlent les gens, et qu'elle vous épargnera une partie de la quantité obscène de temps que j'ai dû passer juste pour comprendre ce que le REST™ Original était censé être.

À tout le moins, vous avez maintenant une nouvelle arme dans votre sac. La prochaine fois que votre patron voudra que vous exposiez certaines opérations serveur comme des services web REST, demandez simplement :

**Pour cette API, avons-nous vraiment besoin de suivre un style architectural composite destiné aux systèmes hypermédia distribués à l'échelle d'Internet ?**

L'expression sur son visage sera votre réponse.



**Veuillez laisser vos commentaires ci-dessous. Et voici les commentaires passés sur cet article sur Medium : [https://medium.com/p/21c59d243438/responses/show](https://medium.com/p/21c59d243438/responses/show)**