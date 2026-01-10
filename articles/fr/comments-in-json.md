---
title: "Commentaires dans JSON \x13 Commenter dans un fichier JSON"
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-31T15:10:51.000Z'
originalURL: https://freecodecamp.org/news/comments-in-json
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--1-.png
tags:
- name: json
  slug: json
seo_title: "Commentaires dans JSON \x13 Commenter dans un fichier JSON"
seo_desc: 'JSON (JavaScript Object Notation) is a popular data interchange format
  used in web development and mobile applications due to its simplicity and flexibility.

  But JSON files do not officially support comments. This makes providing additional
  context o...'
---

JSON (JavaScript Object Notation) est un format d'change de donnes populaire utilis dans le dveloppement web et les applications mobiles grce  sa simplicit et sa flexibilit.

Mais les fichiers JSON ne supportent pas officiellement les commentaires. Cela rend difficile l'ajout de contexte ou d'explications supplmentaires pour les donnes.

Cet article vous montrera comment inclure des commentaires dans les fichiers JSON et pourquoi JSON ne supporte pas nativement les commentaires.

## Pourquoi JSON ne supporte pas les commentaires ?

Selon la spcification JSON, un document JSON ne doit contenir que des structures de donnes comme des tableaux et des objets, et ne doit pas inclure de commentaires. Cela est d au fait que JSON est destin  tre un format de donnes simple et facilement analysable, qui peut tre trait rapidement et efficacement.

Les commentaires, bien qu'utiles pour fournir un contexte ou une explication supplmentaire pour les lecteurs humains, peuvent ajouter de la complexit au processus d'analyse. Cela ralentit les performances et augmente le risque d'erreurs.

La raison principale pour laquelle JSON ne supporte pas les commentaires est que son crateur, [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford), les a dlibrment supprims du format pour viter les mauvaises utilisations et le maintenir comme un format de donnes pur.

Crockford a observ que certaines personnes utilisaient les commentaires pour stocker des directives d'analyse, ce qui pouvait rompre la compatibilit entre diffrents systmes. Par consquent, la dcision de supprimer les commentaires pour maintenir la simplicit et la cohrence du format dans divers langages de programmation et environnements.

En rsultat, la seule option pour ajouter des commentaires  un fichier JSON est d'utiliser une solution de contournement, telle que l'utilisation d'lments personnaliss pour stocker les commentaires.

## Comment ajouter des commentaires dans JSON

Lorsque vous ajoutez des commentaires sous la forme `//`, `#`, ou `/* */`, qui sont utiliss dans les langages de programmation populaires, vous remarquerez l'erreur Les commentaires ne sont pas autoriss dans JSON.

![](https://paper-attachments.dropboxusercontent.com/s_7788E690364D593F2C3E31F8D1CF26EB90DAC0141414EE29BD5F57C061BD4347_1680020901125_image.png align="left")

Alors, comment pouvez-vous ajouter des commentaires  un fichier JSON ?

La seule faon de le faire est d'inclure des commentaires sous forme de paires de donnes dans un fichier JSON. Ce n'est pas une pratique couramment utilise ou recommande, mais techniquement, c'est la meilleure faon d'ajouter des commentaires  votre fichier JSON.

Crez un lment personnalis dans votre objet JSON, tel que "\_comment", pour les distinguer du reste des donnes.

```json
{
    "_comment": "Placez votre commentaire JSON ici",
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "isMarried": true,
    "occupation": "Software Engineer",
}
```

**Note :** Il n'est pas obligatoire d'utiliser des underscores. Vous pouvez dcider d'utiliser deux barres obliques telles que //comment ou tout autre caractre autoris. **Le but est de rendre clair que c'est un commentaire**.

Il est important de noter que cette approche peut rendre le fichier JSON plus complexe et plus difficile  analyser. Mais si les commentaires sont ajouts sous forme d'lments personnaliss, ils seront reus et traits comme toute autre donne dans JSON ct serveur.

Vous savez maintenant comment ajouter techniquement des commentaires  votre fichier JSON. Mais comment pouvez-vous ajouter plusieurs commentaires ? Cela est possible, mais vous devez vous souvenir que JSON ne permet pas de cls d'objet en double. Vous devez inclure des lettres ou des chiffres uniques dans l'lment de commentaire, en veillant  ce qu'il soit valide et distinguable des autres lments dans le fichier JSON.

```json
{
    "_comment1": "Ce sont les donnes de base",
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "_comment2": "Informations maritales",
    "isMarried": true,
    "wifeName": "Jane Doe"
}
```

Lorsque vous avez des objets JSON imbriqus, vous pouvez utiliser des cls d'objet similaires :

```json
{
    "_comment": "Ce sont les donnes de base",
    "name": "John Doe",
    "age": 35,
    "city": "New York City",
    "maritalInfo": {
        "_comment": "Informations maritales",
        "isMarried": true,
        "wifeName": "Jane Doe"
    }
}
```

## Conclusion

Vous savez maintenant comment ajouter des commentaires  votre fichier JSON. Mais parce que ces commentaires sont galement traits et peuvent tre consults, vous devez tre prudent lorsque vous ajoutez des commentaires aux fichiers JSON en utilisant des lments personnaliss.

Merci d'avoir lu. Amusez-vous bien en codant !