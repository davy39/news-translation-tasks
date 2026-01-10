---
title: 'Comment j''ai construit la bibliothèque SiriWaveJS : un regard sur les mathématiques
  et le code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T13:50:53.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-siriwavejs-library-maths-and-code-behind-6971497ae5c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DxOICjfEReAFqCeC5V0oNA.png
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: music
  slug: music
- name: Siri
  slug: siri
- name: 'tech '
  slug: tech
seo_title: 'Comment j''ai construit la bibliothèque SiriWaveJS : un regard sur les
  mathématiques et le code'
seo_desc: 'By Flavio De Stefano

  It was 4 years ago when I had the idea to replicate the Apple® Siri wave-form (introduced
  with the iPhone 4S) in the browser using pure Javascript.

  During the last month, I updated this library by doing a lot of refactoring using...'
---

Par Flavio De Stefano

Cela fait 4 ans que j'ai eu l'idée de répliquer la **forme d'onde** **Apple® Siri** (introduite avec l'iPhone 4S) dans le navigateur en utilisant du Javascript pur.

Au cours du dernier mois, j'ai mis à jour cette bibliothèque en effectuant beaucoup de refactoring en utilisant les fonctionnalités ES6 et j'ai révisé le processus de construction en utilisant **RollupJS**. Maintenant, j'ai décidé de partager ce que j'ai appris pendant ce processus et les mathématiques derrière cette bibliothèque.

Pour avoir une idée du résultat final, visitez l'[**exemple en direct**](http://kopiro.github.io/siriwave/) ; le code source complet est [**ici**](https://github.com/kopiro/siriwave).

