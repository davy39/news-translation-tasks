---
title: 10 Astuces CSS Que Tout Développeur Web Doit Connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-10T18:34:13.000Z'
originalURL: https://freecodecamp.org/news/10-css-hacks-every-web-developer-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/css-hacks.jpg
tags:
- name: CSS
  slug: css
- name: hacks
  slug: hacks
- name: Web Design
  slug: web-design
seo_title: 10 Astuces CSS Que Tout Développeur Web Doit Connaître
seo_desc: 'By Gert Svaiko

  While CSS isn’t as widely used as JavaScript, it’s still in the top 10 coding languages,
  according to Redmonk. Since CSS is quite robust, reasonably easy to learn, and universal
  across different browsers, it’s popular among website dev...'
---

Par Gert Svaiko

Bien que le CSS ne soit pas aussi largement utilisé que [JavaScript](https://www.freecodecamp.org/news/javascript-hacks/), il fait toujours partie des [10 langages de programmation les plus populaires](https://redmonk.com/sogrady/2020/07/27/language-rankings-6-20/), selon Redmonk. Étant donné que CSS est assez robuste, raisonnablement facile à apprendre et universel sur différents navigateurs, il est populaire parmi les développeurs de sites web.

Comme pour tout langage de programmation, il existe plusieurs raccourcis ou astuces avec CSS qui vous permettent d'écrire un code plus propre, d'améliorer les éléments de design et de gagner un temps précieux. De plus, vous pouvez insérer directement ces extraits de code sur votre site en utilisant un [éditeur de code](https://www.freecodecamp.org/news/source-code-editors-explained/).

Il est également important de savoir que vous n'avez pas besoin d'être un développeur web senior pour utiliser CSS. Les données de W3Techs montrent que CSS est utilisé par [96 pour cent de tous les sites web](https://w3techs.com/technologies/details/ce-css), et savoir utiliser CSS pour améliorer la mise en page et l'apparence d'un site web est intégral au fonctionnement des principaux CMS open source comme WordPress.

En fait, la plupart des [meilleurs outils de création de sites web](https://websitesetup.org/best-website-builder-tools/) (généralement connus pour promouvoir une approche "What You See Is What You Get" ou WYSIWYG) permettent désormais aux utilisateurs d'insérer du code CSS personnalisé.

Si vous êtes nouveau dans le domaine du CSS, freeCodeCamp propose un excellent [tutoriel vidéo sur YouTube](https://www.youtube.com/watch?v=kMT54MPz9oE) où vous pouvez apprendre les bases. Si vous connaissez déjà les aspects fondamentaux, alors commençons avec ces dix astuces CSS.

## 1. Comment centrer du contenu avec CSS

Placer du contenu au milieu de l'écran peut être délicat. Cependant, vous pouvez utiliser `position: absolute` pour remplacer le positionnement dynamique et toujours positionner le contenu au centre.

Cela fonctionne également avec toutes les résolutions sur différents appareils. Cependant, vérifiez toujours si tout est positionné comme vous le souhaitez et si l'élément semble naturel même sur les petits écrans.

Exemple de code :

```css
section {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding: 30px;
}
```

## 2. Comment fixer la position d'un élément en CSS

Malgré le fait que les sites web soient dynamiques, vous pouvez avoir certains éléments que vous souhaitez fixer dans certaines positions. Vous pouvez le faire en utilisant le script `position:absolute`.

Cependant, utilisez cette méthode avec prudence et testez-la au préalable sur toutes les tailles et résolutions d'écran pour ne pas casser le design de votre site.

En suivant ce script avec un nœud de position spécifique, vous vous assurez que l'élément reste dans la même position pour tous les utilisateurs.

Exemple de code :

```css
/* supposons que vous souhaitez fixer la position et la taille de votre barre latérale */
.sidebar {
  position: absolute;
  top: 15px;
  right: 15px;
  width: 300px;
  height: 150px;
}
```

## 3. Comment adapter les images à la page en CSS

Il y a peu de choses plus désagréables que vos images débordant de l'écran de vos visiteurs. Cela peut complètement casser le design de votre site et décourager les utilisateurs.

Cependant, avec cette astuce simple, vous pouvez vous assurer que vos images s'adaptent toujours à l'écran du visiteur, quel que soit l'appareil qu'il utilise.

Exemple de code :

```css
img {
  max-width: 100%;
  height: auto;
}
```

## 4. Comment modifier les styles sur une seule page en CSS

Si vous avez un CMS et que vous souhaitez que certains de vos articles aient un aspect différent des autres, vous pouvez utiliser une classe personnalisée pour remplacer les styles CSS du site. Cela garantit que vous ne modifiez qu'une seule page d'article et laissez les autres par défaut.

Lorsque vous créez un article sur un blog WordPress, il inclut l'ID de l'article comme une classe dans le `body`, par exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-97.png)

Vous pourriez alors faire quelque chose comme ceci pour changer le style de cette page d'article uniquement :

```css
.postid-330 {
  font-size: 24px;
  font-weight: 750;
  color: red;
}
```

D'autres CMS populaires vous permettent d'ajouter des classes personnalisées à des articles individuels. Par exemple, Ghost vous permet de marquer un article comme un article en vedette et ajoute une classe `.featured`.

Cependant, si vous utilisez souvent cette méthode, il est préférable de modifier la feuille de style CSS principale pour éviter d'écrire du code inutile.

Et cela ne s'applique pas seulement aux CMS – si vous avez un site web simple avec plusieurs fichiers HTML, vous pourriez appliquer un style personnalisé aux éléments de votre projet et les ajuster via le même fichier CSS.

Par exemple, si vous avez une page avec la classe `.landing` :

```html
<!DOCTYPE html>
<html lang="en">
  <meta charset="UTF-8" />
  <title>Landing Page</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <link href="css/style.css" rel="stylesheet" />
  <body class="landing">
    <h1>Landing Page</h1>
    <p>My landing page.</p>
  </body>
</html>

```

Et une autre avec la classe `.about` :

```html
<!DOCTYPE html>
<html lang="en">
  <meta charset="UTF-8" />
  <title>About Page</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <link href="css/style.css" rel="stylesheet" />
  <body class="landing">
    <h1>About Page</h1>
    <p>My about page.</p>
  </body>
</html>

```

Vous pourriez ajouter ceci à votre feuille de style principale pour ajuster uniquement le style de la page à propos :

```css
.about {
  font-size: 24px;
  font-weight: 750;
  color: red;
}
```

## 5. Comment consolider le style en CSS

Si vous savez que vous souhaitez ajouter un style CSS à plusieurs éléments, écrire ces morceaux de code un par un prend du temps. Cependant, lorsque vous séparez les éléments avec des virgules et écrivez le style CSS à l'intérieur, le style est ajouté à tous.

Cela vous aide à gagner du temps et à réduire le poids de votre code car vous n'avez pas à écrire une ligne de code similaire plusieurs fois.

Exemple de code :

```css
/* supposons que vous souhaitez ajouter une bordure solide autour de votre élément de légende, image et élément de paragraphe */
.caption, img, p {
  border: 2px solid #000000;
}

/* vous pouvez également limiter la sélection en utilisant des sélecteurs */
p.white-text, div > p.unique {
  color: white;
  font-size: 24px;
}
```

## 6. Style des liens visités en CSS

Le style par défaut des liens visités sur lesquels les utilisateurs ont cliqué peut ne pas bien fonctionner avec le style actuel de votre site. Vous pouvez utiliser le code CSS pour ajuster l'apparence des liens avant et après que les visiteurs aient cliqué dessus.

Vous pouvez ensuite les assortir au style global de votre site pour créer une expérience unique.

Exemple de code :

```css
a:link {
  color: #ff0000; /* le lien non visité est rouge */
}
a:visited {
  color: #ee82ee; /* le lien visité devient violet */
}
```

## 7. Effets de survol avec délai en CSS

Le sélecteur `:hover` est une pseudo-classe CSS qui vous permet de créer un effet de survol. Cependant, vous pouvez le styliser davantage en ajoutant un élément `transition` pour retarder l'effet de survol.

Bien que cela semble soigné, cela crée également un sentiment de mouvement dans les yeux des utilisateurs, attirant davantage l'attention sur l'élément.

Exemple de code :

```css
.entry h2 {
  font-size: 48px;
  color: #000000;
  font-weight: 750;
}

/* Ensuite, ajoutez un délai à l'effet de survol */
.entry h2:hover{
  color: #f00;
  transition: all 0.5s ease;
}
```

## 8. Comment désactiver le retour à la ligne du texte et ajouter des points de suspension en CSS

Si vous manquez d'espace pour votre texte, vous devrez peut-être le raccourcir pour qu'il s'adapte à d'autres éléments. Bien sûr, vous pouvez ajuster manuellement chacun des éléments de texte, mais cela prend du temps et nécessite quelques essais et erreurs.

Ce que vous pouvez faire à la place, c'est combiner `overflow`, `white-space` et `text-overflow` pour créer une rupture naturelle dans le texte qui est agréable à l'œil.

L'exemple suivant définit la limite de la largeur du texte, masque la partie débordante, désactive le retour à la ligne du texte et ajoute des points de suspension (...) pour indiquer qu'il y a plus de texte pour les utilisateurs.

Exemple de code :

```css
.product-description {
max-width: 150px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

## 9. Stylisation de la lettre initiale en CSS

Les [lettres initiales stylisées ou lettrines](http://www.magazinedesigning.com/drop-caps-and-initial-letters/) sont utilisées depuis longtemps dans la conception de livres et de magazines. Cela fonctionne en attirant l'attention des lecteurs et en les incitant à lire la première ligne.

Bien que vous puissiez penser que ce style a vieilli, vous pouvez également le concevoir pour qu'il ait un aspect moderne et toujours capitaliser sur l'effet psychologique qu'il crée pour vos visiteurs. De plus, l'option des lettrines est également écrite dans le langage CSS, vous pouvez donc l'utiliser sans effort et donner à vos paragraphes un nouveau look.

Exemple de code :

```css
p:first-letter {
  display: block;
  float: left;
  margin: 5px;
  color: #000000;
  font-size: 60px;
}
```

## 10. Comment réinitialiser les styles CSS

Enfin, mais non des moindres, vous devrez peut-être remplacer tous les attributs de style par défaut sur différents navigateurs pour que votre design fonctionne sans faille.

Chaque navigateur a sa propre feuille de style, avec des styles par défaut intégrés, et cela peut parfois poser problème lorsque vous essayez de faire en sorte que votre site web ait une apparence cohérente sur tous les navigateurs.

Vous pouvez utiliser une réinitialisation CSS complète d'[Eric Meyer](https://meyerweb.com/eric/tools/css/reset/) qui couvre presque tous les aspects. Cependant, vous pouvez également obtenir un résultat de réinitialisation minimal, que vous pouvez emprunter à [Jeff Starr](https://perishablepress.com/a-killer-collection-of-global-css-reset-styles/) :

```css
* {
  vertical-align: baseline;
  font-weight: inherit;
  font-family: inherit;
  font-style: inherit;
  font-size: 100%;
  border: 0;
  outline: 0;
  padding: 0;
  margin: 0;
}
```

Et voilà, dix astuces pour rendre votre code CSS plus propre, réduire votre temps de codage et ajouter des éléments conviviaux pour les visiteurs.

### Merci d'avoir lu !

Je suis un écrivain passionné par le marketing numérique, le développement web et la cybersécurité. Vous pouvez me contacter sur [LinkedIn ici](https://www.linkedin.com/in/gert-svaiko/).

Vous pourriez également apprécier d'autres articles que j'ai écrits :

* [10 Astuces JavaScript Que Tout Développeur Web Doit Connaître](https://www.freecodecamp.org/news/javascript-hacks/)
* [Comment Optimiser les Applications Web Progressives : Aller Au-Delà des Bases](https://www.smashingmagazine.com/2020/12/progressive-web-apps/)
* [Les 10 Attaques de Sécurité de Site Web les Plus Courantes (et Comment Vous Protéger)](https://www.tripwire.com/state-of-security/featured/most-common-website-security-attacks-and-how-to-protect-yourself/)

_[Crédit Image](https://www.hippopx.com/en/code-coder-coding-computer-conceptual-css-data-355989)_