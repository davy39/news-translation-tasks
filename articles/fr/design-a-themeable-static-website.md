---
title: Comment créer un site web statique personnalisable
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-02-08T21:00:38.000Z'
originalURL: https://freecodecamp.org/news/design-a-themeable-static-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/20210207_172754_0000-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Static Site Generators
  slug: static-site-generators
- name: ux design
  slug: ux-design
- name: Web Design
  slug: web-design
seo_title: Comment créer un site web statique personnalisable
seo_desc: 'A while ago I wanted to create a dark theme for my personal site. So I
  did some clicking around to find out the most suitable and clean way to do this.

  I read Max Bock''s article on creating a custom theme, where he explained the process
  quite clearly...'
---

Il y a quelque temps, je voulais créer un thème sombre pour mon [site personnel](https://spruce.com.ng). J'ai donc fait quelques clics pour trouver la manière la plus adaptée et **propre** de procéder.

J'ai lu [l'article de Max Bock sur la création d'un thème personnalisé](https://mxb.dev/blog/color-theme-switcher), où il explique le processus de manière assez claire. Il est également allé très loin (avec DIX schémas de couleurs différents).

Mais pour mon cas, je voulais plus. Je voulais que les utilisateurs puissent changer le schéma de couleurs parmi les différentes options fournies.

Je voulais aussi qu'ils puissent changer la taille de la police. Cela est dû au fait que j'avais un en-tête fixe sur mon site, ce qui était plutôt bien, mais sur les petits appareils mobiles, il occupait beaucoup d'espace – pas idéal pour l'UX, n'est-ce pas ? J'ai donc également donné aux utilisateurs la possibilité de désactiver cet en-tête fixe.

![Aperçu du site web statique personnalisable spruce.com.ng avec thème sombre](https://www.freecodecamp.org/news/content/images/2021/02/spruce-theme.png align="left")

*Site statique personnalisable de Spruce.com.ng*

Vous pouvez trouver un aperçu en direct sur mon site personnel [spruce.com.ng](https://spruce.com.ng). Vous pouvez également copier le code source [ici](#quest-ce-que-vous-etes-une-personne-qui-naime-pas-les-tutoriels-vous-pouvez-copier-le-code-source-complet-ici) pour gagner du temps de lecture.

## Ce que je voulais faire

1. Demander aux utilisateurs leur schéma de couleurs préféré, la taille de la police et le type d'en-tête (fixe ou statique)

2. Collecter les choix des utilisateurs

3. Les sauvegarder dans localStorage

4. Les récupérer depuis localStorage et les afficher immédiatement à l'utilisateur lors du rechargement de la page, s'ils changent d'onglet et reviennent, et s'ils ferment leur navigateur et reviennent après une semaine ou un mois, jusqu'à ce qu'ils effacent le stockage de leur navigateur

## Comment j'ai créé le thème

Dans 11ty (le générateur de site statique que j'utilise), vous pouvez créer un fichier JSON dans le dossier `_data`. Vous pouvez accéder aux données globalement dans votre modèle (Jekyll le fait aussi). Il est probable que votre générateur de site statique préféré (SSG) puisse faire de même.

```json
fichier _data/themes.json

[
    {
        "id": "default",
        "colors": {
            "text": "#222126",
            "text-dark": "#777;",
            "border": "rgba(0,0,0,.1)",
            "primary": "#665df5",
            "secondary": "#6ad1e0",
            "primary-dark": "#382cf1",
            "bg": "#ffffff",
            "bg-alt": "#f8f8f8",
            "overlay": "rgba(255, 255, 255, .4)"
        }
                }, 
    ... autres schémas de couleurs
]
```

## Comment générer le CSS

Pour utiliser le fichier de données, créez un fichier appelé `theme.css.liquid` et donnez-lui un permalien où vous voulez que le fichier CSS soit généré.

```css
fichier css/theme.css.liquid
---
permalink: /css/theme.css
---
// quand aucun thème n'est sélectionné
// utiliser le thème par défaut
:root {
    --text: {{ themes[0].colors.text }};
    --text-dark: {{ themes[0].colors.text-dark }};
    --border: {{ themes[0].colors.border }};
    --primary: {{ themes[0].colors.primary }};
    --secondary: {{ themes[0].colors.secondary }};
    --primary-dark: {{ themes[0].colors.primary-dark }};
    --bg: {{ themes[0].colors.bg }};
    --bg-alt: {{ themes[0].colors.bg-alt }};
}  
// si le schéma de couleurs préféré de l'utilisateur est sombre
// utiliser le thème sombre

@media(prefers-color-scheme: dark) {
    :root {
    --text: {{ themes[1].colors.text }};
    --text-dark: {{ themes[1].colors.text-dark }};
    --border: {{ themes[1].colors.border }};
    --primary: {{ themes[1].colors.primary }};
    --secondary: {{ themes[1].colors.secondary }};
    --primary-dark: {{ themes[1].colors.primary-dark }};
    --bg: {{ themes[1].colors.bg }};
    --bg-alt: {{ themes[1].colors.bg-alt }};
    }
}
// générer le css du thème à partir du fichier de données
// ici nous utilisons une boucle for
// pour itérer sur tous les thèmes dans notre _data/themes.json
// et les sortir en tant que css brut


{% for theme in themes %}
 [data-theme="{{ theme.id }}"] {
    --text: {{ theme.colors.text }};
    --text-dark: {{ theme.colors.text-dark }};
    --border: {{ theme.colors.border }};
    --primary: {{ theme.colors.primary }};
    --secondary: {{ theme.colors.secondary }};
    --primary-dark: {{ theme.colors.primary-dark }};
    --bg: {{ theme.colors.bg }};
    --bg-alt: {{ theme.colors.bg-alt }};
 }
{% endfor %}
```

Remarquez que j'utilise **themes[0].colors.text** parce que mon thème par défaut est le premier de la liste. Il a un index de 0, donc mon thème sombre a également un index de 1.

Dans **Jekyll**, vous pouvez sortir du liquid dans CSS en ajoutant simplement un front matter vide en haut du fichier.

```css
fichier css/theme.css
---
---

// votre liquid dans css va ici
```

Je suis sûr que votre générateur de site statique préféré fournit un moyen similaire de sortir du liquid dans un fichier CSS. Vous pouvez également tout coder à la main si vous écrivez simplement du HTML et du CSS brut sans SSG.

## Comment utiliser le CSS dans votre site

Si vous lisez ceci, alors je suppose que vous savez déjà comment travailler avec les propriétés personnalisées CSS. Je ne vais donc pas entrer dans les détails ici.

```css
// les propriétés personnalisées CSS sont déclarées en utilisant le mot-clé **var**
// color: var(--text);
body {
    background: var(--bg);
    color: var(--text);
}
h1,h2 {
    color: var(--text-dark)
}
// j'avais également des propriétés de taille de police par défaut et de marge supérieure définies
// j'ai ajouté ceci à la racine dans css
:root {
    --font-size: 18px;
    --position: fixed;
    --top-margin: 96px;
}
```

Vous devez simplement changer chaque partie de couleur sur votre site en propriétés personnalisées que vous avez générées.

## Comment générer le HTML

Maintenant, fournissons une interface utilisateur pour permettre aux utilisateurs de changer la taille de la police, le type d'en-tête et le schéma de couleurs de notre site. Le mien est un peu simple, mais vous pouvez aller plus loin. Je n'explique que le concept ici.

```html
fichier theme.html
// créer les boutons de police
// J'ai donné à chaque bouton une valeur
// Je veux obtenir la valeur et la sauvegarder dans le stockage local 

<section class="theme-section">
    <div class="theme-btn-wrapper">
        <button class="btn btn--small btn--border js-font-btn" value="16">16px</button>
        <button class="btn btn--small btn--border js-font-btn" value="18">18px</button>
        <button class="btn btn--small btn--border js-font-btn" value="20">20px</button>
        <button class="btn btn--small btn--border js-font-btn" value="22">22px</button>
    </div>
</section>

// Créer le bouton bascule
// Pour activer et désactiver
// L'en-tête fixe
// Le **sr-only** est utilisé pour masquer le texte visuellement 
// tout en gardant l'accessibilité à l'esprit
// notez le **role="switch"** et aria-checked
// ce sont eux qui transforment le bouton en un interrupteur On et Off
<div class="check-wrapper">
    <span id="btn-label" class="sr-only">En-tête fixe ou statique</span>
   <button role="switch" type="button" aria-checked="true" aria-labelledby="btn-label" class="js-theme-toggle btn btn--border btn--rounded btn--toggle">
       <span>On</span>
       <span>Off</span>
   </button>
</div>
```

C'est à peu près tout le HTML pour mon cas d'utilisation. Encore une fois, vous pouvez faire plus si vous le souhaitez, et il y a un peu de style CSS impliqué (qui serait omis dans notre cas).

## La partie amusante : Comment créer le JavaScript

```js
fichier /assets/js/theme.js
class CustomTheme {
    constructor() {
        // partie A : vérifier si localStorage fonctionne
        this.islocalStorage = function() {
            try {
                localStorage.setItem("test", "testing");
                localStorage.removeItem("test");
                return true;
            } catch (error) {
                return false
            }
           
        };
        // partie B : Obtenir la valeur des boutons
        this.schemeBtns = document.querySelectorAll('.js-theme-color');
        this.schemeBtns.forEach((btn) => {
            const btnVal = btn.value;
            btn.addEventListener('click', () => this.themeScheme(btnVal))
        });

        this.fontBtns = document.querySelectorAll('.js-font-btn');
        this.fontBtns.forEach((btn) => {
            const btnVal = btn.value;
            const btnTag = btn;
            btn.addEventListener('click', () => this.themeFont(btnVal, btnTag))
        });

        // partie C : obtenir l'élément bouton html
        this.switchBtn = document.querySelector('.js-theme-toggle');
        const clicked = this.switchBtn;
        this.switchBtn.addEventListener('click', () => this.themePosition(clicked))
    }

    // partie D : Sauvegarder les données dans localStorage
    themeScheme(btnVal) {
        document.documentElement.setAttribute('data-theme', btnVal);
        if (this.islocalStorage) {
            localStorage.setItem('theme-name', btnVal);
        }
    };
    
    themeFont(btnVal,btnTag) {
        document.documentElement.style.setProperty('--font-size', `${btnVal}px`);
        if (this.islocalStorage) {
            localStorage.setItem('font-size', btnVal);
        }
        ;
        if (btnVal == localStorage.getItem('font-size')) {
            removeActive();
            btnTag.classList.add('active');
    }
};

    themePosition(clicked) {
    if (clicked.getAttribute('aria-checked') == 'true') {
        clicked.setAttribute('aria-checked', 'false');
        document.documentElement.style.setProperty('--position', 'static');
        document.documentElement.style.setProperty('--top-margin', '0px');
        if (this.islocalStorage) {
            localStorage.setItem('position', 'static');
        }

    } else {
        clicked.setAttribute('aria-checked', 'true');
        document.documentElement.style.setProperty('--position', 'fixed');
        document.documentElement.style.setProperty('--top-margin', '96px');
        if (this.islocalStorage) {
            localStorage.setItem('position', 'fixed');
        }
    }

    }
}

function removeActive() {
    const btns = document.querySelectorAll('.js-font-btn');
    btns.forEach((btn) => {
        btn.classList.remove('active');
    })
}

// partie E : N'utiliser notre classe que si les propriétés personnalisées CSS sont supportées
if (window.CSS && CSS.supports('color', 'var(--i-support')) {
    new CustomTheme()
};

// partie E : Ajouter une classe active au bouton de taille de police sélectionné

window.addEventListener('load', () => {
    const fontBtns = document.querySelectorAll('.js-font-btn');
    fontBtns.forEach((btn) => {
        const btnVal = btn.value;
        const btnTag = btn;
        if (btnVal == localStorage.getItem('font-size')) {
            btnTag.classList.add('active');
    }
    });   
})
```

Je sais que c'est un gros morceau de code JavaScript, mais il fait essentiellement quelques choses :

* il collecte et vérifie si localStorage est supporté

* puis il sauvegarde les données dans localStorage

Remarquez également que j'ai utilisé des **Classes JavaScript**, mais vous pourriez utiliser des fonctions aussi.

### Vérification du stockage local

De nombreux navigateurs supportent localStorage de nos jours, mais pourquoi devons-nous encore vérifier ?

Certains utilisateurs peuvent naviguer sur votre site en **mode incognito (mode de navigation privée)**. Et parfois localStorage est désactivé par défaut, donc il ne sauvegarde rien sur l'appareil de l'utilisateur.

Au lieu de le sauvegarder directement et d'obtenir parfois une erreur sur les navigateurs qui ne le supportent pas, nous pouvons vérifier si le navigateur le supporte. Si c'est le cas, c'est super – et si ce n'est pas le cas, nous sommes aussi cool.

Maintenant, si vous remarquez, tout semble fonctionner parfaitement. Mais si vous changez le thème ou la taille de la police et que vous rechargez votre navigateur, tout va revenir à la valeur par défaut. Cela est dû au fait que nous n'avons pas utilisé les données que nous avons stockées dans **localStorage**

Alors, allez-y et ajoutez ce morceau de code en haut de votre fichier head avant tout fichier CSS. Nous faisons cela pour éliminer le flash que vous obtenez lorsque vous rechargez votre navigateur.

```js
<script>
    const scheme = localStorage.getItem('theme-name');
      document.documentElement.setAttribute('data-theme', scheme);

      const fontSize = localStorage.getItem('font-size');
    document.documentElement.style.setProperty('--font-size',  `${fontSize}px`);
    

    const position = localStorage.getItem('position');
    if (position == 'fixed') {
        document.documentElement.style.setProperty('--position', 'fixed');
        document.documentElement.style.setProperty('--top-margin', '96px');

    } else {
        document.documentElement.style.setProperty('--position', 'static');
        document.documentElement.style.setProperty('--top-margin', '0px');

    }    
    
  </script>
```

## Conclusion

Et voilà ! Vous avez maintenant un site statique simple et personnalisable.

Le but principal de ce guide était de vous montrer les possibilités infinies de création d'un site web personnalisable par l'utilisateur. Alors, allez-y et amusez-vous avec – il y a beaucoup de choses que vous pouvez faire, comme :

1. Montrer aux utilisateurs un contenu spécifique basé sur leurs choix

2. Afficher des messages de notification basés sur les visites des utilisateurs

3. Afficher des publicités de la manière la moins ennuyeuse en montrant aux utilisateurs des publicités basées sur leurs choix

Vous pouvez faire ces choses et bien plus avec nos SSG. Imaginez simplement les possibilités infinies.

Vous n'êtes pas une personne qui aime les tutoriels ? Vous pouvez copier le code source complet [ici](https://spruce.com.ng/blog/on-designing-a-themeable-static-website).