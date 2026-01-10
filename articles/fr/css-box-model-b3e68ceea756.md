---
title: Déballer les bases du modèle de boîte CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T21:12:27.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-b3e68ceea756
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1ch1pHZSb3YDog3PlZ7oFQ.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Déballer les bases du modèle de boîte CSS
seo_desc: 'By Bryan Smith

  Understanding the CSS Box Model is crucial in being able to master how elements
  are laid out on a page. In the most basic of terms, the Box Model is as follows:
  margin, border, padding and content. But what does that all mean? How do t...'
---

Par Bryan Smith

Comprendre le modèle de boîte CSS est crucial pour maîtriser la disposition des éléments sur une page. En termes les plus basiques, le modèle de boîte est le suivant : marge, bordure, remplissage et contenu. Mais que signifie tout cela ? Comment ces termes fonctionnent-ils ensemble ?

_Bref._

Dans l'article de cette semaine, nous allons plonger directement dans le sujet et vous faire sentir comme un maître du modèle de boîte. Styliser des éléments et leur donner un espacement approprié à gauche et à droite (et en haut et en bas... vous voyez ? Parce que vous disposez vos éléments sur la page ?... désolé pour les mauvaises blagues).

Jetez un coup d'œil à cette décomposition visuelle fournie par la console Chrome :

![Image](https://cdn-media-1.freecodecamp.org/images/0*fL7IZ5XJwHsQth-a.png)
_Vous pouvez voir cette visualisation en cliquant avec le bouton droit sur votre page dans Chrome (ou votre navigateur de choix), en cliquant sur Inspecter pour ouvrir la console de développement, en sélectionnant l'onglet Styles et en faisant défiler jusqu'en bas._

Vous pouvez voir que chaque partie du modèle de boîte est étiquetée pour vous, sauf le contenu — c'est la boîte bleue au milieu. Décomposons comment chaque partie fonctionne et les différences uniques entre elles.

### Marge

Vous pouvez penser à la marge comme une zone tampon pour votre élément. Vous voulez un peu d'espace autour de votre élément ? C'est à cela que sert la marge. Imaginons que vous avez un rhume. Vous devriez (espérons-le) rester à l'écart des gens pour ne pas le propager. Vous avez besoin d'une marge autour de vous. Jetez un coup d'œil à cette image pour illustrer davantage :

![Image](https://cdn-media-1.freecodecamp.org/images/0*oN7zT5zI3B4lfjED.png)

Remarquez comment vos amis sont tous éloignés de vous et que vous êtes entouré d'orange ? C'est la marge en action. Vous restez de la même taille, mais il y a une zone d'exclusion pour tout ce qui vous entoure. Il en va de même pour les éléments sur votre page. La marge donnera de l'espace autour de votre élément et gardera les choses séparées. Pour faire simple, la marge ajoutera un espacement invisible autour de votre élément sans affecter directement sa taille. Dans cet exemple, nous l'avons rendu orange pour vous donner un indice visuel de sa position par rapport au contenu (un vous malade dans ce cas).

### Bordure

La bordure est la deuxième propriété depuis le bord extérieur de votre élément. La bordure, comme vous l'avez peut-être deviné, est utilisée pour définir un bord visuel à votre élément. La bordure augmentera la taille de présentation de votre élément ou la partie visible à l'écran. Il peut encore y avoir une marge impliquée, mais elle sera sur le bord extérieur de la bordure. Regardons à nouveau vous être malade, mais cette fois avec une petite bordure impliquée :

![Image](https://cdn-media-1.freecodecamp.org/images/0*0SJmRV2kv6hOH4uw.png)

Cela ressemble presque à la démonstration de la marge précédente, sauf qu'il y a maintenant une boîte noire autour. C'est notre bordure. Une chose à retenir est que notre contenu (l'emoji malade) est maintenant de la taille de l'emoji plus la bordure de chaque côté.

Bon, assez avec l'emoji malade. Parlons du remplissage.

### Remplissage

Le remplissage est le troisième élément depuis le bord extérieur. Et, comme la marge et la bordure avant lui, il est totalement optionnel. La chose la plus importante à garder à l'esprit lorsque vous essayez de trouver la différence entre la marge et le remplissage est que le remplissage AUGMENTERA la taille de présentation de votre élément.

Imaginons que votre grand-mère vous envoie un cadeau d'anniversaire. Elle l'emballe et l'envoie par la poste. Maintenant, comme votre grand-mère ne veut pas que votre cadeau soit endommagé pendant l'envoi, elle ajoute vraiment à l'emballage. Voici une visualisation de ce que je veux dire :

![Image](https://cdn-media-1.freecodecamp.org/images/0*4BcD7TiSsoCxd2fo.png)

Vous recevez le cadeau et supposez que grand-mère a tout donné et vous a acheté une télévision de 60 pouces.

Faux.

Elle a simplement ajouté un peu de remplissage (vous voyez ce que j'ai fait là ?) à la boîte, ce qui lui a fait prendre plus de place et paraître plus grande.

Laissez-moi vous donner un exemple de codage pertinent. Vous créez un `<div>` qui fait 100px de large par 100px de haut. Vous ajoutez 10px de remplissage à chaque bord, et maintenant `ce` <div> fait 120px de large par 120px de haut à cause du remplissage ajouté de chaque côté. Gardez cela à l'esprit lorsque vous disposez les éléments de votre page.

### Contenu

Contenu, contenu, contenu. C'est ce dont notre page est faite. Le contenu est la façon dont vous le décrivez initialement dans votre CSS ou sa hauteur naturelle si vous utilisez une image. Vous avez créé un `<div>` qui fait 50px de large par 300px de haut ? C'est la quantité d'espace qu'il occupera sur votre écran s'il n'est pas modifié par l'une des parties ci-dessus du modèle de boîte. Le contenu est le cadeau que votre grand-mère vous a donné, c'est l'emoji malade.

### Dimensionnement de la boîte

Je serais négligent si je ne mentionnais pas `box-sizing: border-box` maintenant. Je ne veux pas entrer trop dans les détails, mais il existe une propriété CSS appelée `box-sizing` qui par défaut a pour valeur `content-box`. Jetez un coup d'œil à ce CodePen pour démontrer. Les enfants n'ont aucun respect pour le conteneur parent, s'étendant hors de celui-ci.

Et maintenant avec le pouvoir qu'est `box-sizing: border-box` :

Les enfants sont maintenant contenus à l'intérieur du parent (et font probablement leurs corvées et rentrent à l'heure pour le couvre-feu). Le CSS est exactement le même dans chaque démonstration, sauf pour un petit ajout dans la deuxième :

```
*, *:before, *:after {   box-sizing: border-box; }
```

Ces trois lignes de code disent à chaque élément de notre page de calculer leur largeur et leur hauteur avec la bordure et le remplissage ajoutés, alors que la première démonstration était un désordre sans respect pour personne ou quoi que ce soit. Le remplissage et la bordure étaient ajoutés à la largeur et débordaient hors du conteneur parent.

### Conclusion

Le modèle de boîte est fondamental pour comprendre comment les éléments seront disposés sur votre page. Espérons que vous avez maintenant une excellente compréhension de comment le modèle de boîte fonctionne et comment vous pouvez l'utiliser à votre avantage. J'espère aussi que cela signifie que vous n'aurez plus à taper "margin: 10px;...[attendre les changements de page...supprimer, supprimer, supprimer] padding: 10px...".

_Publié à l'origine sur [www.frontamentals.com](https://www.frontamentals.com/css-box-model).