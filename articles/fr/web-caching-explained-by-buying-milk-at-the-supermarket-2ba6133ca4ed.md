---
title: Le Cache Web Expliqué par l'Achat de Lait au Supermarché
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T04:45:23.000Z'
originalURL: https://freecodecamp.org/news/web-caching-explained-by-buying-milk-at-the-supermarket-2ba6133ca4ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XUwza_UlWCm8VJ8up0Q1cg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le Cache Web Expliqué par l'Achat de Lait au Supermarché
seo_desc: 'By Kevin Kononenko

  If you have ever bought milk at the supermarket, then you can understand server-side
  and browser-side caching.

  If you are an avid internet user (you probably are), you have benefitted from caching
  over and over again. But, you migh...'
---

Par Kevin Kononenko

**Si vous avez déjà acheté du lait au supermarché, alors vous pouvez comprendre le cache côté serveur et côté navigateur.**

Si vous êtes un utilisateur avide d'Internet (ce qui est probablement le cas), vous avez bénéficié du cache à maintes reprises. Mais vous ne savez peut-être pas quand ni comment il fait sa magie en coulisses.

Du point de vue d'un développeur, le cache facilite grandement la création d'applications web et de serveurs web performants. Au lieu de devoir constamment optimiser des serveurs submergés par des milliers de requêtes, les développeurs peuvent mettre en place des protocoles de cache pour simplifier la vie.

Puisque le cache peut faire la différence entre 1 seconde et 2 secondes pour charger une page, l'impact peut sembler un peu... décevant. Mais il est nécessaire si vous souhaitez gérer un grand volume d'utilisateurs.

Après avoir utilisé le cache dans une ancienne application web, j'ai réalisé qu'il devait y avoir une meilleure façon de l'expliquer que de simplement passer en revue la terminologie. J'ai remarqué qu'il correspondait très bien au parcours du lait, de la ferme à votre réfrigérateur, alors j'ai pensé que ce serait une meilleure façon de l'expliquer.

Pour comprendre ce guide, vous devez simplement connaître les [bases des serveurs web](https://blog.codeanalogies.com/2018/04/26/web-servers-explained-by-running-a-microbrewery/). Commençons !

### À quoi ressemblerait Internet sans cache ?

Avant de parler du cache, réfléchissons à ce à quoi ressemblerait Internet sans cache. Imaginez, un instant, que vous vivez dans les années 1700 ou 1800 dans une zone rurale. Vous possédez une ferme et il n'y a pas de réfrigération disponible. Vous avez quelques vaches sur votre ferme, mais leur lait n'est pas aussi précieux puisqu'il se gâtera rapidement.

Brève interruption : Certaines cultures n'ont toujours pas accès à la réfrigération. Elles boiront soit du lait cru directement du pis d'une vache, soit [mélangeront du lait avec des grains et le laisseront fermenter](https://seymourjacklin.co.uk/2010/11/01/milk-monday-dairy-in-the-days-before-pasteurisation-and-refrigeration/). Intéressant.

BREF, vous voulez vendre votre lait à d'autres personnes de votre village. Mais ils auront très peu de temps pour boire le lait. Disons qu'une de vos vaches peut produire un gallon de lait par jour. Mais si trop de personnes se présentent à votre ferme pour chercher du lait, vous devrez en renvoyer certaines chez elles et leur demander d'attendre jusqu'au lendemain.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UqjXaIdDFuVLfE5k)

De plus, vous ne pouvez même pas penser à ajouter plus de vaches et à développer votre exploitation, car votre distribution est si limitée. Seuls les autres membres de votre village peuvent acheter votre lait. Vous avez des limites claires.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LaOWTms2NkZtDFj5)

Sans cache, vous êtes limité par la puissance de calcul de vos serveurs. Le cache est utilisé pour charger des actifs statiques, comme :

* Images
* CSS
* Fichiers HTML statiques
* Fichiers JavaScript

Un serveur, par défaut, doit soumettre une nouvelle réponse pour chaque requête entrante. Mais une requête pour charger une page pourrait en réalité signifier 4 requêtes séparées — une pour chacune des catégories ci-dessus. Lorsque vous tenez compte des fichiers image plus volumineux, vos serveurs peuvent être submergés par des utilisateurs du monde entier. Les utilisateurs subiront alors des temps de chargement lents en attendant que leur page se charge.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4ajis8HoFZeo7SRf)

