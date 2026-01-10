---
title: Comment j'ai rétro-conçu l'éditeur Hemingway - une application d'écriture populaire
  - et construit le mien depuis une plage en Thaïlande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-03T04:30:00.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-samwcoding-deconstructing-the-hemingway-app-8098e22d878d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca1be740569d1a4ca5067.jpg
tags:
- name: english
  slug: english
- name: JavaScript
  slug: javascript
- name: lessons learned
  slug: lessons-learned
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: Comment j'ai rétro-conçu l'éditeur Hemingway - une application d'écriture
  populaire - et construit le mien depuis une plage en Thaïlande
seo_desc: 'By Sam Williams

  I’ve been using the Hemingway App to try to improve my posts. At the same time I’ve
  been trying to find ideas for small projects. I came up with the idea of integrating
  a Hemingway style editor into a markdown editor. So I needed to f...'
---

Par Sam Williams

J'ai utilisé l'application Hemingway pour essayer d'améliorer mes publications. En même temps, j'ai cherché des idées pour de petits projets. J'ai eu l'idée d'intégrer un éditeur de style Hemingway dans un éditeur markdown. Je devais donc découvrir comment Hemingway fonctionnait !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Hemingway_Editor.png)
_Une capture d'écran de l'éditeur Hemingway_

### Obtenir la logique

Je n'avais aucune idée de comment l'application fonctionnait lorsque j'ai commencé. Elle aurait pu envoyer le texte à un serveur pour calculer la complexité de l'écriture, mais je m'attendais à ce que ce soit calculé côté client.

Ouvrir les outils de développement dans Chrome (Control + Shift + I ou F12 sur Windows/Linux, Command + Option + I sur Mac) et naviguer vers _Sources_ a fourni les réponses. Là, j'ai trouvé le fichier que je cherchais : **hemingway3-web.js.**

