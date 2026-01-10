---
title: 'Services RESTful Partie I : HTTP en bref'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-11T04:32:05.000Z'
originalURL: https://freecodecamp.org/news/restful-services-part-i-http-in-a-nutshell-aab3bfedd131
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vDDox7uxWAuRafuq0WpVOA.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Services RESTful Partie I : HTTP en bref'
seo_desc: 'By Sanchit Gera

  The web has, from it’s inception, been structured around the idea of resources.
  In it’s early days, the web was merely a platform for sharing simple text/HTML based
  files, documents, images etc. In this sense, the web can be thought o...'
---

Par Sanchit Gera

Le web, depuis sa création, a été structuré autour de l'idée de ressources. Dans ses premiers jours, le web n'était qu'une plateforme pour partager des fichiers simples basés sur du texte/HTML, des documents, des images, etc. En ce sens, le web peut être considéré comme une collection de ressources et est souvent qualifié d'_orienté ressources_.

Le web a depuis évolué en un réseau beaucoup plus complexe d'applications interconnectées, regorgeant de contenu riche. Les applications elles-mêmes ont gagné en complexité, intégrant de plus en plus de fonctionnalités.

Les services fournissent un moyen d'exposer cette fonctionnalité aux clients. Généralement, les grandes applications peuvent vouloir fournir un accès programmatique à leur plateforme à d'autres développeurs et peuvent le faire en utilisant des services.

Alternativement, les services peuvent être utilisés pour décomposer une application en différentes unités logiques, interagissant entre elles pour produire un résultat final. Dans ce cas, un service agit comme un consommateur d'autres services.

Les services formant un composant critique des applications web, les développeurs cherchent naturellement à s'assurer qu'ils sont conçus de manière scalable, performante et fonctionnent avec le moins de surcharge possible — à la fois technique et autre.

Entrez REST ! REST, abréviation de REpresentational State Transfer, est un style architectural qui vise à tirer parti de toutes les mêmes constructions qui ont permis au Web de croître au cours des dernières décennies. Il utilise ces principes comme guide pour la conception de services web.

Puisque toute communication sur le Web se fait via HTTP, REST est intimement lié à celui-ci et utilise beaucoup des mêmes idées. Ainsi, une compréhension de REST nécessite une compréhension des concepts sous-jacents de HTTP. C'est le sujet du reste de cet article. :)

### HTTP en bref

La plupart des applications web sont construites autour d'un modèle client-serveur. Un client peut être quelque chose d'aussi simple qu'un navigateur web affichant du HTML, une application mobile récupérant et créant des données, ou même d'autres services web.

De même, les serveurs peuvent être implémentés de diverses manières, en utilisant différentes piles technologiques, langages, et servant différents types de données.

Afin d'accommoder cette diversité, les clients et les serveurs doivent convenir d'un ensemble de conventions — un _protocole_ — qui dicte toute communication entre eux. Ce protocole permet à un serveur web de recevoir les informations — _requêtes_ — envoyées par un client arbitraire, de les traiter et de répondre de manière appropriée.

Les applications web modernes utilisent le Hypertext Transfer Protocol, communément abrégé en HTTP, afin d'échanger des informations.

Essentiellement, cela fournit un format structuré pour l'échange d'informations sur le web. Comme nous allons le voir, HTTP établit un large ensemble de directives afin de décrire le type de données échangées — ainsi que leur format, validité et autres attributs.

Par le passé, les applications se sont généralement appuyées sur HTTP uniquement comme mécanisme de transmission. Les clients et les serveurs échangent des données _en utilisant_ HTTP. D'autres conventions doivent alors être développées afin de donner un sens à ces données. Un exemple de ce paradigme est SOAP, l'un des opposants les plus courants à REST.

La chose merveilleuse à propos de HTTP, cependant, est qu'il possède déjà les constructions nécessaires pour spécifier l'action et la ressource sur laquelle agit cette action (_requête client_), ainsi que le résultat de ces actions (_réponse serveur_), ce qui évite une surcharge supplémentaire pour transférer des informations. Examinons-en quelques-unes !

#### 1. URLs

Les URLs sont l'un des concepts les plus importants et utiles du Web. C'est aussi probablement le concept avec lequel la plupart des utilisateurs sont déjà familiers, même si ce n'est que de manière superficielle. URL est l'abréviation de Uniform Resource Locator et est utilisé pour identifier l'adresse d'une ressource sur le Web.

