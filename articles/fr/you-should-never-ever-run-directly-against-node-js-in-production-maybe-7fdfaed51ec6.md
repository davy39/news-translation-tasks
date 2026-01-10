---
title: Vous ne devriez jamais exécuter directement contre Node.js en production. Peut-être.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T17:22:55.000Z'
originalURL: https://freecodecamp.org/news/you-should-never-ever-run-directly-against-node-js-in-production-maybe-7fdfaed51ec6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lh8JaRfiqPj9bTrd8a3xgQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Vous ne devriez jamais exécuter directement contre Node.js en production.
  Peut-être.
seo_desc: "By Burke Holland\nSometimes I wonder if I know much of anything at all.\n\
  Just a few weeks ago I was talking to a friend who mentioned off-hand, “you would\
  \ never run an application directly against Node in production”. \nI nodded vigorously\
  \ to signal tha..."
---

Par Burke Holland

Parfois, je me demande si je sais vraiment quelque chose.

Il y a quelques semaines à peine, je parlais à un ami qui a mentionné en passant : « tu ne devrais jamais exécuter une application directement contre Node en production ».

J'ai hoché vigoureusement la tête pour signaler que moi aussi, je ne devrais jamais exécuter directement contre Node en production parce que... hahaha... tout le monde sait cela. Mais je ne le savais pas ! Aurais-je dû le savoir ?!?! AI-JE ENCORE LE DROIT DE PROGRAMMER ?

Si je devais dessiner un diagramme de Venn de ce que je sais versus ce que je pense que tout le monde sait, cela ressemblerait à ceci...

