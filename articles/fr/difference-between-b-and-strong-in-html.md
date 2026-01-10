---
title: La Différence Entre <b> et <Strong> en HTML – Explications avec Exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-04-26T23:24:38.000Z'
originalURL: https://freecodecamp.org/news/difference-between-b-and-strong-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--6-.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: La Différence Entre <b> et <Strong> en HTML – Explications avec Exemples
seo_desc: "Bold text is a common formatting technique used to grab attention and highlight\
  \ important information on webpages. \nIn HTML, we have two seemingly interchangeable\
  \ tags for bold formatting: <b> and <strong>. While they may achieve a similar visual\
  \ out..."
---

Le texte en gras est une technique de mise en forme courante utilisée pour attirer l'attention et mettre en évidence des informations importantes sur les pages web.

En HTML, nous avons deux balises apparemment interchangeables pour la mise en forme en gras : `<b>` et `<strong>`. Bien qu'elles puissent produire un résultat visuel similaire, il existe une différence cruciale entre elles.

Cet article explore en profondeur la distinction entre `<b>` et `<strong>` en HTML, en examinant leur signification sémantique, leur rendu, leur accessibilité et les meilleures pratiques pour leur utilisation.

## Qu'est-ce que la balise `b` en HTML ?

La balise `<b>` est un élément HTML utilisé pour appliquer une mise en forme en gras au contenu textuel. Elle signifie "gras" et fait partie de l'ensemble des éléments en ligne en HTML. Lorsque vous encadrez du texte avec des balises `<b>`, le texte inclus est rendu en style de police gras par les navigateurs web.

Mais il est essentiel de noter que la balise `<b>` ne transmet aucune signification sémantique spécifique au texte qu'elle encadre. Contrairement à d'autres éléments comme `<strong>`, qui indique une forte importance ou emphase, la balise `<b>` est principalement utilisée à des fins stylistiques. Elle indique simplement au navigateur d'afficher le texte inclus en gras, sans impliquer une signification ou une importance inhérente.

Par exemple :

```html
<p>Ceci est un texte <b>en gras</b>.</p>
```

<p>Ceci est un texte <b>en gras</b>.</p>

Dans ce cas, le mot "en gras" sera visuellement mis en évidence, mais la balise `<b>` ne fournit aucune information supplémentaire sur la raison pour laquelle le texte est en gras. Pour cette raison, il est crucial d'utiliser la balise `<b>` avec discernement, surtout lorsque vous souhaitez transmettre une emphase ou une importance significative dans votre document HTML.

## Qu'est-ce que la balise `strong` en HTML ?

La balise `<strong>` est un élément HTML utilisé pour désigner un texte ayant une forte importance, une emphase ou une pertinence. C'est l'un des éléments de balisage sémantique en HTML conçus pour transmettre une signification au-delà de la simple présentation.

Lorsque vous encadrez du texte avec des balises `<strong>`, cela indique aux navigateurs web et aux technologies d'assistance que le texte inclus doit être traité comme ayant une forte importance ou une emphase.

Contrairement à la balise `<b>`, qui est principalement utilisée à des fins stylistiques pour appliquer une mise en forme en gras, la balise `<strong>` porte une signification sémantique. Bien que les navigateurs rendent généralement le texte à l'intérieur des balises `<strong>` en police grasse, le but principal de la balise est de fournir un contexte supplémentaire sur la signification du texte inclus.

Par exemple :

```html
<p>Ceci est un texte <strong>important</strong>.</p>
```

<p>Ceci est un texte <strong>important</strong>.</p>

Dans ce cas, le mot "important" n'est pas seulement visuellement mis en évidence avec une police grasse, mais aussi marqué comme ayant une forte importance ou une emphase dans la structure du document.

Cette signification sémantique peut être bénéfique pour l'accessibilité, car les lecteurs d'écran et autres technologies d'assistance peuvent interpréter la signification du texte et la transmettre aux utilisateurs qui ne peuvent pas voir le style visuel.

