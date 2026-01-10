---
title: Je viens de déployer une application serverless — et je ne sais pas coder.
  Voici comment j'ai fait.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T14:35:18.000Z'
originalURL: https://freecodecamp.org/news/i-just-deployed-a-serverless-app-and-i-cant-code-here-s-how-i-did-it-94983d7b43bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zq-SUy3UzV6e09uBD_c8PQ.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: Je viens de déployer une application serverless — et je ne sais pas coder.
  Voici comment j'ai fait.
seo_desc: 'By Andrea Passwater

  Hey there developer friends! I somehow just managed to deploy a real, working application.
  But heads up — I am not one of you.

  I am a writer who honest-to-god composes tweets and blog posts for a living.

  My command line experience...'
---

Par Andrea Passwater

Salut les amis développeurs ! J'ai somehow réussi à déployer une vraie application fonctionnelle. Mais attention — je ne suis pas l'un de vous.

Je suis une écrivaine qui compose honnêtement des tweets et des articles de blog pour gagner sa vie.

Mon expérience avec la ligne de commande se limite à un cours Codecademy que j'ai suivi avant la sortie de l'iPhone 5. Je sais taper `ls` pour voir le contenu d'un dossier sans style visuel. En résumé, je suis une hackeuse badass.

Quoi qu'il en soit, amis, j'ai écrit une application. Et elle est hébergée. Et vous pouvez la visiter vous-même, depuis votre propre ordinateur.

Car, comme je l'ai découvert, [AWS Lambda](https://aws.amazon.com/lambda/) et le [Serverless Framework](http://serverless.com/framework) rendent le déploiement d'une application **vraiment** pas si difficile.

Voici comment vous aussi pouvez écrire et déployer une application serverless avec pratiquement zéro expérience en codage.

### Ok mais comme... pourquoi as-tu fait ça ?

Je suis si contente que vous ayez demandé ! Parce que, regardez — l'automatisation, c'est le pouvoir.

Comme vous, j'ai des choses — trop de choses — à faire, et pas assez de ressources pour les accomplir.

Je veux écrire des bots Slack qui rappellent aux gens quand leurs brouillons de blog sont dus. Je veux créer des campagnes d'emailing basées sur le comportement des utilisateurs sans exploser mon budget avec quinze outils marketing. Je veux fusionner automatiquement des articles de blog selon un calendrier prédéfini.

Les applications personnalisées me donnent ce pouvoir. Je pourrais créer une **équipe de minions robots**.

### Créer l'application

Ce projet entier m'a pris peut-être une heure.

Voici ce que nous allons faire :

* Installer le Serverless Framework
* Créer un compte AWS
* Configurer les permissions AWS (rôles IAM) pour mon utilisateur serverless
* Trouver du code librement disponible sur npm qui fait à peu près ce que je veux
* Le voler
* Le modifier
* Le déployer sur Lambda en utilisant le Serverless Framework

Le truc cool avec Lambda, c'est que je n'ai pas à le gérer, le provisionner, le mettre à l'échelle **ou quoi que ce soit**. Je balance mon code là-bas, et il s'exécute quand il en a besoin. Je peux le déployer et pratiquement l'oublier.

Le truc cool avec le Serverless Framework, c'est que AWS est difficile à comprendre. Le Framework s'occupe de tous les détails en coulisses, et franchement, il rend presque impossible de tout gâcher.

Preuve en est : moi. Je n'ai rien gâché.

Cette chose est à toute épreuve.

### Installer le Serverless Framework

