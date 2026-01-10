---
title: Comment utiliser les sélecteurs CSS
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-06T19:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-selectors
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-karolina-grabowska-4016510.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les sélecteurs CSS
seo_desc: "You can apply CSS to elements like paragraphs and ordered lists, which\
  \ you can learn more about by reading this article. But you're not just restricted\
  \ to those two approaches. \nAs we'll see in this tutorial, you can also control\
  \ content behavior usi..."
---

Vous pouvez appliquer du CSS à des éléments comme des paragraphes et des listes ordonnées, que vous pouvez découvrir en [lisant cet article](https://www.freecodecamp.org/news/css-style-sheets-basics/). Mais vous n'êtes pas limité à ces deux approches.

Comme nous le verrons dans ce tutoriel, vous pouvez également contrôler le comportement du contenu en utilisant des styles personnalisés ou `ID`, des pseudo-classes et l'héritage. Cela se fait par l'utilisation de sélecteurs.

Les sélecteurs CSS ciblent les éléments HTML en fonction de leurs noms de balise, attributs, classes, IDs ou de leur position dans la structure du document. Lorsqu'un sélecteur correspond à un élément, les styles définis dans la règle CSS correspondante sont appliqués à cet élément.

Voici un exemple de code qui illustrera comment les sélecteurs peuvent fonctionner pour contrôler divers types d'éléments. Lisez-le et essayez de comprendre ce que tout fait, puis nous le parcourons section par section.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Cibler les éléments avec une classe */
    .highlight {
      background-color: yellow;
      font-weight: bold;
    }

    /* Cibler les éléments avec un ID */
    #special {
      color: red;
      text-decoration: underline;
    }

    /* Cibler les éléments en fonction de leur nom de balise */
    p {
      font-size: 16px;
    }

    /* Cibler les éléments en fonction de leur relation */
    ul li {
      list-style-type: square;
    }

    /* Cibler les éléments en fonction des valeurs d'attribut */
    input[type="text"] {
      border: 1px solid gray;
    }
  </style>
</head>
<body>
  <h1 id="special">Bienvenue sur mon site web</h1>

  <p>Ce paragraphe aura une taille de police de 16 pixels.</p>

  <ul>
    <li>Élément de liste 1</li>
    <li>Élément de liste 2</li>
    <li class="highlight">Élément de liste 3</li>
  </ul>

  <input type="text" placeholder="Entrez votre nom">
</body>
</html>

```

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/X_F5vK7XeiI]

## Styles CSS personnalisés et ID

Ce premier style est un exemple de sélecteur personnalisé appelé `highlight`.

```
    /* Cibler les éléments avec une classe */
    .highlight {
      background-color: yellow;
      font-weight: bold;
    }

```

Ce HTML pourrait ressembler à ceci :

```
<li class="highlight">Élément de liste 3</li>
```

Ensuite, ce sélecteur d'ID (`#special`) :

```
    /* Cibler les éléments avec un ID */
    #special {
      color: red;
      text-decoration: underline;
    }

```

...sera appliqué dans le HTML via l'attribut `id=` :

```
<h1 id="special">Bienvenue sur mon site web</h1>
```

Nous avons déjà vu comment associer un style à un élément HTML comme `p` fonctionne :

```
    /* Cibler les éléments en fonction de leur nom de balise */
    p {
      font-size: 16px;
    }

```

...Mais la _forme_ de la couleur de fond appliquée aux balises `<ul>` et la couleur de bordure du champ de saisie de texte sont contrôlées par ces deux styles :

```
    /* Cibler les éléments en fonction de leur relation */
    ul li {
      list-style-type: square;
    }

    /* Cibler les éléments en fonction des valeurs d'attribut */
    input[type="text"] {
      border: 1px solid gray;
    }

```

Maintenant, en plus des extraits HTML que nous avons déjà examinés, nous pouvons également voir comment le troisième point de la liste a l'attribut de classe `highlight`, donc il obtiendra à la fois un fond jaune et ce fond sera carré. Enfin, le champ `<input type="text">` obtiendra une bordure grise.

```
<body>
  <h1 id="special">Bienvenue sur mon site web</h1>

  <p>Ce paragraphe aura une taille de police de 16 pixels.</p>

  <ul>
    <li>Élément de liste 1</li>
    <li>Élément de liste 2</li>
    <li class="highlight">Élément de liste 3</li>
  </ul>

  <input type="text" placeholder="Entrez votre nom">
</body>

```

Si vous enregistrez tout ce code dans un fichier `.html` et le chargez dans votre navigateur préféré, vous verrez qu'il ressemble exactement à ce que nous voulions. Espérons, au moins.

## Comment travailler avec la `pseudo-classe` CSS

Il existe un autre type de classe en CSS que nous appelons une `pseudo-classe`. Elles sont appelées "pseudo" car ce ne sont pas exactement des classes traditionnelles, mais des _contrôles de classe_.

Vous avez probablement déjà vu des pseudo-classes en action sur des pages web que vous avez visitées. Les liens ou éléments de page changent leur apparence lorsque différentes actions se produisent autour d'eux.

Par exemple, comme vous pouvez le voir à partir de ce code CSS, il y a des définitions pour les états _normal_, _survol_, _focus_ et _actif_.

```
/* État normal */
button {
  background-color: blue;
  color: white;
}

/* État survol */
button:hover {
  background-color: lightblue;
}

/* État focus */
button:focus {
  outline: 2px solid red;
}

/* État actif */
button:active {
  background-color: darkgreen;
}


```

