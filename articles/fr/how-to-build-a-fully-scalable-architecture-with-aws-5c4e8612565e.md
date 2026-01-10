---
title: Comment construire une architecture évolutive avec AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-07T22:07:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-fully-scalable-architecture-with-aws-5c4e8612565e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FrPZa97jMlK-TARcgvegmA.png
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment construire une architecture évolutive avec AWS
seo_desc: 'By Tim Grossmann

  What I learned building the StateOfVeganism ?

  By now, we all know that news and media shape our views on the topics we discuss.
  Of course, this is different from person to person. Some might be influenced a little
  more than others, b...'
---

Par Tim Grossmann

**Ce que j'ai appris en construisant StateOfVeganism ?**

Nous savons tous maintenant que **les nouvelles et les médias façonnent nos opinions** sur les sujets que nous discutons. Bien sûr, cela diffère d'une personne à l'autre. Certains peuvent être influencés un peu plus que d'autres, mais il y a toujours une opinion communiquée.

En tenant compte de cela, j'ai pensé qu'il serait vraiment intéressant de voir le développement continu de l'humeur dirigée vers un sujet ou une personne spécifique dans les médias.

Pour moi, le [Végétalisme](https://github.com/timgrossmann/stateOfVeganism) est un sujet intéressant, surtout depuis qu'il est fréquemment mentionné dans les médias. Puisque l'opinion des médias change l'opinion des gens, il serait intéressant de voir quel "sentiment" ils communiquent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uvc3UOM8xU42d9GxKRogvg.png)

C'est de cela que traite tout ce projet. Il collecte les nouvelles qui parlent ou mentionnent le [Végétalisme](https://github.com/timgrossmann/stateOfVeganism), découvre le contexte dans lequel il a été mentionné, et analyse s'il propage de la négativité ou de la positivité.

Bien sûr, un grand pourcentage des articles analysés devrait être classé comme "Neutre" si les rédacteurs font un bon travail en ne communiquant que des informations, donc nous devons garder cela à l'esprit également.

J'ai réalisé que c'était une opportunité incroyable de découvrir de nouveaux outils, surtout lorsque j'ai pensé au _nombre énorme d'articles publiés quotidiennement_.   
J'ai donc pensé à construire une architecture évolutive — une qui soit bon marché/gratuite au début lorsqu'il n'y a pas de trafic et seulement quelques articles, mais qui s'adapte facilement et infiniment une fois que le nombre de mentions ou de trafic augmente. J'ai entendu l'appel du cloud.

### Concevoir l'Architecture

La planification est tout, surtout lorsque nous voulons nous assurer que l'architecture est évolutive dès le début.

Commencer sur papier est une bonne chose, car cela vous permet d'être extrêmement rapide et grossier dans l'itération.

Votre premier brouillon ne sera jamais votre version finale, et si c'est le cas, vous avez probablement oublié de remettre en question vos décisions.

Pour moi, le processus de trouver une architecture appropriée et, encore plus important, raisonnable était la chose clé que je voulais améliorer avec ce projet. Les différents composants semblaient assez "faciles" à implémenter et à construire, mais trouver le bon système, la bonne communication, et une belle pipeline de données propre était la partie vraiment intéressante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R99XRe-GvS5TO3wISTR5TA.jpeg)
_Premier Concept avec des composants supprimés_

Au début, j'avais quelques goulots d'étranglement dans ma conception qui, à un moment donné, auraient mis tout mon système à genoux. Dans cette situation, j'ai pensé à ajouter simplement plus de services "évolutifs" comme des files d'attente pour mettre en file d'attente la charge et la gérer.

Lorsque j'ai enfin eu une conception qui, je supposais, pouvait gérer une tonne de charge et était dynamiquement évolutive, c'était un désordre : trop de services, beaucoup de surcharge, et une structure globalement "sale".

