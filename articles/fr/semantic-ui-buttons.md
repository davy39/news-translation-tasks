---
title: Boutons Semantic UI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T21:05:00.000Z'
originalURL: https://freecodecamp.org/news/semantic-ui-buttons
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e52740569d1a4ca3c83.jpg
tags:
- name: toothbrush
  slug: toothbrush
- name: UI Design
  slug: ui-design
seo_title: Boutons Semantic UI
seo_desc: 'What are Semantic UI Buttons?

  A button indicates a possible user action. Semantic UI provides an easy-to-use syntax
  that simplifies not only the styling of a button, but also the natural language
  semantics.

  How to use them

  The Semantic UI class is si...'
---

## **Qu'est-ce que les boutons Semantic UI ?**

Un bouton indique une action possible de l'utilisateur. Semantic UI fournit une syntaxe facile à utiliser qui simplifie non seulement le style d'un bouton, mais aussi la sémantique du langage naturel.

## Comment les utiliser

La classe Semantic UI est simplement ajoutée à un élément bouton. Divers exemples sont donnés ci-dessous pour indiquer comment l'utiliser.

### Types

* Bouton Standard

Bouton Semantic UI standard

```text
<button class="ui button">Bouton Standard</button>
```

* Bouton d'Emphase

Un bouton avec un niveau d'emphase différent

```text
<button class="ui primary button">
```

D'autres classes d'emphase sont `secondary`, `positive`, et `negative`

* Bouton Animé

Un bouton avec animation, montrant des contenus cachés

```text
<div class="ui animated fade button" tabindex="0">
  <div class="visible content">Inscription pour un compte Pro</div>
  <div class="hidden content">12,99 $ par mois</div>
</div>
```

La propriété `tabindex="0"` ci-dessus rend le bouton focusable au clavier, puisque la balise `<button>` n'a pas été utilisée.

* Bouton avec Libellé

Un bouton accompagné d'un libellé

```text
<div class="ui labeled button" tabindex="0">
  <div class="ui button"><i class="heart icon"></i> J'aime</div>
  <a class="ui basic label">2 048</a>
</div>
```

L'élément `<i>` est utilisé pour spécifier une icône, ici il s'agit d'une icône de cœur `<i class="heart icon"></i>` accompagnée d'un libellé basique `<a class="ui basic label">2 048</a>`

* Bouton Icône

Un bouton Semantic UI peut être simplement une icône

```text
<button class="ui icon button">
  <i class="camera icon"></i>
</button>
```

Le bouton ci-dessus est simplement une icône d'appareil photo

### Groupes

Les boutons Semantic UI peuvent exister dans un groupe

```text
<div class="ui buttons">
  <button class="ui button">Un</button>
  <button class="ui button">Deux</button>
  <button class="ui button">Trois</button>
</div>
```

### Contenu

Les boutons Semantic UI peuvent contenir des conditionnels

```text
<div class="ui buttons">
  <button class="ui positive button">Oui</button>
  <div class="or" data-text="ou"></div>
  <button class="ui negative button">Non</button>
</div>
```

### États

Les boutons Semantic UI peuvent exister dans différents états, `active`, `disabled`, `loading`. Il suffit d'ajouter un nom d'état à l'attribut `class` de l'élément.

```text
<button class="ui loading button">Chargement</button>
```

### Variations

Les boutons Semantic UI existent en plusieurs tailles, `mini`, `tiny`, `small`, `medium`, `large`, `big`, `huge`, et `massive`.

```text
<button class="ui massive button">Bouton Massif</button>
```

Il y a beaucoup plus à savoir sur les boutons Semantic UI, visitez le lien fourni dans la section Plus d'Informations pour en apprendre davantage.

#### **Plus d'Informations :**

* [Documentation des Boutons Semantic UI](https://semantic-ui.com/elements/button.html)