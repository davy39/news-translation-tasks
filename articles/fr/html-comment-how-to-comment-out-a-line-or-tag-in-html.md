---
title: Commentaire HTML – Comment commenter une ligne ou une balise en HTML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-29T17:03:35.000Z'
originalURL: https://freecodecamp.org/news/html-comment-how-to-comment-out-a-line-or-tag-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-pixabay-268351.jpg
tags:
- name: best practices
  slug: best-practices
- name: HTML
  slug: html
seo_title: Commentaire HTML – Comment commenter une ligne ou une balise en HTML
seo_desc: 'In this article, you''ll learn how to add single and multi-line comments
  to your HTML documents.

  You''ll also see why comments are considered a good practice when writing HTML code.

  Let''s get started!

  The HTML Comment Tag

  The general syntax for an HTML...'
---

Dans cet article, vous apprendrez à ajouter des commentaires sur une seule ligne et sur plusieurs lignes à vos documents HTML.

Vous verrez également pourquoi les commentaires sont considérés comme une bonne pratique lors de l'écriture de code HTML.

Commençons !

## La balise de commentaire HTML

La syntaxe générale pour un commentaire HTML ressemble à ceci :

```html
<!-- Je suis un commentaire ! -->
```

Les commentaires en HTML commencent par `<!--` et se terminent par `-->`.

N'oubliez pas le point d'exclamation au début de la balise ! Mais vous n'avez pas besoin de l'ajouter à la fin.

La balise entoure tout texte ou toute autre balise HTML que vous souhaitez commenter.

## Quand utiliser les commentaires HTML

Les commentaires HTML ne s'affichent pas dans le navigateur. Cela signifie que tout commentaire que vous ajoutez à votre code source HTML ne sera pas affiché lorsque le document sera rendu dans un navigateur web.

Cela dit, gardez à l'esprit que n'importe qui peut consulter le code source de pratiquement tous les sites web publiés sur Internet en allant dans `View -> Developer -> View Source` – et cela inclut également tous les commentaires !

Ainsi, vos commentaires seront visibles pour les autres si vous rendez le document HTML public et qu'ils choisissent de regarder le code source.

Écrire des commentaires est utile et c'est une bonne pratique à suivre lors de l'écriture de code source. Les commentaires vous aident à documenter et à communiquer sur votre code et votre processus de réflexion pour vous-même (et pour les autres). Cela vous rappelle également ce que vous pensiez/faisiez lorsque vous revenez à un projet après des mois sans y avoir travaillé.

Les commentaires vous aident également à communiquer avec d'autres développeurs qui travaillent sur le projet avec vous. Vos commentaires peuvent clairement leur expliquer pourquoi vous avez ajouté certaines lignes de code.

## Comment écrire des commentaires sur une seule ligne en HTML

Un commentaire sur une seule ligne ne s'étend que sur une seule ligne. Comme mentionné précédemment, cette ligne ne s'affichera pas dans le navigateur.

Utilisez un commentaire sur une seule ligne lorsque vous souhaitez expliquer et clarifier le but du code qui suit ou lorsque vous souhaitez ajouter des rappels pour vous-même comme ceci :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- Ajouter la barre de navigation ici -->
    <h2>À propos de moi</h2>
    <p>J'apprends à coder avec freeCodeCamp.</p>
    <p>Je passe en revue chacune de leurs certifications formidables et super utiles.</p>
    <p>Je suis en route pour devenir un développeur web fullstack !</p>
    <h3>Expérience professionnelle</h3>
</body>
</html>
```

Les commentaires sur une seule ligne sont également utiles lorsque vous souhaitez indiquer clairement où une balise se termine. Cela s'avère pratique dans un document HTML long et complexe où beaucoup de choses se passent et où vous pourriez être confus quant à l'emplacement d'une balise de fermeture.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <section class="contact">
    </section> <!-- balise de fermeture de la section contact est ici -->
</body>
</html>
```

## Comment écrire des commentaires en ligne en HTML

Vous pouvez également ajouter des commentaires au milieu d'une phrase ou d'une ligne de code.

Seul le texte à l'intérieur de `<!-- -->` sera commenté, et le reste du texte à l'intérieur de la balise ne sera pas affecté.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Je suis <!-- sur le point de devenir --> un développeur web</p>
</body>
</html>
```

## Comment écrire des commentaires sur plusieurs lignes en HTML

Les commentaires peuvent également s'étendre sur plusieurs lignes, en utilisant la même syntaxe que vous avez vue jusqu'à présent.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Je suis un développeur web</p>
    <!-- Ceci va être mon portfolio.
    Il présentera les projets dont je suis le plus fier.
    Je pourrais continuer à parler de ce que je veux ajouter
    parce que j'écris un commentaire sur plusieurs lignes ici -->
</body>
</html>
```

## Comment commenter une balise en HTML

Alors, que faire si vous souhaitez commenter une balise en HTML ?

Vous entourez la balise que vous avez sélectionnée avec `<!-- -->`, comme ceci :

```html

!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Ma page de portfolio</h2>
    <h3>Projets de certification freeCodeCamp</h3>
    <!-- <section class="hero">
    </section>  -->
    <h2>À propos de moi</h2>
</body>
</html>
```

Commenter des balises aide au débogage.

Lorsque quelque chose ne fonctionne pas comme prévu ou comme vous l'aviez prévu, commencez à commenter les balises individuelles une par une. Cela vous permet de les tester et de voir laquelle cause le problème.

## Raccourci clavier pour ajouter des commentaires HTML

Il existe des raccourcis que vous pouvez utiliser pour ajouter des commentaires – et vous les utiliserez probablement beaucoup. Le raccourci est `Command /` pour les utilisateurs de Mac ou `Control /` pour les utilisateurs de Windows et Linux.

Pour ajouter un commentaire sur une seule ligne, maintenez simplement la combinaison de touches indiquée ci-dessus à l'intérieur de l'éditeur de code. Ensuite, toute la ligne sur laquelle vous vous trouvez sera commentée. Gardez simplement à l'esprit que, puisque tout sera commenté sur cette ligne, cela ne fonctionne que pour les commentaires sur une seule ligne. Vous devrez ajouter des commentaires en ligne manuellement.

Pour ajouter des commentaires sur plusieurs lignes, sélectionnez et surlignez tout le texte ou les balises que vous souhaitez commenter et maintenez les deux touches indiquées précédemment. Chaque ligne que vous avez sélectionnée aura maintenant un commentaire.

## Conclusion

Et voilà – vous savez maintenant comment et pourquoi utiliser des commentaires en HTML !

Apprenez-en plus sur HTML en regardant les vidéos suivantes sur la chaîne YouTube de freeCodeCamp :

- [Tutoriel HTML - Cours intensif sur les sites web pour débutants](https://www.youtube.com/watch?v=916GWv2Qs08)
- [Cours complet sur HTML - Tutoriel pour créer un site web](https://www.youtube.com/watch?v=pQN-pnXPaVg)

freeCodeCamp propose également une certification gratuite basée sur des projets sur le [Responsive Web Design](https://www.freecodecamp.org/learn/responsive-web-design/).

Elle est idéale pour les débutants complets et ne suppose aucune connaissance préalable. Vous commencerez par les bases absolues nécessaires et développerez vos compétences au fur et à mesure. À la fin, vous complèterez cinq projets.

Merci d'avoir lu et bon apprentissage :)