Vous devriez prendre ces styles CSS et les appliquer à un simple code HTML. Cet exemple montre comment ils pourraient tous être appliqués au texte du bouton `Cliquez-moi` dans le HTML.

```
<button>Cliquez-moi</button>

```

Voyons comment cela fonctionne.

L'apparence normale, au repos, d'un bouton pourrait avoir une couleur de fond bleue et un texte blanc. Mais lorsque vous survolez le bouton avec votre souris, le fond devient bleu clair.

```
/* État survol */
button:hover {
  background-color: lightblue;
}
```

Si vous utilisez la touche `Tab` de votre clavier pour parcourir tous les éléments de la page, une fois que vous atteignez le bouton, l'état deviendra `Focus` et le contour deviendra rouge.

```
/* État focus */
button:focus {
  outline: 2px solid red;
}
```

Lorsque je clique et maintient le bouton, le fond change en vert foncé.

```
/* État actif */
button:active {
  background-color: darkgreen;
}
```

## Héritage CSS

L'héritage CSS est un mécanisme qui permet aux propriétés définies sur les éléments parents d'être héritées par leurs éléments enfants. Lorsqu'une propriété est définie sur un élément parent, sa valeur est automatiquement héritée par ses descendants, sauf si elle est remplacée.

L'héritage s'applique à diverses propriétés CSS, telles que les styles de police, les couleurs de texte et certaines propriétés de mise en page. Par exemple, si vous définissez la famille de polices ou la taille de police sur un élément parent, les éléments enfants à l'intérieur hériteront de ces valeurs, sauf indication contraire explicite.

Dans certains cas, certaines propriétés ne sont _pas_ héritées par défaut. Par exemple, des propriétés comme la couleur de fond, les propriétés de bordure et les propriétés de modèle de boîte ne sont généralement pas héritées. Dans ces cas, les éléments enfants n'hériteront pas des valeurs de leurs éléments parents, sauf si elles sont explicitement définies.

L'héritage CSS simplifie le processus de stylisation en vous permettant de définir des propriétés une fois sur les éléments parents, réduisant ainsi le besoin de stylisation répétitive sur les éléments enfants. Cependant, il est essentiel de savoir quelles propriétés sont héritées et lesquelles ne le sont pas pour garantir le résultat de stylisation souhaité.

Ce code crée un style `#parent` qui définit la police et la couleur de la police. Il crée également un deuxième style qui s'appliquera aux paragraphes dans le HTML. Mais ce deuxième style est également un `enfant` du `parent`.

```
<style type="text/css">
#parent {
  font-family: Arial, sans-serif;
  color: blue;
}
p {
  font-size: 24px;
}
</style>

```

Le HTML existe dans une `<div>` qui utilise l'attribut `id=` pour adopter le style `parent`. Il y a deux lignes de texte, une à l'intérieur de la balise `<p>` et une à l'extérieur.

```
<div id="parent">
  Voici du texte régulier.
  <p>Ceci est un paragraphe à l'intérieur de l'élément parent.</p>
</div>

```

Lorsque nous chargeons notre code dans un navigateur, nous verrons que ces deux lignes de texte seront imprimées en bleu - ce qui signifie que l'élément `enfant` a effectivement adopté les valeurs du parent. Mais il obtiendra également sa propre mise en forme de police plus grande. Ce type de mise en forme peut être puissant lorsque vous souhaitez contrôler très précisément le comportement global, tout en conservant la capacité de définir davantage des éléments individuels.

Pour _empêcher_ l'héritage et établir une valeur complètement nouvelle, le mot-clé `inherit` peut être utilisé pour remplacer la valeur héritée. De plus, le mot-clé initial peut être utilisé pour réinitialiser une propriété à sa valeur par défaut.

Un autre point important, particulièrement pertinent lorsque vous travaillez avec plusieurs styles CSS. Que se passe-t-il lorsque, entre votre CSS en ligne, plusieurs fichiers CSS autonomes et des couches de parents et d'enfants, il y a un conflit entre les styles ? Eh bien, il existe un ensemble de règles qui déterminent comment tout sera géré.

Le code en ligne dans les balises `<style>` d'un fichier HTML est toujours prioritaire. Plus un sélecteur est spécifique, plus sa priorité est grande. Plus un style apparaît bas dans le code, plus sa priorité est grande. Et l'attribut `!important` l'emportera toujours.

### Priorité des règles en CSS

Voici un résumé rapide de la priorité des règles en CSS :

* Le CSS en ligne remplace les règles CSS dans la balise de style et le fichier CSS
* Un sélecteur plus spécifique prime sur un sélecteur moins spécifique
* Les règles qui apparaissent plus tard dans le code remplacent les règles précédentes si les deux ont la même spécificité
* Une règle CSS avec `!important` prime toujours.

## Conclusion

Vous avez vu comment personnaliser vos styles CSS à travers des attributs comme `id` et appliquer des structures comme les pseudo-classes peut grandement contribuer à dynamiser vos pages HTML. Et vous avez vu comment tout cela fonctionne grâce aux sélecteurs CSS.

Vous avez également vu comment l'héritage CSS peut vous aider à contrôler précisément le comportement des objets sur vos pages web.

Vous êtes donc prêt à commencer à construire des sites web assez sophistiqués. Pourquoi ne pas commencer aujourd'hui ?

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _Et il y a beaucoup plus de bonnes technologies disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_