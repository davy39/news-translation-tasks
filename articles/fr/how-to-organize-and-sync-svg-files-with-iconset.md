---
title: Comment organiser et synchroniser des fichiers SVG avec Iconset
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-09-08T15:47:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-organize-and-sync-svg-files-with-iconset
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/iconset.jpg
tags:
- name: Icons
  slug: icons
- name: Productivity
  slug: productivity
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: Comment organiser et synchroniser des fichiers SVG avec Iconset
seo_desc: "SVG is an awesome way to bring vector images into a design and development\
  \ workflow. But collecting and organizing SVG files on your computer can be challenging.\
  \ \nHow can Iconset help take away the pain and get us more productive?\n\nWhat\
  \ is SVG?\nWhat ..."
---

SVG est une excellente façon d'intégrer des images vectorielles dans un flux de travail de conception et de développement. Mais collecter et organiser des fichiers SVG sur votre ordinateur peut être un défi.

Comment Iconset peut-il nous aider à éliminer les difficultés et à améliorer notre productivité ?

* [Qu'est-ce que SVG ?](#heading-qu-est-ce-que-svg)
* [Qu'est-ce qu'Iconset ?](#heading-qu-est-ce-qu-iconset)
* [Que allons-nous apprendre ?](#heading-que-allons-nous-apprendre)
* [Partie 1 : Commencer avec Iconset](#heading-partie-1-commencer-avec-iconset)
* [Partie 2 : Ajouter des icônes à Iconset](#heading-partie-2-ajouter-des-icones-a-iconset)
* [Partie 3 : Utiliser Iconset avec des logiciels de conception comme Figma](#heading-partie-3-utiliser-iconset-avec-des-logiciels-de-conception-comme-figma)
* [Partie 4 : Utiliser Iconset en développement comme avec React](#heading-partie-4-utiliser-iconset-en-developpement-comme-avec-react)
* [Partie 5 : Synchroniser Iconset sur plusieurs ordinateurs avec Dropbox](#heading-partie-5-synchroniser-iconset-sur-plusieurs-ordinateurs-avec-dropbox)

%[https://youtu.be/KXBf5l4rbL4]

## Qu'est-ce que SVG ?

[SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) est un format de fichier image qui existe depuis près de 20 ans. Bien qu'il existe depuis un certain temps, il ne gagne en popularité dans la communauté du développement que récemment.

SVG est génial pour plusieurs raisons. Tout d'abord, c'est un format vectoriel, ce qui signifie qu'il peut être redimensionné à la taille souhaitée.

Mais il est également flexible, car vous pouvez utiliser SVG directement dans votre projet de développement avec une taille de fichier généralement petite et une mise à l'échelle infinie. Vous pouvez même [l'animer](https://frontend.horse/issues/6/#slash) !

Mais essayer de collecter et d'organiser un ensemble de fichiers peut être un défi. Comment les nommer ? Avez-vous un ordinateur qui peut facilement les prévisualiser ? Et pour la recherche ?

## Qu'est-ce qu'Iconset ?

[Iconset](https://iconset.io/) est un outil gratuit multiplateforme qui vous permet de collecter et de gérer tous vos fichiers SVG en un seul endroit.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-font-awesome.jpg)
_Bibliothèque Iconset_

Vous aimez passer rapidement de [Font Awesome](https://fontawesome.com/) à [heroicons](https://heroicons.com/) mais vous ne voulez pas changer constamment de bibliothèque ? Vous pouvez utiliser Iconset pour effectuer une recherche rapide et glisser l'icône directement dans votre projet.

Si vous prévoyez de l'utiliser pour un projet [React](https://reactjs.org/), vous pouvez même copier le fichier en tant que JSX et l'intégrer directement dans votre projet !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-copy-as.jpg)
_Iconset "Copier en tant que"_

## Que allons-nous apprendre ?

Nous allons passer en revue plusieurs scénarios qui nous montreront comment Iconset est utile.

Nous allons également voir comment vous pouvez facilement gérer Iconset entre différents ordinateurs ou environnements afin d'avoir la même bibliothèque partout où vous travaillez.

## Partie 1 : Commencer avec Iconset

Pour commencer, vous devez d'abord installer Iconset localement. Le processus d'installation devrait être similaire à celui de toute autre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-no-icons.jpg)
_Iconset sans icônes_

Une fois qu'il est prêt et disponible localement, vous devriez pouvoir l'ouvrir et voir une interface avec "Aucune icône", ce qui est attendu, car il ne vient avec aucune icône préinstallée.

## Partie 2 : Ajouter des icônes à Iconset

Ajouter des icônes à Iconset est aussi simple que de les glisser-déposer, mais vous avez quelques options pendant le processus.

Pour commencer, téléchargeons l'ensemble d'icônes gratuit [heroicons](https://heroicons.com/).

Télécharger à : [https://heroicons.com/](https://heroicons.com/).

Sur le site web de heroicons, vous devriez voir un grand bouton "Télécharger tout", qui téléchargera un fichier zip contenant toutes les icônes.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/download-heroicons.jpg)
_Téléchargement de heroicons_

Si vous naviguez vers le dossier optimisé, vous verrez qu'il existe deux versions différentes : solid et outline.

Pour les importer dans Iconset, sélectionnez chaque dossier individuellement et glissez-le directement dans Iconset.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-drag-in-icons.gif)
_Glisser-déposer heroicons dans Iconset_

Une fois là, vous avez quelques options.

* **Set** : Comme c'est notre premier ensemble, vous créerez automatiquement un nouveau. Si vous aviez des ensembles existants, vous pourriez importer dans ceux-ci.
* **Nom de l'ensemble** : Ici, nous pouvons nommer l'ensemble de manière à ce que nous nous en souvenions. Pour cela, je recommande de le nommer "heroicons - Outline".
* **Options d'importation** : ce sont des paramètres optionnels, mais je sélectionne généralement les options d'optimisation et de nettoyage pour m'assurer que toutes les icônes sont immédiatement prêtes à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-heroicons.jpg)
_Iconset avec l'ensemble heroicons_

Et une fois que vous cliquez sur Importer, il fera son travail, et vous aurez maintenant votre premier ensemble d'icônes dans Iconset !

Vous pouvez faire de même avec le dossier solid afin d'avoir nos deux ensembles prêts à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-heroicons-solid-outline.jpg)
_Iconset avec les ensembles Outline et Solid de heroicons_

À ce stade, vous pouvez utiliser Iconset pour rechercher parmi vos icônes et voir tous les fichiers actuellement disponibles dans votre collection.

## Partie 3 : Utiliser Iconset avec des logiciels de conception comme Figma

L'un des grands avantages d'Iconset est la facilité avec laquelle vous pouvez l'utiliser avec des logiciels de conception comme [Figma](http://figma.com/).

Si je veux ajouter une icône d'enveloppe à mon site web pour que les gens puissent me contacter, je peux rechercher l'icône de courrier et simplement la glisser sur ma toile :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-drag-icon-into-figma.gif)
_Glisser-déposer l'icône de courrier dans Figma_

Je peux ensuite la traiter comme n'importe quel autre élément de conception vectorielle et l'utiliser immédiatement dans mon projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/svg-icon-in-figma.jpg)
_Icône de courrier SVG dans Figma_

## Partie 4 : Utiliser Iconset en développement comme avec React

Une autre fonctionnalité intéressante est la facilité avec laquelle vous pouvez l'utiliser dans un projet comme React.

Dès le départ, vous avez plusieurs façons de copier le fichier et de l'utiliser en développement, comme le copier en tant que JSX.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-starter-sass.jpg)
_Next.js Sass Starter_

Si je pense que mon [Next.js Sass Starter](https://github.com/colbyfayock/next-sass-starter) pourrait utiliser quelques icônes sur la page, je peux faire un clic droit sur n'importe quelle icône que je veux et, sous "Copier en tant que", sélectionner JSX pour la coller directement dans mon projet !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-copy-icon-as-jsx.gif)
_Copier une icône d'Iconset en tant que JSX_

Et bien qu'elle ait besoin d'un peu de style une fois que vous l'avez insérée, comme n'importe quelle autre image ou icône, elle est immédiatement prête à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/svg-icon-nextjs-project.jpg)
_Utilisation d'une icône JSX dans une application Next.js React_

## Partie 5 : Synchroniser Iconset sur plusieurs ordinateurs avec Dropbox

Avec Iconset, vous avez la possibilité de basculer entre différentes bibliothèques. Mais surtout, vous pouvez également définir l'emplacement de votre bibliothèque.

Lorsque Iconset crée votre bibliothèque, il stocke tout sous forme de fichiers et d'une base de données sur votre ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-location.jpg)
_Dossier de la bibliothèque Iconset_

Et dans l'interface utilisateur d'Iconset, nous pouvons à la fois déplacer et changer l'emplacement que nous utilisons.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-settings.jpg)
_Paramètres de la bibliothèque Iconset_

Si c'est la première fois que vous configurez Iconset, vous pouvez commencer par cliquer sur "Déplacer" puis en sélectionnant l'emplacement où vous souhaitez le synchroniser.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-move-location.jpg)
_Déplacement de l'emplacement de la bibliothèque Iconset_

Et une fois que vous cliquez sur "Déplacer", il le déplacera vers ce répertoire, comme un dossier sur Dropbox, et le synchronisera avec le cloud comme n'importe quel autre dossier et fichier.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-sync-to-dropbox.jpg)
_Synchronisation de la bibliothèque Iconset avec Dropbox_

Alternativement, si vous avez déjà une bibliothèque Iconset partagée ou si vous configurez cela sur un nouvel ordinateur, vous pouvez utiliser l'option "Changer", et sélectionner cette option directement depuis Dropbox.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-switch-locations.jpg)
_Changement de l'emplacement d'Iconset_

Et une fois que vous avez cliqué sur "Changer", vous chargerez maintenant votre bibliothèque partagée et serez prêt à être productif.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-full-library.jpg)
_Iconset avec une bibliothèque complète_

## Que pouvez-vous faire d'autre ?

### Publier et partager des ensembles d'icônes

Une autre fonctionnalité intéressante est que vous pouvez exporter des ensembles et les partager. Si vous avez passé beaucoup de temps sur une collection et que vous souhaitez la partager avec d'autres, exportez-la, publiez-la et partagez-la avec la communauté !

### Plus d'organisation

Iconset prend également en charge des fonctionnalités comme les dossiers et les favoris. Cela rend encore plus facile le regroupement et la collecte des icônes de la manière qui vous convient pour rester productif.

Il prend également en charge le marquage, ce qui facilite encore plus la recherche.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4e93ff Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>