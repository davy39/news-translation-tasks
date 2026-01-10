---
title: Comment rendre l'impossible possible en CSS avec un peu de créativité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T16:19:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-the-impossible-possible-in-css-with-a-little-creativity-bd96bb42b29d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xPfQM8antkW3PhlH
tags:
- name: creativity
  slug: creativity
- name: CSS
  slug: css
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment rendre l'impossible possible en CSS avec un peu de créativité
seo_desc: 'By Facundo Corradini

  If you ever used CSS sibling selectors, you know there’s only two. The + sibling
  combinator selects the first match that comes immediately after, and the ~ subsequent-sibling
  combinator matches all the ones that come after.But th...'
---

Par Facundo Corradini

Si vous avez déjà utilisé [les sélecteurs de frères et sœurs CSS,](https://www.w3.org/TR/selectors-3/#adjacent-sibling-combinators) vous savez qu'il n'y en a que deux. Le combinateur de frères et sœurs `+` sélectionne la première correspondance qui vient immédiatement après, et le combinateur de frères et sœurs suivants `~` correspond à tous ceux qui viennent après. 
Mais il n'y a aucun moyen de sélectionner ce qui est venu avant. Soit les sélecteurs de parents, soit les sélecteurs de frères et sœurs précédents n'existent tout simplement pas.

Je sais que vous le voulez, vous savez que je le veux, mais la vérité cruelle est qu'ils n'existent pas (et qu'ils n'existeront probablement jamais). Il y a un million de posts sur les raisons. Il y a même des propositions sur la façon de les implémenter. Mais nous sommes coincés dans le traitement unidirectionnel des règles CSS, très probablement pour nous protéger de notre "manque d'expertise" qui nous coincerait dans des re-flux et même des boucles infinies.

Heureusement, comme pour la plupart des limitations CSS, **nous pouvons le simuler**.

La première chose à considérer est pourquoi nous voulons des frères et sœurs précédents pour commencer.   
Deux cas me viennent à l'esprit :

1. Nous devons sélectionner tous les frères et sœurs d'un certain élément, et le combinateur de frères et sœurs suivants `~` ne sélectionne que ceux qui viennent après.
2. Nous devons sélectionner uniquement les frères et sœurs qui sont venus avant

### 1. Sélectionner tous les frères et sœurs

Parfois, nous devons sélectionner à la fois les frères et sœurs précédents et suivants. Pour ce faire, nous pouvons en fait sélectionner le parent et utiliser quelques astuces autour de celui-ci.

Par exemple, pour sélectionner tous les spans dans la structure suivante lorsque nous survolons l'un d'eux, nous pourrions simplement utiliser le sélecteur d'enfant sur le survol du parent. Nous nous assurons de désactiver les `pointer-events` du parent et de les réinitialiser sur les enfants. Ainsi, toute action que nous voulons déclencher ne se produira que lorsque nous entrerons dans l'enfant et non dans le parent lui-même.

Si vous devez sélectionner tous les frères et sœurs _sauf_ celui qui est survolé, vous pouvez combiner la technique précédente avec le sélecteur `:not` pour l'exclure.

Un cas d'utilisation typique pour cela est les menus :

Le code ci-dessus réduira l'opacité de tous les éléments `<li>` sauf celui qui est survolé.

De plus, vous pourriez utiliser des filtres tels que les sélecteurs de type et nth pour être extra précis sur les frères et sœurs que vous souhaitez affecter.

Avec un peu de style, cela devrait fonctionner comme ceci :

**Veuillez noter** : Si vous allez utiliser l'approche `pointer-events:none`, gardez à l'esprit qu'elle peut perturber l'empilement (peut vous permettre de sélectionner des éléments qui sont "en dessous" dans l'ordre d'empilement). Elle ne fonctionnera pas non plus dans IE10 et les versions antérieures, en plus de l'implication que vous pourriez avoir besoin des événements de pointeur pour autre chose. Soyez donc extra prudent lorsque vous l'utilisez.

### 2. Sélectionner ce qui est venu avant

Pour ce cas d'utilisation, nous pouvons inverser l'ordre dans le HTML, puis le trier à nouveau dans CSS, et utiliser le combinateur de frères et sœurs suivants `~` ou le sélecteur de frères et sœurs adjacents `+`. De cette façon, nous sélectionnerons les frères et sœurs suivants, mais cela donnera l'impression que nous sélectionnons les précédents.

Il existe plusieurs façons de faire cela. La plus simple et probablement la plus ancienne consiste à changer la direction d'écriture de notre conteneur :

Si vos éléments doivent afficher du texte réel, vous pouvez toujours le réinverser :

Mais cela peut devenir ingérable de plusieurs façons. Heureusement, la boîte à outils CSS moderne rend cela beaucoup plus simple et plus sûr. Nous pouvons simplement utiliser Flexbox sur le conteneur et inverser l'ordre avec `flex-direction:row-reverse` :

Le meilleur aspect de l'approche Flexbox est que nous ne perturbons pas la direction d'écriture. Nous n'avons pas besoin de réinitialiser les enfants, et tout est beaucoup plus prévisible.

### Utiliser les "frères et sœurs précédents" pour créer un système de notation par étoiles en CSS uniquement

Sémantiquement, un système de notation peut être considéré comme une simple liste de boutons radio avec leurs étiquettes correspondantes. Cela s'avère utile, car cela nous permettra d'utiliser le pseudo-sélecteur `:checked` pour modifier les frères et sœurs.

Commençons donc par là :

Comme nous l'avons discuté précédemment, les éléments sont dans l'ordre inverse pour permettre un sélecteur de "frères et sœurs précédents". Remarquez que nous utilisons le caractère unicode "étoile blanche" (U+2606) pour représenter les étoiles vides.

Affichons-les côte à côte, dans le bon ordre (inverse) :

Maintenant, masquons les boutons radio eux-mêmes, personne ne veut voir cela :

Et appliquons un peu de style aux caractères d'étoile :

La seule ligne vraiment importante là-bas est le `position:relative`. Il nous permettra de positionner absolument un pseudo-élément d'étoile remplie (U+2605) par-dessus, qui sera initialement masqué.

Lorsque nous survolons une étoile, le pseudo-élément d'étoile remplie doit devenir visible pour celle-ci et tous les frères et sœurs _précédents_.

Même chose pour la note sélectionnée, en faisant correspondre toutes les étiquettes qui viennent _avant_ le bouton radio coché :

**Rappelez-vous** que l'utilisation du drapeau !important est **exactement le contraire** d'une bonne pratique. Je le fais ici car il n'y a pas d'autre moyen d'atteindre la fonctionnalité ajoutée discutée dans la section suivante sans cela.

Dernier point mais non des moindres, nous devons "nous souvenir" de la note actuelle, au cas où l'utilisateur souhaiterait la changer. Par exemple, s'ils avaient sélectionné cinq étoiles, et pour une raison quelconque veulent la changer en quatre, nous devrions afficher les étoiles 1 à 4 comme remplies et la cinquième comme semi-transparente lors du survol de la quatrième.

Cela peut être réalisé en changeant l'opacité des frères et sœurs _précédents_ de l'entrée cochée lors du survol du conteneur :

C'est aussi pourquoi nous avions besoin de `opacity:1 !important` dans la déclaration de survol initiale. Sinon, cette dernière règle aurait remporté le concours de spécificité et appliqué un remplissage semi-transparent à tout.

Et voilà, un système de notation par étoiles entièrement fonctionnel et compatible avec tous les navigateurs, utilisant des sélecteurs de "frères et sœurs précédents" en CSS uniquement.

Comme vous pouvez le voir, juste parce que "c'est impossible" ne signifie pas que vous ne devriez pas essayer. La programmation consiste à repousser les limites. Donc, chaque fois que vous heurtez le mur, poussez un peu plus fort. Ou je suppose que trouver votre chemin autour de celui-ci pourrait être une meilleure analogie ?... de toute façon, vous savez ce que je veux dire. Continuez à bidouiller !

### Une note sur l'accessibilité

**L'extrait précédent est une simplification afin de le rendre facile à comprendre.** Ce n'est **pas** quelque chose que je recommanderais d'utiliser en production en raison de nombreuses limitations d'accessibilité.

Pour rendre l'extrait un peu plus accessible, la première chose à faire serait de masquer les boutons radio avec presque n'importe quelle technique autre que `display:none` pour les rendre focusables. Nous devrions également ajouter un anneau de focus sur l'ensemble de l'extrait d'étoiles lorsque n'importe quel élément à l'intérieur est focusé, via le pseudo-sélecteur `:focus-within`.

Les étiquettes identiques "★" n'ont aucun sens pour les lecteurs d'écran, donc la meilleure approche serait d'avoir un `<span>` à l'intérieur de l'étiquette avec le texte "n étoiles", qui sera masqué pour les utilisateurs voyants.

De plus, l'approche de la source HTML inversée + `display:row-reverse` rend la notation au clavier maladroite, car elle n'est pas réinversée. [Flexbox et l'accessibilité au clavier](https://tink.uk/flexbox-the-keyboard-navigation-disconnect/) est un sujet assez compliqué, mais la chose la plus proche d'une solution pour cela est d'ajouter une balise `aria-flowto` à chaque élément, ce qui au moins corrige le problème pour certaines combinaisons de lecteurs d'écran + navigateurs.

Pour un extrait plus accessible (utilisant une technique alternative de modification des frères et sœurs suivants pour qu'ils semblent vides au lieu d'essayer d'évaluer les précédents), consultez [Patrick Cole](https://www.freecodecamp.org/news/how-to-make-the-impossible-possible-in-css-with-a-little-creativity-bd96bb42b29d/undefined), comme nous l'avons discuté dans les réponses ci-dessous.