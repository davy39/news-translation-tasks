---
title: Cinq commentaires de code que vous devriez arrêter d'écrire // et un que vous
  devriez commencer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T22:44:58.000Z'
originalURL: https://freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PIFH2fl9dk8fvWJy8ynvgA.png
tags:
- name: clean code
  slug: clean-code
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Cinq commentaires de code que vous devriez arrêter d'écrire // et un que
  vous devriez commencer
seo_desc: 'By Alon Kiriati

  With examples from your favorite and most popular open source projects — React,
  Angular, PHP, Pandas and more!

  The correlation between code quality and comments

  One of the first things we were taught in college was that comments are e...'
---

Par Alon Kiriati

Avec des exemples de vos projets open source préférés et les plus populaires — React, Angular, PHP, Pandas et plus encore !

### La corrélation entre la qualité du code et les commentaires

L'une des premières choses qu'on nous a enseignées à l'université était que les commentaires sont essentiels. On nous a également enseigné qu'il existe une corrélation entre la qualité du code et le nombre de commentaires qu'un code contient — plus vous avez de commentaires, meilleur est votre code. On nous a formés à croire que les commentaires racontent l'histoire du programme que nous écrivons, et qu'ils expriment ce que le code ne peut pas fournir. Nous avons appris que le langage humain est mieux lu par les humains, tandis que le langage machine est mieux lu par les machines.

De plus, cet enseignement n'était pas suffisant et nous étions "punis" pour avoir rendu des devoirs sans commentaires en voyant quelques points déduits de nos notes. Si vous parveniez somehow à éviter les vérifications humaines, votre manque de commentaires était détecté par des scripts conçus pour vérifier cela.

### Peut-être que la corrélation est inverse

En acquérant plus d'expérience, j'ai réalisé que non seulement l'inverse peut être vrai — il est possible qu'il existe une corrélation inverse entre un bon code et le nombre de commentaires que le code contient. Il y a deux raisons principales pour lesquelles cela peut se produire :

1. Trop souvent, les commentaires ne sont qu'une excuse pour écrire un mauvais code. Au lieu d'écrire un bon code, les programmeurs croient que s'ils écrivent du code sale avec quelques hacks bizarres, et le décrivent avec 5 lignes de commentaires — que le code est lisible et bien écrit. Je suis en désaccord — le code est en fait toujours mauvais. Si votre collègue doit lire une longue histoire commentée pour la comprendre, alors vous vous y prenez mal. Si votre code n'est pas auto-explicatif, il est préférable de l'améliorer et de ne pas utiliser de commentaires pour le décrire.
2. Les commentaires se dégradent avec le temps, ce qui les rend incorrects et trompeurs. Ils ne sont vrais que lorsqu'ils sont écrits, et même alors, ils ne peuvent pas être appliqués efficacement. Avec le temps, les gens apporteront inévitablement des modifications logiques, changeront des types et déplaceront des éléments. Certains d'entre eux remarqueront le commentaire qui doit être modifié, et d'autres non. Même si vous trouvez somehow un moyen d'établir une discipline très rigide autour de la mise à jour des commentaires lorsque le code change, cela se brisera la première fois que vous effectuerez un refactoring automatique. Pensez à un refactoring qui ajoute un paramètre à une fonction centrale utilisée plus de 250 fois — voulez-vous vraiment aller et modifier manuellement tous ces commentaires ?