![Image](https://cdn-media-1.freecodecamp.org/images/oiGXAA5yQ5fSF8TySDue6-AM7PJrMeLU7Y4p)

Une URL se compose généralement des éléments suivants :

_Protocole_ : Il s'agit du protocole sur lequel la requête est servie. Il s'agit le plus souvent de HTTP (ou de sa version sécurisée, HTTPS). D'autres protocoles tels que SMTP et FTP existent et peuvent être utilisés à la place, mais nous nous limiterons à HTTP dans cette discussion.

_Domaine_ : Il s'agit du nom d'hôte du serveur auquel la ressource est demandée. Le domaine peut être équivalemment remplacé par une adresse IP, ce qui est généralement fait en coulisses par un DNS.

_Chemin_ : Il s'agit de l'emplacement de la ressource sur le serveur. Cela peut correspondre à l'emplacement de la ressource dans le système de fichiers (c'est-à-dire /search/files/myFile.txt), bien que cette pratique soit rarement utilisée de nos jours. Il est plus courant pour les services web d'imbriquer les chemins en fonction de la relation entre les ressources (c'est-à-dire myBlog/blog/comments) où _blog_ et _comments_ représentent deux ressources distinctes. Cela est exploré plus en détail dans la [deuxième partie](https://medium.com/@sanchit.gera/restful-services-part-ii-constraints-and-goals-530b8f6298b9#.pk4tsd6oz) de cette série.

_Paramètres_ : Il s'agit de données supplémentaires, transmises sous forme de paires clé-valeur, qui peuvent être utilisées par le serveur pour identifier la ressource ou filtrer une liste de ressources.

_Fragment_ : Un fragment fait référence à un emplacement _à l'intérieur_ de la ressource retournée et est généralement appliqué aux documents. Cela peut être considéré comme un marque-page dans le document retourné et indique au navigateur de localiser le contenu au point marqué et de l'afficher. Par exemple, pour les documents HTML, le navigateur fait défiler directement vers l'élément identifié par l'ancre. Les fragments sont également appelés _ancres_.

#### **2. Méthodes HTTP**

HTTP définit un ensemble de méthodes, également appelées "verbes", qu'un client peut utiliser afin de décrire le _type_ de requête effectuée. Cela est mieux compris dans le contexte des ressources discutées précédemment.

Chaque requête peut être modélisée comme effectuant une action spécifique sur une ressource. Par exemple, un client peut demander de créer, supprimer, mettre à jour ou simplement lire une ressource. En HTTP, cela correspond à l'envoi de requêtes POST, DELETE, PUT ou GET respectivement. Les requêtes POST et PUT acceptent des charges utiles correspondant aux données créées ou mises à jour. Nous explorerons ces méthodes en détail lorsque nous aborderons REST dans la prochaine partie.

Deux méthodes supplémentaires, utilisées beaucoup moins fréquemment, sont les méthodes OPTIONS et HEAD.

Simplement, le but d'une requête OPTIONS est de donner au client des informations sur les autres méthodes qui peuvent être utilisées pour interagir avec la ressource en question.

La requête HEAD, en revanche, est un peu plus utile. Une requête HEAD imite une requête GET, sauf qu'elle omet le corps de la réponse. Essentiellement, le client reçoit une réponse identique à celle qu'il aurait reçue pour une requête GET, avec les mêmes métadonnées, mais sans le corps de la réponse. Cela est utile car cela fournit un moyen rapide de vérifier les en-têtes de réponse et l'existence d'une ressource.

Une distinction importante établie par HTTP est de savoir si une méthode est **sûre** ou **non sûre**. Une méthode est dite sûre si elle ne modifie pas une ressource. En d'autres termes, la requête peut être considérée comme "lecture seule". Par exemple, faire une requête GET (ou HEAD) pour une ressource à partir d'un serveur ne devrait pas la modifier de quelque manière que ce soit. Toutes les autres méthodes sont par défaut non sûres.

Enfin, il y a le concept d'idempotence. Une méthode HTTP est dite idempotente si des invocations répétées d'une requête conduisent au même résultat. Tant que les paramètres de la requête restent inchangés, la requête pourrait être faite un nombre quelconque de fois et la ressource serait toujours laissée dans le même état que si la requête n'avait été faite qu'une seule fois. Cela s'inscrit bien dans la notion de pensée orientée ressources.

GET, OPTIONS et HEAD sont toutes des méthodes naturellement idempotentes, car ce sont des opérations en lecture seule. De plus, les méthodes PUT et DELETE sont également caractérisées comme idempotentes. Cela est dû au fait que la mise à jour d'une ressource avec le même ensemble de paramètres encore et encore conduit au même résultat final.

Il peut être légèrement contre-intuitif pour certains de voir pourquoi DELETE est également idempotent. Considérez ce qui se passe dans le système lorsque plusieurs requêtes DELETE sont faites simultanément. La première requête DELETE entraîne, eh bien, la suppression de la ressource. Faire plus de requêtes DELETE à ce stade **ne modifie pas l'état dans lequel se trouve le système**. Le système continue de rester dans le même état que celui dans lequel il se trouvait après l'exécution du premier DELETE.

Pour résumer...

![Image](https://cdn-media-1.freecodecamp.org/images/S6z3ESxzBKEbchGjuPJu4kUuaqLczecBNbYf)

#### **3. Codes de statut**

Les codes de statut sont une construction HTTP utile qui fournit des informations au consommateur sur le résultat d'une requête et comment l'interpréter. Par exemple, si je devais faire une requête pour récupérer un fichier à partir d'un serveur web, je m'attendrais à voir une réponse avec le code de statut décrivant si ma requête a été complétée avec succès ou non. Si ce n'est pas le cas, le code de statut me donnerait un indice supplémentaire sur la raison de l'échec de ma requête.

HTTP définit plusieurs codes de statut, chacun concernant un scénario spécifique. Voici quelques-unes des séries de codes courantes que vous pourriez rencontrer :

**2xx** : Les codes de statut de la série 2xx impliquent que la requête s'est terminée avec succès et sans erreurs. Le code 200 en est l'exemple typique.

**3xx** : Un code de la série 3xx implique une redirection. Cela signifie que le serveur a redirigé vers un autre emplacement lors de la réception de la requête.

**4xx** : Une erreur 4xx, c'est-à-dire 400, 403, 404, etc., est utilisée lorsqu'il y a une erreur dans la requête effectuée. Cela peut être causé par diverses raisons, telles qu'un accès non autorisé à une ressource, une tentative de travail avec une ressource qui n'existe pas réellement, des paramètres invalides, etc.

**5xx** : Enfin, une réponse 5xx est utilisée lorsqu'il y a une erreur du côté du serveur. Cela signifie que le serveur est conscient de l'erreur et est incapable de traiter la requête. Typiquement, la réponse est accompagnée d'une brève description de ce que pourrait être la cause de l'erreur.

#### **4. En-têtes HTTP**

Les en-têtes sont une partie essentielle de la communication HTTP. Ils servent à fournir des informations supplémentaires pour le traitement des requêtes et des réponses. Notez que les en-têtes ne concernent pas l'identification de la ressource sur laquelle on agit. Ils apparaissent généralement sous forme de paires clé-valeur et fournissent une multitude d'informations telles que la politique de cache pour la réponse, les types de réponse acceptables imposés par le client, la langue préférée de la réponse, l'encodage, etc.

Les informations d'authentification et d'autorisation — telles que les jetons d'accès — sont également couramment transmises à l'aide de l'en-tête _Authorization_.

De même, le serveur peut également utiliser les en-têtes de réponse pour définir des cookies sur le client et les récupérer de manière analogue avec le même mécanisme.

![Image](https://cdn-media-1.freecodecamp.org/images/CGyGQ52u9oHzs07w3kg1QWbZOqUEbYS8OqOf)
_En-têtes pour une requête GET faite à medium.com/bookmarks_

**Une note sur HTTPS** : Pour éviter toute confusion, il est également important de comprendre ce qu'est HTTPS et en quoi il diffère de HTTP. HTTP et HTTPS utilisent les mêmes mécanismes sous-jacents pour transférer des informations, bien que HTTPS soit (de loin) plus sécurisé. Les données transférées via HTTPS sont entièrement cryptées. Cela est une considération importante lorsque les informations en question sont confidentielles, telles que des données financières ou des informations personnelles d'un utilisateur.

Dans la prochaine partie de cet article, je discute des contraintes mises en place par REST au-dessus de HTTP, et comment il tire parti de la nature basée sur les ressources du Web pour concevoir des services web simples et scalables. Retrouvez-la [ici](https://medium.com/@sanchit.gera/restful-services-part-ii-constraints-and-goals-530b8f6298b9#.pk4tsd6oz) !

Et enfin, dans la troisième et dernière partie de cette série, vous en apprendrez davantage sur le modèle de maturité de Richardson, un moyen de mesurer quantitativement à quel point un service est RESTful, ou ne l'est pas. [Découvrez-le](https://medium.com/@sanchit.gera/restful-services-part-iii-hateoas-and-the-richardson-maturity-model-48d4e4c79b8d#.a8x1sscv5) ! :-)

_Autres lectures recommandées :_

* [Mozilla Developer Network — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
* [Mozilla Developer Network — URLs](https://developer.mozilla.org/en-US/Learn/Common_questions/What_is_a_URL)
* [HTTP — The Definitive Guide](https://www.amazon.ca/HTTP-Definitive-Guide-David-Gourley/dp/1565925092/ref=sr_1_1?ie=UTF8&qid=1468209162&sr=8-1&keywords=http+the+definitive+guide)
* [TutsPlus](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)