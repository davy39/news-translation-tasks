---
title: 'Une introduction approfondie au cache HTTP : Cache-Control & Vary'
subtitle: ''
author: Léo Jacquemin
co_authors: []
series: null
date: '2019-10-24T09:56:49.000Z'
originalURL: https://freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/martin-adams-uZZw2vh8eqY-unsplash.jpg
tags:
- name: cache-http
  slug: cache-http
- name: cache
  slug: cache
- name: cache-control
  slug: cache-control
- name: caching
  slug: caching
- name: http
  slug: http
seo_title: 'Une introduction approfondie au cache HTTP : Cache-Control & Vary'
seo_desc: 'Introduction - scope of the article

  This series of articles deals with caching in the context of HTTP. When properly
  done, caching can increase the performance of your application by an order of magnitude.
  On the contrary, when overlooked or complete...'
---

### Introduction - portée de l'article

Cette série d'articles traite du cache dans le contexte du HTTP. Lorsqu'il est bien fait, le cache peut augmenter les performances de votre application d'un ordre de grandeur. À l'inverse, lorsqu'il est négligé ou complètement ignoré, il peut entraîner des effets secondaires très indésirables causés par des serveurs proxy mal configurés qui, en l'absence d'instructions de cache claires, décident de mettre en cache et de servir des ressources obsolètes.

Dans la première partie de cette série, nous avons soutenu que le cache est le moyen le plus efficace d'augmenter les performances, mesuré par le temps de chargement de la page. Dans cette deuxième partie, il est temps de nous concentrer sur les mécanismes à notre disposition. En d'autres termes : comment fonctionne réellement le cache HTTP ?

Pour répondre à cette question, nous avons décidé de considérer le cas d'un cache vide qui commence progressivement à mettre en cache et à servir des ressources. Au fur et à mesure qu'il reçoit des requêtes HTTP entrantes, notre cache commencera à se comporter en conséquence. Servir la ressource depuis le cache lorsqu'une copie fraîche est disponible, varier sur plusieurs représentations, faire une requête conditionnelle... De cette manière, nous pouvons introduire chaque concept progressivement au fur et à mesure que nous en avons besoin.

Au début, notre cache vide n'aura d'autre choix que de transférer les requêtes au serveur d'origine. Cela nous permettra de comprendre comment les serveurs d'origine instruisent notre cache sur ce qu'il doit faire avec la ressource, comme s'il est autorisé à la stocker, et pour combien de temps. Pour cela, nous examinerons chaque directive Cache-Control et clarifierons certaines d'entre elles qui sont connues pour avoir des [significations conflictuelles](https://www.google.com/search?q=must-revalidate+vs+no-cache&oq=must+revalidate+vs+&aqs=chrome.1.69i57j0l3.3140j0j4&sourceid=chrome&ie=UTF-8).

Ensuite, nous verrons ce qui se passe lorsque notre cache reçoit une requête pour une ressource qu'il connaît déjà. Comment notre cache décide-t-il s'il peut réutiliser une réponse précédemment stockée ? Comment associe-t-il une requête HTTP donnée à une ressource particulière ? Pour répondre à ces questions, nous apprendrons sur les variations de représentation avec l'en-tête Vary.

Cet article va se concentrer sur les connaissances les plus précieuses du point de vue d'un développeur web. Par conséquent, les requêtes conditionnelles ne sont discutées que brièvement et seront le sujet d'un autre article.

Sans plus tarder, commençons par un aperçu de ce que nous allons explorer.

## L'arbre de décision du cache HTTP

Conceptuellement, un système de cache implique toujours au moins trois participants. Avec HTTP, ces participants sont le client, le serveur et le proxy de cache.

Cependant, lors de l'apprentissage du cache HTTP, nous vous encourageons fortement à ne pas penser au client comme à votre navigateur web typique, car de nos jours, ils sont tous livrés avec leur propre couche de cache HTTP. Cela rend difficile la séparation claire du navigateur et du cache. Pour cette raison, nous vous invitons à penser au client comme à un programme en ligne de commande sans interface graphique, tel que cURL ou toute application sans cache HTTP intégré.

Toutes les précautions mises à part, plongeons maintenant dans le sujet en regardant l'image suivante : l'arbre de décision du cache HTTP.