## But de la mise en forme en gras

Le but de la mise en forme en gras en HTML est principalement de mettre visuellement en évidence certains mots ou phrases dans un bloc de texte. Lorsque le texte est mis en forme en gras, il se distingue plus clairement par rapport au texte environnant, attirant l'attention du lecteur.

Cette emphase peut servir divers objectifs, tels que l'indication d'importance, la mise en évidence de points clés, ou la distinction des titres et sous-titres du texte principal.

La mise en forme en gras peut être particulièrement utile pour :

* **Mettre en évidence des informations importantes** : Le texte en gras est souvent utilisé pour souligner des informations critiques ou des concepts clés dans un paragraphe ou un document, facilitant ainsi l'identification et la compréhension des points essentiels par les lecteurs.
* **Améliorer la lisibilité** : En séparant visuellement les éléments importants du reste du texte, la mise en forme en gras peut améliorer la lisibilité globale du contenu, surtout dans les passages longs.
* **Créer une hiérarchie visuelle** : Le texte en gras peut aider à établir une hiérarchie d'informations dans un document, avec des titres et sous-titres apparaissant plus gras que le texte ordinaire, guidant ainsi les lecteurs à travers la structure du contenu.
* **Souligner les appels à l'action** : En conception web, le texte en gras est fréquemment utilisé pour attirer l'attention sur les boutons ou liens d'appel à l'action (CTA), incitant les utilisateurs à effectuer des actions spécifiques telles qu'un achat, une inscription à une newsletter, ou une navigation vers une autre page.

## Les styles du navigateur peuvent-ils être remplacés ?

Oui, les styles du navigateur peuvent remplacer le rendu par défaut des éléments HTML, y compris les balises `<b>` et `<strong>`.

