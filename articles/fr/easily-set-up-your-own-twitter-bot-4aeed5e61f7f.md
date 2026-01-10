---
title: Pourquoi vous devriez avoir votre propre bot Twitter, et comment en créer un
  en moins de 30 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-28T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/easily-set-up-your-own-twitter-bot-4aeed5e61f7f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TZYrBalMX5If2Jj3.jpg
tags:
- name: bots
  slug: bots
- name: JavaScript
  slug: javascript
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
seo_title: Pourquoi vous devriez avoir votre propre bot Twitter, et comment en créer
  un en moins de 30 minutes
seo_desc: 'By Scott Spence


  UPDATE 20171102: Since this story was originally posted back in January 2017 there
  have been a few things that have changed with the repository on GitHub, if you are
  going to be following along I’d suggest using the repository [READM...'
---

Par Scott Spence

> **MISE À JOUR 20171102 :** Depuis la publication initiale de cet article en janvier 2017, quelques changements ont été apportés au dépôt sur GitHub. Si vous suivez ce guide, je vous suggère d'utiliser le dépôt `[README.md](https://github.com/spences10/twitter-bot-bootstrap/#twitter-bot-bootstrap)` en complément de cet article pour éviter toute confusion.

Les bots Twitter peuvent faire bien plus que simplement spammer des hashtags tendance et suivre sans relâche des utilisateurs.

Prenez par exemple le bot [Twisst ISS alerts](https://twitter.com/twisst), qui vous envoie un message direct chaque fois que la station spatiale internationale (ISS) sera visible depuis votre emplacement.

Ou encore des bots de service public comme [Earthquake Robot](https://twitter.com/earthquakeBot), qui tweete sur tout séisme supérieur à 5,0 sur l'échelle de Richter dès qu'il se produit.

Et bien sûr, un robot qui tweete de la poésie, [poem.exe](https://twitter.com/poem_exe), ainsi qu'un autre qui retweete vos tweets qui se trouvent être des [Accidental Haiku](https://twitter.com/accidental575).

Personnellement, j'utilise un bot pour améliorer mon compte [@ScottDevTweets](https://twitter.com/ScottDevTweets) en aimant et retweetant des sujets qui m'intéressent.

Le défi communautaire [#100DaysOfCode](https://twitter.com/search?q=%23100DaysOfCode&src=savs) vous félicitera lorsque vous commencerez le défi #100DaysOfCode, et à nouveau lorsque vous atteindrez des étapes spécifiques.

![Image](https://cdn-media-1.freecodecamp.org/images/yi92dikGnakxhxMqH9UsdkUTX7akOOyOC3hi)
_Félicitations du bot utilisateur_

Il répondra également avec des encouragements s'il détecte un sentiment négatif (frustration) dans un tweet contenant le hashtag #100DaysOfCode.

![Image](https://cdn-media-1.freecodecamp.org/images/4GbSvxcYAx7pbZ8fP32hyr97WymQ4I-A693F)
_Détection de sentiment par le bot_

Une question qu'on me pose souvent lors des entretiens d'embauche est : « Qu'est-ce que vous retirez du travail avec la technologie ? » Je réponds toujours que « J'aime automatiser les tâches répétitives pour gagner du temps et me concentrer sur d'autres choses. J'aime le sentiment d'accomplissement qui vient du fait d'avoir gagné du temps. »

Dans le cas de mon bot @ScottDevTweets, il sert souvent d'ouverture à une conversation avec une autre personne qui me suit. Ainsi, le bot peut initier la conversation, puis je peux prendre le relais là où le bot s'est arrêté.

Gardant cela à l'esprit, un bot n'est aussi éthique que la personne qui l'a programmé.

Si vous avez des doutes sur l'éthique du bot que vous construisez, consultez la section éthique de [botwiki](https://botwiki.org/bot-ethics).

Alors, prêt à commencer ? OK. C'est parti !

### Comment créer un bot Twitter en 30 minutes

Vous allez utiliser la bibliothèque `twit` pour créer un bot Twitter. Il aimera et retweetera ce que vous spécifiez. Il répondra également à vos abonnés avec une sélection de réponses préenregistrées.

Avant de commencer le chronomètre, vous devrez configurer quelques comptes si vous ne les avez pas déjà.

### Ce dont vous aurez besoin

* [Twitter](https://twitter.com/signup)
* [Cloud9 IDE](https://c9.io/signup)
* [Heroku](https://signup.heroku.com/)

### Étape #1 : Configurer une application Twitter

Soit créez un nouveau compte Twitter, soit utilisez le vôtre pour [créer une nouvelle application Twitter](https://apps.twitter.com/app/new).

Par exemple, je vais configurer mon ancien compte Twitter [@DroidScott](https://twitter.com/droidscott) pour que vous puissiez suivre.

Assurez-vous d'ajouter votre numéro de téléphone à votre compte Twitter avant de cliquer sur le bouton **Créer votre application Twitter**.

![Image](https://cdn-media-1.freecodecamp.org/images/8uxpErBxq4u2urpsGU6xSOU40OljUdwAxGYb)

Vous devriez maintenant être dans la section « Gestion de l'application », où vous devrez noter vos clés. Vous devriez déjà avoir votre « Consumer Key (API Key) » et « Consumer Secret (API Secret) ».

Vous devrez faire défiler jusqu'en bas de la page et cliquer sur **Créer mon jeton d'accès** pour obtenir le « Access Token » et « Access Token Secret ». Notez les quatre, vous en aurez besoin lors de la configuration du bot.

### Étape #2 : Configurer votre environnement de développement

Pour cela, je vais simplement dire d'utiliser [Cloud9](https://c9.io/) car vous pouvez être opérationnel en quelques minutes avec l'un des environnements Node.js préconfigurés.

Notez que si vous choisissez d'utiliser Heroku et/ou Cloud9 IDE pour construire cela (comme je le fais dans ce guide), dans certaines régions, vous serez invité à fournir un numéro de carte de crédit pour créer ces comptes.

![Image](https://cdn-media-1.freecodecamp.org/images/-TD2WPEtoVjnBY0hfFD0HEocqZyqVaaCN7m3)

### Configurer le bot

Dans l'arborescence du projet, supprimez les fichiers de l'exemple de projet `client`, `package.json`, `README.md` et `server.js`, vous n'en aurez pas besoin. Vous pouvez les laisser si vous le souhaitez.

Dans votre nouvel environnement Node.js c9, allez dans le terminal et entrez :

```
git clone https://github.com/spences10/twitter-bot-bootstrap
```

#### Structure du projet

L'arborescence du projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/erBjIDDknKxvS0B3GHKLFMIbDM81iOj0kgoW)

### Dépendances Node

Avant de configurer le bot, nous devons installer les dépendances. Accédez au dossier du projet avec `cd tw*`, ce qui vous déplacera vers `:~/workspace/twitter-bot-bootstrap (master) $`. Depuis le terminal, entrez :

```
npm install
```

Cela installera toutes les dépendances listées dans le fichier `package.json`.

Si vous obtenez des erreurs, je suggère d'installer les dépendances une par une depuis le fichier `package.json` avec la même commande et le nom du package à la fin :

Voici un exemple des `dependencies` dans le fichier `package.json` :

```
"dependencies": {    "dotenv": "^4.0.0",    "twit": "^2.2.5",    "unique-random-array": "^1.0.0",    "unirest": "^0.5.1"  }
```

La commande npm pour les installer tous :

```
npm install --save dotenv twit unique-random-array unirest
```

Si vous obtenez des messages `WARN` tels que `npm WARN package.json twitter-bot@1.0.0 No repository field`, cela n'empêchera pas le bot de fonctionner, vous pouvez donc les ignorer.

Vous pouvez maintenant configurer le bot. Depuis le terminal, entrez :

```
npm init
```

Cela configurera le fichier `package.json` avec vos détails. Continuez à appuyer sur Entrée si vous êtes satisfait des valeurs par défaut.

Maintenant, vous devrez ajouter vos clés Twitter au fichier `.env`. Il suffit d'entrer les clés dans leurs champs correspondants et d'enregistrer le fichier.

Si vous ne trouvez pas le fichier `.env` dans la structure de fichiers de votre projet c9, vous devrez activer l'option `Show Hidden Files`. Dans la vue des fichiers, sélectionnez l'icône d'engrenage des paramètres, puis cochez l'option `Show Hidden Files` si elle n'est pas déjà cochée.

![Image](https://cdn-media-1.freecodecamp.org/images/0dqpIHTE7aBEBFVSOmpoU1mGGu4U79w7HH4R)

La `SENTIMENT_KEY` peut être obtenue en demandant une nouvelle clé API à l'adresse [https://market.mashape.com/vivekn/sentiment-3](https://market.mashape.com/vivekn/sentiment-3). Votre clé se trouve dans l'exemple de requête.

Regardez le gif, cliquez sur le lien, inscrivez-vous ou connectez-vous à `mashape`, cliquez sur `node` dans le panneau de droite et sélectionnez votre clé API, elle se trouvera dans l'espace mis en évidence `<requir`ed> dans le gif.

![Image](https://cdn-media-1.freecodecamp.org/images/XuwVyc42-Ji2JZp3xdAambdU-4ZstLu3h5MK)

Ajoutez votre clé API au fichier `.env` ainsi que vos clés Twitter API ?

Ici, vous devriez ajouter le nom de votre compte Twitter et la fréquence à laquelle vous souhaitez que le bot exécute les fonctions de retweet et de favoris en minutes.

> _NOTE : aucun des éléments `.env` n'a de guillemets `''` autour d'eux._

```
CONSUMER_KEY=Fw***********P9CONSUMER_SECRET=TD************CqACCESS_TOKEN=31**************UCACCESS_TOKEN_SECRET=r0************S2SENTIMENT_KEY=Gj************lFTWITTER_USERNAME=DroidScottTWITTER_RETWEET_RATE=5TWITTER_FAVORITE_RATE=5
```

Vous pouvez ensuite ajouter des mots-clés dans le fichier `strings.js` pour ce que vous souhaitez rechercher ainsi que des sous-requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/cyIPkBgnegAaQhazsjKGk4vlYlMYaSri99Ak)
_ajoutez des chaînes de requête et de sous-requête, vous pouvez également mettre à jour les chaînes bloquées pour bloquer plus de contenu_

Lorsque vous ajoutez des chaînes de sous-requête, assurez-vous de laisser un espace au début de la chaîne afin que `' handy tip'` soit concaténé à `'node.js'` comme `node.js handy tip` et non `node.jshandy tip`.

Cela devrait être tout, allez dans le terminal et entrez `npm start`, vous devriez obtenir une sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/cAf4CXWtySOLnJo3QH3xGB6e4PvGNY8veFhB)

Vérifiez le compte Twitter :

![Image](https://cdn-media-1.freecodecamp.org/images/OpqXq42iaf4kkk7xcn5G-OXg8BgrCc3uyECI)

### Étape #3 : Configuration de Heroku

Super, maintenant nous avons un bot que nous pouvons tester sur notre environnement de développement, mais nous ne pouvons pas le laisser là, nous devons le déployer sur Heroku.

Si vous ne l'avez pas déjà fait, configurez un [compte Heroku](https://signup.heroku.com/), puis sélectionnez **Créer une nouvelle application** dans la liste déroulante en haut à droite de votre tableau de bord. Dans l'écran suivant, nommez l'application si vous le souhaitez, puis cliquez sur **Créer une application**.

![Image](https://cdn-media-1.freecodecamp.org/images/tNXyeqUx-eoCk-QwAtTPcuepDfzYAJh97Xtx)

Vous serez présenté avec votre tableau de bord d'application et des instructions pour la méthode de déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/VgCHJpWojzMLrRkYhA2eX2lC-S7Wnh3iZNTS)

Le nom de votre application devrait s'afficher en haut de votre tableau de bord, vous en aurez besoin lors de la connexion avec l'interface de ligne de commande Heroku, que nous utiliserons pour déployer votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/MXb1DLOg1pHuhv52dISmbAAx93a3TpwV0-si)

### Heroku CLI

Nous allons déployer initialement via l'interface de ligne de commande Heroku (_CLI_).

Dans le terminal de votre environnement c9, connectez-vous à Heroku [il devrait être installé par défaut]

```
heroku login
```

Entrez vos identifiants :

```
cd twitter-bot-bootstrap git init heroku git:remote -a your-heroku-app-name
```

Déployez votre application :

```
git add . git commit -am 'make it better' git push heroku master
```

Vous devriez obtenir une sortie de construction dans le terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/LAyCTurdXyrBq0RVcNX9oFje4NH31heVA9yd)

Puis vérifiez la sortie avec :

```
heroku logs -t
```

Tout est bon ? Super ! ?

#### Configuration des variables Heroku

Maintenant que nous avons notre bot sur Heroku, nous devons ajouter des variables d'environnement pour stocker nos clés Twitter. Cela est dû au fait que le fichier `.env` où nous avons stocké nos clés est listé dans le fichier `.gitignore`, qui indique à git de ne pas télécharger ce fichier sur Heroku. Cela signifie également que si, à l'avenir, nous voulons ajouter notre code à GitHub, nous n'avons pas à nous soucier du fichier `.env` rendant nos clés publiques, car le fichier sera automatiquement ignoré.

Tout ce que vous avez à faire est d'aller dans la console de votre application Heroku et de sélectionner la section « Paramètres » et d'ajouter vos clés Twitter depuis le fichier `.env`. Cliquez sur le bouton « Reveal Config Vars » et ajoutez les variables avec leurs valeurs correspondantes :

```
CONSUMER_KEYCONSUMER_SECRETACCESS_TOKENACCESS_TOKEN_SECRETSENTIMENT_KEY
```

Une fois que vous avez configuré les variables Heroku, regardez le fichier `config.js` de ce projet. Vous allez supprimer cette ligne :

```
require('dotenv').config();
```

Vous êtes maintenant prêt à déployer à nouveau sur Heroku. Vos commandes de console devraient ressembler à ceci :

```
$ git add .$ git commit -m 'add environment variables'$ git push heroku master
```

Vous pouvez ensuite vérifier les logs Heroku à nouveau avec :

```
$ heroku logs -t
```

Vous devriez maintenant avoir un bot que vous pouvez laisser faire son travail pour toujours, ou jusqu'à ce que vous décidiez de changer les critères de recherche ?

#### Déploiement Heroku via GitHub

Vous pouvez également déployer votre application en vous connectant à GitHub et en déployant automatiquement sur Heroku chaque fois que votre branche master est mise à jour sur GitHub, ce qui est assez simple.

Allez dans le tableau de bord « Deploy » sur Heroku, sélectionnez GitHub comme méthode de déploiement. Si vous avez connecté votre compte GitHub à votre compte Heroku, vous pouvez alors rechercher le dépôt. Donc, si vous avez forké ce dépôt, vous pouvez simplement entrer `twitter-bot-bootstrap` et **Rechercher**, puis cliquer sur le bouton **Connecter**. Vous pouvez ensuite déployer automatiquement depuis GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/Bg1mIVR4E7e5zkg0yXv4wvsS9qh9bIjmzRB8)

### Dépannage Heroku

Qu'est-ce que vous voulez dire par « il a planté » ?!

![Image](https://cdn-media-1.freecodecamp.org/images/9nRGo0uO4wvcKzfYV-4MdtgU7c81LOYtABlV)

D'accord, j'ai trouvé que parfois le `worker` est défini comme `web` et il plante. Essayez de reconfigurer le `worker` avec :

```
heroku ps:scale worker=0 heroku ps:scale worker=1
```

Si cela plante toujours, essayez de configurer les `Resources` sur le tableau de bord Heroku. J'ai trouvé que si vous basculez entre `web`, `heroku` et `worker`, cela se stabilise généralement. En gros, vous devez être configuré sur le `worker` Dyno, c'est ce qui cause les plantages `Error R10 (Boot timeout)` car il essaie d'utiliser une des autres ressources alors qu'il devrait utiliser le `worker` Dyno.

![Image](https://cdn-media-1.freecodecamp.org/images/AEaQ8BFU59t41L4RTsXgkCqKF1yPeyP9nWpn)

D'autres commandes Heroku utiles que j'utilise :

```
heroku restart
```

Par défaut, vous ne pouvez pousser que votre branche master si vous travaillez sur une branche de développement, par exemple, la branche `dev`. Si vous voulez tester sur Heroku, vous pouvez utiliser :

```
git push heroku dev:master
```

### Astuce pratique

Si vous souhaitez ajouter cela à votre propre dépôt GitHub et ne pas partager vos clés API ? avec le monde, vous devriez désactiver le suivi du fichier `.env`. Depuis le terminal, entrez cette commande git :

```
$ git update-index --assume-unchanged .env
```

J'ai ajouté mes commandes git les plus utilisées dans ce [gist](https://gist.github.com/spences10/5c492e197e95158809a83650ff97fc3a)

### Conclusion

Votre bot Twitter devrait maintenant être en ligne. Vous pouvez le modifier et le configurer davantage.

Voici mon [dépôt](https://github.com/spences10/twitter-bot-bootstrap) si vous souhaitez le forker et contribuer en utilisant des pull requests. Toutes les contributions, grandes ou petites — fonctionnalités majeures, corrections de bugs, tests d'intégration — sont les bienvenues, mais seront soigneusement examinées et discutées.

### Remerciements

Le crédit pour l'inspiration de cet article revient à [@amanhimself](https://twitter.com/amanhimself) et ses publications sur la création de votre propre bot Twitter.

[create-a-simple-twitter-bot-with-node-js](https://hackernoon.com/create-a-simple-twitter-bot-with-node-js-5b14eb006c08#.flysreo60)

[how-to-make-a-twitter-bot-with-nodejs](https://chatbotslife.com/how-to-make-a-twitter-bot-with-nodejs-d5cb04fdbf97#.h5ah8dq5n)

[twitter-mctwitbot](https://medium.com/@spences10/twitter-mctwitbot-4d15cd005dc0#.dp9q5f427)

[awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots)

D'autres articles détaillant des bots Twitter utiles.

[www.brit.co/twitter-bots-to-follow](http://www.brit.co/twitter-bots-to-follow/)

[www.hongkiat.com/using-twitter-bots](http://www.hongkiat.com/blog/using-twitter-bots/)

Vous avez lu jusqu'ici ? Wow, merci d'avoir lu ! Si vous avez aimé cet article, n'oubliez pas de le recommander en cliquant sur le bouton 496 à côté, et en le partageant avec vos amis sur les réseaux sociaux.

Si vous voulez en savoir plus sur moi, visitez mon [blog](http://spences10.github.io), mon [Github](https://github.com/spences10), ou tweetez-moi [@ScottDevTweets](https://twitter.com/ScottDevTweets).

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).