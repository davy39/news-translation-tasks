---
title: Comment créer un formulaire de connexion et d'inscription à double curseur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:30:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-double-slider-sign-in-and-sign-up-form-6a5d03612a34
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6-JxbwsPgUN6VvBZ.gif
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer un formulaire de connexion et d'inscription à double curseur
seo_desc: 'By Florin Pop

  Some of you might already know but for those who don’t, I’m starting a Weekly Coding
  Challenge with all of you! ?

  This challenge is meant to help improve our coding skills by practicing on real-life
  projects.

  You can read more about thi...'
---

Par Florin Pop

Certains d'entre vous le savent peut-être déjà, mais pour ceux qui ne le savent pas, je commence un Défi de Codage Hebdomadaire avec vous tous ! ?

Ce défi est destiné à améliorer nos compétences en codage en pratiquant sur des projets réels.

Vous pouvez en savoir plus sur ce défi et comment vous pouvez y participer en lisant [Le Guide Complet](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/).

Très bien... le **défi** de cette semaine était donc : **Créer un formulaire de connexion ou d'inscription (ou les deux).**

Ci-dessous, vous pouvez voir une démonstration de ce que j'ai créé :

![Image](https://cdn-media-1.freecodecamp.org/images/0*6-JxbwsPgUN6VvBZ.gif)

À vrai dire, j'ai eu un peu de mal à créer l'animation ?, mais au final, j'ai réussi à la faire fonctionner. ? Je me suis inspiré de ce design sur [Dribbble](https://dribbble.com/shots/5311359-Diprella-Login) par [SELECTO](https://dribbble.com/selecto) — ils ont des designs géniaux, vous devriez les vérifier !

### Description du projet

Avant de passer au code proprement dit, je voudrais décomposer les éléments que nous allons avoir dans le composant. Cela aidera à rendre le code que nous écrivons beaucoup plus clair.

Nous avons 4 écrans/boîtes plus petits à l'intérieur du composant principal (le `.container`) :

1. Le formulaire de **Connexion**
2. Le formulaire d'_Inscription_
3. Le calque de **Connexion**
4. Le calque d'_Inscription_

De plus, à un moment donné, vous pouvez voir soit :

* Le formulaire de **Connexion** avec le calque d'_Inscription_
* Le formulaire d'_Inscription_ avec le calque de **Connexion**

Dans les panneaux de _calque_, nous avons du texte et un `bouton`. En cliquant dessus, vous ferez apparaître l'autre combinaison d'écrans et vice-versa. Regardez à nouveau le GIF ci-dessus pour voir ce que je veux dire.

### L'animation du calque — expliquée

C'est là que cela peut être un peu plus compliqué, mais je vais faire de mon mieux pour expliquer afin que vous puissiez comprendre la logique derrière cela.

Nous avons les _couches_ suivantes pour le composant de calque :

**Le conteneur de calque** — celui-ci affichera la zone **visible** (plus d'informations ci-dessous) à un certain moment. Il a une `largeur` de `50 %` de la largeur totale du conteneur.

**Le calque** — ce div a une taille de `largeur` double (`200 %`) afin qu'il prenne toute la largeur du conteneur principal. (`200 % * 50 % = 100 %`. Les 50 % proviennent du `.overlay-container` ci-dessus).

**Les panneaux de calque** — ce sont les divs qui contiennent le contenu réel (le texte et le bouton) que nous voyons à l'écran. Ils ont tous deux une `position` de `absolute`. Nous pouvons les positionner où nous voulons dans le composant `.overlay`. L'un des panneaux est positionné à `gauche` et l'autre est positionné à `droite`. Tous deux ayant une largeur de `50 %` du composant `.overlay`.

« Pourquoi avons-nous besoin de 3 couches ? » pourriez-vous demander... Eh bien, voyons à quoi cela ressemblerait sans la première couche :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xbuYkIKyX8a5IlhY.png)

Sur l'image ci-dessus, vous pouvez voir que les deux panneaux sont « visibles », ce qui n'est pas ce que nous voulons. C'est pourquoi nous ajoutons le `.overlay-container` pour agir comme une « zone de focus ». Cela nous permet de masquer le panneau qui est en **débordement**, ou qui est hors de ses limites. C'est pourquoi nous avions besoin que le `.overlay` soit deux fois plus grand que le `.overlay-container`. En déplaçant le `.overlay-container`, qui a également une `position` de `absolute`, nous pouvons masquer ou afficher le panneau que nous voulons.

C'était un peu confus ?, je l'admets, mais j'espère avoir éclairci les choses.

### L'animation des formulaires — expliquée

Celles-ci ne sont pas difficiles à comprendre du tout. En gros, nous avons à nouveau deux conteneurs — les `.form-container`. Chacun a une `largeur` de `50 %` et une `position` - `absolute`. Nous déplaçons les deux en même temps de gauche à droite. Lorsqu'ils passent derrière le `.overlay-container` ci-dessus (tout en se déplaçant), nous changeons rapidement la valeur de `z-index`. Le formulaire **Inscription** (par exemple) passera au-dessus du formulaire **Connexion**, et vice-versa. Magique pour les yeux, mais avec une logique de code derrière ! ?

### Le HTML

Maintenant que nous avons décomposé le cœur de la « fonctionnalité » de l'animation, il est temps de voir le code HTML réel. Commençons par le squelette de base :

```html
<div class="container" id="container">
    <div class="form-container sign-up-container">
        <!-- Le code du formulaire d'inscription va ici -->
    </div>
    <div class="form-container sign-in-container">
        <!-- Le code du formulaire de connexion va ici -->
    </div>
    <div class="overlay-container">
        <!-- Le code du calque va ici -->
    </div>
</div>
```

La div principale a une classe `.container` et aussi un id `container` car nous voulons cibler cet élément en JavaScript (plus d'informations ci-dessous). ?

#### **Le formulaire d'inscription**

```html
<div class="form-container sign-up-container">
    <form action="#">
        <h1>Créer un compte</h1>
        <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
        </div>
        <span>ou utilisez votre email pour vous inscrire</span>
        <input type="text" placeholder="Nom" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Mot de passe" />
        <button>S'inscrire</button>
    </form>
</div>
```

#### **Le formulaire de connexion**

Nous avons également quelques classes sur chaque div :

```html
<div class="form-container sign-in-container">
    <form action="#">
        <h1>Se connecter</h1>
        <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
        </div>
        <span>ou utilisez votre compte</span>
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Mot de passe" />
        <a href="#">Mot de passe oublié ?</a>
        <button>Se connecter</button>
    </form>
</div>
```

* La classe `.form-container` contiendra le CSS qui est dupliqué pour les classes `.sign-in-container` et `.sign-up-container` ;
* les 2 classes différentes (mentionnées ci-dessus) contiendront le CSS qui est différent.

De cette manière, nous évitons d'avoir à écrire le même code CSS deux fois et nous utilisons la puissance de pouvoir ajouter plusieurs classes.

Vous avez peut-être également remarqué que les balises `i` ont quelques classes. C'est parce que nous utilisons [FontAwesome](http://fontawesome.io/) pour les icônes. Lisez plus d'informations à leur sujet sur leur site web.

#### **Le conteneur de calque**

```html
<div class="overlay-container">
    <div class="overlay">
        <div class="overlay-panel overlay-left">
            <h1>Content de vous revoir !</h1>
            <p>
                Pour rester connecté avec nous, veuillez vous connecter avec vos informations personnelles
            </p>
            <button class="ghost" id="signIn">Se connecter</button>
        </div>
        <div class="overlay-panel overlay-right">
            <h1>Bonjour, ami !</h1>
            <p>Entrez vos détails personnels et commencez votre voyage avec nous</p>
            <button class="ghost" id="signUp">S'inscrire</button>
        </div>
    </div>
</div>
```

Comme ci-dessus, nous avons une classe commune `.overlay-panel` et deux classes différentes : `.overlay-left` et `.overlay-right`. De plus, nous avons des `id` pour les boutons car nous allons ajouter un écouteur d'événement **onClick** pour les deux dans le `JavaScript`.

### Le JavaScript

Habituellement, nous couvrons le CSS avant la partie JS, mais cette fois il est plus facile de montrer et d'expliquer le code JavaScript en premier. Cela vous aidera à comprendre le CSS que nous allons avoir par la suite.

```js
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});
```

Comme expliqué ci-dessus, nous ajoutons les écouteurs d'événements. Lorsque les boutons sont cliqués, nous `ajoutons` ou `retirons` la classe `.right-panel-active` (pas le meilleur nom pour la classe, mais c'est le meilleur que j'ai trouvé pour le moment ?). Cette classe sera utilisée pour styliser les sous-composants différemment car nous avons deux écrans.

### Le CSS

Tout d'abord, nous avons le CSS de base pour les composants de base :

```css
h1 {
    font-weight: bold;
    margin: 0;
}

p {
    font-size: 14px;
    font-weight: 100;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 20px 0 30px;
}

span {
    font-size: 12px;
}

a {
    color: #333;
    font-size: 14px;
    text-decoration: none;
    margin: 15px 0;
}

button {
    border-radius: 20px;
    border: 1px solid #ff4b2b;
    background-color: #ff4b2b;
    color: #ffffff;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
}

button:active {
    transform: scale(0.95);
}

button:focus {
    outline: none;
}

button.ghost {
    background-color: transparent;
    border-color: #ffffff;
}

form {
    background-color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 50px;
    height: 100%;
    text-align: center;
}

input {
    background-color: #eee;
    border: none;
    padding: 12px 15px;
    margin: 8px 0;
    width: 100%;
}

.social-container {
    margin: 20px 0;
}

.social-container a {
    border: 1px solid #dddddd;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 0 5px;
    height: 40px;
    width: 40px;
}
```

Quelques points à noter ici :

1. Nous stylisons les éléments directement (h1, p, a). Habituellement, vous ne feriez pas cela car cela pourrait se mélanger avec d'autres styles, il est donc bon d'ajouter une classe à chacun d'eux. Mais pour cet exemple, cela fonctionne bien car nous n'avons que ces éléments sur la page.
2. Nous avons une petite `transition` sur le `button`. Lorsqu'il est cliqué, l'état _active_ est déclenché, nous le rendons donc un peu plus petit. Un bel effet de clic simple ?!
3. Le `form` est un conteneur `flex` car nous voulons centrer tout ce qui s'y trouve, et c'est facile à faire avec `flexbox`. Vous verrez ci-dessous qu'il est utilisé quelques fois de plus.

Le CSS du `.container` :

```css
.container {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
}
```

* Position `relative` car nous aurons des éléments enfants positionnés en `absolute` (expliqué pourquoi, ci-dessus).
* Le `overflow` est défini sur `hidden` car nous avons défini un `border-radius` et nous ne voulons pas que les éléments enfants brisent ce rayon et soient affichés à l'extérieur du `.container`.

Maintenant, la partie amusante, le `.form-container` et les styles associés :

```css
.form-container {
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

.sign-in-container {
    left: 0;
    width: 50%;
    z-index: 2;
}

.sign-up-container {
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
}

.container.right-panel-active .sign-in-container {
    transform: translateX(100%);
}

.container.right-panel-active .sign-up-container {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: show 0.6s;
}

@keyframes show {
    0%,
    49.99% {
        opacity: 0;
        z-index: 1;
    }

    50%,
    100% {
        opacity: 1;
        z-index: 5;
    }
}
```

**Notez** ce qui suit :

1. L'`animation` (`show`) qui est responsable du changement de `z-index` des `.form-container` comme discuté ci-dessus. Nous passons en ayant le z-index **1** de `0-49.99 %` et en l'ayant à **5** de `50-100 %`. Ces plages sont utilisées car nous voulons qu'elles changent rapidement.
2. Nous utilisons la classe `.right-panel-active` pour déplacer les `.form-container` lorsque les boutons sont cliqués.

Et enfin, le `.overlay-container` et les styles associés :

```css
.overlay-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform 0.6s ease-in-out;
    z-index: 100;
}

.container.right-panel-active .overlay-container {
    transform: translateX(-100%);
}

.overlay {
    background: #ff416c;
    background: -webkit-linear-gradient(to right, #ff4b2b, #ff416c);
    background: linear-gradient(to right, #ff4b2b, #ff416c);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0 0;
    color: #ffffff;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    transform: translateX(0);
    transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
    transform: translateX(50%);
}

.overlay-panel {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    text-align: center;
    top: 0;
    height: 100%;
    width: 50%;
    transform: translateX(0);
    transition: transform 0.6s ease-in-out;
}

.overlay-left {
    transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
    transform: translateX(0);
}

.overlay-right {
    right: 0;
    transform: translateX(0);
}

.container.right-panel-active .overlay-right {
    transform: translateX(20%);
}
```

* le `.overlay` a un fond dégradé, j'ai utilisé [UI Gradients](https://uigradients.com/) pour l'obtenir ;
* `.overlay-left` et `.container.right-panel-active .overlay-right` ont une translation de `-20 %` et `20 %` sur l'axe X. C'est parce que je voulais ajouter un petit effet au texte lorsqu'il est affiché, comme s'il venait de l'extérieur (en quelque sorte) ?;

Autre que cela... Rien ! Nous avons tout couvert. Nous avons terminé ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*sv0wmyb-gqD-Tp27.gif)

### Conclusion

Cet article était un peu difficile sur les animations, n'est-ce pas ? ? Néanmoins, j'espère que vous en avez appris quelque chose.

N'oubliez pas que vous pouvez également participer au [Défi de Codage Hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) en créant votre propre version du **formulaire de Connexion/Inscription**. Partagez-le avec moi sur Twitter : [@florinpop1705](https://twitter.com/@florinpop1705) pour que je puisse le voir !

De plus, vous pouvez suggérer ce que nous devrions construire pour le prochain Défi dans [ce formulaire Google](https://docs.google.com/forms/d/1oxBbwgMrPCcybKaR90AXxMeITv4kg2f2AelOAVHTqgo).

Vous pouvez trouver la version live du projet que nous avons construit sur [Codepen](https://codepen.io/FlorinPop17/full/vPKWjd).

Merci d'avoir pris le temps de lire ceci ?, j'espère que vous avez appris quelque chose de nouveau !

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/03/double-slider-sign-in-up-form/).