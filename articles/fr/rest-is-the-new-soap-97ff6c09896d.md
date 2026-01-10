---
title: REST est le nouveau SOAP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-15T20:32:11.000Z'
originalURL: https://freecodecamp.org/news/rest-is-the-new-soap-97ff6c09896d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VlkAg8dodbaaKp-Po7DrAA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: REST est le nouveau SOAP
seo_desc: 'By Pakal de Bonchamp

  Written by Pascal Chambon, reviewed by Raphaël Gomès

  Update: this article mostly deals with the RESTish ecosystem, which now constitutes
  a major part of webservices. For more in-depth analysis of the original REST, and
  of HATEOAS...'
---

Par Pakal de Bonchamp

_Rédigé par Pascal Chambon, révisé par Raphaël Gomes_

**_Mise à jour_** : cet article traite principalement de l'écosystème RESTish, qui constitue désormais une part majeure des services web. Pour une analyse plus approfondie du REST original et de HATEOAS, voir mon [article de suivi](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438)._

### Introduction

Il y a quelques années, j'ai développé un nouveau système d'information dans une grande entreprise de télécommunications. Nous devions communiquer avec un nombre croissant de services web, exposés par des systèmes plus anciens ou par des partenaires commerciaux.

Inutile de dire que nous avons eu notre part de l'enfer [SOAP](https://en.wikipedia.org/wiki/SOAP). Des [WSDL](https://en.wikipedia.org/wiki/Web_Services_Description_Language) abstrus, des bibliothèques incompatibles, des bugs étranges... Alors, chaque fois que nous le pouvions, nous prônions — et utilisions — des protocoles simples d'appel de procédure à distance : XMLRPC ou JSONRPC.

Nos premiers serveurs et clients pour ces protocoles étaient assez basiques, limités, fragiles. Mais progressivement, nous les avons améliorés ; et avec quelques centaines de lignes de code supplémentaires, nous avons réalisé le rêve : support de différents dialectes (comme les extensions XMLRPC spécifiques à Apache), conversion intégrée entre les exceptions Python et les codes d'erreur hiérarchiques, gestion séparée des erreurs fonctionnelles et techniques, nouvelles tentatives automatiques pour ces dernières, journalisation et statistiques pertinentes avant/après les requêtes, validation approfondie des données d'entrée...

Maintenant, nous pouvions nous connecter de manière robuste à n'importe quelle API de ce type, avec seulement quelques lignes de code.

Maintenant, nous pouvions exposer n'importe quel ensemble de fonctions à un large public, à des serveurs et à des navigateurs web, avec quelques décorateurs et mises à jour de documentation.

Et lorsqu'il s'agissait de communiquer entre nos différentes applications (style microservices), c'était un travail pour notre administrateur système ; côté logiciel, c'était presque transparent.

