---
title: Comment CSS Grid change la façon dont nous pensons à structurer notre contenu
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-27T15:56:00.000Z'
originalURL: https://freecodecamp.org/news/css-grid-changes-how-we-can-think-about-structuring-our-content
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/marmoset-1567019547013.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: grid layout
  slug: grid-layout
- name: HTML
  slug: html
seo_title: Comment CSS Grid change la façon dont nous pensons à structurer notre contenu
seo_desc: 'By Kevin Powell

  CSS Grid changes how we can think about document structures

  Anyone who has even dabbled a little in creating websites knows that <div>s are
  an essential building block for controlling our layouts.

  HTML5 introduced new semantic element...'
---

Par Kevin Powell

# CSS Grid change la façon dont nous pouvons penser aux structures de documents

Toute personne ayant même un peu expérimenté la création de sites web sait que les `<div>` sont des éléments de construction essentiels pour contrôler nos mises en page.

HTML5 a introduit de nouveaux éléments sémantiques pour aider, et bien qu'ils soient un excellent ajout au langage, ils sont un peu comme la garniture de notre soupe de `<div>`.

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566407449963_div-soup.jpg)

Avec grid, nous n'avons plus besoin de nous appuyer sur des `<div>` pour créer la structure de notre page, ou même un composant plus complexe. La structure est littéralement définie par le parent et non par la façon dont le contenu est organisé à l'intérieur.

Cela signifie que nous pouvons avoir une balisage simple et propre qui se concentre sur le contenu lui-même sans dépendre de l'organisation via l'utilisation de `<div>`.

## Grid peut être compliqué, mais flexbox aussi

J'ai entendu beaucoup de gens se plaindre que grid est trop compliqué et que flexbox fait le travail. **Je soutiendrais qu'ils sont à l'aise avec flexbox et ne veulent pas se donner la peine d'apprendre grid à cause de cela**.

À la fin de la journée, Grid introduit une tonne de nouvelles propriétés et valeurs, donc oui, il y a une courbe d'apprentissage. Mais flexbox est également assez compliqué.

Pouvez-vous me dire les avantages de flex-basis par rapport à la définition d'une largeur ? Ou vraiment, comment flexbox calcule les largeurs des éléments flexibles si nous ne les avons pas explicitement définies ?

Par exemple, si vous montriez l'exemple ci-dessous à quelqu'un qui n'a jamais utilisé flexbox, comment expliquez-vous le fait que c'est le même balisage et le même CSS pour les deux ensembles de colonnes ? Pour aggraver les choses, la deuxième colonne dans les deux cas a une largeur de 50 %. Clairement, cette largeur de 50 % n'est pas vraiment définie à 50 %.

%[https://codepen.io/kevinpowell/pen/WNeRbjg]

"Eh bien, cela commence par les éléments flexibles qui se rétrécissent s'il n'y a pas assez de place, donc même si nous avons défini la largeur à 50 %, il n'a pas l'espace, donc il se rétrécit pour s'adapter parce que l'autre div nécessite plus d'espace. Le 50 % est plus une taille idéale que ce qu'il sera réellement.

"Donc dans l'exemple du haut, le contenu de la première div étant si long pose un problème parce que, en tant qu'élément flexible, par défaut, il veut se rétrécir pour s'adapter à son contenu. Dans ce cas, cet élément a beaucoup de contenu donc...

**Donc oui, flexbox est génial et fait un excellent travail pour créer des mises en page, mais ne me dites pas que c'est simple**. Dès que vous sortez des exemples parfaits, c'est souvent loin d'être intuitif et parfois cela peut être carrément étrange.

Grid est compliqué en ce sens qu'il y a _beaucoup_ de nouvelles propriétés et valeurs, mais elles nous donnent beaucoup plus de contrôle que flexbox.

Dans cet article, j'aimerais examiner comment cette couche supplémentaire de contrôle aide à simplifier notre balisage et nous permet d'écrire moins de code, et cela sans même apprendre à utiliser un tas de ses fonctionnalités sophistiquées.

## Les limitations de flexbox

Même si nous prenons un composant simple et le construisons avec flexbox, parce qu'il n'agit qu'en 1 dimension à la fois (les éléments flexibles sont soit des lignes soit des colonnes, ils ne peuvent pas être les deux), nous sommes laissés avec beaucoup de divs pour diviser les choses en lignes, qui peuvent ensuite être divisées en colonnes.

Par exemple, si nous travaillons sur une carte qui ressemble à ceci :

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566998781330_Screen+Shot+2019-08-28+at+9.26.01+AM.png)

