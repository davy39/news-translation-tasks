---
title: Les Répertoires de Fichiers Expliqués en s'Habillant le Matin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-24T21:37:44.000Z'
originalURL: https://freecodecamp.org/news/file-directories-explained-by-getting-dressed-in-the-morning-2f5d0a69cdde
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ST1cC7voeyDyuOWGubNMgw.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les Répertoires de Fichiers Expliqués en s'Habillant le Matin
seo_desc: 'By Kevin Kononenko

  If you get dressed for work or school in the morning, then you can understand file
  directories.

  When you are building your first website with HTML, CSS and JavaScript, you only
  need a very simple file directory.

  You have one folder...'
---

Par Kevin Kononenko

**Si vous vous habillez pour le travail ou l'école le matin, alors vous pouvez comprendre les répertoires de fichiers.**

Lorsque vous construisez votre premier site web avec HTML, CSS et JavaScript, vous n'avez besoin que d'un répertoire de fichiers très simple.

Vous avez un dossier avec trois fichiers au total, et peut-être un ou deux fichiers image si vous utilisez une image de fond ou un logo.

Mais, à mesure que votre site grandit, vous devrez commencer à utiliser plusieurs dossiers pour organiser vos différents fichiers. Et, si vous écrivez votre propre back-end en utilisant un langage comme Node.js ou Ruby on Rails, alors vous devrez être encore plus concentré sur l'organisation.

Voici le problème : vous devez utiliser des préfixes comme « / » et « ../ » pour faire référence à différents dossiers dans votre répertoire. Ces brefs préfixes ne vous donnent absolument aucun indice sur ce qu'ils font réellement !

Les répertoires de fichiers sont en fait assez similaires à la façon dont une chambre est organisée. Donc, si vous êtes habitué à vérifier plusieurs endroits chaque jour avant le travail pour assembler une tenue, alors vous pouvez comprendre comment naviguer dans les répertoires de fichiers.

Alors, plongeons-nous dans le sujet ! Pour comprendre ce guide, vous devez simplement connaître la différence entre HTML, CSS et JavaScript. [Vous pouvez consulter notre guide ici](https://blog.codeanalogies.com/2018/05/09/the-relationship-between-html-css-and-javascript-explained/).

### L'Installation d'un Répertoire de Fichiers

Imaginons que vous avez une chambre avec une penderie et des tiroirs pour ranger vos vêtements. Vous vous réveillez tous les jours à 7h, et vous devez préparer une tenue pour le travail.

Dans ce cas, les vêtements sont comme des fichiers individuels, tandis que les différentes parties de votre chambre sont comme des dossiers, puisqu'ils contiennent les vêtements. Appelons le dossier de niveau supérieur « /chambre ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*4tREPBNuyL6ADG0FIUI25A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tCzVTBq2cFAc4gYdAgLcPg.jpeg)

Supposons que vous portiez un costume pour aller au travail. Votre costume est accroché dans la penderie, tandis que vos chemises sont dans les tiroirs. Votre costume est comme un fichier HTML, tandis que vos chemises sont comme des fichiers CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0brd9T7rlUzB2-GJ1dw6eQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EoK-fLFWf9nkClyi7Ei8FQ.jpeg)

Dans ce cas, « /chambre » est le **répertoire** entier, tandis que « /penderie » et « /tiroirs » sont des **sous-répertoires**. Et les fichiers eux-mêmes sont contenus dans le sous-répertoire. « /chambre » est le **répertoire de niveau supérieur** ou **racine** ici puisqu'il contient l'ensemble de notre projet.

Réfléchissons à la façon dont vous pourriez vous habiller.

1. Se réveiller
2. Aller à la penderie et choisir une tenue
3. Quitter la penderie
4. Aller aux tiroirs
5. Prendre d'autres vêtements qui compléteront la tenue, comme une chemise à col et des chaussettes

De même, lorsque vous créez un fichier HTML, vous devez trouver un moyen de connecter votre fichier CSS pour ajouter les styles.

1. Commencer au fichier HTML
2. Quitter le dossier (si nécessaire)
3. Accéder au dossier qui contient les fichiers CSS
4. Référencer le fichier HTML spécifique que vous allez utiliser

Voici une note importante. Lorsque vous souhaitez connecter un fichier HTML à un fichier CSS, vous commencez votre navigation dans le répertoire de fichiers à partir du fichier HTML lui-même. Tout comme choisir une tenue, vous naviguez d'un vêtement à un autre. Vous **ne** commencez pas au répertoire racine.

Voici le code pour lier votre fichier workoutfit.html à votre fichier de chemise blanche.

```
<link rel="stylesheet" type="text/css" href="/tiroirs/chemiseblanche.css">
```

Voici les étapes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RDfVmxOgweTNS7C1)

Il pourrait donc être plus judicieux de diviser ce chemin en trois parties distinctes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ESCTx-EdCRBBxVs482f0pg.jpeg)

