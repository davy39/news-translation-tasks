---
title: 'GraphQL avec Golang : Une Plongée Profonde des Bases à l''Avancé'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T17:37:50.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-graphql-with-golang-d3e02a429ac3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xo_ieo3nfyA0KCh-j8l1OQ.png
tags:
- name: coding
  slug: coding
- name: golang
  slug: golang
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'GraphQL avec Golang : Une Plongée Profonde des Bases à l''Avancé'
seo_desc: 'By Ridham Tarpara

  GraphQL has become a buzzword over the last few years after Facebook made it open-source.
  I have tried GraphQL with the Node.js, and I agree with all the buzz about the advantages
  and simplicity of GraphQL.

  So what is GraphQL? This ...'
---

Par Ridham Tarpara

GraphQL est devenu un mot à la mode ces dernières années après que Facebook l'ait rendu open-source. J'ai essayé GraphQL avec Node.js, et je suis d'accord avec tout le battage médiatique concernant les avantages et la simplicité de GraphQL.

Alors, qu'est-ce que GraphQL ? Voici ce que dit la définition officielle de GraphQL :

> GraphQL est un langage de requête pour les API et un runtime pour remplir ces requêtes avec vos données existantes. GraphQL fournit une description complète et compréhensible des données dans votre API, donne aux clients le pouvoir de demander exactement ce dont ils ont besoin et rien de plus, facilite l'évolution des API au fil du temps et permet des outils de développement puissants.