Lorsque j'ai regardé l'architecture quelques jours plus tard, j'ai réalisé qu'il y avait tant de choses que je pouvais optimiser avec quelques changements. J'ai commencé à supprimer toutes les files d'attente et j'ai pensé à remplacer les machines virtuelles réelles par des composants FAAS.   
Après cette session, j'avais une conception beaucoup plus propre et toujours évolutive.

#### Pensez à la structure et aux technologies, pas aux implémentations

C'était l'une des erreurs que j'ai commises assez tôt dans le projet. J'ai commencé par regarder quels services IBM BlueMix pouvait offrir et j'ai continué à partir de là. Lesquels pourrais-je mélanger et utiliser dans ma conception qui semblaient fonctionner ensemble avec des déclencheurs et des files d'attente et tout le reste ?

En fin de compte, j'ai pu supprimer beaucoup de la surcharge en termes de services en m'éloignant simplement et en pensant à la structure globale et aux technologies dont j'avais besoin, plutôt qu'aux différentes implémentations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VbqzQHrKmzuQigKo_JnqvQ.png)
_Architecture Finale_

**Décomposé en quelques étapes distinctes**, le projet devrait :

* Toutes les heures (au début, puisque il n'y aurait que quelques articles pour le moment -> pourrait être fait toutes les minutes ou même toutes les secondes) obtenir les nouvelles de l'API [NewsAPI](http://newsapi.org/) et les stocker.
* Traiter chaque article, analyser le sentiment de celui-ci, et le stocker dans une base de données pour interrogation.
* Lors de la visite du site web, obtenir les données de la plage sélectionnée et afficher les barres/articles.

Donc, ce avec quoi j'ai finalement abouti était un déclencheur CloudWatch qui déclenche une fonction Lambda toutes les heures. Cette fonction obtient les données des nouvelles de la dernière heure à partir de NewsAPI. Elle enregistre ensuite chaque article sous forme de fichier JSON séparé dans un bucket S3.

Ce bucket, lors de la mise en place d'un objet, déclenche une autre fonction Lambda. Celle-ci charge le JSON depuis S3, crée un "contexte" pour l'apparition du mot partiel "vegan", et envoie le contexte créé à l'analyse de sentiment AWS Comprehend. Une fois que la fonction obtient les informations de sentiment pour l'article actuel, elle les écrit dans une table DynamoDB.

Cette table est la racine des données affichées dans le frontend. Elle donne à l'utilisateur quelques filtres avec lesquels il peut explorer les données un peu plus.

> _Si vous êtes intéressé par une explication plus approfondie, descendez à la description des composants séparés._

### Qui est "The One" Fournisseur de Cloud ?

Avant de savoir que j'allais utiliser AWS, j'ai essayé deux autres fournisseurs de cloud. C'est une vue très basique et extrêmement subjective sur quel fournisseur choisir, mais peut-être que cela aidera d'autres "débutants du Cloud" à choisir.

J'ai commencé avec le Cloud Bluemix d'IBM, je suis passé à Google Cloud, et j'ai finalement fini par utiliser AWS. Voici quelques-unes des "raisons" de mon choix.

Beaucoup des points listés ici montrent simplement à quel point la documentation globale et la communauté sont bonnes, combien des problèmes que j'ai rencontrés existaient déjà, et lesquels avaient des réponses sur StackOverflow.

#### La documentation et les communautés sont essentielles

Surtout pour les débutants et les personnes qui n'ont jamais travaillé avec les technologies cloud, c'est définitivement le cas. La documentation et, encore plus important, les exemples documentés et expliqués étaient simplement les meilleurs pour AWS.

Bien sûr, vous n'avez pas à vous contenter d'un seul fournisseur. Dans mon cas, j'aurais facilement pu utiliser les outils NLU de Google car, à mon avis, ils donnaient de meilleurs résultats. Je voulais simplement garder tout mon système sur une seule plateforme, et je peux toujours changer cela plus tard si je le souhaite.

Les packs de démarrage de tous les fournisseurs sont en fait vraiment sympas. Vous obtiendrez 300 $ sur Google Cloud qui vous permettront de faire beaucoup de choses. Cependant, c'est aussi un peu dangereux, car vous serez facturé si vous utilisez tout le montant et oubliez d'éteindre et de détruire tous les services qui accumulent les coûts.

BlueMix n'a qu'un accès très limité aux services sur leur niveau gratuit, ce qui est un peu malheureux si vous voulez tester toute la suite.

Amazon, pour moi, était le plus sympa, car ils ont aussi un niveau gratuit qui vous permettra d'utiliser presque toutes les fonctionnalités (certaines seulement avec la plus petite instance comme EC2.micro).

Comme je l'ai déjà mentionné, c'est une opinion très superficielle et subjective sur lequel choisir... Pour moi, AWS était le plus facile et le plus rapide à apprendre sans investir trop de temps au préalable.

### Les Composants

Le projet entier peut être divisé en trois composants principaux qui nécessitent du travail.

La **Collecte d'Articles**, qui consiste en le travail cron horaire, la fonction lambda qui appelle l'API NewsAPI, et le bucket S3 qui stocke tous les articles.

La partie **Enrichissement des Données** qui charge l'article depuis S3, crée le contexte et l'analyse en utilisant Comprehend, et la DynamoDB qui stocke les données enrichies pour une utilisation ultérieure dans le frontend.

Et le **Frontend** qui s'affiche lorsque les utilisateurs demandent la page web. Ce composant consiste en une interface utilisateur graphique, un service serveur évolutif qui sert la page web, et, à nouveau, la DynamoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5zlW79_Bp5JnyIFY-bj8vQ.png)

#### Collecte d'Articles

![Image](https://cdn-media-1.freecodecamp.org/images/1*n5S48v05Xr2ezB9Y4PQSDg.png)
_Partie Collecte d'Articles_

La première et probablement la partie la plus facile de tout le projet était de collecter tous les articles et nouvelles qui contiennent le mot-clé "vegan". Heureusement, il existe une tonne d'API qui fournissent un tel service.

L'une d'entre elles est [NewsAPI.org](https://newsapi.org).

Avec leur API, c'est extrêmement facile et compréhensible. Ils ont différents endpoints. L'un d'eux s'appelle "everything" qui, comme son nom l'indique, retourne simplement tous les articles qui contiennent un mot-clé donné.

En utilisant Node.js ici, cela ressemble à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1VDkST9u7M1fRcwUSjuU7g.png)
_Requête NewsAPI pour 1 heure de données depuis le début de l'année_

Le signe + devant la chaîne de requête "vegan" signifie simplement que le mot doit apparaître.

La taille de la page définit combien d'articles par requête seront retournés. Vous voulez définitivement garder un œil sur cela. Si, par exemple, votre système a une mémoire extrêmement limitée, il est logique de faire plus de requêtes (utiliser le curseur fourni) afin de ne pas planter l'instance avec des réponses trop grandes.

La réponse de NewsAPI.org ressemble à ceci. Si vous êtes intéressé à voir plus d'exemples, rendez-vous sur leur [site web](https://newsapi.org) où ils ont beaucoup d'exemples affichés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nku1tVq-Lel-Xi4DtbbHiQ.png)

Comme vous pouvez le voir, ces enregistrements d'articles ne donnent qu'une vue très basique de l'article lui-même. Des termes comme vegan, qui apparaissent dans un certain contexte à l'intérieur de l'article sans être le sujet principal, ne sont pas représentés dans le titre ou la description. Par conséquent, nous avons besoin du composant d'enrichissement des données, que nous couvrirons un peu plus tard. Cependant, c'est exactement le type de données JSON qui est stocké dans le bucket S3, prêt pour un traitement ultérieur.

Essayer une API localement et l'utiliser réellement dans le cloud est très similaire.   
Bien sûr, il y a quelques pièges où vous ne voulez pas coller votre clé API dans le code réel mais plutôt utiliser des variables d'environnement, mais c'est à peu près tout.

AWS a une interface graphique très soignée pour la configuration de leur Lambda. Elle vous aide vraiment à comprendre la structure de votre composant et à visualiser quels services et éléments y sont connectés.

Dans le cas du premier composant, nous avons le déclencheur horaire CloudWatch du côté "Entrée" et la journalisation avec CloudWatch et le bucket S3 comme système de stockage du côté "Sortie".

![Image](https://cdn-media-1.freecodecamp.org/images/1*0ENCoQJyv1VcMWEnBrkBjA.png)
_Interface graphique Lambda sur AWS_

Donc, après avoir tout assemblé, importé le SDK Node.JS pour AWS, et testé le script entier localement, je l'ai finalement déployé en tant que fonction Lambda.

Le script final est en fait assez court et compréhensible :

```js

const NewsAPI = require('newsapi')
const moment = require('moment')
const AWS = require('aws-sdk')

exports.handler = async (event) => {
  // Pour l'instant, nous devons interroger l'API toutes les heures car il y a très peu d'articles qui contiennent le mot veganisme
  const toTS = moment().format('YYYY-MM-DDTHH:mm:ss')
  const fromTS = moment(toTS).subtract(1, 'hour').format('YYYY-MM-DDTHH:mm:ss')

  const newsapi = new NewsAPI(process.env.API_KEY)
  const s3 = new AWS.S3()
  const myBucket = process.env.S3_BUCKET

  // Obtenir les nouvelles de la période donnée
  return new Promise((resolve, reject) => {
    newsapi.v2.everything({
      q: '+vegan',
      pageSize: 100,
      from: fromTS,
      to: toTS
    })
      .then(response => {
        console.log(`Travail avec un total de ${response.articles.length} articles.`)

        // Écrire tous les documents dans le bucket S3
        const promisedArticles = response.articles.map(article => {
          const myKey = `sov_${article.publishedAt}.json`

          const params = {Bucket: myBucket, Key: myKey, Body: JSON.stringify(article, null, 2)}

          // Sauvegarder l'enregistrement pour la clé donnée dans S3
          return new Promise((res, rej) => {
            s3.putObject(params, (err, data) => {
              if (err) {
                console.error(`Problème avec la persistance de l'article dans S3... ${err}`)
                rej(err)
                return
              }

              console.log(`Téléchargement réussi des données vers ${myBucket}/${myKey}`)
              res(`Téléchargement réussi des données vers ${myBucket}/${myKey}`)
            })
          })
        })
    })
      .catch(err => {
        console.error(`Rencontré un problème... ${err}`)
        reject(err)
      })
  })
}
view rawsov_article_collection.js hosted with f496 by GitHub
```

L'interface graphique a quelques fonctionnalités de test sympas avec lesquelles vous pouvez simplement déclencher votre fonction manuellement.

Mais rien ne fonctionnait...

Après quelques secondes de recherche sur Google, j'ai trouvé le terme "Politiques". J'en avais entendu parler avant, mais je n'avais jamais lu à leur sujet ou essayé de vraiment les comprendre.

En gros, elles décrivent ce que le service/utilisateur/groupe est autorisé à faire. C'était la pièce manquante : je devais permettre à ma fonction Lambda d'écrire quelque chose dans S3. (Je ne vais pas entrer dans les détails ici, mais si vous voulez passer aux politiques, n'hésitez pas à vous rendre à la fin de l'article.)

Une politique dans AWS est une configuration de style JSON simple qui, dans le cas de ma fonction de collecte d'articles, ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*npLW4w4HXBLauxSs4u2FTA.png)

C'est la configuration qui décrit le côté "Sortie" mentionné précédemment de la fonction. Dans les déclarations, nous pouvons voir qu'elle obtient l'accès à différentes méthodes des outils de journalisation et de S3.

La partie étrange concernant la ressource assignée pour le bucket S3 est que, si ce n'est pas précisé autrement dans les options de votre bucket S3, vous devez fournir à la fois la racine et "tout ce qui est en dessous" en tant que deux ressources séparées.

> _L'exemple donné ci-dessus permet à la fonction Lambda de faire n'importe quoi avec le bucket S3, mais ce n'est pas ainsi que vous devriez configurer votre système ! Vos composants ne devraient être autorisés à faire que ce pour quoi ils sont désignés._

Une fois cela entré, j'ai enfin pu voir les enregistrements être mis dans mon bucket S3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*clogAHGwONSIyv99B1NA9w.png)

#### Les caractères spéciaux sont maléfiques...

Lorsque j'ai essayé de récupérer les données du bucket S3, j'ai rencontré quelques problèmes. Il ne voulait tout simplement pas me donner le fichier JSON pour la clé qui avait été créée.   
J'ai eu du mal à trouver ce qui n'allait pas jusqu'à ce qu'à un moment donné, je réalise que, par défaut, AWS active la journalisation pour vos services.

**C'était de l'or !**

Lorsque j'ai regardé les journaux, le problème m'a sauté aux yeux immédiatement : il semblait que la valeur clé envoyée par le déclencheur S3 effectuait un encodage URL. Cependant, ce problème était absolument invisible lorsque l'on regardait simplement les noms de clés S3 où tout était affiché correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2xIG4cCs82orSaLIfkX9Rw.png)

La solution à ce problème était assez simple. J'ai simplement remplacé chaque caractère spécial par un tiret qui ne sera pas remplacé par une valeur encodée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7guV5ivMyrlBpjfF-ahLA.png)
_Solution au problème de clé encodée en URL_

**Assurez-vous donc de ne pas risquer de mettre des caractères spéciaux dans les clés. Cela pourrait vous faire économiser beaucoup de débogage et d'efforts.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*5zlW79_Bp5JnyIFY-bj8vQ.png)

#### Enrichissement des Données

![Image](https://cdn-media-1.freecodecamp.org/images/1*IlwXtAtgS5cea5aZ9yWS8w.png)
_Partie Enrichissement des Données_

Maintenant que nous avons tous les articles sous forme d'enregistrements individuels dans notre bucket S3, nous pouvons penser à l'enrichissement. Nous devons combiner certaines étapes afin de remplir notre pipeline qui, pour rappel, était le suivant :

* Obtenir l'enregistrement du bucket S3.
* Construire un contexte à partir de l'article réel en combinaison avec le titre et la description.
* Analyser le contexte créé et enrichir l'enregistrement avec le résultat.
* Écrire l'article enrichi dans notre table DynamoDB.

L'une des choses vraiment géniales à propos des Promesses en JavaScript est que vous pouvez modéliser des pipelines exactement de la manière dont vous les décririez en texte. Si nous comparons le code avec l'explication des étapes à suivre, nous pouvons voir la similarité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vJrmbTm85PTdHOF1iWOp7A.png)

Si vous regardez de plus près la première ligne du code ci-dessus, vous pouvez voir le gestionnaire d'exportation. Cette ligne est toujours prédéfinie dans les fonctions Lambda afin de savoir quelle méthode appeler. Cela signifie que votre propre code appartient aux accolades du bloc asynchrone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SBHLxOtPtDpdGQYuxKZLYQ.png)

Pour la partie Enrichissement des Données, nous avons besoin de quelques services supplémentaires. Nous voulons pouvoir envoyer et recevoir des données de l'analyse de sentiment Comprehend, écrire notre enregistrement final dans DynamoDB, et également avoir une journalisation.

Avez-vous remarqué le service S3 du côté "Sortie" ? **C'est pourquoi je mets toujours la Sortie entre guillemets**, même si nous voulons seulement lire les données ici. Il est affiché du côté droit. Je liste simplement tous les services avec lesquels notre fonction interagit.

La politique ressemble à celle du composant de collecte d'articles. Elle a simplement quelques ressources et règles supplémentaires qui définissent la relation entre Lambda et les autres services.

Même si Google Cloud, à mon avis, a les composants NLU "meilleurs", **j'adore la simplicité et l'API unifiée des services AWS.** Si vous avez utilisé l'un d'eux, vous pensez les connaître tous. Par exemple, voici comment obtenir un enregistrement de S3 et comment fonctionne la détection de sentiment en Node.js :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UBo_g5b4jZfu8trW0IViBA.png)

Probablement l'une des tâches les plus intéressantes du composant d'enrichissement des données était la création du "contexte" du mot vegan dans l'article.

Juste pour rappel — nous avons besoin de ce contexte, puisque beaucoup d'articles mentionnent simplement le mot "Vegan" sans avoir "Veganism" comme sujet.

Alors, comment extraire des parties d'un texte ? J'ai opté pour les expressions régulières. Elles sont incroyablement agréables à utiliser, et vous pouvez utiliser des terrains de jeu comme [Regex101](http://regex101.com) pour jouer et trouver la bonne regex pour votre cas d'utilisation.

Le défi était de trouver une regex qui pouvait trouver des phrases contenant le mot "vegan". D'une manière ou d'une autre, c'était plus difficile que je ne l'avais prévu pour généraliser des passages de texte entiers qui avaient également des sauts de ligne, etc.

La regex finale ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*b_89-CiPEPHGp0OSvONsMQ.png)

Le problème était que pour les textes longs, cela ne fonctionnait pas en raison de problèmes de délai d'exécution. La solution dans ce cas était assez "simple"... J'ai simplement parcouru le texte et l'ai divisé par des sauts de ligne, ce qui l'a rendu beaucoup plus facile à traiter pour le module RegEx.

En fin de compte, toute la création de "contexte" était un mélange de **division du texte, filtrage des passages contenant le mot vegan, extraction de la phrase correspondante de ce passage, et réassemblage** afin qu'il puisse être utilisé dans l'analyse de sentiment.

Le titre et la description peuvent également jouer un rôle, donc je les ai ajoutés au contexte s'ils contenaient le mot "vegan".

![Image](https://cdn-media-1.freecodecamp.org/images/1*QUpaU_yM3s_Wh35ZeuXseA.png)

Une fois tout le code pour les différentes étapes en place, j'ai pensé pouvoir commencer à construire le frontend. Mais quelque chose n'allait pas. Certains des enregistrements n'apparaissaient tout simplement pas dans ma table DynamoDB...

#### **Les chaînes vides dans DynamoDB sont également maléfiques**

En vérifiant l'état de mon système déjà en cours d'exécution, j'ai réalisé que certains des articles ne seraient pas convertis en entrée de table DynamoDB du tout.

Après avoir consulté les journaux, j'ai trouvé cette exception qui m'a absolument confus...

![Image](https://cdn-media-1.freecodecamp.org/images/1*FlYJ6Ppo2K39VD7d1yW_eg.png)

Pour être honnête, c'était un comportement vraiment étrange puisque, comme indiqué dans la [discussion](https://forums.aws.amazon.com/thread.jspa?threadID=90137), la sémantique et l'utilisation d'une chaîne vide sont absolument différentes de celles d'une valeur Null.

Cependant, puisque je ne pouvais rien changer à la conception de DynamoDB, j'ai dû trouver une solution pour éviter d'obtenir l'erreur de chaîne vide.

Dans mon cas, c'était vraiment facile. J'ai simplement parcouru tout l'objet JSON et vérifié s'il y avait une chaîne vide ou non. Si c'était le cas, j'ai simplement remplacé la valeur par null. C'est tout, ça marche comme un charme et ne cause aucun problème. (J'ai dû vérifier si cela avait une valeur dans le frontend, cependant, puisque obtenir la longueur d'une valeur null lance une erreur).

![Image](https://cdn-media-1.freecodecamp.org/images/1*dFMXmp_QV3mD0hLCpWU-bg.png)
_Correction "saleté" pour le problème de chaîne vide_

#### Frontend

![Image](https://cdn-media-1.freecodecamp.org/images/1*KKkHqw0BwU5wn6hWQ1JY8w.png)
_Partie Frontend_

La dernière partie était de créer un frontend et de le déployer afin que les gens puissent visiter la page et voir le [StateOfVeganism](http://stateofveganism.com).

Bien sûr, je réfléchissais à savoir si je devais utiliser l'un de ces frameworks frontend fantaisistes comme Angular, React ou Vue.js... Mais, eh bien, je suis allé pour l'ancienne école, du HTML, CSS et JavaScript simples.

**L'idée que j'avais pour le frontend était extrêmement minimaliste**. En gros, c'était juste une barre divisée en trois sections : Positive, Neutre et Négative. En cliquant sur l'une d'entre elles, elle affichait quelques titres et liens vers des articles classés avec ce sentiment.

En fin de compte, c'est exactement ce que c'est devenu. Vous pouvez [consulter la page ici](http://sovfrontend-env.qrg7cy6rmq.us-east-1.elasticbeanstalk.com). J'ai pensé à la rendre active sur stateOfVeganism.com, mais nous verrons...

![Image](https://cdn-media-1.freecodecamp.org/images/1*GiLmRO1YMnLr3dL9OW8g3A.png)
_Interface graphique de StateOfVegnsim_

> _Assurez-vous de noter le troisième article amusant des articles qui ont été classés comme "Négatifs" ;)_

Déployer le frontend sur l'un des services AWS était une autre chose à laquelle je devais réfléchir. Je voulais définitivement prendre un service qui incorporait déjà la mise à l'échelle élastique, donc j'ai dû choisir entre Elastic Container Service ou Elastic Beanstalk (instances EC2 réelles).

En fin de compte, j'ai opté pour Beanstalk, car j'ai vraiment aimé l'approche directe et le déploiement incroyablement facile. Vous pouvez pratiquement le comparer à Heroku dans la manière dont vous le configurez.

Note de côté : J'ai eu quelques problèmes avec mon groupe de mise à l'échelle automatique qui n'était pas autorisé à déployer des instances EC2, car j'utilise le niveau gratuit sur AWS. Mais après quelques emails avec le support AWS, tout a fonctionné directement.

J'ai simplement déployé une application serveur Express Node.js qui sert mon frontend sur chaque chemin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kXVcV9_NmIu-CXIvMUO-qQ.png)

Cette configuration, par défaut, fournit le fichier index.html qui réside dans le dossier "public", ce qui est exactement ce que je voulais.

Bien sûr, c'est la configuration la plus basique. Pour la plupart des applications, ce n'est pas la méthode recommandée, puisque vous devez d'une manière ou d'une autre fournir les informations d'identification afin d'accéder à la table DynamoDB. Il serait préférable de faire un peu de rendu côté serveur et de stocker les informations d'identification dans des variables d'environnement afin que personne ne puisse y accéder.

#### Jouer les cool et déployer les clés AWS dans le frontend

C'est quelque chose que vous ne devriez jamais faire. Cependant, puisque j'ai restreint l'accès de ces informations d'identification à la seule méthode de balayage de la table DynamoDB, vous pouvez avoir la chance de creuser plus profondément dans mes données si vous êtes intéressé.

J'ai également restreint le nombre de requêtes qui peuvent être effectuées, de sorte que les informations d'identification "cesseront de fonctionner" une fois la limite mensuelle gratuite dépassée, juste pour être sûr.

Mais n'hésitez pas à regarder les données et à jouer un peu si vous êtes intéressé. Assurez-vous simplement de ne pas en faire trop, puisque l'API cessera de fournir les données au frontend à un moment donné.

### Politiques, Politiques ?... Politiques !

Lorsque j'ai commencé à travailler avec les technologies cloud, j'ai réalisé qu'il devait y avoir un moyen de permettre/restreindre l'accès aux composants individuels et de créer des relations. C'est là que les politiques entrent en jeu. Elles vous aident également à faire de la gestion d'accès en vous donnant les outils dont vous avez besoin pour donner des permissions à des utilisateurs et groupes spécifiques. À un moment donné, vous allez probablement lutter avec ce sujet, donc il est logique de [lire un peu à ce sujet](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

Il existe essentiellement deux types de politiques dans AWS. Les deux sont des fichiers de configuration de style JSON simple. Cependant, l'une d'entre elles est assignée à la ressource elle-même, par exemple S3, et l'autre est assignée à des rôles, utilisateurs ou groupes.

Le tableau ci-dessous montre quelques déclarations très approximatives sur la politique que vous pourriez vouloir choisir pour votre tâche.

Alors, quelle est la différence réelle ? Cela peut devenir plus clair lorsque nous comparons des exemples des deux types de politiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwRRc2V_eXU8mHyFk9n6Jw.png)
_Politique IAM et Politique de Ressource_

La politique de gauche est la Politique IAM (ou Basée sur l'Identité). Celle de droite est la Politique de Ressource (Basée sur les Ressources).

Si nous commençons à les comparer ligne par ligne, nous ne pouvons voir aucune différence jusqu'à ce que nous atteignions la première déclaration qui définit certaines règles liées à un service. Dans ce cas, c'est S3.

Dans la Politique de Ressource, nous voyons un attribut appelé "Principal" qui est absent dans la Politique IAM. Dans le contexte d'une Politique de Ressource, cela décrit les entités qui sont "assignées" à cette règle. Dans l'exemple donné ci-dessus, ce seraient les utilisateurs, Alice et root.

D'un autre côté, pour obtenir le même résultat avec les Politiques IAM, nous devrions assigner la politique de gauche à nos utilisateurs existants, Alice et root.

Selon votre cas d'utilisation, il peut être logique d'utiliser l'une ou l'autre. C'est aussi une question de ce que votre "style" ou la convention de votre lieu de travail est.

### Qu'est-ce qui suit ?

[StateOfVeganism](http://sovfrontend-env.qrg7cy6rmq.us-east-1.elasticbeanstalk.com) est déjà en ligne. Cependant, cela ne signifie pas qu'il n'y a rien à améliorer. Une chose sur laquelle je dois définitivement travailler est, par exemple, que les recettes de Pinterest ne soient pas classées comme "Positives" mais plutôt "Neutres". Mais la fonctionnalité de base fonctionne comme prévu. Le pipeline de données fonctionne bien, et si quelque chose devait mal se passer, j'aurai une belle journalisation avec CloudWatch déjà activée.

C'était génial de vraiment réfléchir et de construire un tel système. Remettre en question mes décisions a été très utile pour optimiser toute l'architecture.

La prochaine fois que vous pensez à construire un projet secondaire, pensez à le construire avec l'un des fournisseurs de cloud. Cela peut être un investissement en temps plus important au début, mais **apprendre à utiliser et à construire des systèmes avec une infrastructure comme AWS aide vraiment à grandir en tant que développeur**.

J'adorerais entendre parler de vos projets et de ce que vous construisez. [Contactez-moi](mailto:contact.timgrossmann@gmail.com) et parlez-moi d'eux.

Merci d'avoir lu. Assurez-vous de me suivre sur [YouTube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg) et de mettre une étoile à [StateOfVeganism sur GitHub](https://github.com/timgrossmann/stateOfVeganism).

N'oubliez pas de cliquer sur le bouton d'applaudissements et de me suivre sur [Twitter](https://twitter.com/timigrossmann), [GitHub](https://github.com/timgrossmann), [Youtube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg), et [Facebook](https://www.facebook.com/profile.php?id=100000656212416) pour me suivre dans mon voyage.

Je suis toujours à la recherche de nouvelles opportunités.  
Donc [n'hésitez pas à me contacter](mailto:contact.timgrossmann@gmail.com). J'adorerais entrer en contact avec vous.

**De plus, je planifie actuellement de faire un stage de six mois à Singapour à partir de mars 2019. J'aimerais rencontrer autant d'entre vous que possible. Si vous vivez à Singapour, n'hésitez pas à me contacter. J'adorerais discuter autour d'un café ou d'un déjeuner.**