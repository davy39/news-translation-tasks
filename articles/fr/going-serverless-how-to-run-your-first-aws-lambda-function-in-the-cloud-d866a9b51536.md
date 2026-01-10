---
title: 'Passer au Serverless : comment exécuter votre première fonction AWS Lambda
  dans le cloud'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-07T20:49:36.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-how-to-run-your-first-aws-lambda-function-in-the-cloud-d866a9b51536
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PxgWkgtWcOBFUyPHiwv96w.jpeg
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Passer au Serverless : comment exécuter votre première fonction AWS Lambda
  dans le cloud'
seo_desc: 'By Adam Watt

  A decade ago, cloud servers abstracted away physical servers. And now, “Serverless”
  is abstracting away cloud servers.

  Technically, the servers are still there. You just don’t need to manage them anymore.

  Another advantage of going serve...'
---

Par Adam Watt

Il y a une décennie, les serveurs cloud ont abstrait les serveurs physiques. Et maintenant, le "Serverless" abstrait les serveurs cloud.

Techniquement, les serveurs sont toujours là. Vous n'avez simplement plus besoin de les gérer.

Un autre avantage du serverless est que vous n'avez plus besoin de maintenir un serveur en fonctionnement en permanence. Le "serveur" apparaît soudainement lorsque vous en avez besoin, puis disparaît lorsque vous avez terminé. Maintenant, vous pouvez penser en termes de fonctions plutôt que de serveurs, et toute votre logique métier peut désormais résider dans ces fonctions.

Dans le cas des fonctions AWS Lambda, cela s'appelle un déclencheur. Les fonctions Lambda peuvent être déclenchées de différentes manières : une requête HTTP, un nouveau téléchargement de document vers S3, un travail planifié, un flux de données AWS Kinesis, ou une notification d'AWS Simple Notification Service (SNS).

Dans ce tutoriel, je vais vous montrer comment configurer votre propre fonction Lambda et, en bonus, comment configurer une API REST entièrement dans le cloud AWS, tout en écrivant un minimum de code.

Notez que les avantages et inconvénients du Serverless dépendent de votre cas d'utilisation spécifique. Donc dans cet article, je ne vais pas vous dire si le Serverless est adapté à votre application particulière — je vais simplement vous montrer comment l'utiliser.

Tout d'abord, vous aurez besoin d'un compte AWS. Si vous n'en avez pas encore, commencez par ouvrir un compte AWS gratuit [ici](https://aws.amazon.com/free). AWS propose un niveau gratuit qui est plus que suffisant pour ce dont vous aurez besoin pour ce tutoriel.

Nous allons écrire la fonction isPalindrome, qui vérifie si une chaîne de caractères passée est un palindrome ou non.

Ci-dessus se trouve un exemple d'implémentation en JavaScript. Voici le [lien](https://gist.github.com/AWattNY/1fae83d8de8756c9d9b946e36307e8fc85695ae4458c4c2239558c) vers le gist sur GitHub.

Un palindrome est un mot, une phrase ou une séquence qui se lit de la même manière à l'envers qu'à l'endroit. Pour simplifier, nous limiterons la fonction aux mots uniquement.

Comme nous pouvons le voir dans l'extrait ci-dessus, nous prenons la chaîne, nous la divisons, nous l'inversons et puis nous la rejoignons. Si la chaîne et son inverse sont égales, la chaîne est un palindrome, sinon la chaîne n'est pas un palindrome.

### Création de la fonction Lambda isPalindrome

Dans cette étape, nous allons nous rendre dans la console AWS pour créer la fonction Lambda :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1zvZPTbNqf0Rq8eNRzO4A.png)

Dans la console AWS, allez dans Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/1*InZiSTx4EkPmnU7MTYFdCA.png)

Puis appuyez sur « Commencer maintenant ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*v3jOWwns_L-lOAIw57681Q.png)

Pour l'environnement d'exécution, sélectionnez Node.js 6.10, puis appuyez sur « Fonction vide ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*yttJpvtjhSxZ_v6pD3fpig.png)

Passez cette étape et appuyez sur « Suivant ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*sPQEC7nW-TKo-hSerjZlMg.png)

Pour le nom, tapez isPalindrome, pour la description, tapez une description de votre nouvelle fonction Lambda, ou laissez-la vide.

Comme vous pouvez le voir dans le [gist](https://gist.github.com/AWattNY/1b4eda8b807702c0fa9700c4a130fbf7) ci-dessus, une fonction Lambda est simplement une fonction que nous exportons en tant que module, dans ce cas, nommée handler. La fonction prend trois paramètres : event, context et une fonction de rappel.

Le rappel s'exécutera lorsque la fonction Lambda sera terminée et retournera une réponse ou un message d'erreur. Pour le modèle de réponse Lambda vide, la réponse est codée en dur comme la chaîne 'Hello from Lambda'. Pour ce tutoriel, comme il n'y aura pas de gestion d'erreurs, vous utiliserez simplement Null. Nous examinerons de près le paramètre event dans les prochaines diapositives.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y1anI0TWRKPJJ8-6-w69Cw.png)

Faites défiler vers le bas. Pour le rôle, choisissez « Créer un nouveau rôle à partir d'un modèle », et pour le nom du rôle, utilisez isPalindromeRole ou tout autre nom que vous souhaitez.

Pour les modèles de stratégie, choisissez les permissions « Microservice simple ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*qzWhNvjuhgxVSzZKyrqTuw.png)

Pour la mémoire, 128 mégaoctets sont plus que suffisants pour notre fonction simple.

En ce qui concerne le délai d'expiration de 3 secondes, cela signifie que — si la fonction ne retourne pas de réponse dans les 3 secondes — AWS la fermera et retournera une erreur. Trois secondes sont également plus que suffisantes.

Laissez le reste des paramètres avancés inchangés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J99U-snM3CEdoUxRFrfwJg.png)

Appuyez sur « Créer une fonction ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*xeO4D25rwD2jrD0wlyWFig.png)

Félicitations — vous avez créé votre première fonction Lambda. Pour la tester, appuyez sur « Test ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*tAfq6s_0RfWp100ILkmXEQ.png)

Comme vous pouvez le voir, votre fonction Lambda retourne la réponse codée en dur « Hello from Lambda ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*zD0WI6ysj8ejQZg3wXzi_w.png)

Maintenant, ajoutez le code de isPalindrome.js à votre fonction Lambda, mais au lieu de `return result`, utilisez `callback(null, result)`. Ensuite, ajoutez une valeur de chaîne codée en dur `abcd` à la ligne 3 et appuyez sur « Test ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*Du_fuYYkirD8FsxBSaZI6g.png)

La fonction Lambda devrait retourner « abcd n'est pas un palindrome ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*AVUDU79JgxwseK7Bgq5j3g.png)

Pour la valeur de chaîne codée en dur « racecar », la fonction Lambda retourne « racecar est un palindrome ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*e1x97cP2R4qa1EgrfsTIpA.png)

Jusqu'à présent, la fonction Lambda que nous avons créée se comporte comme prévu.

Dans les prochaines étapes, je vais vous montrer comment la déclencher et lui passer un argument de chaîne en utilisant une requête HTTP.

Si vous avez déjà construit des API REST à partir de zéro en utilisant un outil comme Express.js, l'[extrait](https://gist.github.com/AWattNY/50741f8601289b5b6d560d4776fb6162) ci-dessus devrait vous être familier. Vous créez d'abord un serveur, puis définissez toutes vos routes une par une.

Dans cette section, je vais vous montrer comment faire la même chose en utilisant la passerelle API AWS.

### Création de la passerelle API

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZclBoLSJm0mOx1-U_46J6w.png)

Allez dans votre console AWS et appuyez sur « API Gateway ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*JmFWNloht1UGnrR2p_tJCg.png)

Puis appuyez sur « Commencer ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*cUdB6sbEmXljuOh6xA2CkA.png)

Dans le tableau de bord de création d'une nouvelle API, sélectionnez « Nouvelle API ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*BtMmOdLCJH3mOOwu1iqdbg.png)

