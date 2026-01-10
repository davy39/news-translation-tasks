---
title: "Rechercher et remplacer dans Notepad++ \x13 Comment trouver une chaîne avec\
  \ une expression régulière dans Notepad++"
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-05T13:21:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-string-with-regular-expression-in-notepad-find-and-replace-in-notepad
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/findAndReplacewithRe.png
tags:
- name: Regex
  slug: regex
seo_title: "Rechercher et remplacer dans Notepad++ \x13 Comment trouver une chaîne\
  \ avec une expression régulière dans Notepad++"
seo_desc: "Notepad++ has a Find feature with which you can search for any text in\
  \ a file. But it doesn’t end there. \nYou can also use Notepad++'s Find and Replace\
  \ feature to search for a text and replace it with a specified replacement.\nThe\
  \ Find and Find and Re..."
---

Notepad++ dispose d'une fonctionnalité **Rechercher** avec laquelle vous pouvez rechercher n'importe quel texte dans un fichier. Mais ce n'est pas tout. 

Vous pouvez également utiliser la fonctionnalité **Rechercher et Remplacer** de Notepad++ pour rechercher un texte et le remplacer par un remplacement spécifié.

Les fonctionnalités **Rechercher** et **Rechercher et Remplacer** acceptent le texte ordinaire, mais elles acceptent également les expressions régulières.

Voyons comment fonctionnent les fonctionnalités **Rechercher** et **Rechercher et Remplacer** de Notepad++ en utilisant des expressions régulières au lieu de texte ordinaire.


## Comment trouver une chaîne avec des expressions régulières dans Notepad++
Voici le code que j'utiliserai pour cette démonstration :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Trouver une chaîne avec RegEx dans Notepad++</title>
  </head>
  <body>
    <h1>Trouver une chaîne avec RegEx dans Notepad++</h1>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius beatae
      dignissimos alias quo odit aperiam laborum accusamus ea maxime dolores?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae voluptatem
      perferendis iure laborum inventore ducimus harum saepe voluptatibus neque
      earum?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam
      accusantium placeat dolore illo, quidem suscipit. Recusandae corrupti
      assumenda soluta libero!
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>

    <h2>Lorem ipsum dolor sit.</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate
      officia rerum id inventore sunt deleniti quaerat quibusdam libero vero
      non?
    </p>
  <h3>Lorem ipsum dolor sit amet.</h3>
  </body>
</html>
```

Une fois que vous avez ouvert votre fichier dans Notepad++, appuyez sur `CTRL + H` pour ouvrir la fenêtre contextuelle **Rechercher**. Assurez-vous d'être dans l'onglet **Rechercher** car l'onglet **Remplacer** est celui qui s'ouvre par défaut. 

Ensuite, sélectionnez **Expression régulière** :

![ss1-3](https://www.freecodecamp.org/news/content/images/2023/05/ss1-3.png) 

Ensuite, entrez votre expression régulière dans le champ de recherche. Je veux rechercher tous les éléments de titre, donc je vais entrer l'expression régulière `<h(1|2|3|4|5|6)>`

Après avoir entré l'expression régulière, cliquez sur le bouton Rechercher suivant. Il peut également apparaître sous le nom "Rechercher" :

![ss2-1](https://www.freecodecamp.org/news/content/images/2023/05/ss2-1.png) 

Pour continuer à voir les correspondances, vous devez continuer à cliquer sur le bouton "Rechercher suivant". Cependant, vous pouvez cliquer sur le bouton "Compter" pour voir toutes vos correspondances :

![ss3-1](https://www.freecodecamp.org/news/content/images/2023/05/ss3-1.png) 


## Comment trouver et remplacer une chaîne avec des expressions régulières dans Notepad++
Vous pouvez effectuer une recherche et un remplacement presque de la même manière. La seule différence est que vous sélectionnez l'onglet "Remplacer" au lieu de "Rechercher" :

![ss4-1](https://www.freecodecamp.org/news/content/images/2023/05/ss4-1.png)

L'expression régulière de recherche est automatiquement remplie, donc ce que vous devez faire ici est de spécifier par quoi remplacer les correspondances et de cliquer sur **Remplacer**. 

Supposons que je veux remplacer tous les titres par une balise `p` :

![ss5-2](https://www.freecodecamp.org/news/content/images/2023/05/ss5-2.png) 

Au lieu de cliquer sur "Remplacer" plusieurs fois pour remplacer les correspondances, vous pouvez cliquer sur le bouton "Remplacer tout" :

![ss6-1](https://www.freecodecamp.org/news/content/images/2023/05/ss6-1.png) 

Je vais également trouver toutes les balises de fermeture de titre avec cette expression régulière ` <\/h(1|2|3|4|5|6)>` et les remplacer par des balises de fermeture `p`.

Voici à quoi ressemble le code maintenant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Trouver une chaîne avec RegEx dans Notepad++</title>
  </head>
  <body>
    <p>Trouver une chaîne avec RegEx dans Notepad++</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius beatae
      dignissimos alias quo odit aperiam laborum accusamus ea maxime dolores?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae voluptatem
      perferendis iure laborum inventore ducimus harum saepe voluptatibus neque
      earum?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam
      accusantium placeat dolore illo, quidem suscipit. Recusandae corrupti
      assumenda soluta libero!
    </p>
	<p>Lorem ipsum dolor sit amet.</p>

    <p>Lorem ipsum dolor sit.</p>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate
      officia rerum id inventore sunt deleniti quaerat quibusdam libero vero
      non?
    </p>
	<p>Lorem ipsum dolor sit amet.</p>
  </body>
</html>
```


## Conclusion
Rechercher et Remplacer est une excellente fonctionnalité qui vous fait gagner beaucoup de temps dans Notepad++, surtout si vous devez remplacer du texte dans un grand fichier.

Puisque VS Code est l'éditeur de code le plus populaire ces jours-ci, il dispose également de sa propre fonctionnalité de recherche et de remplacement à laquelle vous pouvez accéder en appuyant sur `CTRL + H`. Et si vous voulez rechercher avec des expressions régulières, vous pouvez appuyer sur le bouton `.*` :

![ss7-1](https://www.freecodecamp.org/news/content/images/2023/05/ss7-1.png)

Merci d'avoir lu.