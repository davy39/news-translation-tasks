---
title: Comment déboguer des applications Node.js en utilisant l'instruction debugger;
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2024-04-22T19:50:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-node-js-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/debug_node_js_code_thumbnail-2.png
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Comment déboguer des applications Node.js en utilisant l'instruction debugger;
seo_desc: 'In this tutorial, you will learn the easiest and most efficient way to
  debug Node.js application code.

  So let''s get started.

  Want to watch the video version of this tutorial? You can check out the video below:

  https://www.youtube.com/watch?v=B_oPWQ9W...'
---

Dans ce tutoriel, vous apprendrez la manière la plus facile et la plus efficace de déboguer le code des applications Node.js.

Alors, commençons.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter la vidéo ci-dessous :

%[https://www.youtube.com/watch?v=B_oPWQ9Wyew]

## Table des matières

* [Comment vous déboguez habituellement les applications Node.js](#heading-comment-vous-deboguez-habituellement-les-applications-nodejs)
* [Comment ajouter un débogueur pour déboguer votre code](#heading-comment-ajouter-un-debogueur-pour-deboguer-votre-code)
* [Comment exécuter l'application pour le débogage](#heading-comment-executer-lapplication-pour-le-debogage)
* [Comment accéder aux variables pendant le débogage](#heading-comment-acceder-aux-variables-pendant-le-debogage)
* [Comment créer un script pour déboguer les applications Node.js](#heading-comment-creer-un-script-pour-deboguer-les-applications-nodejs)
* [Récapitulatif rapide](#heading-recapitulatif-rapide)

## **Comment vous déboguez habituellement les applications Node.js**

Si vous souhaitez déboguer une application Node.js, généralement vous ajoutez une instruction `console.log` dans le code que vous voulez déboguer pour connaître la valeur de n'importe quelle variable.

Cela fonctionne, mais vous devez continuer à vérifier la console pour voir la valeur que vous essayez d'afficher.

Et si les données affichées dans la console contiennent des objets imbriqués ou s'il y a beaucoup de données, alors utiliser `console.log` n'est pas faisable.

Heureusement, il existe une meilleure façon.

## **Comment ajouter un débogueur pour déboguer votre code**

Au lieu de cela, vous pouvez ajouter une instruction `debugger;` dans le code que vous voulez déboguer.

Supposons donc que vous avez une route API Express.js pour l'inscription d'un utilisateur comme montré dans le code ci-dessous :

```js
// controllers/auth.js

const register = async (req, res) => {
  try {
    const { email, password } = req.body;
    const existingUser = await User.findOne({
      email,
    });
    if (existingUser) {
      return res.status(400).send('Un utilisateur avec l\'email fourni existe déjà');
    }
    // some more code
    return res.status(201).send();
  } catch (error) {
    console.log(error);
    return res
      .status(500)
      .send('Erreur lors de l\'inscription d\'un nouvel utilisateur. Réessayez plus tard.');
  }
};

module.exports = { register };

// routes/auth.js
const { register } = require('../controllers/auth');

const Router = express.Router();

Router.post('/api/register', register);

```

Et il y a un problème lors de l'inscription d'un utilisateur, donc vous voulez déboguer le code de la fonction `register`.

Dans ce cas, vous pouvez simplement ajouter une instruction `debugger;` à l'intérieur du code de la fonction `register` comme ceci :

```js
const register = async (req, res) => {
  try {
    const { email, password } = req.body;
    debugger;
    const existingUser = await User.findOne({
      email,
    });
    if (existingUser) {
      return res.status(400).send('Un utilisateur avec l\'email fourni existe déjà');
    }
    // some more code
    return res.status(201).send();
  } catch (error) {
    console.log(error);
    return res
      .status(500)
      .send('Erreur lors de l\'inscription d\'un nouvel utilisateur. Réessayez plus tard.');
  }
};

```

## **Comment exécuter l'application pour le débogage**

Normalement, vous démarrez votre application Node.js en exécutant la commande suivante :

```javascript
node index.js

```

Mais au lieu de cela, vous pouvez exécuter la commande suivante :

```javascript
node inspect index.js

```

Ici, nous avons simplement ajouté un mot-clé `inspect` entre les deux.

Si le nom de votre fichier d'application principal est `server.js`, vous pouvez exécuter la commande `node inspect server.js`.

Une fois que vous avez exécuté la commande ci-dessus, vous verrez le résultat affiché comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_debugger_output.png)
_Débogueur attaché_

Comme vous pouvez le voir à partir du résultat, le débogueur est attaché, donc maintenant vous pouvez commencer à déboguer le code.

Pour cela, ouvrez le navigateur Chrome et entrez `chrome://inspect` dans l'URL du navigateur.

Vous verrez le résultat comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/2_chrome_inspect.png)
_Page d'inspection Chrome_

Puisque vous avez exécuté la commande `node inspect index.js` pour commencer l'inspection, vous pouvez voir une nouvelle entrée de cible affichée sous la section `Remote Target`.

Maintenant, si vous cliquez sur le lien bleu `inspect` affiché, alors vous verrez un nouvel outil de développement du navigateur ouvert comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/3_debugger_started.png)
_Débogueur en pause_

Comme vous pouvez le voir dans le panneau de droite dans l'image ci-dessus, le message `Debugger paused` est affiché. Le contrôle de débogage est à la première ligne de code, comme vous pouvez le voir à partir de la ligne jaune surlignée.

Mais vous ne voulez pas commencer à déboguer à partir de la première ligne de code. Au lieu de cela, vous voulez simplement déboguer le code d'inscription. Pour cela, cliquez sur l'icône de triangle bleu qui est affichée juste au-dessus du message `Debugger paused` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/4_debugging_stopped.gif)
_Continuation du débogage_

Maintenant, ne fermez pas cette fenêtre – au lieu de cela, essayez de vous inscrire en tant qu'utilisateur depuis l'application ou faites un appel API en utilisant Postman, afin que le code du gestionnaire de route `/register` que nous avons ajouté précédemment soit exécuté.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/5_registering_user.gif)
_Inscription de l'utilisateur et débogage du code_

Comme vous pouvez le voir ci-dessus, lorsque vous cliquez sur le bouton de création de nouveau compte, vous êtes automatiquement redirigé vers le code où vous avez ajouté l'instruction `debugger;`.

Maintenant, vous pouvez déboguer le code ligne par ligne et voir les valeurs de chaque variable pendant le débogage pour trouver et corriger le problème.

## **Comment accéder aux variables pendant le débogage**

Parfois, lorsque vous survolez une variable pendant le débogage pour voir sa valeur réelle, la valeur peut être trop longue (parce qu'il peut s'agir d'un objet avec de nombreuses propriétés), donc vous ne pouvez pas la voir facilement en la survolant.

Dans ce cas, alors que le débogueur est toujours actif, vous pouvez ouvrir l'onglet console et taper le nom de la variable dont vous voulez voir la valeur – comme vous pouvez le voir dans le Gif ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/6_logging_variables_in_console.gif)
_Journalisation des variables dans la console_

Voici comment vous pouvez facilement déboguer n'importe quel code de vos applications Node.js.

## **Comment créer un script pour déboguer les applications Node.js**

Si vous ne voulez pas taper manuellement la commande `node inspect index.js` à chaque fois dans le terminal, vous pouvez créer un nouveau script `debug` dans le fichier `package.json` comme ceci :

```js
"scripts": {
    "start": "node index.js",
    "debug": "node inspect index.js",
    "dev": "nodemon index.js"
},

```

Ainsi, maintenant, vous pouvez exécuter la commande `npm run debug` pour démarrer votre application en mode débogage.

## **Récapitulatif rapide**

Pour déboguer une application Node.js, vous devez suivre les étapes ci-dessous :

* Ajoutez une instruction `debugger` à l'intérieur du code que vous voulez déboguer.
* Exécutez la commande `node inspect index.js` ou `node inspect server.js` pour démarrer l'application en mode débogage.
* Accédez à l'URL `chrome://inspect` dans votre navigateur Chrome.
* Cliquez sur le lien `inspect` sous la section `Remote Target`.
* Cliquez sur l'icône de triangle bleu pour sauter le débogage si vous ne voulez pas commencer à déboguer votre application à partir de la première ligne du fichier `index.js` ou `server.js`.
* Faites un appel API ou faites quelque chose qui déclenchera le code où vous avez ajouté l'instruction `debugger;`. De cette façon, vous pouvez déboguer le code ligne par ligne et trouver le problème.

## **Merci d'avoir lu**

C'est tout pour ce tutoriel. J'espère que vous avez appris quelque chose de nouveau.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=B_oPWQ9Wyew).

Si vous voulez maîtriser JavaScript, ES6+, React et Node.js avec un contenu facile à comprendre, consultez ma [chaîne YouTube](https://www.youtube.com/@codingmastery_dev/). N'oubliez pas de vous abonner.

Vous voulez rester à jour avec un contenu régulier sur JavaScript, React et Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://www.youtube.com/watch?v=wcjCsMRZKxs" target="_blank"><img src="https://d31ezp3r8jwmks.cloudfront.net/7g60tc6qngrs80np7v12vana6w1s" alt="Apprenez à créer une application de partage de liens Full Stack en utilisant la pile MERN"/></a>