---
title: 'Services RESTful Partie II : Contraintes et Objectifs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-26T04:26:24.000Z'
originalURL: https://freecodecamp.org/news/restful-services-part-ii-constraints-and-goals-530b8f6298b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dum9oGRK7CWpbIOsmmyDcg.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Services RESTful Partie II : Contraintes et Objectifs'
seo_desc: 'By Sanchit Gera

  In Part I of this series I wrote about HTTP and its constructs as they apply to
  web service design.

  HTTP is only a small part of what goes into writing modern web services.

  This post is about how you apply these constructs to create m...'
---

Par Sanchit Gera

Dans [la Partie I de cette série](https://medium.freecodecamp.com/restful-services-part-i-http-in-a-nutshell-aab3bfedd131#.2x2nmd2ie), j'ai écrit sur HTTP et ses constructions telles qu'elles s'appliquent à la conception de services web.

HTTP n'est qu'une petite partie de ce qui entre dans l'écriture de services web modernes.

Cet article traite de la manière dont vous _appliquez_ ces constructions pour créer des services maintenables et robustes.

### Définition de REST

REST signifie **RE**présentation **S**tate **T**ransfer. C'est un _style architectural_. Cela signifie que REST n'impose pas de norme formelle pour déterminer si un service web est RESTful ou non. Plutôt, il a un ensemble de contraintes _larges_, chacune avec un objectif spécifique en tête.

Ces contraintes ont été introduites pour la première fois par Roy Fielding, qui était l'un des co-auteurs de la spécification HTTP en 2000.

### Contraintes de Fielding

Fielding a créé ces contraintes avec l'objectif ultime de rendre les applications plus rapides, plus fiables et plus faciles à mettre à l'échelle.

En tant que concepteur de services web, votre service doit essayer de se conformer à ces contraintes aussi étroitement que possible afin d'en tirer les avantages. Alors, plongeons-nous dans ces contraintes.

#### Contrainte #1 : Architecture Client-Serveur

La première contrainte proposée par REST est la séparation du serveur de son client. Vous devriez encourager la séparation des préoccupations entre votre serveur et vos clients chaque fois que possible. Votre objectif devrait être de maximiser la division du travail — et de minimiser le chevauchement — entre les deux.

Le serveur, ou _back end_, est généralement responsable du stockage des données persistantes de votre application, ainsi que de toute la logique métier nécessaire pour interagir avec elles. Cela peut inclure l'authentification des utilisateurs, l'autorisation, la validation des données, et ainsi de suite.

Le client, ou _front end_, est responsable de l'envoi de requêtes au service, puis de faire quelque chose de significatif avec la réponse qu'il reçoit.

Le client lui-même peut être un service web, auquel cas il consomme simplement les données. Alternativement, il peut être orienté utilisateur. Un exemple de cela serait une application web ou mobile. Ici, il est également responsable à la fois de _présenter_ les données à l'utilisateur et de présenter une _interface_ pour que l'utilisateur interagisse avec elles.

Vous devriez être en mesure de traiter chacun de ces deux composants comme une [boîte noire](https://en.wikipedia.org/wiki/Black_box) l'un par rapport à l'autre. Ainsi, ils peuvent être modifiés indépendamment. Cela encourage la modularité au sein de l'application.

Ce concept n'est pas unique aux applications RESTful, ou même aux applications web. La plupart des développeurs essaient de [diviser leurs projets](https://msdn.microsoft.com/en-us/library/ee658124.aspx?f=255&MSPPError=-2147217396) en composants indépendants de toute façon. Mais en énonçant cela comme une contrainte explicite de la conception RESTful, Fielding encourage davantage cette pratique.

Enfin, réduire le nombre de choses dont le serveur est responsable réduit la quantité de logique nécessaire. Cela permet à son tour une meilleure évolutivité et une performance accrue.

#### Contrainte #2 : Sans état

La prochaine contrainte importante proposée par REST est celle de l'absence d'état.

De manière générale, l'objectif principal d'un service sans état est de rendre les requêtes entrantes autosuffisantes et de les exécuter en isolation complète.

Chaque requête doit contenir toutes les informations dont le serveur pourrait avoir besoin pour la traiter correctement et y répondre. En d'autres termes, le serveur n'a pas besoin d'utiliser les informations des requêtes précédentes. La responsabilité de maintenir l'état de l'application d'un client est ainsi confiée au client lui-même.

Pour comprendre cela, considérons un service web très simple responsable de la réponse aux requêtes de recherche d'un utilisateur. La représentation exacte de l'entité recherchée est sans importance. Ce qui est important, c'est que, au lieu de retourner des centaines de résultats de recherche en une seule fois, le serveur utilise la _pagination_ : ne retournant que 10 résultats à la fois parmi un ensemble de résultats arbitrairement grand.

Dans un modèle de développement traditionnel "avec état", le serveur peut être conçu de manière à suivre tous ses clients, ainsi que toutes les pages qu'ils ont déjà consultées.

Ainsi, lorsqu'une requête arrive pour une nouvelle page, le serveur est en mesure de rechercher le client dans son système et de déterminer la page la plus récente qu'il a reçue.

Ensuite, le serveur peut procéder à la réponse avec la page _suivante_, et mettre à jour son système pour refléter cela. Cela continue pendant que le client continue de naviguer dans l'ensemble des résultats.

Dans une approche alternative, sans état, la responsabilité de maintenir son état est décentralisée et transférée au client. Le client doit alors spécifier les numéros de page _réels_ des résultats qu'il souhaite, au lieu de demander la page suivante. Par exemple :

```
GET http://my-awesome-web-service.com/pages/1GET http://my-awesome-web-service.com/pages/3
```

Une approche sans état apporte avec elle un couple d'avantages majeurs. Tout d'abord, le suivi de l'état du client devient de plus en plus exigeant pour un serveur à mesure que le nombre de clients augmente.

Deuxièmement, et plus important encore, un service sans état est également **facilement distribuable**. Si un serveur est responsable de la maintenance des informations sur l'état d'une application, il est alors impératif que les requêtes futures soient acheminées vers le serveur qui _stocke_ ces informations.

S'il y a des centaines de serveurs responsables du traitement des requêtes entrantes, il doit alors y avoir un mécanisme en place pour garantir que les requêtes d'un client spécifique aboutissent toujours à une instance de serveur spécifique.

Dans le cas où une instance de serveur tombe en panne, toutes les informations sur l'état d'un client qui étaient stockées sur ce serveur tombent avec lui.

Bien sûr, vous pourriez imaginer une architecture où les instances de serveur peuvent partager des données entre elles. Mais cela ajoute une complexité considérable.

Un service sans état, en revanche, simplifie grandement l'ajout et la suppression d'instances de serveur de manière ad hoc. Vous pouvez ensuite équilibrer davantage la charge entre elles selon les besoins.

Puisque les serveurs sont agnostiques aux requêtes entrantes, la mise à l'échelle est simplement une question d'ajout de plus de serveurs à l'équilibreur de charge. De même, la suppression de serveurs — intentionnellement ou non — n'affecte pas la fiabilité d'un service.

Bien sûr, cette simplicité a un coût. Le fait que le client joigne des données identiques à chaque requête est une source potentielle de redondance. La bande passante n'est pas gratuite, donc toute information supplémentaire transférée ajoute une certaine quantité de surcharge.

#### Contrainte #3 : Cache

La troisième contrainte est celle de la mise en cache explicite. L'idée est de marquer les messages retournés par un service comme explicitement mis en cache ou non mis en cache. S'ils sont mis en cache, le serveur doit déterminer la _durée_ pendant laquelle la réponse est valide.

Si le client a accès à une réponse mise en cache valide pour une requête donnée, il évite de répéter la même requête. Au lieu de cela, il utilise sa copie mise en cache. Cela aide à soulager une partie du travail du serveur et contribue ainsi à l'évolutivité et à la performance.

C'est une forme de _réplication optimiste_ — également connue sous le nom de _réplication paresseuse_ — où le service ne cherche pas à garantir une cohérence à 100 % entre lui-même et ses clients, sauf si cela est absolument critique. Au lieu de cela, il fait ce sacrifice en échange d'un gain de performance perçue.

Par exemple, une API correspondant à une plateforme de blogging peut choisir de rendre la liste des articles de blog mise en cache pendant quelques minutes si elle sait que la fréquence à laquelle les gens essaient d'**accéder** aux articles dépasse de loin la fréquence à laquelle de nouveaux articles sont créés. En conséquence, les utilisateurs peuvent **occasionnellement** se voir présenter des données obsolètes, mais le système dans son ensemble fonctionne mieux.

Bien sûr, la possibilité de mise en cache d'une ressource et sa durée ne sont pas universelles et nécessitent une certaine réflexion. Si vous choisissez incorrectement, cela peut frustrer vos utilisateurs.

Les services web atteignent généralement la mise en cache en utilisant l'en-tête standard **Cache-Control**. Parfois, ils le font en conjonction avec d'autres en-têtes spécifiés par HTTP.

L'en-tête Cache-Control sert effectivement de commutateur, déterminant si un navigateur doit mettre en cache la réponse en question.

Les ressources marquées comme _privées_ sont mises en cache uniquement par le client et sont donc limitées à ce client uniquement.

Les ressources marquées _publiques_, en revanche, peuvent être mises en cache par un ou plusieurs proxys intermédiaires entre le service et le client.

En conséquence, ces ressources peuvent potentiellement être servies à plusieurs utilisateurs. Alternativement, on peut passer l'argument _no-cache_ et arrêter complètement toute mise en cache de la ressource.

Voici à quoi ressemble l'un de ces en-têtes Cache-Control :

```
Cache-Control: public;max-age=3431901
```

L'en-tête vous permet également de spécifier la _durée_ pendant laquelle la ressource est valide. Cela permet au client de savoir quand il doit cesser d'utiliser sa copie mise en cache et demander une nouvelle copie.

Voici la logique derrière cela :

![Image](https://cdn-media-1.freecodecamp.org/images/GOgNRiJQOjDPYEKz-xcq-QrREMnQl1fByxo8)
_[Crédit image](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching?hl=en" rel="noopener" target="_blank" title=")_

En dehors de cela, HTTP dispose également de mécanismes pour effectuer ce que l'on appelle une _requête conditionnelle_. L'objectif ici est que le serveur retourne certaines ressources au client **uniquement lorsque des conditions spécifiques sont remplies**_._

![Image](https://cdn-media-1.freecodecamp.org/images/TJEtZCq8MaprADb9P8sUzXRynUvtHSUcC2lW)
_[Crédit image](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers" rel="noopener" target="_blank" title=")_

En supposant que le client dispose d'une copie enregistrée d'une ressource dans son cache, il peut faire une requête au serveur pour déterminer s'il existe une copie mise à jour de cette même ressource. Si c'est le cas, le serveur retourne la nouvelle copie. Sinon, il indique au client de continuer à utiliser sa copie locale.

Cela aide à prévenir le transfert redondant de données sur le réseau, tout en s'assurant que le client a accès à des données fraîches à tout moment.

Il existe plusieurs façons dont HTTP vous permet d'accomplir cela :

#### **Approche de mise en cache #1 : If-Modified-Since/Last-Modified**

Avec chaque réponse que le serveur envoie, il peut choisir de joindre un horodatage _Last-Modified_. Cela indique quand la ressource a été modifiée pour la dernière fois.

Lorsque le client doit demander à nouveau la ressource dans le futur, il fait la requête au serveur comme il le ferait normalement, mais avec un en-tête _If-Modified-Since_ pertinent. Cela indique au serveur de retourner la nouvelle copie de la ressource, si elle existe.

Sinon, le serveur retourne le code d'état **304**, qui indique au client de continuer à utiliser la copie qu'il possède déjà.

#### **Approche de mise en cache #2 : If-None-Match/ETag**

Ce schéma fonctionne de manière similaire au précédent, à l'exception de la manière dont les ressources sont identifiées. Au lieu d'utiliser des horodatages, le serveur envoie avec chaque réponse un hachage unique expliquant l'état de la ressource à ce moment-là (connu sous le nom d'ETag).

Pour les requêtes futures, le client envoie l'ETag pertinent au serveur. Si une ressource existe avec le même ETag, le serveur indique au client de continuer à utiliser la copie mise en cache. Sinon, le serveur envoie une nouvelle copie au client.

La mise en cache est compliquée. À mesure que votre service commence à ajouter plus d'utilisateurs, vous voudrez en apprendre davantage sur la mise en cache et sur la manière dont vous pouvez l'utiliser à votre avantage.

#### Contrainte #4 : Interface Uniforme

L'_Interface Uniforme_ (ou _Contrat Uniforme_) indique à un service RESTful ce qu'il doit servir, sous la forme d'un document, d'une image, d'un objet non virtuel, etc.

REST ne dicte cependant pas _comment_ vous choisissez d'interagir avec ces ressources, tant qu'elles sont cohérentes et bien comprises.

En général, avant qu'un client puisse interagir avec un service RESTful, il doit être d'accord sur :

1. **Identification** : Il doit y avoir un moyen d'identifier de manière unique chaque ressource que le service a à offrir.
2. **Manipulation** : Il doit y avoir un ensemble standard d'opérations qui peuvent être effectuées sur une ressource donnée avec des résultats prévisibles. Les résultats de ces opérations doivent également être auto-descriptifs et uniques.

HTTP, par exemple, utilise des URLs pour l'identification des ressources. Il utilise également une poignée de verbes d'action et de codes d'état bien documentés pour faciliter l'interaction avec les ressources. (Pour une explication plus détaillée des constructions de HTTP, vous pouvez revenir en arrière et lire [la Partie I](https://medium.freecodecamp.com/restful-services-part-i-http-in-a-nutshell-aab3bfedd131#.x6izf0yx4) de cette série.)

Jusqu'à présent, nous avons considéré les services RESTful comme étant strictement liés à HTTP. En ce qui concerne les services web, cela est presque toujours exact.

Mais en théorie, REST peut être implémenté sur n'importe quel protocole qui fournit un moyen décent d'atteindre les deux conditions que j'ai décrites ci-dessus. Pour cette raison, REST est parfois également appelé _REST sur HTTP_ pour clarifier qu'il est utilisé sur le web.

#### Contrainte #5 : Un Système en Couches

Un système en couches s'appuie sur la contrainte client-serveur dont nous avons discuté précédemment et impose une séparation encore plus grande des préoccupations. L'architecture globale de votre service peut être divisée en _couches_ individuelles, chacune servant une fonction spécifique.

Plus important encore, chaque couche doit agir indépendamment et interagir uniquement avec les couches immédiatement adjacentes. Cela force les requêtes à se propager de manière prévisible, sans contourner les couches.

Par exemple, pour mettre à l'échelle, vous pouvez utiliser un proxy se comportant comme un équilibreur de charge. Le seul but du proxy serait alors de transmettre les requêtes entrantes à l'instance de serveur appropriée.

Le client, en revanche, n'a pas besoin d'être conscient de cette division. Il continue simplement à faire des requêtes à la même URL, sans se soucier des détails de la manière dont les requêtes sont traitées.

De même, il peut y avoir une autre couche dans l'architecture responsable de la mise en cache des réponses afin de minimiser le travail nécessaire à effectuer par le serveur.

Une autre couche peut se comporter comme une _passerelle_ et traduire les requêtes HTTP vers d'autres protocoles.

Une façon dont vous pourriez utiliser cela serait de mettre en œuvre un serveur FTP. Le client continuerait à faire des requêtes à ce qu'il perçoit comme un serveur HTTP, tandis que vous avez en réalité un serveur FTP qui fait le travail en coulisses.

Tout comme la distinction client-serveur, cette contrainte de système en couches minimise le risque de couplage de fonctionnalités dans votre service, mais au détriment d'une surcharge supplémentaire dans le système.

### Conclusion

Pour résumer, nous avons examiné les contraintes importantes que vous devez garder à l'esprit lors de la conception de services web RESTful. Je tiens également à souligner que, bien que ces contraintes soient techniquement des exigences strictes qu'un service doit remplir pour être considéré comme RESTful, en pratique, cela ne se produit pas toujours.

La construction de services réels consiste davantage à résoudre les problèmes à portée de main qu'à répondre à des définitions techniques. Par conséquent, ces contraintes sont le plus souvent utilisées comme des lignes directrices par les développeurs et les architectes, qui décident ensuite quelles règles suivre dans leurs efforts pour atteindre leurs propres objectifs spécifiques.

C'est de là que viennent les termes _partiellement restful_ et _totalement restful_. Et en fait, la plupart des services que vous rencontrez en ligne ne sont pas techniquement totalement RESTful.

Dans la prochaine et dernière partie de cette série, je discuterai des principes de HATEOAS, ainsi que du modèle de maturité de Richardson. Cela fournit une approche légèrement plus quantitative pour déterminer à quel point un service web est vraiment RESTful. Vous pouvez le trouver [ici](https://medium.com/@sanchit.gera/restful-services-part-iii-hateoas-and-the-richardson-maturity-model-48d4e4c79b8d#.a8x1sscv5) !

J'espère que cela a été une introduction utile à ce qui entre dans la construction d'une application RESTful. Comprendre les principes de REST est sûr de vous aider lorsque vous travaillez avec de nombreuses API tierces. Ou même lorsque vous construisez vos propres applications sur le web, mobile, ou ailleurs.

En bonus, j'ai également téléchargé une présentation pertinente à ce sujet [ici](http://www.slideshare.net/SanchitGera/impact-of-restful-web-architecture-on-performance-and-scalability). Le diaporama est emprunté à une courte conférence que j'ai donnée il y a quelques mois à mon université intitulée « L'Impact d'une Architecture RESTful sur la Performance et l'Évolutivité des Applications ». J'espère que vous le trouverez utile :)

Faites-moi savoir dans les commentaires si vous avez des retours ou n'hésitez pas à me contacter via mon [LinkedIn](http://linkedin.com/in/sanchitgera).

**Voici quelques ressources pour une lecture approfondie sur REST :**

[Principes Clés de l'Architecture Logicielle — MSDN](https://msdn.microsoft.com/en-us/library/ee658124.aspx?f=255&MSPPError=-2147217396)

[Rest Expliqué, une présentation](http://www.slideshare.net/dnene/rest-representational-state-transfer-explained?from_action=save)

[Services Web RESTful — Sam Ruby](https://www.safaribooksonline.com/library/view/restful-web-services/9780596529260/)

[WhatIsRest.com](http://whatisrest.com)

[Rest In Practice](https://www.amazon.com/REST-Practice-Hypermedia-Systems-Architecture/dp/0596805829)