![Image](https://cdn-media-1.freecodecamp.org/images/5j4RVt-ESeQ5r1KyFgUI4bQ9lzJeEY0FQfpE)
_Fichier minifié en haut, fichier formaté en bas. Quelle différence !_

Ce code est sous une forme minifiée, ce qui est pénible à lire et à comprendre. Pour résoudre cela, j'ai copié le fichier dans VS Code et formaté le document (_Control_ + _Shift_ + _I_ pour VS Code). Cela transforme un fichier de 3 lignes en un fichier de 4859 lignes avec tout bien formaté.

### Explorer le code

J'ai commencé à parcourir le fichier pour trouver quelque chose que je pouvais comprendre. Le début du fichier contenait des expressions de fonction immédiatement invoquées. Je n'avais que peu d'idée de ce qui se passait.

```js
!function(e) {
  function t(r) {
      if (n[r])
          return n[r].exports;
      var o = n[r] = {
          exports: {},
          id: r,
          loaded: !1
      };
...
```

Cela a continué pendant environ 200 lignes avant que je décide que je lisais probablement le code pour faire fonctionner la page (React ?). J'ai commencé à parcourir le reste du code jusqu'à ce que je trouve quelque chose que je pouvais comprendre. (J'ai manqué beaucoup de choses que j'ai trouvées plus tard en cherchant des appels de fonction et en regardant la définition de la fonction).

Le premier morceau de code que j'ai compris était tout en bas à la ligne 3496 !

```
getTokens: function(e) {
  var t = this.getAdverbs(e), 
    n = this.getQualifiers(e),
    r = this.getPassiveVoices(e), 
    o = this.getComplexWords(e);
  return [].concat(t, n, r, o).sort(function(e, t) {
    return e.startIndex - t.startIndex
  })
}
```

Et incroyablement, toutes ces fonctions étaient définies juste en dessous. Maintenant, je savais comment l'application définissait les adverbes, les qualificatifs, la voix passive et les mots complexes. Certains d'entre eux sont très simples. L'application vérifie chaque mot par rapport à des listes de qualificatifs, de mots complexes et de phrases de voix passive. `this.getAdverbs` filtre les mots en fonction de leur terminaison en 'ly' et vérifie ensuite s'ils ne sont pas dans la liste des mots non adverbes se terminant par 'ly'.

Le prochain morceau de code utile était l'implémentation de la mise en surbrillance des mots ou des phrases. Dans ce code, il y a une ligne :

```js
e.highlight.hardSentences += h
```

'hardSentences' était quelque chose que je pouvais comprendre, quelque chose avec du sens. J'ai ensuite recherché dans le fichier `hardSentences` et obtenu 13 correspondances. Cela m'a conduit à une ligne qui calculait les statistiques de lisibilité :

```js
n.stats.readability === i.default.readability.hard && (e.hardSentences += 1),
n.stats.readability === i.default.readability.veryHard && (e.veryHardSentences += 1)
```

Maintenant, je savais qu'il y avait un paramètre `readability` dans `stats` et `i.default`. En recherchant dans le fichier, j'ai obtenu 40 correspondances. L'une de ces correspondances était une fonction `getReadabilityStyle`, où ils notent votre écriture.

Il y a trois niveaux : normal, difficile et très difficile.

```js
t = e.words;
n = e.readingLevel;
return t < 14
  ? i.default.readability.normal
  : n >= 10 && n < 14
    ? i.default.readability.hard
    : n >= 14 ? i.default.readability.veryHard 
      : i.default.readability.normal;
```

'Normal' est moins de 14 mots, 'difficile' est de 10 à 14 mots, et 'très difficile' est plus de 14 mots.

Maintenant, il fallait trouver comment calculer le niveau de lecture.

J'ai passé un certain temps ici à essayer de trouver une notion de comment calculer le niveau de lecture. Je l'ai trouvé 4 lignes au-dessus de la fonction `getReadabilityStyle`.

```js
e = letters in paragraph;
t = words in paragraph;
n = sentences in paragraph;

getReadingLevel: function(e, t, n) {
  if (0 === t 
 0 === n) return 0;
  var r = Math.round(4.71 * (e / t) + 0.5 * (t / n) - 21.43);
  return r <= 0 ? 0 : r;
}
```

Cela signifie que votre score est de 4,71 * longueur moyenne des mots + 0,5 * longueur moyenne des phrases - 21,43. C'est tout. C'est ainsi que Hemingway note chacune de vos phrases.

### Autres choses intéressantes que j'ai trouvées

* Le commentaire de surbrillance (informations sur votre écriture sur le côté droit) est une grande instruction switch. Des instructions ternaires sont utilisées pour changer la réponse en fonction de la qualité de votre écriture.
* La notation va jusqu'à 16 avant d'être classée comme niveau 'Post-Graduate'.

### Ce que je vais faire avec cela

Je prévois de créer un site web de base et d'appliquer ce que j'ai appris en déconstruisant l'application Hemingway. Rien de sophistiqué, plus comme un exercice pour implémenter une certaine logique. J'ai déjà construit un visualiseur Markdown, donc je pourrais aussi essayer de créer une application d'écriture avec le système de surbrillance et de notation.

# Créer ma propre application Hemingway

Ayant compris comment fonctionne l'application Hemingway, j'ai ensuite décidé d'implémenter ce que j'avais appris pour faire une version beaucoup simplifiée.

Je voulais m'assurer que je gardais cela basique, en me concentrant plus sur la logique que sur le style. J'ai choisi d'opter pour une simple zone de texte.

#### Défis

1. Comment assurer la performance. Re-scanner tout le document à chaque pression de touche pourrait être très coûteux en calcul. Cela pourrait entraîner un blocage de l'UX, ce qui n'est évidemment pas ce que nous voulons.

2. Comment diviser le texte en paragraphes, phrases et mots pour la mise en surbrillance.

#### Solutions possibles

* Ne re-scanner que les paragraphes qui changent. Faites cela en comptant le nombre de paragraphes et en comparant cela avec le document avant le changement. Utilisez cela pour trouver le paragraphe qui a changé ou le nouveau paragraphe et ne scannez que celui-ci.
* Avoir un bouton pour scanner le document. Cela réduit massivement les appels de la fonction de scan.

2. Utilisez ce que j'ai appris de Hemingway — chaque paragraphe est un <p> et toute phrase ou mot nécessitant une mise en surbrillance est enveloppé dans un <span> interne avec la classe nécessaire.

### Construire l'application

Récemment, j'ai lu beaucoup d'articles sur la construction d'un Produit Minimum Viable (MVP), donc j'ai décidé que je mènerais ce petit projet de la même manière. Cela signifiait garder tout simple. J'ai décidé d'opter pour une zone de saisie, un bouton pour scanner et une zone de sortie.

Cela a été très facile à configurer dans mon fichier index.html.

```html
<link rel="stylesheet" href="index.css">
<title>Fake Hemingway</title>
<div>
    <h1>Fake Hemingway</h1>
    <textarea name="" id="text-area" rows="10"></textarea>
    <button onclick="format()">Test Me</button>
    <div id="output">
    </div>
</div>
<script src="index.js"></script>
```

Maintenant, commençons la partie intéressante. Maintenant, faisons fonctionner le JavaScript.

La première chose à faire était de rendre le texte de la zone de texte dans la zone de sortie. Cela implique de trouver le texte d'entrée et de définir le html interne de la sortie sur ce texte.

```js
function format() {
    let inputArea = document.getElementById("text-area");
    let text = inputArea.value;
    let outputArea = document.getElementById("output");
    outputArea.innerHTML = text;
}
```

Ensuite, il faut diviser le texte en paragraphes. Cela est accompli en divisant le texte par '\n' et en mettant chacun de ceux-ci dans une balise <p>. Pour ce faire, nous pouvons mapper le tableau de paragraphes, en les mettant entre des balises <p>. L'utilisation de chaînes de modèles rend cela très facile.

```js
let paragraphs = text.split("\n");
let inParagraphs = paragraphs.map(paragraph => `<p>${paragraph}</p>`);
outputArea.innerHTML = inParagraphs.join(" ");
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nv9Mb4gnGQZTMmYReYb1HQ.png)

Pendant que je travaillais là-dessus, je commençais à être agacé de devoir copier et coller le texte de test dans la zone de texte. Pour résoudre cela, j'ai implémenté une Expression de Fonction Immédiatement Invoquée (IIFE) pour remplir la zone de texte lorsque la page web se charge.

```js
(function start() {
    let inputArea = document.getElementById("text-area");
    let text = `The app highlights lengthy, …. compose something new.`;
    inputArea.value = text;
})();
```

Maintenant, la zone de texte était pré-remplie avec le texte de test chaque fois que vous chargez ou actualisez la page web. Bien plus simple.

### Mise en surbrillance

Maintenant que je rendais bien le texte et que je testais sur un texte cohérent, je devais travailler sur la mise en surbrillance. Le premier type de mise en surbrillance que j'ai décidé de traiter était la mise en surbrillance des phrases difficiles et très difficiles.

La première étape de cela est de boucler sur chaque paragraphe et de les diviser en un tableau de phrases. Je l'ai fait en utilisant une fonction `split()`, en divisant à chaque point avec un espace après.

```js
let sentences = paragraph.split('. ');
```

De Hemingway, je savais que je devais calculer le nombre de mots et le niveau de chacune des phrases. Le niveau de la phrase dépend de la longueur moyenne des mots et des mots moyens par phrase. Voici comment j'ai calculé le nombre de mots et le total des mots par phrase.

```js
let words = sentence.split(" ").length;
let letters = sentence.split(" ").join("").length;
```

En utilisant ces nombres, j'ai pu utiliser l'équation que j'ai trouvée dans l'application Hemingway.

```js
let level = Math.round(4.71 * (letters / words) + 0.5 * words / sentences — 21.43);
```

Avec le niveau et le nombre de mots pour chacune des phrases, définissez leur niveau de difficulté.

```js
if (words < 14) {
    return sentence;
} else if (level >= 10 && level < 14) {
    return `<span class="hardSentence">${sentence}</span>`;
} else if (level >= 14) {
    return `<span class="veryHardSentence">${sentence}</span>`;
} else {
    return sentence;
}
```

Ce code dit que si une phrase est plus longue que 14 mots et a un niveau de 10 à 14, alors elle est difficile, si elle est plus longue que 14 mots et a un niveau de 14 ou plus, alors elle est très difficile. J'ai utilisé des chaînes de modèles à nouveau mais j'ai inclus une classe dans les balises span. C'est ainsi que je vais définir la mise en surbrillance.

Le fichier CSS est vraiment simple ; il contient simplement chacune des classes (adverb, passive, hardSentence) et définit leur couleur de fond. J'ai pris les couleurs exactes de l'application Hemingway.

Une fois les phrases retournées, je les ai toutes jointes pour faire chacun des paragraphes.

À ce stade, j'ai réalisé qu'il y avait quelques problèmes dans mon code.

* Il n'y avait pas de points. Lorsque j'ai divisé les paragraphes en phrases, j'ai supprimé tous les points.
* Le nombre de lettres dans la phrase incluait les virgules, les tirets, les deux-points et les points-virgules.

Ma première solution était très primitive mais elle fonctionnait. J'ai utilisé split('symbole') et join('') pour supprimer la ponctuation et j'ai ensuite ajouté '.' à la fin. Bien que cela fonctionnait, j'ai cherché une meilleure solution. Bien que je n'aie pas beaucoup d'expérience avec les regex, je savais que ce serait la meilleure solution. Après quelques recherches sur Google, j'ai trouvé une solution beaucoup plus élégante.

```js
let cleanSentence = sent.replace(/[^a-z0-9. ]/gi, "") + ".";
```

Avec cela fait, j'avais un produit partiellement fonctionnel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aAQaw7iyax7r87qlh2i_sg.png)
_Mise en surbrillance des phrases difficiles_

La prochaine chose que j'ai décidé de traiter était les adverbes. Pour trouver un adverbe, Hemingway trouve simplement des mots qui se terminent par 'ly' et vérifie ensuite qu'ils ne sont pas dans une liste de mots non adverbes se terminant par 'ly'. Ce serait mauvais si 'apply' ou 'Italy' étaient étiquetés comme des adverbes.

Pour trouver ces mots, j'ai pris les phrases et je les ai divisées en un tableau de mots. J'ai mappé ce tableau et utilisé une instruction IF.

```js
if(word.match(/ly$/) &&, !lyWords[word] ){
    return `<span class="adverb">${word}</span>`;
} else {
    return word
};
```

Bien que cela fonctionnait la plupart du temps, j'ai trouvé quelques exceptions. Si un mot était suivi d'un signe de ponctuation, il ne correspondait pas à la fin avec 'ly'. Par exemple, 'The crocodile glided elegantly; it's prey unaware' aurait le mot 'elegantly;' dans le tableau. Pour résoudre cela, j'ai réutilisé la fonctionnalité `.replace(/^a-z0-9. ]/gi,"")` pour nettoyer chacun des mots.

Une autre exception était si le mot était en majuscule, ce qui a été facilement résolu en appelant `toLowerCase()` sur la chaîne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iIvcSMYCHDp7Z5BhUnAogw.png)
_Adverbes fonctionnant_

Maintenant, j'avais un résultat qui fonctionnait avec les adverbes et la mise en surbrillance des mots individuels. J'ai ensuite implémenté une méthode très similaire pour les mots complexes et qualifiants. C'est alors que j'ai réalisé que je ne cherchais plus seulement des mots individuels, je cherchais des phrases. J'ai dû changer mon approche de la vérification si chaque mot était dans la liste à voir si la phrase contenait chacune des phrases.

Pour ce faire, j'ai utilisé la fonction `.indexOf()` sur les phrases. Si il y avait un index du mot ou de la phrase, j'ai inséré une balise span d'ouverture à cet index et ensuite la balise span de fermeture après la longueur de la clé.

```js
let qualifiers = getQualifyingWords();
let wordList = Object.keys(qualifiers);
wordList.forEach(key => {
    let index = sentence.toLowerCase().indexOf(key);
    if (index >= 0) {
    sentence =
        sentence.slice(0, index) +
        'span class="qualifier"' +
        sentence.slice(index, index + key.length) +
        "</span>" +
        sentence.slice(index + key.length);
    }
});
```

Avec cela fonctionnant, cela commence à ressembler de plus en plus à l'éditeur Hemingway.

![Image](https://cdn-media-1.freecodecamp.org/images/1*szV4gRH35rLe0xxRSgOxZw.png)
_Obtenir des phrases complexes et des qualifiants fonctionnant_

La dernière pièce du puzzle de la mise en surbrillance à implémenter était la voix passive. Hemingway a utilisé une fonction de 30 lignes pour trouver toutes les phrases passives. J'ai choisi d'utiliser la plupart de la logique que Hemingway a implémentée, mais d'ordonner le processus différemment. Ils cherchaient à trouver des mots qui étaient dans une liste (is, are, was, were, be, been, being) et vérifiaient ensuite si le mot suivant se terminait par 'ed'.

J'ai parcouru chacun des mots dans une phrase et vérifié s'ils se terminaient par 'ed'. Pour chaque mot 'ed' que j'ai trouvé, j'ai vérifié si le mot précédent était dans la liste des mots précédents. Cela semblait beaucoup plus simple, mais peut être moins performant.

Avec cela fonctionnant, j'avais une application qui mettait en surbrillance tout ce que je voulais. C'est mon MVP.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pgZcfGjZGkRiyE48v-UTOQ.png)
_Toute la mise en surbrillance fonctionnant_

### Ensuite, j'ai rencontré un problème

Pendant que j'écrivais ce post, j'ai réalisé qu'il y avait deux énormes bugs dans mon code.

```js
// de getQualifier et getComplex
let index = sentence.toLowerCase().indexOf(key);
// de getPassive
let index = words.indexOf(match);
```

Cela ne trouvera jamais que la première instance de la clé ou de la correspondance. Voici un exemple des résultats que ce code produira.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jKeU9Dn7Yu1XZn8YHUmh6w.png)
_Code avec des bugs_

'Perhaps' et 'been marked' auraient dû être mis en surbrillance deux fois chacun, mais ils ne le sont pas.

Pour corriger le bug dans getQualifier et getComplex, j'ai décidé d'utiliser la récursivité. J'ai créé une fonction `findAndSpan` qui utilise `.indexOf()` pour trouver la première instance du mot ou de la phrase. Elle divise la phrase en 3 parties : avant la phrase, la phrase, après la phrase. La récursivité fonctionne en passant la chaîne 'après la phrase' dans la fonction. Cela continuera jusqu'à ce qu'il n'y ait plus d'instances de la phrase, où la chaîne sera simplement renvoyée.

```js
function findAndSpan(sentence, string, type) {
    let index = sentence.toLowerCase().indexOf(key);
    if (index >= 0) {
        sentence =
            sentence.slice(0, index) +
            `<span class="${type}">` +
            sentence.slice(index, index + key.length) +
            "</span>" +
            findAndSpan(
                sentence.slice(index + key.length), 
                key,
                type);
    }
    return sentence;
}
```

Quelque chose de très similaire devait être fait pour la voix passive. La récursivité était dans un motif presque identique, passant les éléments de tableau restants au lieu de la chaîne restante. Le résultat de l'appel de récursivité a été étalé dans un tableau qui a ensuite été renvoyé. Maintenant, l'application peut gérer les adverbes répétés, les qualifiants, les phrases complexes et les utilisations de la voix passive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*15D7mV2ycniuDJ7As5en1A.png)

### Compteur de statistiques

La dernière chose que je voulais faire fonctionner était la belle ligne de boîtes vous informant du nombre d'adverbes ou de mots complexes que vous aviez utilisés.

Pour stocker les données, j'ai créé un objet avec des clés pour chacun des paramètres que je voulais compter. J'ai commencé par avoir cette variable comme une variable globale mais je savais que je devrais la changer plus tard.

Maintenant, je devais remplir les valeurs. Cela a été fait en incrémentant la valeur chaque fois qu'elle était trouvée.

```js
data.sentences += sentence.length
ou
data.adverbs += 1
```

Les valeurs devaient être réinitialisées chaque fois que le scan était exécuté pour s'assurer que les valeurs n'augmentaient pas continuellement.

Avec les valeurs dont j'avais besoin, je devais les afficher à l'écran. J'ai modifié la structure du fichier html de sorte que la zone de saisie et la zone de sortie soient dans une div à gauche, laissant une div de droite pour les compteurs. Ces compteurs sont des divs vides avec un id et une classe appropriés ainsi qu'une classe 'counter'.

```html
<div id="adverb" class="adverb counter"></div>
<div id="passive" class="passive counter"></div>
<div id="complex" class="complex counter"></div>
<div id="hardSentence" class="hardSentence counter"></div>
<div id="veryHardSentence" class="veryHardSentence counter"></div>
```

Avec ces divs, j'ai utilisé document.querySelector pour définir le html interne pour chacun des compteurs en utilisant les données qui avaient été collectées. Avec un peu de style de la classe 'counter', l'application web était complète. [Essayez-la ici](https://samwsoftware.github.io/Projects/hemingway/) ou regardez [mon code ici.](https://github.com/SamWSoftware/Projects/tree/master/hemingway)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C1uc-HKl7IAjxXYDWWIWqQ.png)
_L'application terminée_