Ce n'est pas une mise en page compliquée, mais nous devons toujours organiser notre contenu de manière assez spécifique pour que cela fonctionne.

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566999564535_flex-overlay.jpg)

Les boîtes jaune et orange sont nécessaires, afin que lorsque nous plaçons un display: flex; sur le .card lui-même (la boîte rouge), il créera deux colonnes. Donc pour structurer tout, nous obtenons un balisage qui ressemble à ceci :

```html
<div class="card">
    <div class="profile-sidebar">
        <!-- image de profil et liste sociale ici -->
    </div>
    <div class="profile-body">
        <!-- nom, position, description ici -->
    </div>
</div>
```

Ce n'est pas excessivement compliqué de quelque manière que ce soit, et une fois que vous comprenez comment fonctionne flexbox, c'est relativement simple.

Lorsque nous mettons un `display: flex` sur le `.card`, nous obtenons nos deux colonnes, et ensuite nous devons entrer dans celles-ci et commencer à les styliser.

Voici un exemple fonctionnel avec tout le style :

%[https://codepen.io/kevinpowell/pen/rNBjaqV]

Le problème est que **en ayant à créer des colonnes de contenu, nous compliquons un peu plus le balisage, et nous nous limitons également** car nous avons forcé différentes parties du contenu à être regroupées.

## Simplifier tout avec CSS Grid

Parce que grid est bidimensionnel, ce qui signifie qu'il nous permet de créer des lignes _et_ des colonnes en même temps, cela signifie que notre conteneur de grid (où nous déclarons display: grid) a un contrôle total sur la mise en page à l'intérieur.

Nous avions l'habitude de _nécessiter_ des <div> pour faire cela, comme dans l'exemple ci-dessus avec flexbox. Avec grid, nous pouvons supprimer les <div> complètement.

```html
<div class="card">
  <img src="https://i.pravatar.cc/125?image=3" alt="" class="profile-img">
  <ul class="social-list"> ... </ul>
  <h2 class="profile-name">Ramsey Harper</h2>
  <p class="profile-position">Graphic Designer</p>
  <p class="profile-info">Lorem ipsum ...</p>
</div>
```

D'un point de vue balisage, cela n'a-t-il pas plus de sens ?

Nous avons un `.card` et ensuite nous plaçons le contenu de ce composant là. Nous n'avons pas besoin de nous soucier de la façon dont il sera structuré, nous plaçons simplement le contenu dont nous avons besoin et passons à autre chose.

### Structurer la mise en page

Tout comme lorsque nous avons utilisé flexbox pour cela, nous devons toujours décomposer la mise en page, bien que, grâce au fonctionnement de grid, cela semble un peu différent.

C'est l'un des endroits où les gens pourraient soutenir que grid est plus compliqué, mais en réalité, je dessine simplement des boîtes autour de chaque morceau de contenu, puis j'étend ces lignes.

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566999543180_grid-overlay.jpg)

Avec flexbox, nous avons créé deux divs qui agiraient comme nos colonnes. Lorsque nous utilisons grid, nous configurons plutôt toute la grid sur le parent lui-même, puis nous pouvons indiquer aux enfants où ils appartiennent sur cette grid.

Pour configurer la grid, nous pouvons faire quelque chose comme ceci :

```css
.card {
    display: grid;
    grid-template-columns: 1fr 3fr;
}
```

