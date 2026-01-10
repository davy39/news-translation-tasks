---
title: Accessibilité Web – Erreurs ARIA courantes à éviter
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2023-01-11T21:58:45.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-common-aria-mistakes-to-avoid
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/a11y-image.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: Accessibilité Web – Erreurs ARIA courantes à éviter
seo_desc: 'Accessible Rich Internet Applications – or ARIA – is a set of attributes
  and roles defined by the Web Accessibility Initiative. These make the web more accessible
  to people with disabilities.

  ARIA is extremely important for building accessible web ap...'
---

Les Applications Internet Riches Accessibles – ou ARIA – sont un ensemble d'attributs et de rôles définis par l'[Initiative pour l'Accessibilité du Web](https://www.w3.org/WAI/). Ceux-ci rendent le web plus accessible aux personnes en situation de handicap.

ARIA est extrêmement important pour construire des applications web accessibles. Mais il est très facile de mal utiliser ARIA et de rendre le site web moins accessible.

Cet article démontrera cinq erreurs ARIA courantes et comment les corriger.

## Ne pas utiliser de labels ARIA inutiles

La première règle de ARIA est que vous ne devriez pas utiliser ARIA sauf si vous y êtes obligé. Les éléments HTML ont déjà une accessibilité intégrée, et l'ajout de labels ARIA inutiles peut casser l'accessibilité.

Pour cette raison, il est beaucoup mieux d'utiliser des éléments HTML, au lieu de construire du code avec des labels ARIA.

**Exemple de mauvaise utilisation des labels ARIA :**

⚠️ MAUVAIS : Ci-dessous se trouve un élément `button` avec `aria-label` :

```html
<button aria-label="Envoyer">Envoyer</button>
```

✅ BON : Ci-dessous se trouve un élément `button` :

```html
<button>Envoyer</button>
```

Dans les exemples ci-dessus, je crée un élément bouton. Dans le premier extrait de code, il y a un `aria-label` avec le label « Envoyer ». L'élément bouton de HTML a déjà une accessibilité intégrée. Il n'est pas nécessaire d'ajouter un `aria-label`, il est donc beaucoup mieux de supprimer le label.

L'élément `button` lira déjà le texte à l'intérieur. Nous n'avons pas besoin d'ajouter le `aria-label` pour le décrire.

**À retenir :** N'ajoutez pas de labels ARIA inutiles si vous pouvez utiliser des éléments HTML accessibles à la place.

## Ne pas utiliser les mauvais attributs ARIA

Il existe des états et propriétés ARIA prédéfinis par le groupe de travail ARIA, qui fait partie du World Wide Web Consortium.

Les développeurs doivent utiliser les états et propriétés disponibles – vous ne pouvez pas créer les vôtres dans votre code. Vous pouvez trouver la liste des propriétés et états sur le [Site Web de W3](https://www.w3.org/TR/wai-aria-1.0/states_and_properties).

**Exemple d'utilisation d'attributs ARIA incorrects :**

⚠️ MAUVAIS

```html
<span aria-donotshow="true">Ne pas montrer ceci</span>
```

✅ BON

```html
<span aria-hidden="true">Ne pas montrer ceci</span>
```

Cela signifie qu'une nouvelle propriété, comme `aria-donotshow`, n'est pas correcte. `aria-donotshow` n'est pas une propriété sur le site W3, vous ne devriez donc pas l'utiliser.

**À retenir :** Ne créez pas vos propres attributs ARIA. Vous ne pouvez utiliser que ceux définis par le groupe de travail ARIA.

## Savoir quand utiliser `aria-labelledby`

Une autre erreur courante est lorsque les développeurs utilisent `aria-label` pour décrire le contenu à l'intérieur du DOM.

Tous les éléments interactifs ont besoin d'un nom accessible. Si nous voulons ajouter un nom accessible à un élément où le nom a besoin de contenu provenant d'ailleurs dans le DOM, nous devons utiliser `aria-labelledby`. Si aucun contenu ne peut être référencé pour créer un nom accessible, alors nous pouvons utiliser `aria-label`.

**Exemple de quand utiliser** `aria-labelledby` :

⚠️ MAUVAIS

```html
<div aria-label="Contenu Connexe">				
    <span>Contenu Connexe</span>		
</div>
```

✅ BON

```html
<div aria-labelledby="nav-title">				
    <span id='nav-title'>Contenu Connexe</span>		
</div>
```

Dans l'exemple ci-dessus, le premier extrait de code utilise `aria-label` et l'associe au texte « Contenu Connexe ». Mais le `span` à l'intérieur du texte contient déjà le contenu correct que nous voulons qu'un lecteur d'écran lise.

Au lieu d'utiliser `aria-label` dans cet exemple, nous devons référencer le contenu du span en ajoutant `aria-labelledby` qui est associé à l'id du contenu que nous voulons référencer.

**À retenir :** Si vous voulez référencer du contenu à l'intérieur du DOM, utilisez `aria-labelledby` avec l'id correspondant.

## Savoir quand utiliser `aria-describedby`

Parfois, nous devons donner plus d'informations à un élément. Par exemple, nous pouvons vouloir dire à l'utilisateur que le bouton qu'il va presser ouvrira un nouvel onglet.

Cette information est importante car l'utilisateur doit savoir où il se trouve lors de la navigation sur les sites web.

Pour ces types de scénarios, nous pouvons utiliser `aria-describedby` pour donner des informations supplémentaires.

**Exemple :**

⚠️ MAUVAIS

```html
<button aria-label="Fermer" aria-label="Ouvre dans un nouvel onglet">	
Montrer le contenu connexe		
</button>
```

✅ BON

```html
<button aria-label="Fermer" aria-describedby="description">			Montrer le contenu connexe		
</button>		
<div id="description">Ouvre dans un nouvel onglet</div>
```

Dans le premier exemple ci-dessus, ce que les ingénieurs s'attendent à ce que le lecteur d'écran annonce est : « bouton, Montrer le contenu connexe, ouvre dans un nouvel onglet ».

Mais le lecteur d'écran ne fait pas cela. Au lieu de cela, il dit : « bouton, ouvre dans un nouvel onglet ». Le lecteur d'écran ne lit pas le contenu à l'intérieur, car aria-label remplace toujours le contenu textuel de l'élément HTML5 auquel il a été appliqué.

Le deuxième extrait de code montre la bonne façon d'utiliser `aria-describedby`. Le lecteur d'écran lira : « bouton, Montrer le contenu connexe, ouvre dans un nouvel onglet ».

Ces informations indiquent à l'utilisateur que le bouton sert à montrer le contenu connexe et que s'il presse ce bouton, il le dirigera vers un autre onglet.

**À retenir :** Utilisez `aria-describedby` pour ajouter des informations supplémentaires aux éléments.

## Ne pas utiliser les rôles enfants ARIA sans les rôles parents

Il existe certains attributs ARIA qui nécessitent une relation parent/enfant. Cela signifie que vous ne pouvez pas utiliser l'attribut enfant ARIA sans l'envelopper autour de son attribut parent ARIA.

Il est facile d'oublier la relation parent/enfant et de construire du code qui n'utilise que l'attribut parent sans l'enfant, ou de construire du code qui n'utilise que l'attribut enfant sans son parent.

Si vous oubliez la relation parent/enfant, le code devient plus inaccessible, ce qui va à l'encontre du but de ARIA.

**Exemple :**

⚠️ MAUVAIS :

`role="listbox"` est une propriété parent. La liste `ul` ci-dessous n'a pas `role=option` qui est sa propriété enfant.

```html
<div role="listbox">
    <ul>
        <li></li>
    </ul>
</div>
```

✅ BON :

`role="listbox"` est une propriété parent. La liste `ul` ci-dessous a `role=option` qui est sa propriété enfant.

```html
<div role="listbox">
    <ul>
        <li option="option"></li>
    </ul>
</div>
```

Dans l'exemple de code ci-dessus, le premier code a un extrait de code qui a `role=listbox` qui est un élément parent. `listbox` a besoin d'enfants à l'intérieur qui sont `option`. Nous ne pouvons pas utiliser `listbox` seul pour construire des sites web accessibles.

**À retenir :** Utilisez toujours les propriétés parent/enfant ensemble.

## Résumé

ARIA est un ensemble d'attributs et de rôles définis par WAI pour rendre le web plus accessible aux personnes en situation de handicap. Bien qu'il soit nécessaire de créer un web accessible, il est très facile de mal utiliser ARIA et de rendre les sites web moins accessibles.

Essayez d'éviter ces cinq erreurs ARIA les plus courantes :

1. N'utilisez pas inutilement aria-label. Les sémantiques HTML intégrées sont toujours meilleures.
   
2. Ne créez pas votre propre attribut aria. Utilisez uniquement ceux définis par ARIA.
   
3. Utilisez `aria-labelledby` avec un id lorsque vous avez du contenu qui enveloppe des divs et que vous voulez regrouper des sections.
   
4. Utilisez `aria-describedby` lorsque vous avez des sections qui nécessitent plus de descriptions.
   
5. N'utilisez pas un ARIA enfant sans un ARIA parent prédéfini.
   

ARIA a été créé pour rendre les sites web plus accessibles aux personnes en situation de handicap. Si nous évitons les erreurs courantes, nous nous assurerons que nos sites web sont accessibles.