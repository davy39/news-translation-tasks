---
title: 'Le nouvel ordre des Mèmes : changer la donne avec un simple cache navigateur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T19:49:43.000Z'
originalURL: https://freecodecamp.org/news/changing-the-meme-game-bcd24a07dc3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sa36HnySp33Inkm62q-Scw.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: memes
  slug: memes
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Le nouvel ordre des Mèmes : changer la donne avec un simple cache navigateur'
seo_desc: 'By Philipp

  Even in 2018, not all humans have access to 3G internet and are trapped inside a
  memeingless world. It’s time to stop this madness.

  In case you are not familiar with the meme concept, a meme is typically an image
  associated with a specific...'
---

Par Philipp

Même en 2018, tous les humains n'ont pas accès à Internet 3G et sont piégés dans un monde sans mèmes. Il est temps de mettre fin à cette folie.

Au cas où vous ne seriez pas familier avec le concept de **mème**, un mème est typiquement une image associée à un contexte ou une idée spécifique.

Ajouter différents textes à ces images — les mèmes — est principalement utilisé comme moyen de ridiculiser le comportement humain ou de décrire des situations. Les mèmes se propagent largement en ligne, notamment via les réseaux sociaux et les plateformes d'images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nw3DnbmpuEBnbtP-gdqyfg.png)
_Votre mème typique de quartier_

### Il y a un problème

Chacun de ces mèmes a été utilisé des millions de fois pour faire des millions de blagues. Actuellement, tous les moteurs de recherche, réseaux sociaux et plateformes d'images chargent chacune de ces images séparément. Cela génère des **mégaoctets** de trafic et nécessite de la capacité de données sur votre téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bt-YmOk2Aa2F4Hbj1FaQIw.png)
_Résultats de recherche pour « Bad Luck Brian »_

### Mon idée

J'ai eu l'idée de sauvegarder une fois les images de mèmes les plus utilisées, puis d'ajouter le reste du texte dynamiquement plus tard.

Cela fonctionne très bien pour les mèmes, car les images restent les mêmes et seul le texte change.

L'énorme avantage est la réduction du transfert de données. Dix à quinze images « normales » peuvent facilement transférer 1 Mo de données. Je peux charger 1000 mèmes et plus avec le même 1 Mo de transfert de données, car le texte brut est beaucoup plus léger que les images.

Ainsi, par exemple, le deuxième mème de cet article Medium est enregistré sous forme d'image et fait plus de **80 ko**, mais pourrait également être enregistré comme suit :

1. **Image :** « success_kid.jpg »

2. **Texte du haut :** « Nuit de beuverie intense »

3. **Texte du bas :** « Réveillé avec les clés, le portefeuille et le téléphone »

Cela nécessiterait seulement **0,1 ko**, à condition que l'image « success_kid.jpg » ait été mise en cache une fois auparavant. Si l'image n'est pas dans le cache du navigateur, elle serait téléchargée une fois. Elle pourrait ensuite être réutilisée indéfiniment sans aucun autre transfert de données.

L'utilisateur bénéficie d'une énorme réduction du temps de chargement et de l'utilisation des données. Avec ce système, peu importe si votre fournisseur mobile a réduit votre bande passante — vous pouvez toujours utiliser des mèmes comme un fou. Le système économise également de l'espace de stockage sur votre téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMaYMU0jYu1hLypBslw_pA.png)
_Chaque « Type XHR » = 15 Mèmes, Document = Code pour la mise en page et la fonctionnalité_

Pour charger **100** mèmes, seulement **15 ko** ont été transférés au total, car les images sont déjà « mises en cache » (« Transféré » **0 o**) et 15 publications nécessitent moins de **1,5 ko** de données. Le site web lui-même fait moins de **10 ko**. J'ai réalisé cela en :

1. **N'utilisant** aucun plug-in/bibliothèque et en écrivant du code natif.

2. **N'utilisant** pas d'images pour créer la mise en page et des images de haute qualité en général.

3. En gardant tout **simple et basique**.