Les navigateurs web ont leurs propres feuilles de style par défaut (feuilles de style de l'agent utilisateur) qui définissent comment les éléments HTML doivent être affichés si aucun style spécifique n'est fourni par la page web elle-même. Ces feuilles de style par défaut peuvent spécifier la taille de la police, la famille de polices, la couleur et d'autres propriétés visuelles pour divers éléments HTML.

Lorsque vous utilisez les balises `<b>` ou `<strong>` sans fournir de styles personnalisés, les navigateurs appliqueront généralement leurs styles par défaut pour le texte en gras. Mais ces styles par défaut peuvent être remplacés par des styles CSS définis dans la feuille de style de la page web ou des styles en ligne appliqués directement aux éléments.

Par exemple, si vous avez le HTML suivant :

```html
<p>Ceci est un texte <strong>important</strong>.</p>
```

Et que vous appliquez des styles CSS personnalisés pour remplacer la mise en forme en gras par défaut :

```css
strong {
    font-weight: normal; /* Remplacer le poids de la police en gras */
    color: red; /* Changer la couleur du texte */
}
```

<style>
strong {
  font-weight: normal; /* Remplacer le poids de la police en gras */
  color: red; /* Changer la couleur du texte */
}
</style>
</head>
<body>
<p>Ceci est un texte <strong style="font-weight: normal; color: red;">important</strong>.</p>

Le texte à l'intérieur de la balise `<strong>` n'apparaîtra plus en gras et sera affiché en rouge, comme spécifié par les règles CSS.

De même, vous pouvez remplacer les styles par défaut pour la balise `<b>` en utilisant CSS, bien que ce soit moins courant puisque la balise `<b>` est généralement utilisée à des fins purement présentatives sans transmettre de signification sémantique.

Les lecteurs d'écran interprètent la balise `<strong>` comme indiquant un texte ayant une forte importance ou une emphase. Lorsqu'ils rencontrent du contenu encadré par des balises `<strong>`, les logiciels de lecture d'écran annoncent généralement le texte avec une emphase supplémentaire, indiquant aux utilisateurs que le contenu encadré est particulièrement important ou pertinent dans le contexte du document.

Ce balisage sémantique est crucial pour l'accessibilité, car il permet aux utilisateurs qui dépendent des lecteurs d'écran de comprendre la signification du texte sans se fier uniquement aux indices visuels. En transmettant l'importance ou l'emphase du texte par le biais d'un balisage sémantique comme `<strong>`, les lecteurs d'écran peuvent fournir une représentation plus précise et informative du contenu aux utilisateurs qui peuvent être malvoyants ou autrement incapables de voir le style visuel de la page web.

Par exemple, si un lecteur d'écran rencontre le HTML suivant :

```html
<p>Ceci est un texte <strong>important</strong>.</p>
```

Il annoncerait le texte "important" avec une emphase supplémentaire, comme en ajustant le débit ou le volume de la parole, pour indiquer à l'utilisateur que ce texte particulier est d'une importance accrue dans le document.

## Problèmes potentiels avec `<b>`

L'utilisation de la balise `<b>` peut entraîner plusieurs problèmes potentiels, notamment en termes d'accessibilité et de balisage sémantique :

**Manque de signification sémantique** : La balise `<b>` est purement présentative et ne transmet aucune signification sémantique spécifique sur le texte qu'elle encadre. Cela peut poser problème pour les utilisateurs qui dépendent des technologies d'assistance comme les lecteurs d'écran pour accéder au contenu web, car la mise en forme en gras fournie par la balise `<b>` ne donne aucune indication sur l'importance ou l'emphase du texte.

**Problèmes d'accessibilité** : Les lecteurs d'écran peuvent ne pas interpréter le texte encadré par des balises `<b>` comme étant plus important ou pertinent que le texte environnant, ce qui peut entraîner une perte de contexte ou de compréhension pour les utilisateurs handicapés. Sans balisage sémantique pour transmettre la signification du texte, les utilisateurs peuvent avoir du mal à comprendre le sens voulu du contenu.

**Impact sur le SEO** : Les moteurs de recherche peuvent ne pas accorder autant d'importance au contenu stylisé avec la balise `<b>` par rapport au contenu marqué avec des éléments sémantiques comme `<strong>`. Cela pourrait potentiellement affecter les classements dans les moteurs de recherche, car les moteurs de recherche s'appuient sur le balisage sémantique pour comprendre la pertinence et l'importance du contenu sur les pages web.

**Défis de maintenance** : L'utilisation excessive de la balise `<b>` à des fins purement présentatives peut entraîner des défis de maintenance, car il peut être difficile de distinguer le texte mis en gras pour des raisons stylistiques du texte qui est réellement important ou mis en emphase dans le document. Ce manque de clarté peut rendre plus difficile pour les développeurs la maintenance et la mise à jour du contenu à l'avenir.

Dans l'ensemble, bien que la balise `<b>` puisse être utile pour ajouter une mise en forme en gras au texte, il est important de l'utiliser avec discernement et de considérer les implications potentielles pour l'accessibilité, le SEO et la structure du document.

## `<strong>` a-t-il un impact sur le SEO ?

Oui, la balise `<strong>` peut indirectement influencer le SEO (Search Engine Optimization) de plusieurs manières, bien que l'utilisation de `<strong>` puisse indirectement affecter le SEO en améliorant la lisibilité et l'accessibilité du contenu, ce n'est pas un facteur de classement direct.

**Balisage sémantique** : Les moteurs de recherche comme Google visent à comprendre le contenu des pages web pour fournir des résultats de recherche pertinents aux utilisateurs. Le balisage sémantique, tel que la balise `<strong>`, fournit un contexte et une clarté supplémentaires sur l'importance ou l'emphase du texte dans un document. Lorsque vous utilisez `<strong>`, vous signalez aux moteurs de recherche que le texte encadré est d'une grande importance ou pertinence, influençant potentiellement la manière dont ils interprètent et indexent votre contenu.

**Lisibilité du contenu** : Un contenu clair et bien structuré améliore la lisibilité, ce qui est un facteur clé en SEO. En utilisant `<strong>` pour souligner des mots-clés ou des phrases importantes, vous pouvez améliorer la lisibilité et la compréhension de votre contenu pour les utilisateurs et les moteurs de recherche.

**Engagement des utilisateurs** : Un contenu qui communique efficacement les points clés en utilisant un balisage sémantique comme `<strong>` peut entraîner une augmentation de l'engagement des utilisateurs, comme un temps plus long passé sur la page ou des taux de clics plus élevés. Les moteurs de recherche peuvent considérer les métriques d'engagement des utilisateurs comme des indicateurs de la qualité du contenu, ce qui peut avoir un impact positif sur les classements SEO.

**Accessibilité** : Le balisage sémantique améliore l'accessibilité pour les utilisateurs handicapés, y compris ceux qui utilisent des lecteurs d'écran. En marquant correctement le contenu important avec `<strong>`, vous garantissez que tous les utilisateurs, quelles que soient leurs capacités, peuvent comprendre la signification du texte. Une accessibilité améliorée peut conduire à de meilleures expériences utilisateur, potentiellement entraînant des classements plus élevés dans les pages de résultats des moteurs de recherche (SERPs).

### Quand utiliser `<strong>`

Vous devriez utiliser la balise `<strong>` lorsque vous souhaitez souligner un texte qui a une forte importance ou pertinence dans le contexte de votre document. Voici quelques scénarios où l'utilisation de `<strong>` serait appropriée :

* **Mots-clés importants** : Utilisez `<strong>` pour mettre en évidence des mots-clés ou des phrases importantes qui sont centraux pour le sujet ou le point principal de votre contenu. Cela aide les lecteurs et les moteurs de recherche à comprendre la signification de ces termes.
* **Points clés** : Utilisez `<strong>` pour souligner les points clés, les arguments ou les conclusions dans votre contenu. Cela attire l'attention sur les informations critiques et les rend plus mémorables pour les lecteurs.
* **Avertissements ou notices** : Utilisez `<strong>` pour mettre en évidence les avertissements, les notices ou les alertes qui nécessitent une attention immédiate de votre audience. Cela garantit que les messages importants se distinguent et ne sont pas négligés.
* **Appels à l'action** : Utilisez `<strong>` pour souligner les appels à l'action (CTA) tels que "Acheter maintenant", "S'inscrire" ou "En savoir plus". Cela encourage l'engagement des utilisateurs et augmente la probabilité de conversion.
* **Titres et sous-titres** : Utilisez `<strong>` dans les titres et sous-titres pour leur donner une emphase et une hiérarchie supplémentaires dans la structure de votre document. Cela aide les utilisateurs à scanner rapidement et à comprendre l'organisation de votre contenu.
* **Citations ou références** : Utilisez `<strong>` pour souligner les citations ou les références de sources autorisées, indiquant leur importance ou leur pertinence pour votre contenu.

### Quand `<b>` pourrait-il être acceptable ?

`<b>` pourrait être acceptable pour une mise en forme en gras purement stylistique lorsque aucune signification sémantique spécifique n'est prévue.

## Conclusion

En conclusion, comprendre les différences subtiles mais cruciales entre `<b>` et `<strong>` est essentiel pour créer un HTML bien structuré et sémantique.

En privilégiant la balise `<strong>` pour transmettre l'importance et en réservant `<b>` pour les situations où l'emphase est purement visuelle, vous contribuez à une expérience web plus claire et plus accessible pour tous les utilisateurs.

Rappelez-vous, le HTML sémantique ne bénéficie pas seulement aux utilisateurs handicapés, mais peut également jouer un rôle dans l'optimisation pour les moteurs de recherche. Alors, faites un choix conscient : utilisez `<strong>` pour mettre en évidence ce qui compte vraiment, et utilisez CSS pour ajuster finement la présentation visuelle de votre texte en gras.

En adoptant des pratiques de codage sémantique, vous créerez des pages web qui ne sont pas seulement informatives, mais qui parlent également un langage clair aux utilisateurs et aux moteurs de recherche.

Connectez-vous avec moi sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).