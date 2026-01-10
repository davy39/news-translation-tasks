---
title: Commencez avec WebAssembly — en utilisant seulement 14 lignes de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T08:28:06.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-webassembly-using-only-14-lines-of-javascript-b37b6aaca1e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sHlMI2kxKBlm76U2Gmt2Cw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Commencez avec WebAssembly — en utilisant seulement 14 lignes de JavaScript
seo_desc: 'By Daniel Simmons

  WebAssembly is a brand new web technology with massive potential. It will have a
  significant impact on how web applications are developed in the future.

  But, sometimes, I feel like it just doesn’t want to be understood… almost in a ...'
---

Par Daniel Simmons

[WebAssembly est une toute nouvelle technologie web](https://www.youtube.com/watch?v=6v4E6oksar0&t=241s) avec un potentiel énorme. Elle aura un impact significatif sur la manière dont les applications web seront développées à l'avenir.

Mais, parfois, j'ai l'impression qu'elle ne veut tout simplement pas être comprise… presque d'une manière étrangement passive-agressive.

Lorsque je regarde la documentation et les quelques tutoriels qui existent déjà, je ne peux m'empêcher de me sentir comme un agriculteur qui a prié pour la pluie, pour finalement se noyer dans une inondation. J'ai techniquement obtenu ce que je voulais… juste pas de la manière que j'espérais. « Tu veux de la pluie ?! Oh, je vais te donner de la **pluie** ! »

C'est parce que WebAssembly rend tant de nouvelles choses possibles et peut être implémentée de tant de manières différentes. Mais, elle a tellement changé au cours de son développement jusqu'à sa [version MVP officielle en février](http://webassembly.org/roadmap/), que lorsque vous commencez à l'apprendre, il est facile de se noyer dans un océan de détails.

En continuant la métaphore de la pluie, cet article est ma tentative de fournir une légère averse d'introduction à WebAssembly. Pas les concepts ou les détails techniques, mais l'implémentation réelle.

Je vais vous guider à travers les étapes pour créer et implémenter un projet extrêmement simple, en supprimant la complexité partout où c'est possible. Après l'avoir implémenté une fois, même simplement, beaucoup de ces idées de haut niveau sont beaucoup plus faciles à comprendre.

#### Décomposons cela

Tout sera beaucoup plus clair si nous faisons un pas en arrière et regardons une liste des étapes impliquées dans l'implémentation de WebAssembly dans un projet.

Lorsque vous commencez, il est facile de regarder WebAssembly et de ne voir qu'un gros tas d'options et de processus. Le décomposer en étapes discrètes nous aidera à avoir une image claire de ce qui se passe :

1. **Écrire** : Écrivez quelque chose (ou utilisez un projet existant) en C, C++ ou Rust
2. **Compiler** : Compilez-le en WebAssembly (ce qui vous donne un fichier binaire .wasm)
3. **Inclure** : Obtenez ce fichier .wasm dans un projet
4. **Instancier** : Écrivez un ensemble de JavaScript asynchrone qui compilera le binaire .wasm et l'instanciera en quelque chose avec lequel JS peut interagir facilement.

Et c'est à peu près tout. Certes, il existe différentes permutations de ce processus, mais c'est l'essentiel.

De manière générale, ce n'est pas si compliqué. Cependant, cela _peut_ devenir extrêmement compliqué, car la plupart de ces étapes permettent des degrés de complexité très variables. Dans chaque cas, je vais opter pour la simplicité la plus basique.

Pour notre projet, nous allons écrire une fonction simple en C++ (ne vous inquiétez pas si vous n'êtes pas familier avec le C++, elle sera _extrêmement_ simple). La fonction retournera le carré d'un nombre donné.

Ensuite, nous allons le compiler en .wasm en utilisant un outil en ligne (vous n'aurez pas besoin de télécharger ou d'utiliser des utilitaires en ligne de commande). Ensuite, nous allons l'instancier avec 14 lignes de JS.

Lorsque nous aurons terminé, vous pourrez appeler une fonction écrite en C++ comme si c'était une fonction JS, et vous serez émerveillé !

Le nombre de possibilités que cela ouvre est absolument époustouflant.

#### Écrire

Commençons par notre code C++. Souvenez-vous, nous n'utiliserons pas d'environnement de développement local pour écrire ou compiler cela.

Au lieu de cela, nous utiliserons un outil en ligne appelé [WebAssembly Explorer](https://mbebenita.github.io/WasmExplorer/). C'est un peu comme CodePen pour WebAssembly, et il vous permet de compiler votre code C ou C++ directement dans le navigateur et de télécharger un fichier .wasm, le tout en un seul endroit.

Une fois que vous avez ouvert WebAssembly Explorer, tapez ce code C++ dans la fenêtre la plus à gauche :

```
int squarer(int num) {  return num * num;}
```

Comme je l'ai dit, nous utilisons un exemple vraiment simple ici. Même si vous n'avez jamais regardé du C ou du C++ auparavant, il n'est probablement pas trop difficile de comprendre ce qui se passe.

#### Compiler

Ensuite, cliquez sur le bouton qui dit « compile » dans la barre rouge au-dessus de votre code C++. Voici ce que vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KAAS0TC2K5c2xkBiaWNNjg.png)

La colonne du milieu vous montre une version lisible par l'homme du binaire .wasm que vous venez de créer. Cela s'appelle « WAT » ou [WebAssembly Text Format](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format).

À droite se trouve le code assembleur résultant. Plutôt cool.

Je ne vais pas entrer dans les détails de l'un ou l'autre, mais vous devez connaître au moins un peu le fichier WAT afin de suivre les étapes suivantes.

WAT existe parce que nous, les humains, avons généralement du mal à comprendre le binaire pur. C'est essentiellement une couche d'abstraction qui vous aide à comprendre et à interagir avec votre code WebAssembly.

Dans notre cas, ce que nous voulons comprendre, c'est comment notre WebAssembly fait référence à la fonction que nous venons de créer. Cela parce que nous devrons utiliser exactement le même nom dans notre fichier JS plus tard pour y faire référence.

Toutes les fonctions que vous écrivez dans votre code C++ seront disponibles dans WebAssembly sous forme de ce qu'on appelle une « exportation ». Nous en parlerons un peu plus tard, mais pour l'instant, tout ce que vous devez savoir, c'est que les exportations sont les choses avec lesquelles vous pourrez interagir et que vous pourrez utiliser.

Jetez un coup d'œil au fichier WAT et cherchez le mot « export ». Vous le verrez deux fois : une fois à côté du mot `memory` et une autre fois à côté du mot `_Z7squareri`. Nous n'avons pas besoin de connaître `memory` pour l'instant, mais nous sommes définitivement intéressés par `_Z7squareri`.

Nous avons utilisé le nom de fonction `squarer` dans notre C++, mais maintenant cela est devenu `_z7squareri`. Cela peut définitivement être déroutant la première fois que vous le voyez.

Pour autant que je sache, le préfixe « _Z7 » et le suffixe « i » sont des [marqueurs de débogage](https://docs.microsoft.com/en-us/cpp/build/reference/z7-zi-zi-debug-information-format) introduits par le compilateur C++. Ce n'est pas vraiment important de comprendre en profondeur, cependant. Vous devez simplement être conscient que cela se produira, car vous devez utiliser ce nom exact dans votre fichier JS afin d'appeler votre fonction C++.

#### Inclure

Maintenant, cliquez simplement sur le bouton « download » en haut de la section WAT violette. Vous obtiendrez le fichier binaire .wasm. Renommez-le `squarer.wasm`. Ensuite, créez un nouveau répertoire et placez votre fichier `squarer.wasm` dedans, ainsi que deux autres fichiers :

* `index.html` (boilerplate)
* `scripts.js` (vide pour l'instant)

#### Instancier

Maintenant, la partie délicate. Ou, du moins, la partie qui m'a causé beaucoup de confusion lorsque j'ai commencé à parcourir la documentation.

Bien que vous puissiez éventuellement inclure des modules .wasm comme un bon vieux module ES6 (en utilisant `<script type='module'>`), pour l'instant, vous devez le « configurer manuellement ». Cela se fait en effectuant une série d'appels asynchrones à l'API WebAssembly. Il y a trois étapes :

* Obtenez votre fichier binaire .wasm dans un **tampon de tableau***
* Compilez les octets en un **module WebAssembly***
* **Instanciez** le module WebAssembly

Si tout cela vous semble clair, vous pouvez passer à la section suivante. Mais si vous vous êtes gratté la tête et souhaitez une explication plus détaillée, continuez à lire.

#### *Tampon de tableau

Un tampon est un endroit de stockage temporaire pour les données pendant qu'elles sont déplacées. Généralement, cela est utile lorsque les données sont reçues et traitées à des rythmes différents.

Par exemple, lorsqu'une vidéo est en tampon, les données sont reçues à un rythme plus lent que celui auquel le lecteur vidéo peut les lire. L'une des choses que fait notre tampon de tableau est de mettre en file d'attente nos données binaires afin qu'elles puissent être compilées plus facilement.

Mais il se passe autre chose de très important ici. En JavaScript, un tampon de tableau est un [tableau typé](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays), qui est quelque chose utilisé spécifiquement pour stocker des données binaires.

Le fait qu'il soit explicitement typé signifie que le moteur JS peut interpréter un tampon de tableau beaucoup plus rapidement qu'un tableau régulier, car il connaît déjà le type de données et n'a pas à passer par le processus de le déterminer.

#### *Module WebAssembly

Une fois que vous avez toutes vos données binaires dans un tampon de tableau, vous pouvez les compiler en un module. Le module WebAssembly est, en lui-même, inerte. Ce n'est que le binaire compilé, en attente que quelque chose soit fait avec.

Vous pouvez presque penser au module comme à une recette de gâteau. La recette est juste un format pour stocker des informations sur la façon de faire un gâteau. Si vous voulez vraiment un gâteau, vous devez créer une instance du gâteau décrit dans la recette (instancier le gâteau).

Vous faites cela en suivant les instructions énoncées dans la recette. Alternativement, vous pourriez envoyer la recette à quelqu'un d'autre (un « service worker »), ou vous pourriez la sauvegarder et l'utiliser plus tard (« cache »). Les deux sont beaucoup plus pratiques à faire avec une recette, qu'avec un vrai gâteau.

#### *Instancier

La dernière chose que vous devez faire est de créer une instance de votre module WebAssembly, ce qui « lui donne vie » et le rend réellement utilisable.

L'instance vous donne accès aux exportations du module (vous vous souvenez de cela dans notre fichier WAT ?). Il s'agit d'un objet qui contient :

* Mémoire (pas pertinent pour nous, mais vous pouvez en lire plus [ici](https://hacks.mozilla.org/2017/02/creating-and-working-with-webassembly-modules/))
* Toutes les fonctions qui étaient présentes dans votre code C++. C'est ainsi que vous utiliserez la fonction C++ que vous avez écrite.

#### Terminez et exécutez-le !

Voici le code qui accomplit toutes les étapes que nous venons de passer en revue (celui-ci va dans votre fichier `scripts.js`) :

La fonction `loadWebAssembly()` récupère votre fichier .wasm puis effectue les opérations mentionnées ci-dessus. Ensuite, elle retourne une nouvelle instance de votre module WebAssembly.

Notre fonction C++ (souvenez-vous qu'elle est référencée par le nom étrange que nous avons mentionné précédemment : `_z7squareri`) se trouve dans la propriété exports de notre instance. Vous pouvez la voir être assignée à la variable globale `squarer` à la ligne 12. Maintenant, nous pouvons utiliser `squarer()` comme une fonction JavaScript régulière !

Une fois que vous avez mis cela dans votre fichier `scripts.js` et que vous avez enregistré, vous pouvez l'ouvrir sur localhost et vous devriez voir le message « Fin de la compilation… » dans la console.

Maintenant, appelez simplement votre fonction et passez un argument depuis la console. Essayez quelque chose comme `squarer(9)`. Appuyez sur Entrée et vous verrez `81`. Cela fonctionne ! Vous appelez une fonction écrite en C++ !

![Image](https://cdn-media-1.freecodecamp.org/images/1*nMZGPLafGLLuEombmJ4LPg.png)

### C'est fantastique

Vous pouvez simplement imaginer toutes les choses que cela rend possibles.

Tout d'abord, JavaScript n'est plus votre seule option pour « faire des choses » dans le navigateur. C'est absolument énorme.

Ensuite, il y a les améliorations de performance, puisque WebAssembly, contrairement à JS, s'exécute à une vitesse quasi native.

Et puis il y a tout le code hérité qui est maintenant à votre disposition. Le C et le C++ existent depuis longtemps, et pendant ce temps, beaucoup de personnes brillantes ont créé des projets open-source incroyables avec. Des projets qui peuvent maintenant être intégrés dans des sites web ou des applications.

À partir de là, vous pouvez écrire du code C, C++ ou Rust plus complexe, ou même adapter un projet existant, et le « wasm-iser » dans un projet web.

Un bémol, cependant, est que si vous souhaitez créer des fonctions qui acceptent des arguments ou retournent des valeurs qui ne sont pas des nombres, alors les choses commencent à devenir un peu plus compliquées. C'est à ce moment-là que vous devrez en apprendre un peu plus sur l'attribut mémoire des exportations de l'instance .wasm.

Ce projet est [disponible sur GitHub](https://github.com/lordpoint/wasm-demo) si vous souhaitez simplement cloner une copie fonctionnelle en plus de suivre l'article.