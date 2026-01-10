---
title: Comment contourner le blocage du mode incognito
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T05:34:54.000Z'
originalURL: https://freecodecamp.org/news/disabling-browser-incognito-check-cc84288e89b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BgAlYI-fuv9BrHQHPnNZoQ.jpeg
tags:
- name: hacking
  slug: hacking
- name: incognito
  slug: incognito
- name: JavaScript
  slug: javascript
- name: Tampermonkey
  slug: tampermonkey
- name: Web Development
  slug: web-development
seo_title: Comment contourner le blocage du mode incognito
seo_desc: 'By Mátyás Fodor

  Recently I came across several sites that showed a warning or paywall because I
  was using incognito mode. I think it is unfair. I should be allowed to use whatever
  browser and mode I want. This is a way to enforce their tracking tools...'
---

Par Mátyas Fodor

Récemment, je suis tombé sur plusieurs sites qui affichaient un avertissement ou un paywall parce que j'utilisais le mode incognito. Je trouve cela injuste. Je devrais être autorisé à utiliser le navigateur et le mode que je veux. C'est une façon d'imposer leurs outils de suivi. Je sais que [le mode incognito n'est pas sûr](https://thevpn.guru/is-incognito-mode-safe-secure/), mais c'est le minimum que vous pouvez faire pour éviter que les publicités vous suivent.

Tout cela m'a pris environ deux heures et j'ai beaucoup appris sur les extensions de navigateur et le piratage du code côté client en tant qu'utilisateur final. J'ai pensé que cela pourrait valoir la peine d'être partagé.

Tout d'abord, j'ai dû chercher comment détecter le mode privé. À ma connaissance, il n'existe pas d'API de navigateur pour détecter directement le mode privé, donc j'étais sûr qu'il s'agissait d'un petit script sournois. [Cette](https://stackoverflow.com/a/27805491/2419215) réponse StackOverflow m'a donné un indice, donc je savais que je devrais chercher `webkitRequestFileSystem`. J'ai trouvé [ce](https://gist.github.com/matyasfodor/15e8863ab15baf4791a5fa4c748b64af) morceau dans l'un de ces sites détestant le mode privé, dans leur code JavaScript minifié. Voici la partie excitante :

Je pouvais tester le [module](https://gist.github.com/matyasfodor/15e8863ab15baf4791a5fa4c748b64af) en le collant dans la console de développement d'une fenêtre de navigateur incognito et publique, puis en exécutant :

```
var module = {};incognito(null, module);module.exports.detectIncognito().then(console.log)
```

Bingo ! C'est ça, je dois simplement trouver un moyen de ne pas appeler le callback d'erreur dans `window.webkitRequestFileSystem(..)`. La façon la plus simple est de faire un monkey patch de la fonction :

```
(function(webkitRequestFileSystem) {  window.webkitRequestFileSystem = function(t, s, success, error) {    webkitRequestFileSystem(t, s, success, success);  }})(window.webkitRequestFileSystem);
```

Si vous n'êtes pas familier avec la technique, le [monkey patching](https://www.audero.it/blog/2016/12/05/monkey-patching-javascript/) est un moyen d'ajouter, de modifier ou de supprimer le comportement par défaut d'un morceau de code à l'exécution sans changer son code source original.

**Détour 1 :** Au début, j'ai commencé à écrire ma propre extension Chrome en utilisant [Extensionizr](https://extensionizr.com). C'est un excellent outil qui génère le code de base des extensions Chrome. Mais au final, j'ai trouvé une solution plus facile.

Chaque fois qu'il s'agit de personnaliser des sites web, j'utilise [Tampermonkey](https://tampermonkey.net/) (par exemple, [masquer les annonces d'emploi](https://gist.github.com/rjrudman/a472924d3fb078bd73bb12066e0319a0) sur Stack Overflow quand je ne devrais vraiment pas passer de temps à chercher de nouvelles positions). Vous n'avez pas à installer une n+1ème extension, et cela fournit une interface pratique pour gérer vos scripts. D'accord, pratique est probablement une exagération, c'est moche mais utile.

J'ai donc ajouté le script de monkey patch que j'ai référencé ci-dessus, déjà en rigolant de la facilité avec laquelle c'était fait, mais bummer, cela n'a pas fonctionné. J'ai essayé quelques autres choses, par exemple :

```
window.foobar = 'baz';
```

Mais dans la console de développement, cette propriété était absente de la variable `window`. Il s'est avéré que les [scripts de contenu](https://stackoverflow.com/a/20513730/2419215) s'exécutent dans un environnement isolé, ils ne partagent que le DOM avec les scripts de la page web. J'ai commencé à travailler avec la solution référencée de SO. Il y avait une chose très importante cependant, je devais exécuter ce code avant le code de la page actuelle. Voici ce que j'ai imaginé :

```
function injectScript(file_path, node) {        var element = document.createElement('script');        element.setAttribute('type', 'text/javascript');        element.setAttribute('src', file_path);        element.setAttribute('async', false);        node.appendChild(element);}injectScript(url, document.documentElement);
```

**Détour 2 :** Comme j'ai commencé avec une extension, charger un autre fichier JavaScript était trivial. Cependant, ce n'est pas le cas avec les scripts Tampermonkey (du moins, je ne le sais pas). J'ai donc décidé de mettre mon code dans un gist GitHub, et j'ai essayé de charger le [fichier brut](https://gist.githubusercontent.com/matyasfodor/ab6c92e32a35ebae0bebedff8e7cf569/raw/4f97a8fb702ae8710ba9542b5a7a8127495cf9e4/fakepublic.js). Mais ensuite, le navigateur se plaignait de son type MIME. Finalement, j'ai utilisé [https://rawgit.com/](https://rawgit.com/), qui était exactement l'outil qu'il fallait pour cela.

J'ai réalisé que je devrais ajouter ces quelques lignes de code de monkey patch sous forme de chaîne, et remplir le texte de l'élément script avec cela. Voici ma solution finale :

Une chose importante à savoir si vous travaillez avec Tampermonkey en mode incognito : les modifications que vous apportez en mode incognito n'apparaîtront pas en mode normal, et vice versa : vous devez fermer toutes vos fenêtres privées si vous voulez essayer vos dernières modifications apportées en mode public.

**Attention !** Si vous décidez d'utiliser mon script, vous devez savoir que cela _peut_ (bien que ce ne soit pas très probable) casser certaines pages web. Vous pouvez toujours les désactiver dans Tampermonkey. Utilisez-le à vos propres risques.