---
title: Comment construire facilement la barre de navigation de Mashable avec HTML
  et CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T17:51:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-build-mashables-navigation-bar-with-html-and-css-9e5007af786
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1h5VsMH4IW1T-ejq9p4c4g.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
seo_title: Comment construire facilement la barre de navigation de Mashable avec HTML
  et CSS
seo_desc: 'By Codesmith

  When you visit wecodejs.com, you might think to yourself, “Man, what a navigation
  bar. What a big, beautiful navigation bar. It’s winning.”

  And then you go to your code editor and can’t seem to get your blob of HTML elements
  to resemble ...'
---

Par Codesmith

Lorsque vous visitez wecodejs.com, vous pourriez vous dire : « Wow, quelle barre de navigation. Quelle grande et belle barre de navigation. Elle est géniale. »

Puis vous allez dans votre éditeur de code et vous n'arrivez pas à faire ressembler votre amas d'éléments HTML à cette grande et belle barre de navigation.

Écrire du CSS, c'est comme se faire soigner une carie, pensez-vous. En fait, cela pourrait tout aussi bien être de la magie.

Eh bien, ce n'est pas de la magie. Vous pouvez styliser une « barre de navigation » ou tout autre composant web facilement. Tout ce que vous avez à faire, c'est changer votre façon de voir le CSS.

### Élément, qu'es-tu ?

La première chose à clarifier est l'idée que le CSS ne sert qu'à embellir les choses. C'est la mauvaise façon d'aborder un projet CSS, car cela vous distrait de ce à quoi le CSS sert vraiment. À un niveau très basique, nous utilisons le CSS pour organiser les éléments sur une page web.

Maintenant, qu'est-ce qu'un élément ? Voici comment le MDN définit un élément HTML :

> Un **élément** est une partie d'une page web. En [XML](https://developer.mozilla.org/en-US/docs/Glossary/XML) et [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML), un élément peut contenir un élément de données ou un morceau de texte ou une image, ou peut-être rien. Un élément typique inclut une balise d'ouverture avec certains [attributs](https://developer.mozilla.org/en-US/docs/Glossary/Attribute), un contenu textuel enfermé, et une balise de fermeture.

Beurk. Cela ne nous aide pas vraiment. La définition de W3Schools est plus directe : « Tous les éléments HTML peuvent être considérés comme des boîtes. »

C'est incroyable ! Non, sérieusement, cela ne peut pas être assez souligné. Il est très facile de simplement passer outre cette déclaration lorsque vous vous battez avec le CSS. Si nous pouvons conceptualiser que chaque élément HTML que nous créons est une nouvelle boîte, nous pouvons mieux comprendre le rôle du CSS dans l'arrangement de ces boîtes.

Soudainement, le « modèle de boîte » prend tout son sens. Je suis sûr que vous l'avez déjà vu auparavant.

![Image](https://cdn-media-1.freecodecamp.org/images/43HeLouo7GKAT8qwQHK04-tAf25aVZZ0cpft)
_w3schools_

Les propriétés de remplissage (padding), de bordure et de marge aident toutes à donner une forme à nos boîtes. Nous utilisons le remplissage pour créer l'image visuelle de la boîte, une bordure pour délimiter son périmètre, et une marge pour la séparer de toutes les autres boîtes.

Maintenant, comment cela s'applique-t-il à notre problème de barre de navigation ? Commençons à coder pour le découvrir. Nous allons recréer la barre de navigation de Mashable sans les icônes de menu déroulant et les icônes sociales (c'est pour un autre tutoriel). Assurez-vous de coder en même temps, car c'est la meilleure façon d'apprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/qU4ZygWrljDt44qqdJQtCN6fxE7SoQ13kA-d)
_Regardez tous ces quadrilatères ! Commentez ci-dessous le nombre de boîtes sur cette page_

### Planifier, planifier, planifier

Commencer un projet avec une liste de contrôle nous aide à écrire du code organisé. Normalement, nous créerions un wireframe, mais nous avons déjà un modèle sur lequel travailler.

**HTML :**

1. Créer un élément nav qui contient tous les éléments d'onglet
2. Créer des éléments d'onglet
3. Identifier l'onglet le plus haut comme un logo

**CSS :**

1. Définir la couleur de la barre de navigation sur une teinte de bleu
2. Définir la couleur de la boîte d'onglet sur une teinte plus claire de bleu
3. Définir les polices dans les boîtes d'onglet en sans-serif et les colorer en blanc
4. Définir la police et les propriétés de la boîte du logo.

