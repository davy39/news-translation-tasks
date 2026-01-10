---
title: Comment créer un site portfolio simple avec HTML et CSS
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2025-01-13T23:06:17.482Z'
originalURL: https://freecodecamp.org/news/build-a-simple-portfolio-website-with-html-and-css
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736809428369/d28ee1e5-c11b-48fa-9ccd-b7fbaedd52da.png
tags:
- name: Web Development
  slug: web-development
- name: Beginner Developers
  slug: beginners
- name: portfolio
  slug: portfolio
seo_title: Comment créer un site portfolio simple avec HTML et CSS
seo_desc: 'While browsing through some of my old projects, I stumbled upon a portfolio
  I worked on a while back. The funny thing? I never used it. So, I decided to give
  it a fresh look and thought, why not share it with you?

  As a developer, having a portfolio i...'
---

En parcourant certains de mes anciens projets, je suis tombé sur un portfolio sur lequel j'avais travaillé il y a quelque temps. Le plus drôle ? Je ne l'ai jamais utilisé. Alors, j'ai décidé de lui donner un nouveau look et je me suis dit, pourquoi ne pas le partager avec vous ?

En tant que développeur, avoir un portfolio est important. C'est votre espace personnel pour mettre en valeur vos compétences, partager des projets et impressionner les employeurs potentiels. Que vous cherchiez à construire une présence en ligne, à partager votre travail avec des amis ou à faire passer votre carrière au niveau supérieur, un portfolio est le moyen idéal pour mettre en avant ce que vous savez faire.

Dans cet article, je vais vous guider à travers la création d'un site portfolio simple en utilisant uniquement HTML et CSS. À la fin, vous aurez un site portfolio entièrement fonctionnel prêt à être partagé avec n'importe qui.

### À quoi ressemble le portfolio terminé :

Avant de commencer, voici un aperçu de ce à quoi votre portfolio ressemblera une fois terminé :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736721383725/d8c88f72-5e79-466d-9fe0-d8814be7f1cb.png align="center")