J'ai récemment basculé vers Golang pour un nouveau projet sur lequel je travaille (depuis Node.js) et j'ai décidé d'essayer GraphQL avec lui. Il n'y a pas beaucoup d'options de bibliothèques avec Golang, mais j'ai essayé avec [Thunder](https://github.com/samsarahq/thunder), [graphql](https://github.com/graphql-go/graphql), [graphql-go](https://github.com/graph-gophers/graphql-go) et [gqlgen](https://github.com/99designs/gqlgen). Et je dois dire que [gqlgen](https://github.com/99designs/gqlgen) est le gagnant parmi toutes les bibliothèques que j'ai essayées.

[gqlgen](https://github.com/99designs/gqlgen) est toujours en version bêta avec la dernière version [0.7.2](https://github.com/99designs/gqlgen/releases/tag/v0.7.2) au moment de la rédaction de cet article, et il évolue rapidement. Vous pouvez trouver leur feuille de route [ici](https://github.com/99designs/gqlgen/projects/1). Et maintenant, [99designs](https://99designs.com/) les sponsorise officiellement, donc nous verrons une vitesse de développement encore meilleure pour ce projet open source génial. [vektah](https://github.com/vektah) et [neelance](https://github.com/neelance) sont les principaux contributeurs, et [neelance](https://github.com/neelance) a également écrit [graphql-go](https://github.com/graph-gophers/graphql-go).

Alors, plongeons dans la sémantique de la bibliothèque en supposant que vous avez des connaissances de base sur GraphQL.

### Points forts

Comme leur titre l'indique,

> Il s'agit d'une bibliothèque pour créer rapidement des serveurs GraphQL strictement typés en Golang.

Je pense que c'est la chose la plus prometteuse à propos de la bibliothèque : vous ne verrez jamais `map[string]interface{}` ici, car elle utilise une approche strictement typée.

En outre, elle utilise une **approche Schema first** : vous définissez donc votre API en utilisant le langage de définition de schéma [Schema Definition Language](http://graphql.org/learn/schema/). Cela a ses propres outils de génération de code puissants qui généreront automatiquement tout votre code GraphQL et vous devrez simplement implémenter la logique principale de cette méthode d'interface.

J'ai divisé cet article en deux phases :

* Les bases : Configuration, Mutations, Requêtes et Abonnement
* L'avancé : Authentification, Dataloaders et Complexité des Requêtes

### Phase 1 : Les Bases - Configuration, Mutations, Requêtes et Abonnements

![Image](https://cdn-media-1.freecodecamp.org/images/1*PbZAsqIeqb9-3IwmRSTwgQ.png)

Nous utiliserons un site de publication de vidéos comme exemple dans lequel un utilisateur peut publier une vidéo, ajouter des captures d'écran, ajouter un avis et obtenir des vidéos et des vidéos connexes.

```
mkdir -p $GOPATH/src/github.com/ridhamtarpara/go-graphql-demo/
```

Créez le schéma suivant à la racine du projet :

Ici, nous avons défini nos modèles de base et une mutation pour publier de nouvelles vidéos, et une requête pour obtenir toutes les vidéos. Vous pouvez en savoir plus sur le schéma graphql [ici](https://graphql.org/learn/schema). Nous avons également défini un type personnalisé (scalaire), car par défaut, graphql n'a que 5 types [scalaires](https://graphql.org/learn/schema/#scalar-types) qui incluent Int, Float, String, Boolean et ID.

Donc, si vous voulez utiliser un type personnalisé, vous pouvez définir un scalaire personnalisé dans `schema.graphql` (comme nous avons défini `Timestamp`) et fournir sa définition dans le code. Dans gqlgen, vous devez fournir des méthodes de marshal et unmarshal pour tous les scalaires personnalisés et les mapper dans `gqlgen.yml`.

Un autre changement majeur dans gqlgen dans la dernière version est qu'ils ont supprimé la dépendance aux binaires compilés. Ajoutez donc le fichier suivant à votre projet sous scripts/gqlgen.go.

et initialisez dep avec :

```
dep init
```

Maintenant, il est temps de tirer parti de la fonction de codegen de la bibliothèque qui génère tout le code squelette ennuyeux (mais intéressant pour certains).

```
go run scripts/gqlgen.go init
```

ce qui créera les fichiers suivants :

**gqlgen.yml** — Fichier de configuration pour contrôler la génération de code.  
**generated.go** — Le code généré que vous ne voulez peut-être pas voir.  
**models_gen.go** — Tous les modèles pour l'entrée et le type de votre schéma fourni.  
**resolver.go** — Vous devez écrire vos implémentations.  
**server/server.go** — point d'entrée avec un http.Handler pour démarrer le serveur GraphQL.

Jetons un coup d'œil à l'un des modèles générés du type `Video` :

Ici, comme vous pouvez le voir, ID est défini comme une chaîne et CreatedAt est également une chaîne. Les autres modèles liés sont mappés en conséquence, mais dans le monde réel, vous ne voulez pas cela — si vous utilisez un type de données SQL, vous voulez votre champ ID comme int ou int64, selon votre base de données.

Par exemple, j'utilise PostgreSQL pour la démonstration, donc bien sûr _je veux ID comme un int et CreatedAt comme un time.Time_. Nous devons donc définir notre propre modèle et instruire gqlgen d'utiliser notre modèle au lieu d'en générer un nouveau.

et mettre à jour gqlgen pour utiliser ces modèles comme ceci :

Le point focal est donc les définitions personnalisées pour ID et Timestamp avec les méthodes de marshal et unmarshal et leur mappage dans un fichier gqlgen.yml. Maintenant, lorsque l'utilisateur fournit une chaîne comme ID, UnmarshalID convertira une chaîne en un int. Lors de l'envoi de la réponse, MarshalID convertira int en chaîne. Il en va de même pour Timestamp ou tout autre scalaire personnalisé que vous définissez.

Maintenant, il est temps d'implémenter la logique réelle. Ouvrez `resolver.go` et fournissez la définition de la mutation et des requêtes. Les stubs sont déjà auto-générés avec une instruction de panique non implémentée, alors remplaçons cela.

et exécutez la mutation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dTOTfTVx5XIV4E_Pys468g.png)
_Mutation createVideo_

Oh, ça a marché... mais attendez, pourquoi mon utilisateur est vide ?? Ici, il y a un concept similaire à celui du chargement paresseux et du chargement impatient. Comme GraphQL est extensible, vous devez définir quels champs vous voulez remplir de manière impatiente et lesquels de manière paresseuse.

J'ai créé cette règle d'or pour mon équipe d'organisation travaillant avec gqlgen :

> _N'incluez pas les champs dans un modèle que vous voulez charger uniquement lorsqu'ils sont demandés par le client._

Pour notre cas d'utilisation, je veux charger les vidéos connexes (et même les utilisateurs) uniquement si un client demande ces champs. Mais comme nous avons inclus ces champs dans les modèles, gqlgen supposera que vous fournirez ces valeurs lors de la résolution de la vidéo — donc actuellement, nous obtenons une structure vide.

Parfois, vous avez besoin d'un certain type de données à chaque fois, donc vous ne voulez pas le charger avec une autre requête. Vous pouvez plutôt utiliser quelque chose comme les jointures SQL pour améliorer les performances. Pour un cas d'utilisation (non inclus dans l'article), j'avais besoin des métadonnées de la vidéo à chaque fois avec la vidéo qui est stockée à un autre endroit. Donc, si je les chargeais lorsqu'elles étaient demandées, j'aurais eu besoin d'une autre requête. Mais comme je connaissais mes exigences (que j'en avais besoin partout côté client), j'ai préféré les charger de manière impatiente pour améliorer les performances.

Alors, réécrivons le modèle et régénérons le code gqlgen. Pour simplifier, nous ne définirons des méthodes que pour l'utilisateur.

Nous avons donc ajouté UserID et supprimé User struct et régénéré le code :

```
go run scripts/gqlgen.go -v
```

Cela générera les méthodes d'interface suivantes pour résoudre les structures non définies et vous devez les définir dans votre resolver :

Et voici notre définition :

Maintenant, le résultat devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3-LA9IVeYwONtc243zB8dQ.png)

Cela couvre les bases de graphql et devrait vous permettre de commencer. Essayez quelques choses avec graphql et la puissance de Golang ! Mais avant cela, jetons un coup d'œil à l'abonnement qui devrait être inclus dans le cadre de cet article.

#### Abonnements

Graphql fournit un abonnement comme type d'opération qui vous permet de vous abonner à des données en temps réel dans GraphQL. gqlgen fournit des événements d'abonnement en temps réel basés sur des websockets.

Vous devez définir votre abonnement dans le fichier `schema.graphql`. Ici, nous nous abonnons à l'événement de publication de vidéo.

Régénérez le code en exécutant : `go run scripts/gqlgen.go -v`.

Comme expliqué précédemment, cela créera une interface dans generated.go que vous devez implémenter dans votre resolver. Dans notre cas, cela ressemble à ceci :

Maintenant, vous devez émettre des événements lorsqu'une nouvelle vidéo est créée. Comme vous pouvez le voir à la ligne 23, nous avons fait cela.

Et il est temps de tester l'abonnement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8NqJCSQllG9F21bnZf-ubQ.gif)

GraphQL présente certains avantages, mais tout ce qui brille n'est pas de l'or. Vous devez prendre soin de quelques choses comme les autorisations, la complexité des requêtes, la mise en cache, le problème des requêtes N+1, la limitation de débit et quelques autres problèmes — sinon, cela mettra vos performances en péril.

### Phase 2 : L'avancé - Authentification, Dataloaders et Complexité des Requêtes

![Image](https://cdn-media-1.freecodecamp.org/images/1*UzMSr7FUq_StYTvqLtAgXw.png)

Chaque fois que je lis un tutoriel comme celui-ci, j'ai l'impression de savoir tout ce que j'ai besoin de savoir et de pouvoir résoudre tous mes problèmes.

Mais lorsque je commence à travailler sur des choses par moi-même, je finis généralement par obtenir une erreur de serveur interne ou des requêtes sans fin ou des impasses et je dois creuser profondément pour me frayer un chemin. Espérons que nous pouvons aider à prévenir cela ici.

Jetons un coup d'œil à quelques concepts avancés en commençant par l'authentification de base.

#### Authentification

Dans une API REST, vous avez un système d'authentification et certaines autorisations prêtes à l'emploi sur des endpoints particuliers. Mais dans GraphQL, un seul endpoint est exposé, vous pouvez donc y parvenir avec des directives de schéma.  
Vous devez modifier votre schema.graphql comme suit :

Nous avons créé une directive isAuthenticated et nous avons maintenant appliqué cette directive à l'abonnement `createVideo`. Après avoir régénéré le code, vous devez donner une définition de la directive. Actuellement, les directives sont implémentées comme des méthodes de struct au lieu de l'interface, donc nous devons donner une définition.  
J'ai mis à jour le code généré de server.go et créé une méthode pour retourner la configuration graphql pour server.go comme suit :

Nous avons lu l'userId à partir du contexte. Cela semble étrange, n'est-ce pas ? Comment l'userId a-t-il été inséré dans le contexte et pourquoi dans le contexte ? D'accord, donc gqlgen ne vous fournit que les contextes de requête au niveau de l'implémentation, donc vous ne pouvez pas lire les données de la requête HTTP comme les en-têtes ou les cookies dans les resolvers ou les directives graphql. Par conséquent, vous devez ajouter votre middleware et récupérer ces données et mettre les données dans votre contexte.

Nous devons donc définir un middleware d'authentification pour récupérer les données d'authentification de la requête et les valider.

Je n'ai pas défini de logique là, mais j'ai plutôt passé l'userId comme autorisation à des fins de démonstration. Ensuite, enchaînez ce middleware dans `server.go` avec la nouvelle méthode de chargement de configuration.

Maintenant, la définition de la directive a du sens. Ne gérez pas les utilisateurs non autorisés dans votre middleware car cela sera géré par votre directive.

Heure de la démonstration :

![Image](https://cdn-media-1.freecodecamp.org/images/1*510I9jDI6QxKQXRS33Qv7A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ynDxZmD-y27TwEG86uLvIg.png)

Vous pouvez même passer des arguments dans les directives de schéma comme ceci :

```
directive @hasRole(role: Role!) on FIELD_DEFINITIONenum Role { ADMIN USER }
```

#### Dataloaders

Tout cela semble élégant, n'est-ce pas ? Vous chargez les données lorsque cela est nécessaire. Les clients ont le contrôle des données, il n'y a pas de sous-chargement et pas de surchargement. Mais tout cela a un coût.

Alors, quel est le coût ici ? Jetons un coup d'œil aux logs lors de la récupération de toutes les vidéos. Nous avons 8 entrées vidéo et il y a 5 utilisateurs.

```
query{  Videos(limit: 10){    name    user{      name    }  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9YduHfCEyejPzhH9wmz2w.png)

```
Query: Videos : SELECT id, name, description, url, created_at, user_id FROM videos ORDER BY created_at desc limit $1 offset $2Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1Resolver: User : SELECT id, name, email FROM users where id = $1
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*79fcEJbYDH0MTYn3HGMzBQ.png)

Pourquoi 9 requêtes (1 table vidéos et 8 tables utilisateurs) ? Cela semble horrible. J'étais sur le point de faire une crise cardiaque lorsque j'ai pensé à remplacer nos serveurs API REST actuels par celui-ci... mais les dataloaders sont arrivés comme une cure complète pour cela !

Cela est connu comme le problème N+1. Il y aura une requête pour obtenir toutes les données et pour chaque donnée (N), il y aura une autre requête de base de données.

C'est un problème très sérieux en termes de performance et de ressources : bien que ces requêtes soient parallèles, elles utiliseront vos ressources.

Nous utiliserons la bibliothèque [dataloaden](https://github.com/vektah/dataloaden) de l'auteur de gqlgen. C'est une bibliothèque générée en Go. Nous générerons le dataloader pour l'utilisateur en premier.

```
go get github.com/vektah/dataloadendataloaden github.com/ridhamtarpara/go-graphql-demo/api.User
```

Cela générera un fichier `userloader_gen.go` qui contient des méthodes comme Fetch, LoadAll et Prime.

Maintenant, nous devons définir la méthode Fetch pour obtenir le résultat en masse.

Ici, nous attendons 1 ms pour qu'un utilisateur charge les requêtes et nous avons gardé un lot maximum de 100 requêtes. Donc maintenant, au lieu de lancer une requête pour chaque utilisateur, le dataloader attendra soit 1 milliseconde pour 100 utilisateurs avant de frapper la base de données. Nous devons changer notre logique de resolver d'utilisateur pour utiliser le dataloader au lieu de la logique de requête précédente.

Après cela, mes logs ressemblent à ceci pour des données similaires :

```
Query: Videos : SELECT id, name, description, url, created_at, user_id FROM videos ORDER BY created_at desc limit $1 offset $2Dataloader: User : SELECT id, name, email from users WHERE id IN ($1, $2, $3, $4, $5)
```

Maintenant, seulement deux requêtes sont lancées, donc tout le monde est heureux. La chose intéressante est que seulement cinq clés d'utilisateur sont données à la requête même s'il y a 8 vidéos. Donc le dataloader a supprimé les entrées en double.

#### Complexité des Requêtes

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhL1ly1CNuOlQB8S1nIRMw.png)

Dans GraphQL, vous donnez un moyen puissant au client de récupérer ce dont il a besoin, mais cela vous expose au risque d'attaques par déni de service.

Comprenons cela à travers un exemple que nous avons utilisé pour cet article.

Maintenant, nous avons un champ related dans le type vidéo qui retourne les vidéos connexes. Et chaque vidéo connexe est du type vidéo graphql, donc elles ont toutes des vidéos connexes aussi... et ainsi de suite.

Considérez la requête suivante pour comprendre la gravité de la situation :

```
{  Videos(limit: 10, offset: 0){    name    url    related(limit: 10, offset: 0){      name      url      related(limit: 10, offset: 0){        name        url        related(limit: 100, offset: 0){          name          url        }      }    }  }}
```

Si j'ajoute un autre sous-objet ou que j'augmente la limite à 100, alors ce seront des millions de vidéos chargées en un seul appel. Peut-être (ou plutôt définitivement) cela rendra votre base de données et votre service non réactifs.

gqlgen fournit un moyen de définir la complexité maximale de la requête autorisée en un seul appel. Vous devez simplement ajouter une ligne (ligne 5 dans l'extrait suivant) dans votre gestionnaire graphql et définir la complexité maximale (300 dans notre cas).

gqlgen attribue un poids de complexité fixe pour chaque champ, donc il considérera struct, array et string comme égaux. Donc pour cette requête, la complexité sera de 12. Mais nous savons que les champs imbriqués pèsent trop, donc nous devons dire à gqlgen de calculer en conséquence (en termes simples, utiliser la multiplication au lieu de la simple somme).

Tout comme les directives, la complexité est également définie comme une struct, donc nous avons changé notre méthode de configuration en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VyGf4i0ql2akhu_wdon1Ug.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hSyVXGoiQ5Th9DaxtWjIAg.png)

Je n'ai pas défini la logique de la méthode related et j'ai simplement retourné le tableau vide. Donc related est vide dans la sortie, mais cela devrait vous donner une idée claire sur la façon d'utiliser la complexité des requêtes.

### Notes Finales

Ce code est sur [Github](https://github.com/ridhamtarpara/go-graphql-demo). Vous pouvez jouer avec, et si vous avez des questions ou des préoccupations, faites-le moi savoir dans la section des commentaires.

**Merci d'avoir lu ! Quelques (espérons 50) applaudissements ? sont toujours appréciés.** Je **écris sur JavaScript, le langage Go, DevOps et l'informatique. Suivez-moi et partagez cet article si vous l'aimez.**

**Contactez-moi sur @[Twitter](https://twitter.com/RidhamTarpara) @[Linkedin](https://www.linkedin.com/in/ridham-tarpara-97430270). Visitez [www.ridham.me](http://www.ridham.me) pour plus d'informations.**