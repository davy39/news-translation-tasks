---
title: 'Accessibilité de niveau supérieur : 5 façons dont j''ai rendu le Guide freeCodeCamp
  utilisable pour les personnes handicapées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T21:22:50.000Z'
originalURL: https://freecodecamp.org/news/next-level-accessibility-freecodecamp-guide-7cbd6473eabd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4PC4r1YSSbxvkJEjE_eCbw.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Accessibilité de niveau supérieur : 5 façons dont j''ai rendu le Guide
  freeCodeCamp utilisable pour les personnes handicapées'
seo_desc: 'By Scott Vinkle

  I spent the majority of Hacktoberfest 2017 working with some great folks over at
  freeCodeCamp. My focus was specifically on helping to bring the accessibility of
  their Guide site to the next-level.

  The first time I saw the site I knew...'
---

Par Scott Vinkle

J'ai passé la majorité de [Hacktoberfest 2017](https://hacktoberfest.digitalocean.com/) à travailler avec des gens formidables chez [freeCodeCamp](https://www.freecodecamp.org/). Mon objectif était spécifiquement d'aider à porter l'accessibilité de leur site [Guide](https://guide.freecodecamp.org/) au niveau supérieur.

La première fois que j'ai vu le site, j'ai su qu'il serait une ressource fantastique pour beaucoup de gens, alors j'ai relevé le défi d'aider à garantir que son utilisabilité soit au top pour tout le monde !

Travailler sur le site était également très amusant car il est construit avec [React](https://reactjs.org/), ce qui a apporté quelques défis de codage supplémentaires en cours de route.

Examinons ensemble les **5 problèmes** que j'ai trouvés et comment je les ai résolus !

### Amélioration de l'accessibilité #1 : Lien de navigation de saut indisponible

L'une des premières choses que je vérifie sur un site est la présence d'un lien de navigation de saut. Les liens de navigation de saut sont une petite mais utile fonctionnalité pour tout site à avoir pour les utilisateurs de clavier uniquement ou de lecteur d'écran. Pourquoi ?

#### Le problème

Sans un lien de navigation de saut, les personnes utilisant uniquement le clavier pour naviguer devraient appuyer sur `Tab` pour chaque lien dans la barre latérale à chaque fois que la page se recharge. Comme il y a beaucoup de liens disponibles, naviguer dans cette section serait fastidieux.

#### La solution

La mise en place d'un lien de navigation de saut est assez simple. Il est généralement le premier élément dans le DOM (Document Object Model) et, au clic, le focus du clavier est envoyé à l'élément de la page qui contient le contenu principal de la page.

Le lien que j'ai ajouté a été codé comme suit :

```
<a className='skip-link sr-only sr-only-focusable' href='#main'>  Aller au contenu principal</a>
```

La valeur `#main` dans l'attribut `href` envoie le focus du clavier à l'élément de la page qui possède l'attribut `id="main"`.

Pour que cet élément de page puisse recevoir le focus du clavier, j'ai dû ajouter un attribut `tabindex` au conteneur :

```
<main className='main' id='main' tabIndex='-1'>  { props.children() }</main>
```

L'ajout de la valeur `tabindex` de `-1` permet à un élément non focusable de recevoir le focus de manière programmatique, mais il est exclu de l'ordre de tabulation naturel.

#### Le résultat

Avec le lien de navigation de saut en place, les personnes utilisant un clavier peuvent sauter les régions répétées comme la zone de navigation latérale pour atteindre facilement la section de contenu principal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X41ZaBWAUA96WNeTb34q4w.gif)
_GIF animé montrant le lien "Aller au contenu" qui n'est visible qu'au focus._

