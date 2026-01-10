---
title: Comment personnaliser Bootstrap avec Sass
subtitle: ''
author: Vinod Mathew Sebastian
co_authors: []
series: null
date: '2022-06-21T20:59:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-customize-bootstrap-with-sass
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/How_to_customize_Boostrap_with_Sass.png
tags:
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
- name: Sass
  slug: sass
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment personnaliser Bootstrap avec Sass
seo_desc: 'Bootstrap is an awesome CSS framework that can help you create stylish
  and sleek websites.

  Some developers and teams find that code written in Bootstrap is easier to maintain
  than regular CSS, so they prefer Bootstrap to vanilla CSS.

  But if everyone ...'
---

Bootstrap est un framework CSS génial qui peut vous aider à créer des sites web stylés et élégants.

Certains développeurs et équipes trouvent que le code écrit en Bootstrap est plus facile à maintenir que le CSS régulier, donc ils préfèrent Bootstrap au CSS vanilla.

Mais si tout le monde utilisait Bootstrap avec ses styles par défaut, alors tous les sites se ressembleraient – et rapidement, l'internet deviendrait assez fade. Heureusement, Bootstrap est également hautement personnalisable.

## Comment personnaliser Bootstrap

Si vous êtes débutant, vous pouvez personnaliser Bootstrap avec une feuille de style CSS personnalisée. La spécificité CSS est importante ici. Vous écrivez du CSS personnalisé, avec la même spécificité ou une spécificité plus élevée, et vous le liez dans la section head de votre index.html *après* la ligne qui lie le CSS Bootstrap original.

```typescript
<!-- index.html -->
<head>

    <link rel="stylesheet" href="./node_modules/bootstrap/dist/css/bootstrap.min.css">
    <!-- le CSS personnalisé doit venir après le CSS Bootstrap -->
    <link rel="stylesheet" href="./custom.css"
  
</head>
```

Pour de petits ajustements, cela va. Mais pour des projets plus importants, cela peut être chronophage et il peut y avoir beaucoup de déclarations de style redondantes. Il doit donc y avoir une autre méthode, plus propre.

### Comment utiliser Sass avec Bootstrap

La solution est d'utiliser Sass – un préprocesseur CSS. Sass est compilé en CSS avant d'être utilisé sur les pages web.

Jusqu'à la version 3.x de Bootstrap, vous aviez le choix entre les préprocesseurs CSS : Less ou Sass. Mais depuis la version 4, Bootstrap utilise uniquement Sass. Le code source des frameworks Bootstrap 4 et 5 est entièrement écrit en Sass, ce qui témoigne de la maturité de Sass.

