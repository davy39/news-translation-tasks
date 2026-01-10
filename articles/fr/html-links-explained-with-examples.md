---
title: Comment créer des liens en HTML – Tutoriel avec exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-02T07:59:34.000Z'
originalURL: https://freecodecamp.org/news/html-links-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/White-Soft-Brown-Professional-Elegant-Marketing-Strategy-Presentation-169.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Comment créer des liens en HTML – Tutoriel avec exemples
seo_desc: "Links are an essential part of the web because they connect web pages,\
  \ documents, and resources across the internet. \nIn HTML (which is short for Hypertext\
  \ Markup Language), links play a crucial role in creating a web of interconnected\
  \ content, allow..."
---

Les liens sont une partie essentielle du web car ils connectent les pages web, les documents et les ressources à travers l'internet. 

En HTML (qui signifie Hypertext Markup Language), les liens jouent un rôle crucial dans la création d'un réseau de contenu interconnecté, permettant aux utilisateurs de naviguer de manière transparente entre différentes pages web et sites web. 

Dans cet article, nous allons explorer les fondamentaux des liens en HTML, y compris leurs types, attributs et meilleures pratiques.

## Qu'est-ce qu'un lien en HTML ?

En HTML, un lien, également connu sous le nom d'hyperlien, est un élément qui permet aux utilisateurs de naviguer d'une page web à une autre. Ils permettent également aux utilisateurs de naviguer vers des ressources externes telles que des documents, des images, des vidéos, et plus encore.

HTML offre plusieurs types de liens, chacun servant un objectif spécifique. Voyons quelques-uns d'entre eux en action dans les sections suivantes.

### Comment créer des liens texte

Les liens texte sont le type de liens le plus courant. Ils sont créés en enveloppant du texte avec un élément d'ancrage (`<a>`). Lorsque les utilisateurs cliquent sur le texte lié, ils sont dirigés vers l'URL spécifiée dans l'attribut `href` du lien :

```html
<a href="https://www.example.com">Visitez Example.com</a>
```

Les liens texte sont polyvalents et peuvent être utilisés à diverses fins, telles que lier à d'autres pages web, des sites web externes, ou même des sections spécifiques au sein d'une page en utilisant des balises d'ancrage.

### Comment créer des liens image

Vous pouvez transformer des images en liens cliquables en les enveloppant dans un élément d'ancrage. Cela est utile pour créer une navigation basée sur des images ou lier à des versions plus grandes des images :

```html
<a href="https://www.example.com">
  <img src="image.jpg" alt="Image d'exemple">
</a>
```

Les liens image sont visuellement engageants et sont souvent utilisés pour des éléments comme des logos, des bannières, ou des images miniatures qui, lorsqu'on clique dessus, mènent les utilisateurs à une page web ou une ressource associée.

### Comment créer des liens email

Pour créer des liens qui ouvrent un client email avec une adresse de destinataire pré-remplie, utilisez le schéma `mailto` :

```html
<a href="mailto:contact@example.com">Envoyer un email</a>
```

Les liens email sont pratiques pour permettre aux utilisateurs d'initier une communication par email avec un simple clic. Ils sont couramment utilisés pour les informations de contact sur les sites web.

### Comment créer des liens externes

Les liens externes pointent vers des ressources sur d'autres sites web. Il est essentiel d'indiquer qu'un lien est externe en utilisant l'attribut `target="_blank"` pour ouvrir la page liée dans un nouvel onglet ou une nouvelle fenêtre du navigateur. Cela garantit que votre site web reste ouvert dans l'onglet actuel de l'utilisateur tandis que le contenu lié apparaît dans un onglet ou une fenêtre séparée :

```html
<a href="https://www.external-site.com" target="_blank">Visitez le site externe</a>
```

Les liens externes sont un moyen de fournir des ressources supplémentaires, des références ou des sources à votre contenu tout en permettant aux utilisateurs de revenir facilement à votre site.

### Comment créer des liens internes

Les liens internes sont utilisés pour naviguer au sein du même site web. Ils référencent généralement d'autres pages au sein du site en utilisant des URLs relatives :

```html
<a href="/about">En savoir plus sur nous</a>
```

Les liens internes sont essentiels pour la navigation sur le site, aidant les utilisateurs à trouver du contenu associé ou à se déplacer entre différentes sections de votre site web.

## Explication des attributs de lien

Pour créer des liens fonctionnels et conviviaux, il est crucial de comprendre les attributs clés qui peuvent être utilisés avec les éléments d'ancrage (`<a>`).

### Comment utiliser l'attribut `href`

L'attribut `href` spécifie l'URL de destination ou la ressource vers laquelle le lien pointe. Il peut s'agir d'une URL absolue (commencant par "http://" ou "https://") ou d'une URL relative (relative à la page actuelle).

Voici comment créer des URLs absolues :

```html
<a href="https://www.example.com">Visitez Example.com</a>
```

Et voici comment créer des URLs relatives :

```html
<a href="/about">En savoir plus sur nous</a>
```

L'utilisation d'URLs relatives est souvent préférée lors de la liaison au sein du même site web car cela rend vos liens plus adaptables aux changements dans la structure du domaine.

### Comment utiliser l'attribut `target`