Si vous n'avez pas déjà Homebrew (je ne l'avais pas), vous devrez l'installer d'abord. [Homebrew](https://brew.sh/) facilite l'installation de toutes sortes de trucs pour développeurs sur votre machine.

Ouvrez votre terminal, et collez le snippet de la page d'accueil de Homebrew :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Attendez une éternité (aka 5 minutes) pour que ça se termine, puis installez Node ; le Framework en a besoin pour fonctionner :

`brew install node`

Ensuite, collez le snippet de la page d'accueil de Serverless.com :

`npm install serverless -g`

Félicitations ! Vous êtes arrivé jusqu'ici en utilisant uniquement le copier/coller.

### Créer un compte AWS

Allez sur [aws.amazon.com](https://aws.amazon.com/) et cliquez sur l'un des quinze boutons utiles qui vous permettent de créer un nouveau compte. J'ai choisi celui en haut à droite :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Ils vont vous faire répondre à beaucoup de questions. Désolé pour ça. Tout cela sera bientôt terminé.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Quand ils vous demandent votre carte de crédit, vous devrez leur en donner une. Ils ne vous facturent rien d'avance, mais ils la gardent dans leurs dossiers au cas où.

![Image](https://cdn-media-1.freecodecamp.org/images/7VTKpigfo8aAw9ZJx07wazSRe4qGdqhicMtK)

Ok, j'ai menti sur la partie "bientôt terminé". Maintenant, ils vont vouloir vérifier votre identité en faisant appeler un robot (lol). Contentez-les, nous sommes sérieusement presque terminés cette fois.

Quand votre téléphone sonne, entrez le code PIN à 4 chiffres sur votre écran. J'ai regardé le chronomètre sur mon téléphone ; c'était un appel de 20 secondes.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Enfin, choisissez votre plan de support ! Ce qui signifie, ne choisissez pas de plan de support. À moins que vous ne soyez une vraie entreprise, je suppose, au quel cas dépensez ces dollars d'investisseurs comme vous le souhaitez.

Ici, je ne suis pas une vraie entreprise et je choisis l'option "Basic" parce qu'elle est gratuite :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Maintenant, allez-y et cliquez sur "Launch the console" et connectez-vous à nouveau.

Tout bien considéré, cette étape prend 5 à 10 minutes, selon que vous avez (vanterie modeste) votre numéro de carte de crédit mémorisé parce que vous êtes un acheteur en ligne prolifique.

### Configurer un utilisateur IAM

Le Serverless Framework en a besoin pour faire toute la configuration compliquée de Lambda à votre place.

Ça me semble être un bon échange ! Faisons-le.

Il est utile de noter que j'ai utilisé [ce guide incroyablement utile](https://serverless.com/blog/anatomy-of-a-serverless-app/) pour me guider tout au long du processus de configuration. Vous pourriez l'aimer aussi.

Maintenant que vous avez lancé votre console AWS, tapez "iam" dans cette boîte de recherche pratique :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Oui, nous aimerions gérer l'Accès utilisateur et les Clés de chiffrement. Cliquez dessus.

Une fois que vous êtes dans IAM, allez dans Utilisateurs dans le menu de gauche :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Puis Ajouter un utilisateur en haut :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Maintenant, nous devons configurer cet nouvel utilisateur.

Vous pouvez soit [regarder cette vidéo de 75 secondes](https://www.youtube.com/watch?v=yaLMc7WMmHQ&index=1&list=PLIIjEI2fYC-A5wxo521u6OqAwbsFFQFbW) et faire exactement ce qu'ils font, **ou** si vous êtes un geek pour les abstractions, vous pouvez faire défiler ces captures d'écran de **moi** faisant exactement ce qu'ils font et copier celles-ci à la place.

Créez n'importe quel nom d'utilisateur que vous voulez et cochez la case à côté de Accès programmatique :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Cliquez sur Attacher des politiques existantes directement puis cochez la case à côté de AdministratorAccess :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Il est utile de noter que, selon [cet article de blog de Serverless.com sur IAM](https://serverless.com/blog/abcs-of-iam-permissions/), prendre la voie AdministratorAccess est la méthode YOLO rapide mais risquée. Je vais le faire quand même parce que je ne suis pas une développeuse et donc ne comprends pas le chaos que je pourrais causer.

S'il vous plaît, ne me piratez pas.

Si vous voulez être extra diligent à ce sujet, suivez leurs directives sur [l'approche lente mais sûre](https://serverless.com/blog/abcs-of-iam-permissions/#managing-permissions-for-the-serverless-framework-user).

Allez-y et cliquez sur Suivant puis sur Créer un utilisateur.

Vous arriverez sur un écran comme celui-ci. **Ne fermez pas cette fenêtre encore, nous allons en avoir besoin** :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Installer AWS CLI

Cela nous permettra (1) de faire des choses avec AWS sans fouiller dans leur interface intimidante avec trop d'icônes ; (2) de copier/coller sans réfléchir des choses dans le terminal que des experts sur internet disent faire ce que nous voulons.

Pour commencer cette fête de copier/coller, mettez `brew install awscli` dans votre terminal pour faire installer AWS CLI par Homebrew.

Une fois que c'est fait, tapez `aws configure`.

Maintenant, vous aurez besoin de cette fenêtre d'utilisateur IAM, que vous n'avez définitivement pas fermée ! Copiez l'ID de la clé d'accès et la Clé d'accès secrète de cette fenêtre et collez-les dans le terminal comme demandé.

Je laisse le reste vide parce que (comme nous l'avons déjà couvert) YOLO :

```
AWS Access Key ID [None]: PLZ-PUT-UR-ACCESS-KEY-HEREAWS Secret Access Key [None]: PLZ-PUT-UR-SECRET-ACCESS-KEY-HEREDefault region name [None]: Default output format [None]:
```

### Surfer sur NPM pour du code pré-écrit

Puisque je suis une hipster avec un sens de l'humour ironique, j'ai décidé de faire de ma première application serverless un générateur de Serverless Ipsum.

C'est comme Lorem Ipsum, mais avec des mots-clés aléatoires du mouvement serverless. Vous voyez. C'est une application Serverless serverless. ?

Je suis allée sur [npmjs.com](https://www.npmjs.com/), qui est un site web magique où des gens avec des cœurs beaucoup plus grands que le mien postent leur code NodeJS pour que d'autres personnes puissent l'utiliser. ...gratuitement. Je n'arrive toujours pas à croire que cela existe vraiment.

J'ai tapé lorem ipsum dans la boîte de recherche et évalué mes options.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

J'ai cliqué sur celui qui s'appelait simplement lorem-ipsum, parce qu'en tant qu'écrivaine professionnelle, j'ai une affinité pour le minimalisme dans le choix des mots. (Merci [knicklabs](https://www.npmjs.com/~knicklabs)!)

Allons le récupérer.

Mais d'abord, nous devons créer un endroit pour le mettre. Un nouveau projet serverless, si vous voulez.

#### Utiliser le Serverless Framework pour créer un nouveau projet

Vous vous souvenez, au début de cet article, quand nous avons fait `npm install serverless -g` ? Cela a installé le Serverless Framework, que nous allons maintenant utiliser !

D'abord, créons un dossier pour garder tous nos nombreux projets serverless futurs. Je vais appeler mon dossier Code parce que ça rime avec Node et que je suis une poétesse.

Voici où mes compétences de hackeuse badass de Codecademy deviennent pertinentes. Dans votre terminal, tapez `ls` pour voir tous vos noms de dossiers. (Je ne pense pas vraiment qu'il y ait une raison pour laquelle vous **devez** faire cela, mais il n'y a pas de raison de ne pas le faire non plus, alors autant s'échauffer.)

Vous devriez voir une liste de tous les dossiers sur votre bureau, dans une police monospace propre. Magique.

Maintenant, tapez `mkdir Code` — aka, créer un répertoire (dossier) appelé 'Code'. Puis `cd Code` pour vous y rendre.

Dans ce tout nouveau dossier Code, je vais créer ma toute première application serverless. Regardez-moi faire :

`serverless create --template aws-nodejs --path serverless-ipsum`

La partie `--template aws-nodejs` indique à Serverless que nous utilisons AWS et NodeJS. Ils utiliseront ces informations pour faire des tours de configuration magiques en notre nom.

La partie `--path serverless-ipsum` indique à Serverless que notre nouveau projet s'appelle serverless-ipsum. Vous devriez donc remplacer serverless-ipsum par ce que vous voulez comme nom de projet.

Quand vous appuyez sur `enter`, Serverless créera un nouveau dossier appelé serverless-ipsum. Tout le contenu de votre application vivra là.

Nous venons de créer les débuts d'une application. Maintenant, donnons-lui du code à exécuter.

#### Installer ce package lorem ipsum de NPM

Naviguez jusqu'à ce répertoire serverless-ipsum que nous venons de créer en tapant `cd serverless-ipsum` dans votre terminal.

Puis tapez `npm install lorem-ipsum` pour installer le package lorem ipsum de NPM.

Maintenant, notre dossier d'application contient du code ! C'est déjà pratiquement une application ! En quelque sorte.

#### Modifier ce code NPM

Nous devons apporter quelques modifications à ce code, alors allez-y et ouvrez votre éditeur de code préféré. J'ai utilisé [Atom](https://atom.io/) parce que je n'ai pas d'éditeur de code préféré mais j'ai une unité de matière préférée.

En tout cas, voici à quoi votre fichier `handler.js` devrait ressembler maintenant :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Ouvrez-le et remplacez le contenu en haut par ceci :

```
'use strict';
```

```
const ipsum = require("lorem-ipsum")
```

```
module.exports.hello = (event, context, callback) => {  const response = {    statusCode: 200,    body: ipsum(),  };
```

```
callback(null, response);};
```

De sorte que votre fichier `handler.js` ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/jc2AY8UcAB3waJg0X-lbBk-clwiFRHP0BIPg)

Ce que nous avons fait ici, c'est dire à notre petit gestionnaire de fonction d'exécuter ce package `lorem-ipsum` que nous avons téléchargé et d'imprimer la sortie pour nous.

Nous avons d'abord requis le package en haut avec `const ipsum = require("lorem-ipsum")`, puis nous avons dit au `body` d'imprimer ce ipsum généré avec `body: ipsum()`. Tout le reste est resté le même.

#### Le tester localement dans le terminal

Les gars. Nous avons créé un projet serverless dans le Framework. Nous avons téléchargé du code pré-écrit qui génère du lorem ipsum.

Nous pouvons dire à Serverless de l'exécuter. Maintenant. Dans nos terminaux.

Moment de vérité. Tapez : `serverless invoke local --function hello`

Attendez...

```
{"statusCode": 200,"body": "Amet cillum est dolor eiusmod elit eiusmod nulla eu do."}
```

Oh mon dieu.

### Modifier ce générateur de lorem ipsum pré-construit

Le latin, c'est bien, mais le charabia serverless, c'est mieux. Nous faisons, après tout, un générateur de **Serverless** Ipsum.

Retournez dans Atom, où votre projet serverless-ipsum est probablement encore ouvert. Il contient plusieurs fichiers, et nous allons en ajouter un de plus.

Appuyez sur `cmd/ctrl + n` pour créer un nouveau fichier, et nommez-le `dictionary.js`. Créez un [tableau](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Array) et remplissez-le avec des mots à la mode de l'industrie comme Lambda et serverdeath :

![Image](https://cdn-media-1.freecodecamp.org/images/wU4Xhy41DtdJw3m9yV2KAHra3RyG0wWRGoAA)

Pour ceux d'entre vous qui sont exclusivement dans le train du copier/coller, voici :

```
module.exports = ['auto-scaling','zero-maintenance','pay-per-execution','serverdeath','function','event','handler','cloud','NoOps','Lambda','microservices','monitoring',]
```

Ensuite, enregistrez le fichier avec `cmd/ctrl + s`.

Nous devons également retourner dans notre fichier `handler.js`, et lui dire d'utiliser le fichier de dictionnaire que nous venons de créer.

Alors cliquez dans `handler.js`, et mettez ceci en haut :

```
const dictionary = require("./dictionary")
```

Maintenant, retournez dans le `body` de votre fonction, et dites-lui de prendre tous ses mots dans le dictionnaire que vous venez de créer, c'est-à-dire :

```
module.exports.hello = (event, context, callback) => {  const response = {    statusCode: 200,    body: ipsum({      words: dictionary,    }),  };
```

Votre fichier `handler.js` devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Essayons-le à nouveau localement, et voyons si la sortie est du Serverless Ipsum au lieu de Lorem Ipsum. Retournez dans le terminal et retapez cette commande `--function` d'avant :

`serverless invoke local --function hello`

Attendez...

```
{"statusCode": 200,"body": "Multi-cloud openWhisk google cloud functions lambda source services signature function monitoring zero-maintenance monitoring multi-cloud azure."}
```

C'est littéralement la chose la plus belle que j'aie jamais vue.

### Mettons cette chose sur internet

Oui oui, d'accord, donc ça marche sur votre ordinateur portable personnel. Mais les vrais devs ont leurs trucs disponibles sur **Chrome**.

Cela prend une étape minuscule de plus.

#### Modifier ce serverless.yml

Le YAML serverless (`serverless.yml`) est le fichier de configuration que Serverless utilise pour gérer les fonctions (aka, les morceaux de code) que vous déployez sur Lambda. Nous devons lui dire de créer un petit site web pour nous.

Voici à quoi ressemble actuellement notre fichier YAML `serverless-ipsum` (tous les commentaires effondrés pour la concision) :

![Image](https://cdn-media-1.freecodecamp.org/images/MtSdYP0449FYoFNF3rBocTw97JBEzSlJtosH)

Nous allons changer quelques choses dans la partie `functions`.

Ce truc hello est par défaut. Nous allons le remplacer par ipsum, parce que j'ai raisonnablement décidé que je voulais exécuter Serverless Ipsum avec la commande `ipsum`. (**Note :** Cela signifie que dorénavant, vous exécuterez `--function ipsum` au lieu de `--function hello`.)

Ensuite, nous allons dire au gestionnaire de fonction que, quand nous exécutons `ipsum`, ce que nous voulons vraiment qu'il fasse, c'est poster Serverless Ipsum sur une URL publique via une requête HTTP.

Blah blah blah allez simplement à la ligne 57 dans votre éditeur et remplacez tout ce truc par ceci :

```
functions:  ipsum:    handler: handler.ipsum    events:      - http:          method: get          path: /
```

Et maintenant votre `serverless.yml` devrait ressembler à ceci !

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Retournez dans votre fichier `handler.js` et changez `module.exports.hello` pour dire `module.exports.ipsum`. C'est parce que nous avons changé le nom de notre fonction de hello à ipsum.

Donc maintenant votre fichier `handler.js` ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Déployer déployer déployer !

C'est le moment. Nous sommes prêts à lancer cette chose pour de vrai.

Mettez-vous dans ce terminal.

Tapez `serverless deploy`.

Retenez votre souffle.

Et —

(!!!)

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

BOOM.

Prenez cette URL à côté de `GET` : [https://791qej6263.execute-api.us-east-1.amazonaws.com/dev/](https://791qej6263.execute-api.us-east-1.amazonaws.com/dev/?paragraphs=6)

Copiez/collez-la dans votre navigateur, et admirez :

![Image](https://cdn-media-1.freecodecamp.org/images/kDNZvno6vKXA5fvrbIoZ-kbQ1KRXkmNIxIU1)

Notre application. Est vivante. **Sur internet !**

### Choses que je dois encore faire

Ok, soyons réalistes. L'UI n'est pas jolie. Je prévois d'obtenir un domaine pour cela et de lui donner une sorte de frontend simple pour qu'il ait au moins l'air professionnel de manière plausible.

Un autre jour, les amis. Un autre jour.

### En somme

Je suis une écrivaine. Je ne sais pas coder. Mais j'ai fait une application serverless et je l'ai mise sur internet pour que tout le monde puisse la voir.

Serverless : **littéralement n'importe qui peut le faire**_._

AWS : **pas si effrayant** après tout_._

J'espère que vous utiliserez tous cela pour faire quelque chose de cool.