Vous avez peut-être entendu le slogan, "Sass est CSS avec des superpouvoirs". Si vous voulez apprendre Sass, le site [officiel](https://sass-lang.com) est une excellente ressource. Vous pouvez également vous référer à d'autres tutoriels sur freeCodeCamp, comme celui-ci sur [comment utiliser Sass avec CSS](https://www.freecodecamp.org/news/how-to-use-sass-with-css/), ou ce cours vidéo sur [comment utiliser Sass avec Bootstrap 5](https://www.freecodecamp.org/news/learn-bootstrap-5-and-sass-by-building-a-portfolio-website/).

Sass vient avec deux syntaxes. L'ancienne utilise l'indentation et la nouvelle syntaxe SCSS (SCSS pour Sassy CSS) utilise des accolades de type CSS.

SCSS est un sur-ensemble de CSS. Ainsi, le code CSS enregistré avec une extension .scss (ou SCSS entrecoupé de CSS) est également un code Sass valide.

Dans ce tutoriel, nous allons utiliser la version SCSS. Quelle que soit le style, Sass indenté ou SCSS de type CSS, le compilateur Sass le transpilera en CSS vanilla pour être utilisé dans le navigateur.

### Ce que nous allons faire dans ce tutoriel

1. Nous allons changer les couleurs de thème primaire et secondaire fournies par Bootstrap.
    
2. Nous allons également changer les points de rupture média par défaut utilisés par Bootstrap.
    

Une fois que nous pourrons faire cela, il deviendra facile de faire d'autres personnalisations.

### Les prérequis

1. Node.js avec npm ou yarn
    
2. Un éditeur de code, de préférence VS Code.
    
3. Une compréhension de base de Sass
    

Téléchargez Bootstrap depuis le site officiel : [https://getbootstrap.com](https://getbootstrap.com)

Puisque nous avons Node.js installé, je vais utiliser la version npm.

`npm i bootstrap`

Nous devons également installer le compilateur Sass. Nous pouvons obtenir la version officielle dart-sass depuis [leur site web](https://sass-lang.com). Que vous soyez sous Windows, Mac ou Linux, vous devez simplement télécharger le package dart-sass, le décompresser et l'ajouter au chemin (variables d'environnement).

Il existe un package npm sass. De plus, il existe une extension *Live Sass Compiler* pour VS Code avec plus de 2 millions d'installations. N'hésitez pas à utiliser le compilateur Sass avec lequel vous êtes à l'aise.

Ici, nous allons utiliser le package npm : sass.

Après avoir téléchargé Bootstrap et le compilateur Sass, dans le répertoire `node-modules`, il y a un dossier nommé `bootstrap`.

Il y a également trois dossiers à l'intérieur : `dist`, `js` et `scss`.

Tout le CSS compilé est dans `dist`, le code JavaScript de Bootstrap dans `js`, et tous les fichiers Sass sont dans le dossier `scss`.

### Comment changer les couleurs de thème primaire et secondaire

Pour la personnalisation, notre idée est de remplacer les fichiers .scss et de les recompiler.

La documentation officielle de Bootstrap déconseille de modifier les fichiers principaux de Bootstrap chaque fois que possible. Nous allons donc créer une feuille de style custom.scss.

Et nous allons importer tout Bootstrap dans le fichier custom.scss.

```typescript
//custom.scss

@import "../node_modules/bootstrap/scss/bootstrap";
```

Les variables sont suffixées avec un `!default` (un drapeau Sass) dans Bootstrap. Le drapeau `!default` indique au compilateur de définir la valeur uniquement si la valeur n'est pas définie.

Nous définissons donc les variables avant la directive @import afin que, plus tard, le compilateur définisse notre valeur au lieu des valeurs par défaut.

```typescript
//custom.scss

$primary: teal;
$secondary: green;

@import "../node_modules/bootstrap/scss/bootstrap";
```

Nous avons également besoin d'un fichier HTML pour prévisualiser les résultats.

```typescript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenue ! Personnalisez Bootstrap avec Sass</title>
    <link rel="stylesheet" href="./node_modules/bootstrap/dist/css/bootstrap.min.css"
</head>
<body>
 <div class="container" >
 <div class="row">
    <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Personnaliser Bootstrap</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Basculer la navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Accueil</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Lien</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Menu déroulant
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Une autre action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Autre chose ici</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Désactivé</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Rechercher" aria-label="Rechercher">
              <button class="btn btn-outline-success" type="submit">Rechercher</button>
            </form>
          </div>
        </div>
      </nav>
<div class="container">
<div class="row">

  <div class="col-xl pt-3">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, laborum hic, quia maiores animi nobis eligendi est eos saepe architecto reiciendis! Aliquam inventore distinctio reprehenderit corporis amet assumenda officiis dolorem, animi delectus sunt dolor commodi. Adipisci nam nemo labore eligendi quas, rem ipsum iusto eveniet itaque vero necessitatibus! Quas, cupiditate tempora unde nam exercitationem libero aut labore deserunt nesciunt voluptate dignissimos quis porro reprehenderit maiores excepturi, esse, nisi dolores sit tenetur voluptatum corrupti alias provident pariatur? Quam illo unde autem, fugit numquam dolores, odio sed rem saepe exercitationem fuga, nisi soluta sunt officiis! Similique, vero repudiandae quae dignissimos fuga natus!
    </div>

  <div class="col-xl pt-3 ">
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Numquam, aliquid, cumque nisi tenetur similique labore repudiandae voluptas qui hic blanditiis beatae sapiente autem dolore! Quam, cupiditate nostrum laboriosam blanditiis vel ratione, repellat, incidunt modi tempore soluta ab nesciunt? Ab similique illum suscipit exercitationem et, aut quisquam neque atque recusandae rem delectus facilis. Magnam rerum fugit minus explicabo vel! Hic quibusdam laudantium dolorum, pariatur ipsam veritatis voluptate animi, nesciunt dolorem autem dicta. Debitis quae nam dicta autem ipsum mollitia! Ipsum ipsa, molestias fugiat officiis aut illum ullam architecto maxime labore vitae. Ipsum quos neque rerum, esse iste quo explicabo eos ipsa?
    </div>
 
</div>
</div>

<div class="mt-5 pt-5 mb-5 text-center">
  <button type="button" class="btn btn-primary">Primaire</button>
  <button type="button" class="btn btn-secondary">Secondaire</button>
  <button type="button" class="btn btn-success">Succès</button>
  <button type="button" class="btn btn-danger">Danger</button>
  <button type="button" class="btn btn-warning">Avertissement</button>
  <button type="button" class="btn btn-info">Info</button>
  <button type="button" class="btn btn-light">Clair</button>
  <button type="button" class="btn btn-dark">Foncé</button>
  <button type="button" class="btn btn-link">Lien</button>
</div>

 </div>

 </div>
    
</body>
</html>
```

Nous n'avons pas encore compilé Sass. Pour voir les styles par défaut, exécutez *Live Server*.

Si *Live Server* n'est pas installé, vous pouvez télécharger l'extension gratuite depuis le marché des extensions VS Code.

Voici ce que nous voyons :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/default_theme-3.png align="left")

Il est temps de compiler notre fichier Sass personnalisé.

La syntaxe de compilation est simple : spécifiez les dossiers source et de destination séparés par un deux-points.

J'ai mon fichier custom.scss dans un dossier appelé `custom_scss`.

`sass custom_scss/custom.scss:assets/css/custom_bootstrap.css`

Après la recompilation, nous avons le bootstrap personnalisé dans le fichier `assets/css/custom_bootstrap.css`.

Au lieu du fichier bootstrap par défaut, nous allons utiliser cette feuille de style bootstrap personnalisée.

```typescript
<!-- index.html -->
<head>

<link rel="stylesheet" href="./assets/css/custom_bootstrap.css"> `

</head>
```

Ensuite, exécutez à nouveau le *Live Server*.

Nous obtenons la page web personnalisée avec nos nouveaux styles.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/custom_theme..png align="left")

### Comment changer les points de rupture de la grille

Nous allons maintenant personnaliser les points de rupture média. Parallèlement, nous devons également redéfinir les largeurs maximales des conteneurs.

Le moyen le plus simple est de simplement remplacer les variables :

```typescript
$primary: teal;
$secondary:green;

$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1280px,
  xxl: 1600px
);

$container-max-widths: (
  sm: 540px,
  md: 720px,
  lg: 960px,
  xl: 1220px,
  xxl: 1520px
);

@import '../node_modules/bootstrap/scss/bootstrap'
```

Puisque cela violerait les principes DRY (Don't Repeat Yourself), l'utilisation de la fonction `map-merge()` est une meilleure option.

Nous devons d'abord importer les fonctions dans le fichier custom.scss pour rendre `map.merge()` disponible.

Nous devons également importer les variables car $grid-breakpoints (à utiliser à l'intérieur de la fonction) y est défini.

```typescript
//custom.scss

$primary: teal;
$secondary: green;

@import '../node_modules/bootstrap/scss/functions';
@import '../node_modules/bootstrap/scss/variables';
```

Voici le code :

```typescript
//custom.scss

$primary: teal;
$secondary: green;

//Nous devons d'abord importer les fonctions pour utiliser map.merge()

@import '../node_modules/bootstrap/scss/functions';

// Nous devons importer les variables au préalable pour 
//utiliser la variable $grid-breakpoints.
// Sinon, le compilateur affichera une erreur - '$grid-breakpoints 
//non défini.'

@import '../node_modules/bootstrap/scss/variables';

$new-breakpoints: (
    xl: 1280px,
    xxl:1600px
);

$grid-breakpoints: map-merge($grid-breakpoints, $new-breakpoints);

$new-container-max-widths: (
  xl: 1220px,
  xxl:1520px
);

$container-max-widths: map-merge($container-max-widths, $new-container-max-widths);

@import "../node_modules/bootstrap/scss/bootstrap";
```

Nous compilons à nouveau et utilisons le fichier le plus récent à la place de l'ancien.

`<link rel="stylesheet" href="./assets/css/custom_bootstrap.css">`

Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/custom_theme_with_custom_breakpoints-1.png align="left")

Ce ne sont pas seulement les couleurs de thème et les points de rupture média. Les bordures, l'espacement, l'ombre de boîte, les polices, les icônes... vous pouvez tout personnaliser.

J'ai mis tout le code ci-dessus dans ce dépôt GitHub [repo](https://github.com/vinod-vms/Customize_Bootstrap_with_Sass).

Pour explorer davantage, la documentation officielle de Bootstrap [documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) est une excellente ressource à cet égard.

## Conclusion

Dans ce tutoriel, je vous ai montré comment nous pouvons utiliser Sass pour personnaliser Bootstrap.

Même si nous sommes dans un projet qui utilise React avec Bootstrap, l'idée est la même. Créez un fichier .scss personnalisé, faites des personnalisations, importez bootstrap, recompilez, puis liez-le au fichier personnalisé à la place du fichier bootstrap original.

Bon apprentissage !