![Image](https://lh5.googleusercontent.com/4wnpOGgUnR2bJxcKqsUruzDIQrdmd5o956v85GGUARZKQYG77olAVBslIc_ZL1d0FZLVwlCuLLFeUzlSBYKaE-ALN-dWjijBbkzoVDuoTVQvG_GEAGABdZDXfl8TvBw2NdAgsnxk align="left")

Cette image illustre tous les chemins possibles qu'une requête peut prendre chaque fois qu'un client demande une ressource à un serveur d'origine derrière un système de cache. Un examen attentif de cette illustration révèle qu'il n'y a que quatre résultats possibles.

Séparer clairement ces résultats dans notre esprit est en fait très pratique, car chaque concept de cache important (instructions de cache, correspondance de représentation, requêtes conditionnelles et vieillissement des ressources) correspond à chacun d'entre eux.

Décrivons succinctement chacun d'eux en introduisant deux termes importants relatifs à la terminologie du cache HTTP : les hits de cache et les misses de cache.

### Hits et misses

Le premier résultat possible est lorsque le cache trouve une ressource correspondante et est autorisé à la servir, ce qui, dans le monde du cache, sont en effet deux choses distinctes. Ce résultat est ce que nous appelons communément un hit de cache, et c'est la raison pour laquelle nous utilisons des caches en premier lieu.

Lorsque qu'un hit de cache se produit, il décharge complètement le serveur d'origine et la latence est considérablement réduite. En fait, lorsque le hit de cache se produit dans le cache HTTP du navigateur, la latence est nulle et la ressource demandée est instantanément disponible.

Malheureusement, les hits de cache ne représentent qu'un des quatre résultats possibles. Les autres tombent dans la deuxième catégorie, également connue sous le nom de misses de cache, qui peuvent se produire pour seulement trois raisons.

La première raison pour laquelle un miss de cache se produit généralement est simplement lorsque le cache ne trouve aucune ressource correspondante dans son stockage. Cela est généralement un signe que la ressource n'a jamais été demandée auparavant, ou a été évincée du cache pour libérer de l'espace. Dans de tels cas, le proxy n'a d'autre choix que de transférer la requête au serveur d'origine, de télécharger complètement la réponse et de rechercher des instructions de cache dans les en-têtes de réponse.

La deuxième raison pour laquelle un miss de cache peut se produire est en fait tout aussi préjudiciable, où le cache détecte une représentation correspondante, une qu'il pourrait potentiellement utiliser. Cependant, la ressource n'est plus considérée comme *fraîche* - nous verrons comment exactement dans la section cache-control de cet article - mais est dite *obsolète.*

Dans un tel cas, le cache envoie un type spécial de requête, appelé une *requête conditionnelle* au serveur d'origine. Les requêtes conditionnelles permettent aux caches de récupérer des ressources uniquement si elles sont différentes de celles qu'ils ont dans leur stockage local. Puisque seul le serveur d'origine a toujours la représentation la plus récente d'une ressource donnée, les requêtes conditionnelles *doivent toujours* passer par toute la chaîne de proxy de cache jusqu'au serveur d'origine.

Ces requêtes spéciales n'ont que deux résultats possibles. Si la ressource n'a pas changé, le cache est instruit d'utiliser sa copie locale en recevant une réponse 304 Not Modified avec des en-têtes mis à jour et un corps vide. Ce résultat, le troisième sur notre liste, est appelé une validation réussie.

Enfin, le dernier résultat possible est lorsque la ressource a changé. Dans ce cas, le serveur d'origine envoie une réponse normale 200 OK, comme il le ferait si le cache était vide et avait transféré la requête. En d'autres termes, les misses de cache causés par un cache vide et une validation échouée produisent exactement la même réponse HTTP.

Pour mieux visualiser ces quatre chemins, il est utile de les imaginer dans une timeline, comme illustré ci-dessous.

![Image](https://lh6.googleusercontent.com/eV4YKvBdmE_SD0dSlu7Gt4oQKW9IpekfHv5R_odd4m4Hq4HO71cgGez9MtxtGBd5ghP36tfWoj8OTMzE-N0iWiMI5WgOusUl7dOXUtLQM7MvywGqSaYuBRbS4oH-rbXdpdwTWW6h align="left")

Au début, le cache est vide. Le flux de requêtes commence par un miss de cache (résultat de cache vide). Sur le chemin du retour, le cache lirait les instructions de cache et stockerait la réponse. Toutes les requêtes ultérieures pour cette ressource particulière entraîneraient des hits de cache, jusqu'à ce que la ressource devienne obsolète et doive être révalidée.

Lors d'une première révalidation, il est possible que la ressource n'ait pas changé, d'où l'envoi d'un 304 Not Modified.

Ensuite, la ressource est finalement mise à jour par un client, généralement avec une requête PUT ou PATCH. Lorsque la prochaine requête conditionnelle arrive, le serveur d'origine détecte que la ressource a changé et répond par un 200 OK avec des en-têtes ETag et Last-Modified mis à jour.

Connaître les hits et misses de cache ainsi que les 4 chemins possibles que chaque requête cacheable pourrait prendre devrait vous donner un bon aperçu de comment fonctionne le cache.

Bien que les aperçus ne puissent vous mener que jusqu'à un certain point. Dans la section suivante, nous donnerons une explication détaillée de comment les serveurs d'origine communiquent les instructions de cache.

### Comment les serveurs d'origine communiquent les instructions de cache

Les serveurs d'origine communiquent leurs instructions de cache aux proxies de cache en aval en ajoutant un en-tête Cache-Control à leur réponse. Cet en-tête est une addition HTTP/1.1 et remplace l'en-tête Pragma obsolète, qui n'a jamais été un standard.

Les valeurs de l'en-tête Cache-Control sont appelées directives. La spécification en définit beaucoup, avec divers usages et [support par les navigateurs](https://www.mnot.net/blog/2017/03/16/browser-caching). Ces directives sont principalement utilisées par les développeurs pour communiquer les instructions de cache. Cependant, lorsqu'elles sont présentes dans une requête HTTP, les clients peuvent également influencer la décision de cache. Prenons maintenant le temps de décrire les directives les plus utiles.

### max-age

La première directive Cache-Control importante à connaître est la directive max-age, qui permet à un serveur de spécifier la durée de vie d'une représentation. Elle est exprimée en secondes. Par exemple, si un cache voit une réponse contenant l'en-tête Cache-Control: max-age=3600, il est autorisé à stocker et à servir la même réponse pour toutes les requêtes ultérieures pour cette ressource pendant les 3600 prochaines secondes.

Pendant ces 3600 secondes, la ressource sera considérée comme fraîche et des hits de cache se produiront. Passé ce délai, la ressource deviendra obsolète et la validation prendra le relais.

### no-store, no-cache, must-revalidate

Contrairement à max-age, les directives no-store, no-cache et must-revalidate concernent l'instruction aux caches de ne pas mettre en cache une ressource. Cependant, elles diffèrent de manière subtile.

no-store est assez explicite, et en fait, il fait même un peu plus que ce que le nom suggère. Lorsqu'il est présent, un cache conforme HTTP/1.1 ne doit pas tenter de stocker quoi que ce soit, et doit également prendre des mesures pour supprimer toute copie qu'il pourrait avoir, soit en mémoire, soit stockée sur disque.

La directive no-cache, en revanche, est sans doute beaucoup moins explicite. Cette directive signifie en fait de ne jamais utiliser une copie locale sans d'abord valider avec le serveur d'origine. Ce faisant, elle empêche toute possibilité de hit de cache, même avec des ressources fraîches.

En d'autres termes, la directive no-cache indique que les caches doivent révalider leurs représentations avec le serveur d'origine. Mais voici une autre directive, maladroitement nommée... must-revalidate.

Si cela commence à vous sembler confus, rassurez-vous, vous n'êtes pas seul. Si ce que l'on veut, c'est de ne pas mettre en cache, il faut utiliser no-store au lieu de no-cache. Et si ce que l'on veut, c'est de toujours révalider, il faut utiliser no-cache au lieu de must-revalidate.

Confus, en effet.

Quant à la directive must-revalidate, elle est utilisée pour interdire à un cache de servir une ressource obsolète. Si une ressource est fraîche, must-revalidate permet parfaitement à un cache de la servir sans forcer aucune révalidation, contrairement à no-store et no-cache. C'est pourquoi cet en-tête doit toujours être utilisé avec une directive max-age, pour indiquer un désir de mettre en cache une ressource pendant un certain temps et, lorsqu'elle est devenue obsolète, imposer une révalidation.

En ce qui concerne ces trois dernières directives, nous trouvons le choix des mots pour décrire chacune d'entre elles particulièrement confus : no-store et no-cache sont exprimés négativement alors que must-revalidate est exprimé positivement. Leurs différences seraient probablement plus évidentes si elles étaient exprimées de la même manière.

Par conséquent, il est utile de penser à chacune d'entre elles exprimée en termes de ce qui n'est pas autorisé :

* **no-store :** ne jamais stocker quoi que ce soit

* **no-cache :** ne jamais avoir de hit de cache

* **must-revalidate :** ne jamais servir de ressource obsolète

Techniquement, ces directives peuvent apparaître dans le même en-tête Cache-Control. Il n'est pas rare de les voir combinées sous forme de liste de valeurs séparées par des virgules. Beaucoup de sites web populaires semblent encore se comporter de manière très conservative, envoyant des pages HTML avec l'en-tête suivant :

Cache-Control: no-cache, no-store, max-age=0, must-revalidate

Lorsque vous tombez sur cela, l'intention derrière est généralement assez claire : l'équipe de développement web veut s'assurer que la ressource ne soit jamais servie obsolète à personne.

Cependant, de telles lignes de cache-buster ne sont probablement plus nécessaires. Un [travail précédent](https://github.com/web-platform-tests/wpt/pull/5137) réalisé en 2017 a déjà montré que les navigateurs sont en fait plutôt conformes à la spécification en ce qui concerne les directives de réponse Cache-Control. Par conséquent, sauf si vous prévoyez de configurer une pile de cache avec des logiciels vieillis de plusieurs décennies, vous devriez être en mesure d'utiliser uniquement les directives dont vous avez besoin. Les combinaisons les plus populaires seront analysées dans un autre article.

### public, private

Les dernières directives importantes que nous n'avons pas encore discutées sont un peu différentes, car elles contrôlent quels types de caches sont autorisés à mettre en cache les ressources. Il s'agit des directives public et private, private étant celle par défaut si non spécifiée.

![Image](https://lh3.googleusercontent.com/kiq8Sq0igyLzRFkX4qddKF4y6xdltA1rXwjBOaqvWlqD1mJbaQe2WuLIparaOSfQ36iUT4kaHSKxzBY4TVbaVXtq7w3W6Hhq7QllsTf6WD2rAFq9MRG2AFNMI-EmUNmLn1TfmKnC align="left")

Les caches privés sont ceux qui sont censés être utilisés par un seul utilisateur. Typiquement, il s'agit du cache du navigateur web. Les CDN et les reverse-proxies, au contraire, gèrent les requêtes provenant de plusieurs utilisateurs.

Pourquoi devons-nous distinguer ces deux types de caches ? La réponse est simple : la sécurité, comme l'illustre l'exemple suivant.

De nombreuses applications web exposent des endpoints de commodité qui reposent sur des informations provenant d'ailleurs que l'URL. Si deux utilisateurs accèdent à leur profil en demandant /users/me, à [https://api.example/com](https://api.example/com/), et que leur identifiant utilisateur réel est caché dans un jeton Authorization: Bearer 4Ja23ç42…. le cache ne pourra pas dire qu'il s'agit en fait de deux ressources très différentes.

![Image](https://lh3.googleusercontent.com/48yzQ_RyKvQoWxgPmvvwijI74hSD_NNfjViTUDHeNvkmd-U-2wCqgCZWnmjRyTYNqwRGJPZJ-GuIoFbflCT_x6CCB6wIJGdHluEBK9BahnkL7pdzEmV9kwinkwJibC5JTLKAAGct align="left")

En effet, lors de la construction de leur clé de cache, les caches n'inspectent pas les en-têtes HTTP sauf si on leur donne des instructions spécifiques pour le faire, comme nous le verrons dans la section suivante.

### s-maxage

La directive s-maxage est similaire à la directive max-age, sauf qu'elle ne s'applique qu'aux caches publics, qui sont également appelés caches *partagés* (d'où le préfixe s-). Si les deux directives sont présentes, s-maxage prendra le pas sur max-age sur les caches publics et sera ignorée sur les caches privés.

Lors de l'utilisation de cette directive, la règle générale est de toujours s'assurer que la valeur de s-maxage est inférieure à celle de max-age. La logique derrière cette règle est que plus vous êtes proche de l'origine, plus il est approprié de vérifier fréquemment quelle est la dernière représentation.

Imaginez que vous mettez en cache pendant un jour dans le proxy, et une heure dans les navigateurs.

Chaque fois qu'un navigateur demanderait une ressource aux serveurs en amont, nous pourrions savoir *à l'avance* que le proxy ne contactera pas le serveur d'origine pendant au moins un jour. Par conséquent, pourquoi ne pas mettre le même TTL directement dans les navigateurs ? En conclusion, il est une bonne pratique de toujours laisser un TTL plus long dans max-age que dans s-maxage.

**stale-while-revalidate et stale-if-error**  
Ces deux directives ne font pas techniquement partie de la spécification originale mais font partie d'une [extension](https://tools.ietf.org/html/rfc5861) qui a été décrite pour la première fois il y a plus de [10](https://www.mnot.net/blog/2007/12/12/stale) ans. Bien que leur support par les navigateurs soit limité, [certains](https://www.fastly.com/blog/stale-while-revalidate-stale-if-error-available-today) CDN populaires les supportent depuis plus de 5 ans !

Bien que stale-while-revalidate soit assez utile. Comme son nom l'indique, il permet à un cache de *« [...] retourner immédiatement une réponse obsolète tout en la révalidant en arrière-plan, masquant ainsi la latence (à la fois dans le réseau et sur le serveur) aux clients ».*

Cette extension de cache s'avère vraiment utile pour des éléments comme les images, où la réduction de la latence est cruciale pour l'expérience utilisateur, et où avoir une version obsolète pendant quelques secondes est souvent mieux qu'une image qui se télécharge péniblement.

Quant à stale-if-error, il permet à un cache de servir une version obsolète si le serveur d'origine retourne un code d'état 5xx. Cela donne aux développeurs une chance de corriger les problèmes potentiels pendant une période de grâce où les clients sont protégés des pages d'erreur irritantes.

Prenez le cas d'un script tiers de météo. Si le serveur de météo est inaccessible pendant quelques minutes, il est probablement préférable d'afficher une prévision légèrement obsolète pendant ce laps de temps, plutôt que de voir une partie de la page être vide (ou une page entièrement vide si le code ne gère pas les échecs de chargement des scripts tiers).

### Ce que nous ne savons pas encore

Après avoir examiné ces directives Cache-Control, nous comprenons maintenant comment les applications distribuées sur le web tendent à exploiter les mécanismes de cache HTTP de multiples façons, selon leurs besoins.

Cependant, ce que nous ne comprenons pas encore, c'est ce que les logiciels de cache font réellement avec la réponse qu'ils reçoivent. Ils devront probablement la stocker quelque part afin de la récupérer plus tard. C'est l'idée centrale de tout système de cache après tout.

Dans des circonstances normales, cela ressemble certainement à ce que nous appellerions un détail d'implémentation. Il devrait être suffisamment clair que les ressources sont effectivement stockées d'une certaine manière. Pourtant, dans ce cas, apprendre un peu plus est en fait crucial.

Négliger les mécanismes qui régissent la manière dont les logiciels de cache mappent les objets de l'espace des réponses HTTP à leur espace de stockage peut avoir des conséquences vraiment inattendues, comme servir un document chinois encodé en brotli, à un utilisateur qui ne comprend pas le chinois, utilisant un navigateur incapable de décoder le brotli 🉐_(ツ)_/🉐

## Comment les caches stockent et récupèrent les ressources

Bien que peu probable, puisque la plupart des navigateurs peuvent décoder le brotli - et puisque la plupart des gens savent comment dire 说中文 - la situation précédente peut encore facilement se produire. Pour comprendre pourquoi c'est le cas, il faut considérer *comment* les caches stockent leurs représentations.

En vertu de ce qu'ils tentent d'accomplir, la plupart des logiciels de cache doivent être capables de récupérer rapidement des documents texte simples. Pour ce faire, une stratégie très simple mais puissante consiste à utiliser un magasin clé-valeur. Cette stratégie convient bien aux représentations en mémoire. Par conséquent, la question à laquelle il faut répondre lors de la conception est la suivante : comment construire une clé de cache à partir d'une réponse HTTP ?

Ce que nous cherchons ici est un moyen d'*identifier* de manière unique une *ressource*. Heureusement, c'est exactement pourquoi les [URI](https://tools.ietf.org/html/rfc3986) - Uniform Resource Identifiers - ont été inventés en premier lieu !

Mais les URI ne disent pas toute la vérité sur les ressources. Ils ne les décrivent jamais entièrement, ne serait-ce que parce que les ressources changent avec le temps.

Les sites web sont rebrandés, de nouveaux contenus sont publiés et les utilisateurs mettent à jour leur profil. Certes, pas pour les mêmes raisons ou à la même fréquence, mais toutes les ressources finiront par changer. En fait, toute la spécification des requêtes conditionnelles est basée sur cette seule observation : *rien n'est permanent sauf le* [*changement*](https://en.wikiquote.org/wiki/Heraclitus)*.*

Mettons de côté les citations philosophiques, il existe cependant une autre raison indépendante du temps pour laquelle les ressources changent. En effet, à tout moment, les ressources peuvent être disponibles en plusieurs représentations. C'est pourquoi nous avons la négociation de contenu.

Les en-têtes de requête HTTP Accept, Accept-Language, Accept-Encoding, Accept-Charset (et quelques autres en-têtes qui ne font pas strictement partie de la négociation de contenu) ajoutent une autre dimension sur laquelle les représentations peuvent différer. Ainsi, le problème de trouver une bonne clé de cache devient plus compliqué. Puisque toutes ces représentations partagent la même URI, les caches doivent avoir un moyen de les distinguer afin de servir la bonne représentation à chaque client, en respectant la négociation de contenu.

Et puisque seuls les serveurs d'origine savent quelles représentations différentes sont disponibles, c'est à nouveau la responsabilité du serveur d'origine d'indiquer à un cache sur la base de quels en-têtes il générera une représentation différente. Pour ce faire, les serveurs d'origine doivent ajouter un en-tête Vary [header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#The_Vary_response_header) contenant la valeur des en-têtes de requête qui provoquent la génération de représentations différentes.

Lorsque les caches voient une réponse provenant d'un serveur d'origine avec, par exemple, l'en-tête Vary: Accept-Language, il examinera la valeur de l'en-tête Accept-Language, telle que fr-FR, et utilisera cette valeur pour construire une clé de cache plus spécifique, peut-être comme https://example.net/home.html**fr-FR**.

La stratégie d'implémentation réelle est de peu d'importance pour nous. Modifier la clé de cache n'est peut-être même pas la meilleure façon de le faire. Il doit d'une manière ou d'une autre utiliser la *valeur* de l'en-tête pour différencier les représentations.

L'en-tête Vary peut en fait pointer vers plus d'un en-tête, lorsque les ressources sont disponibles en plusieurs représentations. Sélectionner une clé de cache lorsque plusieurs en-têtes sont impliqués n'est pas vraiment plus compliqué qu'avec un seul en-tête. Le vrai problème lorsque l'on varie sur plusieurs dimensions est l'explosion combinatoire.

Malheureusement, il n'y a pas de moyen de contourner cela. Si vous devez mettre en cache et servir vos ressources en plusieurs représentations, vous devez payer le coût d'un grand stockage. Si vous décidez de réduire votre cardinalité de variation, certains de vos utilisateurs recevront des hits de cache pour des réponses qui ne correspondront pas à leurs requêtes.

D'un autre côté, si vous variez correctement sur tout, et que vous n'avez pas assez d'espace de stockage, il est probable que vos utilisateurs ne verront pas de hits de cache de sitôt.

Maintenant, il est important de savoir que ce n'est un problème que si vous décidez d'utiliser un cache public, pour lequel deux requêtes différentes provenant de deux utilisateurs différents exécutent le même code, au niveau du proxy. Si vous décidez de tirer parti uniquement du cache du navigateur, alors vous pouvez sauter l'en-tête Vary et servir les ressources dans autant de représentations que vous le souhaitez. Cela est dû au fait que chaque cache de navigateur ne mettra en cache que les représentations correspondant aux préférences de l'utilisateur. C'est une bonne nouvelle !

Mais ne nous emballons pas trop vite. Comme nous l'avons dit, les caches utilisent la *valeur* de l'en-tête comme entrée pour générer une clé de cache plus spécifique. Mais qu'est-ce qui garantit que toutes ces valeurs sont bien formatées ? Absolument rien ! C'est la conséquence plutôt gênante du principe de robustesse du [père](https://tools.ietf.org/html/rfc2468) [RFC](https://en.wikipedia.org/wiki/Robustness_principle). Les serveurs HTTP sont en effet très *libéraux dans ce qu'ils acceptent*.

Cependant, il y a de l'espoir.

Considérons le cas d'un serveur d'origine qui ne peut produire une représentation que dans deux langues différentes, les caches doivent être capables de regrouper les valeurs Accept-Content entrantes telles que fr, fr-FR, fr_FR_.._ en quelque chose comme FR. Sinon, tout comme avant avec l'explosion combinatoire, le nombre de représentations explosera, mais dans ce cas, pour une raison erronée.

Le processus par lequel toutes ces représentations sont regroupées est appelé *normalisation* et est souvent effectué au niveau du cache. De nombreux caches offrent des utilitaires de configuration ou leurs propres langages pour traiter ces situations. Parfois, les fonctions sont même déjà écrites, ou des extraits peuvent facilement être trouvés sur Internet. L'image suivante illustre le processus pour l'infâme en-tête User-Agent.

![Image](https://lh3.googleusercontent.com/YjJ67y4VX8-kzzVY78G6ICtdafwsx_M6_n9ce30Qv9jVYU3LrBXQrrxb13VkPjpm9WpBNs6JParrx5VEbtuKwKr5cTSUmMiXcayum2RTwRKho3c6R5iqmYj0lYqM5f6Klb2leIAo align="left")

Fastly, un CDN populaire, a [échantillonné](https://www.fastly.com/blog/best-practices-using-vary-header) 100 000 requêtes et a trouvé que l'en-tête Accept-Encoding était exprimé de 44 manières différentes ! Quant à l'en-tête User-Agent, ils en ont trouvé près de... 8000 différents ! Sans normalisation, il est probable que le cache ne verra jamais de hit.

Cela conclut la section sur la variation des représentations. À ce stade, nous savons comment instruire les caches pour stocker nos ressources, et avons appris à utiliser l'en-tête Vary pour éviter les accidents lors de l'utilisation de caches publics. Nous avons maintenant couvert suffisamment de la spécification pour être en mesure de mettre en cache les ressources de manière efficace.

### Idées fausses courantes

À ce stade, vous devriez avoir une compréhension approfondie de comment fonctionne le cache HTTP. Le contrôle de fraîcheur, les représentations des ressources et les hits de cache ne sont plus des concepts mystérieux pour vous. Et si vous commencez à vous sentir puissant avec toutes ces connaissances, nous avons une bonne nouvelle pour vous : nous avons couvert une grande partie de la spécification, et vous savez maintenant à peu près tout ce qui est nécessaire pour être opérationnel.

Mais ne vous y trompez pas. Le cache *est* un sujet complexe.

L'expérience nous a montré que, sauf si vous traitez cela au quotidien, ce qui peut être clair aujourd'hui deviendra rapidement quelque chose de plutôt flou après quelques semaines. Par conséquent, nous avons décidé de conclure cet article en dissipant deux idées fausses courantes qui sont trop faciles à faire.

### Contrôle de fraîcheur et validation

Cela peut sembler évident après avoir lu les sections précédentes, mais cela vaut la peine d'être répété plusieurs fois. Le contrôle de fraîcheur et la validation (*que nous avons légèrement discutée au début*) sont deux mécanismes très distincts qui servent deux objectifs très différents, et impliquent des requêtes HTTP entre différentes parties.

* Le contrôle de fraîcheur se produit toujours dans un cache **et est uniquement basé sur le temps**

* Les validations se produisent toujours dans le serveur d'origine et sont basées **à la fois sur le temps et sur les identifiants (ETags)**

C'est quelque chose que nous trouvons important de nous rappeler. Cela signifie qu'une fois que le cache a reçu des instructions temporelles, il peut - et croyez-le, il le fera - servir des ressources sans jamais contacter le serveur d'origine jusqu'à ce que le minuteur expire.

Par exemple, si le fichier HTML de votre application web atteint un navigateur et que la réponse HTTP contient l'en-tête Cache-Control: max-age=86400, le navigateur servira joyeusement la même version de votre application pendant une journée. Dans ce cas, le navigateur la servirait pendant une journée sans aucune action possible de votre part ou de celle de quiconque, sauf l'utilisateur, si jamais il décidait de vider le cache de son navigateur.

Si vous pensez que tout le monde peut faire des erreurs, et qu'une journée n'est pas si grave, eh bien, préparez-vous : la valeur maximale de max-age est... 31536000 secondes ! C'est-à-dire, *une année.* C'est la raison pour laquelle les fichiers HTML sont très dangereux à mettre en cache de cette manière, et devraient généralement être déclarés avec Cache-Control: no-cache.

### Fraîcheur et représentation la plus récente

Une autre idée fausse est de croire que les hits de cache et la fraîcheur ont quelque chose à voir avec le fait d'avoir la dernière version disponible d'une ressource. C'est ce que nous essayons tous d'atteindre, mais on ne peut jamais vraiment savoir si la ressource qui nous a été servie depuis un cache est effectivement la version la plus à jour. En fait, cela reste vrai même en l'absence de cache. Cela a à voir avec la nature des applications distribuées : les actions des autres peuvent changer les choses avec lesquelles nous interagissons à tout moment.

Lors de l'interrogation de l'état de l'application, l'en-tête ETag doit toujours être utilisé pour toujours laisser le serveur savoir quelle est notre compréhension actuelle de l'état de l'application. Et si cela ne correspond pas à celle du serveur, des 409 Conflict sont attendus d'être reçus côté client.

## Conclusion

Tout au long de cet article, nous avons décrit comment fonctionne réellement le cache. Ce serait un bon moment pour lancer un serveur de développement local et bidouiller avec ces deux en-têtes principaux : Cache-Control et Vary pour les voir en action.

Nous avons commencé par donner un aperçu de comment fonctionne le cache, illustrant les quatre chemins possibles qu'une requête peut prendre : le chemin heureux (cache hit) et les 3 façons possibles d'avoir un cache miss : cache vide, révalidation échouée et révalidation réussie. Cet aperçu seul donne la possibilité de comprendre comment des topologies de cache complexes peuvent s'emboîter.

Ensuite, nous avons approfondi et examiné toutes les directives Cache-Control les plus utiles, et clarifié certaines différences subtiles qui sont toutes facilement manquées.

Nous avons également examiné l'en-tête Vary et la différence fondamentale entre les ressources et les représentations, pour éviter de servir la mauvaise *représentation* au bon client.

Enfin, nous avons pris le temps de tout passer en revue sous l'angle des idées fausses courantes que vous pourriez rencontrer, et espérons vous avoir aidé à les éviter.

Dans le prochain article, nous appliquerons toutes ces connaissances pour configurer un environnement de laboratoire local dans lequel nous mettrons le feu à une innocente application node.js avec un outil de test de charge, juste avant de la sauver avec l'aide d'un logiciel de cache populaire.

Restez à l'écoute !

### Pour aller plus loin :

La spécification officielle sur le matériel que nous avons couvert (et d'autres choses)  
[https://tools.ietf.org/html/rfc7234#section-5.3](https://tools.ietf.org/html/rfc7234#section-5.3)

Les fondamentaux de Google Web  
[https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#defining-optimal-cache-control-policy](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#defining-optimal-cache-control-policy)

À propos de l'en-tête Cache-Control :  
[https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Cache-Control](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Cache-Control)

À propos de l'en-tête Vary :  
[https://www.smashingmagazine.com/2017/11/understanding-vary-header/](https://www.smashingmagazine.com/2017/11/understanding-vary-header/)  
[https://www.fastly.com/blog/best-practices-using-vary-header](https://www.fastly.com/blog/best-practices-using-vary-header)  
[https://www.fastly.com/blog/getting-most-out-vary-fastly](https://www.fastly.com/blog/getting-most-out-vary-fastly)  
[https://www.fastly.com/blog/understanding-vary-header-browser](https://www.fastly.com/blog/understanding-vary-header-browser)