Pour le nom de l'API, utilisez « palindromeAPI ». Pour la description, tapez une description de votre nouvelle API ou laissez-la vide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v0ONd5gjG7_2GD53hf2R-g.png)

Notre API sera simple et n'aura qu'une seule méthode GET qui sera utilisée pour communiquer avec la fonction Lambda.

Dans le menu Actions, sélectionnez « Créer une méthode ». Un petit sous-menu apparaîtra. Allez-y et sélectionnez GET, puis cliquez sur la coche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-hBon4l3x8Djqe8gkP8FaQ.png)

Pour le type d'intégration, sélectionnez Fonction Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b2ZLauodGV0PhAGMfuqS-Q.png)

Puis appuyez sur « OK ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*enal7klPDe2YUgVgNv3GyQ.png)

Dans l'écran d'exécution de la méthode GET, appuyez sur « Requête d'intégration ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*xESNRDWg8-YRdp4O4n3J9g.png)

Pour le type d'intégration, assurez-vous que Fonction Lambda est sélectionné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tqZ6DaWFuWELN_CuexvAyg.png)

Pour le passage du corps de la requête, sélectionnez « Lorsqu'il n'y a pas de modèles définis » et pour Content-Type, entrez « application/json ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wrxe17v1TwC9VsmhoO3bzQ.png)

Dans l'espace vide, ajoutez l'objet JSON montré ci-dessous. Cet objet JSON définit le paramètre « string » qui nous permettra de passer des valeurs de chaîne à la fonction Lambda en utilisant une requête HTTP GET. Cela est similaire à l'utilisation de `req.params` dans Express.js.

Dans les prochaines étapes, nous verrons comment passer la valeur de chaîne à la fonction Lambda et comment accéder à la valeur passée depuis l'intérieur de la fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h5ToO2kS-L7omHU38zkZKQ.png)

L'API est maintenant prête à être déployée. Dans le menu Actions, cliquez sur « Déployer l'API ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZW43YsKKFY6W1J949ma9DQ.png)

Pour l'étape de déploiement, sélectionnez « [Nouvelle étape] ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*O8eS2Pnka9DxLkgGnttcxQ.png)

Et pour le nom de l'étape, utilisez « prod » (qui est l'abréviation de « production »).

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1tQG72coTJkxTOt4VIDmQ.png)

L'API est maintenant déployée, et l'URL d'invocation sera utilisée pour communiquer via une requête HTTP avec Lambda. Si vous vous souvenez, en plus d'un rappel, Lambda prend deux paramètres : event et context.

Pour envoyer une valeur de chaîne à Lambda, vous prenez l'URL d'invocation de votre fonction et vous y ajoutez `?string=someValue`, puis la valeur passée peut être accessible depuis l'intérieur de la fonction en utilisant `event.string`.

Modifiez le code en supprimant la valeur de chaîne codée en dur et en la remplaçant par `event.string` comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DnkdYgHUaTKOmRfvFwUSVg.png)

Maintenant, dans le navigateur, prenez l'URL d'invocation de votre fonction et ajoutez `?string=abcd` pour tester votre fonction via le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BFphcVCa21NOehuL.png)

Comme vous pouvez le voir, Lambda répond que abcd n'est pas un palindrome. Faites de même pour racecar.

![Image](https://cdn-media-1.freecodecamp.org/images/0*m78OHG2PLRqpudhA.png)

Si vous préférez, vous pouvez également utiliser Postman pour tester votre nouvelle fonction Lambda isPalindrome. Postman est un excellent outil pour tester vos points de terminaison d'API, vous pouvez en apprendre plus à ce sujet [ici](https://www.getpostman.com/).

Pour vérifier qu'elle fonctionne, voici un palindrome :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bX9E0bUCMgMLJaxVGMTgKQ.png)

Et voici un non-palindrome :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9K9rmcnTwbXD9FtrmBr-yA.png)

Félicitations — vous venez de configurer et de déployer votre propre fonction Lambda !

Merci d'avoir lu !