Consultez le changement de code complet dans la PR (Pull Request) : [Added skip link #4175](https://github.com/freeCodeCamp/guides/pull/4175).

### Amélioration de l'accessibilité #2 : Champ de recherche manquant une étiquette

J'ai remarqué que le champ de recherche `input` manquait une `label`. Avoir une `label` associée pour chaque `input` de formulaire est clé pour une expérience utilisateur réussie. Pourquoi ?

#### Le problème

Lorsque les champs `input` manquent une `label`, les lecteurs d'écran ne peuvent pas décrire avec précision quel est le but prévu du champ. Imaginez un instant un lien sans texte ; que fait ce lien ?

#### La solution

Celle-ci était assez simple. Ajouter une `label` à un `input` consiste à créer l'élément `label` avec un attribut `for`, puis à l'associer avec un `input` avec un `id`.

Pour ne pas perturber la conception actuelle du site, j'ai également ajouté la propriété `srOnly` pour que la `label` soit visuellement cachée.

La `label` a été codée comme suit :

```
<ControlLabel htmlFor='searchInput' srOnly={ true }>  Rechercher</ControlLabel>
```

Ensuite, pour le contrôle `input` existant, j'ai simplement ajouté la propriété `id='searchInput'`.

#### Le résultat

Maintenant, lorsque les utilisateurs de lecteurs d'écran naviguent vers le champ de recherche, ils entendront la valeur de la `label` _"rechercher"_ et auront plus de contexte sur ce qui est attendu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SPIYKJsNV9iHC6U-QMtsdA.png)
_Capture d'écran du contrôle de recherche après l'ajout de l'étiquette ; aucun changement visuel !_

Consultez le changement de code complet dans la PR : [Search input a11y updates #4123](https://github.com/freeCodeCamp/guides/pull/4123).

### Amélioration de l'accessibilité #3 : Ajustements des rôles de la barre latérale

En inspectant le code source HTML, j'ai remarqué que certains éléments de la barre latérale comportaient incorrectement des attributs `role="presentation"`. J'ai également remarqué que certains éléments étaient marqués comme des `div` au lieu d'un balisage sémantique approprié. Cela nécessitait quelques ajustements. Pourquoi ?

#### Le problème

Deux problèmes existaient avec cette section du site :

1. Lorsque vous appliquez `[role="presentation"](https://www.w3.org/TR/wai-aria-1.1/#presentation)` sur un élément, cela supprime toute signification sémantique. En d'autres termes, lorsqu'un lecteur d'écran rencontre l'élément, il n'y a pas d'annonce _significative_ pour notifier l'utilisateur de la fonction de l'élément. Imaginez un lien sur une page, mais son texte est de la même couleur que le texte du contenu et sans soulignement. Comment sauriez-vous que c'est un lien ?
2. L'autre problème ici est lorsque des éléments `div` sont utilisés pour marquer une structure significative. Comme vous le savez peut-être, les éléments `div` n'ont aucune signification sémantique et sont généralement réservés pour créer une structure sur une page. Dans les cas où ils sont utilisés à la place d'éléments sémantiques natifs, vous devriez appliquer l'attribut `role` approprié pour transmettre cette signification.

#### La solution

1. Pour chaque élément de liste de navigation et lien, j'ai simplement supprimé la propriété `role` afin de permettre à la signification sémantique de resplendir pour les utilisateurs de lecteurs d'écran.
2. Pour les composants dynamiques qui généraient des éléments `div`, j'ai appliqué des propriétés `role` appropriées, y compris `role="list"` pour le composant `PanelGroup`, et `role="listitem"` pour toute instance du composant `Panel`.

#### Le résultat

Avec les propriétés `role` ajustées, les utilisateurs de lecteurs d'écran entendront des annonces claires et précises lorsqu'ils rencontreront ces éléments, y compris :

* Les instances du composant `Link` seront annoncées comme un élément _"lien"_ — très important, et ;
* Les éléments du composant `PanelGroup` et `Panel` seront annoncés comme un élément _"liste"_. En conséquence, le nombre total d'éléments sera également annoncé, donnant un contexte du nombre d'éléments disponibles sur le chemin à venir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7tlF9wzW2yEDcE8GC6GYjw.png)
_Capture d'écran de la barre latérale après les ajustements des attributs de rôle ; aucun changement visuel !_

Consultez le changement de code complet dans la PR : [Side nav a11y updates #4093](https://github.com/freeCodeCamp/guides/pull/4093).

### Amélioration de l'accessibilité #4 : Disponibilité des résultats de recherche non annoncée

En tant qu'utilisateur voyant, j'étais conscient lorsqu'une recherche était réussie grâce à la zone de contenu principale changeant son contenu pour présenter une liste d'éléments. Mais qu'en est-il d'un utilisateur aveugle de lecteur d'écran ?

#### Le problème

Si un utilisateur de lecteur d'écran entrait du texte de recherche et appuyait sur `Entrée`, rien ne serait annoncé indiquant une recherche réussie ou des résultats. Comment quelqu'un pourrait-il savoir lorsque des éléments sont disponibles afin de continuer et de découvrir ce nouveau contenu ?

#### La solution

Pour que le nombre de résultats actuel soit annoncé, j'ai créé une nouvelle région `aria-live`, visuellement cachée. Cette région est remplie avec un nouveau contenu lorsque de nouveaux résultats de recherche sont présents.

La région est marquée à l'aide d'une `div` avec quelques attributs supplémentaires :

* `[aria-live="polite"](https://www.w3.org/TR/wai-aria-1.1/#aria-live)` crée la région "live" et indique aux lecteurs d'écran d'attendre que d'autres processus soient terminés avant d'annoncer son contenu.
* `[aria-atomic="true"](https://www.w3.org/TR/wai-aria-1.1/#aria-atomic)` indique aux lecteurs d'écran d'annoncer tout le texte dans la région, et non seulement le texte modifié.
* `[role="status"](https://www.w3.org/TR/wai-aria-1.1/#status)` définit l'attente pour les lecteurs d'écran d'interpréter le contenu live comme une information "conseil". En d'autres termes, c'est assez important, mais pas _critique_ (car les gens pourraient naviguer vers l'avant et découvrir le contenu par eux-mêmes.)

Voici à quoi ressemble le code final :

```
<div aria-atomic='true' aria-live='polite' className='sr-only' role='status'>  {`${results.length} résultat${results.length === 1 ? '' : 's'} trouvé${results.length === 1 ? '' : 's'}`}</div>
```

Remarquez l'utilisation de la [littérale de gabarit ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) pour interpoler le contenu ainsi que pour exécuter une instruction conditionnelle ternaire afin d'ajuster pour un état pluriel ou singulier.

#### Le résultat

Maintenant, avec un lecteur d'écran actif, après avoir soumis un terme de recherche, le nombre de résultats sera annoncé par la technologie d'assistance : _"20 résultats trouvés !"_

![Image](https://cdn-media-1.freecodecamp.org/images/1*cb-q7heN9pfleDkW69FGSg.png)
_Capture d'écran des résultats de recherche après l'ajout de la région live ; aucun changement visuel !_

Consultez le changement de code complet dans la PR : [Search results announcements #5137](https://github.com/freeCodeCamp/guides/pull/5137).

### Amélioration de l'accessibilité #5 : Gestion du focus des liens de la barre latérale

J'ai remarqué qu'en naviguant avec un clavier, après avoir cliqué sur un lien pour charger le contenu de la page, l'indicateur de focus restait sur l'élément actuel. C'était un problème. Pourquoi ?

#### Le problème

Sans une gestion appropriée du focus, les utilisateurs de clavier uniquement ou de lecteurs d'écran devraient naviguer à travers toute la navigation de la barre latérale pour atteindre le contenu de la page. Non seulement cela, mais il n'y a également aucune annonce audible alertant l'utilisateur qu'un événement a eu lieu lors du `click()`.

#### La solution

La solution que j'ai finie par adopter était un peu un hack. Normalement, vous créeriez une propriété `ref` sur le conteneur de contenu, puis vous passeriez l'objet `ref` au composant qui génère les éléments de lien de la barre latérale, puis vous définiriez `focus()` sur le conteneur lors du `click()`. Cela n'était pas une solution possible en raison du site utilisant quelque chose appelé Gatsby et il y avait un [problème avec le passage d'objets aux composants `Link`](https://github.com/freeCodeCamp/guides/issues/897#issuecomment-342404647). Je ne suis pas vraiment sûr du problème, mais cela n'a tout simplement pas coopéré.

Pour contourner cette limitation, ma solution a été la suivante :

1. J'ai ajouté un attribut `data-navitem="true"` à chacun des composants `Link` appropriés de la barre latérale.
2. Lors de l'événement `click()`, le composant `Article` se charge avec le contenu demandé, définissant `document.activeElement` sur l'élément de lien cliqué.
3. Dans la méthode `componentWillMount()` du composant `Article`, je vérifie si l'élément actuellement focalisé (le lien de la barre latérale via `document.activeElement`) possède l'attribut `data-navitem`.
4. Si cette condition est `true`, je déplace le focus du clavier vers l'élément `article`.

#### Le résultat

Maintenant, lorsque quelqu'un utilisant le clavier active l'un des liens de sous-navigation de la barre latérale, le focus du clavier se déplace vers le conteneur de contenu `article`. Et cela fournit également un contexte aux utilisateurs de lecteurs d'écran, indiquant que quelque chose s'est produit lors du `click()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Py_UmVtD1IbtcSem1OdBaw.gif)
_GIF animé montrant la gestion du focus vers l'article lors du clic sur un lien de la barre latérale._

Consultez le changement de code complet dans la PR : [NavItem focus #7818](https://github.com/freeCodeCamp/guides/pull/7818).

Et voilà ! Avec ces quelques ajustements, l'accessibilité et l'utilisabilité du site [freeCodeCamp Guide](https://guide.freecodecamp.org/) ont considérablement augmenté ! Les gens peuvent utiliser le site plus confortablement avec facilité et succès.

Ce n'est qu'un aperçu de haut niveau de quelques problèmes que j'ai abordés, mais je sais qu'il y a plus à faire. Tout le monde sur le [dépôt freeCodeCamp Guide](https://github.com/freeCodeCamp/guides) était très amical et désireux d'aider à répondre à mes questions de débutant sur React, alors n'hésitez pas si vous voulez aider !

Bon hacking ! 😊