### Une histoire de deux barres de navigation

Il semble que nous soyons prêts à coder, mais attendez ! Vous souvenez-vous lorsque nous avons mentionné « amas d'HTML » plus tôt ? Eh bien, vous voulez réfléchir aux éléments que vous souhaitez utiliser pour créer votre barre de navigation. Une façon de l'écrire en HTML est de créer une liste non ordonnée :

![Image](https://cdn-media-1.freecodecamp.org/images/TbdCFWwj9opFZ24sZKmL4Vv01rDO62bnSva6)

sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/WWBFowjXamo4ehCQB1AJTY61KS9mjMBPJpCD)

Si vous débutez avec CSS, cela peut ressembler à un amas immuable. Nous n'avons même pas ajouté de liens, ce qui signifie que nous devons imbriquer des éléments.

Voici une approche plus simple pour créer une barre de navigation tout en gardant notre balisage sémantique :

![Image](https://cdn-media-1.freecodecamp.org/images/SrrLbBisu3vB9tw-XWEyKJ7H9mfot8IdrKQJ)

![Image](https://cdn-media-1.freecodecamp.org/images/7y6SIBwgWUszE1MOnTPH9mICAgBahIMJPeDc)
_Tout est bien arrangé pour nous grâce aux ancres !_

Comme vous pouvez le voir, nous avons créé une barre de navigation simplement en utilisant HTML. Maintenant, tout ce que nous avons à faire est d'implémenter le modèle de boîte pour les espacer. Utilisons le second modèle HTML pour créer la barre de navigation de Mashable, puis nous fournirons un guide sur la façon de la styliser correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/e8JSOBDcujnMPrbqiXGdapUCleJlHgsI3iCb)
_Remarquez comment nous utilisons un id pour différencier le logo._

### CSS à la rescousse

Maintenant, organisons ces boîtes avec un peu de CSS. Nous allons lister tous les sélecteurs dont nous aurons besoin pour cette tâche.

```
/* nous ciblerons toute la nav */nav {}
```

```
/* nous ciblerons un onglet spécifique */  nav a { }
```

```
/* nous allons utiliser une pseudo-classe CSS pour changer la couleur de fond lorsque nous survolons un onglet */  nav a:hover {  }/* nous allons cibler le logo pour quelques styles spécifiques car le logo est super spécial */  #logo {  }
```

La première chose que nous devrions faire est de définir la largeur et la hauteur de notre nav, et d'ajouter un peu de couleur. Une excellente ressource pour une roue chromatique est disponible [ici](https://www.sessions.edu/color-calculator/).

```
nav {  width: 100%; // la largeur doit être en pourcentage pour la réactivité  height: 38px; // la hauteur doit être en px. Ajustez à votre convenance  background-color: #0b98de;// le code couleur hexadécimal doit être utilisé
```

```
}  nav a { }  nav a:hover {  }  #logo {  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/d9WAQfv3BpbUea3QM2oHYkNU8HNs-OFl21FU)

Nous avons notre barre de navigation ! Ensuite, commençons à créer des boîtes que nous pourrons déplacer. Nous pouvons le faire en affichant les éléments comme des blocs.

```
nav {  width: 100%;  background-color: #0b98de;
```

```
}  nav a {    display: block;     
```

```
 }  nav a:hover {  }  #logo {  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/cAVvhInyvKOpxuU0w91q6NQ1TW1cM2YxAwn2)

Il semble que nous ayons cassé notre belle nav. Nous n'avions pas nécessairement besoin de faire cela, mais aligner nos éléments est beaucoup plus facile lorsque nous pouvons traiter chaque élément comme un bloc. Pour corriger cela, nous écrivons simplement `float: left;`. Cela nous ramènera à la case départ.

**Note :** cette étape peut être ignorée, **mais** si vous utilisez une liste non ordonnée, alors elle doit être implémentée.

Maintenant, créons les boîtes. Si vous regardez le modèle de boîte, vous remarquerez que le remplissage est ce qui crée ces boîtes. Si vous voulez voir comment cela fonctionne et tester la taille de vos boîtes, définissez une `background-color` et `border:` dans le sélecteur `nav a`.

```
  nav a {    display: block;    float: left;/* Nous configurons simplement les paramètres de police ici */
```

```
    font-family: sans-serif;    font-size: 9px;    color: white;
```

```
/* Méthode de test de boîte AKA handicap */
```

```
    background-color: #17b0cf;    border: 1px solid #000;   
```

```
   /* Remplissage de notre boîte */
```

```
    padding-top: 20px;    padding-right: 10px;    padding-bottom: 10px;    padding-left: 10px;
```

```
/ Supprimons la décoration de lien stupide */    text-decoration: none;
```

```
} 
```

![Image](https://cdn-media-1.freecodecamp.org/images/zoH3wjdFq9lviMOyd2l1uVf1Xc1iUgTzXFSV)

Les largeurs sont toutes différentes, mais cela est cohérent avec le style aléatoire de Mashable. Vous pouvez toujours définir une largeur si vous recherchez la cohérence. Nous avons également ajusté la police ici pour un look propre. Vous pouvez obtenir de superbes polices de [Google](https://fonts.google.com). Assurez-vous de coller la balise de lien qu'ils fournissent dans votre balise `<head>`.

Nous supprimerons notre handicap et déplacerons la propriété `background-color` vers le sélecteur `nav a:hover`. Vous pouvez toujours garder l'handicap activé si vous devez faire des ajustements.

![Image](https://cdn-media-1.freecodecamp.org/images/hKBcQLcBv51lBUEO9oerqzfNu85Xorcw0o92)
_C'est une assez belle couleur de survol_

Nous avons presque terminé. Travaillons sur le logo.

```
#logo { /* police */
```

```
  font-family: 'Hind', sans-serif;  font-size: 30px;  letter-spacing: -2px;  text-shadow: 1px 1px 2px #c4c4c4;
```

```
/* boîte */
```

```
  padding-left: 20px;  padding-right: 40px;  margin-right: 10px;  margin-top: -20px;  }
```

Vous avez peut-être remarqué que vos boîtes rembourrées dépassent de la nav. Tout ce que vous avez à faire est de masquer le débordement en ajoutant `overflow: hidden;` à votre sélecteur `nav`. Cette petite propriété élimine beaucoup de frustrations.

### Le produit final

![Image](https://cdn-media-1.freecodecamp.org/images/dsXj8YNdod6jU8j65L57JLqaJ9XMwoyY3zAK)

![Image](https://cdn-media-1.freecodecamp.org/images/WVOpcy5MGUaAWivhguhcGOOJRGv4iPtW2Fxf)

### Déclarations de clôture

Le CSS peut sembler être un langage rempli de magie, surtout si vous êtes habitué à la logique des langages de programmation. Mais tout ce que vous avez à faire est de garder à l'esprit la méthode des boîtes lorsque vous construisez la mise en page d'un site.

Bien sûr, il existe des astuces que les maîtres du CSS utilisent pour ajouter cette touche de style supplémentaire. Nous listerons ci-dessous une série de ressources qui vous rendront professionnel en CSS en un rien de temps. Si vous êtes toujours énervé avec le CSS, alors vous devriez jeter un coup d'œil à certains des [préprocesseurs](https://htmlmag.com/article/an-introduction-to-css-preprocessors-sass-less-stylus) conçus pour rendre la tâche de stylisation d'un site entier plus efficace.

### Ressources :

[CSS Tricks](https://css-tricks.com/)

Vous saurez comment créer tout ce que vous pouvez imaginer en parcourant ce site.

[Thecodeplayer](http://thecodeplayer.com/)

Thecodeplayer offre du codage en direct pour vous aider à comprendre les nuances du CSS.

[Calculateur de couleurs](https://www.sessions.edu/color-calculator/)

Obtenez des valeurs précises pour vos couleurs de fond.

N'oubliez pas de laisser quelques applaudissements si ce tutoriel vous a aidé. Partagez-le avec des amis qui se cognent la tête sur leur bureau lorsqu'ils luttent avec le CSS.

Codez en paix,

Raji Ayinla|rédacteur de contenu technique stagiaire|email : rajiayinla858@gmail.com

![Image](https://cdn-media-1.freecodecamp.org/images/VJ3NN-YikvPkHZjQrkTWTRfJO9nctolN0gT4)
_Icônes conçues par [www.flaticon.com](http://www.freepik.com/" rel="noopener" target="_blank" title="">**Freepik** </a>from **<a href="http://www.flaticon.com/" rel="noopener" target="_blank" title=")**_