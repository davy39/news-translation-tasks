---
title: Comment transformer du JSON en CSV avec jq en ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-14T14:57:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-transform-json-to-csv-using-jq-in-the-command-line-4fa7939558bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9v1EW10o8um03EbAdinhYg.png
tags:
- name: command line
  slug: command-line
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment transformer du JSON en CSV avec jq en ligne de commande
seo_desc: 'By Knut Melvær

  The shell tool jq is awesome for dealing with JSON-data. It can also transform that
  data into handy CSV-files, ready for all your spreadsheet wrangling needs.

  jq is an excellent little tool that lives in your terminal and does useful s...'
---

Par Knut Melvær

L'outil shell jq est génial pour manipuler des données JSON. Il peut également transformer ces données en fichiers CSV pratiques, prêts pour tous vos besoins de manipulation de feuilles de calcul.

`jq` est un excellent petit outil qui vit dans votre terminal et fait des choses utiles avec les données JSON. C'est un outil puissant, mais aussi pratique pour les petites choses. Par exemple, si vous pipez des données JSON vers lui, il les imprime avec une coloration syntaxique par défaut :

`$ cat some-data.json|jq`

Vous pouvez [installer jq](https://stedolan.github.io/jq/download/) sur la plupart des systèmes. (`brew install jq` sur un Mac avec [homebrew](https://brew.sh/) / `chocolatey install jq` sur Windows avec [chocolatey](https://chocolatey.org/)). Cet article présente une technique plus avancée de `jq`. Si vous voulez apprendre les bases, vous devriez [consulter le tutoriel](https://stedolan.github.io/jq/tutorial/).

`jq` fonctionne avec n'importe quelle source JSON. Puisque je passe la plupart de mes journées à travailler avec des backends basés sur [Sanity.io](https://sanity.io?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq), je vais utiliser cela comme exemple. Aussi parce que je pense que c'est immensément cool ce que nous pouvons faire avec cette combinaison.

[Sanity est un backend pour le contenu structuré](https://?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq) et vient avec une API en temps réel, et un langage de requête appelé [GROQ](https://www.sanity.io/docs/data-store/how-queries-work?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq). Vous pouvez interagir avec Sanity via [HTTP](https://www.sanity.io/docs/reference/http-api?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq) et [JS/PHP clients](https://github.com/sanity-io/sanity#api-clients), mais aussi avec l'outil CLI avec `$ sanity documents query 'GROQ-expression'`.

![Image](https://cdn-media-1.freecodecamp.org/images/RS3kI4oS3QmUl6XYU0JWUst09IJGXi2oLJFd)
_Sortie de sanity.io pipée à travers jq_

Donc, si vous voulez vos documents de type `post`, vous mettez `$ sanity documents query '*[_type == "post"]'`. Ou si vous voulez uniquement ceux avec une date de publication en 2018, c'est `$ sanity documents query '*[_type == "post" && publishedAt > "2018-01-01"]'`. Cette requête vous donne des documents complets. Si vous vouliez uniquement les titres et les dates de publication, vous écriviez : `*[_type == "post"]{title, publishedAt}`.

![Image](https://cdn-media-1.freecodecamp.org/images/isYCXU3wUsZ9ucMhJyY1CRYaPjmSIeX66y8B)
_La sortie de Sanity CLI pipée à travers jq_

Vous pouvez également extraire des clés et des valeurs des données JSON dans `jq`. Aujourd'hui, nous allons l'utiliser pour transformer du contenu structuré dans un tableau JSON en un fichier CSV. Parce que votre patron veut des trucs dans des feuilles Excel, n'est-ce pas ? Accrochez-vous, et plongeons ! 🚀

Disons que vous voulez une liste des titres, slugs et dates de publication de vos entrées de blog dans une feuille de calcul. L'expression complète ressemblerait à ceci :

```
sanity documents query '*[_type == "post"]{title, "slug": slug.current, publishedAt}'|jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv'
```

Vous pouvez copier cela et l'exécuter ou [jouer avec sur jqplay.com](https://jqplay.org/s/QOs3d_fMLU), mais voyons ce qui se passe dans l'expression `jq` :

* `-r` est pour `--raw-output` et garantit que la sortie est du texte simple sans couleurs ni formatage spécial.
* `(map(keys) | add | unique) as $cols` itère (`map`) à travers les clés de votre objet et `add` les clés `unique` à une variable appelée `$cols`. En d'autres termes, c'est ainsi que vos en-têtes de colonne sont créés.

![Image](https://cdn-media-1.freecodecamp.org/images/e6sn55BOmzgF2Zkd1DW510oi4vLKhnSQVAjw)
_Map out unique keys to use as column headers_

* `map(. as $row | $cols | map($row[.])) as $rows` prend tous les objets dans le tableau externe, et itère à travers toutes les clés de l'objet (title, slug, publishedAt). Il ajoute les valeurs à un tableau, ce qui vous donne un tableau de tableaux avec les valeurs, ce que vous voulez lorsque vous transformez du JSON en CSV.
* `$cols, $rows[] | @csv` place les en-têtes de colonne en premier dans le tableau, puis chacun des tableaux qui sont transformés en lignes en les pipant à `@csv`, qui formate la sortie en... csv.

![Image](https://cdn-media-1.freecodecamp.org/images/TjZbfS7LCA033RdEiJ45l5-qBGIeQyVG9tAF)
_Le résultat final_

Cette commande imprime le résultat dans le shell. Si vous voulez l'écrire directement dans un fichier, vous pouvez ajouter `> filename.csv` à la fin, ou, par exemple, dans le presse-papiers (pipez-le `to | pbcopy` si vous êtes sur macOS). Ou peut-être ferez-vous quelque chose d'excitant avec le csv [in pan](https://pandas.pydata.org/)das 🐼 en Python ?

Si vous avez trouvé cela utile, nous aimerions en entendre parler dans la section des commentaires !

Si vous voulez essayer Sanity.io, vous pouvez aller sur [sanity.io/freecodecamp](https://sanity.io/freecodecamp?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq) et obtenir un plan développeur gratuit amélioré. ✨

_Publié à l'origine sur [sanity.io](https://www.sanity.io/blog/exporting-your-structured-content-as-csv-using-jq-in-the-command-line?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq)._