---
title: Comment créer une passerelle proxy API avec AWS HTTP API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-21T16:43:47.000Z'
originalURL: https://freecodecamp.org/news/create-an-api-proxy-gateway-with-aws-http-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/praneet-kumar-H8dcf-v98mA-unsplash.jpg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
seo_title: Comment créer une passerelle proxy API avec AWS HTTP API
seo_desc: 'By Prajwal Kulkarni

  In today''s fast-paced world, seamless integration between various services and
  systems has become ever more important.

  Security is also equally important while stitching these services together. So it''s
  crucial to design applicati...'
---

Par Prajwal Kulkarni

Dans le monde rapide d'aujourd'hui, l'intégration transparente entre divers services et systèmes est devenue de plus en plus importante.

La sécurité est également tout aussi importante lors de la connexion de ces services. Il est donc crucial de concevoir des applications de manière significative afin qu'il y ait un minimum de friction entre les différents systèmes.

Cet article se concentre sur la communication entre un client et d'autres services backend, qu'il s'agisse d'une fonction serverless ou d'une API tierce.

Que vous soyez développeur, architecte ou passionné de technologie, ce tutoriel vous fournira les connaissances et les compétences nécessaires pour configurer une passerelle API robuste et évolutive qui simplifie la communication entre les clients et les services backend.

## Un bref rappel des fondamentaux

Avant de plonger et de comprendre le potentiel de l'API HTTP AWS pour rationaliser votre processus d'intégration API, revoyons rapidement les terminologies de base.

Beaucoup d'entre vous comprennent probablement ce qu'est une API et une passerelle proxy. Cela dit, les choses peuvent devenir un peu intimidantes lorsque nous approfondissons de tels concepts en essayant de comprendre les détails et les différences.

Une API (Application Programming Interface) est une abstraction qui permet à deux programmes de communiquer entre eux. Les API peuvent être des méthodes exposées par les fournisseurs de services API sous forme de package ou d'un endpoint via lequel des informations peuvent être transmises (API REST).

Une passerelle proxy est une passerelle qui transmet les requêtes entrantes à l'URI cible, tandis qu'une passerelle régulière envoie les informations dans les deux sens entre le client et le serveur.

Les passerelles proxy sont également un excellent moyen de masquer vos URI cibles et vos clés API, qui seraient autrement exposées si l'appel réseau était effectué directement depuis le frontend (navigateur).

### HTTP API vs REST API – Quelle est la différence ?

Techniquement parlant, il n'existe pas d'"HTTP API" – cela est spécifique à AWS.

Lors de la création d'une passerelle API sur AWS, vous pouvez créer une API HTTP ou une API REST. La différence entre les deux est que cette dernière offre plus de flexibilité dans la conception d'une API, comme la limitation du débit par client, la validation des requêtes, les endpoints privés, et ainsi de suite.

### Pourquoi choisir HTTP API plutôt que REST API ?

Comme mentionné ci-dessus, REST API offre plus de flexibilité et une configuration fine pour configurer des API par rapport à HTTP API. Pourquoi voudriez-vous alors travailler avec HTTP API ?

Eh bien, ce n'est pas toujours une question de flexibilité d'avoir de nombreuses options parmi lesquelles choisir – à moins que l'exigence ne soit concrète, cela ajoute généralement du bruit lorsqu'il s'agit de choisir le bon ensemble d'options.

D'autre part, HTTP API vient avec des options de configuration limitées, ce qui vous aide à construire des API avec un minimum de décisions.

Un autre avantage de HTTP API est qu'elle vous permet d'ajouter un autorisateur JWT à la passerelle, ce qui n'est pas présent dans REST API.

Si vous utilisez un système d'authentification tiers dans votre application, il serait judicieux d'utiliser l'autorisateur JWT pour protéger vos endpoints API.

Enfin, HTTP API est plus abordable que REST API.

En regardant les caractéristiques saillantes, le choix entre les deux dépend entièrement de vos exigences. Mais en termes vagues, les API HTTP sont un bon choix pour les applications à petite échelle et non critiques pour les affaires.

## Comment créer une passerelle proxy HTTP et l'intégrer avec une URI cible

Il est temps de mettre les mains dans le cambouis.

Naviguez vers votre console AWS et recherchez **"API Gateway"**.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/target-uri1.png)
_Trouver API Gateway sur la console AWS_

En cliquant sur Créer une API, vous verrez les différents types d'API disponibles. Cliquez sur "Build" pour HTTP API.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/target-uri2.png)
_Choisir "Build" pour HTTP API_

Entrez le nom de l'API et cliquez sur "Review and create". Alternativement, vous pourriez entrer d'autres informations de configuration requises, mais ignorez-les pour l'instant, car nous verrons la configuration en détail ci-dessous.

Il y a 3 parties pour créer une passerelle proxy sécurisée :

1. Définir les routes
2. Ajouter l'intégration
3. Attacher les autorisateurs

Examinons chacun d'eux plus en détail.

### Comment définir les routes

Les routes sont les endpoints de chemin qui correspondent à une action de ressource ou à une URI cible.

Il est possible d'envoyer des valeurs dynamiques à la route en définissant des variables de chemin dans la route. Les variables de chemin sont définies en ajoutant des accolades autour de la variable de chemin, comme suit : `/getmusic/{track}`.

Dans la route ci-dessus, **`{track}`** est la variable de chemin qui peut être substituée par n'importe quelle valeur.

Une route peut avoir n'importe quel nombre de variables de chemin. Cependant, il est important de savoir que les paramètres de requête ne peuvent pas être ajoutés dans la définition de la route.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/route-definition.png)
_Définir la route pour la passerelle proxy API_

Assurez-vous également de sélectionner la méthode appropriée pour la route définie. Pour simplifier, vous pouvez envisager d'utiliser "GET".

### Comment ajouter l'intégration

C'est probablement l'étape la plus importante dans la création d'une passerelle proxy.

La partie difficile ici est de créer le mappage correct des valeurs dynamiques entre la requête entrante et la requête sortante. Il est assez surprenant de constater qu'il n'y a pas de tutoriels, de docs ou de guides abordant ce problème, alors j'espère que cela aidera.

Après avoir cliqué sur la méthode de la route nouvellement définie, vous pouvez voir les détails de la route dans le volet de droite.

Vous pouvez remarquer qu'il n'y a pas d'intégrations attachées à la route. Cliquez sur "Attach integration" suivi de "Create and attach an integration".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/attach-integration-1.png)
_Créer et attacher un écran d'intégration_

Dans le type d'intégration, sélectionnez "HTTP URI" car nous visons à créer une passerelle proxy qui transmet la requête à une API tierce cible.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/http-uri.png)
_Sélectionnez "HTTP URI" parmi les options_

Entrez votre URI cible et sélectionnez la même méthode que la requête entrante, afin que la requête soit transmise avec la méthode appropriée.

> Attention : Dans l'URI cible, vous devez ajouter uniquement le domaine de l'API et non le chemin complet avec les paramètres de requête, car c'est quelque chose que nous allons construire via le mappage de paramètres.

Par exemple, supposons que nous voulons obtenir une liste de pistes par leur nom.

Dans ce cas, votre endpoint d'entrée pourrait être :

`/getmusic/{track}`

Et selon l'API tierce que vous utilisez, l'URI cible pourrait être quelque chose comme :

`http://api.musixmatch.com/ws/1.1/track.search?q_track={track}`

Notre objectif est de nous assurer que la valeur envoyée pour la variable de chemin `track` est correctement substituée par la valeur réelle dans le paramètre de requête de la requête sortante.

Étrangement, si nous définissons notre URI cible comme : `http://api.musixmatch.com/ws/1.1/track.search?q_track={track}`, la variable `{track}` n'est pas substituée par la valeur réelle.

Au lieu de cela, la chaîne littérale `{track}` est envoyée telle quelle pour la valeur du paramètre de requête, vous obtenant le même ensemble de mauvais résultats quelle que soit votre demande.