Si vous préférez passer directement à la suite, vous pouvez obtenir le code complet sur [GitHub](https://github.com/iamspruce/Simple-HTML-CSS-Portfolio).

## Voici ce que nous allons couvrir :

* [Aperçu du projet et installation](#heading-installation)
    
* [Comment construire l'en-tête et la section héro](#heading-comment-construire-len-tete-et-la-section-hero)
    
* [Comment construire la section À propos](#heading-comment-construire-la-section-a-propos)
    
* [Comment construire la section Travail](#heading-comment-construire-la-section-travail)
    
* [Comment construire la section Contact et le pied de page](#heading-comment-construire-la-section-contact-et-le-pied-de-page)
    
* [Conclusion](#heading-conclusion)
    

## Aperçu du projet et installation

Avant de commencer à coder, examinons la structure de base du projet. Voici comment tout sera organisé :

```bash
/assets
  - background_image.jpg
  - user.png
  - icon-github.svg
  - icon-twitter.svg
  - logo1.png
  - logo2.png
  - logo3.png
index.html
styles.css
```

Cette structure de dossier garde tout bien organisé. Le dossier `/assets` contiendra toutes vos images et icônes qui seront utilisées sur le site web, tandis que le fichier `index.html` contiendra la structure de votre portfolio, et `styles.css` contrôlera l'apparence de tout.

### Configuration du fichier HTML

Commençons par la structure HTML de base. Ouvrez votre fichier `index.html` et ajoutez le code suivant :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>Spruce - Portfolio Dev</title>
  </head>
  <body>
    <!-- Le contenu ira ici -->
  </body>
</html>
```

Voici une explication de ce que fait ce code :

1. **DOCTYPE** : Cela indique au navigateur qu'il s'agit d'un document HTML5.
    
2. **meta charset** : Définit l'encodage des caractères, ce qui aide à afficher correctement le texte.
    
3. **meta viewport** : Assure que le site web est réactif sur différentes tailles d'écran.
    
4. **lien vers styles.css** : Lie le fichier `styles.css` pour styliser votre site web.
    
5. **title** : C'est le texte qui apparaît dans l'onglet du navigateur lorsque vous ouvrez le site web.
    

Maintenant que notre fichier HTML est configuré, nous passerons au CSS.

### Configuration du fichier CSS

Ajoutons maintenant un style de base en utilisant une réinitialisation CSS. Cela aide à éliminer les incohérences entre les navigateurs en normalisant les styles.

Voici la réinitialisation CSS de base dont vous aurez besoin :

```css
/**
 * CONFIGURATION CORE
 * Cela alimente tout, de la génération de classes utilitaires aux points d'arrêt
 * pour activer/désactiver les composants/utilitaires pré-construits.
 */
/* Règles de dimensionnement de la boîte */
*,
*::before,
*::after {
  box-sizing: border-box;
  font-family: sans-serif;
}

/* Supprimer la marge par défaut */
body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

/* Supprimer les styles de liste sur les éléments ul, ol avec un rôle de liste, ce qui suggère que le style par défaut sera supprimé */
ul[role="list"],
ol[role="list"] {
  list-style: none;
  padding: 0;
}

/* Définir les valeurs par défaut de la racine */
html:focus-within {
  scroll-behavior: smooth;
}

/* Définir les valeurs par défaut du corps */
body {
  min-height: 100vh;
  text-rendering: optimizeSpeed;
  letter-spacing: -0.01em;
}

/* Tous les éléments qui n'ont pas de classe obtiennent des styles par défaut */
a:not([class]) {
  text-decoration-skip-ink: auto;
}

/* Rendre les images plus faciles à utiliser */
img,
picture {
  max-width: 100%;
  display: block;
}

/* Hériter des polices pour les entrées et les boutons */
input,
button,
textarea,
select {
  font: inherit;
}

@media (prefers-reduced-motion: reduce) {
  html:focus-within {
    scroll-behavior: auto;
  }
}

:focus {
  outline: 2px dashed #00ff19;
  outline-offset: 0.25rem;
}

main:focus {
  outline: none;
}
```

Cette réinitialisation efface toutes les marges et les rembourrages par défaut, garantissant que votre mise en page reste cohérente entre les navigateurs. Vous pouvez trouver plus d'informations sur ce que fait le code dans les commentaires.

### Dimensionnement et espacement avec Utopia

Pour l'espacement et la typographie, nous utiliserons un système flexible d'Utopia, un outil conçu pour rendre la typographie réactive plus facile à mettre en œuvre. Voici le CSS qui nous donnera un espacement et des tailles de police ajustables et évolutifs :

```css
/* @link https://utopia.fyi/type/calculator?c=320,18,1.2,1240,20,1.25,5,2,&s=0.75|0.5|0.25,1.5|2|3|4|6,s-l&g=s,l,xl,12 */

:root {
  --step--2: clamp(0.7813rem, 0.7747rem + 0.0326vw, 0.8rem);
  --step--1: clamp(0.9375rem, 0.9158rem + 0.1087vw, 1rem);
  --step-0: clamp(1.125rem, 1.0815rem + 0.2174vw, 1.25rem);
  --step-1: clamp(1.35rem, 1.2761rem + 0.3696vw, 1.5625rem);
  --step-2: clamp(1.62rem, 1.5041rem + 0.5793vw, 1.9531rem);
  --step-3: clamp(1.944rem, 1.771rem + 0.8651vw, 2.4414rem);
  --step-4: clamp(2.3328rem, 2.0827rem + 1.2504vw, 3.0518rem);
  --step-5: clamp(2.7994rem, 2.4462rem + 1.7658vw, 3.8147rem);
}

/* @link https://utopia.fyi/space/calculator?c=320,18,1.2,1240,20,1.25,5,2,&s=0.75|0.5|0.25,1.5|2|3|4|6,s-l&g=s,l,xl,12 */

:root {
  --space-3xs: clamp(0.3125rem, 0.3125rem + 0vw, 0.3125rem);
  --space-2xs: clamp(0.5625rem, 0.5408rem + 0.1087vw, 0.625rem);
  --space-xs: clamp(0.875rem, 0.8533rem + 0.1087vw, 0.9375rem);
  --space-s: clamp(1.125rem, 1.0815rem + 0.2174vw, 1.25rem);
  --space-m: clamp(1.6875rem, 1.6223rem + 0.3261vw, 1.875rem);
  --space-l: clamp(2.25rem, 2.163rem + 0.4348vw, 2.5rem);
  --space-xl: clamp(3.375rem, 3.2446rem + 0.6522vw, 3.75rem);
  --space-2xl: clamp(4.5rem, 4.3261rem + 0.8696vw, 5rem);
  --space-3xl: clamp(6.75rem, 6.4891rem + 1.3043vw, 7.5rem);
}
```

Ces variables CSS vous donnent des tailles de police et des espacements flexibles et réactifs, basés sur la taille de la fenêtre. Par exemple, `--step-5` correspond à la plus grande taille de police, que vous utiliserez pour les titres principaux (`h1`), et des tailles plus petites comme `--step-1` pour le texte moins proéminent.

### Comment la typographie et l'espacement fonctionnent ensemble

Pour appliquer ces valeurs évolutives, nous utiliserons les suivantes pour les titres :

```css
h1,
.h1 {
  font-size: var(--step-5);
}

h2,
.h2 {
  font-size: var(--step-4);
}

h3,
.h3 {
  font-size: var(--step-3);
}

h4,
.h4 {
  font-size: var(--step-2);
}

h5,
.h5 {
  font-size: var(--step-1);
}
```

Ici, le `h1` sera la plus grande taille (en utilisant `--step-5`), et `h2` sera un peu plus petit (`--step-4`), continuant jusqu'à `h5`. Ces variables garantissent que le texte s'adapte à différentes tailles d'écran et maintient une hiérarchie visuelle cohérente.

### Définition des constantes pour les mises en page et l'espacement

Nous pouvons également définir quelques classes utilitaires et enveloppes pour des mises en page plus cohérentes sur le site web. Voici comment nous pouvons définir certaines constantes pour le style de mise en page :

```css
/* définir quelques constantes */
.flex {
  display: flex;
  align-items: center;
  gap: var(--space-s);
}
@media (max-width: 468px) {
  .flex {
    flex-wrap: wrap;
  }
}
.flex_center {
  justify-content: center;
}
.flex_around {
  justify-content: space-around;
}
.flex_between {
  justify-content: space-between;
}
@media (max-width: 468px) {
  .flex_around {
    justify-content: center;
  }
  .flex_between {
    justify-content: center;
  }
}
.text_center {
  text-align: center;
}
.text_right {
  text-align: right;
}

/* définir l'espacement */
.padding-top-3xs {
  padding: var(--space-3xs);
}
```

Ces classes vous permettent d'appliquer rapidement des mises en page flexibles et des espacements dans votre design. La classe `.flex` appliquera Flexbox, tandis que `.flex_center` centra le contenu. Il y a également des ajustements réactifs pour les petits écrans comme l'enveloppement des éléments flexibles lorsque cela est nécessaire.

### Création des enveloppes

Pour aider à structurer votre mise en page de manière nette et cohérente, nous utiliserons des enveloppes. Les enveloppes garantissent que le contenu est centré et ne s'étire pas trop sur les écrans larges :

```css
/* créer les enveloppes */
.wrapper {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
}
.wrapper_inner {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}
```

La classe `.wrapper` garantit que le contenu ne devient pas trop large, tandis que `.wrapper_inner` ajoute une autre couche de contrôle pour les sections internes comme une zone de contenu principale ou des conteneurs plus petits.

## Comment construire l'en-tête et la section héro

Maintenant que notre structure de projet est prête, commençons à construire les premières sections majeures : l'en-tête et la section héro. Ces sections sont la première impression de votre site, donnant aux visiteurs une idée de qui vous êtes tout en offrant une navigation facile.

### HTML pour l'en-tête et la section héro

Voici la structure HTML pour les deux sections :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>Spruce - Portfolio Dev</title>
  </head>
  <body>
    <header class="site_header">
      <div class="wrapper_inner">
        <nav class="site_header_nav">
          <ul role="list" class="flex flex_center">
            <li><a href="#0">ACCUEIL</a></li>
            <li><a href="#apropos">À PROPOS</a></li>
            <li><a href="#travail">TRAVAIL</a></li>
            <li><a href="#contact">CONTACT</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <main>
      <section id="hero">
        <div class="wrapper">
          <div class="wrapper_inner">
            <div class="text_center hero_content">
              <h1 class="h2">Spruce Emmanuel</h1>
              <p class="h5">DÉVELOPPEUR WEB && RÉDACTEUR TECHNIQUE</p>
            </div>
          </div>
          <ul role="list" class="flex flex_between hero_social">
            <address>Port Harcourt, Nigeria</address>
            <ul role="list" class="flex">
              <li>Trouvez-moi en ligne</li>
              <li>
                <a href="https://github.com/iamspruce" target="_blank">
                  <img src="/assets/icon-github.svg" alt="GitHub" width="24" height="24" />
                </a>
              </li>
              <li>
                <a href="https://x.com/sprucekhalifa" target="_blank">
                  <img src="/assets/icon-twitter.svg" alt="Twitter" width="24" height="24" />
                </a>
              </li>
            </ul>
          </ul>
        </div>
      </section>
    </main>
  </body>
</html>
```

Décomposition de l'en-tête :

* **Navigation** : La barre de navigation permet aux utilisateurs de sauter rapidement vers des sections clés comme Accueil, À propos, Travail et Contact. Elle est centrée en utilisant les classes `.flex` et `.flex_center`, ce qui la rend propre et accessible.
    
* **Disposition Flex** : Les liens sont disposés horizontalement en utilisant `.flex` pour un look fluide et moderne.
    

Décomposition de la section héro :

* **Contenu de la section héro** : C'est ici que vous vous présentez. Votre nom et votre titre sont centrés avec un rembourrage pour leur donner de l'espace et de la clarté.
    
* **Réseaux sociaux de la section héro** : Sous votre bio, nous avons ajouté votre localisation et des liens vers vos réseaux sociaux. Ceux-ci sont alignés avec `.flex` pour garder tout propre et facile à naviguer.
    

### CSS pour l'en-tête et la section héro

Voici le CSS pour styliser ces sections :

#### Style de l'en-tête :

```css
/* Style de l'en-tête */
.site_header {
  padding: var(--space-s) 0;
  background: linear-gradient(rgba(26, 26, 64, 0.9), rgba(26, 26, 64, 0.9));
}

.site_header_nav ul li a {
  text-decoration: none;
  color: #fff;
}
```

* `.site_header` : Ajoute un rembourrage et un dégradé sombre pour un arrière-plan élégant.
    
* `.site_header_nav ul li a` : Supprime les soulignements des liens et rend le texte blanc pour un look moderne et audacieux.
    

#### Style de la section héro :

```css
/* Style de la section héro */
.hero_content {
  padding: var(--space-3xl) 0;
}

.hero_content h1 {
  margin-bottom: var(--space-s);
}

.hero_social {
  padding-top: var(--space-3xl);
}

/* Style général pour la section héro */
section {
  padding: var(--space-2xl) var(--space-l);
}

section#hero {
  background: linear-gradient(rgba(26, 26, 64, 0.9), rgba(26, 26, 64, 0.9)),
    url("/assets/background_image.jpg");
  padding-bottom: 4px;
  background-size: cover;
  background-position: top;
  background-attachment: scroll;
  color: #fafafa;
  --color-accent: #8a2be2;
}
```

* `.hero_content` : Ajoute un rembourrage pour garder le contenu spacieux.
    
* `.hero_social` : Fait de la place pour les liens des réseaux sociaux pour qu'ils se démarquent.
    
* `section#hero` : Définit un arrière-plan de dégradé stylisé avec une image, garantissant que la section héro semble engageante et visuellement frappante.
    

Voici à quoi cela ressemble à ce stade :

![Portfolio après avoir ajouté les sections héro et en-tête](https://cdn.hashnode.com/res/hashnode/image/upload/v1735812582003/a755c5b5-b5b9-4bdd-9d1b-c0ff850f066d.png align="center")

## Comment construire la section À propos

La section À propos vous permet de vous présenter et de partager votre parcours professionnel, donnant aux visiteurs un aperçu de qui vous êtes et de ce que vous faites.

### HTML pour la section À propos

Voici la structure HTML pour la section À propos :

```html
<section id="apropos">
  <div class="wrapper">
    <div class="text_center">
      <h2>
        Je suis un développeur web et un rédacteur technique. J'écris des articles sur le développement web et la programmation.
      </h2>
    </div>
    <div class="wrapper_inner">
      <div class="about_content flex flex_around">
        <figure class="about_figure text_center">
          <img width="200px" height="200px" src="/assets/user.png" alt="Développeur" class="about_img" />
          <figcaption class="about_caption">Spruce 💖</figcaption>
        </figure>
        <p class="h5">
          Né au Nigeria, j'ai passé 4+ ans à construire et à écrire sur JavaScript. J'aide les entreprises à commercialiser leurs produits et services grâce à la rédaction technique.
        </p>
      </div>
    </div>
  </div>
</section>
```

Décomposition de la section À propos :

* **Introduction** : Une déclaration courte et claire sur votre rôle en tant que développeur.
    
* **Contenu À propos** : L'image de profil et la bio sont positionnées côte à côte avec un conteneur flex pour l'équilibre.
    
* **Figure et image** : L'image de profil est affichée dans une balise `<figure>`, avec une légende en dessous.
    
* **Texte** : Une bio brève expliquant votre parcours et votre expertise.
    

### CSS pour la section À propos

Voici le style CSS pour la section À propos :

#### Style de la section À propos :

```css
/* Section À propos */
.about_content {
  padding: var(--space-xl) 0;
  transform: skewX(-10deg);
}

@media (max-width: 468px) {
  .about_content {
    transform: skewX(0deg);
  }
}

.about_figure {
  padding: var(--space-xl) 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 2px solid #ccc;
  display: inline-block;
  padding: 5px;
}

.about_img {
  width: 300px;
  height: 200px;
  object-fit: cover;
}

.about_caption {
  padding: var(--space-3xs) 0;
}

section#apropos {
  background-color: #ffffff;
  color: #333;
  --color-accent: #ffd700;
}
```

Décomposition du CSS :

* **Effet de skew** : La classe `.about_content` donne à la section un look dynamique avec un léger skew, qui est supprimé sur les petits écrans.
    
* **Style de la figure** : L'image de profil obtient un rembourrage et une ombre de boîte subtile pour l'aider à se démarquer.
    
* **Style de l'image** : L'image remplit l'espace de manière proportionnelle, garantissant qu'elle ne se déforme pas.
    
* **Style de la légende** : Le rembourrage autour de la légende fournit un meilleur espacement.
    

### Aperçu de la section À propos :

Voici à quoi ressemblera votre section À propos après avoir appliqué ces styles :

![Portfolio après avoir ajouté la section À propos](https://cdn.hashnode.com/res/hashnode/image/upload/v1735812908296/509c6cf0-a8c5-448b-8bb4-a466a76a2cbe.png align="center")

## Comment construire la section Travail

La **section Travail** est l'endroit où vous pouvez présenter les entreprises ou les projets avec lesquels vous avez travaillé ou contribué. Cette section aide à démontrer votre expérience et l'impact que vous avez eu, tout en fournissant aux visiteurs des exemples visuels de votre parcours professionnel.

### HTML pour la section Travail

Voici la structure HTML pour la **section Travail** :

```html
<section id="travail">
  <div class="wrapper_inner">
    <div class="text_center">
      <h4 class="h5">
        Jusqu'à présent, j'ai aidé 20+ entreprises à construire leur présence en ligne et
        à améliorer leur documentation technique.
      </h4>
      <ul role="list" class="work_logos flex flex_center">
        <li>
          <img src="/assets/logo1.png" alt="Acme Corp" />
        </li>
        <li>
          <img src="/assets/logo2.png" alt="Acme Innovations" />
        </li>
        <li>
          <img
            src="/assets/logo1.png"
            alt="Acme Solutions"
            width="50"
            height="50"
          />
        </li>
        <li>
          <img src="/assets/logo3.png" alt="Acme Technologies" />
        </li>
        <li>
          <img src="/assets/logo1.png" alt="Acme Enterprises" />
        </li>
      </ul>
    </div>
  </div>
</section>
```

Décomposition de la section Travail :

* **Introduction** : L'élément `<h4>` introduit l'expérience de travail avec une déclaration mettant en avant comment vous avez aidé les entreprises avec leur présence en ligne et leur documentation technique.
    
* **Logos** : Les logos des entreprises avec lesquelles vous avez travaillé sont placés à l'intérieur d'une liste non ordonnée (`<ul>`). Chaque logo est enveloppé dans un élément de liste (`<li>`) pour une meilleure structure et mise en page.
    
* **Disposition Flexbox** : Les logos sont positionnés dans une mise en page flexible en utilisant les classes `flex` et `flex_center`. Cela garantit que les logos sont espacés uniformément et centrés horizontalement dans la section.
    

### Style CSS pour la section Travail

Ajoutons maintenant du style à la section Travail pour la rendre visuellement attrayante et réactive.

#### Style de la section Travail :

```css
/* section travail */
.work_logos {
  margin-top: var(--space-xl);
}

section#travail {
  background-color: #87ceeb;
  color: #0c0c0c;
  --color-accent: #2e8b57;
}
```

## Comment construire la section Contact et le pied de page

La **section Contact** et le **pied de page** fournissent un espace pour que les visiteurs puissent vous contacter et une touche finale pour la page web. Il est essentiel d'avoir un formulaire facile à utiliser pour les demandes, ainsi qu'un pied de page qui inclut vos informations de copyright.

### HTML pour la section Contact et le pied de page

Voici la structure HTML pour la **section Contact** et le **pied de page** :

```html
<section id="contact">
  <div class="wrapper">
    <div class="text_left">
      <p>
        Vous voulez travailler ensemble ? <br />
        J'adorerais avoir de vos nouvelles.
      </p>
    </div>

    <div class="wrapper_inner">
      <h5 class="h3">Contactez-moi</h5>
      <form action="" method="post" class="contact_form">
        <div class="flex">
          <div class="form_group">
            <label for="name">NOM</label>
            <input type="text" id="name" name="name" />
          </div>
          <div class="form_group">
            <label for="email">EMAIL</label>
            <input type="email" id="email" name="email" />
          </div>
        </div>
        <div class="form_group">
          <label for="message">Message</label>
          <textarea id="message" name="message"></textarea>
        </div>
        <button type="submit">ENVOYER LE MESSAGE</button>
      </form>
    </div>
  </div>
</section>


<footer>
  <section id="footer">
    <div class="wrapper">
      <div class="text_right">
        <p>&copy; 2025 Spruce Emmanuel</p>
      </div>
    </div>
  </section>
</footer>
```

Décomposition du HTML :

* **Section Contact** : Cette section comprend un texte d'accueil qui invite les utilisateurs à vous contacter, suivi d'un formulaire de contact avec des champs pour le nom de l'utilisateur, l'email et un message.
    
* **Pied de page** : Le pied de page comprend les informations de copyright, garantissant que les visiteurs savent qui possède le contenu. Il est placé en bas de la page et donne une touche professionnelle au site.
    

### CSS pour la section Contact et le pied de page

Stylisons maintenant la **section Contact** et le **pied de page** pour les rendre à la fois conviviaux et visuellement attrayants.

#### Style de la section Contact :

```css
/* section contact */
.contact_form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form_group {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

textarea {
  resize: vertical;
  height: 150px;
}

button[type="submit"] {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
```

#### Style de la section Pied de page :

```css
/* section pied de page */
section#footer {
  padding: var(--space-l) var(--space-l);
}
```

## Conclusion

Et voilà ! Vous venez de créer un site portfolio simple en utilisant uniquement HTML et CSS. Vous avez appris à structurer votre projet, à appliquer une réinitialisation CSS, et à créer des systèmes de typographie et de mise en page réactifs qui s'adaptent magnifiquement à différentes tailles d'écran.

En suivant ce guide, vous avez maintenant un portfolio dont vous pouvez être fier et que vous pouvez partager avec vos amis, votre famille ou des employeurs potentiels. La beauté de ce projet est que vous pouvez continuer à l'étendre et à le personnaliser en ajoutant de nouvelles sections, en mettant en avant davantage de votre travail, ou en expérimentant avec JavaScript pour ajouter des éléments interactifs.

Si vous êtes intéressé à explorer des fonctionnalités plus avancées ou à apprendre comment héberger votre portfolio en ligne, consultez mon tutoriel sur [Comment héberger votre projet sur GitHub – Expliqué avec des exemples](https://www.freecodecamp.org/news/host-your-first-project-on-github/).

Si vous avez des questions, n'hésitez pas à me trouver sur Twitter à [@sprucekhalifa](https://x.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus de conseils et de mises à jour. Bon codage !