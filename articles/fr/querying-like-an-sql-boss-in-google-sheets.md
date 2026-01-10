---
title: Comment interroger des données dans Google Spreadsheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-06-16T16:32:35.000Z'
originalURL: https://freecodecamp.org/news/querying-like-an-sql-boss-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/querying-2.jpg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: google sheets
  slug: google-sheets
seo_title: Comment interroger des données dans Google Spreadsheets
seo_desc: 'I built a spreadsheet and wanted to display some of the data in a small
  table which would update based on the day of the week.

  After some digging, querying seemed the best option to pull this off.

  In this article, you''ll learn several things about Go...'
---

J'ai créé une feuille de calcul et je voulais afficher certaines des données dans un petit tableau qui se mettrait à jour en fonction du jour de la semaine.

Après quelques recherches, l'interrogation semblait être la meilleure option pour y parvenir.

Dans cet article, vous apprendrez plusieurs choses sur les tableaux, fonctions, requêtes, validation des données et mise en forme de Google Sheets, notamment :

1. Créer un tableau de données propre et utilisable.
2. Créer une liste déroulante de validation des données
3. Nommer des plages pour une utilisation plus facile et une gestion des données plus propre
4. Les bases des requêtes, y compris SELECT, WHERE et les fonctions TEXT() et TODAY()
5. La syntaxe particulière pour référencer des cellules dans les requêtes de Google Sheets
6. Où aller dans la documentation officielle pour plus d'informations.

## Google Sheets est similaire à SQL

Google Sheets dispose effectivement d'un "Google Visualization API Query Language" intégré. Consultez la documentation [ici](https://developers.google.com/chart/interactive/docs/querylanguage).

Une partie de la syntaxe est la même et une grande partie de la fonctionnalité est similaire à SQL, donc vous devriez le comprendre rapidement si vous êtes familier avec SQL.

Je ne connais que peu de choses en SQL, mais j'ai pu comprendre quelques requêtes de base sans trop de difficulté.

En fait, la chose qui m'a posé le plus de problèmes était la **syntaxe de référence des cellules**. Et j'espère que cet article peut vous éviter quelques grattages de tête que j'ai eus aujourd'hui.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/barney-head-scratch.gif)
_Barney se grattant la tête_

## Installez votre tableau

Premièrement : mettez toutes les données dans un tableau bien organisé. C'est parfois la partie la plus difficile de toute analyse de données : simplement obtenir les données dans un format ordonné et utilisable.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/neat-2.png)
_tableau de données_

J'ai utilisé la validation des données pour les jours de la semaine afin de m'assurer qu'il n'y avait pas de faute de frappe, car notre requête dépendra de ces jours.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-83.png)
_validation des données_

## Créez une plage nommée

Sélectionnez l'ensemble du tableau pour créer une plage nommée. Cela rendra les choses plus propres et plus faciles à l'étape suivante. C'est une bonne pratique de garder les données aussi ordonnées que possible.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-75.png)
_plage nommée_

Confirmez et nommez la plage pour la sauvegarder.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-76.png)
_confirmation de la plage nommée_

## Comment écrire la requête

Maintenant, créons une autre feuille pour y mettre notre requête. Je n'ai besoin que de deux colonnes pour nos données : une pour la personne et une pour la tâche. Faites de la place pour plus si vos données l'exigent.

La première étape nécessite un petit truc pour faire afficher le jour actuel lorsque la feuille est chargée et pour que cela soit utilisé dans notre requête.

Il existe une fonction intégrée `=Today()`, mais l'utiliser seule ne suffit pas, même lorsque vous changez le formatage. La requête ne la reconnaîtra pas comme correspondant au texte des jours de la semaine dans notre tableau.

Au lieu de cela, enveloppez la fonction `Today()` à l'intérieur de la fonction `Text()` comme montré ci-dessous. La fonction `Text()` accepte un nombre et un format comme arguments. Lorsque nous lui passons `Today()`, elle peut convertir ce nombre de date en texte en utilisant le format `"dddd"`. Sympa, non ? 😊

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-79.png)
_fonctions text() et today()_

Dans Google Sheets, `=QUERY` est également une fonction intégrée. Lorsque vous la tapez dans la cellule (`B22` dans mon exemple), vous pouvez cliquer sur la flèche déroulante en haut à droite pour obtenir plus d'informations sur les paramètres acceptés.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/more-info.png)
_paramètres de la fonction Query_

Nous allons sélectionner nos données. Tapez le nom de la plage que vous avez créée et elle sélectionnera automatiquement ce tableau.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-77.png)

Vous pouvez sélectionner manuellement la plage pour le tableau à interroger si vous le souhaitez. Mais vous voulez être aussi génial que possible, alors utilisez cette plage nommée ! 👌

Nous voulons sélectionner et retourner les deux premières colonnes (les noms et les tâches) dans notre feuille de données en fonction de la quatrième colonne (le jour de la semaine).

La requête se lit `=QUERY(heat,"select B,C where D='"&B21&"'",1)`.

Et oui, cette laideur avec les guillemets simples, les guillemets doubles et les esperluettes est nécessaire pour la déclaration conditionnelle que nous créons.

Nous disons à la requête de faire correspondre la colonne D dans notre feuille de données avec la valeur dans `B21` qui est maintenant du texte grâce à notre formule précédente manipulant le jour de la semaine.

La syntaxe pour faire correspondre le texte dans la cellule est désagréable, mais c'est simplement comme ça que vous devez le faire.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-80.png)
_Fonction Query_

Ce dernier paramètre `1)` indique à la requête qu'il y a une ligne d'en-têtes à afficher (nom, tâche).

Et, voilà ! Nous avons une liste de tâches qui se met à jour automatiquement en fonction du jour actuel de la semaine. Il ne reste plus qu'à nettoyer le résultat final ! 🎁

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-82.png)

## Exemples officiels

J'ai référencé [cet article](https://support.google.com/docs/answer/3093343?hl=en) de la page de la fonction QUERY sur le support Google pour apprendre, et il contient une feuille Google que vous pouvez copier avec un tas d'exemples. Super utile.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/ex.png)

## Ma feuille de calcul d'exemple

[Voici la feuille](https://docs.google.com/spreadsheets/d/1oO5SMyVlk2KbqXmW534JH2kYSoqfP1IgVf80KRwpQgY/edit?usp=sharing) que j'ai créée pour cet article. Vous êtes libre d'en faire une copie et de l'utiliser vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/copy.png)
_faire une copie de la feuille Google_

## Merci d'avoir lu !

J'écris sur le design et le développement web du point de vue d'un solopreneur sur [https://blog.eamonncottrell.com/](https://blog.eamonncottrell.com/) et vous pouvez me trouver sur Twitter : [https://twitter.com/EamonnCottrell](https://twitter.com/EamonnCottrell)

Passez une excellente journée ! 🎉

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bye.gif)
_au revoir !_