---
title: Comment préparer votre futur vous-même pour le succès avec de bonnes habitudes
  de codage
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-16T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/set-future-you-up-for-success-with-good-coding-habits
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/set-up-for-success.jpg
tags:
- name: Self-awareness
  slug: self-awareness
- name: 100Days100Projects
  slug: 100days100projects
- name: clean code
  slug: clean-code
- name: code
  slug: code
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: fundamentals
  slug: fundamentals
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: Self Development
  slug: self-development
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment préparer votre futur vous-même pour le succès avec de bonnes habitudes
  de codage
seo_desc: 'Think before you code. You have the power to make your future self''s life
  Heaven on Earth or a living hell.

  In this article we''ll explore what kinds of things you can do to make it a little
  easier on your future self.

  Revisiting "prior art"

  We''ve all...'
---

Réfléchissez avant de coder. Vous avez le pouvoir de rendre la vie de votre futur vous-même un paradis sur terre ou un enfer.

Dans cet article, nous explorerons les types de choses que vous pouvez faire pour faciliter un peu la vie de votre futur vous-même.

## Revisiter l'« art antérieur »

Nous y avons tous été. Six mois après le début d'un projet, vous essayez d'écraser un bug, et ce que vous trouvez est choquant. Vous pourriez vous demander, « qui écrirait ce genre de code ? »

Alors vous fouillez dans l'historique des commits git en utilisant `git log -p filename.js` montrant les changements pour un fichier spécifique, essayant de voir qui aurait pu inventer quelque chose comme ça. Et puis votre cœur s'arrête – c'est vous qui l'avez écrit !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/tituss-burgess-shocked.gif)
_Tituss Burgess choqué_

C'est un scénario courant pour tout développeur, expérimenté ou novice. Si vous n'avez pas encore rencontré ce scénario, je vous promets que si vous continuez à coder suffisamment longtemps, vous le rencontrerez.

## Devenir plus conscient de nos habitudes de codage

Ce point de réflexion à six mois est inévitable. C'est beaucoup de temps que vous avez probablement utilisé pour travailler sur d'autres parties du projet ou sur un autre projet complètement. Il est probable que vous ayez monté de niveau, ce qui a changé la façon dont vous écrivez du code.

D'un autre côté, il arrive parfois que l'on doive sortir du code pour voir le tableau d'ensemble et avoir une meilleure vue d'ensemble de la façon dont toutes les pièces s'emboîtent. Nous pouvons naturellement nous enfoncer trop profondément dans une solution et devenir un peu trop concentrés sur la résolution de ces défis.

Mais dans tous les cas, bien que faire partie du voyage du code consistera simplement à gagner plus d'expérience et à en apprendre davantage sur votre métier, il existe d'autres petites habitudes que vous pouvez adopter dès le début et qui vous aideront sur le long terme.

Alors plongeons-nous dans le sujet.

## Améliorer la lisibilité de votre code

### Quel est le défi ?

Faire partie de notre métier est amusant car il existe une tonne de façons de faire la même chose. Vous pensez qu'une instruction `if` est trop longue ? Eh bien, nous pouvons l'écrire en style [ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) !

```js
// Exemple d'instruction ternaire
const isFreezing = temperature <= 32 ? true : false;

```

Mais parfois, cela nuit à la lisibilité de votre code. Bien que cela puisse sembler joli et super propre sur une ligne, imaginez que lorsque cette ternaire devient plus complexe, quelqu'un devra passer plus de temps à comprendre ce qu'elle signifie.

```js
const minutes = 30;
const cookie = {
  color: 'black'
};

const cookieStatus = minutes > 20 ? cookie.color === 'black' ? 'burned' : 'done' : 'not done';

```

### Que pouvons-nous faire de mieux ?

Maintenant, je suppose que la plupart d'entre nous peuvent comprendre ce qu'est `cookieStatus` dans cet exemple (spoiler : `burned`). Mais pensez au temps que vous avez passé à le comprendre. Qu'il s'agisse d'une seconde ou deux de plus, cela vous force à dépenser une énergie cognitive supplémentaire pour lire le code.

D'un autre côté :

```js
const minutes = 30;
const cookie = {
  color: 'black'
};
let cookieStatus;

if ( minutes <= 20 ) {
  cookieStatus = 'not done';
} else if ( cookie.color === 'black' ) {
  cookieStatus = 'burned';
} else {
  cookieStatus = 'done';
}

```

Non, ce n'est peut-être pas aussi propre ou astucieux que l'instruction ternaire en une ligne, mais la prochaine fois que vous la visiterez, vous aurez moins à réfléchir sur la réponse. 

Cela rendra également plus facile pour les bugs de se glisser et de passer inaperçus auprès de vos relecteurs de code lorsque toutes vos modifications de code sont dans une ligne de diff git.

