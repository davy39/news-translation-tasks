---
title: Créer un site web portfolio avec HTML, CSS et JavaScript
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-03-17T14:49:23.000Z'
originalURL: https://freecodecamp.org/news/create-a-portfolio-website-using-html-css-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/portfoliojs.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: youtube
  slug: youtube
seo_title: Créer un site web portfolio avec HTML, CSS et JavaScript
seo_desc: If you are looking for a web developer job it can be helpful to have a portfolio
  website. It can also be helpful to have projects you've created to show to potential
  employers. You can accomplish both tasks at once by creating your own portfolio
  webs...
---

Si vous recherchez un emploi de développeur web, il peut être utile d'avoir un site web portfolio. Il est également utile d'avoir des projets que vous avez créés à montrer à des employeurs potentiels. Vous pouvez accomplir ces deux tâches à la fois en créant votre propre site web portfolio avec HTML, CSS et JavaScript.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous aidera à améliorer vos compétences en développement frontend en vous apprenant à construire un site web portfolio.

MacLinz a développé ce cours. C'est un développeur frontend expérimenté qui a créé de nombreux excellents cours sur sa chaîne YouTube.

Dans ce cours, vous apprendrez à construire un site web portfolio responsive avec un design moderne et des effets JavaScript sympas. Vous pourrez utiliser ce que vous apprendrez dans ce cours et personnaliser votre site portfolio pour mettre en valeur votre historique professionnel et vos compétences en design.

C'est un excellent projet pour les débutants qui souhaitent améliorer leurs compétences en HTML, CSS et JavaScript.

Le cours comprend les sections suivantes :

* Introduction
* Passer d'une section à l'autre
* Contenu de l'en-tête
* Section À propos
* Section Portfolios
* Section Blogs
* Section Contact
* Media Queries

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/xV7S8BhIeBo) (durée : 3 heures).