Idéalement, vous voudriez réduire la demande sur vos serveurs en stockant les réponses aux requêtes courantes. Votre serveur n'aurait pas besoin de traiter chaque nouvelle requête individuelle, mais votre cache pourrait fournir une réponse immédiate. Vous pourriez toujours payer pour plus de serveurs, mais cela peut entraîner des dépenses incontrôlables.

### Qu'est-ce que le cache côté serveur ?

Retour à notre scénario de ferme. Savez-vous ce qui rendrait la gestion d'une ferme laitière réussie beaucoup plus facile ?

Un supermarché avec réfrigération !

Ainsi, les gens n'auront pas besoin de se rendre à votre ferme et de consommer le lait immédiatement. Vous pourrez le conserver en toute sécurité pendant quelques semaines à la fois.

Le supermarché réduit beaucoup de stress sur votre ferme, car vos vaches ne seront pas tenues de produire en temps réel. Le supermarché gérera la demande. Vous devez simplement maintenir les vaches productives au quotidien. Mieux encore, les résidents de tous les villages environnants peuvent maintenant acheter du lait de votre ferme, car il sera toujours disponible dans le réfrigérateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kko1_aNf6X-cZzUy9IwF-A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jwi2U9sBznjtd_zZoszx6w.jpeg)

Tout comme un supermarché, un [cache côté serveur](https://www.digitalocean.com/community/tutorials/web-caching-basics-terminology-http-headers-and-caching-strategies) gérera les requêtes populaires et livrera le contenu beaucoup plus rapidement et de manière plus fiable.

Dans l'image ci-dessus, j'utilise le terme **proxy de cache**. Un proxy de cache est un serveur qui stocke les fichiers statiques utilisés pour répondre aux requêtes courantes. Un proxy de cache intercepta les requêtes courantes et livrera rapidement une réponse. Il empêche ces requêtes de solliciter vos principaux serveurs web.

Vous avez probablement un tas de questions comme :

1. Qu'est-ce qui détermine une requête "populaire" ?
2. Combien de temps le proxy mettra-t-il en cache les réponses ?

Cela nécessiterait un tutoriel plus long sur la configuration du cache, mais pour l'instant, vous devez connaître un concept important appelé **fraîcheur**. Le proxy de cache aura différents fichiers qui ont été mis en cache à différents moments, et il doit décider s'il doit toujours servir ces fichiers. Cela dépendra de votre **politique de cache**.

Cela fonctionne également comme le lait dans un supermarché. Un gestionnaire de supermarché doit décider combien de temps il conservera votre lait avant de le jeter. Les proxys de cache mesurent leur succès grâce à un **taux de succès de cache** — le pourcentage de contenu qui peut être servi via le serveur de cache.

### Qu'est-ce qu'un CDN ?

Jusqu'à présent, il y a un seul magasin d'alimentation qui vend votre lait. Bien que ce soit une grande amélioration, vous n'avez toujours aucun moyen de faire parvenir votre lait aux personnes en dehors de la zone de ce magasin local. Vous allez devoir ajouter plus de magasins si vous voulez développer votre exploitation.

Alors, disons que vous commencez à distribuer votre lait à plus de supermarchés. Maintenant, vous pouvez satisfaire les clients sur une zone géographique beaucoup plus large. Cela ressemble à un réseau de diffusion de contenu, ou CDN. Un CDN est une série de serveurs proxy (comme nous en avons discuté ci-dessus) situés dans le monde entier.

En tant qu'utilisateur final, vous pensez probablement que l'internet haut débit permet à la plupart des sites de se charger très rapidement. Cependant, ce n'est que parce qu'ils utilisent des CDN pour diffuser des fichiers statiques à grande vitesse !

Si vous êtes situé en Angleterre et que vous essayez de charger un fichier mis en cache dans un serveur en Virginie, vous subirez un certain délai, car le signal original ne peut voyager que si vite le long de milliers de kilomètres de câble. Un proxy de cache local au Royaume-Uni permettrait au site de se charger plus rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RvgDAlDHt24dcvBImoxCZQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*H8xPw2BZp_bAwgaUKeI2eA.jpeg)

