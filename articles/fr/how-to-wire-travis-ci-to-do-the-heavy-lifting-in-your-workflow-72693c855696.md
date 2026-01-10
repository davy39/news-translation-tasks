---
title: Comment utiliser Travis CI et GitHub pour automatiser votre flux de travail
  de développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-27T19:11:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-wire-travis-ci-to-do-the-heavy-lifting-in-your-workflow-72693c855696
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KuG9pmpZOl03m_EM9eAQCw.jpeg
tags:
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Travis CI et GitHub pour automatiser votre flux de travail
  de développement web
seo_desc: 'By Vijayabharathi Balasubramanian

  It’s common to hack together apps on CodePen when you are starting out. But there
  will be a time when you will want to publish your own web apps to the whole world.
  They could be side projects or projects for a clien...'
---

Par Vijayabharathi Balasubramanian

Il est courant de bricoler des applications sur [CodePen](https://codepen.io/) lorsque vous débutez. Mais il arrivera un moment où vous voudrez publier vos propres applications web pour le monde entier. Cela pourrait être des projets secondaires ou des projets pour un client. Un bon flux de travail de développement fera toute la différence à ce moment-là.

Nous allons configurer un flux de travail de développement en utilisant les outils suivants :

* create-react-app
* scripts npm
* Travis-CI

Nous allons connecter Travis CI et GitHub ensemble. À la fin, nous obtiendrons un joli badge brillant comme celui ci-dessous.

Mais plus que l'apparence, le badge signifie une fonction. C'est un signe que Travis CI teste, construit et publie nos commits sur GitHub. Travis CI ne publie que si les tests passent.

Préparez-vous à placer ces badges sur votre dépôt :

![Image](https://cdn-media-1.freecodecamp.org/images/0OKbYVdWQeqFIG3PGgeAT-xXvZyhfVQFhsQc)

J'ai organisé tout le flux de travail en étapes. Une session devrait suffire pour chaque étape. Cela prend environ 50 minutes.

### Étape 1 : Exécuter create-react-app localement

#### Préparez votre dépôt git

La première chose à faire est de créer un nouveau dépôt sur [GitHub](https://github.com/). Si vous n'avez pas encore de compte, c'est le moment de vous inscrire. Les dépôts publics sont gratuits. Lorsque vous créez un nouveau dépôt, GitHub vous permet de créer des fichiers pour `.gitignore`, `license` et `README.md`.

Si vous débutez avec Git, vous pouvez lire ce livre [gratuit](https://git-scm.com/book/en/v2) en ligne. Il y a aussi une section [d'aide](https://help.github.com/) sur GitHub.

Voici à quoi ressemblera notre nouveau dépôt :

![Image](https://cdn-media-1.freecodecamp.org/images/b-nypK9R614MkibgvmEpSx0hXhnQqz5eXSws)

Très bien, mettons cela sur notre terminal. Voyez-vous ce bouton vert brillant sur l'image ci-dessus montrant **Clone or download**. Cela nous donnera l'URL du dépôt. Sur votre terminal, exécutez cette commande :

```
git clone git@github.com:pineboat/react-continuous-deployment.git
```

Cette commande téléchargera le contenu du dépôt dans un nouveau répertoire. Il nomme le répertoire de la même manière que le dépôt. Dans notre cas, le nom du répertoire sera **react-continuous-deployment**.

Si vous voulez vous assurer qu'un lien vers le dépôt original est prêt, utilisez la commande :

`git remote -v`

Maintenant que nous sommes prêts à pousser nos changements vers GitHub, lançons React.

#### Démarrer avec `create-react-app`

Démarrer un nouveau projet React à partir de zéro peut prendre plus de temps que prévu. Surtout lorsque vous n'utilisez aucun échafaudage prédéfini. Il existe plusieurs solutions que nous pouvons utiliser pour commencer. J'ai choisi [Create React App](https://github.com/facebookincubator/create-react-app) officiel parce que je l'ai essayé en premier et que je suis resté avec. Lorsque vous n'avez pas à micro-gérer vos configurations, cela vous donne un bon départ pour que vous puissiez commencer à coder.

Comme le montre le fichier `README.md` du dépôt, vous n'avez qu'à l'installer une fois globalement. Ensuite, vous pouvez l'utiliser pour échafauder autant de projets que vous le souhaitez.

Pour l'installer, tapez :

```
npm install -g create-react-app
```

Une fois installé, vous pouvez l'exécuter à partir de n'importe quel répertoire pour créer une nouvelle application. Donnons-lui le nom de notre dépôt :

```
create-react-app react-continuous-deployment
```

Cela ne créera **pas** de nouveau dossier car nous avons déjà le dossier créé par Git. Au lieu de cela, il commencera à installer les `node_modules` nécessaires et à échafauder les scripts dans le dossier existant.

Si vous voulez une nouvelle application, vous pouvez utiliser :

`create-react-app fancy-app-name`

Ensuite, vous devrez créer un dépôt Git et le connecter à GitHub. Ce n'est pas trop difficile. Vous pouvez utiliser cette page [d'aide](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) de GitHub.

L'installation est-elle terminée ? Cela ne devrait pas prendre plus de 5 minutes. Cela m'a pris environ 15 minutes. Ne vous laissez pas effrayer par cela. À moins que vous ne soyez comme moi, et que vous utilisiez une carte de données 4G de 150 mb/s qui vous donne environ 512 kbps de vitesse de téléchargement dans sa meilleure journée.

La bonne chose est que l'installation a déplacé notre ancien fichier `README.md`. Le terminal montre ce message :

```
You had a `README.md` file, we renamed it to `README.old.md`
```

Le terminal devrait également vous avoir montré l'énorme liste de packages dans une structure arborescente. Cela peut sembler effrayant. Mais la plupart de ces packages sont des dépendances entre eux. Ils sont là pour vous aider à développer votre application. Le produit final ne contiendra que les fichiers JavaScript nécessaires tels que `react.js` et `react-dom.js`. Nous y viendrons dans un moment.

Pour l'instant, réveillons notre application. Une fois l'installation terminée, `create-react-app` nous donnera une liste de commandes qui seront utiles.

Voici un catalogue pour référence :

* `npm start`  
Démarre le serveur de développement
* `npm run build`  
Regroupe l'application en fichiers statiques pour la production
* `npm test`   
Démarre le test runner
* `npm run eject`   
Supprime la dépendance unique de build de votre projet Voir [ici](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#npm-run-eject)
* `npm run deploy`   
Pour déployer la build sur la branche gh-pages

Les commandes intégrées de nœud `npm start` et `npm test` sont reconnues par défaut. Vous devez exécuter d'autres scripts tels que build, eject et deploy en utilisant un drapeau run supplémentaire :   
`npm run script_name`

Nous en ajouterons quelques-uns de plus au fur et à mesure. Maintenant, il est temps de charger notre site sur un navigateur. Entrez dans le répertoire de l'application et exécutez :

```
npm start
```

Comme par magie, un nouvel onglet de navigateur s'ouvre et vous voyez une belle roue React tourner. La vue doit vous défier de construire la prochaine meilleure application que l'internet est sur le point de voir.

Voici ce que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/sUEp8EOb2VUO72SH2iNiaj3-utJkqX3uUwyv)

C'est un GIF (Graphics Interchange Format) assez soigné, n'est-ce pas ? Sauf pour mon curseur qui apparaît. J'ai capturé ce GIF avec un outil appelé [Peek.](https://github.com/phw/peek) Consultez-le lorsque vous en avez besoin.

Bien joué ! J'espère que cela n'a pas pris plus de 45 minutes. Si vous rencontrez des problèmes, faites attention aux messages d'erreur et essayez de les corriger.

Lorsque vous êtes proche du point de frustration, rendez-vous sur [Stack Overflow](https://stackoverflow.com/) pour obtenir de l'aide. Ou laissez vos questions dans les commentaires ci-dessous.

Avant de modifier l'un des fichiers, engageons le code et poussons-le vers le dépôt GitHub. Ces commandes feront l'affaire :

```
git status git add --all git commit -m "Initial Scaffold, this is your own message"
```

* `git status`   
Affiche une liste des changements que nous avons effectués
* `git add`   
Ajoute ces changements à un endroit temporaire appelé `stage` avant de les pousser dans le cloud

Si vous exécutez à nouveau `git status`, il indiquera que

```
Your branch is ahead of 'origin/master' by 1 commit. (use "git push" to publish your local commits) nothing to commit, working directory clean
```

C'est exact, nous avons effectué et engagé des changements localement. Il n'y a pas de changements non engagés. Mais nous sommes en avance sur la version cloud de notre dépôt. Il est temps de les publier dans un endroit sûr, qui est GitHub.

Tout ce que vous devez exécuter est :  
`git push origin master`

Vous obtiendrez un joli rapport montrant un hash comme `fb74259..045ec7a`, qui est une référence pour notre commit. Bien sûr, votre hash sera différent.

Vérifiez votre dépôt GitHub. Êtes-vous surpris de voir un long `README.md` ? Souvenez-vous que `create-react-app` a remplacé notre petit `README.md` par le sien. Il est énorme et utile, alors nous allons le garder pour l'instant avant d'écrire le nôtre.

### Étape 2 : Transférer le site sur GitHub Pages

#### Construire le site statique

Jetons un coup d'œil à la construction finale.

Vous n'avez qu'à exécuter :

`npm run build`

Assurez-vous d'être dans le répertoire de l'application pour toutes les commandes. Nous obtiendrons ce joli texte nous montrant ce qui s'est passé et ce que nous pouvons faire d'autre :

```
$ npm run build > react-continuous-deployment@0.1.0 build /home/weebee/Projects/blog_projects/react-continuous-deployment> react-scripts buildCreating an optimized production build...Compiled successfully.File sizes after gzip:  48.12 KB  build/static/js/main.9fdf0e48.js  288 B     build/static/css/main.cacbacc7.cssThe project was built assuming it is hosted at the server root.To override this, specify the homepage in your package.json.For example, add this to build it for GitHub Pages:  "homepage" : "http://myname.github.io/myapp",The build folder is ready to be deployed.You may serve it with a static server:  npm install -g serve  serve -s build
```

La commande `npm run build` fait ce que nous avons demandé. Elle construit notre application, optimise et [minifie](https://en.wikipedia.org/wiki/Minification_(programming)) nos actifs. Et elle place tout dans un dossier appelé **build**.

Vers le bas, la suggestion est d'installer le package npm `serve` pour démarrer un serveur local. La plupart du temps, si vous êtes sous Linux, vous aurez déjà Python installé. Il est assez facile de démarrer un serveur local si vous avez Python.

Entrez dans le répertoire `**build**` et démarrez un serveur, voir les commandes suivantes :

```
cd buildpython -m SimpleHTTPServer
```

La commande Python démarre par défaut le serveur sur le port 8000. Donc, `http://localhost:8000` servira la version de production du site web. Il utilise les actifs de votre répertoire local **build** que nous venons de créer.

Si cela a l'air bien, nous allons l'envoyer sur GitHub pages.

#### Introduction à GitHub pages

GitHub pages est une solution d'hébergement fournie par GitHub pour les dépôts. Il y a quelques endroits où vous pouvez héberger votre site, tous dans un dépôt :

* Vous pouvez utiliser la branche **master** (celle par défaut) pour héberger votre site web  
Si vous avez un `index.html`, il s'affichera. Sinon, votre `README.md` s'affichera.
* Vous pouvez également utiliser le dossier **docs** dans une branche master pour héberger votre site  
Le cas d'utilisation serait lorsque vous avez un logiciel ou une bibliothèque développé sur GitHub. Vous pourriez vouloir héberger la documentation dans le même dépôt.
* Vous pouvez utiliser la branche **gh-pages** pour héberger votre site

Il y a une exception. Le nom de votre dépôt ne doit pas être `<your_user_name>.git`hub.`io ou <orgname&g`t;.github.io

Ce sont des noms spéciaux et ils vous limitent à l'utilisation de la branche **master**.

Une fois que vous avez hébergé votre site web, vous pouvez le charger dans les URL suivantes. Cela dépend du fait que votre dépôt soit sous votre compte ou un compte d'organisation :

```
https://<your_user_name>.github.io/<your_repository_name>/ 
```

```
https://<organization_name>.github.io/<your_repository_name>/
```

Avec cette compréhension, équipons notre dépôt pour qu'il soit en ligne.

#### Publier sur GitHub pages

Le nouveau `README.md` qui nous a été donné par `create-react-app` a une section séparée sur GitHub pages. Il y a quelques choses que nous devons faire.

#### **Vérifier les ajouts au fichier `package.json`**

```
"homepage": "http://<user_name>.github.io/<your_repository_name", "scripts": { "predeploy": "npm run build", "deploy": "gh-pages -d build"}
```

**Note** : Habituellement, la dernière section ou entrée dans un JSON n'a pas besoin de virgule, toutes les autres doivent en avoir une.

#### Installer le package gh-pages

Cela est facile. Il suffit d'exécuter la commande suivante lorsque vous êtes dans le répertoire du projet :

`npm install --save gh-pages`

Le drapeau `--save` ajoutera `gh-pages` comme une dépendance à `package.json`. Cela garantit que toute autre personne qui clone votre projet peut également l'obtenir lorsqu'elle exécute `npm install`.

Voici un instantané de la commande `git diff` montrant tout ce que nous avons ajouté depuis la création de `package.json`.

![Image](https://cdn-media-1.freecodecamp.org/images/zhiLdMIfyW2ecDys15MdpTwOLdJPN9Y1kXBJ)

#### Déployer sur la branche gh-pages

Exécutons `npm run deploy`. Il exécutera automatiquement `predeploy`, pour générer la build de production que nous avons vue précédemment. Il déployera ensuite la build dans notre dépôt sous une nouvelle branche nommée **gh-pages**.

Vérifiez si vous obtenez un statut `Published` comme dernière déclaration. Si c'est le cas, vous avez déployé avec succès la build de production sur GitHub. Voici la sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/tG4iWR7jDJbMuVMzVpWNSnEESUNDVuHr7XsI)

#### Sélectionner la branche gh-pages à publier

Rendons-nous sur le dépôt GitHub et publions notre site. Ouvrez le dépôt et allez dans l'onglet des paramètres en haut. Cela ressemble à l'image ci-dessous, attendez une minute ! GitHub a automatiquement publié la branche **gh-pages**. Il n'y a rien de plus à faire. Il montre également l'URL à laquelle nous pouvons accéder au site.

Le sous-titre ci-dessus devrait en fait dire **Ne rien faire**. Tout est fait et prêt à être utilisé.

![Image](https://cdn-media-1.freecodecamp.org/images/gbqqTF9QNBdmD1iyzhkiLvA12ntRAD3dXh0f)

**Note** : L'URL affichée pour mon dépôt peut vous induire en erreur. C'est parce que j'ai créé ce dépôt sous une organisation nommée PineBoat, qui est mon blog. GitHub place cela sous mon domaine personnalisé, ce que je n'attendais pas lorsque j'ai essayé cela. Le vôtre sera différent.

Jusqu'à présent, tout va bien. Si vous avez déjà de l'expérience avec Git et les packages Node, vous n'auriez pas dû avoir de problème pour arriver jusqu'ici. En fait, le `README.md` par défaut était suffisant pour m'aider jusqu'ici. Si vous n'avez pas d'expérience, j'espère que vous avez apprécié le voyage.

Mais nous aspirons à un flux de travail de déploiement continu. Nous commençons à naviguer dans des eaux inexplorées. Certains pourraient dire que rien n'est inexploré sur Internet. Je serais d'accord, mais je créerais quand même ma propre carte.

### Étape 3 : Déploiement continu

C'est ici que nous faisons appel à des bots pour effectuer la plupart du déploiement que nous avons fait dans l'étape 2.

#### Intégrer Travis CI pour une construction automatique

Faisons en sorte que Travis CI effectue le déploiement pour nous. Il n'y a aucun mal à construire et déployer votre site vous-même. Comme nous l'avons vu, cela ne prend que quelques minutes de notre temps précieux.

Cependant, lorsque vous travaillez sur des projets plus importants, il est préférable de laisser des bots de confiance effectuer certaines des tâches. Travis CI est un tel service.

Nous pouvons tirer parti de Travis CI pour construire et déployer chaque fois que nous validons notre code dans le dépôt.

#### Inscription à Travis CI

Il serait ennuyeux si je commençais par « si vous avez un compte GitHub » maintenant. Je suis sûr que vous en avez un maintenant et nous pouvons l'utiliser pour nous inscrire à Travis CI.

#### Connexion au dépôt GitHub

Faites attention aux permissions. Si votre dépôt ne s'affiche pas, cliquez sur le bouton **sync** et actualisez la page. J'ai dû accorder la permission à l'organisation « PineBoat » avant de pouvoir voir le dépôt.

Travis CI vous montre les étapes. Activez ce commutateur contre votre dépôt pour le connecter.

Cliquez sur le nom du dépôt pour l'ouvrir. Il affichera un statut de construction comme **inconnu** et une note plus grande disant **Aucune construction pour ce dépôt**.

![Image](https://cdn-media-1.freecodecamp.org/images/VRqkHvHEBLL5KY2SUDCUZ534Cxoc8Hvfujyi)

Pas pour longtemps. Changeons cela.

#### Ajouter `.travis.yml` au dépôt

Voici le `.travis.yml` qui doit être ajouté. Jetez un coup d'œil, et restez avec moi pendant que je clarifie certaines des questions que vous pourriez avoir.

```
language: node_js
```

```
node_js: - "node"
```

```
after_success: - git config --global user.name "vijayabharathi" - git config --global user.email "[email protected]" - git remote rm origin - git remote add origin https://vijayabharathib:${GH_TOKEN}@github.com/pineboat/react-continuous-deployment.git - npm run deploy
```

Soyez prudent avec `git remote add origin`, c'est une longue ligne. La syntaxe `YAML` est légèrement différente de `JSON`. [Cette page](http://docs.ansible.com/ansible/latest/YAMLSyntax.html) pourrait aider. Maintenant, il est temps de le décomposer. Vous avez peut-être compris la plupart de ces messages.

**Voici en anglais simple :**

* Il s'agit d'un projet node. Obtenez la dernière version de node
* Puisque Travis exécute `npm test` par défaut, nous lui demandons de faire des choses après que le test soit réussi
* Ajoutez votre nom d'utilisateur Git et votre email
* Ensuite, ajoutez `git remote origin` pour le dépôt  
Utilisez votre nom d'utilisateur et le GH_TOKEN généré comme identifiants
* Enfin, exécutez la commande `npm run deploy`  
Si vous vous souvenez, cela exécutera `npm run predeploy` avant d'exécuter `npm run deploy`

#### Valider et regarder Travis CI construire

Gardez votre page de dépôt Travis CI ouverte. Sur votre terminal, ajoutez les changements, validez et poussez-les vers GitHub.

Au cas où vous auriez besoin d'un rappel, voici la liste des commandes :

```
git add --all git commit -m "add .travis.yml configuration for automatic build" git push origin master
```

Si vous basculez vers la page Travis CI, vous verrez la page s'animer une fois que `git push` est terminé ou dans quelques secondes. La construction commence automatiquement et vous saurez si elle est réussie.

Voici ma page Travis CI montrant un joli statut vert.

![Image](https://cdn-media-1.freecodecamp.org/images/IczxuHQPRW8kvJPJza0WYmij24QUcTkf-tfr)

Le journal affiché n'est pas moins de 2500 lignes. Je suis content que Travis-CI ne montre que ce dont nous avons besoin.

Une indication claire des étapes suivies comme montré ci-dessous dans l'image :

![Image](https://cdn-media-1.freecodecamp.org/images/XUh1uyAQUpPSni0UyPkrPDbUoFP8ZKOsCIyi)

### Vérification ponctuelle, avons-nous vraiment réussi ?

C'est ici que les tests automatisés qui s'exécutent en production peuvent être utiles.

Mais ce sera pour un autre jour. Le [Selenium WebDriver](http://www.seleniumhq.org/projects/webdriver/) peut attendre jusqu'à ce que nous terminions ce câblage. Vérifions manuellement si Travis CI a vraiment publié sur GitHub pages.

#### Un autre essai, cette fois avec des changements de code

La dernière fois, nous n'avons pas pu voir de différence dans notre application après le déploiement. C'est parce que nous n'en avons pas fait. Il n'y avait donc aucun moyen de savoir si la construction avait réussi. Vous pouvez charger la branche gh-pages et regarder les commits, mais je m'égare.

Maintenant, faisons quelques petits changements. Il est temps de faire revenir la roue React dans le temps.

Nous ne ferons que deux changements.

Dans le fichier `src/App.css`, il y a une section pour l'animation nommée `@keyframes App-logo-spin`. Changez ce `360deg` en `-360deg`. Cela fait tourner la roue dans le sens inverse des aiguilles d'une montre.

Chargez le fichier `src/logo.svg` et changez la couleur de remplissage de `#61DAFB` à `#DA61FB`. Si votre serveur s'exécute via `npm start`, vous pouvez déjà voir une roue violette tourner dans le sens inverse des aiguilles d'une montre. Sinon, ajoutez les changements à la réserve, validez et poussez-les vers le dépôt. Regardez si la construction est réussie dans Travis-CI puis rendez-vous sur votre page GitHub.

Chargez `your_user_name.github.io/repository_name`. Vous devriez voir la roue violette au lieu de la bleue.

Hélas, je ne vois pas cette roue violette. Je vois toujours la bleue par défaut.

#### Corriger le GH_TOKEN manquant

Bien que Travis CI ait signalé que tout allait bien, ce n'est pas le cas. Si vous ouvrez la branche **gh-pages**, vous verrez le commit original que nous avons fait à partir du terminal local. Aucun autre commit. Cela signifie que les commandes `after_success` n'ont pas été si réussies.

Si vous développez la section `npm run deploy` dans le journal de construction de Travis, vous verrez des **erreurs d'authentification**. C'est parce que nous n'avons pas donné à Travis CI la permission d'écrire dans notre dépôt.

Vous pouvez créer un nouveau jeton à partir de la page [Personal access tokens](https://github.com/settings/tokens) de GitHub.com. N'oubliez pas de donner accès au dépôt public seul. Une seule coche contre `public_repo` suffira. **Ne manquez pas cela.** Une fois que vous avez généré un jeton, copiez-le. GitHub vous avertit à juste titre que vous ne pourrez plus le voir.

Rendez-vous sur Travis CI, cliquez sur **More Options** pour votre dépôt et choisissez **settings**. Il affichera plusieurs sections, mais **Environment Variables** est celle à rechercher.

Nommez le jeton `GH_TOKEN` et collez le jeton sous le champ de valeur. Cliquez sur ajouter. **N'**activez **pas** l'option **Display value in logs** car elle pourrait être visible par les personnes si vous envoyez les journaux. Le jeton est équivalent à votre mot de passe.

C'est tout, maintenant Travis-CI peut écrire dans notre dépôt.

Retournez à l'onglet **Current** du dépôt et cliquez sur **Restart build**. Une fois la construction terminée, vous pouvez vérifier les journaux et vérifier la branche **gh-pages** sur GitHub. Vous devriez voir un nouveau commit.

Félicitations ! C'est notre premier déploiement automatisé. Et le site `github.io` lui-même ? Aucune quantité de rafraîchissement ne ferait apparaître la roue violette tant attendue. Ne perdez pas espoir pour l'instant.

#### Demander au service worker de faire une pause

La roue saigne toujours en bleu. Mais la branche **gh-pages** dans le dépôt montre un deuxième commit. Comparons le `index.html` sur le dépôt et sur la source de la page web. Ils pointent vers différents fichiers CSS et JavaScript. Le suffixe de hachage est notre indice.

Cela semble être le résultat d'un service worker JavaScript énergique. Il a mis en cache la page pour une utilisation hors ligne. Mais cette conclusion nécessite plus de recherches. En attendant, arrêtons simplement le service worker et effaçons le stockage.

Si vous êtes sur Chrome, **Developer Tools** peut être accessible depuis le menu ou en appuyant sur `F12`. L'onglet **Application** dans Chrome DevTools a une section **Clear Storage**. Cochez toutes les entrées et cliquez enfin sur **Clear site data**.

Rafraîchissez et boom ! Voici notre roue inversée en violet vif. Maintenant, c'est le moment de célébrer.

![Image](https://cdn-media-1.freecodecamp.org/images/h2r8cWq2PGEZppd9LJX6gzGDIWqOCfoi1ad5)

**Note** : il doit y avoir un meilleur moyen de faire ce nettoyage de stockage automatiquement. Ce serait une douleur si nous devons arrêter et nettoyer le service worker et le stockage chaque fois pour obtenir les changements en ligne. C'est un sujet pour plus de recherches.

### Étape 4 : Badge d'honneur de Travis CI

Il reste une dernière tâche devant nous. Il s'agit d'obtenir un joli badge de statut de construction Travis CI sur le fichier `README.md` de notre dépôt.

Ouvrez Travis CI et cliquez sur le badge **build:passing**. Il affichera une boîte de dialogue avec des options pour porter l'image. Laissez la branche comme **master**. Sélectionnez **Markdown** au lieu de **Image URL**. Copiez le texte qui vous est donné.

Collez-le dans le `README.old.md`, qui nous a été laissé par `create-react-app` précédemment. Écrivez votre propre contenu.

Vous pouvez supprimer le `README.md` par défaut du dépôt et renommer le `README.old.md` en `README.md`.

Ajoutez les changements à la zone de transit Git, validez et poussez vers le cloud. Maintenant, le dépôt devrait montrer le badge que vous avez toujours voulu. Voici l'URL affichée pour notre projet.

```
https://travis-ci.org/pineboat/react-continuous-deployment.svg?branch=master
```

Vous pouvez ajouter cette URL au `README.md` en haut. Voici l'image :

![Image](https://cdn-media-1.freecodecamp.org/images/wvSWCLbsrzYzZa5arMQ3CX5flVEQRptZoF7Z)
_Nous avons terminé ici ! Temps de célébrer._

Je voudrais vous laisser avec une question. Si vous travaillez dans de grandes équipes utilisant un flux de travail similaire, quels sont les défis auxquels vous êtes confrontés et comment les résoudrez-vous ? Écrivez un commentaire et faites-le moi savoir.

Merci beaucoup d'avoir lu. J'espère que vous l'avez trouvé utile.

Cela a été publié à l'origine sur [pineboat.in](https://www.pineboat.in/post/travis-to-deploy-react-to-github-pages/).

Applaudir montre à quel point vous avez apprécié cet article.