%[https://youtu.be/xV7S8BhIeBo]

### Transcription

(générée automatiquement)

Dans ce cours, vous allez améliorer vos compétences en HTML, CSS et JavaScript en construisant un site web portfolio.

Bonjour à tous. Dans la vidéo d'aujourd'hui, nous allons construire un site web portfolio en utilisant HTML, CSS et JavaScript.

Voici donc la page d'accueil principale du portfolio. Nous avons de jolis effets de survol sur les boutons et les images. Nous pouvons également basculer entre le thème clair et le thème sombre.

La section suivante sera la section "À propos", nous y aurons des informations avec également de beaux effets. Nous aurons des statistiques ici avec des barres de progression, ainsi qu'une chronologie.

Le rendu est également très bien avec le thème clair.

Ensuite, la section suivante sera la section portfolio avec un effet de survol. L'un de ces boutons peut nous mener vers n'importe quel travail que vous souhaitez lier. Par exemple, si vous voulez lier vers GitHub, vous cliquez et cela va sur GitHub, ou YouTube, peu importe.

La section suivante sera la section blog. Nous avons également un bel effet de survol sur les images des articles de blog. Et enfin, nous avons la section contact où vous pouvez mettre vos informations de contact.

Tout ce que vous voulez, c'est à vous de décider.

Ce site web est également responsive, il supportera plusieurs écrans, vous pouvez même le rendre encore plus responsive si vous le souhaitez.

Lorsque je diminue la largeur, il va vérifier les contrôles ici et les placer en bas. Vous pouvez basculer entre les pages avec les contrôles en bas au lieu qu'ils soient sur le côté droit.

Comme vous pouvez le voir, tout va répondre agréablement aux différentes tailles d'écran.

La section "À propos" et le portfolio seront également parfaitement responsives.

Je vous montrerai tout pour le rendre encore plus responsive, vous aurez les connaissances nécessaires pour faire la différence.

Voilà, je pense que c'est tout pour cette démonstration rapide. On se retrouve dans la vidéo.

J'ai un dossier d'images ici. Il n'y a pas beaucoup d'images. Ce sont les images que nous allons utiliser pour ce projet. Je vais commencer par créer un nouveau fichier HTML, `index.html`, puis je vais créer un nouveau dossier.

Celui-ci servira à stocker tous nos styles. À l'intérieur du dossier styles, je vais créer un nouveau style. L'extension que nous allons utiliser pour celui-ci est `.scss`. C'est le préprocesseur Sass.

C'est beaucoup plus rapide pour faire des styles que le CSS normal. Pour pouvoir utiliser Sass, vous devez aller dans les extensions, chercher SAS, puis l'installer. Il y a aussi un compilateur en direct (Live Compiler), donc nous n'avons pas besoin de redémarrer à chaque mise à jour du code. Nous pouvons simplement compiler le code en direct.

Vous pourriez aussi vouloir télécharger des snippets HTML CSS pour un futur support HTML/CSS, installez simplement ces deux-là.

C'est tout pour le moment, nous devons aller dans les styles et faire une réinitialisation de base de la page.

```scss
* {
    margin: 0; // marge à zéro
    padding: 0; // remplissage à zéro
    box-sizing: border-box;
    list-style: none;
}

body {
    background-color: red; // juste pour vérifier si nos styles fonctionnent
}
```

Nous devons compiler ce fichier Sass dans le dossier styles. Ici, vous verrez un bouton "Watch Sass", cliquez dessus. Cela va générer un fichier `style.css` ici.

Allons dans l'index et générons le boilerplate HTML. Pour ce faire, maintenez Shift et 1, puis appuyez sur Entrée.

Je vais nommer cela "Portfolio".

Maintenant, je vais lier le fichier `style.css`.

```html
<link rel="stylesheet" href="styles/style.css">
```

Je vais lancer cela avec Live Server. Vous pouvez aller dans les extensions et chercher l'extension Live Server.

Voilà, cela signifie que nos styles fonctionnent. Je vais supprimer la couleur de fond rouge. Je vais d'abord récupérer des polices sur Google Fonts. Je vais prendre la police appelée "Poppins".

Vous devez sélectionner plusieurs graisses de police (font weights). Nous utiliserons 400, 500, jusqu'à 800. Une fois cela fait, copiez le lien, allez dans l'index sous les styles et collez-le. Je vais aussi copier le nom de la famille de polices et le mettre dans le body.

Maintenant que nous avons fait les polices, nous allons pouvoir basculer entre le mode sombre et le mode clair. Pour ce faire, nous allons utiliser des variables CSS. Pour faire des variables, nous tapons `:root` et nous mettons des variables à l'intérieur.

Les variables concerneront principalement les couleurs. La première sera `color-primary`. Ce sera une couleur sombre.

```scss
:root {
    --color-primary: #191d2b;
    --color-secondary: #27ae60;
    --color-white: #FFFFFF;
    --color-black: #000;
    --color-grey0: #f8f8f8;
    --color-grey-1: #dbe1e8;
    --color-grey-2: #b2becd;
    --color-grey-3: #6c7983;
    --color-grey-4: #454e56;
    --color-grey-5: #2a2e35;
    --color-grey-6: #12181b;
    --br-sm-2: 14px;
    --box-shadow-1: 0 3px 15px rgba(0,0,0,.3);
}
```

Pour le body, je vais lui donner une couleur de fond en utilisant la variable.

```scss
body {
    background-color: var(--color-primary);
    font-family: 'Poppins', sans-serif;
    font-size: 1.1rem;
    color: var(--color-white);
    transition: all .4s ease-in-out;
}
```

Dans l'index, je vais donner au body la classe `main-content`. À l'intérieur, nous aurons un `header` avec la classe `section`, `sec1` et `header`. Il aura aussi une classe `active`.

Ensuite, dans le `main`, nous aurons plusieurs sections :

```html
<main>
    <section class="section sec2 about" id="about"></section>
    <section class="section sec3 portfolio" id="portfolio"></section>
    <section class="section sec4 blogs" id="blogs"></section>
    <section class="section sec5 contact" id="contact"></section>
</main>
```

Travaillons sur la fonctionnalité pour basculer entre les sections en utilisant JavaScript. Je vais vous présenter Font Awesome pour les icônes. Cherchez le CDN Font Awesome, copiez le lien et collez-le dans votre HTML.

Pour créer l'effet de basculement, nous devons cacher les autres sections et n'afficher que celle sur laquelle nous avons cliqué. Chaque section aura une position `absolute`.

```scss
.section {
    transform: translateY(-100%) scale(0);
    transition: all .4s ease-in-out;
    background-color: var(--color-primary);
}

.active {
    display: block;
    animation: scaleAnim 1s ease-in-out;
    @keyframes scaleAnim {
        0% { transform: translateY(-100%) scaleY(0); }
        100% { transform: translateY(0) scaleY(1); }
    }
}
```

Dans notre fichier `app.js`, nous sélectionnons les éléments :

```javascript
const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelector('.main-content');

function PageTransitions() {
    // Bouton clic classe active
    for(let i = 0; i < sectBtn.length; i++) {
        sectBtn[i].addEventListener('click', function() {
            let currentBtn = document.querySelectorAll('.active-btn');
            currentBtn[0].className = currentBtn[0].className.replace('active-btn', '');
            this.className += ' active-btn';
        })
    }

    // Sections classe active
    allSections.addEventListener('click', (e) => {
        const id = e.target.dataset.id;
        if(id) {
            // supprimer la sélection des autres boutons
            sectBtns.forEach((btn) => {
                btn.classList.remove('active')
            })
            e.target.classList.add('active')

            // cacher les autres sections
            sections.forEach((section) => {
                section.classList.remove('active')
            })

            const element = document.getElementById(id);
            element.classList.add('active');
        }
    })
}

PageTransitions();
```

Passons au contenu de l'en-tête. Nous aurons un côté gauche avec l'image et un côté droit avec le texte.

```html
<div class="header-content">
    <div class="left-header">
        <div class="h-shape"></div>
        <div class="image">
            <img src="img/hero.png" alt="">
        </div>
    </div>
    <div class="right-header">
        <h1 class="name">
            Salut, je suis <span>MacLinz.</span>
            Un développeur Web.
        </h1>
        <p>
            Je suis un développeur frontend passionné par la création de sites web magnifiques et fonctionnels.
        </p>
        <div class="btn-con">
            <a href="" class="main-btn">
                <span class="btn-text">Télécharger CV</span>
                <span class="btn-icon"><i class="fas fa-download"></i></span>
            </a>
        </div>
    </div>
</div>
```

Pour la section "À propos", nous utilisons une grille pour afficher nos statistiques et notre expérience. Nous réutilisons le composant bouton.

La section portfolio utilise également une grille (`display: grid`) avec trois colonnes. Chaque élément de portfolio a un effet de survol qui affiche les liens vers le code source ou la démo.

```scss
.portfolio-item {
    position: relative;
    .hover-items {
        width: 100%;
        height: 100%;
        background-color: var(--color-secondary);
        position: absolute;
        left: 0;
        top: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        opacity: 0;
        transform: scale(0);
        transition: all .4s ease-in-out;
    }
}

.portfolio-item:hover .hover-items {
    opacity: 1;
    transform: scale(1);
}
```

Enfin, pour les Media Queries, nous créons un fichier `_media.scss`. Nous déplaçons les contrôles en bas de l'écran pour les appareils mobiles.

```scss
@media screen and (max-width: 600px) {
    .header-content {
        grid-template-columns: 1fr;
        padding-bottom: 6rem;
    }
    .left-header .h-shape {
        display: none;
    }
    .right-header {
        grid-row: 1;
        width: 90%;
        margin: 0 auto;
    }
    .controls {
        top: auto;
        bottom: 0;
        flex-direction: row;
        justify-content: center;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        background-color: var(--color-grey-5);
        .control {
            margin: 1rem .3rem;
        }
    }
}
```

C'est ainsi que nous rendons le site responsive. Vous pouvez ajouter autant de points de rupture (breakpoints) que nécessaire pour affiner le design sur tablette et mobile.

Merci d'avoir suivi ce cours. N'oubliez pas de liker et de vous abonner si vous êtes nouveau. À la prochaine !