---
title: Qu'est-ce que la déclaration DOCTYPE en HTML ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T22:02:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-doctype-declaration-in-html
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e63740569d1a4ca3cda.jpg
tags:
- name: HTML
  slug: html
seo_title: Qu'est-ce que la déclaration DOCTYPE en HTML ?
seo_desc: The HTML document type declaration, also known as DOCTYPE, is the first
  line of code required in every HTML or XHTML document. The DOCTYPE declaration is
  an instruction to the web browser about what version of HTML the page is written
  in. This ensure...
---

La déclaration de type de document HTML, également connue sous le nom de `DOCTYPE`, est la première ligne de code requise dans chaque document HTML ou XHTML. La déclaration `DOCTYPE` est une instruction au navigateur web sur la version de HTML dans laquelle la page est écrite. Cela garantit que la page web est analysée de la même manière par différents navigateurs web.

Dans HTML 4.01, la déclaration `DOCTYPE` fait référence à une définition de type de document (DTD). Une DTD définit la structure et les éléments légaux d'un document XML. Parce que HTML 4.01 était basé sur le Standard Generalised Markup Language (SGML), il était nécessaire de faire référence à une DTD dans la déclaration `DOCTYPE`.

De plus, les doctypes pour HTML 4.01 nécessitaient la déclaration de soit `strict`, `transitional`, ou `frameset` DTD, chacun avec un cas d'utilisation différent comme décrit ci-dessous.

* **Strict DTD** : Utilisé pour les pages web qui _excluent_ les attributs et éléments que le W3C prévoit de supprimer à mesure que le support CSS grandit
* **Transitional DTD** : Utilisé pour les pages web qui _incluent_ les attributs et éléments que le W3C prévoit de supprimer à mesure que le support CSS grandit
* **Frameset DTD** : Utilisé pour les pages web avec des frames

En revanche, la déclaration du `DOCTYPE` HTML5 est beaucoup plus simple : elle ne nécessite plus de référence aux DTD car elle n'est plus basée sur SGML. Voir les exemples ci-dessous pour une comparaison entre les `DOCTYPE` de HTML 4.01 et HTML5.

### **Exemples**

Syntaxe du doctype pour HTML5 et au-delà :

```html
<!DOCTYPE html>
```

Syntaxe du doctype pour le strict HTML 4.01 :

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

Syntaxe du doctype pour le transitional HTML 4.01 :

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
```

Syntaxe du doctype pour le frameset HTML 4.01 :

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
```

## **Histoire**

Pendant les années de formation de HTML, les normes web n'étaient pas encore convenues. Les fournisseurs de navigateurs développaient de nouvelles fonctionnalités de la manière qu'ils voulaient. Il y avait peu de préoccupation pour les navigateurs concurrents.

Le résultat était que les développeurs web devaient choisir un navigateur pour développer leurs sites. Cela signifiait que les sites ne s'afficheraient pas correctement dans les navigateurs non supportés. Cette situation ne pouvait pas continuer.

Le W3C (World Wide Web Consortium) a écrit un ensemble de normes web pour gérer cette situation. Tous les fournisseurs de navigateurs et les développeurs web devraient adhérer à ces normes. Cela garantirait que les sites web s'afficheraient correctement dans tous les navigateurs.

Les changements requis par les normes étaient assez différents de certaines pratiques existantes. Les respecter briserait les sites web existants non conformes aux normes.

Pour gérer ce problème, les fournisseurs ont commencé à programmer des modes de rendu dans leurs navigateurs. Les développeurs web devraient ajouter une déclaration de doctype en haut d'un document HTML. La déclaration de doctype indiquerait au navigateur quel mode de rendu utiliser pour ce document.

Trois modes de rendu distincts étaient généralement disponibles dans les navigateurs.

* **Mode pleinement conforme aux normes** rend les pages selon les normes web du W3C.
* **Mode de compatibilité** rend les pages de manière non conforme aux normes.
* **Mode presque conforme aux normes** est proche du mode pleinement conforme aux normes, mais prend en charge un petit nombre de particularités.

À l'ère moderne de HTML5, les normes web sont pleinement implémentées dans tous les principaux navigateurs. Les sites web sont généralement développés de manière conforme aux normes. Pour cette raison, la déclaration de doctype HTML5 n'existe que pour indiquer au navigateur de rendre le document en mode pleinement conforme aux normes.

## **Utilisation**

La déclaration Doctype doit être la toute première ligne de code dans un document HTML, à l'exception des commentaires, qui peuvent être placés avant si nécessaire. Pour les documents HTML5 modernes, la déclaration de doctype doit être la suivante :

`<!DOCTYPE html>`

#### **Plus d'informations :**

Bien qu'ils ne soient plus d'usage général, il existe plusieurs autres types de déclarations de doctype provenant des versions précédentes de HTML. Il existe également des versions spécifiques pour les documents XML. Pour en savoir plus sur ces sujets et pour voir des exemples de code pour chacun, consultez l'article [Wikipedia](https://en.wikipedia.org/wiki/Document_type_declaration).

[Une note du W3](https://www.w3.org/QA/Tips/Doctype)

[Entrée du glossaire MDN](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)

[W3Schools](https://www.w3schools.com/tags/tag_doctype.asp)

[Une explication rapide du "Quirks Mode" et du "Standards Mode"](https://developer.mozilla.org/en-US/docs/Quirks_Mode_and_Standards_Mode)