Ainsi, vos serveurs peuvent envoyer une copie des actifs statiques à chacun de ces serveurs proxy au sein de votre réseau CDN, et ils peuvent gérer les requêtes locales jusqu'à ce que les actifs ne soient plus "fraîches". Certains fournisseurs de CDN courants incluent Rackspace, Akamai et Amazon Web Services.

### Qu'en est-il du cache du navigateur ?

Maintenant, les gens à travers le pays (ou le monde) peuvent ramener du lait froid de votre ferme chez eux. Il y a juste un problème — ils n'ont aucun moyen de le stocker chez eux. Vos clients doivent encore boire le lait assez rapidement après l'avoir acheté, puis retourner à l'épicerie pour en avoir plus. Donc, ce système ne sert toujours pas particulièrement bien les clients.

La solution ? Un réfrigérateur !

Avec un frigo, vous pouvez stocker le lait localement et éviter un retour au supermarché. En termes de cache, nous parlons d'un emplacement complètement séparé pour stocker des actifs statiques, car il est côté client, ou sur le même ordinateur que le navigateur. Notre serveur proxy était situé dans un endroit distant.

C'est génial pour des sites comme Facebook ou Amazon que vous visitez fréquemment. C'est aussi génial pour leurs coûts de serveur, car ils peuvent réduire le nombre de requêtes qu'ils doivent gérer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RncfZ7NATKE9ciV-F54ODg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wct_mY7Bbuvsd4pwyQJ5Dg.jpeg)

Une chose importante à noter — nous ne disons PAS que le lait arrive magiquement dans votre réfrigérateur ! Vous devez toujours faire cette requête initiale qui atteint soit le serveur, soit le serveur proxy. Après cela, vous pouvez mettre en cache certains des fichiers localement.

Comment votre navigateur sait-il quand demander de nouveaux fichiers au serveur ? Sinon, vous ne verriez jamais les versions mises à jour de ces fichiers locaux.

Eh bien, tout comme les producteurs de lait mettent une date sur leur emballage de lait, les serveurs ajouteront une sorte d'identifiant dans l'en-tête de la réponse HTTP. Il existe en réalité [4 systèmes séparés pour le cache HTTP](https://betterexplained.com/articles/how-to-optimize-your-site-with-http-caching/). Le scénario montré ci-dessus ressemble de près à la méthode de la "date d'expiration". Certaines des autres méthodes nécessitent toujours que votre navigateur vérifie avec le serveur avant d'envoyer le fichier mis en cache.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7yAXQNZN-0XzIQHB)

### Quand commencer à utiliser le cache

Disons que vous construisez votre première application web. Jusqu'à ce que vous ayez des milliers d'utilisateurs, vous n'aurez probablement pas besoin de vous soucier des protocoles de cache, car les coûts des serveurs resteront faibles. Cependant, à mesure que vous développez votre application, vous devrez mettre en place le cache si vous voulez que votre application se charge rapidement.

Heroku, par exemple, est un excellent outil pour déployer votre première application web. Mais il vous oblige à utiliser un [service séparé pour mettre en place le cache](https://devcenter.heroku.com/articles/http-caching), comme CloudFront ou CloudFlare d'Amazon. Cela prendra plus de temps à apprendre.

Côté navigateur, vous avez probablement rencontré le cache lorsque vous essayez de recharger une page avec de nouveaux actifs statiques, mais la page ne change tout simplement pas. Peu importe le nombre de fois où vous actualisez la page, rien ne change.

Cela est généralement dû à un protocole de cache côté navigateur. Pour contourner le cache de votre navigateur et demander de nouveaux actifs au serveur, vous pouvez utiliser **Cmd+Shift+R** sur un Mac ou **Ctrl+Shift+R** sur PC.

### Obtenez plus de tutoriels visuels

Avez-vous apprécié ce tutoriel ? Donnez-lui un "clap" ! Ou inscrivez-vous ici pour recevoir mes derniers tutoriels visuels du blog CodeAnalogies.