Pour éviter ce piège, nous ne définissons pas le chemin complet dans l'URI cible.

En continuant, ajoutez la partie domaine de l'API, qui devrait être `http://api.musixmatch.com` en considérant l'exemple ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/parameter-mapping-1.png)

Comme vous pouvez le voir, sous la section des détails d'intégration, il y a des règles de mappage de paramètres qui sont actuellement vides. Cliquez sur "Create" pour commencer à ajouter des règles de mappage.

Ensuite, sélectionnez le type de mappage comme "All incoming requests" suivi de "Add new mapping".

Pour créer une règle de mappage, vous devez être conscient des trois choses suivantes :

* ce qui doit être modifié
* comment cela doit être modifié
* quelle doit être la valeur modifiée

Que doit être modifié ? Typiquement, tous les endpoints API auraient un chemin suffixé à la partie domaine, par exemple `v1/`, qui serait redondant dans notre endpoint de passerelle proxy. Nous voudrions donc commencer par écraser le chemin.

La valeur est quelque chose qui est typée statiquement pour se conformer au chemin URI.

En prenant l'API ci-dessus comme exemple, la valeur devrait être :

`/ws/1.1/track.search`

La partie dynamique de l'URI est la valeur de la piste qui est un paramètre de requête.

Ensuite, nous devons ajouter un paramètre de requête qui contient la valeur dynamique.

Pour ce faire, cliquez sur "Add new mapping" et sélectionnez `querystring.<querystring_name>` dans le paramètre à modifier suivi de la sélection de "Append".

Dans le champ de saisie de la valeur, entrez `$request.path.track` car `{track}` est le nom de la variable de chemin dans la requête entrante. Référez-vous à cette [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html) d'AWS pour plus d'informations sur la syntaxe.

En résumé, vos règles de mappage devraient maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/parameter-mapping-2.png)
_Règles de mappage de paramètres_

Cliquez sur "Create" et maintenant votre passerelle proxy API devrait être prête à l'emploi. Hourra !

Vous pouvez de manière similaire ajouter d'autres paramètres de requête en ajoutant la chaîne de requête au chemin en tant que nouveau mappage. Par exemple, les clés API sont généralement envoyées en tant que paramètre de requête.

De plus, il est également possible d'envoyer des en-têtes et un corps dans la requête sortante.

### Comment attacher des autorisateurs

Bien que l'attachement d'autorisateurs ne soit pas obligatoire lors du test de vos passerelles API, il est définitivement recommandé de les sécuriser en production.

Si vous utilisez un service d'authentification tiers comme Google Authenticator ou quelque chose de similaire, la passerelle API HTTP fournit un moyen facile de gérer l'autorisation sur vos routes en fonction du token JWT.

Naviguez vers la page "Authorization" dans le menu de gauche et cliquez sur "Create and attach an authorizer". Par défaut, le "Authorizer type" est sélectionné comme JWT.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/authorizers.png)

Saisissez les entrées requises comme le nom, l'URL de l'émetteur et l'audience. La valeur et le format varient en fonction du service d'authentification que vous utilisez. Par exemple, l'URL de l'émetteur de Google Auth est `https://securetoken.google.com/<project-id>`.

## Conclusion

L'essentiel de cet article est l'accent mis sur la construction du chemin en utilisant le mappage de paramètres, contrairement à sa définition directe dans la route et à l'attente que la magie opère.

Un inconvénient que j'ai remarqué est que le mappage de paramètres ne fonctionne pas lorsqu'il y a plus d'une variable de chemin définie dans la requête sortante. Il est donc important de s'assurer que la requête sortante a au plus un paramètre de chemin.

Les passerelles API HTTP sont un moyen rapide et facile de configurer des passerelles proxy/non-proxy avec des configurations minimales.

C'est tout, les amis ! J'espère que cela vous a aidé à acquérir quelques connaissances sur la création de passerelles API HTTP et la construction de chemins avec le mappage de paramètres. Partagez-le avec vos amis et connaissances qui pourraient être intéressés à lire cela.

Continuez à coder, continuez à construire. À la prochaine fois.