![Image](https://cdn-media-1.freecodecamp.org/images/7YrMu1H2zUOi2iRAJC9k38eT3ARmfCC9HDhw)
_[www.imagewishes.com](http://www.imagewishes.com" rel="noopener" target="_blank" title=")_

### Quels sont les commentaires les plus courants que vous devriez essayer d'éviter ?

Tout cela ne signifie pas que vous devriez arrêter d'écrire des commentaires immédiatement ou essayer de réduire le nombre de commentaires que vous avez à tout prix. Je ne recommanderais pas non plus de parcourir votre code et d'essayer de nettoyer tous les commentaires inutiles ou trompeurs — cela prendrait trop de temps et votre temps est mieux utilisé ailleurs. Au lieu de cela, je recommanderais d'être plus réfléchis avant d'ajouter votre prochain commentaire et de vous poser ces trois questions :

1. Ce commentaire est-il vraiment nécessaire et quelle valeur ajoute-t-il ?
2. Existe-t-il un moyen d'améliorer le code pour que ce commentaire soit inutile ?
3. Est-ce que je ne fais que couvrir mes arrières en ajoutant ce commentaire ?

Pour vous aider, j'ai identifié les 5 pires commentaires que j'ai vus au fil du temps — ces types de commentaires devraient soulever un drapeau rouge avant de les ajouter. J'ai utilisé certains projets open source très courants pour obtenir des exemples. Ne vous méprenez pas, je ne pense pas que ces projets soient mal écrits. Au contraire, ce sont mes projets préférés. Mais rien dans la vie n'est parfait ; tout code peut être amélioré.

#### 1. Énoncer l'évidence

Ce sont des commentaires qui expliquent ce que fait votre code. Vous en avez probablement vu certains :

Un exemple de [react.js](https://github.com/facebook/react/blob/master/scripts/jest/noHaste.js#L5) :

```js
getHasteName() {
   // Nous ne voulons jamais Haste.
   return null;
}
```

Et un autre de [vscode](https://github.com/Microsoft/vscode/blob/master/src/cli.js#L11) :

```js
// Éviter les Monkey Patches d'Application Insights
bootstrap.avoidMonkeyPatchFromAppInsights();
// Activer le support portable
bootstrap.configurePortable();
// Activer le support ASAR
bootstrap.enableASARSupport();
// Charger le CLI via le chargeur AMD
require('./bootstrap-amd').load('vs/code/node/cli');
```

Croyez-le ou non, les personnes qui lisent votre code sont elles-mêmes des codeurs. Il est fortement probable qu'elles travaillent dans la même entreprise que vous ou sur le même projet. Elles ont un certain contexte et sont assez intelligentes (espérons... si vous pensez être entouré d'idiots, vous pourriez envisager de mettre à jour votre Linkedin). Elles peuvent lire du code, même sans notes de bas de page. Si vos variables, fonctions et classes ont des noms significatifs, alors ne les encombrez pas avec des explications inutiles qui seront obsolètes lors de la prochaine modification ou refactorisation du code.

Avis de non-responsabilité : Comme beaucoup d'autres, j'ai une cécité aux commentaires. J'ignore les commentaires et ne remarquerai probablement jamais qu'il y avait un commentaire qui devait être mis à jour lors de la modification ou de la refactorisation du code.

Revenons à l'exemple — que se passe-t-il si nous supprimons tous les commentaires dans le code ci-dessus ? Serait-il vraiment beaucoup plus difficile à lire ?

#### 2. Expliquer votre code

Si votre code est propre et utilise le bon niveau d'abstraction, vous n'avez pas besoin d'expliquer ce qu'il fait. Si vous vous retrouvez toujours à expliquer le code, cela peut être le résultat d'une habitude que vous avez prise au fil des années. Vous pourriez envisager de vous en débarrasser, ou de devoir supporter un code qui n'est pas auto-expressif.

Regardez ce code de [react.js](https://github.com/facebook/react/blob/master/dangerfile.js#L35) :

```js
if (!existsSync('./scripts/rollup/results.json')) {
  // Cela indique que la construction a échoué précédemment.
  // Dans ce cas, il n'y a rien à faire pour le Dangerfile.
  // Quittez tôt pour éviter de laisser un commentaire PR redondant (et potentiellement confus).
  process.exit(0);
}
```

Ne serait-ce pas plus propre si nous le refactorions comme ceci :

```js
if (buildFailedPreviously())
  process.exit(0);
```

Un autre exemple courant peut être le nommage ; soit des fonctions, des variables ou des classes. Un bon nommage est l'une des choses les plus difficiles à faire, mais cela ne signifie pas que nous devons lever un drapeau blanc sans condition et utiliser des commentaires pour décrire ce que fait notre code. Regardez ce code de [php](https://github.com/php/php-src/blob/master/main/alloca.c#L226) :

```php
struct stack_control_header
{ 
  long shgrow:32;    /* Nombre de fois où la pile a grandi.  */
  long shaseg:32;    /* Taille des incréments de la pile.  */
  long shhwm:32;     /* Marque de haut niveau de la pile.  */
  long shsize:32;    /* Taille actuelle de la pile (tous les segments).  */
};
```

Si vous le passez et essayez de l'utiliser, vous ne comprendrez peut-être pas immédiatement ce que sont shgrow, shaseg et d'autres champs. Et si nous l'écrivions de cette manière :

```
struct stack_control_header
{
  long num_of_time_grown:32;
  long size_of_inc:32;
  long high_water_mark:32;
  long current_size:32;
};
```

Vous voyez ? Bien mieux. Le lecteur peut mieux comprendre ce que fait chaque champ sans avoir besoin de sauter à la définition de la structure et de lire les commentaires.

#### 3. Commentaires longs

Les commentaires longs utilisés pour décrire chaque décision que vous avez prise. Ces commentaires peuvent expliquer chaque ligne en détail : pourquoi vous avez choisi de l'écrire de cette manière, quelles étaient les alternatives, quel est l'historique du code qui y a conduit. Cela rend la lecture fluide du code vraiment difficile et peut causer une confusion supplémentaire au lecteur. Finalement, causant plus de dommages que de bien. Essayez de garder les commentaires aussi courts que possible avec un contexte minimal.

Si la raison pour laquelle vous ajoutez un commentaire est que le code est hacky ou compliqué, alors rendez-le lisible en le refactorisant — pas en ajoutant une autre couche de confusion. Choisissez de meilleurs noms, divisez les fonctions pour qu'elles fassent une seule chose et utilisez des abstractions. Tout ce dont vous avez besoin pour rendre votre code plus lisible, faites-le avec du code, pas avec des commentaires.

Un exemple de [vue.js](https://github.com/vuejs/vue/blob/dev/src/core/observer/scheduler.js#L36) :

```js
// Cas limite async #6566 nécessite d'enregistrer le timestamp lorsque les écouteurs d'événements sont
// attachés. Cependant, l'appel à performance.now() a un surcoût de performance, surtout
// si la page a des milliers d'écouteurs d'événements. Au lieu de cela, nous prenons un timestamp
// chaque fois que le planificateur se vide et l'utilisons pour tous les écouteurs d'événements
// attachés pendant ce vidage.
export let currentFlushTimestamp = 0
// La correction du cas limite async nécessite de stocker le timestamp d'attachement d'un écouteur d'événement.
let getNow: () => number = Date.now
// Déterminez quel timestamp d'événement le navigateur utilise. Agacement, le
// timestamp peut être soit haute résolution (relatif au chargement de la page) ou basse résolution
// (relatif à l'époque UNIX), donc pour comparer le temps, nous devons utiliser le
// même type de timestamp lors de l'enregistrement du timestamp de vidage.
if (inBrowser && getNow() > document.createEvent('Event').timeStamp) {
// si le timestamp basse résolution qui est plus grand que le timestamp de l'événement
// (qui est évalué APRES) cela signifie que l'événement utilise un timestamp haute résolution,
// et nous devons utiliser la version haute résolution pour les écouteurs d'événements également.
getNow = () => performance.now()
}
```

Cela nécessitera probablement plus de refactoring pour déplacer l'accent des commentaires vers le code réel.

#### 4. Titres, en-têtes et autres "embellissements"

Écrire du code joli est essentiel, mais cela ne signifie pas que vous devez le décorer comme un livre. Nous avons parfois tendance à créer des blocs de code et à leur donner des titres, afin de différencier un bloc d'un autre. Regardons cet exemple de [angular.js](https://github.com/angular/angular.js/blob/master/lib/grunt/utils.js#L134) :

```js
...
build: function(config, fn) {
var files = grunt.file.expand(config.src);
  // grunt.file.expand peut réorganiser la liste des fichiers
  // lorsqu'il développe les globs, donc nous utilisons les champs prefix et suffix
  // pour nous assurer que les fichiers sont au début ou à la fin de
  // la liste (principalement pour l'encapsulation dans un IIFE).
  if (config.prefix) {
    files = grunt.file.expand(config.prefix).concat(files); 
  }
  if (config.suffix) {
   files = files.concat(grunt.file.expand(config.suffix));
  }
  var styles = config.styles;
  var processedStyles;
  //concat
  var src = files.map(function(filepath) {
    return grunt.file.read(filepath);
  }).join(grunt.util.normalizelf('\n'));
  //process
  var processed = this.process(src, grunt.config('NG_VERSION'), config.strict);
  if (styles) {
  processedStyles = this.addStyle(processed, styles.css, styles.minify);
  processed = processedStyles.js;
  if (config.styles.generateCspCssFile) {
    grunt.file.write(removeSuffix(config.dest) + '-csp.css', CSP_CSS_HEADER + processedStyles.css);
  }
}
//write
grunt.file.write(config.dest, processed);
grunt.log.ok('File ' + config.dest + ' created.');
fn();
...

```

Si vous vous retrouvez à faire cela, votre fonction fait sans aucun doute plus d'une chose. Elle est probablement trop longue, explicite et manque de certains niveaux d'abstraction. Dans l'exemple ci-dessus, la fonction a au moins quatre parties : récupérer les fichiers, concaténer, traiter et écrire. Chacune de ces parties apparaît avec une implémentation détaillée, ce qui crée des fonctions longues qui sont également difficiles à lire. Cela peut être corrigé en développant chaque bloc en une fonction différente.

```js
build: function(config, fn) {
  files = this.fetch_files(config)
  var src = this.concat(files)
  var processed = this.process(src)
  write(processed, config)
}
```

À mesure que le code grandit, les "en-têtes" ne sont pas assez gras. C'est là que nous devenons créatifs et ajoutons des "embellissements" supplémentaires à nos commentaires — ligne d'astérisques, de tirets, de signes égal, etc. Jetez un œil à ce code de [pandas](https://github.com/pandas-dev/pandas/blob/master/pandas/core/algorithms.py) :

```py
...
# --------------- #
# dtype access    #
# --------------- #
def _ensure_data(values, dtype=None):
...
def _reconstruct_data(values, dtype, original):
...
def _get_hashtable_algo(values):
...
# --------------- #
# top-level algos #
# --------------- #
def match(to_match, values, na_sentinel=-1):
...
def unique(values):
...
def isin(comps, values):
...
# --------------- #
# select n        #
# --------------- #
class SelectN(object):
...
class SelectNSeries(SelectN):
...
class SelectNFrame(SelectN):
...
# ------------ #
# searchsorted #
# ------------ #
def searchsorted(arr, value, side="left", sorter=None):
...
# ---- #
# diff #
# ---- #
_diff_special = {
...
}
def diff(arr, n, axis=0):
...
```

Le module inclut une liste de fonctions, de variables et de classes, toutes mélangées dans un seul bundle avec des dépendances couplées. Cela pourrait être évité en utilisant une règle simple — si vous sentez que vous avez besoin de titres pour regrouper des fonctions ou des classes, ce serait un bon moment pour diviser votre code en parties plus petites.

Si votre classe a des "groupes" de méthodes de différents types — chaque groupe de fonctions devrait être une classe à part entière. Si votre fichier a trop de classes ou de fonctions qui nécessitent un regroupement, il est temps de diviser chaque groupe dans son propre fichier.

Le code ci-dessus pourrait être beaucoup plus facile à comprendre et à naviguer si nous le divisons en fichiers. En faisant cela, nous découplons également les dépendances, afin que nous puissions importer uniquement le code dont nous avons besoin :

```py
date_acces.py:
def _ensure_data(values, dtype=None)
def _reconstruct_data(values, dtype, original)
def _get_hashtable_algo(values):
top_level_algos.py
def match(to_match, values, na_sentinel=-1):
def unique(values):
def isin(comps, values):
selectn.py
class SelectN(object):
selectn_series.py
class SelectNSeries(SelectN):
selectn_frames.py
class SelectNFrame(SelectN):
search_sorted,py
def searchsorted(arr, value, side="left", sorter=None):
diff.py
_diff_special = {
...
}
def diff(arr, n, axis=0):
...
```

#### 5. /* TODO: */

de [react.js](https://github.com/facebook/react/blob/master/packages/react-dom/server.browser.js#L14) :

```
// TODO: décider de la forme d'exportation de haut niveau.
// C'est hacky mais cela fonctionne avec Rollup et Jest
module.exports = ReactDOMServer.default || ReactDOMServer;
```

Qu'il s'agisse de /* TODO */, [#TODO](https://paper.dropbox.com/?q=%23TODO), ou <! — TODO →, une chose est sûre — personne ne le fera jamais. Oui, même si vous ajoutez un nom à côté et l'assignez à quelqu'un. L'assigné quittera l'entreprise bien avant de corriger ce problème. Je n'ai jamais entendu quelqu'un, quelque part, dire quelque chose comme : "Hey les gars, nous avons un peu de temps libre, pourquoi ne pas corriger tous les todos dans notre code ?" (Si vous avez du temps pour cela, alors votre entreprise a de plus gros problèmes, mais nous laisserons cela pour un autre post).

![Image](https://cdn-media-1.freecodecamp.org/images/5ynOP9pwo8quY5qsMsN8P5U8nlxpbDQo7xWV)
_www.xkcd.com_

Le principal problème avec les todos est que ce n'est pas seulement une excuse pour écrire un mauvais code, mais aussi qu'il n'est pas clair pour le lecteur quel est l'état de ce code — Va-t-il être changé bientôt ? Cela a-t-il déjà été corrigé et l'auteur a oublié de supprimer le commentaire ? Y a-t-il une pull request en attente qui devrait corriger ce problème ? L'auteur du code l'a-t-il laissé pour que nous le corrigions ? — Prenez une décision, soit corrigez-le, soit acceptez les conséquences.

La seule exception est si vous travaillez sur une fonctionnalité et souhaitez diviser vos modifications de code en plusieurs commits. Dans ce cas, ajoutez le commentaire todo et ajoutez le numéro/lien de votre tâche à une vraie tâche dans votre système de gestion des tâches. De cette façon, vous pouvez le suivre et vous assurer qu'il est sur votre feuille de route. Si pour une raison quelconque vous avez décidé de ne pas gérer la tâche, n'oubliez pas de supprimer également le commentaire.

### Enfin, voici les commentaires que vous devriez écrire

Une règle de base — utilisez les commentaires pour répondre à "Pourquoi ?" et le code pour répondre à "Comment ?".

Même si le code est auto-explicatif, la raison pour laquelle nous avons décidé de prendre une approche n'est pas toujours claire, surtout si le lecteur n'a pas de contexte. Cela peut être dû à des exigences produit, à une limitation du système, à l'efficacité ou simplement à un mauvais code que vous n'avez pas eu le temps de refactoriser.

Utiliser des commentaires pour mettre en évidence pourquoi vous avez fait quelque chose de la manière dont vous l'avez fait est bien, mais gardez-les courts et ciblés. Si vous voulez documenter, utilisez un wiki ; si vous voulez parler largement de votre processus de décision, utilisez un doc ; si vous voulez enregistrer l'historique des modifications du code, c'est à cela que servent les commentaires git.

Un bon exemple de [linux](https://github.com/torvalds/linux/blob/master/lib/xz/xz_dec_bcj.c#L337) :

```c
/*
Appliquer le filtre BCJ sélectionné. Mettre à jour *pos et s->pos pour correspondre à la quantité de données qui ont été filtrées. NOTE : Cela est implémenté comme une instruction switch pour éviter d'utiliser des pointeurs de fonction, ce qui pourrait être problématique dans le code de démarrage du noyau, qui doit éviter les pointeurs vers des données statiques (au moins sur x86).
*/
static void bcj_apply(struct xz_dec_bcj *s, uint8_t *buf, size_t *pos, size_t size)
```

**Si vous ne deviez retenir qu'une chose de cet article — utilisez le code pour raconter votre histoire et les commentaires pour transformer « WTF ? » en « OHHHH… ? »**

![Image](https://cdn-media-1.freecodecamp.org/images/q1VxxU9Mei14U0INJ4pfOSgIydZPscPlRLvc)
_www.giphy.com_

**Merci d'avoir consacré quelques minutes de votre temps. Si vous avez aimé, n'hésitez pas à ? ou à répondre avec /*commentaires*/**

**-Alon**

**_Remerciements spéciaux à :_**

* **[Rina Artstain](https://www.freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c/undefined) _et [Keren](https://www.freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c/undefined) pour la relecture, la révision de cet article et les excellents retours techniques_**