1. **/** — nous renvoie au dossier racine
2. **tiroirs** — nous ouvrons le dossier tiroirs dans le dossier racine
3. **/chemiseblanche.css** — c'est le fichier réel que nous voulons connecter, dans le dossier tiroirs

### Comment Accéder aux Fichiers dans le Même Dossier

La plupart du temps, vous essayerez d'accéder à des fichiers à partir d'autres dossiers dans votre répertoire. À mesure que votre projet grandit, cela sera particulièrement important pour garder une trace de tous les différents fichiers utilisés.

Mais parfois, vous accéderez à des fichiers à partir du même sous-répertoire. Cela est courant lorsque votre projet est à un stade précoce — un fichier HTML, un fichier CSS et un fichier JavaScript (plus des images).

Dans ce cas, le chemin est beaucoup plus simple. Revenons à notre exemple de chambre, et imaginons que vous devez également choisir une cravate pour votre tenue. Cette cravate est également rangée dans la penderie.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ws2QYEzv7VD5beK7)

Nous voulons donc maintenant lier deux feuilles de style distinctes à notre fichier HTML. Une dans le même dossier, une dans un dossier séparé. C'est une pratique courante lorsque vous avez une feuille de style générale qui est partagée entre de nombreux fichiers HTML.

```
<link rel="stylesheet" type="text/css" href="cravate.css"> <link rel="stylesheet" type="text/css" href="/tiroirs/chemiseblanche.css">
```

Remarquez comment _cravate.css_ n'a aucun préfixe. Le chemin du fichier est simplement le nom du fichier et le suffixe. Cela signifie que le fichier est dans le même sous-répertoire que le fichier HTML. C'est comme chercher dans votre penderie et prendre deux articles qui sont côte à côte.

### Une Dernière Façon de Naviguer dans Votre Répertoire

Une fois que votre application devient plus grande, vous pourriez avoir besoin de plusieurs niveaux de sous-répertoires pour stocker tous les différents types de scripts, feuilles de style et images. Jusqu'à présent, nous n'avons couvert qu'une seule façon de naviguer dans cela : en revenant complètement au répertoire racine, et en accédant aux fichiers à partir de là.

Mais cela peut créer des chemins de fichiers longs, et cela introduit la possibilité de confusion et de bugs lorsqu'une autre personne examine votre code.

Parfois, il est plus facile de travailler en arrière, un sous-répertoire à la fois. C'est là que le préfixe « ../ » entre en jeu.

Réorganisons notre penderie pour voir comment plusieurs niveaux de dossiers peuvent être utilisés. Maintenant, dans notre penderie, il y aura un dossier _porte_cravates_ pour contenir le fichier _cravate.css_, et un dossier _cintres_ pour contenir _tenuedetravail.html_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zx0mKUlQqivPDUUY)

Nous voulons toujours connecter notre fichier cravate.css à tenuedetravail.html. Mais il n'est pas très logique de revenir au répertoire racine et de naviguer ensuite jusqu'au dossier _porte_cravates_.

Au lieu de cela, nous pouvons utiliser le préfixe ../ pour revenir en arrière d'un dossier, puis naviguer vers porte_cravates.

![Image](https://cdn-media-1.freecodecamp.org/images/0*I0wmgDIWCB6WPe2Y)

Et voici le code.

```
<link rel="stylesheet" type="text/css" href="../porte_cravates/cravate.css">
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*O3cj8DVh78w_YMBo)

Cela rend notre code un peu plus maintenable. Par exemple, que se passerait-il si nous changions une partie de la structure du répertoire à un niveau supérieur ? Alors tous nos chemins de fichiers seraient rompus, et nous serions obligés de partir à la chasse aux chemins rompus. Cela rend plus probable que nous pourrons maintenir notre code. Vous pouvez même enchaîner plus d'un. « ../../ » signifie que vous devez monter de **deux** niveaux dans votre répertoire.

### Utiliser l'Inspecteur Chrome pour Voir les Sites en Direct

Une fois que votre site est en ligne, ces fichiers seront hébergés en utilisant la même structure sur un serveur. Cela signifie que si la structure fonctionne localement... elle devrait également fonctionner en direct.

Vous pouvez utiliser l'Inspecteur Chrome (ou les outils de développement dans le navigateur de votre choix) pour vérifier cela. Par exemple, si vous allez sur codeanalogies.com et inspectez le logo en haut à gauche, voici ce que vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/0*LIQgu_fn1Mc93xj0)

Cela signifie que je stocke le logo principal de mon site dans un dossier appelé _img_. Il est situé un niveau en dessous du dossier racine.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GDPpDuOgAEvUAlVq)

D'autres sites peuvent utiliser un CDN pour stocker des actifs statiques. [Vous pouvez en lire plus à ce sujet ici](https://blog.codeanalogies.com/2018/06/11/web-caching-explained-by-buying-milk-at-the-supermarket/).

### Obtenez Plus de Tutoriels Visuels

Avez-vous apprécié ce guide ? Donnez-lui un « clap », ou inscrivez-vous ici pour recevoir mes dernières explications visuelles sur les sujets de développement web :