Puisque les mèmes sont si légers, il était logique de garder la mise en page et la fonctionnalité également légères, afin que le site web soit compact et rapide.

Les gens du monde entier ont des problèmes pour charger des pages web car cela prend trop de temps pour les ouvrir. La [page web moyenne fait environ 2 300 ko](https://www.wired.com/2016/04/average-webpage-now-size-original-doom/), et les forums d'images ou les plateformes vidéo sont souvent inaccessibles car le contenu est trop volumineux à télécharger avec une connexion faible ou réduite.

J'espère que ce système de cache aidera en fournissant une alternative qui nécessite moins d'utilisation de données. Il est temps de rendre Internet et la vie des gens plus remplie de mèmes en rendant cette partie de la culture Internet accessible à tous, à tout moment.

Le reste de l'article traite de l'implémentation technique et un peu de moi-même. Si vous souhaitez simplement jeter un coup d'œil au projet, allez sur **CacheMe.me** (assurez-vous de vérifier les outils comme le visionneur de mèmes hors ligne et bien plus encore en ouvrant le Menu (☰) → Gadgets).

### Partie technique

Pour démontrer l'idée, j'ai créé un petit exemple. J'ai utilisé dix mèmes typiques et, après cela, des mèmes infinis avec des nombres générés aléatoirement (personne n'a le temps de générer une infinité d'exemples réels).

**Pour transformer cet exemple en une vraie machine à mèmes**, interrogez une base de données et ajoutez le contenu retourné. Si vous voulez voir des exemples complets, consultez mon [GitHub](https://github.com/Cachememe/Cachememes). Le front-end (HTML, CSS, JS, Kotlin et Swift) sera open source, de toute façon.

#### Front-end

Cet article se **concentrera** sur l'implémentation web du concept. Il existe une application pour Android, mais je n'entrerai pas dans les détails dans cet article. Si vous voulez que j'écrive à ce sujet, laissez un commentaire.

**Html/CSS :** Le `<div>` que j'utilise comme conteneur de mème doit avoir la propriété CSS `position:relative;` pour que le texte soit sur l'image, et `text-align:center` pour aligner le texte au centre (qui l'aurait deviné).

```
/* Classe CSS pour le texte supérieur et inférieur du mème */
.text1, .text2 {
   left: 0;
   font-family: Impact,sans-serif /*sans-serif comme solution de repli*/;
   width: 100%;
   color: white;
   position: absolute;
   z-index: 99;
   pointer-events: none;
   text-align: center;
   -webkit-text-stroke: 1px #000
}
```

Le texte reçoit une `font-family: Impact; color: white; -webkit-text-stroke: 1px #000` pour obtenir le texte stylisé typique des mèmes. L'attribut `position:absolute`, en combinaison avec le conteneur de mème `position:relative`, est utilisé pour obtenir le texte au-dessus de l'image. En ajoutant des attributs comme `z-index:99` et `pointer-events:none`, j'ai fait en sorte que le mème ressemble davantage à une image habituelle.

```
<!-- La structure du Mème dans sa forme naturelle -->
<h2>titre</h2>
<div style="position: relative;text-align: center;">
  <span class="text1">premier texte</span>
  <img src="image_url">
  <span class="text2">second texte</span>
</div>
```

**JavaScript :** Pour obtenir plus de contenu/du contenu infini, j'appelle une fonction dans ce cas avec Ajax/XHR (pour que le site ne se recharge pas). Cela envoie une requête au serveur pour plus de contenu. Si la réponse est au format HTML, je l'ajoute directement comme suit :

```
function get_memes() {
   var xhr = new XMLHttpRequest();
   xhr.open('GET', "url");
   xhr.onload = function () {
     if (xhr.status === 200) {
       // si la réponse est déjà en HTML
       document.getElementsByTagName("body")[0].insertAdjacentHTML("beforeend", xhr.responseText)
     }
   };
   xhr.send();
};
```

Si le `responseText` est au format JSON, je parse d'abord le texte de la réponse, puis je crée du HTML à partir du contenu dans une boucle `for` comme suit :

```
...
var meme_collection = JSON.parse(xhr.responseText)
for (var i = 0; i <= meme_collection.length; i++) {
  var o = '<h2>titre</h2><div style="position: relative;"><span class="text1">'+meme_collection[i]["text1"]+'</span><img src="'+meme_collection[i]["image"]+'"><span class="text2">'+meme_collection[i]["text2"]+'</span></div>'
```

```
  document.getElementsByTagName("body")[0].insertAdjacentHTML("beforeend", o)
}
```

La meilleure partie : je n'ai même pas besoin d'écrire une fonction pour mettre en cache les images, chaque navigateur web le fait par défaut. Vous pouvez simplement réutiliser le même lien d'image et la magie opère déjà.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pAmE_dqKdzDrjO6_deW2vg.png)

#### Backend

L'effet d'économie de données est le résultat de la manière dont le front-end (HTML/XML) est structuré — donc le backend n'est pas vraiment pertinent pour l'effet d'économie de données. Basiquement, un serveur qui retourne des données au format HTML ou JSON (texte du haut, texte du bas, nom de l'image) est tout ce qui est requis.

Pour mon projet, j'ai choisi [**Django**](https://www.djangoproject.com) (un framework web Python). J'ai également intégré un peu de [**Golang**](https://golang.org). Django/Python s'occupe de la plateforme en général (utilisateurs, contenu et HTML) tandis que Golang intervient pour gérer les requêtes API et servir du JSON au client. Les deux langages de programmation travaillent avec la même base de données **PostgreSQL**.

### $whoami

Je m'appelle Philipp, et l'année dernière, j'ai commencé à apprendre à coder en parallèle de mes études. J'ai toujours voulu apprendre à coder, mais j'avais peur du code car je l'imaginais très abstrait et complexe. J'avais en partie raison. Il y a le développement web, mobile et d'applications de bureau, et chacun d'eux nécessite un ensemble de compétences différent. Il existe une tonne de langages, frameworks et bibliothèques différents, et tout le monde recommande d'apprendre quelque chose de différent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZQ-nJEzv6ONWBlfNHFpMZw.png)
_Principaux sujets en programmation et leurs connexions. De [StackOverflow Survey](https://insights.stackoverflow.com/survey/2018/#technology-how-technologies-are-connected" rel="noopener" target="_blank" title=")_

Heureusement, je suis tombé sur [freeCodeCamp](https://www.freecodecamp.org), qui a été un point de départ génial pour apprendre et se lancer dans le codage. Je pouvais décider moi-même quand et où apprendre et, surtout, le parcours de cours clair m'a permis de rester sur la bonne voie pour savoir quoi apprendre ensuite. Cela a toujours aidé de voir que d'autres personnes avaient des problèmes similaires et que je n'étais pas le seul à avoir du mal à résoudre des algorithmes « faciles ».

La communauté freeCodeCamp a été suffisamment soutenante pour me faire traverser ces premières semaines/mois de frustration, et m'a guidé pour commencer des projets par moi-même. Après avoir obtenu mon certificat de front-end, j'ai commencé à me lancer dans Python et après 6 mois, j'ai pu obtenir un poste de Junior Full Stack (à temps partiel puisque je dois finir mes études) dans une jeune entreprise.

Merci à toute la communauté de programmation. Sans freeCodeCamp, StackOverflow et GitHub, je n'en serais pas arrivé là. Merci également à tous mes compagnons humains de mèmes, vos mèmes étaient là quand personne d'autre ne l'était.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqjMpHNELDuu8UzEreH7kQ.png)
_**Le nouvel ordre des Mèmes**_

Pour profiter de quelques Mèmes mis en cache et rejoindre la révolution, rendez-vous sur [CacheMe.me](https://www.cacheme.me) ou téléchargez l'[Application Android](https://play.google.com/store/apps/details?id=com.herokuapp.meme_maschine.low_data) !