L'unité `fr` est unique à grid, et représente une fraction de l'espace disponible. L'utiliser de cette manière est très similaire à la configuration des deux colonnes dans flexbox et à leur donner des largeurs de `25%` et `75%` respectivement.

### Placer les éléments sur la grid

Peut-être est-ce parce que j'ai utilisé les floats pour créer des mises en page pendant des années, mais cela semble toujours un peu magique lorsque les différents éléments se retrouvent là où nous voulons qu'ils soient !

Nous pourrions utiliser `grid-row` et `grid-column` sur chaque élément pour le placer où nous voulons, mais plus j'utilise grid, plus je tombe amoureux de la prise de temps pour configurer `grid-template-areas` et placer mes éléments dans ces zones.

La configuration est un peu plus longue, mais le retour sur investissement est vraiment évident lorsque nous rendons les choses responsives (nous y viendrons bientôt).

Donc, d'abord, sur le `.card`, nous devons configurer les `grid-template-areas`, puis nous pouvons assigner tous les enfants à ces zones :

```css
.card {
  ...
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-column-gap: 2em;
  grid-template-areas:
      "image name"
      "image position"
      "social description";
}


.profile-name     { grid-area: name; }
.profile-position { grid-area: position; }
.profile-info     { grid-area: description; }
.profile-img      { grid-area: image; }
.social-list      { grid-area: social; }
```

Jetez un coup d'œil ici si vous souhaitez voir tout cela en action :

