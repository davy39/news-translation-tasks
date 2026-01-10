---
title: Conseils et astuces pour créer des composants UI réutilisables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T18:29:17.000Z'
originalURL: https://freecodecamp.org/news/tips-tricks-for-creating-reusable-ui-components-2b1452147bda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Conseils et astuces pour créer des composants UI réutilisables
seo_desc: 'By Gabriel Colombo

  In this article I want to share some tips and tricks I use while building our core
  frontend library using Ember.js. Having no contact with it before, it has been a
  great learning opportunity. I hope you guys enjoy it! Please note, ...'
---

Par Gabriel Colombo

Dans cet article, je souhaite partager quelques conseils et astuces que j'utilise lors de la création de notre bibliothèque frontend principale avec Ember.js. N'ayant jamais été en contact avec ce framework auparavant, cela a été une grande opportunité d'apprentissage. J'espère que vous apprécierez ! Veuillez noter que le code utilisé pour illustrer les idées dans cet article contient juste assez d'informations pour faire passer le message. Il utilise également certains termes spécifiques à Ember.js, mais les concepts sont destinés à être indépendants du framework.

### Les objectifs

Pour faire simple, les exigences pour construire la bibliothèque sont les suivantes :

1. Elle doit être productive.
2. Elle doit être maintenable.
3. Elle doit être cohérente.

### Les approches

#### Minimiser la logique métier

L'un des problèmes les plus fréquents que je rencontre dans les projets sont les composants qui contiennent beaucoup trop de logique. Ainsi, ils effectuent des tâches qui, théoriquement, sont en dehors de leur portée.

Avant d'implémenter une fonctionnalité, il est bon de délimiter certaines des responsabilités du composant.

Imaginons que nous construisons un composant bouton.

Je voudrais pouvoir :

* Indiquer quel type de bouton il est — Primaire ou régulier
* Indiquer le contenu affiché à l'intérieur du bouton (Icône et texte)
* Désactiver ou activer le bouton
* Effectuer une action au clic

Avec ce petit schéma, décomposez les différentes parties impliquées dans le processus de construction de ce composant. Essayez d'identifier où les choses pourraient être placées.

1 — Le type et le contenu sont spécifiques au composant, donc ils peuvent être placés dans le fichier du composant.

Puisque le type est — dans une certaine mesure — requis, ajoutons une vérification au cas où aucune valeur n'aurait été fournie.

```
const type = get(this, 'type');
```

```
const types = {  primary: 'btn--primary',  regular: 'btn--regular',}
```

```
return (type) ? types[type] : types.regular;
```

J'aime mapper les propriétés dans un objet car cela permet de faire évoluer les choses sans trop d'effort — au cas où nous aurions besoin d'un bouton de danger ou autre chose de similaire.

2 — L'état désactivé peut être trouvé sur différents composants comme une entrée. Afin d'éviter la répétition, ce comportement peut être déplacé dans un module ou toute structure partagée — les gens l'appellent un _mixin_.

3 — L'action de clic peut être trouvée dans différents composants. Elle peut donc également être déplacée dans un autre fichier et ne doit contenir aucune logique — simplement appeler le callback fourni par le développeur.

De cette manière, nous pouvons avoir une idée des cas que notre composant doit traiter tout en aidant à définir une architecture de base qui supporte l'expansion.

#### Séparer l'état UI réutilisable

Certaines interactions UI sont courantes parmi différents composants, comme :

* Activer/désactiver — _ex. boutons, entrées_
* Étendre / Réduire — _ex. collapse, listes déroulantes_
* Afficher / masquer — _Pratiquement tout_

Ces propriétés sont souvent utilisées simplement pour contrôler l'état visuel — espérons-le.

Maintenez une nomenclature cohérente dans différents composants. Toutes les actions liées à un état visuel peuvent être déplacées dans un mixin.

```
/* UIStateMixin */
```

```
disable() {  set(this, 'disabled', true);
```

```
  return this;},
```

```
enable() {  set(this, 'disabled', false);
```

```
  return this;},
```

Chaque méthode est uniquement responsable de basculer une variable particulière et retourne le contexte actuel pour l'enchaînement, comme :

```
button  .disable()  .showLoadingIndicator();
```

Cette approche peut être étendue. Elle peut accepter différents contextes et contrôler des variables externes au lieu d'utiliser des variables internes. Par exemple :

```
_getCurrentDisabledAttr() {  return (isPresent(get(this, 'disabled')))    ? 'disabled'            /*  Paramètre externe  */    : 'isDisabled';         /*  Variable interne   */},
```

