---
title: Comment créer de superbes contrôles de formulaire HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-05T17:43:37.000Z'
originalURL: https://freecodecamp.org/news/perfect-html-input
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/HTML-Blog-Cover.png
tags:
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: Comment créer de superbes contrôles de formulaire HTML
seo_desc: 'By Austin Gil

  Today I''m going to show you all the things to consider when building the perfect
  HTML input. Despite its seemingly simple nature, there''s actually a lot that goes
  into it.

  How to Make the Control

  Well, we need to start somewhere. Might ...'
---

Par Austin Gil

Aujourd'hui, je vais vous montrer tout ce qu'il faut considérer lors de la création d'une entrée HTML parfaite. Malgré son apparence simple, il y a en réalité beaucoup de choses à prendre en compte.

## Comment créer le contrôle

Eh bien, il faut bien commencer quelque part. Autant commencer par le contrôle lui-même.

HTML offre trois différents contrôles de formulaire parmi lesquels choisir : `[<input>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input)`, `[<textarea>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)`, et `[<select>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)`. Aujourd'hui, nous utiliserons `<input>`, mais les mêmes règles s'appliqueront aux autres.

```html
<input />
```

## Comment faire fonctionner `<input>`

Les entrées sont généralement utilisées pour capturer les données de l'utilisateur. Pour ce faire, elles doivent être placées dans un élément `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)`, mais ce n'est pas tout à fait suffisant. Lorsque le formulaire est soumis, il ne saura pas comment étiqueter les données de l'entrée.

Pour qu'un formulaire inclue les données d'une entrée lors de la soumission du formulaire, l'entrée a besoin d'un attribut `[name](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name)`. Vous n'avez pas besoin de gestion d'état ou de liaison de données. Juste un `name`.

```html
<input name="data" />
```

## Comment rendre l'entrée accessible

Maintenant que nous avons rendu les robots heureux, il est temps de se concentrer sur les humains.

Chaque entrée a également besoin d'une étiquette, à la fois pour la clarté et pour l'accessibilité. Il y a plusieurs options :

* Ajouter un élément `[<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)` avec un attribut `[for](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label#attr-for)` et l'assigner à l'`[id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)` de l'entrée (étiquette explicite).
* Envelopper l'entrée avec un élément `<label>` (étiquette implicite).
* Ajouter un attribut `[aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)` à l'entrée.
* Ajouter un attribut `[aria-labelledby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-labelledby)` à l'entrée et l'assigner à l'`id` d'un autre élément.

Parmi toutes ces options, la plus fiable est une étiquette explicite car elle fonctionne sur la plupart des navigateurs, des technologies d'assistance et des interfaces de contrôle vocal. Les étiquettes implicites ne fonctionnent pas dans Dragon Speech Recognition. Les attributs ARIA sont capricieux.

Les attributs `[placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#placeholder)` et `[title](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title)` ne sont pas des étiquettes appropriées.

Je recommande de ne pas envelopper tout dans une balise `<label>` car :

1. Cela peut inclure plus de contenu que ce qui serait considéré comme l'étiquette. Cela entraîne une mauvaise expérience pour les utilisateurs de lecteurs d'écran.
2. Il est courant d'ajouter des styles à l'élément enveloppant de l'entrée. Ces styles peuvent entrer en conflit avec le comportement par défaut d'une `<label>`.

En général, je préfère utiliser une `[<div>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)` pour isoler le contrôle.

```html
<div>
    <label for="input-id">Étiquette</label>
    <input id="input-id" name="data" />
</div>
```

Si vous voulez un jour une entrée qui ne montre pas l'étiquette, ne retirez pas l'étiquette du HTML. Au lieu de cela, cachez-la avec CSS ou utilisez une option moins fiable. Gardez l'étiquette dans le balisage et cachez-la visuellement avec une `class` avec ces styles. Ces styles la gardent accessible aux technologies d'assistance, tout en la supprimant visuellement :

```css
.visually-hidden {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  width: 1px;
  height: 1px;
  margin: -1px;
  border: 0;
  padding: 0;
}
```

Notez qu'il est généralement conseillé d'inclure une étiquette visible pour éviter toute confusion. Un `placeholder` ne doit pas servir d'étiquette.

## Comment choisir un type (ou non)

En plus des différentes balises listées ci-dessus, vous pouvez changer le comportement du contrôle en définissant un attribut `[type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types)` d'entrée. Par exemple, si vous souhaitez accepter l'email d'un utilisateur, vous pouvez définir l'attribut `type` sur "email".

Les types d'entrée peuvent changer le comportement ou l'apparence de l'UI. Voici quelques exemples :

* Le type "[number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number)" change le comportement en empêchant les entrées de valeurs non numériques.
* Le type "[color](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color)" change l'UI en ajoutant un bouton qui ouvre un sélecteur de couleur.
* Le type "[date](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date)" améliore l'expérience de saisie des données en offrant un sélecteur de date.
* Le type "[email](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email)" applique une validation de contrainte intégrée lors de la soumission du formulaire.

Cependant, certains types d'entrée peuvent être des [faux amis](https://en.wikipedia.org/wiki/False_friend).

Considérez une entrée qui demande un code postal américain. Seules les entrées numériques sont valides, donc il pourrait être judicieux d'utiliser un type "number". Cependant, un problème avec l'entrée "number" est qu'elle ajoute une fonctionnalité d'événement de défilement telle qu'un utilisateur peut faire défiler vers le haut sur l'entrée pour incrémenter la valeur ou vers le bas pour la décrémenter.

Pour une entrée de code postal, il est possible qu'un utilisateur clique sur l'entrée, entre son code postal, puis essaie de faire défiler la page vers le bas. Cela décrémenterait la valeur qu'il a entrée, et il est très facile pour l'utilisateur de manquer ce changement. En conséquence, le nombre qu'il a entré pourrait être incorrect.

Dans ce cas, il peut être préférable d'éviter complètement l'attribut `type` et d'utiliser un `[pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#pattern)` tel que `[0-9]*` si vous souhaitez limiter l'entrée aux seules valeurs numériques. En fait, le type "number" est [souvent plus problématique qu'il n'en vaut la peine](https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/).

## Soyez descriptif

Puisque nous avons brièvement abordé la validation des contraintes, c'est un bon moment pour mentionner les descriptions.

Bien qu'HTML dispose d'attributs de validation intégrés et qu'il existe plusieurs bibliothèques de validation JavaScript plus robustes, il existe une autre approche efficace pour amener les utilisateurs à remplir des données correctes qui peut être moins ennuyeuse.

Dites-leur exactement ce que vous voulez.

Certains contrôles de formulaire comme "nom" ou "email" peuvent être évidents, mais pour ceux qui ne le sont pas, fournissez une description claire de ce dont vous avez besoin.

Par exemple, si vous demandez aux utilisateurs de créer un nouveau mot de passe, dites-leur quelles sont les exigences **avant** qu'ils n'essaient de soumettre le formulaire. Et n'oubliez pas les utilisateurs de technologies d'assistance.

Nous pouvons associer une entrée à une description par proximité visuelle ainsi qu'en utilisant l'attribut `[aria-describedby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby)`.

```html
<div>
    <label for="password">Mot de passe</label>
    <input id="password" name="password" type="password" aria-describedby="password-requirements" />
    <p id="password-requirements">Veuillez créer un nouveau mot de passe. Doit contenir au moins 8 caractères, une lettre majuscule, une lettre minuscule et un caractère spécial.</p>
</div>
```

Les descriptions sont également un endroit efficace pour mettre tout message de retour de validation.

## Soyez flexible

Lors de la création d'entrées, il est souvent tentant d'ajouter des contraintes pour les valeurs acceptables afin de s'assurer que l'utilisateur n'envoie que de bonnes données. Mais être trop strict peut conduire à une mauvaise expérience utilisateur.

Par exemple, si vous demandez à l'utilisateur d'entrer un numéro de téléphone, considérez qu'il existe plusieurs formats acceptables différents :

* 8008675309
* 800 867 5309
* 800-867-5309
* 800.867.5309
* (800) 867-5309
* +1 (800) 867-5309
* 001 800 867 5309

Tous les exemples ci-dessus représentent le même numéro de téléphone. Idéalement, un utilisateur devrait pouvoir entrer l'un de ces formats et toujours pouvoir soumettre le formulaire sans problème.

Si vous voulez que votre entrée n'envoie que des caractères numériques, il est possible de permettre à l'utilisateur de taper dans le format qu'il souhaite. Ensuite, vous pouvez utiliser JavaScript pour ajouter un gestionnaire d'événements à l'événement `blur`, et supprimer tous les caractères indésirables (espace, trait d'union, point, etc.) de la valeur de l'entrée. Cela ne laisserait que les nombres.

## Rendez-le facile

Si vous avez déjà rempli un formulaire en utilisant un appareil mobile, vous avez peut-être remarqué que le clavier de votre téléphone semble différent sur différentes entrées.

Pour une entrée de texte de base, vous voyez le clavier standard, pour les entrées d'email vous pouvez voir le symbole @ plus commodément placé, et pour les entrées numériques vous pouvez voir le clavier remplacé par un pavé numérique.

Dans de nombreux cas, le navigateur choisira un clavier plus approprié à afficher aux utilisateurs si le `type` d'entrée est défini. Mais comme nous l'avons vu ci-dessus, il est souvent préférable d'utiliser une simple entrée de texte.

Nous pouvons toujours offrir une meilleure expérience utilisateur aux utilisateurs mobiles en demandant au navigateur d'afficher des claviers spécifiques malgré l'absence d'un attribut `type` dans l'entrée. Nous pouvons y parvenir avec l'attribut `[inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#inputmode)` qui accepte huit options différentes.

* text (valeur par défaut)
* none
* decimal
* numeric
* tel
* search
* email
* url

Vous voulez essayer ? Rendez-vous sur [inputmodes.com](https://inputmodes.com/) sur votre appareil mobile. C'est assez cool.

## Continuez à apprendre

Cela fait plus de mille mots que j'avais à dire sur la création de contrôles de formulaire. J'espère que vous l'avez trouvé utile.

Si vous souhaitez continuer à apprendre, j'ai écrit une série en cinq parties sur la façon de créer de meilleurs formulaires HTML :

* [Partie 1 : Sémantique](https://austingil.com/how-to-build-html-forms-right-semantics/)
* [Partie 2 : Accessibilité](https://austingil.com/how-to-build-html-forms-right-accessibility/)
* [Partie 3 : Styles personnalisés](https://austingil.com/build-html-forms-right-styling/)
* [Partie 4 : Expérience utilisateur](https://austingil.com/build-html-forms-right-user-experience/)
* [Partie 5 : Sécurité](https://austingil.com/how-to-build-html-forms-right-security/)

Si vous avez aimé cet article, veuillez le [partager](https://twitter.com/share?via=heyAustinGil). C'est l'une des meilleures façons de me soutenir. Vous pouvez également [vous inscrire à ma newsletter](https://austingil.com/newsletter/) ou [me suivre sur Twitter](https://twitter.com/heyAustinGil) si vous voulez savoir quand de nouveaux articles sont publiés.