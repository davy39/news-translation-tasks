---
title: Une introduction au langage de balisage extensible (XML)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-extensible-markup-language-xml
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1f740569d1a4ca3600.jpg
tags:
- name: markup
  slug: markup
- name: toothbrush
  slug: toothbrush
- name: xml
  slug: xml
seo_title: Une introduction au langage de balisage extensible (XML)
seo_desc: "XML stands for eXtensible Markup Language. It is extensible, because unlike\
  \ HTML, it does not use a predefined set of tags for identifying structural components.\
  \ Instead, it provides a mechanism for users to define tags themselves. \nXML was\
  \ designed ..."
---

XML signifie eXtensible Markup Language. Il est extensible, car contrairement à HTML, il n'utilise pas un ensemble prédéfini de balises pour identifier les composants structurels. Au lieu de cela, il fournit un mécanisme permettant aux utilisateurs de définir eux-mêmes les balises.

XML a été conçu pour simplifier le partage et le transport de données, et se concentre sur la structuration de ces informations de manière logique.

## **Syntaxe de XML**

La syntaxe de XML est très simple et assez facile à apprendre.

Les documents XML doivent contenir un élément racine qui est le parent de tous les autres éléments :

```text
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```

La syntaxe ci-dessus montre l'élément racine qui est nécessaire lors de la création d'un code XML.

Mais l'élément racine peut s'appeler n'importe quoi. Par exemple :

```text
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Rappel</heading>
  <body>Ne m'oublie pas ce week-end !</body>
</note>
```

Dans le code ci-dessus, `<note>` est l'élément racine.

Avantages de l'utilisation de XML :

* Simplicité - Les documents XML sont des fichiers texte ordinaires qui peuvent être créés et édités avec n'importe quel éditeur de texte.
* Indépendance vis-à-vis des fournisseurs
* Indépendance vis-à-vis des plateformes
* Infrastructure extensive

Inconvénients de l'utilisation de XML :

* Syntaxe verbeuse et encombrante
* Stockage très inefficace