---
title: Astuces RegEx simples pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:40:49.000Z'
originalURL: https://freecodecamp.org/news/simple-regex-tricks-for-beginners-3acb3fa257cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wUY_k-Q4q-z10Zo425qC5Q.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Astuces RegEx simples pour débutants
seo_desc: 'By Andrei Chernikov

  Always wanted to learn Regular Expressions but got put off by their complexity?
  In this article, I will show you five easy-to-learn RegEx tricks which you can start
  using immediately in your favorite text editor.

  Text Editor Setup...'
---

Par Andrei Chernikov

Vous avez toujours voulu apprendre les expressions régulières mais vous avez été découragé par leur complexité ? Dans cet article, je vais vous montrer cinq astuces RegEx faciles à apprendre que vous pouvez commencer à utiliser immédiatement dans votre éditeur de texte préféré.

### Installation de l'éditeur de texte

Bien que presque tous les éditeurs de texte supportent les expressions régulières maintenant, j'utiliserai Visual Studio Code pour ce tutoriel, mais vous pouvez utiliser n'importe quel éditeur que vous préférez. Notez également que vous devez généralement activer RegEx quelque part près de la barre de recherche. Voici comment faire dans VS Code :

![Image](https://cdn-media-1.freecodecamp.org/images/GjEq59Gj7Io7MWY4OuayOCmqZo0f5ezXyvOS)
_Vous devez activer RegEx en cochant cette option_

### 1) `.` — Correspond à n'importe quel caractère

Commençons simplement. Le symbole point `.` correspond à n'importe quel caractère :

```
b.t
```

![Image](https://cdn-media-1.freecodecamp.org/images/tMEDSKS2mHfOfqYTQP-elCZI5OnGUObC484v)

L'expression régulière ci-dessus correspond à `"bot"`, `"bat"` et tout autre mot de trois caractères commençant par `b` et se terminant par `t`. Mais si vous voulez rechercher le symbole point, vous devez l'échapper avec `\`, donc cette expression régulière ne correspondra qu'au texte exact `"b.t"` :

```
b\.t
```

![Image](https://cdn-media-1.freecodecamp.org/images/anNgoajLGzpFhPWYRnVGlowi0bL4Z4xni59R)

### 2) .* — Correspond à n'importe quoi

Ici, `.` signifie _"n'importe quel caractère"_ et `*` signifie _"n'importe quoi avant ce symbole répété un nombre quelconque de fois."_ Ensemble (`.*`) ils signifient _"n'importe quel symbole un nombre quelconque de fois."_ Vous pouvez l'utiliser, par exemple, pour trouver des correspondances commençant ou se terminant par un certain texte. Supposons que nous avons une méthode JavaScript avec la signature suivante :

```
loadScript(scriptName: string, pathToFile: string)
```

Et nous voulons trouver tous les appels de cette méthode où `pathToFile` pointe vers n'importe quel fichier dans le dossier `"lua"`. Vous pouvez utiliser l'expression régulière suivante pour cela :

```
loadScript.*lua
```

Ce qui signifie, _"correspond à tout le texte commençant par `"loadScript"` suivi de n'importe quoi jusqu'à la dernière occurrence de `"lua"`"_

![Image](https://cdn-media-1.freecodecamp.org/images/wCWC964KLZKxEHdW0fZlr4Z-X-vdcbYX-ogk)
_`loadScript.*lua` : correspond à tout ce qui commence par "loadScript" et se termine par "lua"_

### 3) ? — Correspondance non-gourmande

Le symbole `?` après `.*` et certaines autres séquences RegEx signifie "correspondre le moins possible". Si vous regardez l'image précédente, vous verrez que le texte `"lua"` apparaît deux fois dans chaque correspondance, et tout ce qui précède le second `"lua"` a été correspond. Si vous vouliez correspondre à tout ce qui précède la première occurrence de `"lua"` à la place, vous utiliseriez l'expression régulière suivante :

```
loadScript.*?lua
```

Ce qui signifie, _"correspond à tout ce qui commence par `"loadScript"` suivi de n'importe quoi jusqu'à la première occurrence de `"lua"`"_

![Image](https://cdn-media-1.freecodecamp.org/images/NnHX2yevennzK3Z9ddpq1NPBsbfWnyalfFrw)
_`loadScript.*?lua` : correspond à tout ce qui commence par loadScript et jusqu'à la première occurrence de "lua"_

### 4) ( ) $ — Groupes de capture et références arrière

D'accord, maintenant nous pouvons correspondre à du texte. Mais que faire si nous voulons changer des parties du texte que nous avons trouvé ? Nous devons souvent utiliser des groupes de capture pour cela.

Supposons que nous avons modifié notre méthode `loadScript` et qu'elle a soudainement besoin d'un autre argument inséré entre ses deux arguments. Appelons ce nouvel argument `id`, donc la nouvelle signature de la fonction devrait ressembler à ceci : `loadScript(scriptName, id, pathToFile)`. Nous ne pouvons pas utiliser la fonction de remplacement normale de notre éditeur de texte ici, mais une expression régulière est exactement ce dont nous avons besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/hRdlYnNzYuX64kcVoXrvtH2RfwaY3FzNZedD)
_loadScript\(.*?,.*?\)_

Au-dessus, vous pouvez voir le résultat de l'exécution de l'expression régulière suivante :

```
loadScript\(.*?,.*?\)
```

Ce qui signifie : _"correspond à tout ce qui commence par `"loadScript("` suivi de n'importe quoi jusqu'à la première `,`, puis suivi de n'importe quoi jusqu'à la première `)`"_

Les seules choses qui peuvent vous sembler étranges ici sont les symboles `\`. Ils sont utilisés pour échapper les parenthèses.

Nous devons échapper les symboles `(` et `)` car ce sont des caractères spéciaux utilisés par RegEx pour capturer des parties du texte correspond. Mais nous devons correspondre aux caractères de parenthèses réels.

Dans l'expression régulière précédente, nous avons défini deux arguments de notre appel de méthode avec les symboles `.*?`. Faisons de chacun de nos arguments un **groupe de capture** séparé en ajoutant les symboles `(` et `)` autour d'eux :

```
loadScript\((.*?),(.*?)\)
```

Si vous exécutez cette expression régulière, vous verrez que rien n'a changé. Cela est dû au fait qu'elle correspond au même texte. Mais maintenant nous pouvons nous référer au premier argument comme `$1` et au second argument comme `$2`. Cela s'appelle une référence arrière, et cela nous aidera à faire ce que nous voulons : ajouter un autre argument au milieu de l'appel :

Entrée de recherche :

```
loadScript\((.*?),(.*?)\)
```

Ce qui signifie la même chose que l'expression régulière précédente mais mappe les arguments aux groupes de capture 1 et 2 respectivement.

Entrée de remplacement :

```
loadScript($1,id,$2)
```

Ce qui signifie _"remplacer chaque texte correspond par le texte `"loadScript("` suivi du groupe de capture 1, `"id"`, du groupe de capture 2 et de `)`"_. Notez que vous n'avez pas besoin d'échapper les parenthèses dans l'entrée de remplacement.

![Image](https://cdn-media-1.freecodecamp.org/images/w27UNrc7N2hkWAO1DmU6p0gulIYiwU-oYjpT)
_Résultat du remplacement_

### 5) [ ] — Classes de caractères

Vous pouvez lister les caractères que vous voulez correspondre à une position spécifique en plaçant les symboles `[` et `]` autour de ces caractères. Par exemple, la classe `[0-9]` correspond à tous les chiffres de 0 à 9. Vous pouvez également lister tous les chiffres explicitement : `[0123456789]` — le sens est le même. Vous pouvez utiliser le tiret avec les lettres aussi, `[a-z]` correspondra à n'importe quel caractère latin minuscule, `[A-Z]` correspondra à n'importe quel caractère latin majuscule et `[a-zA-Z]` correspondra aux deux.

Vous pouvez également utiliser `*` après une classe de caractères tout comme après `.`, ce qui dans ce cas signifie : _"correspond à n'importe quel nombre d'occurrences des caractères dans cette classe"_

![Image](https://cdn-media-1.freecodecamp.org/images/2aTqw0lDyht0cE1gqoF3O5eYcemyzhIBhSzU)
_expect.*to.equal\([09]*\) : Correspond seulement à ces lignes où nous attendons que la variable testée soit égale à un nombre_

### Dernier mot

Vous devez savoir qu'il existe plusieurs variantes de RegEx. Celle dont j'ai discuté ici est le moteur RegEx de JavaScript. La plupart des moteurs modernes sont similaires, mais il peut y avoir quelques différences. Habituellement, ces différences incluent les caractères d'échappement et les marques de références arrière.

Je vous exhorte à ouvrir votre éditeur de texte et à commencer à utiliser certaines de ces astuces dès maintenant. Vous verrez que vous pouvez maintenant accomplir de nombreuses tâches de refactorisation beaucoup plus rapidement qu'auparavant. Une fois que vous êtes à l'aise avec ces astuces, [vous pouvez commencer à rechercher plus sur les expressions régulières](https://www.regular-expressions.info/).

**Merci d'avoir lu mon article jusqu'à la fin. Ajoutez des applaudissements si vous l'avez trouvé utile et abonnez-vous pour plus de mises à jour. Je publierai plus d'articles sur les expressions régulières, JavaScript et la programmation en général.**