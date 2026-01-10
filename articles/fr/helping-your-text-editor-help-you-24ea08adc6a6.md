---
title: Comment aider votre éditeur de texte à vous aider
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T15:23:06.000Z'
originalURL: https://freecodecamp.org/news/helping-your-text-editor-help-you-24ea08adc6a6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ia2Y_ugGsTSSMf3KV4gbcA.png
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment aider votre éditeur de texte à vous aider
seo_desc: 'By Evy

  Tips & tricks for writing more efficient and enjoyable code


  Over six internships, I’ve had lots of lovely mentors who have watched me code and
  let me watch them code. (I ? pair programming!) Thanks to them, there are lots of
  things I’ve learn...'
---

Par Evy

#### Astuces pour écrire du code plus efficace et agréable

![Image](https://cdn-media-1.freecodecamp.org/images/sU6v-eVAoUsJZFAPquJ7NDaWXIlffjPVSlqM)

Au cours de six stages, j'ai eu beaucoup de mentors formidables qui m'ont regardée coder et m'ont laissé les regarder coder. (J'❤️ la [programmation en binôme](https://content.pivotal.io/blog/pair-programming-considered-extremely-beneficial)) Grâce à eux, j'ai appris beaucoup de choses sur le terrain qui ont rendu mon travail plus efficace et agréable.

Certaines de ces choses sont des astuces pour l'éditeur de texte, et je veux partager avec vous ce que j'ai appris !

**Ce n'est pas un article sur quel éditeur de texte vous devriez utiliser**. Je vais partager quelques exemples dans l'éditeur que j'utilise ces jours-ci (Sublime Text sur Mac) — mais de nombreux éditeurs de texte sont personnalisables. Cela signifie que beaucoup de ces astuces peuvent probablement être configurées dans votre éditeur (et j'adorerais voir des commentaires expliquant comment !) Éliminez le discours "cet outil est le meilleur" et apprenons simplement à aider nos outils à mieux nous aider. ✨

### Linter automatiquement votre code

Les linters peuvent être excellents pour rendre le code plus propre et plus facile à lire, et pour attraper les erreurs. Parfois, je lance un linter après avoir terminé une série de modifications, ou je laisse un linter s'exécuter en ligne après avoir ouvert une pull request sur GitHub. Mais j'ai été beaucoup plus rapide à écrire du code qui passe le linter lorsque le linter s'exécutait... pendant que j'écrivais mon code ! Je n'ai pas seulement arrêté de faire des ajustements ennuyeux pendant plusieurs minutes avant de soumettre du code. Je m'entraîne également à corriger les problèmes avant qu'ils ne se produisent.

![Image](https://cdn-media-1.freecodecamp.org/images/MOw7rJCjUU--NZ8yk2uB7EBHZmtzykiLkrSu)
_Le [linter](http://www.sublimelinter.com/en/latest/index.html" rel="noopener" target="_blank" title=") me dit immédiatement : une variable est non définie, et il me manque un point-virgule_

### Règle de 80 caractères

En parlant de règles arbitraires, de nombreux guides de style préfèrent que les lignes ne dépassent pas 80 caractères (ou 100, ou autre chose). La plupart des éditeurs de texte ont un moyen d'ajouter une petite ligne pour vous rappeler lorsque vous atteignez cette limite, quelle qu'elle soit.

![Image](https://cdn-media-1.freecodecamp.org/images/CGUAYQQrt4GIhkJ8g6BUkD8LoccxYp9RsWxP)
_Dans Sublime Text, vous pouvez activer cela depuis View > Ruler_

### Suivre automatiquement certaines conventions d'espacement

De nombreux guides de style préfèrent que les fichiers n'aient pas d'espaces de fin et exactement une nouvelle ligne à la fin de chaque fichier. Il peut être difficile de s'en souvenir, donc c'est bien lorsque mon éditeur de texte le fait pour moi ! Sublime a cela dans ses paramètres utilisateur : « ensure_newline_at_eof_on_save » et « trim_trailing_white_space_on_save ».

### Rechercher (et remplacer) dans toute la base de code

Lorsque je travaille avec une base de code composée de nombreux fichiers, il est utile de rechercher dans celle-ci pour voir tous les endroits où quelque chose est utilisé ou référencé (⌘ shift F sur MacOS dans Sublime). C'est encore mieux d'avoir l'option de rechercher spécifiquement dans un certain dossier ou type de fichier. Parfois, je trouve utile d'activer/désactiver la sensibilité à la casse ou d'utiliser des expressions régulières — bien que je n'utilise pas souvent ces fonctionnalités.

### Trouver rapidement les définitions de fonctions

Bien sûr, je pourrais rechercher dans la base de code le nom d'une fonction, trouver sa définition, et _ensuite_ comprendre comment elle fonctionne. Mais ne serait-ce pas bien d'avoir un moyen d'y arriver plus rapidement ?

![Image](https://cdn-media-1.freecodecamp.org/images/He6pNBtDumRVhUlHH0twAwZnSxCUPgNmQlVo)
_clic droit, aller à la définition, et ...aha ! **c'est** ce que cela fait_

### Trouver rapidement des fichiers

Je veux souvent trouver et ouvrir un fichier mais je ne me souviens pas exactement où il se trouve dans la base de code. J'adore pouvoir entrer le nom du fichier dans une barre de recherche et voir tous les fichiers possibles que je recherche, ce qui me permet d'ouvrir de nouveaux fichiers rapidement. J'adore le bonus supplémentaire d'une entrée de recherche vraiment flexible. Je peux faire toute une série de fautes de frappe ou omettre des parties du nom du fichier et Sublime arrive toujours à comprendre ce que je veux ! (Je parie que la technologie derrière cet algorithme de recherche, souvent appelé « [recherche floue](https://github.com/junegunn/fzf) », est assez intéressante !)

![Image](https://cdn-media-1.freecodecamp.org/images/M5A7Qc4qL8pbVwKOzs944SvbcdBcjkTQx40E)
_Dans Sublime Text, vous pouvez faire apparaître cette barre de recherche avec ⌘P_

### Déplacer des lignes vers le haut et vers le bas

Pour déplacer une ligne de code (ou une fonction entière) en dessous d'une autre, j'utilisais beaucoup de sélection + copie + collage. J'ai depuis découvert comment déplacer des lignes vers le haut et vers le bas avec un raccourci. C'est un petit changement, mais je trouve que cela semble _beaucoup_ plus agréable (un peu comme la sensation incroyable du [glisser à trois doigts](https://support.apple.com/en-us/HT204609)).

![Image](https://cdn-media-1.freecodecamp.org/images/Xt3p6XFHzhT0jjrIIbGJNRW7LjvpozLwnccd)
_ctrl + ⌘ + haut/bas (sur MacOS) dans Sublime Text_

### Colorisation syntaxique

La colorisation syntaxique rend la lecture et l'analyse du code beaucoup plus faciles. Mais elle aide également à attraper les erreurs au fur et à mesure qu'elles sont tapées — si cela ne semble pas correctement coloré, cela pourrait être une erreur.

Parfois, la syntaxe est mise en évidence par défaut. Parfois, seuls certains langages/technologies sont dans vos paramètres par défaut. J'ai eu un nouvel ordinateur portable de travail et je savais que je devais [installer un package](http://gunnariauvinen.com/getting-es6-syntax-highlighting-in-sublime-text/) pour obtenir la colorisation syntaxique `jsx`. Pourtant, j'ai _toujours_ procrastiné pendant quelques mois tout en travaillant avec de nombreux fichiers `jsx`. Après avoir pris une minute pour l'installer, les choses sont devenues beaucoup meilleures.

![Image](https://cdn-media-1.freecodecamp.org/images/DeRG0dUpyd8w0xB3VHcLbMwaOmU3pJtv83js)

![Image](https://cdn-media-1.freecodecamp.org/images/89b8ZaIYbqfGixOrU3z0CJg5gfOqJlmlg8wG)
_Avant et après l'ajout de la colorisation syntaxique pour les fichiers React .jsx_

### Fonctionnalités Git

Enfin, si vous utilisez git dans votre flux de travail, vous pouvez ajouter un support à votre éditeur de texte pour vous indiquer des informations liées à git. Une chose que j'aime voir est quelles lignes ont été ajoutées/supprimées/modifiées depuis mon dernier commit (un `git diff` léger). J'utilise parfois un outil (construit autour du [mal nommé](https://gitlab.com/gitlab-org/gitlab-ce/issues/34469) `[git blame](https://git-scm.com/docs/git-blame)`) pour voir qui a modifié une ligne dans un fichier en dernier.

![Image](https://cdn-media-1.freecodecamp.org/images/tcxOLrCgNk3C3xsjYh4aL43Mliapxp-bnFYc)
_les marqueurs dans les marges de gauche sont grâce au package [GitGutter](https://github.com/jisaacks/GitGutter" rel="noopener" target="_blank" title=")_

### Et plus encore !

Il y a beaucoup de choses cool que votre éditeur de texte peut faire pour vous ! Je suis sûre que je continuerai à apprendre des outils qui m'aideront à être plus efficace et à rendre mon travail plus agréable. Et je ne prévois pas de commencer à tous les utiliser en même temps — avec le temps, je choisirai des outils au fur et à mesure que je m'enthousiasmerai pour eux ou que j'en trouverai le besoin.

J'espère que certaines de ces astuces vous ont été utiles ou excitantes ! J'adorerais entendre dans les commentaires quelles fonctionnalités de l'éditeur de texte vous aimez utiliser. 😊