%[https://codepen.io/kevinpowell/pen/wvwdVyJ]

## C'est si simple

L'une des choses que j'aime dans l'utilisation de `grid-template-areas` est qu'il est _si_ facile pour quelqu'un d'autre de regarder ce code et de comprendre immédiatement ce qui se passe.

Si quelqu'un vous montre quelque chose qui a été configuré en utilisant `grid-row` et `grid-column` avec des nombres et des spans, il est assez facile de compter les choses et de comprendre où elles vont se retrouver. Pour des mises en page simples ou pour un span 3 rapide ici et là, je pense qu'il est acceptable de les utiliser, **mais c'est si agréable de regarder _uniquement_ le CSS d'un élément parent et de comprendre immédiatement à quoi va ressembler toute cette mise en page**.

### Il est plus facile de connaître la taille réelle d'un élément lorsque l'on utilise grid

Dans cet exemple tout premier où nous avons défini la largeur de l'un des éléments flexibles à 50 %, ce n'était pas vraiment 50 %. Si vous comprenez pourquoi c'est le cas, c'est bien, mais cela peut encore être ennuyeux parfois. Il est assez facile de contourner cela, mais lorsque l'on utilise grid, c'est _beaucoup_ moins un problème.

Parce que nous définissons la mise en page complète, nous définissons également exactement combien d'espace nous voulons que les éléments occupent.

Et bien sûr, nous avons `minmax()` et `fr` qui brouillent un peu les pistes car ils permettent un dimensionnement plus flexible (comme nous l'utilisons dans notre exemple ci-dessus), mais même alors, nous avons toujours un contrôle total sur cette flexibilité, et tout est contrôlé par le parent plutôt que de devoir définir certaines choses sur le parent et d'autres sur les enfants.

## Changements limités

En regardant notre exemple ci-dessus, nous ne pouvons pas changer cette mise en page pour qu'elle ressemble à ceci sans changer le balisage :

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1567000172227_Screen+Shot+2019-08-28+at+9.49.09+AM.png)

Nous nous sommes contraints en raison de la manière dont nous avons dû regrouper les choses dans des `<div>`. Nous avons dû utiliser ces `<div>` afin de faire fonctionner la mise en page, mais nous sommes maintenant bloqués.

**Avec le balisage plat de notre grid, tout est possible** ! Et en bonus, parce que nous avons tout configuré en utilisant grid-template-areas, faire ces changements est super facile !

```css
.card {
  /* ancienne mise en page
  grid-template-areas:
      "image name"
      "image position"
      "social description"; */

  /* mise en page mise à jour */
  grid-template-areas:
      "image name"
      "image position"
      "image social"
      ". description";
}
```

En jouant avec les `grid-template-areas` comme ceci, cela déplace les icônes sociales là où nous voulons qu'elles soient si rapidement et facilement (le `.` dans la dernière partie indique une cellule vide).

## Cela rend la vie si facile lorsque l'on traite avec les media queries

Comme je l'ai mentionné plusieurs fois maintenant, l'un des endroits où cela porte ses fruits. Nous pouvons contrôler complètement notre mise en page avec notre parent :

```css
.card {
  /* configuration pour les petits écrans */
  display: grid;
  grid-template-columns: 1fr;
  grid-column-gap: 2em;
  grid-template-areas:
      "name"
      "image"
      "social"
      "position"
      "description";
}
.profile-name     {  grid-area: name;}
.profile-position {  grid-area: position; }
.profile-info     {  grid-area: description; }
.profile-img      {  grid-area: image; }
.social-list      {  grid-area: social; }


/* réorganisation de la mise en page pour les grands écrans */

@media (min-width: 600px) {
  .card {
    text-align: left;
    grid-template-columns: 1fr 3fr;
    grid-template-areas:
        "image name"
        "image position"
        "social description";
  }
  .profile-name::after {
    margin-left: 0;
  }
}
```

Le stylo ci-dessous a tout le style. Plongez-vous dedans, jouez avec les grid-areas, et voyez à quel point il est facile de changer complètement la mise en page !

%[https://codepen.io/kevinpowell/pen/BaBRXvZ]

## Flexbox a encore sa place

Je me tourne de plus en plus vers grid, mais je pense que flexbox a encore sa place. Si j'ai un logo et une navigation côte à côte, il est agréable de faire simplement quelque chose comme ceci et de savoir qu'ils sont là où je veux qu'ils soient :
`.header {  display: flex;  justify-content: space-between;}`

De même pour le `<ul>` que nous utilisons pour une navigation pour simplement obtenir les éléments côte à côte, ou comme vous l'avez peut-être remarqué dans l'exemple de carte que nous regardions, il est parfait pour le `.social-list`.

Pour les composants simples où nous n'avons pas besoin d'une mise en page plus complexe, cela fonctionne très bien. Mais je me tourne de plus en plus vers grid, parfois parce que j'en ai vraiment besoin, d'autres fois parce que je veux utiliser `minmax()` ou utiliser des unités `fr`.

Mais à la fin de la journée, je pense que le meilleur aspect de grid est la façon dont nous pouvons simplifier notre balisage.

Nous devons encore utiliser le modeste `<div>`, mais grâce à grid, nous n'avons plus à nous appuyer sur le remplissage de notre balisage avec eux.

## Conclusion

Aussi génial que soit flexbox, il n'est pas plus simple que grid. Il fait certaines choses vraiment bien, mais grid nous permet, lorsque nous travaillons sur des mises en page plus complexes, d'avoir beaucoup plus de contrôle. Ce contrôle est amplifié lorsque nous traitons avec le design responsif lors de la réalisation de changements dans les media queries.

Avec flexbox, notre grand changement est de modifier la flex-direction. Avec grid, nous pouvons complètement redessiner un composant rapidement et facilement.

Il y a beaucoup plus à dire sur flexbox et grid. Chacun a son but, mais si vous avez l'impression de ne pas savoir lequel choisir, ou si vous avez du mal à comprendre le design responsif en général, j'ai récemment publié un cours qui plonge dans le design responsif sur Scrimba appelé **[The Responsive Web Design Bootcamp](https://scrimba.com/g/gresponsive)**.

Il inclut une plongée en profondeur dans Grid et Flexbox, ainsi qu'un module complet dédié à la façon de commencer à penser de manière responsive. Au total, il compte plus de 170 leçons, avec 15+ heures de contenu, organisées en 6 modules. Donc, si vous souhaitez continuer à plonger dans le monde responsive de CSS, vous pouvez [le découvrir ici](https://scrimba.com/g/gresponsive).