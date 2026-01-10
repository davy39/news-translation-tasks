---
title: Bash Sleep – Comment faire attendre un script shell N secondes (Exemple de
  commande)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-13T14:29:40.000Z'
originalURL: https://freecodecamp.org/news/bash-sleep-how-to-make-a-shell-script-wait-n-seconds-example-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels
seo_title: Bash Sleep – Comment faire attendre un script shell N secondes (Exemple
  de commande)
---

--------------------1560424.jpg
tags:
- name: Bash
  slug: bash
- name: script shell
  slug: script-shell
seo_title: null
seo_desc: "Par Veronica Stork\nLorsque vous écrivez un script shell, vous pouvez avoir besoin\n  \ qu'il attende un certain nombre de secondes avant de continuer. Par exemple,\
  \ vous pouvez vouloir que le script attende qu'un processus se termine ou avant de réessayer\
  \ une commande échouée. \n..."
---

Par Veronica Stork

Lorsque vous écrivez un script shell, vous pouvez avoir besoin qu'il attende un certain nombre de secondes avant de continuer. Par exemple, vous pouvez vouloir que le script attende qu'un processus se termine ou avant de réessayer une commande échouée. 

Pour cela, vous pouvez utiliser la commande très simple `sleep`. 

## Comment utiliser la commande Bash Sleep

`Sleep` est une commande très polyvalente avec une syntaxe très simple. Il suffit de taper `sleep N`. Cela mettra en pause votre script pendant `N` secondes, où `N` peut être un entier positif ou un nombre à virgule flottante. 

Considérez cet exemple de base :

```
echo "Bonjour !"
sleep 2
echo "Oups ! Je me suis endormi pendant quelques secondes !"
```

Le résultat de ce script ressemblera à ceci :

![gif du script en cours d'exécution](https://www.freecodecamp.org/news/content/images/2021/09/2021-09-10-22.33.49.gif)

De même, vous pouvez utiliser un nombre à virgule flottante pour représenter des fractions de secondes. Par exemple, `sleep .8` mettra en pause votre script pendant 0,8 seconde. 

C'est tout pour l'utilisation de base de la commande `sleep` ! 

## Ce qu'il faut garder à l'esprit lors de l'utilisation de la commande Sleep

L'unité de temps par défaut de `Sleep` est les **secondes**, c'est pourquoi nous n'avons pas besoin de spécifier une unité dans les exemples ci-dessus. 

Sur certains types de machines (notamment les systèmes BSD et MacOS), la seule unité de temps prise en charge est les secondes. D'autres systèmes d'exploitation de type Unix prendront probablement en charge les unités de temps suivantes :

* `s` : secondes
* `m` : minutes
* `h` : heures
* `d` : jours

Il est également possible d'utiliser plus d'un argument avec la commande `sleep`. Si deux nombres ou plus sont inclus, le système attendra pendant une durée équivalente à la somme de ces nombres.

Par exemple, `sleep 2m 30s` créera une pause de 2 minutes et demie. Notez que pour obtenir le même résultat sur une machine MacOS ou BSD, vous exécuteriez la commande équivalente `sleep 150`, car 2 minutes et 30 secondes équivalent à 150 secondes. 

## Conclusion

La commande `sleep` est un moyen utile d'ajouter des pauses dans votre script Bash. Utilisée en conjonction avec d'autres commandes, `sleep` peut vous aider à créer une alarme minutée, à exécuter des opérations dans le bon ordre, à espacer les tentatives de connexion à un site web, et plus encore. Alors ajoutez cet outil simple mais puissant à votre boîte à outils Bash et continuez à coder !