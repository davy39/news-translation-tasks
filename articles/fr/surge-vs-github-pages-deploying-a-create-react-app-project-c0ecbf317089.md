---
title: 'Surge VS GitHub Pages: Comment déployer un projet create-react-app'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-11T16:45:30.000Z'
originalURL: https://freecodecamp.org/news/surge-vs-github-pages-deploying-a-create-react-app-project-c0ecbf317089
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hCctQRV_ZZl-2Kc2eLQ0zA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Surge VS GitHub Pages: Comment déployer un projet create-react-app'
seo_desc: 'By Jake Wiesler

  As a developer, there are several ways you can show off your skills to peers and
  prospective employers. Open source contributions are great. Blogging is great. But
  at some point you’ll want to get projects up on the web, where people ...'
---

Par Jake Wiesler

En tant que développeur, il existe plusieurs façons de montrer vos compétences à vos pairs et à vos employeurs potentiels. Les contributions open source sont géniales. Le blogging est génial. Mais à un moment donné, vous voudrez mettre des projets en ligne, où les gens peuvent réellement les utiliser.

Trop de fois, j'ai commencé quelque chose localement et ne l'ai jamais mené à terme. Vous avez peut-être fait de même. Une raison pour laquelle cela est si courant est à cause de tout le travail supplémentaire que nécessite le déploiement.

Ne serait-il pas agréable d'avoir un hub central où tous vos projets vivent sans vous soucier de l'hébergement et de la configuration du serveur ? Cet article vous guidera à travers deux outils de déploiement populaires qui nécessitent un minimum d'effort.

