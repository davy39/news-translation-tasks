---
title: Présentation d'ABS, un langage de programmation pour le scripting shell
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T17:33:17.000Z'
originalURL: https://freecodecamp.org/news/introducing-abs-a-programming-language-for-shell-scripting-dfbd737d621
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_BSX61CxShyqW7oT7Kgc8Q.jpeg
tags:
- name: Bash
  slug: bash
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: 'tech '
  slug: tech
seo_title: Présentation d'ABS, un langage de programmation pour le scripting shell
seo_desc: 'By Alex Nadalin

  Over the past few days I took some time to work on a project I had in mind for ages,
  a scripting alternative to Bash: let me introduce you to the ABS programming language.


  Why

  Let me keep this brief: we all love shell programming — a...'
---

Par Alex Nadalin

Au cours des derniers jours, j'ai pris le temps de travailler sur un projet que j'avais en tête depuis des années, une alternative de scripting à Bash : permettez-moi de vous présenter le [langage de programmation ABS](https://www.abs-lang.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/SEQ45gplyveMOk8nKiL8d-w5azHRSEjtC7-8)

### Pourquoi

Permettez-moi d'être bref : nous aimons tous la programmation shell — automatiser des tâches répétitives sans trop d'effort.

Nous pourrions probablement convenir que la programmation shell est aussi un peu folle en termes de syntaxe :

```
if [ -z $STRING ]; then    ...fi
```

Genre, euh, _quoi ? fi ? -z ? les crochets ?_

Se battre avec Bash, ou le langage de programmation shell courant, peut devenir intense de temps en temps. Écrire du code tel que :

```
if (this == that) {    parts = this.split("/").filter(...).map(...)}
```

vous fera pleurer si vous utilisez le shell.

Maintenant, vous pouvez faire des choses similaires avec n'importe quel langage de programmation grand public (l'exemple ci-dessus est du JavaScript valide) : ce que ces langages ne font pas bien, c'est leur intégration avec le système sous-jacent — un [shell est simplement beaucoup plus concis/puissant](https://stackoverflow.com/questions/796319/strengths-of-shell-scripting-compared-to-python) de ce point de vue.

Imaginez que vous pourriez exécuter du code comme :

```
host = $(hostname)
```

```
if (host == "johns_computer") {    ...}
```

Eh bien, vous n'avez plus à « imaginer » : ABS est un langage qui combine des commandes système rapides et simples avec une syntaxe plus élégante.

Pensez-y comme à la meilleure chose depuis les bonbons, en vous souvenant que c'est la définition que l'auteur d'ABS vous a donnée. Mais sérieusement, c'est plutôt très pratique.

Vous ne me croyez pas ? Lisez la suite !

### Exemples

Je suis un fervent croyant du mantra « montre-moi le code ! », alors passons rapidement à cela. Exécuter des commandes shell est extrêmement facile dans ABS :

```
# Obtenir le contenu de votre fichier host$(cat /etc/hosts)
```

et les pipes fonctionnent aussi :

```
# Vérifier si un domaine est dans votre fichier host$(cat /etc/hosts | grep domain.com | wc -l)
```

À ce stade, nous pouvons simplement capturer la sortie de notre commande et écrire un script dessus :

```
# Vérifier si un domaine est dans votre fichier hostmatches = $(cat /etc/hosts | grep domain.com | wc -l)
```

```
# Si c'est le cas, imprimer une chaîne génialeif matches.int() > 0 {  echo("We got ya!")}
```

Cela n'arrivera pas, mais disons qu'une erreur se produit :

```
# Vérifier si un domaine est dans votre fichier hostmatches = $(cat /etc/hosts | grep domain.com | wc -l)
```

```
if !matches.ok {    echo("Comment faites-vous même...")}
```

```
# Si c'est le cas, imprimer une chaîne génialeif matches.int() > 0 {  echo("We got ya!")}
```

Nous pourrions rendre cela un peu plus général :

```
$ cat script.abs# Usage $ abs script.abs domain.com# Vérifier si un domaine est dans votre fichier hostdomain = arg(2)matches = $(cat /etc/hosts | grep $domain | wc -l)
```

```
if !matches.ok {    echo("Comment faites-vous même...")}
```

```
# Si c'est le cas, imprimer une chaîne génialeif matches.int() > 0 {  echo("We got %s!", domain)}
```

Maintenant, les chaînes sont assez ennuyeuses, alors nous pouvons essayer quelque chose de plus amusant :

```
# Disons que nous obtenons un peu de JSON à partir d'une commande x = $(echo '{"some": {"dope": "json"}}')x.json().some.dope # "json"
```

```
# Des tableaux, dites-vous ?tz = $(cat /etc/timezone) # "Asia/Dubai"parts = tz.split("/") # ["Asia", "Dubai"]
```

```
# Vous feriez mieux de déstructurer tout cela ![continent, city] = tz.split("/")
```

...et ainsi de suite. Il y a des tonnes de choses « régulières » que vous pouvez faire avec ABS, donc je ne vais pas me concentrer beaucoup sur celles-ci — laissez-moi plutôt vous montrer les parties les plus étranges :

```
# Éviter le bug qui est arrivé parce que# nous avons oublié de comparer les chaînes de manière insensible à la casse"HELLO" ~ "hello" # true
```

```
# Juste une plage1..3 # [1, 2, 3]
```

```
# Opérateur de comparaison combiné (merci Ruby !)5 <=> 5 # 05 <=> 6 # -16 <=> 5 # 1
```

```
# Court-circuit classique1 && 2 # 21 || 2 # 1
```

Vous pouvez parcourir toute la [documentation](https://www.abs-lang.org/introduction/why-another-scripting-language) en 15 minutes : l'objectif d'ABS n'est pas d'être un langage généraliste, chargé de fonctionnalités, donc la surface n'est pas si large. De plus, si vous avez travaillé avec des langages tels que JavaScript, Python ou Ruby, vous n'aurez pas de difficultés à vous habituer à ABS.

### Que va-t-il se passer maintenant ?

Vous pouvez vous rendre sur le [site web d'ABS](https://www.abs-lang.org/), et en apprendre davantage sur le langage. Les plus courageux iront plutôt faire un tour sur le [dépôt github d'ABS](https://github.com/abs-lang/abs) et [télécharger une version](https://github.com/abs-lang/abs/releases) pour l'installer localement.

Les plus courageux encore exécuteront simplement :

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

_(vous devrez peut-être utiliser sudo juste avant cela)_

Lequel serez-vous ?

![Image](https://cdn-media-1.freecodecamp.org/images/964Hq52XCeztEs5UKsPayCvFgCTtLfD1pcRZ)
_Photo par [Unsplash](https://unsplash.com/photos/XMFZqrGyV-Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Fabian Grohs</a> sur <a href="https://unsplash.com/search/photos/programming?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

_Publié à l'origine sur [odino.org](https://odino.org/introducing-abs-a-programming-language-for-shell-scripting/) (25 décembre 2018)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ ?