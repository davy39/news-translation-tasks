---
title: Pour votre premier code HTML, aidons Batman à écrire une lettre d'amour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-30T18:03:31.000Z'
originalURL: https://freecodecamp.org/news/for-your-first-html-code-lets-help-batman-write-a-love-letter-64c203b9360b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kZxbQJTdb4jn_frfqpRg9g.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pour votre premier code HTML, aidons Batman à écrire une lettre d'amour
seo_desc: 'By Kunal

  One fine night, your stomach refuses to digest the large Pizza you had at dinner,
  and you have to rush to the bathroom in the middle of your sleep.

  In the bathroom, while wondering why this is happening to you, you hear a heavy
  voice from th...'
---

Par Kunal

Un beau soir, votre estomac refuse de digérer la grande pizza que vous avez mangée au dîner, et vous devez vous précipiter aux toilettes au milieu de votre sommeil.

Dans la salle de bain, en vous demandant pourquoi cela vous arrive, vous entendez une voix grave venir de la ventilation : « Hé, je suis Batman. »

Que feriez-vous ?

Avant de paniquer et de vous lever en plein milieu du processus critique, Batman dit : « J'ai besoin de votre aide. Je suis un super geek, mais je ne connais pas le HTML. Je dois écrire ma lettre d'amour en HTML — pourriez-vous le faire pour moi ? »

Qui pourrait refuser une demande de Batman, n'est-ce pas ? Écrivons la lettre d'amour de Batman en HTML.

### Votre premier fichier HTML

Une page web HTML est comme les autres fichiers sur votre ordinateur. Comme un fichier .doc s'ouvre dans MS Word, un fichier .jpg s'ouvre dans un visualiseur d'images, et un fichier .html s'ouvre dans votre navigateur.

Alors, créons un fichier .html. Vous pouvez le faire dans le Bloc-notes, ou tout autre éditeur de base, mais je vous recommande d'utiliser VS Code à la place. [Téléchargez et installez VS Code ici](https://code.visualstudio.com/). C'est gratuit, et le seul produit Microsoft que j'aime.

Créez un répertoire dans votre système et nommez-le « Pratique HTML » (sans les guillemets). À l'intérieur de ce répertoire, créez un autre répertoire appelé « Lettre d'amour de Batman » (sans les guillemets). Ce sera notre répertoire racine du projet. Cela signifie que tous nos fichiers liés à ce projet vivront ici.

Ouvrez VS Code et appuyez sur ctrl+n pour créer un nouveau fichier et ctrl+s pour enregistrer le fichier. Accédez au dossier « Lettre d'amour de Batman » et nommez le fichier « lettre-amour.html » et cliquez sur enregistrer.

Maintenant, si vous ouvrez ce fichier en double-cliquant dessus depuis votre explorateur de fichiers, il s'ouvrira dans votre navigateur par défaut. Je recommande d'utiliser Firefox pour le développement web, mais Chrome est bien aussi.

Relions ce processus à quelque chose que nous connaissons déjà. Vous souvenez-vous de la première fois où vous avez mis la main sur un ordinateur ? La première chose que j'ai faite a été d'ouvrir MS Paint et de dessiner quelque chose. Vous dessinez quelque chose dans Paint et vous l'enregistrez en tant qu'image et ensuite vous pouvez voir cette image dans le visualiseur d'images. Ensuite, si vous voulez modifier cette image à nouveau, vous la rouvrez dans Paint, vous la modifiez et vous l'enregistrez.

Notre processus actuel est assez similaire. Comme nous utilisons Paint pour créer et modifier des images, nous utilisons VS Code pour créer et modifier nos fichiers HTML. Et comme nous utilisons le visualiseur d'images pour voir les images, nous utilisons le navigateur pour voir nos pages HTML.

### Votre premier paragraphe en HTML

Nous avons notre fichier HTML vide, alors voici le premier paragraphe que Batman veut écrire dans sa lettre d'amour

« Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, et après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous. »

Copiez le paragraphe dans votre lettre-amour.html dans VS Code. Activez le retour à la ligne en cliquant sur Affichage -> Basculer le retour à la ligne (alt+z).

Enregistrez et ouvrez le fichier dans votre navigateur. S'il est déjà ouvert, cliquez sur actualiser dans votre navigateur.

Voilà ! C'est votre première page web !

Notre premier paragraphe est prêt, mais ce n'est pas la manière recommandée d'écrire un paragraphe en HTML. Nous avons une manière spécifique de faire savoir au navigateur qu'un texte est un paragraphe.

Si vous encadrez le texte avec `<p>` et `</p>`, alors le navigateur saura que le texte à l'intérieur de `<p>` et `</p>` est un paragraphe. Faisons cela :

```htmls
<p>Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.</p>
```

En écrivant le paragraphe à l'intérieur de `<p>` et `</p>`, vous avez créé un élément HTML. Une page web est une collection d'éléments HTML.

Clarifions d'abord quelques termes : `<p>` est la balise ouvrante, `</p>` est la balise fermante, et « p » est le nom de la balise. Le texte à l'intérieur des balises ouvrante et fermante d'un élément est le contenu de cet élément.

### L'attribut « style »

Vous verrez que le texte couvre toute la largeur de l'écran.

Nous ne voulons pas cela. Personne ne veut lire des lignes si longues. Donnons une largeur de, disons, 550px à notre paragraphe.

Nous pouvons faire cela en utilisant l'attribut « style » de l'élément. Vous pouvez définir le style d'un élément (par exemple, la largeur dans notre cas), à l'intérieur de son attribut style. La ligne suivante créera un attribut style vide sur un élément « p » :

```
<p style="">...</p>
```

Vous voyez ces `""` vides ? C'est là que nous allons définir l'apparence de l'élément. Pour l'instant, nous voulons définir la largeur à 550px. Faisons cela :

```html
<p style="width:550px;">  
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
</p>
```

Nous avons défini la propriété « width » à 550px séparée par un deux-points « : » et terminée par un point-virgule « ; ».

Remarquez également comment nous avons mis les balises `<p>` et `</p>` sur des lignes séparées et le contenu du texte indenté avec une tabulation. Styliser votre code de cette manière le rend plus lisible.

### Les listes en HTML

Ensuite, Batman veut lister certaines des vertus de la personne qu'il admire, comme ceci :

« Vous complétez mon obscurité avec votre lumière. J'aime :  
- la façon dont vous voyez le bon côté des pires choses  
- la façon dont vous gérez les situations émotionnellement difficiles  
- la façon dont vous voyez la Justice  
J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps. »

Cela semble simple.

Allons-y et copions le texte requis sous le `</p>` :

```html
<p style="width:550px;">
  Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
</p>
<p style="width:550px;">
  Vous complétez mon obscurité avec votre lumière. J'aime :
  - la façon dont vous voyez le bon côté des pires choses
  - la façon dont vous gérez les situations émotionnellement difficiles
  - la façon dont vous voyez la Justice
  J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
</p>
```

Enregistrez et actualisez votre navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/Q0mTGa1Um3uttUDNvapGuc1i46SRAoJNB3vp)

Woah ! Que s'est-il passé ici, où est notre liste ?

Si vous regardez de près, vous remarquerez que les sauts de ligne ne sont pas affichés. Nous avons écrit les éléments de la liste sur de nouvelles lignes dans notre code, mais ceux-ci sont affichés sur une seule ligne dans le navigateur.

Si vous voulez insérer un saut de ligne en HTML (nouvelle ligne), vous devez le mentionner en utilisant `<br>`. Utilisons `<br>` et voyons comment cela ressemble :

```html
<p style="width:550px;">
  Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
</p>
<p style="width:550px;">
  Vous complétez mon obscurité avec votre lumière. J'aime : <br>
  - la façon dont vous voyez le bon côté des pires choses <br>
  - la façon dont vous gérez les situations émotionnellement difficiles <br>
  - la façon dont vous voyez la Justice <br>
  J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
</p>
```

Enregistrez et actualisez :

![Image](https://cdn-media-1.freecodecamp.org/images/6y3OmcBYrMFMTk2uA3E8iz9yARbsVvmTKfdo)

D'accord, maintenant cela ressemble à ce que nous voulons.

Remarquez également que nous n'avons pas écrit de `</br>`. Certaines balises n'ont pas besoin de balise fermante (et elles sont appelées balises auto-fermantes).

Une autre chose : nous n'avons pas utilisé de `<br>` entre les deux paragraphes, mais le deuxième paragraphe commence toujours sur une nouvelle ligne. C'est parce que l'élément « p » insère automatiquement un saut de ligne.

Nous avons écrit notre liste en utilisant du texte brut, mais il y a deux balises que nous pouvons utiliser à cette fin : `<ul>` et `<li>`.

Pour clarifier les noms : ul signifie Unordered List (liste non ordonnée), et li signifie List Item (élément de liste). Utilisons ces balises pour afficher notre liste :

```html
<p style="width:550px;">
  Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
</p>

<p style="width:550px;">
  Vous complétez mon obscurité avec votre lumière. J'aime :
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
</p>
```

Avant de copier le code, remarquez les différences que nous avons faites :

* Nous avons supprimé tous les `<br>`, puisque chaque `<li>` s'affiche automatiquement sur une nouvelle ligne
* Nous avons encadré les éléments individuels de la liste entre `<li>` et `</li>`.
* Nous avons encadré la collection de tous les éléments de la liste entre `<ul>` et `</ul>`
* Nous n'avons pas défini la largeur de l'élément « ul » comme nous le faisions avec l'élément « p ». C'est parce que « ul » est un enfant de « p » et « p » est déjà limité à 550px, donc « ul » ne dépassera pas cette largeur.

Enregistrons le fichier et actualisons le navigateur pour voir les résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/dx2kvF97ux465bKbKFUr3I9oabjcfrtBl9MN)

Vous remarquerez instantanément que nous obtenons des puces affichées avant chaque élément de la liste. Nous n'avons plus besoin d'écrire ce « - » avant chaque élément de la liste.

En inspectant attentivement, vous remarquerez que la dernière ligne dépasse la largeur de 550px. Pourquoi ? Parce qu'un élément « ul » n'est pas autorisé à l'intérieur d'un élément « p » en HTML. Placions les première et dernière lignes dans des éléments « p » séparés :

```html
<p style="width:550px;">
  Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
</p>

<p style="width:550px;">
  Vous complétez mon obscurité avec votre lumière. J'aime :
</p>

<ul style="width:550px;">
  <li>la façon dont vous voyez le bon côté des pires choses</li>
  <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
  <li>la façon dont vous voyez la Justice</li>
</ul>

<p style="width:550px;">
  J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
</p>
```

Enregistrez et rechargez.

Remarquez que cette fois, nous avons également défini la largeur de l'élément « ul ». C'est parce que nous avons maintenant déplacé notre élément « ul » hors de l'élément « p ».

Définir la largeur de tous les éléments de notre lettre peut devenir fastidieux. Nous avons un élément spécifique à cet effet : l'élément « div ». Un élément « div » est un conteneur générique utilisé pour regrouper du contenu afin qu'il puisse être facilement stylisé.

Encadrons toute notre lettre avec un élément div et donnons une largeur de 550px à cet élément div :

```hsml
<div style="width:550px;">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
</div>
```

Super. Notre code est beaucoup plus propre maintenant.

### Les titres en HTML

Batman est assez content des résultats jusqu'à présent, et il veut un titre sur la lettre. Il veut faire le titre : « Bat Lettre ». Bien sûr, vous avez déjà vu ce nom venir, n'est-ce pas ? :D

Vous pouvez ajouter un titre en utilisant les balises h1, h2, h3, h4, h5 et h6, h1 est le plus grand et le titre principal et h6 le plus petit.

![Image](https://cdn-media-1.freecodecamp.org/images/D63UfAr57z1DhRhjr77cx0jLjYidb1IqMSaw)

Faisons le titre principal en utilisant h1 et un sous-titre avant le deuxième paragraphe :

```html
<div style="width:550px;">
  <h1>Bat Lettre</h1>
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
</div>
```

Enregistrez et rechargez.

![Image](https://cdn-media-1.freecodecamp.org/images/j1RGvFzqF0Is6C2ZN-TUeRu5SMKcJs1-pDqM)

### Les images en HTML

Notre lettre n'est pas encore complète, mais avant de continuer, une grande chose manque — un logo Bat. Avez-vous déjà vu quelque chose que Batman possède qui n'a pas de logo Bat ?

Non.

Alors, ajoutons un logo Bat à notre lettre.

Inclure une image en HTML est comme inclure une image dans un fichier Word. Dans MS Word, vous allez dans menu -> insérer -> image -> puis naviguez jusqu'à l'emplacement de l'image -> sélectionnez l'image -> cliquez sur insérer.

En HTML, au lieu de cliquer sur le menu, nous utilisons la balise `<img>` pour faire savoir au navigateur que nous devons charger une image. Nous écrivons l'emplacement et le nom du fichier à l'intérieur de l'attribut « src ». Si l'image est dans le répertoire racine du projet, nous pouvons simplement écrire le nom du fichier image dans l'attribut src.

Avant de plonger dans le codage, téléchargez ce logo Bat depuis [ici](https://www.pexels.com/photo/batman-black-and-white-logo-93596/). Vous voudrez peut-être recadrer l'espace blanc supplémentaire dans l'image. Copiez l'image dans votre répertoire racine du projet et renommez-la « bat-logo.jpeg ».

```html
<div style="width:550px;">
  <h1>Bat Lettre</h1>
  <img src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  
<h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
</div>
```

Nous avons inclus la balise img à la ligne 3. Cette balise est également une balise auto-fermante, donc nous n'avons pas besoin d'écrire `</img>`. Dans l'attribut src, nous donnons le nom du fichier image. Ce nom doit être **exactement** le même que le nom de votre image, y compris l'extension (.jpeg) et sa casse.

Enregistrez et actualisez pour voir le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/pardq2YWbIaIJU5uPxyfhcOeI4YN1tv2lq7D)

Damn ! Que s'est-il passé ?

Lorsque vous incluez une image en utilisant la balise img, par défaut l'image sera affichée dans sa résolution d'origine. Dans notre cas, l'image est beaucoup plus large que 550px. Définissons sa largeur en utilisant l'attribut style :

```html
<div style="width:550px;">
  <h1>Bat Lettre</h1>
  <img src="bat-logo.jpeg" style="width:100%">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
    
<h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
</div>
```

Vous remarquerez que cette fois, nous avons défini la largeur avec « % » au lieu de « px ». Lorsque nous définissons une largeur en « % », elle occupera ce % de la largeur de l'élément parent. Donc, 100% de 550px nous donnera 550px.

Enregistrez et actualisez pour voir les résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/DITE-kzRRX-nopJ0HcTXOYfrjGgYDYgAN-F9)

Fantastique ! Cela apporte un sourire timide sur le visage de Batman :)

### Gras et Italique en HTML

Maintenant, Batman veut avouer son amour dans les derniers paragraphes. Il a ce texte pour vous à écrire en HTML :

« J'ai une confession à faire

Il semble que ma poitrine _a_ un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.

Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous. »

En lisant cela, vous demandez à Batman : « Attendez, pour qui est-ce ? » et Batman répond :

« C'est pour Superman. »

![Image](https://cdn-media-1.freecodecamp.org/images/RWeRsIsKuUvOrb07wrUz70-yfmjnKkXXvLEO)

Vous : Oh ! J'allais deviner Wonder Woman.

Batman : Non, c'est Sups, s'il vous plaît écrivez « Je t'aime Superman » à la fin.

Bon, faisons-le alors :

```html
<div style="width:550px;">
  <h1>Bat Lettre</h1>
  <img src="bat-logo.jpeg" style="width:100%">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
    
<h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine a un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p>Je t'aime Superman.</p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
```

La lettre est presque terminée, et Batman veut juste deux autres changements. Batman veut que le mot « a » dans la première phrase du paragraphe de confession soit en italique, et que la phrase « Je t'aime Superman » soit en gras.

Nous utilisons `<em>` et `<strong>` pour afficher le texte en italique et en gras. Mettons à jour ces changements :

```html
<div style="width:550px;">
  <h1>Bat Lettre</h1>
  <img src="bat-logo.jpeg" style="width:100%">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
    
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/n0q06ejkUQm1RQ9ZEwK16wu355HjWOmDtvgg)

### Styling en HTML

Il existe trois façons de styliser ou de définir l'apparence d'un élément HTML :

* Styling en ligne : Nous écrivons les styles en utilisant l'attribut « style » des éléments. C'est ce que nous avons fait jusqu'à présent. Ce n'est pas une bonne pratique.
* Styling intégré : Nous écrivons tous les styles dans un élément « style » encadré par <style> et </style>.
* Feuille de style liée : Nous écrivons les styles de tous les éléments dans un fichier séparé avec l'extension .css. Ce fichier est appelé Feuille de style.

Regardons comment nous avons défini le style en ligne de la « div » jusqu'à présent :

```html
<div style="width:550px;">
```

Nous pouvons écrire ce même style à l'intérieur de `<style>` et `</style>` comme ceci :

```css
div{
  width:550px;
}
```

Dans le styling intégré, les styles que nous écrivons sont séparés des éléments. Nous avons donc besoin d'un moyen de relier l'élément et son style. Le premier mot « div » fait exactement cela. Il fait savoir au navigateur que tout style à l'intérieur des accolades `{026}` appartient à l'élément « div ». Puisque cette phrase détermine à quel élément appliquer le style, elle est appelée un sélecteur.

La façon dont nous écrivons le style reste la même : propriété (width) et valeur (550px) séparées par un deux-points (:) et terminées par un point-virgule (;).

Retirons le style en ligne de notre « div » et de l'élément « img » et écrivons-le à l'intérieur de l'élément `<style>` :

```html
<style>
  div{
    width:550px;
  }
  img{
    width:100%;
  }
</style>

<div>
  <h1>Bat Lettre</h1>
  <img src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
    
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
```

Enregistrez et actualisez, et le résultat devrait rester le même.

Il y a cependant un gros problème — que se passe-t-il s'il y a plus d'un élément « div » et « img » dans notre fichier HTML ? Les styles que nous avons définis pour div et img à l'intérieur de l'élément « style » s'appliqueront à chaque div et img de la page.

Si vous ajoutez une autre div dans votre code à l'avenir, alors cette div deviendra également large de 550px. Nous ne voulons pas cela.

Nous voulons appliquer nos styles à la div et à l'image spécifiques que nous utilisons actuellement. Pour ce faire, nous devons donner à notre div et à notre élément img des identifiants uniques. Voici comment vous pouvez donner un identifiant à un élément en utilisant son attribut « id » :

```
<div id="letter-container">
```

et voici comment utiliser cet identifiant dans notre style intégré en tant que sélecteur :

```css
#letter-container{
  ...
}
```

Remarquez le symbole « # ». Il indique qu'il s'agit d'un identifiant, et les styles à l'intérieur des accolades `{026}` doivent s'appliquer uniquement à l'élément avec cet identifiant spécifique.

Appliquons cela à notre code :

```html
<style>
  #letter-container{
    width:550px;
  }
  #header-bat-logo{
    width:100%;
  }
</style>

<div id="letter-container">
  <h1>Bat Lettre</h1>
  <img id="header-bat-logo" src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
    
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
```

Notre HTML est prêt avec le style intégré.

Cependant, vous pouvez voir que lorsque nous incluons plus de styles, la balise <style></style> devient plus grande. Cela peut rapidement encombrer notre fichier html principal. Alors, allons un peu plus loin et utilisons le style lié en copiant le contenu à l'intérieur de notre balise style dans un nouveau fichier.

Créez un nouveau fichier dans le répertoire racine du projet et enregistrez-le sous style.css :

```css
#letter-container{
  width:550px;
}

#header-bat-logo{
  width:100%;
}
```

Nous n'avons pas besoin d'écrire `<style>` et `</style>` dans notre fichier CSS.

Nous devons lier notre fichier CSS nouvellement créé à notre fichier HTML en utilisant la balise `<link>` dans notre fichier html. Voici comment nous pouvons faire cela :

```html
<link rel="stylesheet" type="text/css" href="style.css">
```

Nous utilisons l'élément link pour inclure des ressources externes dans votre document HTML. Il est principalement utilisé pour lier des feuilles de style. Les trois attributs que nous utilisons sont :

* rel : Relation. Quelle relation le fichier lié a avec le document. Le fichier avec l'extension .css est appelé une feuille de style, et donc nous gardons rel="stylesheet".
* type : le type du fichier lié ; c'est "text/css" pour un fichier CSS.
* href : Hypertext Reference. Emplacement du fichier lié.

Il n'y a pas de </link> à la fin de l'élément link. Donc, <link> est également une balise auto-fermante.

```html
<link rel="gf" type="cute" href="girl.next.door">
```

Si seulement obtenir une petite amie était si facile :D

Nah, cela n'arrivera pas, continuons.

Voici le contenu de notre lettre-amour.html :

```html
<link rel="stylesheet" type="text/css" href="style.css">
<div id="letter-container">
  <h1>Bat Lettre</h1>
  <img id="header-bat-logo" src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
```

et notre style.css :

```css
#letter-container{
  width:550px;
}

#header-bat-logo{
  width:100%;
}
```

Enregistrez les deux fichiers et actualisez, et votre sortie dans le navigateur devrait rester la même.

### Quelques formalités

Notre lettre d'amour est presque prête à être livrée à Batman, mais il reste quelques pièces formelles.

Comme tout autre langage de programmation, le HTML a également connu de nombreuses versions depuis son année de naissance (1990). La version actuelle du HTML est HTML5.

Alors, comment le navigateur saura-t-il quelle version de HTML vous utilisez pour coder votre page ? Pour dire au navigateur que vous utilisez HTML5, vous devez inclure `<!DOCTYPE html>` en haut de la page. Pour les anciennes versions de HTML, cette ligne était différente, mais vous n'avez pas besoin de l'apprendre car nous ne les utilisons plus.

De plus, dans les versions précédentes de HTML, nous avions l'habitude d'encapsuler l'ensemble du document à l'intérieur de la balise `<html></html>`. L'ensemble du fichier était divisé en deux sections principales : Head, à l'intérieur de `<head></head>`, et Body, à l'intérieur de `<body></body>`. Ce n'est pas requis en HTML5, mais nous le faisons toujours pour des raisons de compatibilité. Mettons à jour notre code avec `<Doctype>`, `<html>`, `<head>` et `<body>` :

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div id="letter-container">
  <h1>Bat Lettre</h1>
  <img id="header-bat-logo" src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
</body>
</html>
```

Le contenu principal va à l'intérieur de `<body>` et les métadonnées vont à l'intérieur de `<head>`. Nous gardons donc la div à l'intérieur de `<body>` et chargeons les feuilles de style à l'intérieur de `<head>`.

Enregistrez et actualisez, et votre page HTML devrait s'afficher de la même manière qu'auparavant.

### Titre en HTML

C'est le dernier changement. Je vous le promets.

Vous avez peut-être remarqué que le titre de l'onglet affiche le chemin du fichier HTML :

