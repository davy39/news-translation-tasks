---
title: 'ABS 1.2 : commandes en arrière-plan et la possibilité d''importer des fichiers'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T19:13:17.000Z'
originalURL: https://freecodecamp.org/news/abs-1-2-background-commands-the-ability-to-import-files-e5d1e046cb35
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ph8ChGDlQ8vqoWTp.png
tags:
- name: Bash
  slug: bash
- name: General Programming
  slug: programming
- name: Scripting
  slug: scripting
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'ABS 1.2 : commandes en arrière-plan et la possibilité d''importer des
  fichiers'
seo_desc: 'By Alex Nadalin

  ABS is a programming language that puts together the productivity of bash scripts
  with the elegance of high-level languages such as Python or Ruby. It lets you issue
  system commands by simply wrapping them in backticks (very similar t...'
---

Par Alex Nadalin

[ABS](https://www.abs-lang.org/) est un langage de programmation qui combine la productivité des scripts bash avec l'élégance des langages de haut niveau tels que Python ou Ruby. Il vous permet d'exécuter des commandes système en les enveloppant simplement dans des backticks (très similaire à la façon dont vous le feriez dans Bash) et vous permet d'utiliser leur sortie avec une syntaxe claire et concise.

Voici, par exemple, un script qui tenterait d'exécuter une commande `curl`, et quitterait si le serveur à `example.org` ne répondait pas dans les 10 secondes :

![Image](https://cdn-media-1.freecodecamp.org/images/dSVYyySoZGbfUcDXgDVHZ674fUKRRG5GGL8n)

Il y a quelques semaines, l'équipe [ABS](https://github.com/abs-lang/abs) a réussi à rassembler une nouvelle version mineure du langage, [1.2.0](https://github.com/abs-lang/abs/releases/tag/1.2.0), qui inclut des tonnes de fonctionnalités intéressantes — découvrons-les !

### ~/.absrc

ABS recherchera désormais un fichier `~/.absrc` par défaut à précharger chaque fois que vous exécutez un script. Cela est particulièrement utile si vous souhaitez déposer des fonctions "de base" que vous êtes susceptible de réutiliser dans plusieurs scripts à un endroit commun. Votre `.absrc` pourrait ressembler à :

```
tenth = f(x) {   return x / 10 }
```

ainsi, dans n'importe quel autre script abs, vous pouvez utiliser `tenth(x)`.

### ~/.abs_history

Nous avons également introduit un fichier d'historique afin de pouvoir répéter facilement les commandes lors de l'utilisation du repl ABS. Celui-ci est, par défaut, situé à `~/.abs_history` et est synchronisé chaque fois que vous fermez une session repl :

```
$ absHello alex, welcome to the ABS (1.2.0) programming language!Type 'quit' when you're done, 'help' if you get lost!⟶  `sleep 1`
```

```
⟶  quitAdios!$ tail ~/.abs_history`sleep 1`
```

### require(file)

Une grande nouveauté ici : vous pouvez maintenant **importer des fichiers externes** via `require(chemin/vers/fichier.abs)`.

C'est une étape qui permet de créer des bibliothèques de base qui peuvent être réutilisées dans plusieurs scripts ABS, et organise le code ABS un peu mieux.

### Commandes en arrière-plan

Une autre grande fonctionnalité ici : vous pouvez maintenant exécuter des commandes "en arrière-plan" qui ne bloqueront pas votre script ABS (ces commandes sont exécutées dans une [Goroutine](https://tour.golang.org/concurrency/1)).

Une commande en arrière-plan diffère d'une commande régulière simplement parce qu'elle utilise un `&` à la fin de la commande elle-même — voyons-les en action :

```
`sleep 10`echo("Hello world!") # Cela sera imprimé après 10s
```

```
`sleep 10 &`echo("Hello world!") # Cela sera imprimé immédiatement
```

Vous pouvez vérifier si une commande en arrière-plan est terminée avec la propriété `.done` :

```
cmd = `sleep 10 &`cmd.done # falsewait(10000)cmd.done # true
```

et nous avons ajouté la fonction `wait()` si vous avez besoin de bloquer jusqu'à ce que la commande soit terminée :

```
cmd = `sleep 10 &`cmd.wait() # Le script sera bloqué pendant 10secho("Hello world!")
```

### Divers

Quelques fonctionnalités supplémentaires qui ont été incluses dans cette version :

* fonctions numériques telles que `floor`, `round` et `ceil`
* `cd()`, qui change le `cwd` d'un script
* vous pouvez personnaliser votre prompt en définissant les variables d'environnement `ABS_PROMPT_LIVE_PREFIX=true` et `ABS_PROMPT_PREFIX=templated_string`. La chaîne de caractères peut utiliser `{dir}`, `{user}`, `{host}` qui seront remplacés à la volée. Pour plus d'informations, consultez l'exemple de fichier [.absrc](https://github.com/abs-lang/abs/blob/d1e92899ed0d6b3abb7a0a3fc6ec18d13dbe3ff2/tests/test-absrc.abs)

### Corrections de bugs

Comme d'habitude, nous avons réussi à corriger quelques bugs mineurs en cours de route :

* correction de quelques paniques aléatoires lors de l'appel de fonctions intégrées sans suffisamment d'arguments ([#193](https://github.com/abs-lang/abs/pull/193))
* les commandes Windows utilisent désormais cmd.exe plutôt que bash, car bash pourrait ne pas être disponible sur le système ([#180](https://github.com/abs-lang/abs/pull/180))
* meilleurs messages d'erreur lors de l'analyse de nombres "invalides" ([#182](https://github.com/abs-lang/abs/pull/182))
* l'installateur ABS ne fonctionnait pas avec wget 1.20.1 ([#178](https://github.com/abs-lang/abs/pull/178))
* l'analyseur ABS prend désormais en charge les nombres en notation scientifique (par exemple, 8.366100560806463e-7, [#174](https://github.com/abs-lang/abs/pull/174))
* les erreurs sur les fonctions intégrées ne rapportaient pas les numéros de ligne/colonne d'erreur corrects ([#168](https://github.com/abs-lang/abs/pull/168))

### Et maintenant ?

Installez ABS avec une simple commande :

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

… et commencez à scripter comme si c'était 2019 !

PS : Encore une fois, un grand merci à [Erich](https://github.com/ntwrick), qui a pris un rôle de plus en plus important au fil des semaines. Sans lui, beaucoup des choses incluses dans la version 1.2 ne seraient pas possibles !

PPS : [La version 1.3.0 est déjà bien avancée](https://github.com/abs-lang/abs/milestone/10) — attendez-vous à la voir à un moment donné en avril. Nous introduirons des fonctionnalités extrêmement intéressantes telles que la possibilité de tuer des commandes en arrière-plan, donc ce sera une version passionnante !

_Publié à l'origine sur [odino.org](https://odino.org/abs-1-dot-2-background-commands-and-the-ability-to-import-files/) (21 mars 2019)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ 😊