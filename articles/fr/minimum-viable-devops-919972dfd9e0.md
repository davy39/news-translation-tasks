---
title: Minimum Viable DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-06T00:19:02.000Z'
originalURL: https://freecodecamp.org/news/minimum-viable-devops-919972dfd9e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6yL_QTApwZcnDR4HKH4vow.png
tags:
- name: Devops
  slug: devops
- name: growth hacking
  slug: growth-hacking
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Minimum Viable DevOps
seo_desc: 'By Michael Shilman

  A quick and dirty guide to scaling your launch and embracing the Internet hug of
  death

  Startup Genome says premature scaling is the number one cause of startup death.
  You shouldn’t spend time optimizing a product when you don’t eve...'
---

Par Michael Shilman

#### Un guide rapide et efficace pour dimensionner votre lancement et embrasser l'étreinte mortelle d'Internet

Startup Genome affirme que le [dimensionnement prématuré](http://www.forbes.com/sites/nathanfurr/2011/09/02/1-cause-of-startup-death-premature-scaling/#7171575515aa) est la principale cause de mort des startups. Vous ne devriez pas passer du temps à optimiser un produit lorsque vous ne savez même pas si les utilisateurs en veulent.

Pourtant, chaque fois que vous lancez une application web, vous courez le risque de réellement réussir, et votre serveur doit être prêt à gérer la charge.

Dans cet article, je vais partager une recette simple et gratuite pour rendre votre application prête au lancement. Une heure passée à suivre ces étapes vous fera économiser d'innombrables heures de sommeil tout au long de la vie de votre produit.

En résumé :

1. Effectuez un benchmarking à l'aide d'un outil de test de charge comme Loader.io.
2. Utilisez un proxy de cache comme NGINX pour atténuer la charge du serveur.
3. Utilisez un CDN comme Cloudflare pour un chargement rapide et une distribution mondiale.

### Problèmes de premier monde

Commençons par cela. Avoir trop de trafic sur votre site web est un problème de premier monde, et en écrire est le humblebrag ultime. Coupable sur tous les fronts. Poursuivez-moi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_0xNmiOilaYHRVPK02k9Lg.png)

Mais c'est toujours un problème. Le monde des startups est rempli d'histoires de services atteignant la première page de Reddit, étant "inattendus" sur Product Hunt, et ainsi de suite. C'est un cliché à ce stade.

Cet article est l'opposé de cela. Au cours de l'année passée, j'ai lancé trois services auprès de millions d'utilisateurs et j'ai dormi comme un bébé pendant que mon serveur était submergé de clics, sans aucun temps d'arrêt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZhOwckDdGMmvKfizDju-SQ.png)
_Vous ne savez jamais quels canaux généreront des clics, mais il est bon d'être préparé._

[Hello Money](https://hellomoney.co/) est l'outil de choix de Reddit pour la visualisation de portefeuille et les retours des pairs. **Pics :** Il a été classé [n°1 sur Product Hunt](https://www.producthunt.com/@amitch5903/collections/investing-products) le jour de son lancement et nommé par PH comme l'une des [7 meilleures applications de finance personnelle](https://medium.com/@producthunt/the-7-best-personal-finance-apps-bf1fbd6caa9d#.1tj1vmspv), a atteint le sommet de [/r/personalfinance](https://www.reddit.com/r/personalfinance) à plusieurs reprises (près de 7M de lecteurs), et a été présenté sur Hacker News.

[Goodbye Gun Stocks](https://goodbyegunstocks.com/) montre aux investisseurs socialement conscients si leurs fonds communs de placement et ETF sont investis dans des entreprises d'armes à feu et les aide à trouver des fonds similaires sans armes à feu avec des frais plus bas et de meilleurs rendements historiques. **Pics :** écrit dans [New York Daily News](http://www.nydailynews.com/news/national/couple-launches-money-goodbye-gun-stocks-website-article-1.2637231?cid=bitly), [Fortune](http://fortune.com/2016/06/13/orlando-shooting-gun-companies-stocks/), [Time](http://time.com/money/4366155/gun-companies-stocks-orlando-shooting/), [Fast Company](http://www.fastcoexist.com/3058717/against-gun-violence-then-get-your-money-out-of-gun-stocks-with-this-easy-tool), [Vice](http://motherboard.vice.com/read/goodbye-gun-stocks-you-might-be-contributing-to-the-firearm-industry-and-not-know-it) ([Deux fois !](http://www.vice.com/read/how-gun-divestment-advocates-are-reacting-to-the-orlando-shooting)), [GOOD](https://www.good.is/articles/issue-37-funds-ammo), c'est la n°1 [application politique](https://www.producthunt.com/topics/politics) sur Product Hunt à l'exclusion des blagues sur Trump (qui sont difficiles à battre !). Il a également reçu beaucoup d'amour sur Twitter et Facebook.

[Sidebar](http://sidebar.io/) est la newsletter quotidienne de design de [Sacha Greif](https://www.freecodecamp.org/news/minimum-viable-devops-919972dfd9e0/undefined). Sacha est une puissance du design avec plus de 20k d'abonnés sur Twitter, de nombreuses listes de diffusion massives, et une abondance de karma sur Hacker News. Chaque fois qu'il lance quelque chose, cela est inondé d'attention, donc avant qu'il ne lance une refonte de Sidebar, j'ai utilisé ce plan de jeu pour aider à m'assurer qu'il pouvait gérer la charge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3tmKj3QAgn9UEE-CJgSqiA.png)
_De beaux problèmes à avoir !_

### Solution de troisième monde

Pour toute personne ayant construit un service véritablement à l'échelle d'Internet, comme Google, Facebook, Amazon, je m'excuse à l'avance. De même, si vous listez DevOps comme l'une de vos compétences, vous pourriez être dégoûté par ce que vous lisez ici.

Ce que je décris est une solution rapide pour des gens comme moi qui sont ravis lorsque leur site reçoit 100 000 visiteurs d'un coup. Pour une solution de dimensionnement à long terme, cherchez ailleurs.

Je vais présenter la solution dans l'ordre. Prévoyez de passer un après-midi dessus la première fois que vous implémentez ce flux. Une fois que vous êtes à l'aise avec cela, vous devriez pouvoir préparer un site en une heure environ.

Voici les étapes à nouveau :

1. Effectuez un benchmarking à l'aide d'un outil de test de charge comme Loader.io.
2. Utilisez un proxy de cache comme NGINX pour atténuer la charge du serveur.
3. Utilisez un CDN comme Cloudflare pour un chargement rapide et une distribution mondiale.

### 1. La mère de toutes les charges

La première étape pour se préparer est de mesurer votre service existant sous charge, en simulant des milliers de visites d'utilisateurs sur un intervalle d'1 minute.

Il existe un million d'outils open source différents pour les tests de charge, mais nous voulons tout faire en une heure, donc nous utiliserons [Loader.io](https://loader.io/), un SaaS gratuit qui est trivial à configurer et à utiliser.

Il n'y a que quelques paramètres que vous devez configurer et ensuite vous êtes prêt :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PxD9g8loSX2Gl4PBikhb2g.png)
_Le test de charge de votre service est aussi simple que de remplir deux champs._

Si vous n'avez pas encore fait d'optimisations, la première exécution va probablement casser votre service, et c'est OK. Voici moi en train de casser Goodbye Gun Stocks pendant ma préparation de lancement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_z_xuSYW-r4VtEG6TrjYug.png)
_Avant optimisation : GoodbyeGunStocks.com se casse avec une charge de 4K clients sur un intervalle d'1 minute._

Sur l'axe X se trouve le temps, et l'axe Y montre à la fois les clients actifs et le temps de réponse moyen. Au fil du temps, ces deux valeurs augmentent régulièrement. Le temps de réponse commence à 0 et atteint plus de 10 secondes au cours de l'exécution. Cela est dû au fait que le service n'est pas optimisé et ne peut pas gérer les requêtes à temps. Les requêtes s'accumulent et tout s'arrête.

En revanche, voici à quoi ressemble une exécution réussie. Le temps de réponse est réduit à une moyenne de 9 ms et reste ainsi pendant la majeure partie de l'exécution, atteignant occasionnellement environ 17 ms.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_O4dy8Xu3wYgV_7efnj8IQ.png)
_Après optimisation : GoodbyeGunStocks.com survit à une charge de 10K clients sur un intervalle d'1 minute._

Notez que puisque cette approche est rapide et approximative pour les tests de charge, elle a ses limites :

1. **Charge limitée.** Le plan gratuit de Loader.io est limité à un maximum de 10 000 requêtes par minute, mais c'est plus que ce que la plupart des services recevront, même s'ils atteignent le sommet de ProductHunt, Hacker News et Reddit. Si vous vous en souciez vraiment, vous pouvez simplement passer à une version payante.
2. **HTTP/S uniquement.** Loader.io ne prend en charge que les requêtes HTTP/S pour l'instant. Certaines applications web modernes, telles que [Meteor](https://www.meteor.com/) (qui a été utilisé pour construire les trois services ci-dessus), utilisent également des websockets pour la communication. Si vous vous en souciez vraiment, vous pouvez utiliser d'autres outils pour les tests de charge, mais vous ne serez probablement pas terminé en une heure. Par exemple, Meteor dispose de [MeteorDown](https://github.com/meteorhacks/meteor-down) pour les tests de charge. [Kadira](https://kadira.io/), des mêmes auteurs, est le meilleur outil pour comprendre les problèmes de performance de Meteor.

### 2. NGINX : Le pansement de l'Internet

Si votre service a survécu au test de charge, vous pouvez tout aussi bien le lancer maintenant. Sinon, vous pourriez vous remettre en question, et il vaut probablement la peine de voir s'il existe une solution rapide.

Il existe tant d'explications possibles à ce qui a mal tourné, et même pour une petite application, vous pourriez passer une vie à ajuster les configurations du serveur, les requêtes de la base de données et les boucles mal écrites.

Mais oubliez tout cela. [NGINX](https://nginx.org/en/) est un serveur web haute performance gratuit et open-source, et un proxy polyvalent. Vous pouvez l'utiliser pour résoudre la plupart des problèmes de performance avec un petit investissement en temps. Une fois que vous l'aurez appris, ce sera un outil de confiance que vous pourrez utiliser pour bricoler tout ce que vous construisez à l'avenir.

L'essentiel avec NGINX est qu'il est extrêmement rapide et, avec un peu de travail, vous pouvez le configurer pour faire presque n'importe quoi. Pour tous mes services, j'exécute un serveur NGINX devant le service réel, en tant que proxy inverse d'équilibrage de charge avec cache :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tNEcvS4fkq2wWWyR3R5hAA.png)
_Un proxy inverse d'équilibrage de charge avec cache pour expier tous vos péchés de performance._

#### Configuration

La configuration de NGINX est un processus rapide et [bien documenté](http://nginx.org/en/docs/beginners_guide.html). La chose déroutante est qu'il fait tant de choses différentes qu'il peut être difficile à configurer. Alors je vais aller droit au but et partager la configuration que nous utilisons pour Sidebar, et l'expliquer afin que vous puissiez l'utiliser comme point de départ pour optimiser votre propre service :

Il y a trois choses clés qui se passent ici :

1. **Proxy inverse.** Toutes les lignes de configuration sous la ligne **PROXY STARTS HERE** configurent NGINX pour qu'il soit un proxy inverse, ce qui signifie qu'il transmet les requêtes à votre application web, récupère la réponse et renvoie la réponse au demandeur.
2. **Équilibreur de charge.** La déclaration **upstream** en haut configure NGINX pour qu'il soit également un équilibreur de charge, afin qu'il puisse répartir les requêtes sur plusieurs serveurs backend au lieu d'un seul.
3. **Cache.** Tout ce qui suit la ligne **CACHING** configure NGINX pour qu'il soit un cache, ce qui signifie que NGINX peut stocker certaines des réponses et retourner les résultats sans jamais atteindre le serveur d'application backend.

NGINX en tant que proxy inverse n'est pas important en soi, mais il permet l'équilibrage de charge et le caching, ce qui est génial pour la scalabilité. Alors approfondissons un peu ces aspects.

#### Équilibreur de charge

L'équilibrage de charge signifie que vous pouvez configurer plusieurs serveurs d'application pour exécuter votre application. Cela présente quelques avantages :

1. **Scalabilité horizontale.** Si votre application est limitée par le CPU ou la mémoire, et que votre trafic maximise votre serveur, vous pouvez facilement ajouter un autre serveur backend.
2. **Redéploiement dynamique.** Si vous devez modifier votre code serveur, vous pouvez lancer une nouvelle machine exécutant le nouveau code, le tester, puis l'ajouter à l'équilibreur de charge.
3. **Tolérance aux pannes.** Si l'un de vos serveurs plante ou est surchargé, NGINX peut être configuré pour le retirer automatiquement de la liste. La configuration ci-dessus ne fait pas cela, mais il est possible de l'ajouter.

Le seul inconvénient de l'exécution d'un équilibreur de charge est une légère augmentation de la complexité (totalement justifiée), et potentiellement des coûts de serveur accrus. Notez que vous pouvez également faire un proxy vers un serveur exécuté sur un port différent de la même machine pour économiser des coûts, et NGINX est si efficace que cela est acceptable pour toutes les charges sauf les plus importantes.

#### Caching

Le caching signifie que les réponses HTTP sont stockées sur le disque pendant une certaine période, et lorsqu'un client fait la même requête pendant cette période de cache, NGINX renverra la réponse en cache plutôt que de solliciter le serveur d'application.

Cela présente quelques avantages clés :

1. **Charge serveur réduite.** NGINX est incroyablement efficace et peut gérer des milliers de requêtes sur un serveur normal. Je n'ai jamais rencontré de problèmes avec lui, même en exécutant des sites à fort trafic. Le vrai problème vient des serveurs d'application ou des bases de données, et chaque réponse en cache de NGINX est une requête de moins que le serveur d'application doit gérer.
2. **Vitesse de réponse.** Les réponses en cache sont super rapides. Si vos données ne changent pas rapidement ou ne sont pas spécifiques à l'utilisateur, alors l'utilisateur devrait voir le résultat en millisecondes s'il est sur une connexion raisonnablement rapide.

Contrairement à l'équilibrage de charge, le caching peut avoir quelques inconvénients, et vous devez être prudent sur la manière dont vous cachez.

1. **Données obsolètes.** Le problème le plus évident est celui des données obsolètes. Si vos données contiennent beaucoup de données hautement dynamiques comme un site de bourse en temps réel, ou beaucoup de données spécifiques à l'utilisateur, alors le caching est un défi. Cependant, la plupart des pages et applications ont une page d'accueil principalement statique qui capte la plupart du trafic, puis des sections plus dynamiques vers lesquelles beaucoup moins d'utilisateurs cliquent. Si votre service suit ce schéma, vous pouvez mettre en cache la première, et laisser la seconde non mise en cache.
2. **Sécurité réduite.** Si vos réponses contiennent des données sensibles à l'utilisateur, vous ne pouvez pas les mettre en cache. Soyez prudent avec le caching et la sécurité ! Dans la configuration ci-dessus, nous avons créé une variable **$skip_cache** pour éviter la mise en cache pour les utilisateurs connectés. Nous testons le cookie **meteor_login_token**, mais cela devrait être facile à personnaliser pour votre configuration.
3. **Complexité / Débogabilité.** Dès que vous commencez à mettre en cache, vous introduisez une nouvelle source majeure de complexité dans le système. Lorsque quelque chose ne va pas, est-ce à cause d'un bug dans le service, ou d'un bug dans la réponse en cache, ou autre chose ?

Malgré les problèmes liés au caching, avec un peu de pratique, cela peut être une excellente solution rapide pour presque tous les problèmes de performance. Il existe de nombreux autres endroits où vous pouvez mettre en cache (requêtes de base de données, etc.), mais NGINX est facile.

#### Relancez votre test de charge

Au fur et à mesure que vous optimisez votre service, relancez votre test de charge. Voici Goodbye Gun Stocks après avoir reçu un peu d'amour de NGINX :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_O4dy8Xu3wYgV_7efnj8IQ.png)
_Après optimisation : GoodbyeGunStocks.com survit à une charge de 10K clients sur un intervalle d'1 minute._

Après que votre service gère la charge, assurez-vous de faire des tests manuels pour vous assurer que vous n'avez rien cassé. Assurez-vous de tester les fonctions de base comme la connexion/déconnexion de l'utilisateur, car ce sont des choses faciles à perturber lorsque vous mettez en cache. Si tout semble bon, vous devriez être prêt à partir.

La configuration de NGINX comme ceci peut couvrir même le code serveur le plus inefficace. Cela peut nécessiter quelques ajustements, mais pour la plupart des applications, cela fera l'affaire pour vous rendre prêt au lancement en un clin d'œil.

### 3. Devenir mondial

D'accord, vous avez surmonté la partie difficile et vous avez un service capable de résister à la plupart des pics de trafic. Mais Internet est un village mondial, et si vous publiez votre service sur une source de trafic majeure, vous recevrez du trafic de l'autre côté de la planète. Assurons-nous que ces utilisateurs aient également une expérience décente.

Heureusement, il existe des réseaux de diffusion de contenu pour cela. Je recommande [Cloudflare](https://www.cloudflare.com/). Les options de base sont gratuites et devraient être plus que suffisantes pour votre [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product).

![Image](https://cdn-media-1.freecodecamp.org/images/1*dbRFcFGzWWrn01G5rWGsew.png)
_L'interface utilisateur à onglets de Cloudflare offre de nombreuses options, mais il ne faut qu'une minute pour configurer les bases._

En plus de rendre tous vos actifs statiques plus rapides à charger, la configuration de Cloudflare présente quelques autres avantages :

1. **Sécurité.** Cloudflare offre un HTTPS en un clic. La configuration de HTTPS sur votre serveur peut être fastidieuse, même avec des services géniaux comme [LetsEncrypt](https://letsencrypt.org/) qui la rendent relativement bon marché et facile. Cloudflare fournit un HTTPS minimal avec un clic de bouton, même si votre serveur n'exécute que HTTP. Cela est suffisant pour de nombreux produits viables minimaux, bien que si vous traitez des informations sensibles telles que la finance ou la santé, vous devriez définitivement crypter tout le flux.
2. **Protection DDoS.** Lorsque je lançais Goodbye Gun Stocks, je m'inquiétais des potentielles attaques par déni de service, car la prévention de la violence par arme à feu est un sujet brûlant aux États-Unis. Cela n'a finalement pas été un problème, mais si cela avait été le cas, Cloudflare dispose d'un service intégré pour aider à gérer cela. Je ne l'ai pas utilisé, mais c'est rassurant de savoir que quelqu'un vous couvre.

### D'accord, maintenant lancez-le !

En utilisant ce kit de lancement, vous pouvez rapidement transformer votre nouveau service d'un produit viable minimal en un service testé sous charge, prêt au lancement et accessible mondialement. Tout cela est possible en utilisant des outils gratuits et un investissement de temps mineur.

Si votre service devient totalement viral comme [The Dress](https://en.wikipedia.org/wiki/The_dress_(viral_phenomenon)), dont la page Tumblr a reçu 14 000 vues par seconde à son apogée, alors ces techniques ne suffiront probablement pas, et vos serveurs pourraient finir en un tas fumant. Mais hé, il y a pire problème à avoir !

Commentez ci-dessous avec vos questions ou suggestions. Et suivez-moi ici ou [sur Twitter](https://twitter.com/mshilman) pour _d'autres grands articles à venir._

Bonne chance et bon lancement !

**Et enfin, si cela a été utile, veuillez appuyer sur le bouton ? ci-dessous. Merci !**

_Merci beaucoup à [Keywon](https://www.freecodecamp.org/news/minimum-viable-devops-919972dfd9e0/undefined) pour avoir fait des lancements de Hello Money et Goodbye Gun Stocks un succès et m'avoir présenté ce « problème » ; [Sacha Greif](https://www.freecodecamp.org/news/minimum-viable-devops-919972dfd9e0/undefined) et [Josh Owens](https://www.freecodecamp.org/news/minimum-viable-devops-919972dfd9e0/undefined) pour la collaboration sur les opérations de Sidebar ; [WooGenius](https://www.freecodecamp.org/news/minimum-viable-devops-919972dfd9e0/undefined) pour avoir compris les tests de charge avec moi._

Image d'en-tête : [Jeff Eaton](https://www.flickr.com/photos/jeffeaton/6586677927/)