```
enable(context) {  set(context || this, this._getCurrentDisabledAttr(), false);
```

```
  return this;}
```

#### Abstraction des fonctionnalités de base

Chaque composant contient certaines routines. Ces routines doivent être effectuées indépendamment du but du composant. Par exemple, vérifier un callback avant de le déclencher.

Ces méthodes par défaut peuvent également être déplacées dans leurs propres mixins, comme suit :

```
/* BaseComponentMixin */
```

```
_isCallbackValid(callbackName) {  const callback = get(this, callbackName);    return !!(isPresent(callback) && typeof callback === 'function');},
```

```
_handleCallback(callback, params) {  if (!this._isCallbackValid(callback)) {    throw new Error(/* message */);  }
```

```
  this.sendAction(callback, params);},
```

Et ensuite inclus dans les composants.

```
/* Component */
```

```
onClick(params) {  this._handleCallback('onClick', params);}
```

Cela maintient votre architecture de base cohérente. Cela permet également l'expansion et même l'intégration avec des logiciels tiers. Mais s'il vous plaît, ne soyez pas un [_philosophizing abstracter_](https://www.quora.com/What-are-the-growth-stages-of-a-programmer/answer/Andreas-Blixt).

#### Composition des composants

Évitez de réécrire des fonctionnalités autant que possible. La spécialisation peut être atteinte. Elle peut être réalisée par composition et regroupement. Ainsi que par l'ajustement de petits composants ensemble afin de créer de nouveaux composants.

Par exemple :

```
Composants de base : Button, dropdown, input.
```

```
Dropdown button => button + dropdownAutocomplete => input + dropdownSelect => input (readonly) + dropdown
```

De cette manière, chaque composant a ses propres responsabilités. Chacun gère son propre état et ses paramètres tandis que le composant wrapper gère sa logique spécifique.

_Séparation des préoccupations à son meilleur._

#### Séparation des préoccupations

Lors de la composition de composants plus complexes, il est possible de séparer les préoccupations. Vous pouvez séparer les préoccupations entre différentes parties d'un composant.

Supposons que nous construisons un composant select.

```
{{form-select binding=productId items=items}}
```

```
items = [  { description: 'Product #1', value: 1 },  { description: 'Product #2', value: 2 }]
```

En interne, nous avons un simple composant input et un drop-down.

```
{{form-input binding=_description}}
```

```
{{ui-dropdown items=items onSelect=(action 'selectItem')}}
```

Notre tâche principale est de présenter la description à l'utilisateur, mais elle n'a pas de sens pour notre application — la valeur, si.

Lors de la sélection d'une option, vous divisez l'objet, envoyant la description vers notre input via une variable interne tout en poussant la valeur vers le contrôleur, mettant à jour la variable liée.

Ce concept peut être appliqué aux composants où la valeur liée doit être transformée, comme un nombre, un champ d'autocomplétion ou de sélection. Les sélecteurs de date peuvent également implémenter ce comportement. Ils peuvent démasquer la date avant de mettre à jour la variable liée tout en présentant la valeur masquée à l'utilisateur.

Les risques augmentent à mesure que les transformations deviennent plus complexes. Par une logique excessive ou en ayant à supporter des événements — alors réfléchissez bien avant d'implémenter cette approche.

#### Préréglages vs Nouveaux Composants

Parfois, il est nécessaire d'optimiser les composants et les services afin de faciliter le développement. Ceux-ci sont livrés sous forme de préréglages ou de nouveaux composants.

Les préréglages sont des paramètres. Lorsqu'ils sont informés, ils définissent des valeurs prédéfinies sur le composant, simplifiant sa déclaration. Cependant, les nouveaux composants sont généralement des versions plus spécialisées des composants de base.

La partie difficile est de savoir quand implémenter des préréglages ou créer de nouveaux composants. J'utilise les directives suivantes lorsque je prends cette décision :

**Quand créer des préréglages**

1 — Modèles d'utilisation répétitifs

Il arrive que qu'un composant particulier soit réutilisé à divers endroits avec les mêmes paramètres. Dans ces cas, je préfère les préréglages aux nouveaux composants, surtout lorsque le composant de base a un nombre excessif de paramètres.

```
/* Implémentation régulière */
```

```
{{form-autocomplete    binding=productId    url="products"            /*   URL à récupérer         */    labelAttr="description"   /*   Attribut utilisé comme label   */    valueAttr="id"            /*   Attribut utilisé comme valeur   */    apiAttr="product"         /*   Param envoyé dans la requête     */}}
```

```
/* Préréglages */
```

