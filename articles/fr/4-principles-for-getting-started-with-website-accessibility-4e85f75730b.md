---
title: Comment commencer avec l'accessibilité des sites web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T11:01:02.000Z'
originalURL: https://freecodecamp.org/news/4-principles-for-getting-started-with-website-accessibility-4e85f75730b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gSXpULAAseIwyvF6rs_t5Q.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment commencer avec l'accessibilité des sites web
seo_desc: 'By Ben Robertson

  When I was entering the front end developer ranks, no one talked to me about accessibility.
  I didn’t know you could break the law by having an inaccessible website, until one
  day a university client came to my team for help on perfor...'
---

Par Ben Robertson

Lorsque j'ai commencé à travailler comme développeur front-end, personne ne m'a parlé d'[accessibilité](https://benrobertson.io/accessibility). Je ne savais pas qu'on pouvait enfreindre la loi en ayant un site web inaccessible, jusqu'au jour où un client universitaire est venu vers mon équipe pour obtenir de l'aide afin de réaliser un audit d'accessibilité. J'étais complètement dépassé.

J'ai commencé à creuser et à faire des recherches, mais j'ai trouvé une grande partie de la documentation intimidante. Certaines choses étaient au-dessus de ma tête. Il y avait tellement de choses à assimiler, mais j'ai finalement réussi à m'en sortir. (En fait, je suis encore en train de m'en sortir).

J'ai depuis appris que l'accessibilité n'a pas à être intimidante, et peut même être amusante.

Ce qui m'aurait aidé au début, ce sont quelques principes pratiques pour m'aider à comprendre les bases.

Alors, laissez-moi vous partager : **Les principes d'accessibilité web maison de Ben.**

Ce ne sont pas des règles.

Ce sont des changements mentaux que j'ai dû faire lorsque j'ai commencé à développer des sites web accessibles.

Commençons.

### Principe 1 : Le design web est plus que du design graphique

Lorsque j'ai commencé mon premier emploi dans le web, on m'a donné une image d'un site web et on m'a demandé de la transformer en un site web.

Après avoir fait cela, les designers ont ensuite comparé méticuleusement mon site web à leur image de site web et m'ont dit toutes les erreurs que j'avais faites.

> _La hauteur de ligne doit être de 18px, pas 16._

> _Ce gris n'est pas le bon gris clair. Il devrait être gris très clair._

> _Le flou de l'ombre de la boîte est décalé d'un pixel._

Des choses comme ça. Ils étaient très impressionnants et j'ai appris énormément.

Mais aucun de nous n'a vraiment considéré que le web n'est pas un médium contrôlé. Nous étions si préoccupés par les éléments visuels du travail que nous n'avons pas considéré comment le site pourrait performer sur un téléphone Android à 99 $ en 3G, ou pour quelqu'un qui était daltonien, ou quelqu'un qui ne pouvait pas voir du tout.

Et le fait que le web puisse être accessible par différentes personnes dans différentes situations est ce qui fait que le design web est bien plus que du design graphique.

Alors, au lieu de me concentrer uniquement sur les éléments visuels, j'ai divisé mon travail en trois tâches principales.

#### Trois tâches du design web

**Tâche 1 : Écrire un bon balisage (lire : sémantique)**

La première tâche est d'écrire un bon balisage.

Cela signifie organiser le contenu de la page de manière appropriée. Utiliser le HTML comme il était censé être utilisé. Le HTML est accessible par défaut. Donc, si nous faisons cela correctement dès le début, notre travail sera beaucoup plus facile. Nous passerons un peu plus de temps sur cela plus tard.

**Tâche 2 : Améliorer le balisage avec CSS**

La deuxième tâche est d'utiliser CSS pour **améliorer** l'excellent balisage que nous avons écrit.

Le CSS doit être utilisé pour souligner la signification de votre contenu. Il doit le rendre plus significatif, plus impactant. Mais vous devez utiliser le bon HTML dès le début, sinon votre travail sera beaucoup plus difficile.

**Tâche 3 : Ajouter une couche d'interactivité sur votre HTML et CSS avec JavaScript**

La troisième tâche est d'ajouter une couche d'interactivité sur la structure et le style avec JavaScript.

#### Avant et après

Avant d'adopter cette approche, j'avais l'habitude de simplement choisir l'élément le plus facile à styliser et de l'utiliser.

> _J'ai besoin d'un texte grand, donc j'utiliserai un h1._

> _J'ai une interface d'accordéon compliquée, donc j'utiliserai un tas de divs._

Des choses comme ça. Mais cela ne se concentre que sur les aspects **visuels**. Pour construire des sites web accessibles, nous devons penser à plus que simplement à la correspondance du site avec l'image. C'est plus que le design visuel ou graphique. C'est pourquoi nous l'appelons le design web.

Cela nous amène au principe 2.

### Principe 2 : Soyez ASAP (aussi sémantique que possible)

Voici comment je recommande de faire cela.

Chaque fois que vous commencez à taper `<d`iv>...

Arrêtez.

Regardez-vous dans le miroir.

Et demandez-vous.

_Pourrais-je utiliser un élément plus sémantique ?_

Comment savez-vous s'il existe un élément plus sémantique à utiliser ?

Le Mozilla Development Network a une page de [tous les éléments HTML organisés par leur but](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). (Cette référence est géniale — utilisez-la !)

![Image](https://cdn-media-1.freecodecamp.org/images/tWhH-vQt-omDDVvjExK14iIeGOOn6qr1MWl9)

Examinons quelques-unes des alternatives sémantiques que nous avons pour les `<d`iv>.

#### Alternatives à `<d`iv>

Si vous avez une section autonome d'une page, envisagez d'utiliser la balise `<secti`on>.

Si vous avez un blog, un article de presse, un message de forum ou tout type de contenu autonome, vous pourriez utiliser un `<artic`le>.

Vous avez plusieurs composants du même type les uns à côté des autres ? Envisagez d'utiliser une liste ordonnée ou non ordonnée (`<`ul> ou <ol>).

Vous avez une section supérieure sur votre article de blog avec un titre et des métadonnées ? Utilisez un `<head`er>. Vous avez une section inférieure avec des tags et autres ? Utilisez un `<footer>`.

Vous avez une barre latérale ? Utilisez un `<aside>` !

Vous avez quelque chose qui doit être cliquable ? Utilisez un `<button>`. Celui-ci est important. Si cela doit être cliquable et n'est pas un lien, vous devriez probablement utiliser un bouton.

Permettez-moi de répéter cela : Si cela doit être cliquable et n'est pas un lien, vous devriez probablement [utiliser un bouton](https://benrobertson.io/accessibility/javascript-accessibility#1-use-the-button-element-for-anything-that-users-click-on). Nous en parlerons plus tard.

Rappelez-vous simplement : [Soyez ASAP. Aussi sémantique que possible](https://benrobertson.io/accessibility/principles-getting-started-website-accessibility#principle-2-be-asap-as-semantic-as-possible).

### Principe 3 : Les sites web doivent bien paraître nus

Ce que je veux dire par là, c'est que si vous retirez tout le CSS de votre page, votre site web doit toujours être lisible et utilisable.

Ce principe renforce vraiment le point du [principe 2 ASAP](https://benrobertson.io/accessibility/principles-getting-started-website-accessibility#principle-2-be-asap-as-semantic-as-possible).

Pensez-y de cette manière : si votre balisage est sémantique, alors vous utilisez des éléments qui transmettent une signification. Et cela signifie que le navigateur fournira des affordances et des signifiants pour la signification et/ou la fonctionnalité de votre balisage.

Donc, le "test nu" est vraiment un test de la sémantique de votre balisage.

Votre balisage doit ressembler à un plan bien structuré, comme ceux que nous faisions à l'école pour les dissertations.

#### Comment vérifier cela ?

Voici le code. Si vous collez cela dans la console de vos outils de développement, il supprimera tout ce qui se trouve dans le `<he`ad> de votre document, y compris les styles.

```
document.head.parentNode.removeChild(document.head);
```

Ce qu'il fait, c'est cibler la tête du document et ensuite supprimer tous ses enfants.

La plupart du temps, j'utilise cela comme un petit bookmarklet dans mon navigateur.

```javascript
javascript:(function() { document.head.parentNode.removeChild(document.head); })();
```

Pour utiliser cela comme un bookmarklet, ajoutez un nouveau marque-page dans votre navigateur. Dans le champ URL, copiez et collez le code ci-dessus au lieu d'une URL. Maintenant, vous pouvez cliquer sur ce marque-page sur n'importe quel site et il supprimera tous les styles de la tête du document.

Regardons un exemple de cela en action.

### Le formulaire de connexion Google

Je pense que tout le monde est probablement familier avec le formulaire de connexion Google. Il a un titre, la saisie de l'email, et quelques boutons pour Email oublié, Créer un compte, et Suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/mfAeK10fGQruahB-4ziHXJpOWi3hzENgN5LP)
_Le formulaire de connexion Google_

Alors, que se passe-t-il lorsque nous le regardons nu ?

### Formulaire de connexion Google nu

![Image](https://cdn-media-1.freecodecamp.org/images/uiaI-fFomYCz8C8dFkKMnyWUFT-gWeNj7H2D)
_Le formulaire de connexion Google avec le CSS retiré._

Après avoir retiré les styles, nous avons toujours le bel en-tête "Connexion", donc nous savons de quoi parle cette page.

Nous avons quelques champs de saisie, mais les étiquettes ne sont pas exactement claires.

Et... où sont passés nos boutons ?

Si vous regardez de près, vous pouvez voir que ce qui était autrefois les boutons "Suivant", "Email oublié" et "Créer un compte" apparaissent maintenant tous comme du texte normal.

Nous avons maintenant trois champs de saisie au lieu d'un seul, et les étiquettes semblent être après eux.

Les boutons Suivant et Créer un compte ont échangé leurs positions.

Donc, tout est toujours là, mais je dirais que la principale préoccupation que j'ai est que les boutons ne sont pas vraiment des boutons. Ils ne sont pas clairs.

Et laissez-moi simplement dire que juste parce que Google n'utilise pas l'élément HTML `<butt`on> ne signifie pas que ce formulaire est intrinsèquement inaccessible. Cela signifie simplement qu'ils doivent faire beaucoup plus de travail avec JavaScript et gérer les interactions clavier que le navigateur ferait typiquement pour vous.

J'utilise généralement le test nu comme un contrôle pour moi-même. Juste parce qu'un site échoue au test nu ne signifie pas que le site est nécessairement inaccessible. Vous pouvez échouer au test nu et toujours avoir un site web accessible. Mais le test nu révèlera les zones où vous n'utilisez pas de balisage sémantique, et ces zones peuvent nécessiter une attention particulière pour l'accessibilité.

#### Que chercher pendant le test nu

Voici ce que je cherche lorsque je fais ce test.

Tout d'abord, je vérifie que la structure du site a du sens. Les choses sont-elles dans le bon ordre ? Chaque section a-t-elle un en-tête clair avec le bon niveau de balise d'en-tête ?

Ensuite, le contenu semble-t-il organisé ? Puis-je parcourir la page et avoir une idée du contenu comme si je parcourais un plan ?

Troisièmement, je regarde si les éléments interactifs semblent être interactifs. Si j'ai créé un tas d'éléments interactifs en utilisant des `<d`iv>, ils n'apparaîtront pas interactifs. Ensuite, je saurai que je dois passer un peu plus de temps à vérifier la fonctionnalité clavier de ces éléments pour l'accessibilité.

Et enfin, je veux m'assurer que les champs de saisie ont des étiquettes claires.

Cela résume à peu près le test nu. Pour réitérer, le but du test est de révéler les faiblesses dans la sémantique de votre site et de pointer les zones où vous devrez passer un peu plus de temps à tester pour vous assurer que ces composants sont accessibles.

### Principe 4 : Parlez à votre ordinateur

Voici mon quatrième et dernier principe maison : Parlez à votre ordinateur.

D'accord, peut-être ne parlez pas réellement à voix haute à votre ordinateur. Ce que je veux dire ici, c'est **communiquer** avec votre ordinateur — donnez au navigateur un peu de contexte en utilisant les [attributs ARIA](https://www.w3.org/WAI/standards-guidelines/aria/).

#### Attributs ARIA

ARIA signifie Accessible Rich Internet Applications. Il existe des états, des rôles et des propriétés ARIA qui indiquent certaines choses au navigateur sur votre page web, si vous choisissez de les utiliser.

Je vous suggère de les utiliser là où c'est **approprié**. Ils ne seront pas visibles pour les utilisateurs, mais ils seront utilisés par le navigateur et les lecteurs d'écran pour fournir un peu de contexte supplémentaire aux utilisateurs en arrière-plan.

Voici quelques exemples :

#### `aria-label`

L'attribut `aria-label` peut être ajouté comme attribut d'un élément HTML pour indiquer à un lecteur d'écran ce qu'il est. Je les utilise beaucoup sur les liens, pour fournir un contexte supplémentaire aux utilisateurs de lecteurs d'écran sur l'endroit où le lien les mène.

#### `aria-labelledby`

Si vous souhaitez concaténer plusieurs nœuds de texte existants en un seul `aria-label`, vous devriez utiliser `aria-labelledby`. Cet attribut acceptera une ou plusieurs références d'ID aux nœuds de texte que vous souhaitez utiliser pour étiqueter la saisie. Voici un exemple :

```html
<p id="sample-id">Some Text</p>
<input aria-labelledby="sample-id another-id" value="" />
<p id="another-id">That defines this input.</p>
```

Un lecteur d'écran lira la saisie comme "Some text that defines this input".

Le truc cool à propos de cela est qu'il concatène le texte de tous les ID que vous passez. (`aria-label` n'a pas cette même fonctionnalité). Il y a quelques exemples de [pourquoi vous pourriez vouloir concaténer des étiquettes](https://www.w3.org/WAI/GL/wiki/Using_aria-labelledby_to_concatenate_a_label_from_several_text_nodes#Examples) sur le site w3.

#### `aria-expanded`

L'attribut `[aria-expanded](https://benrobertson.io/accessibility/javascript-accessibility#3-manage-aria-states)` indique si un élément est ouvert ou fermé. Vous pourriez utiliser cela sur un bouton hamburger qui contrôle votre navigation principale. Lorsque l'utilisateur du lecteur d'écran se concentre sur le bouton avec une valeur `aria-expanded` de false, le lecteur d'écran dira quelque chose comme "Menu principal, bouton replié" et ils sauront qu'ils peuvent ouvrir le menu.

#### `aria-describedby`

L'attribut `aria-describedby` pointe vers un élément qui décrit l'élément actuel. Si vous souhaitez ajouter un texte d'erreur à une saisie, vous pourriez utiliser cela.

Voici un exemple :

```html
<label for="example-input">Email</label> 
<input type="email" id="example-input" aria-describedby="email-error" /> 
<div id="email-error"> 
  <p>The email address is in an invalid format.</p> 
</div>
```

Dans cet exemple, lors de la soumission du formulaire, le texte "The email address is in an invalid format." est ajouté dynamiquement à la div. Lorsque la saisie est focalisée, ce message sera lu à voix haute aux lecteurs d'écran.

#### `aria-live`

`aria-live` permet à l'ordinateur de savoir qu'une zone de la page sera mise à jour plus tard. Cela est vraiment pratique avec les éléments AJAX. Il peut avoir une valeur de polite, assertive, ou off.

Avec ces attributs, vous donnez au navigateur un contexte supplémentaire afin qu'il puisse avoir une meilleure idée de la fonctionnalité qu'un certain élément peut avoir, et plus de contexte aux utilisateurs de lecteurs d'écran et d'autres technologies d'assistance.

### Résumé des principes

Cela conclut mes quatre principes simples.

Pour résumer :

Le principe 1 est que le design web est plus que du design graphique.

Le principe 2 est d'être aussi sémantique que possible.

Le principe 3 est que les sites web doivent bien paraître nus.

Le principe 4 est de parler à votre ordinateur, utilisez ARIA.

En respectant ces principes, vous pourrez éviter une bonne partie des erreurs commises en utilisant un code non sémantique, préoccupé uniquement par les apparences.

Et, si vous voulez voir comment commencer à mettre cela en pratique, je lance un cours gratuit par email : [_9 erreurs courantes d'accessibilité des sites web et comment les corriger_](https://benrobertson.io/courses/common-accessibility-mistakes/). Obtenez l'accès au cours en vous inscrivant [ici](https://benrobertson.io/courses/common-accessibility-mistakes/) !

[**Erreurs courantes d'accessibilité et comment les éviter**](https://benrobertson.io/courses/common-accessibility-mistakes/)  
[_Une introduction gratuite à l'accessibilité web pour les développeurs web. Cliquez ici pour vous inscrire !_benrobertson.io](https://benrobertson.io/courses/common-accessibility-mistakes/)

_Publié à l'origine sur [benrobertson.io](https://benrobertson.io/accessibility/principles-getting-started-website-accessibility)._