![Image](https://cdn-media-1.freecodecamp.org/images/tfRodzkgaOVM9HEExezIOQS1L4uUOp9102Gb)
_Soyez la tortue._

### create-react-app

Avant de commencer, laissez-moi vous parler de mon nouveau meilleur ami, `create-react-app`. Si vous avez pensé à apprendre React — mais que vous êtes découragé par le temps nécessaire pour lancer un projet — cet [outil de ligne de commande (CLI)](https://github.com/facebookincubator/create-react-app) est votre grâce salvatrice. Il prendra en charge la plupart du code boilerplate dont vous avez besoin pour démarrer un projet.

Pour l'installer et créer votre premier projet, allez dans votre terminal et exécutez ces commandes :

```
npm install -g create-react-app 
```

```
create-react-app <nom-de-votre-projet>
```

```
cd <nom-de-votre-projet>
```

Dès sa sortie, `create-react-app` vient avec quelques scripts pratiques qui vous permettent de développer votre projet localement et de le déployer ensuite. Ils peuvent être trouvés dans le fichier `package.json` à la racine de votre répertoire de projet.

Utilisez `npm start` pour exécuter votre projet localement pendant que vous le développez. Ensuite, utilisez `npm run build` pour préparer votre projet pour le déploiement.

### Surge.sh et GitHub Pages

Avancez rapidement un peu. Vous avez construit une application de base et êtes prêt à la déployer sur le web.

Il existe de nombreuses options dans le domaine des plateformes d'hébergement de sites statiques, mais les deux avec lesquelles nous allons travailler sont [Surge.sh](https://surge.sh/) et [GitHub Pages](https://pages.github.com/).

Ces deux plateformes sont puissantes à leur manière. Celle que vous utilisez dépend de votre situation. Mon objectif est de vous donner une meilleure compréhension de l'existence de ces outils et de ce que vous pouvez faire avec eux.

Notez également que même si cet article parle de la publication de projets créés avec le CLI `create-react-app`, Surge et GitHub Pages fonctionneront même avec les projets les plus basiques. Vous pourrez peut-être sauter certaines de ces étapes si vous n'utilisez pas React lui-même.

### Surge.sh

Surge est un logiciel vraiment génial que j'ai récemment découvert grâce à un fil de discussion sur Reddit. Au cœur de Surge se trouve un CLI qui vous permet de déployer vos projets gratuitement. Et rapidement aussi. Ce qui fait vraiment ressortir Surge, c'est sa simplicité.

Parcourons un exemple simple en utilisant `create-react-app`.

Tout d'abord, installez le package `surge` globalement :

```
npm install -g surge 
```

Maintenant que Surge est installé sur votre machine, vous devez préparer votre projet pour le déploiement. J'ai mentionné ci-dessus que `create-react-app` dispose d'un script dans `package.json` appelé `build`. Ce script prépare essentiellement l'application pour la production en regroupant et en optimisant tout le code.

Exécutez `npm run build` à la racine de votre projet :

```
npm run build
```

Vous devriez remarquer qu'un nouveau dossier a été créé à la racine de votre répertoire de projet appelé `build`. Ce dossier contient l'application prête pour la production.

Excellent, vous avez presque terminé. Il ne reste plus qu'à exécuter la commande `surge` à la racine de votre projet :

```
surge
```

Si c'est la première fois que vous exécutez `surge`, vous serez invité à créer un compte. Ajoutez un email et un mot de passe, puis appuyez sur Entrée. Vous verrez alors une sortie similaire à celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/h0vdYcH66bzM4-kdGXo0baicormFe9SUTweQ)

Pour déployer votre projet, Surge n'a besoin que de deux choses de votre part :

1. Le chemin vers le projet
2. Le domaine pour l'héberger

#### Chemin du projet

Vous remarquerez que le champ _chemin du projet_ dans le terminal est par défaut le répertoire racine. Surge suppose que le répertoire dans lequel vous exécutez la commande `surge` est le répertoire que vous souhaitez déployer. Dans votre cas, vous devez indiquer à Surge le répertoire `build` créé lorsque vous avez exécuté `npm run build`.

Si votre chemin de projet est `path/to/my-project`, modifiez-le en `path/to/my-project/build`. Une fois que vous avez fait cette modification, appuyez sur Entrée pour confirmer.

![Image](https://cdn-media-1.freecodecamp.org/images/s-I7bAtExcfNprnJifQCtX1s4QBpyjkbUJTP)

#### Domaine

Après avoir saisi le chemin du projet, Surge suggérera un domaine aléatoire à utiliser. Vous pouvez le supprimer et ajouter votre propre domaine si vous le souhaitez. Il doit simplement avoir l'extension `.surge.sh` à la fin. L'outil permet également les [domaines personnalisés](https://surge.sh/help/adding-a-custom-domain), ce qui est vraiment génial.

Acceptez le domaine suggéré ou ajoutez le vôtre (personnalisé ou aléatoire avec la bonne extension surge), puis appuyez sur Entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/Qol-myCxpcLsFKeu3Ef4hcd3NzK9QIJbrRUc)

C'est tout ! Naviguez vers le domaine dans votre navigateur et vous devriez voir votre projet en cours d'exécution.

Notez que si votre application utilise le **routing côté client**, Surge recommande de renommer le fichier `index.html` dans votre répertoire `build` en `200.html` avant d'exécuter la commande `surge`. Vous pouvez trouver plus d'informations dans la [documentation](https://surge.sh/help/adding-a-200-page-for-client-side-routing) de Surge.

### GitHub Pages

GitHub Pages facilite la transformation des dépôts GitHub en sites web statiques complets. De nombreuses organisations utilisent ce service pour héberger leur documentation et leurs démonstrations de projets, mais vous pouvez l'utiliser pour ce que vous voulez.

Notez que pour que cela fonctionne, vous devez d'abord pousser le code vers un dépôt sur GitHub. Si cela vous semble étranger, consultez la documentation supplémentaire [ici](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

Si vous avez déjà exécuté `npm run build` en utilisant `create-react-app` auparavant, vous avez peut-être remarqué une sortie qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/pPUrTPAMPSRXJSy00LfWnzoRrCriMJlZunbf)
_sortie initiale après avoir exécuté `npm run build`_

`create-react-app` vient avec une documentation détaillée pour aider les utilisateurs à publier leur travail en utilisant toutes sortes d'outils. Ici, vous pouvez voir la sortie du terminal en temps réel nous instruisant sur la façon de le faire via GitHub Pages. Essayons-le.

#### Étape 1

Modifiez `package.json` en ajoutant un nouveau champ nommé `homepage:`

```
"homepage": "https://<nom-utilisateur-github>.github.io/<dépôt-projet>"
```

Si votre nom d'utilisateur GitHub est `george-lucas`, et que le dépôt GitHub de votre projet est `SithJS`, la valeur du champ `homepage` doit être `"https://george-lucas.github.io/SithJS"`.

Exécutons à nouveau `npm run build` après la modification :

![Image](https://cdn-media-1.freecodecamp.org/images/gGsMWtxELueH9A9yjIfHyU0CfEUEffhjZSwy)
_nouvelle sortie après avoir ajouté un champ `homepage` dans `package.json`_

Avez-vous remarqué la nouvelle sortie ci-dessus ? Le CLI `create-react-app` nous guide à travers tout le processus. Plutôt élégant.

#### Étape 2

Ensuite, vous devez installer le plugin `gh-pages`. Cela nous permettra de publier sur la branche `gh-pages` sur GitHub directement depuis le terminal :

```
npm install --save-dev gh-pages
```

`gh-pages` est une branche spéciale que GitHub Pages utilise pour publier des projets. La belle chose à propos de celle-ci est que la branche vit dans le même dépôt que le code de votre projet, mais n'affecte pas le projet lui-même.

Notez que si vous avez déjà une branche `gh-pages` dans le dépôt de votre projet, elle mettra à jour la branche en conséquence. Si la branche n'existe pas, elle la créera à la volée.

#### Étape 3

Ajoutez un nouveau script au champ `scripts` à l'intérieur de `package.json`. Appelons le script `deploy` :

```
"deploy" : "npm run build&&gh-pages -d build"
```

Et enfin, exécutons-le :

```
npm run deploy
```

![Image](https://cdn-media-1.freecodecamp.org/images/CNm53LXP-1E6LV7fl5PqiQqmt78IXryDcnrL)

`npm run deploy` construira d'abord votre projet via `npm run build`. Ensuite, il le publiera sur une branche `gh-pages` sur GitHub via `gh-pages -d build`.

#### Étape 4

Nous avons presque terminé. Rendez-vous dans les paramètres du dépôt de votre projet sur GitHub. Dans la section **GitHub Pages**, confirmez que votre projet est configuré pour utiliser la branche `gh-pages`.

![Image](https://cdn-media-1.freecodecamp.org/images/-d7-rHeLpbrp8xPZ868uvkYNEZan2gt5t8dt)
_Un exemple de ma liste de tâches React utilisant la branche gh-pages_

Vous pouvez maintenant naviguer vers l'URL que vous avez entrée dans le champ `homepage` de votre fichier `package.json`, où vous verrez que votre projet a été déployé !

![Image](https://cdn-media-1.freecodecamp.org/images/vn-Nm8yFDXfuEc3ecaY-e4EGgCsXSWya5H1C)

Notez que — comme avec Surge — GitHub Pages a également des problèmes avec le routage côté client. `create-react-app` liste quelques solutions dans la [documentation](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#notes-on-client-side-routing) pour l'intégration de GitHub Pages.

### Le gagnant

En toute honnêteté, vous ne pouvez pas vous tromper avec l'une ou l'autre de ces options. Elles sont toutes les deux géniales. Récapitulons quelques caractéristiques clés de chacune :

#### **Surge**

* Configuration minimale pour déployer un projet
* Ne fait aucune hypothèse sur la technologie utilisée
* Intégration transparente avec des outils de construction tels que Grunt et Gulp
* Peut être utilisé comme une dépendance de développement lors de la construction de vos propres outils

#### GitHub Pages

* Garde le code du projet et la ou les pages web hébergées dans un seul dépôt
* Centralise tous les projets sous votre domaine _<nom-utilisateur>.github.io_
* Déployez depuis la ligne de commande ou depuis les paramètres de votre dépôt sur GitHub
* Fonctionne très bien avec des générateurs de sites statiques comme Jekyll

Personnellement, j'ai choisi GitHub Pages pour mon projet le plus récent parce que j'utilise déjà GitHub au quotidien et que j'aime garder tout centralisé. Peut-être est-ce mon TOC qui parle, mais j'adore avoir des dépôts GitHub individuels pour les projets que je peux déployer en tant que sous-domaine de `jake-wies.github.io`.

Si vous créez simplement un projet de test, ou si vous voulez montrer une démonstration à un client, utiliser le CLI super-rapide de Surge pour générer une page web est difficile à refuser. Vous pouvez générer le domaine rapidement et le supprimer ensuite.

À la fin de la journée, le meilleur outil pour le travail est celui qui vous rend productif. Les informations que j'ai fournies devraient vous donner une bonne compréhension de là où chacun excelle. Auditez les besoins de votre projet et choisissez celui qui vous convient.

_Merci d'avoir lu ! Je suis un développeur autodidacte et je passe la plupart de mon temps libre à plonger dans les outils front-end et à [écrire](https://www.jakewiesler.com/). Contactez-moi sur [Twitter](https://twitter.com/jakewies) si vous avez des questions !_