Et oui, c'est un exemple simple. Mais imaginez cela dans un scénario réel avec une logique métier importante où vous pourriez rencontrer ces situations fréquemment.  

Supposons que vous deviez ajouter une autre condition – cette ternaire ne fera que devenir de plus en plus complexe ! Vous ne faites que rendre le débogage ou l'extension plus difficiles, alors que les instructions `if` peuvent continuer de manière facilement lisible.

Pour ce qu'elles valent, les ternaires et autres raccourcis peuvent être simples et efficaces dans le code, mais n'abusez pas de cette efficacité et ne finissez pas par rendre les choses plus difficiles.

## Garder les choses cohérentes

### Quel est le défi ?

Nous avons tous notre façon préférée de coder. Bien que je soutienne que ne pas inclure de point-virgule à la fin de votre JavaScript est tout simplement faux, vous pourriez préférer écrire votre code de la mauvaise manière sans eux.

```jsx
// Style de code de Jim

function MyComponent() {
  function handleOnClick() {
    alert('Click!')
  }
  return (
    <button onClick={handleOnClick}>My Button</button>
  )
}

// Style de code de Creed

const MyComponent = () => <button onClick={() => alert('Click!')}>My Button</button>;
```

Mais ce n'est pas toujours une question de ce que _vous_ préférez. Lorsque vous travaillez avec une équipe, il est probable que l'opinion de chacun sur la façon dont le code devrait être écrit soit légèrement différente. Vous pourriez être d'accord sur le point-virgule, mais en désaccord sur les espaces.

Et personne n'a tort (sauf ceux qui n'utilisent pas de point-virgule) ! Il existe des arguments valables pour la plupart des styles de code, qu'ils soient pour ou contre, mais la solution n'est pas que chacun écrive son code à sa manière.

### Que pouvons-nous faire de mieux ?

Garder le code cohérent est important pour maintenir la santé du code. Un objectif typique est de « faire en sorte que la base de code semble avoir été écrite par une seule personne ».

Le but n'est pas qu'une seule personne impose sa manière, mais que l'équipe soit parvenue à une conclusion sur un ensemble de règles qu'ils utiliseraient et que tout le monde suivrait. Avoir cette cohérence réduit la charge cognitive des personnes travaillant sur le code. Cela donne à chacun la capacité de savoir à quoi s'attendre lors de la lecture du code.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/linting-code.jpg)
_Erreurs de linting de code_

Et atteindre cet objectif n'a pas besoin d'être difficile. Il existe des outils qui peuvent simplement [vérifier ces incohérences](https://www.colbyfayock.com/2019/10/what-is-linting-and-how-can-it-save-you-time) comme [Eslint](https://eslint.org/) pour JavaScript. Et encore mieux, il existe un autre niveau d'outils comme [Prettier](https://prettier.io/) qui [le corrigeront pour vous](https://www.colbyfayock.com/2019/11/dont-just-lint-your-code-fix-it-with-prettier) !

## Commenter votre code

### Quel est le défi ?

Maintenir les commentaires de votre code est un moyen important de mettre en contexte une logique complexe. Autant nous voulons tous que notre code soit auto-documenté, ce n'est rarement le cas.

Trop souvent, nous nous retrouvons à traiter un bloc de code qui n'a tout simplement pas de sens. Et même s'il a du sens en soi, nous pourrions ne pas être en mesure de comprendre comment il s'intègre dans le reste de l'application.

### Que pouvons-nous faire de mieux ?

En fournissant un bon ensemble de commentaires, vous préparez la prochaine personne qui touchera ce code à avoir une meilleure compréhension de ce que fait le code avant qu'elle ne le modifie.

```js
// NE PAS CHANGER - CELA ARRÊTERA DE FAIRE DE L'ARGENT

const shouldMakeMoney = true;

function makeMoney() {
  if ( shouldMakeMoney ) {
    return noMoney;
  }
  return moreMoney;
}

```

Bien que ce soit un exemple idiot, il soulève un cas réel. Les entreprises dépendent de plus en plus de la capacité à maintenir un site web fiable pour gagner de l'argent. Qu'il s'agisse d'une entreprise de commerce électronique ou d'un géant de la publicité, ces sites web reposent sur une logique métier qui détermine des choses comme les coûts, les taxes, les remises et d'autres éléments mathématiques que nous avons tendance à ne pas vouloir penser, mais qui peuvent faire ou défaire une entreprise sur internet.

Mais ce n'est pas seulement une question de l'entreprise pour laquelle vous travaillez. Toucher un ancien code peut être effrayant. C'est encore plus effrayant lorsque personne dans votre équipe n'était présent lorsqu'il a été écrit, donc personne ne sait ce qu'il fait !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/patton-oswalt-hands-over-mouth.gif)
_Patton Oswalt se couvre la bouche_

