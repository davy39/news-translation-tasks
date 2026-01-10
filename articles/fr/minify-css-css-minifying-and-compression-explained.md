---
title: Minifier le CSS – Minification et compression du CSS expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-18T15:20:23.000Z'
originalURL: https://freecodecamp.org/news/minify-css-css-minifying-and-compression-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-magda-ehlers-2590535.jpg
tags:
- name: compression
  slug: compression
- name: CSS
  slug: css
- name: optimization
  slug: optimization
seo_title: Minifier le CSS – Minification et compression du CSS expliquées
seo_desc: "By Dillion Megida\nMinification is the process of reducing code size to\
  \ reduce the size of your files. So how does this apply to CSS?\nTake a look at\
  \ this code:\nh1 {\n  color: yellow;\n}\n\np {\n  color: pink;\n}\n\nAnd the compressed\
  \ version of it:\nh1 { color..."
---

Par Dillion Megida

La minification est le processus de réduction de la taille du code pour réduire la taille de vos fichiers. Alors, comment cela s'applique-t-il au CSS ?

Jetez un coup d'œil à ce code :

```css
h1 {
  color: yellow;
}

p {
  color: pink;
}
```

Et la version compressée de celui-ci :

```css
h1 { color: yellow; } p { color: pink; }
```

Ces deux blocs de code sont identiques et fonctionnent de la même manière car ils ont la syntaxe CSS correcte. Mais il y a deux différences entre ces blocs de code :

* le premier est plus lisible et compréhensible par rapport au second avec une seule ligne
* le premier résulte en une taille de fichier plus grande par rapport au second.

En testant cela sur mon ordinateur, le premier a une taille de **46 octets** tandis que le second est de **40 octets**. Cette différence peut sembler insignifiante, mais elle devient notable lorsque l'on considère la différence qu'une version compressée d'une base de code plus grande peut faire.

## Pourquoi la taille compressée est-elle importante ?

Lorsque le navigateur reçoit un document HTML d'un serveur, il récupère les ressources liées dans le document. Ces ressources incluent des images, des scripts et aussi des feuilles de style.

Plus un fichier CSS est grand, plus il nécessite de ressources (comme la bande passante réseau) pour être téléchargé. De plus, plus il faut de temps pour télécharger de tels fichiers. Cela entraîne des temps de chargement de page plus lents et affecte l'expérience utilisateur globale.

Ces coûts peuvent être ignorés pour les petits fichiers CSS, mais à mesure qu'un programme grandit, la compression devient un facteur essentiel pour améliorer les temps de chargement des pages.

## Tout ce dont le navigateur a besoin est un CSS valide, pas un CSS lisible ou formaté

Les tailles de fichiers compressés n'affectent pas la manière dont le navigateur analyse le CSS. Le navigateur n'a pas besoin de CSS lisible pour pouvoir l'interpréter sur une page web. Il a seulement besoin de CSS valide (code CSS avec une syntaxe correcte – accolades, points-virgules, etc.).

Par conséquent, les espaces supplémentaires, les commentaires et les indentations n'ont pas d'importance pour le navigateur. Ils ne comptent que pour le développement.

Pour les applications déployées, vous avez besoin d'une version **distribuable** du CSS.

La version **distribuable** n'est pas destinée à être lue par les humains ou utilisée pendant le développement – mais plutôt utilisée pour les applications déployées car elles ne comptent que pour le navigateur.

## Comment fonctionne le CSS minifié ?

Le but de la minification est de supprimer les parties de votre code CSS qui sont sans importance pour le navigateur afin d'interpréter le CSS.

Par exemple, ce code :

```css
h1 {
  /* un en-tête */
  color: yellow;
}
```

Voici une présentation graphique des parties du code qui comptent et de celles qui ne comptent pas :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-85.png)

Les commentaires de code peuvent aider les développeurs à travailler ensemble, à se souvenir pourquoi des décisions sont prises et à comprendre le but des différentes parties du code. Mais le navigateur n'a pas besoin de ces informations.

Les espaces et l'indentation améliorent la lisibilité du code par les humains, mais le navigateur peut lire le code sans espaces.

Le sélecteur d'élément, les accolades et le point-virgule sont des parties essentielles du code car ils suivent la syntaxe CSS et aident le navigateur à interpréter correctement le code.

Les méthodes de minification CSS prennent ces parties dont le navigateur n'a pas besoin dans le code, ce qui résulte en un fichier de taille réduite, et rend plus rapide pour le navigateur le téléchargement de tels fichiers depuis le serveur.

La version minifiée du code ci-dessus est :

```css
h1{color:yellow;}
```

Et tout fonctionne toujours parfaitement sur le navigateur.

## Comment minifier le CSS

Maintenant que vous comprenez la pertinence des fichiers CSS compressés et leur fonctionnement, comment minifiez-vous vos fichiers CSS ?

Bien sûr, vous ne pouvez pas écrire de code CSS minifié pendant le développement car cela rend la collaboration, la lecture et la compréhension du code difficiles.

Voici quelques outils que vous pouvez utiliser pour minifier votre CSS.

### clean-css

[clean-css](https://www.npmjs.com/package/clean-css) est une bibliothèque NPM que vous pouvez utiliser pour minifier vos fichiers CSS localement ou depuis un serveur distant.



![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-88.png)

### Minifier CSS de Dan's Tools

[Minifier CSS de Dan's Tools](https://www.cleancss.com/css-minify/) est un outil en ligne de minification CSS pour minifier le CSS. Vous pouvez coller le CSS dans un champ d'entrée, entrer une URL où se trouve le fichier CSS, ou coller le fichier CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-86.png)
_Capture d'écran de la page Minifier CSS de Dan's Tools_

### Minifier CSS de Toptal

[Minifier CSS de Toptal](https://www.toptal.com/developers/cssminifier/) fournit une interface utilisateur pour ajouter votre CSS et voir la sortie minifiée. Il fournit également une API et des plugins qui automatisent le processus.


![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-87.png)
_Capture d'écran du Minifier CSS de Toptal_

Il existe plus d'outils et de configurations que vous pouvez appliquer pour rendre le processus plus facile – ceci n'est qu'un aperçu.

## Conclusion

La minification, en général, est une excellente approche pour optimiser les sites web. La minification des fichiers CSS augmente les temps de chargement des pages et nécessite moins de ressources par le navigateur pour le téléchargement.

Pendant le développement, les commentaires, l'indentation et d'autres formes de formatage améliorent la lisibilité et la collaboration du code. Mais le navigateur n'en a pas besoin.

La minification CSS est le processus de compression des tailles de fichiers CSS en supprimant les parties sans importance des fichiers dont le navigateur n'a pas besoin pour interpréter sur une page web.

Heureusement, certains outils facilitent cela, afin que vous puissiez profiter du processus de développement et obtenir également une version distribuable à la fin.