L'attribut `target` définit comment la ressource liée doit être affichée lorsqu'on clique dessus. Les valeurs courantes incluent :

* `_self` (par défaut) : Ouvre le lien dans le même onglet ou la même fenêtre du navigateur.
* `_blank` : Ouvre le lien dans un nouvel onglet ou une nouvelle fenêtre du navigateur.
* `_parent` : Ouvre le lien dans le cadre ou la fenêtre parent.
* `_top` : Ouvre le lien dans le corps complet de la fenêtre, remplaçant tous les cadres.

```html
<a href="https://www.external-site.com" target="_blank">Visitez le site externe</a>
```

L'utilisation de la cible `_blank` est courante pour les liens externes afin d'empêcher les utilisateurs de quitter entièrement votre site.

### Comment utiliser l'attribut `rel`

L'attribut `rel` spécifie la relation entre le document actuel et la ressource liée. Par exemple, `rel="noopener"` est souvent utilisé pour des raisons de sécurité lors de l'ouverture de liens dans un nouvel onglet :

```html
<a href="https://www.example.com" rel="noopener">Visitez Example.com</a>
```

La valeur `noopener` aide à protéger contre les potentielles vulnérabilités de sécurité associées à l'ouverture de nouveaux onglets ou fenêtres.

## Bonnes pratiques pour les liens HTML

Pour garantir une excellente expérience utilisateur et maintenir les normes d'accessibilité web et de SEO (Search Engine Optimization), vous pouvez suivre certaines bonnes pratiques lors de l'utilisation de liens en HTML.

### Utiliser un texte descriptif

Le texte utilisé pour les ancres de lien doit être descriptif et transmettre le but du lien aux utilisateurs. Évitez les phrases génériques comme "cliquez ici".

Non recommandé : `<a href="https://www.example.com">Cliquez ici</a>`

Recommandé : `<a href="https://www.example.com">Visitez Example.com</a>`

Un texte de lien descriptif améliore l'expérience utilisateur et aide les utilisateurs à comprendre où le lien les mènera.

### Fournir un contexte

Lors de la liaison à des ressources externes, envisagez d'ajouter une brève description ou un attribut de titre pour informer les utilisateurs sur le contenu lié :

```html
<a href="https://www.example.com" title="Visitez Example.com">Example.com</a>
```

Fournir un contexte améliore l'utilisabilité et l'accessibilité, en particulier pour les utilisateurs handicapés qui dépendent des technologies d'assistance.

### Tester les liens

Testez régulièrement tous les liens sur votre site web pour vous assurer qu'ils fonctionnent correctement. Les liens brisés peuvent frustrer les utilisateurs et nuire à la réputation de votre site web.

Envisagez d'utiliser des outils automatisés de vérification de liens pour scanner votre site à la recherche de liens brisés et les corriger rapidement.

### Optimiser pour l'accessibilité

Utilisez le HTML sémantique et fournissez un texte alternatif pour les images au sein des liens afin de rendre votre contenu accessible aux utilisateurs handicapés.

```html
<a href="/about">
  <img src="about-image.jpg" alt="À propos de nous">
</a>
```

Les liens accessibles garantissent que tous les utilisateurs, quelles que soient leurs capacités, peuvent naviguer et interagir avec votre contenu.

### Considérer le SEO

Lors de la liaison à des pages internes, utilisez un texte d'ancrage significatif qui inclut des mots-clés pertinents. Cela peut améliorer le classement de votre site web dans les moteurs de recherche.

Non recommandé : `<a href="/product123">Cliquez ici pour plus d'informations</a>`

Recommandé : `<a href="/product123">En savoir plus sur le produit XYZ</a>`

Un texte d'ancrage riche en mots-clés aide les moteurs de recherche à comprendre le contenu et le contexte de vos liens, ce qui peut améliorer la visibilité de votre site dans les résultats de recherche.

### Utiliser des URLs relatives

Lors de la liaison au sein de votre propre site web, préférez les URLs relatives aux URLs absolues. Cela rend votre site web plus maintenable et adaptable aux changements dans la structure du domaine.

```html
<a href="/about">En savoir plus sur nous</a>
```

Les URLs relatives sont moins sujettes à la rupture lorsque vous apportez des modifications à la structure de votre site web ou que vous le migrez vers un domaine différent.

### Utiliser des indicateurs de lien externe

Lors de la liaison à des sites web externes, faites-le clairement savoir aux utilisateurs qu'ils quittent votre site. Cela peut aider à établir la confiance et la transparence.

Envisagez d'utiliser une icône ou un texte tel que "Lien externe" à côté des liens externes pour fournir cette indication.

## Conclusion

En conclusion, les liens sont la colonne vertébrale du web, permettant une navigation et une exploration transparentes du contenu en ligne. En comprenant les types de liens disponibles en HTML, leurs attributs et les meilleures pratiques pour leur utilisation, vous pouvez créer une expérience web conviviale et accessible tout en améliorant la visibilité et la crédibilité de votre site web sur l'internet.

Avec une utilisation appropriée des liens, vous pouvez connecter votre audience à des ressources précieuses, fournir une expérience utilisateur fluide et contribuer au succès global de votre site web.