Bien que vous ne soyez peut-être pas la prochaine personne à toucher ce code, essayez d'aider votre futur ami qui s'attaque au prochain ticket impliquant ce code. Car il y a aussi de bonnes chances que vous soyez cette personne et vous souhaiterez vous souvenir de son fonctionnement.

## Documenter vos solutions

### Quel est le défi ?

La documentation est similaire au commentaire de votre code, mais sous un angle différent. La documentation et les commentaires consistent tous deux à trouver des moyens de décrire une solution de manière lisible par l'homme, ce qui donnera finalement plus de contexte. Mais la documentation concerne davantage la solution globale plutôt que les détails d'implémentation.

Avoir une application performante est l'objectif de tous. Mais comment y sommes-nous arrivés ? Il y a une chance réaliste que quelqu'un doive travailler sur le même projet que vous, comme l'intégration d'un nouveau membre de l'équipe. Comment pourront-ils maintenir cette haute performance s'ils ne savent pas comment cela fonctionne ?

### Que pouvons-nous faire de mieux ?

Qu'il s'agisse de présenter ce nouveau membre de l'équipe au projet ou d'essayer de partager des connaissances avec une autre équipe de projet, la documentation est une partie importante de la maintenance d'un projet. Elle aide à garder tout le monde sur la même page afin que nous sachions tous en toute confiance ce vers quoi nous travaillons.

Par exemple, si nous travaillons toujours sur notre projet de commerce électronique avec notre logique métier, il y aura des règles que le code devra implémenter. Bien que les commentaires puissent donner des détails en ligne sur la manière dont les règles ont été implémentées, la documentation définirait ces règles.

```js
/**
 * DOCUMENTATION
 * Total de la commande >= 25 : Remise de 10%
 * Total de la commande >= 50 : Remise de 15%
 * Total de la commande >= 100 : Remise de 20%
 * Total de la commande >= 75 : Livraison gratuite
 */

const orderSubTotal = 84.00;
let orderTotal = orderSubTotal;

// Si le total de la commande est inférieur à 75, appliquer la remise sur les frais de port

if ( orderTotal < 75 ) {
  orderTotal = addShipping(orderTotal);
}

// Si le total de la commande atteint un seuil, appliquer la remise donnée

if ( orderTotal >= 100) {
  orderTotal = applyDiscount(orderTotal, .2);
} else if ( orderTotal >= 50 ) {
  orderTotal = applyDiscount(orderTotal, .15);
} else if ( orderTotal >= 25 ) {
  orderTotal = applyDiscount(orderTotal, .1);
}

```

C'est un exemple minimal, mais nous pouvons voir la différence entre les règles en haut et comment nous les appliquons. La documentation devrait expliquer clairement quelles sont les règles, mais elle ne devrait pas se soucier de la manière dont ces règles ont été implémentées.

D'un autre côté, les commentaires pourraient ne pas se soucier des règles, mais doivent les implémenter de manière efficace et logique. Nous devrions être en mesure de mettre à jour le code avec les règles métier, comme changer le niveau de remise de haut niveau de 100 $ à 80 $, sans avoir à retravailler le code.

Mais la documentation est bien plus que des règles métier – c'est fournir un moyen pour quiconque de comprendre votre travail à un niveau supérieur. Cela pourrait inclure tout, des diagrammes architecturaux à la théorie derrière votre algorithme principal.

Bien que peut-être le code ne soit pas le meilleur endroit pour que des détails comme celui-ci vivent, c'est une information vraiment importante qui peut aider à inspirer confiance dans votre projet et donner aux autres une opportunité de comprendre davantage le travail.

## Créer des Pull Requests efficaces

### Quel est le défi ?

Les pull requests (ou merge requests) sont une partie centrale du cycle de vie de tout projet d'équipe de développement. Ils fournissent un moyen d'emballer et de présenter votre code de manière consommable pour que vos pairs puissent le réviser et comprendre votre travail.

Il y a beaucoup de choses qui peuvent entrer dans une pull request, d'un seul commit à l'intégralité de la prochaine version de votre site web. C'est beaucoup de contexte à attendre de quelqu'un pour comprendre en lisant simplement les commits.

### Que pouvons-nous faire de mieux ?

Les pull requests n'ont pas besoin d'être un art. Il devrait y avoir un objectif principal dans la préparation que vous y mettez – fournir du contexte à vos changements. Au minimum, cela devrait répondre aux questions « quoi » et « pourquoi ».

