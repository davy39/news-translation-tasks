---
title: Comment créer une PWA personnalisée avec Workbox dans create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T19:23:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-custom-pwa-with-workbox-in-create-react-app-be580686cf73
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sp2Kk29yH_3VsOeB4i1dpg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer une PWA personnalisée avec Workbox dans create-react-app
seo_desc: 'By Zaid Humayun

  Note: This is the third in a series of posts about PWAs inside of React. For a quick
  primer, see the previous two posts here and here.

  In this follow up post, I’m going to take you through how to build a custom Progressive
  Web App (PW...'
---

Par Zaid Humayun

**Note :** Il s'agit du troisième article d'une série sur les PWAs dans React. Pour une introduction rapide, consultez les deux articles précédents [ici](https://medium.freecodecamp.org/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3) et [ici](https://medium.freecodecamp.org/how-to-customize-service-workers-with-create-react-app-4424dda6210c).

Dans cet article de suivi, je vais vous expliquer comment créer une Progressive Web App (PWA) personnalisée en utilisant la [bibliothèque Workbox de Google](https://developers.google.com/web/tools/workbox/) sans éjecter du shell create-react-app (CRA).

Workbox est une collection de bibliothèques qui facilitent la création de fonctionnalités hors ligne. Workbox est également considéré comme le successeur de la bibliothèque `sw-precache`, que CRA utilise pour générer un SW par défaut.

Il y a eu des discussions sur la migration de CRA de `sw-precache` vers Workbox (voir [cet issue](https://github.com/facebook/create-react-app/issues/2340) pour plus de détails). Malheureusement, rien ne semble en être sorti pour l'instant.

### **Objectifs**

1. Configurer la construction CRA pour utiliser [react-app-rewired](https://github.com/timarney/react-app-rewired). (react-app-rewired est une bibliothèque pour configurer la construction CRA par défaut sans éjecter)
2. Utiliser react-app-rewired pour personnaliser la construction afin d'utiliser Workbox pour générer un service worker
3. Créer une application todo très simple
4. Implémenter une fonctionnalité hors ligne pour l'application todo en utilisant Workbox.
   La fonctionnalité hors ligne que nous allons cibler :
   a) Mettre en cache les ressources récupérées pour qu'elles puissent être servies hors ligne
   b) Permettre l'envoi de données en POST hors ligne

### **Introduction de Workbox dans CRA**

Tout d'abord, créez un nouveau dépôt CRA avec la commande suivante :

```
npx create-react-app react-app-rewire-workbox
```

Cela devrait configurer un nouveau dossier avec le nom pertinent. Une fois ce dossier configuré, accédez-y et créez un fichier de service worker dans le dossier public. Je vais appeler le mien `custom-service-worker.js`.

Une fois cela fait, allez-y et supprimez la vérification de `NODE_ENV` étant défini sur PRODUCTION à l'intérieur de `registerServiceWorker.js`.

Enfin, à l'intérieur du fichier `custom-service-worker.js`, collez le code suivant :

Ce snippet de code est quelque chose que j'ai pris directement du [site web de Workbox](https://developers.google.com/web/tools/workbox/guides/get-started). Vous utilisez la ligne `importScripts` pour injecter une variable globale nommée `workbox` dans votre fichier. Le script que vous importez est servi via un CDN. Vous avez ensuite une simple vérification pour voir si la variable a été chargée correctement par le script ou non.

Ainsi, nous avons maintenant Workbox qui fonctionne pour nous dans un environnement de développement. Ensuite, déterminons comment implémenter `react-app-rewired` dans CRA.

### **Implémentation de react-app-rewired dans CRA**

Ajoutez le package `react-app-rewired` à votre dossier de projet en utilisant la commande suivante :

```
npm install --save-dev react-app-rewired
```

Maintenant, si vous lisez [la documentation](https://github.com/timarney/react-app-rewired), ils mentionnent que vous devez configurer un fichier `config-overrides.js` dans le répertoire racine de votre projet. Commençons par comprendre ce que cela fait.

Je vais configurer un fichier minimal et vous expliquer ce qu'il signifie. Il y a une explication très détaillée de cela dans [la documentation](https://github.com/timarney/react-app-rewired#extended-configuration-options), si vous souhaitez la lire à la place.

Vous pouvez exporter un objet à partir de ce fichier avec trois clés : webpack, jest, devServer. Les fonctions respectives vous permettent de configurer la configuration du serveur de production webpack, la configuration jest, et enfin la configuration du serveur de développement webpack.

Si vous regardez la clé `devServer` dans le fichier `config-overrides.js`, vous remarquerez que nous enregistrons `configFunction.toString()` au lieu de simplement `configFunction`. Cela est dû au fait que si vous essayez ce dernier, Node imprimera simplement `[Function]` dans la console.

Ouvrez votre fichier `package.json` et remplacez la commande de script pour start par `react-app-rewired start`.

### **Création de l'application Todo**

Jusqu'à présent, nous avons réussi à introduire Workbox dans notre environnement de développement, et nous avons également introduit `react-app-rewired` dans notre shell CRA. Laissons les choses telles qu'elles sont et créons une application todo de démonstration, et faisons-la fonctionner dans l'environnement de développement.

L'application todo va nécessiter quelques éléments mobiles, juste pour que nous puissions réellement utiliser les service workers.

Cela va impliquer :

1. Une couche UI de base (je vais complètement ignorer le style pour cela.)
2. Un `json-server` auquel nous pouvons demander des données

Je ne vais pas entrer dans trop de détails sur la configuration de cela, car c'est assez simple. Je vais inclure un lien vers un dépôt git avec une version fonctionnelle de cette application à la fin de cet article, afin que vous puissiez y jeter un coup d'œil.

Voici le composant Todo que j'ai écrit.

Le composant fait une requête fetch à un `json-server` que j'ai configuré, et obtient une réponse composée d'un tableau de todos. Le composant rend ensuite ces todos. Comme je l'ai dit, extrêmement simple.

Pour configurer le `json-server`, exécutez la commande suivante :

```
npm install --save json-server
```

Créez un fichier appelé `db.json` avec la structure suivante

Enfin, exécutez la commande suivante dans le terminal :

```
json-server --watch db.json --port 8000
```

Cela exécute un serveur local sur le port 8000, et surveille le fichier `db.json` pour tout changement. En cas de changement, le serveur se redémarre. C'est un moyen très simple de simuler un serveur pour tester votre application.

Enfin, mettez à jour votre fichier `App.js` pour refléter votre nouveau composant Todo, et supprimez le JSX par défaut de ce fichier.

Lancez l'application (dans une fenêtre de navigation privée) et regardez à quoi elle ressemble maintenant. Vous devriez voir une liste de todos et une zone de saisie en dessous avec un bouton pour soumettre. Comme je l'ai dit, une UI très simple.

Une fois que vous avez tout cela configuré, déterminons un moyen de faire fonctionner tout cela hors ligne en utilisant Workbox.

**Note :** Lors du test de la fonctionnalité des service workers dans un environnement de développement, assurez-vous toujours de le faire dans une nouvelle fenêtre de navigation privée à chaque fois. Cela rend le test et le débogage beaucoup moins fastidieux car vos données ne sont pas stockées entre les sessions.

### **Implémentation de la mise en cache avec Workbox**

Maintenant, si vous allez de l'avant et ouvrez la barre d'outils Chrome, vous devriez voir quelque chose qui ressemble à ce qui suit sous l'onglet Application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6M7SSHyjM_1Yf2GV8Dvk9A.png)
_Barre d'outils de développement Google Chrome_

Cochez la case hors ligne, puis essayez de recharger votre page web. Elle échouera probablement avec une erreur indiquant qu'aucune connexion réseau n'a été détectée. Si vous regardez l'onglet réseau, vous verrez un tas de requêtes réseau échouées.

La plus évidente qui échouera est la requête à notre `json-server` pour récupérer la liste des todos. Corrigons cela en premier. Ouvrez le fichier `custom-service-worker.js` et ajoutez le code suivant

```
workbox.routing.registerRoute(
  'http://localhost:8000/todos',
  workbox.strategies.networkFirst()
)
```

Cela configure une stratégie de mise en cache `networkFirst` pour toute requête faite à l'endpoint `http://localhost:8000/todos`. L'image ci-dessous vous donne une explication claire de ce que la stratégie `networkFirst` implique. Vous vérifiez toujours le réseau en premier, et seulement en cas d'échec du réseau, vous allez dans le cache pour récupérer la ressource. Il s'agit d'une stratégie typique que vous pourriez utiliser lors de l'interrogation d'une API susceptible de fournir des données fraîches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xTrAJtPw5Cdb-SErJgBSYg.png)
_Stratégie Network First_

Maintenant, l'application ne va toujours pas se charger car il nous manque encore deux éléments importants. À savoir, nous ne mettons toujours pas en cache

1. Le bundle JS qui est servi par notre serveur de développement local.
2. Le fichier `index.html`

Ajoutez le code suivant à `custom-service-worker.js`

```
workbox.routing.registerRoute(
  /\.(?:js|css|html)$/,
  workbox.strategies.networkFirst(),
)

workbox.routing.registerRoute(
  'http://localhost:3000',
  workbox.strategies.networkFirst()
)
```

Si vous remarquez, la première route dans l'extrait de code ci-dessus est un objet `RegEx`. Il s'agit d'un moyen propre et simple de cibler plusieurs routes avec la même stratégie. Cependant, si vous ciblez une ressource qui ne suit pas la même politique d'origine, assurez-vous de spécifier la route complète.

Ce n'est bien sûr pas la manière idéale de faire les choses. Idéalement, nous voulons que les ressources statiques comme les bundles JS, les feuilles de style et les fichiers HTML soient précachées dans le cadre du processus de construction de Webpack. Nous y viendrons, mais il est important de comprendre qu'il n'y a pas de magie noire. Tout cela n'est que de la mise en cache simple.

Allez-y et lancez à nouveau la page et ouvrez votre console. Vous devriez voir un tas de logs de Workbox concernant le routage. Passez en mode hors ligne et actualisez la page. Vous devriez voir tout se charger comme d'habitude. Si vous ouvrez les logs de Workbox dans la console, vous verrez Workbox imprimer si la requête réseau a échoué ou réussi, et la réponse de Workbox à cet échec (voir la capture d'écran ci-dessous) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*deKoAAdcLbj8PjqykZNvsQ.png)
_Log Workbox dans la fenêtre Chrome Dev Tools_

### **Implémentation de l'envoi différé de données avec Workbox**

D'accord, ensuite : comment renvoyer des données POST au serveur sans connexion réseau ?

Tout d'abord, configurons un moyen de renvoyer des données en ligne, et assurons-nous que cela fonctionne. Mettez à jour votre fonction `addTodo` à l'intérieur de votre composant Todo pour qu'elle ressemble à ce qui suit :

Tout ce que nous avons fait, c'est ajouter un gestionnaire de rappel à `setState` afin que nous puissions être informés lorsque l'état a été mis à jour. À ce stade, nous avons fait une requête POST au `json-server` pour mettre à jour `db.json` avec le nouveau todo.

Essayez de soumettre un nouveau todo, ouvrez `db.json` et vous devriez voir le nouveau todo ajouté à votre tableau d'objets.

Maintenant, essayez de faire exactement la même chose hors ligne, et vous devriez obtenir une erreur réseau pour des raisons évidentes. Vous obtiendrez probablement une déclaration de log qui dit : Failed to fetch.

Pour résoudre cela, nous allons utiliser quelque chose appelé backgroundSync, dont vous pouvez lire la spécification [ici](https://wicg.github.io/BackgroundSync/spec/). Le fonctionnement est le suivant : chaque fois que vous faites une requête à un serveur pour une ressource spécifique (dans notre cas une requête POST), si aucun réseau n'est détecté, Workbox stockera cette requête dans indexedDB et continuera à interroger la requête pendant une période définie. Lorsqu'une connexion réseau est détectée, la requête sera rejouée. Si aucune connexion réseau n'est établie dans le délai prédéterminé, la requête est abandonnée.

L'API backgroundSync utilise quelque chose appelé SyncManager sous le capot. Vous pouvez en lire plus dans la documentation MDN [ici](https://developer.mozilla.org/en-US/docs/Web/API/SyncManager). Malheureusement, comme vous pouvez le voir, SyncManager n'est pas sur la voie des standards et Chrome est le seul navigateur qui a une spécification entièrement implémentée. Cela signifie que Chrome est le seul navigateur où cela est garanti de fonctionner de manière fiable.

Nous devons ajouter du code à `custom-service-worker.js` pour que le backgroundSync fonctionne pour nous. Ajoutez le code suivant au fichier :

Nous utilisons un plugin de synchronisation en arrière-plan que Workbox nous fournit. Le premier paramètre que vous fournissez au constructeur est le nom de la file d'attente que vous voulez que Workbox crée lors du stockage des requêtes échouées. Le deuxième paramètre est un objet d'options, où nous définissons la durée maximale pour tenter de rejouer les requêtes.

Enfin, nous enregistrons une nouvelle route avec la méthode POST, et configurons la stratégie que nous voulons utiliser pour la mise en cache. Cela est très similaire à ce que nous avons déjà fait, à l'exception de la définition du type de requête effectuée, et également d'avoir un plugin défini pour notre stratégie.

Maintenant, essayez de passer par le même scénario de soumission d'un todo sans aucune connexion réseau et observez ce qui se passe dans le log. Vous obtiendrez un log qui ressemble à la capture d'écran suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fga8x8OIE4dT8b4DMvBRIw.png)
_Workbox ajoute la requête échouée à une file d'attente_

Vous pouvez regarder la requête qui a été ajoutée en cherchant indexedDB sous l'onglet application dans la fenêtre Chrome DevTools. Ouvrez les sous-répertoires listés sous le menu déroulant indexedDB, et vous devriez voir la requête stockée, en attente d'être rejouée.

Désactivez l'option hors ligne dans la fenêtre DevTools, et vous devriez voir un nouveau log Workbox apparaître presque immédiatement. Il ressemblera à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C46elEi-gXvBXEwpy1INqw.png)
_Log Workbox détaillant que la requête échouée a été rejouée et soumise_

L'image ci-dessus montre Workbox rejouant la requête échouée dès qu'il reçoit une requête de synchronisation, et vous donnant la confirmation que votre requête a réussi. Si vous regardez `db.json` maintenant, vous remarquerez que le nouveau todo a été ajouté au fichier.

Eh bien, nous y voilà. Nous avons maintenant un moyen de rejouer les requêtes échouées via un service worker.

Ce que nous devons faire ensuite, c'est intégrer un plugin Webpack afin que Workbox puisse mettre en cache les ressources statiques dans le cadre du processus de construction. Cela éliminera le besoin d'avoir explicitement une route pour mettre en cache les ressources statiques à l'intérieur de notre fichier Service Worker.

### **Précache des ressources statiques**

Cela va être l'étape finale. Dans cette section, nous allons apporter des modifications au processus de construction de CRA pour le forcer à générer le fichier Service Worker en utilisant Workbox au lieu de `sw-precache`.

Tout d'abord, installez les packages suivants : `workbox-webpack-plugin` et `path`.

Ouvrez le fichier `package.json` et modifiez le script de construction pour qu'il s'exécute avec `react-app-rewired` au lieu de `react-scripts`, de la même manière que nous l'avons fait pour le script de démarrage.

Enfin, ouvrez le fichier `config-overrides.js` et modifiez-le pour qu'il ressemble à ce qui suit :

Il y a quelques choses que nous faisons dans ce fichier.

Tout d'abord, nous vérifions s'il s'agit d'une construction de production. Si c'est le cas, nous créons un objet de configuration Workbox et lui fournissons le chemin de notre SW personnalisé, ainsi que le chemin du SW de sortie que nous voulons.

Nous fournissons également une option appelée `importWorkboxFrom` et la définissons sur `disabled`.

Il s'agit d'une option spécifiant que nous ne voulons pas que Workbox soit importé de quelque part, puisque nous le demandons directement à partir d'un CDN dans notre script SW.

Enfin, nous avons une fonction appelée `removeSWPrecachePlugin`. Tout ce qu'elle fait est de parcourir les plugins listés dans la configuration Webpack, de trouver le bon, et de retourner l'index afin que nous puissions le supprimer.

Maintenant, allez-y et exécutez la construction de l'application, et ouvrez le fichier SW généré dans le dossier de construction. Dans mon cas, ce fichier SW a le nom `custom-service-worker.js`.

Vous remarquerez un nouvel appel `importScripts` en haut du fichier, qui semble demander un fichier de manifeste de précache. Ce fichier est stocké dans le dossier de construction, et si vous l'ouvrez, vous devriez voir la liste de toutes les ressources statiques mises en cache par Workbox.

### **Conclusion**

Ainsi, nous avons accompli les objectifs suivants :

1. Configurer la construction CRA pour utiliser [react-app-rewired](https://github.com/timarney/react-app-rewired)
2. Utiliser react-app-rewired pour personnaliser la construction afin d'utiliser Workbox pour générer un Service Worker — Nous avons accompli cela en utilisant `workbox-webpack-plugin`. Le processus de construction va maintenant automatiquement mettre en cache toutes les ressources statiques.
3. Créer une application todo très simple
4. Implémenter une fonctionnalité hors ligne pour l'application todo en utilisant Workbox.
   La fonctionnalité hors ligne que nous allons cibler :
   a) Mettre en cache les ressources récupérées pour qu'elles puissent être servies hors ligne
   b) Permettre l'envoi de données en POST hors ligne

Voici le [lien](https://github.com/redixhumayun/react-app-rewired-workbox) vers le dépôt qui contient une version fonctionnelle de l'application. Vous pouvez le cloner et jouer avec.

> Suivez-moi sur Twitter [ici](https://twitter.com/zz_humayun). Suivez-moi sur GitHub [ici](https://github.com/redixhumayun)