![Image](https://cdn-media-1.freecodecamp.org/images/XxSVlvsg3r0LRzsn5jScRraVZBNig3WHaf-R)

Nous pouvons utiliser la balise `<title>` pour définir un titre pour notre fichier HTML. La balise de titre, comme la balise de lien, va à l'intérieur de head. Mettons « Bat Lettre » dans notre titre :

```html
<!DOCTYPE html>
<html>
<head>
  <title>Bat Lettre</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div id="letter-container">
  <h1>Bat Lettre</h1>
  <img id="header-bat-logo" src="bat-logo.jpeg">
  <p>
    Après toutes les batailles que nous avons menées ensemble, après tous les moments difficiles que nous avons traversés ensemble, après tous les bons et mauvais moments que nous avons vécus, je pense qu'il est temps de vous faire savoir ce que je ressens pour vous.
  </p>
  <h2>Vous êtes la lumière de ma vie</h2>
  <p>
    Vous complétez mon obscurité avec votre lumière. J'aime :
  </p>
  <ul>
    <li>la façon dont vous voyez le bon côté des pires choses</li>
    <li>la façon dont vous gérez les situations émotionnellement difficiles</li>
    <li>la façon dont vous voyez la Justice</li>
  </ul>
  <p>
    J'ai beaucoup appris de vous. Vous avez occupé une place spéciale dans mon cœur avec le temps.
  </p>
  <h2>J'ai une confession à faire</h2>
  <p>
    Il semble que ma poitrine <em>a</em> un cœur. Vous faites battre mon cœur. Votre sourire apporte un sourire sur mon visage, votre douleur apporte de la douleur à mon cœur.
  </p>
  <p>
    Je ne montre pas mes émotions, mais je pense que cet homme derrière le masque tombe amoureux de vous.
  </p>
  <p><strong>Je t'aime Superman.</strong></p>
  <p>
    Votre amant pas si secret, <br>
    Batman
  </p>
</div>
</body>
</html>

```

Enregistrez et actualisez, et vous verrez qu'au lieu du chemin du fichier, « Bat Lettre » est maintenant affiché sur l'onglet.

La lettre d'amour de Batman est maintenant complète.

Félicitations ! Vous avez fait la lettre d'amour de Batman en HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/KApRcQx1O1WLKNGvHcMYIvjLcG7c49MBRGzp)

### Ce que nous avons appris

Nous avons appris les nouveaux concepts suivants :

* La structure d'un document HTML
* Comment écrire des éléments en HTML (<p></p>)
* Comment écrire des styles à l'intérieur de l'élément en utilisant l'attribut style (c'est ce qu'on appelle le style en ligne, évitez cela autant que possible)
* Comment écrire les styles d'un élément à l'intérieur de <style>026</style> (c'est ce qu'on appelle le style intégré)
* Comment écrire des styles dans un fichier séparé et le lier en HTML en utilisant <link> (c'est ce qu'on appelle une feuille de style liée)
* Qu'est-ce qu'un nom de balise, un attribut, une balise ouvrante et une balise fermante
* Comment donner un identifiant à un élément en utilisant l'attribut id
* Les sélecteurs de balises et les sélecteurs d'identifiants en CSS

Nous avons appris les balises HTML suivantes :

* <p> : pour les paragraphes
* <br> : pour les sauts de ligne
* <ul>, <li> : pour afficher des listes
* <div> : pour regrouper des éléments de notre lettre
* <h1>, <h2> : pour les titres et sous-titres
* <img> : pour insérer une image
* <strong>, <em> : pour le style de texte en gras et en italique
* <style> : pour le style intégré
* <link> : pour inclure une feuille de style externe
* <html> : pour encapsuler l'ensemble du document HTML
* <!DOCTYPE html> : pour faire savoir au navigateur que nous utilisons HTML5
* <head> : pour encapsuler les métadonnées, comme <link> et <title>
* <body> : pour le corps de la page HTML qui est réellement affiché
* <title> : pour le titre de la page HTML

Nous avons appris les propriétés CSS suivantes :

* width : pour définir la largeur d'un élément
* Unités CSS : « px » et « % »

C'est tout pour aujourd'hui les amis, à la prochaine dans le prochain tutoriel.

**Vous voulez apprendre le développement web avec des tutoriels amusants et engageants ?**

[**Cliquez ici pour obtenir de nouveaux tutoriels de développement web chaque semaine.**](http://supersarkar.com)