![Image](https://cdn-media-1.freecodecamp.org/images/1*ThJbM2JMjrnTuHczo0tLqw.png)

Au fait, ce petit point devient de plus en plus petit à mesure que je vieillis.

Il existe un meilleur diagramme créé par [Alicia Liu](https://medium.com/counter-intuition/overcoming-impostor-syndrome-bdae04e46ec5) qui a un peu changé ma vie. Elle dit que c'est plutôt comme ceci...

![Image](https://cdn-media-1.freecodecamp.org/images/1*N7vv39ri9yC0l6krsSFlQA.png)

J'adore ce diagramme parce que je veux qu'il soit vrai. Je ne veux pas passer le reste de ma vie en tant que petit point bleu rétrécissant d'insignifiance.

TROP DRAMATIQUE. C'est la faute à Pandora. Je ne contrôle pas ce qui est joué ensuite pendant que j'écris cet article et [Dashboard Confessional](https://www.youtube.com/watch?v=ixG3DgrPC3c) est une drogue d'enfer.

Eh bien, en supposant que le diagramme d'Alicia est vrai, je voudrais partager avec vous ce que je sais maintenant sur l'exécution des applications Node en production. Peut-être que nos diagrammes de Venn relatifs ne se chevauchent pas sur ce sujet.

Tout d'abord, abordons l'affirmation « ne jamais exécuter des applications directement contre Node en production ».

#### Ne jamais exécuter directement contre Node en production

Peut-être. Mais peut-être pas. Parlons de la raison derrière cette affirmation. D'abord, voyons pourquoi ne pas le faire.

Disons que nous avons un serveur Express simple. Le serveur Express le plus simple auquel je puisse penser...

```js
const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

// vu à http://localhost:3000
app.get("/", function(req, res) {
  res.send("Again I Go Unnoticed");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```

Nous exécuterions cela avec un script de démarrage dans le fichier `package.json`.

```
"scripts": {
  "dev": "npx supervisor index.js",
  "start": "node index.js"
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VceC98Qk5zKqzBmiu1szDQ.png)

Il y a deux problèmes ici. Le premier est un problème de développement et le second est un problème de production.

Le problème de développement est que lorsque nous changeons le code, nous devons arrêter et démarrer l'application pour que nos changements soient pris en compte.

Pour résoudre cela, nous utilisons généralement un gestionnaire de processus Node comme `supervisor` ou `nodemon`. Ces packages surveilleront notre projet et redémarreront notre serveur chaque fois que nous apporterons des modifications. Je fais généralement cela comme ceci...

```
"scripts": {  "dev": "npx supervisor index.js",  "start": "node index.js"}
```

Ensuite, j'exécute `npm run dev`. Notez que j'exécute `npx supervisor` ici, ce qui me permet d'utiliser le package `supervisor` sans avoir à l'installer. J'❤️ 2019. Pour la plupart.

Notre autre problème est que nous exécutons toujours directement contre Node et nous avons déjà dit que c'était mauvais et nous allons maintenant découvrir pourquoi.

Je vais ajouter une autre route ici qui tente de lire un fichier sur le disque qui n'existe pas. C'est une erreur qui pourrait facilement apparaître dans n'importe quelle application réelle.

```js
const express = require("express");
const app = express();
const fs = require("fs");
const port = process.env.PORT || 3000;

// vu à http://localhost:3000
app.get("/", function(req, res) {
  res.send("Again I Go Unnoticed");
});

app.get("/read", function(req, res) {
  // ceci n'existe pas
  fs.createReadStream("my-self-esteem.txt");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```

Si nous exécutons cela directement contre Node avec `npm start` et que nous naviguons vers le point de terminaison `read`, nous obtenons une erreur car ce fichier n'existe pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pAUoJV-LRJwxs7MRegnuoA.png)

Ce qui — pas grave, non ? C'est une erreur. Cela arrive.

NON. Gros problème. Si vous retournez à votre terminal, vous verrez que l'application est complètement arrêtée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*69LuEt53W2isIXP34vUlYA.png)

Ce qui signifie que si vous retournez au navigateur et essayez d'aller à l'URL racine du site, vous obtenez la même page d'erreur. Une erreur dans une méthode a fait tomber l'application pour **tout le monde**.

C'est mauvais. Vraiment mauvais. C'est l'une des principales raisons pour lesquelles les gens disent **« ne jamais exécuter directement contre Node en production »**.

D'accord. Donc si nous ne pouvons pas exécuter contre Node en production, quelle est la bonne façon d'exécuter Node en production ?

#### Options pour Node en production

Nous avons quelques options.

L'une d'entre elles serait d'utiliser simplement quelque chose comme `supervisor` ou `nodemon` en production de la même manière que nous les utilisons en développement. Cela fonctionnerait, mais ces outils sont un peu légers. Une meilleure option est quelque chose appelé pm2.

#### pm2 à la rescousse

pm2 est un gestionnaire de processus Node qui a beaucoup de fonctionnalités. Comme tout le reste « JavaScript », vous l'installez (globalement) depuis `npm` — ou vous pouvez simplement utiliser `npx` à nouveau. Je ne veux pas vous dire comment vivre votre vie.

Il existe de nombreuses façons d'exécuter votre application avec pm2. La manière la plus simple est d'appeler simplement `pm2 start` sur votre point d'entrée.

```
"scripts": {
  "start": "pm2 start index.js",
  "dev": "npx supervisor index.js"
},
```

Et vous verrez quelque chose comme ceci dans le terminal...

![Image](https://cdn-media-1.freecodecamp.org/images/1*uvsnmQahRBHtnh0X7tt_xA.png)

C'est notre processus qui s'exécute en arrière-plan, surveillé par pm2. Si vous visitez le point de terminaison `read` et que l'application plante, pm2 la redémarrera automatiquement. Vous ne verrez rien de cela dans le terminal car il s'exécute en arrière-plan. Si vous voulez voir pm2 faire son travail, vous devez exécuter `pm2 log 0`. Le `0` est l'ID du processus pour lequel nous voulons voir les logs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AbR1eyySpr2IllYtA4wE-Q.png)

Nous y voilà ! Vous pouvez voir pm2 redémarrer l'application lorsqu'elle tombe en panne à cause de notre erreur non gérée.

Nous pouvons également sortir notre commande de développement et faire en sorte que pm2 surveille les fichiers pour nous et redémarre à chaque changement.

```
"scripts": {
  "start": "pm2 start index.js --watch",
  "dev": "npx supervisor index.js"
},
```

Notez que, comme pm2 exécute les choses en arrière-plan, vous ne pouvez pas simplement quitter un processus pm2 en cours avec `ctrl+c`. Vous devez l'arrêter en passant l'ID ou le nom.

`pm2 stop 0`

`pm2 stop index`

De plus, notez que pm2 conserve une référence au processus afin que vous puissiez le redémarrer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z4yLru6TmwUVQv84DkZDAQ.png)

Si vous voulez supprimer cette référence de processus, vous devez exécuter `pm2 delete`. Vous pouvez arrêter et supprimer un processus en une seule commande avec `delete`.

`pm2 delete index`

Nous pouvons également utiliser pm2 pour exécuter plusieurs processus de notre application. pm2 équilibrera automatiquement la charge entre ces instances.

#### Plusieurs processus avec le mode fork de pm2

pm2 dispose de nombreuses options de configuration et celles-ci sont contenues dans un fichier « ecosystem ». Pour en créer un, exécutez `pm2 init`. Vous obtiendrez quelque chose comme ceci...

```js
module.exports = {
  apps: [
    {
      name: "Express App",
      script: "index.js",
      instances: 4,
      autorestart: true,
      watch: true,
      max_memory_restart: "1G",
      env: {
        NODE_ENV: "development"
      },
      env_production: {
        NODE_ENV: "production"
      }
    }
  ]
};
```

Je vais ignorer la section « deploy » dans cet article car je ne sais pas ce qu'elle fait.

La section « apps » est l'endroit où vous définissez les applications que vous voulez que pm2 exécute et surveille. Vous pouvez en exécuter plus d'une. Beaucoup de ces paramètres de configuration sont probablement auto-explicatifs. Celui sur lequel je veux me concentrer ici est le paramètre **instances**.

pm2 peut exécuter plusieurs instances de votre application. Vous pouvez passer un nombre d'instances que vous voulez exécuter et pm2 en démarrera autant. Donc, si nous voulons exécuter 4 instances, nous pourrions avoir le fichier de configuration suivant.

```js
module.exports = {
  apps: [
    {
      name: "Express App",
      script: "index.js",
      instances: 4,
      autorestart: true,
      watch: true,
      max_memory_restart: "1G",
      env: {
        NODE_ENV: "development"
      },
      env_production: {
        NODE_ENV: "production"
      }
    }
  ]
};
```

Ensuite, nous l'exécutons simplement avec `pm2 start`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_rYp7NMQTCMmOfBV0w0RTw.png)

pm2 s'exécute maintenant en mode « cluster ». Chacun de ces processus s'exécute sur un CPU différent de ma machine, en fonction du nombre de cœurs que j'ai. Si nous voulons exécuter un processus pour chaque cœur sans savoir combien de cœurs nous avons, nous pouvons simplement passer le paramètre `max` à la valeur `instances`.

```
{
   ...
   instances: "max",
   ...
}
```

Découvrons combien de cœurs j'ai dans cette machine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nhjuG0xFsMgkYB382_xfyw.png)

8 CŒURS ! Mon Dieu. Je vais installer Subnautica sur ma machine fournie par Microsoft. Ne leur dites pas que j'ai dit cela.

Le bon côté d'exécuter des processus sur des CPU séparés est que si vous avez un processus qui s'emballe et prend 100 % du CPU, les autres continueront à fonctionner. Si vous passez plus d'instances que vous n'avez de cœurs, pm2 doublera les processus sur les CPU si nécessaire.

Vous pouvez faire BEAUCOUP plus avec pm2, y compris la surveillance et la gestion de ces variables d'environnement ennuyeuses.

Un autre point à noter : si pour une raison quelconque vous voulez que pm2 exécute votre script `npm start`, vous pouvez le faire en exécutant npm en tant que processus et en passant `-- start`. L'espace avant « start » est super important ici.

```
pm2 start npm -- start
```

Dans [Azure AppService](https://docs.microsoft.com/en-us/azure/app-service/?WT.mc_id=medium-blog-buhollan), nous incluons pm2 par défaut en arrière-plan. Si vous voulez utiliser pm2 dans Azure, vous n'avez pas besoin de l'inclure dans votre fichier `package.json`. Vous pouvez simplement ajouter un fichier ecosystem et vous êtes prêt à partir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TYOm2q57lXad3te35tGwqg.png)

D'accord ! Maintenant que nous avons tout appris sur pm2, parlons de pourquoi vous ne voulez peut-être pas l'utiliser et qu'il pourrait effectivement être acceptable d'exécuter directement contre Node.

#### Exécuter directement contre Node en production

J'avais quelques questions à ce sujet, alors j'ai contacté [Tierney Cyren](https://twitter.com/bitandbang) qui fait partie de l'énorme cercle orange de la connaissance, surtout en ce qui concerne Node.

Tierney a souligné quelques inconvénients à l'utilisation de gestionnaires de processus basés sur Node comme pm2.

La principale raison est que vous ne devriez pas utiliser Node pour surveiller Node. Vous ne voulez pas utiliser la chose que vous surveillez pour surveiller cette chose. C'est un peu comme si vous demandiez à mon fils adolescent de se surveiller lui-même un vendredi soir : cela va-t-il mal se terminer ? Peut-être, et peut-être pas. Mais vous allez le découvrir à vos dépens.

Tierney recommande de ne pas avoir de gestionnaire de processus Node exécutant votre application du tout. Au lieu de cela, avoir quelque chose à un niveau supérieur qui surveille plusieurs instances séparées de votre application. Par exemple, une configuration idéale serait si vous aviez un cluster Kubernetes avec votre application s'exécutant sur des conteneurs séparés. Kubernetes peut alors surveiller ces conteneurs et, si l'un d'eux tombe en panne, il peut les redémarrer et faire un rapport sur leur état de santé.

Dans ce cas, vous **pouvez** exécuter directement contre Node car vous surveillez à un niveau supérieur.

Il s'avère qu'Azure fait déjà cela. Si nous ne poussons pas de fichier ecosystem pm2 vers Azure, il démarrera l'application avec notre script de démarrage du fichier `package.json` et nous pouvons exécuter directement contre Node.

```
"scripts": {
  "start": "node index.js"
}
```

Dans ce cas, nous exécutons directement contre Node et c'est OK. Si l'application devait planter, vous remarquerez qu'elle revient. C'est parce que dans Azure, votre application s'exécute dans un conteneur. Azure orchestre le conteneur dans lequel votre application s'exécute et sait quand il plante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YSvtZOR4DIt1McSdDChVew.png)

Mais vous n'avez toujours qu'une seule instance ici. Il faut quelques secondes au conteneur pour revenir en ligne après un plantage, ce qui signifie qu'il pourrait y avoir quelques secondes d'indisponibilité pour vos utilisateurs.

Idéalement, vous voudriez plus d'un conteneur en cours d'exécution. La solution à cela serait de déployer plusieurs instances de votre application sur plusieurs sites Azure AppService, puis d'utiliser Azure Front Door pour équilibrer la charge des applications derrière une seule adresse IP. Front Door saura quand un conteneur est en panne et redirigera le trafic vers d'autres instances saines de votre application.

[**Azure Front Door Service | Microsoft Azure**](https://azure.microsoft.com/en-us/services/frontdoor/?WT.mc_id=medium-blog-buhollan)
[_Livrez, protégez et suivez les performances de vos applications de microservices distribuées mondialement avec Azure Front Door..._azure.microsoft.com](https://azure.microsoft.com/en-us/services/frontdoor/?WT.mc_id=medium-blog-buhollan)

#### systemd

Une autre suggestion de Tierney était d'exécuter Node avec `systemd`. Je ne comprends pas trop (ou rien du tout) à propos de `systemd` et j'ai déjà mal formulé cela une fois, alors je vais laisser Tierney le dire avec ses propres mots...

> Cette option n'est possible que si vous avez accès à Linux dans votre déploiement et que vous contrôlez la manière dont Node est démarré au niveau du service. Si vous exécutez votre processus Node.js dans une machine virtuelle Linux de longue durée, comme les VM Azure, vous êtes dans un bon endroit pour exécuter Node.js avec systemd. Si vous déployez simplement vos fichiers vers un service comme Azure AppService ou Heroku ou si vous exécutez dans un environnement conteneurisé comme Azure Container Instances, vous devriez probablement éviter cette option.

[**Exécuter votre application Node.js avec Systemd - Partie 1**](https://nodesource.com/blog/running-your-node-js-app-with-systemd-part-1/)
[_Vous avez écrit la prochaine grande application, en Node, et vous êtes prêt à la déchaîner sur le monde. Ce qui signifie que vous pouvez..._nodesource.com](https://nodesource.com/blog/running-your-node-js-app-with-systemd-part-1/)

#### Threads de travail Node.js

Tierney veut également que vous sachiez que les threads de travail arrivent dans Node. Cela vous permettra de démarrer votre application sur plusieurs « workers » (threads), annulant ainsi le besoin de quelque chose comme pm2. Peut-être. Je ne sais pas. Je n'ai pas vraiment lu l'article.

[**Documentation Node.js v11.14.0**](https://nodejs.org/api/worker_threads.html)
[_Le module worker_threads permet l'utilisation de threads qui exécutent JavaScript en parallèle. Pour y accéder : const worker =..._nodejs.org](https://nodejs.org/api/worker_threads.html)

#### Soyez un adulte

La dernière suggestion de Tierney était de simplement gérer l'erreur et d'écrire quelques tests comme un adulte. Mais qui a le temps pour cela ?

#### Le petit cercle persiste

Maintenant, vous savez la plupart de ce qui se trouve dans le petit cercle bleu. Le reste n'est que des faits inutiles sur les groupes emo et la bière.

Pour plus d'informations sur pm2, Node et Azure, consultez les ressources suivantes...

* [http://pm2.keymetrics.io/](http://pm2.keymetrics.io/)
* [Déploiement Node.js sur VS Code](https://code.visualstudio.com/tutorials/nodejs-deployment/getting-started?WT.mc_id=medium-blog-buhollan)
* [Déployer un site Node simple sur Azure](https://azurecasts.com/2019/03/31/002-node-vscode/)