```
{{form-autocomplete    preset="product"    binding=productId}}
```

Les valeurs du préréglage ne sont définies que si le paramètre n'a pas été informé, conservant ainsi sa flexibilité.

```
/* Implémentation naïve du module de préréglages */
```

```
const presets = {  product: {    url: 'products',    labelAttr: 'description',    valueAttr: 'id',    apiAttr: 'product',  }, }
```

```
const attrs = presets[get(this, 'preset')];
```

```
Object.keys(attrs).forEach((prop) => {  if (!get(this, prop)) {    set(this, prop, attrs[prop]);  }});
```

Cette approche réduit les connaissances requises pour personnaliser votre composant. Simultanément, elle facilite la maintenance en vous permettant de mettre à jour les valeurs par défaut en un seul endroit.

2 — Le composant de base est trop complexe

Lorsque le composant de base que vous utiliseriez pour créer un composant plus spécifique accepte trop de paramètres. Ainsi, sa création générerait certains problèmes. Par exemple :

* Vous devriez injecter la plupart — si ce n'est tous — les paramètres du nouveau composant vers le composant de base. À mesure que de plus en plus de composants en dérivent, toute mise à jour du composant de base refléterait un énorme volume de changements. Ainsi, conduisant à une incidence plus élevée de bugs.
* À mesure que plus de composants sont créés, il devient plus difficile de documenter et de mémoriser les différentes nuances. Cela est particulièrement vrai pour les nouveaux développeurs.

**Quand créer de nouveaux composants**

1 — Étendre la fonctionnalité

Il est viable de créer un nouveau composant lors de l'extension de la fonctionnalité d'un composant plus simple. Cela vous aide à prévenir la fuite de logique spécifique à un composant vers un autre composant. Cela est particulièrement utile lors de l'implémentation d'un comportement supplémentaire.

```
/* Déclaration */
```

```
{{ui-button-dropdown items=items}}
```

```
/* Sous le capot */
```

```
{{#ui-button onClick=(action 'toggleDropdown')}}  {{label}} <i class="fa fa-chevron-down"></i>  {{/ui-button}}
```

```
{{#if isExpanded}}  {{ui-dropdown items=items}}{{/if}}
```

L'exemple ci-dessus utilise le composant bouton. Cela étend sa mise en page pour supporter une icône fixe tout en incluant un composant drop-down et son état de visibilité.

2 — Décorer les paramètres

Il existe une autre raison possible de créer de nouveaux composants. C'est lorsqu'il est nécessaire de contrôler la disponibilité des paramètres ou de décorer les valeurs par défaut.

```
/* Déclaration */
```

```
{{form-datepicker onFocus=(action 'doSomething')}}
```

```
/* Sous le capot */
```

```
{{form-input onFocus=(action '_onFocus')}}
```

```
_onFocus() {  $(this.element)    .find('input')    .select();                 /* Sélectionner la valeur du champ au focus */
```

```
  this._handleCallback('onFocus'); /* Déclenche le callback du paramètre */}
```

Dans cet exemple, une fonction destinée à être appelée lorsque le champ est focalisé a été fournie au composant.

En interne, au lieu de passer le callback directement au composant de base, il passe une fonction interne. Celle-ci effectue une tâche particulière (sélectionner la valeur du champ) puis appelle le callback fourni.

Il ne redirige pas tous les paramètres acceptés par le composant d'entrée de base. Cela aide à contrôler la portée de certaines fonctionnalités. Cela évite également les validations inutiles.

Dans mon cas, l'événement onBlur a été remplacé par un autre événement — onChange. Celui-ci se déclenche lorsque l'utilisateur remplit le champ ou sélectionne une date dans le calendrier.

### Conclusion

Lors de la construction de vos composants, considérez votre côté ainsi que celui de la personne utilisant ce composant dans sa vie quotidienne. De cette manière, tout le monde y gagne.

> Le meilleur résultat vient de chacun dans le groupe faisant ce qui est meilleur pour lui-même et le groupe — John Nash

De plus, n'ayez pas honte de demander des retours. Vous trouverez toujours quelque chose qui peut être amélioré.

Pour affûter encore plus vos compétences en ingénierie logicielle, je recommande de suivre la série d'Eric Elliott _Composing Software_. C'est génial !

Eh bien, j'espère que vous avez apprécié l'article. Veuillez prendre ces concepts, les transformer en vos propres idées et les partager avec nous !

De plus, n'hésitez pas à me contacter sur Twitter [@gcolombo_](https://twitter.com/gcolombo_) ! J'adorerais entendre votre opinion et même travailler ensemble.

Merci !