![Image](https://cdn-media-1.freecodecamp.org/images/U8IwqOXGlnAp-z3A25ZgRz3Gm2PUjlduG1-c)
_Développeur se reposant après 30 minutes difficiles passées à intégrer une API RPC._

**Puis vint REST.**   
**REpresentational State Transfer.**

Une vague de renouvellement a secoué les fondements de la communication inter-services.

RPC était mort, l'avenir était RESTful : des ressources vivant chacune sur son propre URL, et manipulées exclusivement via le protocole HTTP.

Dès lors, chaque API que nous devions exposer ou consommer est devenue un nouveau défi ; pour ne pas dire un témoignage de folie.

### Quel est le problème avec REST ?

Un court exemple vaut un long discours. Voici une petite API, avec les types de données supprimés pour plus de lisibilité.

```
createAccount(username, contact_email, password) -> account_id
addSubscription(account_id, subscription_type) -> subscription_id
sendActivationReminderEmail(account_id) -> null
cancelSubscription(subscription_id, reason, immediate=True) -> null
getAccountDetails(account_id) -> {full data tree}
```

Ajoutez simplement une hiérarchie de exceptions bien documentée (InvalidParameterError, MissingParameterError, WorkflowError...), avec des sous-classes pour identifier les cas importants (par exemple, AlreadyExistingUsernameError), et vous êtes prêt à partir.

Cette API est facile à comprendre, facile à utiliser et robuste. Elle est soutenue par une machine à états précise, mais l'ensemble restreint d'opérations disponibles éloigne les utilisateurs des interactions nonsensiques (comme changer la date de création d'un compte).

**Temps estimé pour exposer cette API en tant que service RPC simple : quelques heures.**

D'accord, maintenant il est temps de passer à la manière RESTful.

Plus de standards, plus de spécifications précises. Juste une vague « philosophie RESTful », sujette à des débats métaphysiques sans fin, et à autant de contournements laids.

Comment mappez-vous les fonctions précises ci-dessus, à une poignée d'opérations CRUD ? L'envoi de l'e-mail de rappel d'activation est-il une mise à jour sur un attribut « must_send_activation_reminder_email » ? Ou la création d'une « ressource activation_reminder_email » ? Est-il sensé d'utiliser DELETE pour cancelSubscription() si l'abonnement reste actif pendant une période de grâce, et peut être ressuscité pendant ce temps ? Comment divisez-vous l'arbre de données de getAccountDetails() entre les endpoints, pour respecter le modèle de données de REST ?

Quel endpoint URL attribuez-vous à chacune de vos « ressources » ? Oui, c'est facile, mais il faut le faire quand même.

Comment exprimez-vous la diversité des conditions d'erreur, en utilisant le très limité ensemble de codes HTTP ?

Quels formats de sérialisation, quels dialectes spécifiques utilisez-vous pour les payloads d'entrée et de sortie ?

Comment répartissez-vous exactement ces signatures simples entre la méthode HTTP, l'URL, la chaîne de requête, le payload, les en-têtes et le code de statut ?

Et vous voilà parti pour des heures, à réinventer la roue. Pas même une roue sur mesure et intelligente. Une roue cassée et fragile, nécessitant des tonnes de documentation pour être comprise, et violant les spécifications sans même le savoir.

![Image](https://cdn-media-1.freecodecamp.org/images/0bAxdhnQJw0WseQEmDT9Km9hn2Nj2VfsWJzb)

**Comment se fait-il que REST signifie tant de TRAVAIL ?**   
_C'est à la fois un paradoxe et un jeu de mots éhonté._

Plongeons plus profondément dans les problèmes artificiels nés de cette philosophie de conception.

_ATTENTION : à travers ce document, vous rencontrerez de nombreuses questions techniques semi-rhéthoriques. Ne les mécomprenez pas, elles ne signifient PAS que les services web RESTish ne peuvent pas résoudre ces problèmes. Elles signifient simplement que les utilisateurs ont un fardeau supplémentaire de décisions à prendre, d'extensions à intégrer, de solutions de contournement personnalisées à appliquer, et c'est un problème en soi._

### La joie des verbes REST

Rest n'est pas CRUD, ses défenseurs veilleront à ce que vous ne confondiez pas ces deux concepts. Pourtant, quelques minutes plus tard, ils se réjouiront que les méthodes HTTP aient des sémantiques bien définies pour créer (POST), récupérer (GET), mettre à jour (PUT/PATCH) et supprimer (DELETE) des ressources.

Ils se délecteront à professer que ces quelques « verbes » suffisent à exprimer n'importe quelle opération. Eh bien, bien sûr qu'ils suffisent ; de la même manière qu'une poignée de verbes suffirait à exprimer n'importe quel concept en anglais : « Aujourd'hui, j'ai mis à jour mon CarDriverSeat avec mon corps, et créé un EngineIgnition, mais le FuelTank s'est supprimé lui-même » ; le fait que ce soit possible ne le rend pas moins maladroit. À moins que vous ne soyez un admirateur de la langue [Toki Pona](https://en.wikipedia.org/wiki/Toki_Pona).

Si l'objectif est d'être minimaliste, au moins faites-le correctement. Savez-vous pourquoi PUT, PATCH et DELETE n'ont jamais été implémentés dans les formulaires des navigateurs web ? Parce qu'ils sont inutiles et dangereux. Nous pouvons simplement utiliser GET pour la lecture et POST pour l'écriture. Ou POST exclusivement, lorsque la mise en cache au niveau HTTP n'est pas souhaitée. Les autres méthodes, au mieux, se mettront en travers de votre chemin, au pire, gâcheront votre journée.

Vous voulez utiliser PUT pour mettre à jour votre ressource ? D'accord, mais certaines Spécifications Sacrées indiquent que les données d'entrée doivent être équivalentes à la représentation reçue via un GET. Alors, que faites-vous des nombreux paramètres en lecture seule retournés par GET (heure de création, heure de dernière mise à jour, jeton généré par le serveur...) ? Vous les omettez et violez les principes de PUT ? Vous les incluez quand même, et attendez un « HTTP 409 Conflict » s'ils ne correspondent pas aux valeurs côté serveur (vous forçant alors à émettre un GET...) ? Vous leur donnez des valeurs aléatoires et attendez que les serveurs les ignorent (la joie des erreurs silencieuses) ? Choisissez votre poison, REST n'a clairement aucune idée de ce qu'est un attribut en lecture seule, et cela ne sera pas corrigé de sitôt. Pendant ce temps, un GET est censé retourner le mot de passe (ou le numéro de carte de crédit) qui a été envoyé dans un précédent POST/PUT ; bonne chance pour gérer également ces paramètres en écriture seule.

Ai-je oublié de mentionner que PUT apporte également des conditions de course dangereuses, où plusieurs clients écrasent les modifications des autres, alors qu'ils voulaient simplement mettre à jour des champs différents ?

Vous voulez utiliser PATCH pour mettre à jour votre ressource ? Bien, mais comme 99% des personnes utilisant ce verbe, vous allez simplement envoyer un sous-ensemble de champs de ressource dans votre payload de requête, en espérant que le serveur comprenne correctement l'opération prévue (et tous ses effets secondaires possibles) ; de nombreux paramètres de ressource sont profondément liés ou mutuellement exclusifs (par exemple, c'est soit une carte de crédit, soit un jeton Paypal, dans les informations de facturation d'un utilisateur), mais la conception RESTful cache également cette information importante. De toute façon, vous violerez à nouveau les spécifications : PATCH n'est pas censé envoyer simplement un ensemble de champs à remplacer. Au lieu de cela, vous êtes censé fournir un « ensemble d'instructions » à appliquer sur les ressources. Alors, vous voilà reparti, prenez votre papier et votre tasse de café, vous devrez décider comment exprimer ces instructions. Souvent avec des spécifications artisanales, puisque le syndrome Not-Invented-Here est une norme de facto dans le monde REST. (Edit : les défenseurs de REST ont fait machine arrière sur ce sujet, avec [Json Merge Patch](https://tools.ietf.org/html/rfc7386), une alternative aux formats comme [Json Patch](https://tools.ietf.org/html/rfc6902))

Vous voulez supprimer des ressources ? D'accord, mais j'espère que vous n'avez pas besoin de fournir des données de contexte substantielles ; comme un scan PDF de la demande de résiliation de l'utilisateur. DELETE interdit d'avoir un payload. Une contrainte que les architectes REST ignorent souvent, puisque la plupart des serveurs web n'appliquent pas cette règle sur les requêtes qu'ils reçoivent. Quelle compatibilité, d'ailleurs, aurait une requête DELETE avec 2 Mo de chaîne de requête base64 attachée ? (Edit : le [RFC 2616](https://tools.ietf.org/html/rfc2616#section-4.3), indiquant que les payloads sans sémantique doivent être ignorés, est désormais obsolète)

![Image](https://cdn-media-1.freecodecamp.org/images/Kh0pTcWKoXqHlue3kdqTPNk9HhwjzDoe4kFQ)

Les passionnés de REST professent facilement que « les gens font cela de travers » et que leurs API ne sont « pas vraiment RESTful ». Par exemple, de nombreux développeurs utilisent PUT pour créer une ressource directement sur son URL final (_/myresourcebase/myresourceid_), alors que la « bonne manière » (edit : selon beaucoup) de le faire est de POST sur une URL parente (_/myresourcebase_), et de laisser le serveur indiquer, avec un en-tête HTTP « Location », l'URL de la nouvelle ressource (edit : ce n'est pas une redirection HTTP cependant). La bonne nouvelle est : cela n'a pas d'importance. Ces principes rigoureux sont comme Big Endian vs Little Endian, ils occupent les philosophes pendant des heures, mais ont très peu d'impact sur les problèmes de la vie réelle, c'est-à-dire « faire avancer les choses ».

Au fait... concevoir des URL à la main est toujours très amusant. Savez-vous combien d'implémentations urlencodent() correctement les identifiants lors de la construction des URL REST ? Pas tant que cela. Préparez-vous à des pannes désagréables et à des attaques SSRF/CSRF.

![Image](https://cdn-media-1.freecodecamp.org/images/3cj3Mv2d3PmHunKtUoRheSjqK4ALGsJXAEud)
_Quand vous oubliez d'urlencoder les noms d'utilisateur dans 1 de vos 30 URL conçues à la main._

### La joie de la gestion des erreurs REST

Presque tous les codeurs sont capables de faire fonctionner un « cas nominal ». La gestion des erreurs est l'une de ces fonctionnalités qui décidera si votre code est un logiciel robuste ou un énorme tas d'allumettes.

HTTP fournit une liste de codes d'erreur prêts à l'emploi. Super, voyons cela.

Utiliser « HTTP 404 Not Found » pour notifier une ressource inexistante semble très RESTful, n'est-ce pas ? Dommage : votre nginx a été mal configuré pendant 1 heure, donc vos consommateurs d'API n'ont reçu que des erreurs 404 et ont purgé des centaines de comptes, pensant qu'ils avaient été supprimés...

![Image](https://cdn-media-1.freecodecamp.org/images/E7ViySx5TgWjpOm4ajHxsAhkfRY58Sz1IQW5)
_Nos clients, après que nous ayons supprimé par erreur leurs gigaoctets d'images de chatons._

Utiliser « HTTP 401 Unauthorized » lorsqu'un utilisateur n'a pas d'identifiants d'accès à un service tiers semble acceptable, n'est-ce pas ? Cependant, si un appel ajax dans votre navigateur Safari reçoit ce code d'erreur, il pourrait surprendre votre client final avec une invite de mot de passe très inattendue [c'était le cas il y a des années, YMMV].

HTTP existait bien avant les « services web RESTful », et l'écosystème web est rempli d'hypothèses sur la signification de ses codes d'erreur. Les utiliser pour transporter des erreurs d'application est comme utiliser des bouteilles de lait pour se débarrasser de déchets toxiques : inévitablement, un jour, il y aura des problèmes.

Certains codes d'erreur HTTP standard sont spécifiques à Webdav, d'autres à Microsoft, et les quelques autres ont des définitions si floues qu'ils ne sont d'aucune aide. En fin de compte, comme la plupart des utilisateurs de REST, vous utiliserez probablement des codes HTTP aléatoires, comme « HTTP 418 I'm a teapot » ou des numéros non attribués, pour exprimer vos exceptions spécifiques à l'application. Ou vous retournerez sans vergogne « HTTP 400 Bad Request » pour toutes les erreurs fonctionnelles, puis inventerez votre propre format d'erreur maladroit, avec des booléens, des codes entiers, des slugs et des messages traduits fourrés dans un payload arbitraire. Ou vous abandonnerez complètement la gestion des erreurs appropriée ; vous retournerez simplement un message en langage naturel, et espérerez que l'appelant sera un humain capable d'analyser le problème et de prendre des mesures. Bonne chance pour interagir avec de telles API à partir d'un programme autonome.

### La joie des concepts REST

REST a fait carrière en se vantant de concepts que tout architecte de service dans son bon sens respecte déjà, ou de principes qu'il ne suit même pas. Voici quelques extraits, tirés de pages web bien classées.

_REST est une architecture client-serveur. Le client et le serveur ont chacun un ensemble différent de préoccupations._ Quelle révélation dans le monde du logiciel.

_REST fournit une interface uniforme entre les composants._ Eh bien, comme tout autre protocole le fait, lorsqu'il est imposé comme la _lingua franca_ de tout un écosystème de services.

_REST est un système en couches. Les composants individuels ne peuvent pas voir au-delà de la couche immédiate avec laquelle ils interagissent._ Cela semble être une conséquence naturelle de toute architecture bien conçue et faiblement couplée ; incroyable.

Rest est génial, car il est SANS ÉTAT. Oui, il y a probablement une énorme base de données derrière le service web, mais il ne se souvient pas de l'état du client. Ou, bien, oui, en fait, il se souvient de sa session d'authentification, de ses permissions d'accès... mais il est sans état, néanmoins. Ou plus précisément, tout aussi sans état que n'importe quel protocole basé sur HTTP, comme le RPC simple mentionné précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/kRhdDUN-QCazUckRJuN8D4cKsB7zNS0mcWbp)

Avec REST, vous pouvez exploiter la puissance de la MISE EN CACHE HTTP ! Eh bien, voici enfin un point concluant : une requête GET et ses en-têtes de contrôle de cache sont effectivement compatibles avec les caches web. Cela dit, les caches locaux (Memcached, etc.) ne suffisent-ils pas pour 99% des services web ? Les caches hors de contrôle sont des bêtes dangereuses ; combien de personnes veulent exposer leurs API en texte clair, afin qu'un Varnish ou un Proxy sur le chemin puisse continuer à fournir du contenu obsolète, longtemps après qu'une ressource a été mise à jour ou supprimée ? Peut-être même le fournir « pour toujours », si une erreur de configuration s'est produite une fois ? Un système doit être sécurisé par défaut. J'admets parfaitement que certains systèmes très chargés veulent bénéficier de la mise en cache HTTP, mais cela coûte beaucoup moins cher d'exposer quelques endpoints GET pour les interactions en lecture seule intensives, que de basculer toutes les opérations vers REST et sa gestion des erreurs douteuse.

_Grâce à tout cela, REST a des PERFORMANCES ÉLEVÉES_ ! En sommes-nous sûrs ? Tout concepteur d'API le sait : localement, nous voulons des API fines, pour pouvoir faire tout ce que nous voulons ; et à distance, nous voulons des API grossières, pour limiter l'impact des allers-retours réseau. Voici encore un domaine dans lequel REST échoue misérablement. La division des données entre « ressources », chaque instance sur son propre endpoint, conduit naturellement au problème des N+1 requêtes. Pour obtenir les données complètes d'un utilisateur (compte, abonnements, informations de facturation...), vous devez émettre autant de requêtes HTTP ; et vous ne pouvez pas les paralléliser, puisque vous ne connaissez pas à l'avance les identifiants uniques des ressources associées. Cela, plus l'incapacité à récupérer seulement une partie des objets de ressource, crée naturellement des goulots d'étranglement désagréables (edit : oui, vous pouvez intégrer des extensions comme Compound/Partial Documents dans votre configuration pour aider à cela)..

_REST offre une meilleure compatibilité._ Comment cela ? Pourquoi tant de services web REST ont-ils « /v2/ » ou « /v3/ » dans leurs URL de base alors ? Les API compatibles ascendantes et descendantes ne sont pas difficiles à réaliser, avec des langages de haut niveau, tant que des règles simples sont suivies lors de l'ajout/dépréciation de paramètres. À ma connaissance, REST n'apporte rien de nouveau sur le sujet.

_REST est SIMPLE, tout le monde connaît HTTP !_ Eh bien, tout le monde connaît aussi les cailloux, pourtant les gens sont heureux d'avoir de meilleurs blocs pour construire leur maison. De la même manière que XML est un méta-langage, HTTP est un méta-protocole. Pour avoir un vrai protocole d'application (comme les « dialectes » le sont pour XML), vous devrez spécifier beaucoup de choses ; et vous finirez avec Yet Another RPC Protocol, comme s'il n'y en avait pas déjà assez.

_REST est si facile, il peut être interrogé à partir de n'importe quel shell, avec CURL !_ D'accord, en fait, tout protocole basé sur HTTP peut être interrogé avec CURL. Même SOAP. Émettre un GET est particulièrement simple, c'est sûr, mais bonne chance pour écrire des payloads POST json ou xml à la main ; les gens utilisent généralement des fichiers de fixtures, ou, beaucoup plus pratique, des clients API complets instanciés directement dans l'interface de ligne de commande de leur langage préféré.

« Le client n'a besoin d'aucune connaissance préalable du service pour l'utiliser ». C'est de loin ma citation préférée. Je l'ai trouvée de nombreuses fois, sous différentes formes, surtout lorsque le mot à la mode [HATEOAS](https://fr.wikipedia.org/wiki/HATEOAS) rôdait ; parfois avec quelques phrases « except » prudentes (mais insuffisantes) qui suivaient. Pourtant, je ne sais pas dans quel monde fantastique vivent ces gens, mais dans celui-ci, un programme client n'est pas une colonie de fourmis ; il ne parcourt pas les API distantes de manière aléatoire, puis décide comment les gérer au mieux, sur la base de la reconnaissance de motifs ou de la magie noire. Tout au contraire ; le client a des attentes précises sur ce que cela signifie, de PUT ce champ à cette URL avec cette valeur, et le serveur ferait mieux de respecter la sémantique qui a été convenue lors de l'intégration, sinon tout l'enfer pourrait se déchaîner.

![Image](https://cdn-media-1.freecodecamp.org/images/34MrY7lPN5IORJltxiixXPAQaJPXy6efQRNa)
_Quand vous demandez comment HATEOAS est censé fonctionner._

### Comment faire REST correctement et rapidement ?

Oubliez la partie « correctement ». REST est comme une religion, aucun simple mortel ne saisira jamais l'étendue de son génie, ni ne « le fera correctement ».

Donc la vraie question est : si vous êtes forcé d'exposer ou de consommer des services web de manière quelque peu RESTful, comment vous dépêcher de faire ce travail, et passer à des tâches plus constructives _dès que possible_ ?

**_Mise à jour_** : il s'avère qu'il existe en fait de nombreuses « normes » et efforts d'industrialisation pour REST, bien que je ne les aie jamais rencontrés personnellement (peut-être parce que peu de gens les utilisent ?). Plus d'informations dans mon [article de suivi](https://medium.com/@pakaldebonchamp/follow-up-to-rest-is-the-new-soap-the-origins-of-rest-21c59d243438)._

#### Comment industrialiser l'exposition côté serveur ?

Chaque framework web a sa propre manière de définir les endpoints URL. Donc, attendez-vous à de grosses dépendances, ou à une bonne couche de code boilerplate écrit à la main, pour brancher votre API existante sur votre serveur préféré en tant qu'ensemble d'endpoints REST.

Des bibliothèques comme Django-Rest-Framework automatisent la création d'API REST, en agissant comme des wrappers centrés sur les données au-dessus des schémas SQL/noSQL. Si vous voulez simplement faire du « CRUD sur HTTP », vous pourriez être satisfait avec elles. Mais si vous voulez exposer des API communes « faites-le-pour-moi », avec des workflows, des contraintes, des impacts de données complexes et autres, vous aurez du mal à plier un framework REST à vos besoins.

Préparez-vous à connecter, une par une, chaque méthode HTTP de chaque endpoint, à l'appel de méthode correspondant ; avec une bonne part de gestion des exceptions faite main, pour traduire les exceptions traversantes en codes d'erreur et payloads correspondants.

#### Comment industrialiser l'intégration côté client ?

D'après mon expérience, mon estimation est : vous ne le faites pas.

Pour chaque intégration d'API, vous devrez parcourir de longues documentations, et suivre des recettes détaillées sur la manière dont chacune des N opérations possibles doit être effectuée.

Vous devrez concevoir des URL à la main, écrire des sérialiseurs et désérialiseurs, et apprendre à contourner les ambiguïtés de l'API. Préparez-vous à quelques essais et erreurs avant de dompter la bête.

Savez-vous comment les fournisseurs de services web compensent cela et facilitent l'adoption ?

Simple, ils écrivent leurs propres implémentations de clients officiels.

POUR. CHAQUE. LANGAGE. MAJEUR. ET. PLATEFORME.

J'ai récemment traité avec un système de gestion d'abonnements. Ils fournissent des clients pour PHP, Ruby, Python, .NET, iOS, Android, Java... plus quelques contributions externes pour Go et NodeJS.

Chaque client vit dans son propre dépôt Github. Chacun avec sa propre grande liste de commits, de tickets de suivi de bugs et de pull requests. Chacun avec ses propres exemples d'utilisation. Chacun avec son architecture maladroite, quelque part entre ActiveRecord et un proxy RPC.

C'est stupéfiant. Combien de temps est passé à développer de tels wrappers étranges, au lieu d'améliorer le vrai, le précieux, le service web qui fait avancer les choses ?

![Image](https://cdn-media-1.freecodecamp.org/images/6e6uGUi7IVtFgglB6VlN3m6Kq5ohKtztGVet)
_Sisyphe développant Encore Un Client pour son API._

### **Conclusion**

Pendant des décennies, presque tous les langages de programmation ont fonctionné avec le même workflow : envoyer des entrées à un appelable, et obtenir des résultats ou des erreurs en sortie. Cela fonctionnait bien. Très bien.

Avec Rest, cela s'est transformé en un travail insensé de mapping de pommes à des oranges, et de louanges aux spécifications HTTP pour mieux les violer quelques minutes plus tard.

À une époque où les [MICROSERVICES](https://en.wikipedia.org/wiki/Microservices) sont de plus en plus courants, comment se fait-il qu'une tâche aussi simple — lier des bibliothèques sur des réseaux — reste-t-elle aussi artificiellement astucieuse et encombrante ?

Je ne doute pas que certaines personnes intelligentes là-bas fourniront des cas où REST brille ; elles mettront en avant leur protocole maison basé sur REST, permettant de découvrir et de faire des opérations CRUD sur des arbres d'objets arbitraires, grâce à des hyperliens ; elles expliqueront comment la conception REST est si brillante, que je n'ai simplement pas lu assez d'articles et de dissertations sur ses concepts.

Je m'en fiche. Les arbres sont reconnus par leurs propres fruits. Ce qui m'a pris quelques heures de codage et a fonctionné de manière très robuste, avec un simple RPC, prend maintenant des semaines et ne cesse d'inventer de nouvelles façons d'échouer ou de briser les attentes. Le développement a été remplacé par du bricolage.

L'appel de procédure à distance presque transparent était ce dont 99% des gens avaient vraiment besoin, et les protocoles existants, aussi imparfaits qu'ils étaient, faisaient très bien le travail. Cette monomanie de masse pour le plus petit dénominateur commun du web, HTTP, a principalement abouti à un énorme gaspillage de temps et de matière grise.

**REST a promis la simplicité et a livré la complexité.**  
**REST a promis la robustesse et a livré la fragilité.**  
**REST a promis l'interopérabilité et a livré l'hétérogénéité.**  
**REST est le nouveau SOAP.**

### Épilogue

L'avenir pourrait être radieux. Il existe encore de nombreux excellents protocoles disponibles, en format binaire ou texte, avec ou sans schéma, certains exploitant les nouvelles capacités de HTTP2... alors passons à autre chose, les gens. Nous ne pouvons pas rester éternellement à l'âge de pierre des services web.

_Edit_ : beaucoup de gens ont demandé ces protocoles alternatifs, le sujet mériterait sa propre histoire, mais on pourrait jeter un œil à XMLRPC et JSONRPC (simples mais assez pertinents), ou JSONWSP (inclut des schémas), ou des couches spécifiques aux langages comme Pyro ou RMI pour un usage interne, ou les nouveaux venus comme GraphQL et gRPC pour les API publiques...

![Image](https://cdn-media-1.freecodecamp.org/images/L5hrdnm4vPQK-RaCYSy4z49vFhqYeUdsZom3)
« Terminez toujours une tirade sur une note positive », a dit maman.

Édité le 12 décembre 2017 :

* normaliser les titres de section
* corriger quelques fautes de frappe
* rectifier la formulation impropre « redirection HTTP » après les opérations POST
* ajouter des suggestions de protocoles alternatifs

Édité le 28 décembre 2017 :

* corriger le mélange entre « méthodes HTTP » et « verbes REST »

Édité le 7 janvier 2018 :

* corriger les formulations ambiguës

Édité le 19 janvier 2018 :

* corriger la formulation incorrecte sur les remarques « PUT vs GET »
* préciser la notion de « vraies API » (non-CRUD)
* mentionner le risque de remplacements avec PUT
* mettre à jour les paragraphes sur les problèmes de PATCH et DELETE

Édité le 19 janvier 2018 :

* corriger la formulation autour du syndrome Not-Invented-Here

Édité le 2 février 2018 :

* ajouter des liens vers l'article de suivi sur The Original REST, dans les chapitres « introduction » et « comment industrialiser »

Édité le 14 avril 2019 :

* ajouter une clarification sur la « question semi-rhétorique », et des indices sur les extensions comme les documents composés/partiels

Édité le 6 juillet 2019 :

* corriger les fautes de frappe et les liens français

**Veuillez laisser vos commentaires ci-dessous. Et voici les commentaires passés sur cet article sur Medium : [https://medium.com/p/97ff6c09896d/responses/show](https://medium.com/p/97ff6c09896d/responses/show)**