Nous pouvons même utiliser des outils comme des modèles de pull request pour nous orienter dans la bonne direction. [Définissez un plan](https://www.freecodecamp.org/news/why-you-should-write-merge-requests-like-youre-posting-to-instagram-765e32a3ec9c/) de ce que vous voulez expliquer et il y a des chances que les gens suivent ce plan. Cela aide à éviter la description en une ligne « ferme [ticket] » ou pire, une description vide.

Avec mes projets, j'espère avoir quelques questions répondue avant de plonger dans une revue de code :

* Quel est le changement ?
* Qu'est-ce que cela impacte ?
* Comment reproduire ou tester le changement ?

Quelques détails autour de l'ensemble de changements peuvent fournir un contexte très nécessaire pour ceux qui révisent votre code. Il est facile de regarder le code, mais il est plus difficile de le comprendre sans savoir comment il s'intègre dans le tableau d'ensemble.

## Renforcer votre code avec des tests

### Quel est le défi ?

Les tests sont un moyen de s'assurer que votre code s'exécute de la même manière à chaque fois. Pouvoir prouver que la même entrée aura toujours la même sortie aidera à vous donner, à vous et à votre équipe, un niveau de confiance plus élevé que votre application ne s'écroulera pas avec le prochain petit changement.

Sans eux, nous sommes laissés avec l'erreur humaine, où peu importe à quel point votre ingénieur QA est bon (mention spéciale à mes testeurs), quelque chose passera toujours à travers les mailles du filet. Et ce n'est pas pour dire que vos tests attraperont toujours chaque problème, mais nous pouvons utiliser les outils disponibles pour aider à l'empêcher.

### Que pouvons-nous faire de mieux ?

Là où les commentaires sont un moyen de fournir le contexte de fonctionnement de quelque chose, les tests sont un moyen de s'assurer qu'ils fonctionnent. Fournir des cas de test qui sont reproductibles aide à renforcer cela.

```js
function applyDiscount(value, discount) {
  const discountAmount = value * discount;
  return value - discountAmount;
}

expect(applyDiscount(10, .1)).toEqual(.9);
expect(applyDiscount(532151235, .1054)).toEqual(476062494.831);

```

Si je falsifie les maths dans notre fonction `applyDiscount` ci-dessus, il y a une forte probabilité que le test échoue (ne dites jamais jamais).

Mais les tests n'ont pas besoin d'être difficiles. Il existe de nombreux outils qui aident sous différents angles. Par exemple, vous pourriez utiliser [Jest](https://jestjs.io/) pour exécuter vos tests unitaires ou ajouter [Enzyme](https://enzymejs.github.io/enzyme/) par-dessus pour tester vos composants React. Mais vous pouvez également intégrer [Cypress](https://www.cypress.io/) comme solution de test d'intégration qui fonctionnera comme un robot cliquant à travers votre application pour vous assurer que tous les composants fonctionnent réellement ensemble.

Il existe également différentes méthodologies de test. Bien que vous voyez probablement la plupart des équipes écrire leurs tests après avoir une solution fonctionnelle, certaines personnes jurent par le [développement piloté par les tests](https://en.wikipedia.org/wiki/Test-driven_development). Ils pourraient écrire leurs tests en premier où le code doit passer les tests plutôt que l'inverse. C'est un excellent moyen de définir les exigences du code avant de plonger directement.

Quelle que soit la méthode, capturez les points qui sont les plus susceptibles de se casser ou les fonctions qui ajoutent le plus de valeur métier. Vous aiderez à prévenir une perte potentielle pour l'entreprise ou même plus simplement, un mal de tête.

## Que pouvons-nous apprendre de cela ?

Cela peut être beaucoup à digérer, mais ce sont des points importants à considérer à mesure que vous grandissez en tant que développeur. Commencer ces habitudes tôt dans votre carrière vous aidera à construire naturellement ces compétences et à travailler de cette manière par défaut.

Et si vous êtes en fin de carrière, il n'est jamais trop tard pour commencer. Nous devrions tous vouloir nous efforcer d'être le meilleur développeur possible et faire de notre mieux pour faciliter la vie de nos coéquipiers, car nous sommes tous dans le même bateau.

## À la recherche de plus à apprendre ?

* [Posez le Javascript - Apprenez le HTML & CSS](https://www.colbyfayock.com/2019/08/put-down-the-javascript-learn-html-css)
* [Comment devenir un développeur web full stack en 2020](https://www.colbyfayock.com/2020/02/how-to-become-a-full-stack-web-developer-in-2020)
* [Qu'est-ce que le JAMstack et comment commencer ?](https://www.colbyfayock.com/2020/02/what-is-the-jamstack-and-how-do-i-get-started)
* [Qu'est-ce que le linting et comment peut-il vous faire gagner du temps ?](https://www.colbyfayock.com/2019/10/what-is-linting-and-how-can-it-save-you-time)
* [Pourquoi vous devriez écrire des merge requests comme si vous postiez sur Instagram](https://www.freecodecamp.org/news/why-you-should-write-merge-requests-like-youre-posting-to-instagram-765e32a3ec9c/)

## Quel est votre conseil pour grandir en tant que développeur ?

[Partagez avec moi sur Twitter !](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>