De plus, vous pouvez télécharger tous les graphiques dessinés dans cet article au format GCX (format Grapher OSX) : [**default.gcx**](https://github.com/kopiro/siriwave/raw/master/default.gcx) et [**ios9.gcx**](https://github.com/kopiro/siriwave/raw/master/ios9.gcx).

### **Le style classique de l'onde**

![Image](https://cdn-media-1.freecodecamp.org/images/U5DWfdAYQRgGntwYHyJQh2SPSbr2Eals8fD8)
_Style classique_

Initialement, cette bibliothèque n'avait que le style classique de la forme d'onde que vous vous souvenez tous avoir utilisé dans iOS 7 et iOS 8.

Ce n'est pas une tâche difficile de répliquer cette simple forme d'onde, seulement un peu de mathématiques et des concepts de base de l'API Canvas.

![Image](https://cdn-media-1.freecodecamp.org/images/HGJeelo1DbenKSl72V423t-q89s3aBWrLet4)
_Forme d'onde Siri dans iOS 7/8_

Vous pensez probablement que la forme d'onde est une modification de l'équation mathématique **Sinus**, et vous avez raison... enfin, presque raison.

Avant de commencer à coder, nous devons trouver notre équation linéaire qui sera simplement appliquée par la suite. Mon éditeur de graphiques préféré est **Grapher** ; vous pouvez le trouver dans toute installation OSX sous _Applications > Utilitaires > Grapher.app_.

Nous commençons par dessiner la bien connue :

![Image](https://cdn-media-1.freecodecamp.org/images/-OIGYrieegxfDZ-rlhtkXmrrgBv6VgxZnb3f)

![Image](https://cdn-media-1.freecodecamp.org/images/AyYMYn3BxP7KdVZqlLdJ55gcqZHTHB5PFLVi)
_Graphique pour y = sin(x)_

Parfait ! Maintenant, ajoutons quelques paramètres (Amplitude **[A]**, Coordonnée temporelle **[t]** et Fréquence spatiale **[k]**) qui seront utiles plus tard (Lire plus ici : [https://en.wikipedia.org/wiki/Wave](https://en.wikipedia.org/wiki/Wave)).

![Image](https://cdn-media-1.freecodecamp.org/images/tDIRSzaKzb3bBDMJpQ2JfuHxwFPirZliPMV2)

Maintenant, nous devons "atténuer" cette fonction sur les limites du graphique, de sorte que pour **|x| > 2**, les valeurs de y tendent vers 0. Dessinez séparément une équation **g(x)** qui a ces caractéristiques.

![Image](https://cdn-media-1.freecodecamp.org/images/EGqbusNiAWDyno0CSwWWpjmklbWccDUeypq1)

![Image](https://cdn-media-1.freecodecamp.org/images/L68Rd8wjrZV-9X9al6sme2Wi4kt7Z171E6bb)

Cela semble être une bonne équation pour commencer. Ajoutons également quelques paramètres ici pour lisser la courbe à nos fins :

![Image](https://cdn-media-1.freecodecamp.org/images/FWPk14LdAEnYMvGdv-X65IMf8pMPgJx6pO-5)

Maintenant, en multipliant notre **f(x, …)** et **g(x, …)**, et en définissant des paramètres précis pour les autres valeurs statiques, nous obtenons quelque chose comme ceci.

* **A = 0.9** définit l'amplitude de l'onde à Y max = A
* **k = 8** définit la fréquence spatiale et nous obtenons "plus de pics" dans la plage [-2, 2]
* **t = -π/2** définit la translation de phase de sorte que **f(0, …) = 1**
* **K = 4** définit le facteur pour l'équation "d'atténuation" de sorte que l'équation finale est y = 0 lorsque **|x| ≥ 2**

![Image](https://cdn-media-1.freecodecamp.org/images/mI5c-n9vpwQWrtIK2pWz6R3gz6CCrJ0gRQ3s)

Cela a l'air bien ! 💡

Maintenant, si vous remarquez sur l'onde originale, nous avons d'autres sous-ondes qui donneront une valeur plus faible pour l'amplitude. Dessinez-les pour **A = {0.8, 0.6, 0.4, 0.2, -0.2, -0.4, -0.6, -0.8}**

![Image](https://cdn-media-1.freecodecamp.org/images/73RU94BxLIkS49r4TWBmA5IVuQwJAyTYPpF6)

Dans la composition finale du canvas, les sous-ondes seront dessinées avec une opacité décroissante tendant vers 0.

#### Concepts de base du code

Que faisons-nous maintenant avec cette équation ?

Nous utilisons l'équation pour obtenir la **valeur Y** pour une **entrée X**.

En gros, en utilisant une simple **boucle for** de **-2 à 2**, (les _limites du graphique dans ce cas_), nous devons dessiner **point par point** l'équation sur le canvas en utilisant l'API [**beginPath**](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/beginPath) et [lineTo](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineTo).

```
const ctx = canvas.getContext('2d');
```

```
ctx.beginPath();ctx.strokeStyle = 'white';
```

```
for (let i = -2; i <= 2; i += 0.01) {   const x = _xpos(i);   const y = _ypos(i);   ctx.lineTo(x, y);}
```

```
ctx.stroke();
```

Probablement ce pseudo-code éclaircira ces idées. Nous devons encore implémenter nos fonctions **_xpos** et **_ypos**.

Mais… hey, qu'est-ce que **0.01🔥** ? Cette valeur représente **combien de pixels** vous avancez à chaque itération avant d'atteindre la limite droite du graphique… mais quelle est la valeur correcte ?

Si vous utilisez une valeur vraiment petite (**<0.01**), vous obtiendrez un rendu incroyablement précis du graphique, mais vos performances diminueront car vous aurez trop d'itérations.

En revanche, si vous utilisez une valeur vraiment grande (**> 0.1**), votre graphique perdra en précision et vous le remarquerez instantanément.

![Image](https://cdn-media-1.freecodecamp.org/images/3c8OI5O8uiBqD8YUn7bp22xCmxHpCElp8pIh)
_Graphique dessiné avec une précision = 0.2_

Vous pouvez voir que le code final est en fait similaire au pseudo-code : [https://github.com/kopiro/siriwave/blob/master/src/curve.js#L25](https://github.com/kopiro/siriwave/blob/master/src/curve.js#L25)

#### Implémenter _xpos(i)

Vous pourriez argumenter que si nous dessinons le graphique en incrémentant **_x_**, alors **__xpos_** peut simplement retourner l'argument d'entrée.

Cela est presque correct, mais notre graphique est toujours dessiné de **-B** à **B** _(B = Limite = 2)._

Ainsi, pour dessiner sur le canvas via **les coordonnées en pixels**, nous devons traduire **-B en 0**, et **B en 1** (simple transposition de [-B, B] en [0,1]) ; puis multiplier [0,1] et la **largeur du canvas (w)**.

> _xpos(i) = w * [ (i + B) / 2B ]

[https://github.com/kopiro/siriwave/blob/master/src/curve.js#L19](https://github.com/kopiro/siriwave/blob/master/src/curve.js#L19)

#### **Implémenter _ypos**

Pour implémenter **_ypos**, nous devrions simplement écrire notre équation obtenue précédemment (de près).

```
const K = 4;const FREQ = 6;
```

```
function _attFn(x) {   return Math.pow(K / (K + Math.pow(x, K)), K);}
```

```
function _ypos(i) {   return Math.sin(FREQ * i - phase) *       _attFn(i) *       canvasHeight *      globalAmplitude *       (1 / attenuation);}
```

Clarifions quelques paramètres.

* **canvasHeight** est la hauteur du Canvas exprimée en PX
* **i** est notre valeur d'entrée (le **x**)
* **phase** est le paramètre le plus important, discutons-en plus tard
* **globalAmplitude** est un paramètre statique qui représente l'amplitude de l'onde totale (composée de sous-ondes)
* **attenuation** est un paramètre statique qui change pour chaque ligne et représente l'amplitude d'une onde

[https://github.com/kopiro/siriwave/blob/master/src/curve.js#L24](https://github.com/kopiro/siriwave/blob/master/src/curve.js#L24)

#### **Phase**

Maintenant, discutons de la **variable de phase** : c'est la **première variable changeante** au fil du temps, car elle simule le mouvement de l'onde.

Que signifie-t-il ? Cela signifie que **pour chaque _frame d'animation_**, notre contrôleur de base devrait **incrémenter** cette valeur. Mais pour éviter que cette valeur ne provoque un débordement de tampon, faisons un modulo avec 2π (puisque le domaine de **Math.sin** est déjà modulo 2π).

```
phase = (phase + (Math.PI / 2) * speed) % (2 * Math.PI);
```

Nous multiplions **speed** et **Math.PI** de sorte qu'avec **speed = 1**, nous avons la vitesse maximale (pourquoi ? parce que **sin(0) = 0, sin(π/2) = 1, sin(π) = 0, … 💡**)

#### Finalisation

Maintenant que nous avons tout le code pour dessiner une seule ligne, nous définissons un tableau de configuration pour dessiner toutes les sous-ondes, puis nous les parcourons.

```
return [   { attenuation: -2, lineWidth: 1.0, opacity: 0.1 },   { attenuation: -6, lineWidth: 1.0, opacity: 0.2 },   { attenuation: 4, lineWidth: 1.0, opacity: 0.4 },   { attenuation: 2, lineWidth: 1.0, opacity: 0.6},
```

```
   // ligne de base   { attenuation: 1, lineWidth: 1.5, opacity: 1.0},];
```

[https://github.com/kopiro/siriwave/blob/master/src/siriwave.js#L190](https://github.com/kopiro/siriwave/blob/master/src/siriwave.js#L190)

### Le style iOS 9+

![Image](https://cdn-media-1.freecodecamp.org/images/KAVRuTjxVxZvEQEIyG2xru3yzDpLZWvd8zdO)
_GIF de SiriwaveJS iOS9+_

Maintenant, les choses commencent à se compliquer. Le style introduit avec iOS 9 est vraiment complexe et l'ingénierie inverse pour le simuler **n'est pas du tout facile** ! Je ne suis pas entièrement satisfait du résultat final, mais je continuerai à l'améliorer jusqu'à obtenir le résultat souhaité.

Comme précédemment, commençons par obtenir les équations linéaires des ondes.

![Image](https://cdn-media-1.freecodecamp.org/images/kxsuU2ovEPmN0mqiOwoWM3dHUYmG4wnRAQpc)
_Forme d'onde Siri originale iOS 9+_

Comme vous pouvez le remarquer :

* nous avons trois **équations spéculaires différentes** avec différentes couleurs (**vert, bleu, rouge**)
* une seule onde semble être une **somme d'équations sinusoïdales** avec **différents paramètres**
* toutes les autres couleurs sont une **composition** de ces trois couleurs de base
* il y a une **ligne droite** aux limites du graphique

En reprenant nos équations précédentes, définissons une équation plus complexe qui **implique une translation**. Nous commençons par définir à nouveau notre équation d'atténuation :

![Image](https://cdn-media-1.freecodecamp.org/images/PFv-Gz5oeue1rG-Wg06zngdoCsTpTPM83k6c)

Maintenant, définissons la fonction **h(x, A, k, t)**, qui est la **fonction sinus** multipliée par la **fonction d'atténuation**, dans sa valeur absolue :

![Image](https://cdn-media-1.freecodecamp.org/images/77pEjutms8rTTvzBaxAIX0dFAyqp6C5pChFp)

![Image](https://cdn-media-1.freecodecamp.org/images/gICWeQIDSMxE5jJMSZ2WQv6Kg5zmRQPT54tl)

Nous avons maintenant un outil puissant.

Avec **h(x)**, nous pouvons maintenant créer la forme d'onde finale en sommant différentes **h(x)** avec différents paramètres impliquant différentes amplitudes, fréquences et translations. Par exemple, définissons la **courbe rouge** en mettant des valeurs aléatoires.

![Image](https://cdn-media-1.freecodecamp.org/images/hbal1DKzau5IyTSD4DaTdYc8pJpr3xZqd8Si)

![Image](https://cdn-media-1.freecodecamp.org/images/pLT6aOYpEHowx2xYoKy3Iqve6cqC9z4YADZ9)

Si nous faisons de même avec une courbe **verte** et **bleue**, voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/QAB6jCDUoq4uzllkLTbhIhKa0XCecjennMZL)

Ce n'est pas tout à fait parfait, mais cela pourrait fonctionner.

Pour obtenir la version spéculaire, il suffit de multiplier le tout par **-1.**

Côté codage, l'approche est la même, nous avons simplement une équation plus complexe pour **_ypos.**

```
const K = 4;const NO_OF_CURVES = 3;
```

```
// Ces paramètres doivent être générés aléatoirementconst widths = [ 0.4, 0.6, 0.3 ];const offsets = [ 1, 4, -3 ];const amplitudes = [ 0.5, 0.7, 0.2 ];const phases = [ 0, 0, 0 ];
```

```
function _globalAttFn(x) {   return Math.pow(K / (K + Math.pow(x, 2)), K);}
```

```
function _ypos(i) {   let y = 0;   for (let ci = 0; ci < NO_OF_CURVES; ci++) {      const t = offsets[ci];      const k = 1 / widths[ci];      const x = (i * k) - t;            y += Math.abs(         amplitudes[ci] *          Math.sin(x - phases[ci]) *          _globalAttFn(x)      );   }
```

```
   y = y / NO_OF_CURVES;   return canvasHeightMax * globalAmplitude * y;}
```

Il n'y a rien de complexe ici. La seule chose qui a changé est que nous parcourons **NO_OF_CURVES** fois tous les paramètres pseudo-aléatoires et nous **sommons** toutes les valeurs **y.**

Avant de multiplier par **canvasHeightMax** et **globalAmplitude** qui nous donnent la coordonnée PX absolue du canvas, nous divisons par NO_OF_CURVES de sorte que **y est toujours ≤ 1.**

[https://github.com/kopiro/siriwave/blob/master/src/ios9curve.js#L103](https://github.com/kopiro/siriwave/blob/master/src/ios9curve.js#L103)

#### **Opération composite**

Une chose qui compte vraiment ici est le mode **globalCompositeOperation** à définir dans le Canvas. Si vous remarquez, dans le contrôleur original, lorsqu'il y a un chevauchement de 2+ couleurs, elles sont en fait mélangées de manière standard.

Le mode par défaut est **source-over**, mais le résultat est médiocre, même avec une opacité définie.

![Image](https://cdn-media-1.freecodecamp.org/images/fR8PeyeFbcJq-8Qycopohv6M1hfIK4Zudjal)
_opération composite : source-over_

Vous pouvez voir tous les exemples de **globalCompositeOperation** ici : [https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation)

En définissant **globalCompositeOperation** sur **"lighter"**, vous remarquerez que l'intersection des couleurs est plus proche de l'original.

![Image](https://cdn-media-1.freecodecamp.org/images/I5HGeo9b8U3bmt1XquQiRsdohkUZeRzIFE3x)
_Opération composite : lighter_

### Construction avec RollupJS

Avant de tout refactoriser, je n'étais pas du tout satisfait de la base de code : des classes de type prototype ancien, un seul fichier Javascript pour tout, pas d'uglify/minify et **pas de build du tout.**

En utilisant les nouvelles fonctionnalités ES6 comme **les classes natives, les opérateurs de propagation** et **les fonctions lambda**, j'ai pu tout nettoyer, diviser les fichiers et réduire les lignes de code inutiles.

De plus, j'ai utilisé [RollupJS](https://rollupjs.org/) pour créer une build transpilée et minifiée dans divers formats.

Puisque cette bibliothèque est uniquement pour les navigateurs, j'ai décidé de créer deux builds : un build **UMD (Universal Module Definition)** que vous pouvez utiliser directement en important le script ou en utilisant un CDN, et un autre en tant que module **ESM.**

Le module UMD est construit avec cette configuration :

```
{   input: 'src/siriwave.js',   output: {      file: pkg.unpkg,      name: pkg.amdName,      format: 'umd'    },    plugins: [       resolve(),       commonjs(),       babel({ exclude: 'node_modules/**' }),    ]}
```

Un module **UMD minifié** supplémentaire est construit avec cette configuration :

```
{   input: 'src/siriwave.js',   output: {      file: pkg.unpkg.replace('.js', '.min.js'),      name: pkg.amdName,      format: 'umd'    },    plugins: [       resolve(),       commonjs(),       babel({ exclude: 'node_modules/**' }),       uglify()]}
```

En bénéficiant du service UnPKG, vous pouvez trouver la build finale sur cette URL servie par un CDN : [https://unpkg.com/siriwave/dist/siriwave.min.js](https://unpkg.com/siriwave/dist/siriwave.min.js)

C'est la manière "ancienne" de Javascript — vous pouvez simplement importer votre script et ensuite vous y référer dans votre code en utilisant l'objet global **SiriWave.**

Pour fournir une manière plus élégante et moderne, j'ai également construit un module ESM avec cette configuration :

```
{    input: 'src/siriwave.js',   output: {       file: pkg.module,       format: 'esm'   },    plugins: [       babel({ exclude: 'node_modules/**' })   ]}
```

Nous ne voulons clairement pas les plugins **resolve** ou **commonjs** de RollupJS car le transpileur du développeur résoudra les dépendances pour nous.

Vous pouvez trouver la configuration finale de RollupJS ici : [https://github.com/kopiro/siriwave/blob/master/rollup.config.js](https://github.com/kopiro/siriwave/blob/master/rollup.config.js)

#### **Surveillance et rechargement à chaud du code**

En utilisant RollupJS, vous pouvez également tirer parti des plugins **rollup-plugin-livereload** et **rollup-plugin-serve** pour fournir une meilleure façon de travailler sur les scripts.

En gros, vous ajoutez simplement ces plugins lorsque vous êtes en mode "développeur" :

```
import livereload from 'rollup-plugin-livereload';import serve from 'rollup-plugin-serve';
```

```
if (process.env.NODE_ENV !== 'production') { additional_plugins.push(  serve({   open: true,   contentBase: '.'  }) ); additional_plugins.push(  livereload({   watch: 'dist'  }) );}
```

Nous terminons en ajoutant ces lignes dans le **package.json** :

```
"module": "dist/siriwave.m.js","jsnext:main": "dist/siriwave.m.js","unpkg": "dist/siriwave.js","amdName": "SiriWave","scripts": {   "build": "NODE_ENV=production rollup -c",   "dev": "rollup -c -w"},
```

Clarifions quelques paramètres :

* **module / jsnext:main** : chemin du module ESM dist
* **unpkg** : chemin du module UMD dist
* **amdName** : nom de l'objet global dans le module UMD

Un grand merci à **RollupJS** !

J'espère que vous trouverez cet article intéressant, à bientôt ! 💡