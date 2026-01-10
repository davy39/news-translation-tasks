---
title: 7 Façons Efficaces Pour Accélérer Votre Site
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-22T14:03:00.000Z'
originalURL: https://freecodecamp.org/news/seven-ways-to-optimize-your-site-for-speed
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/seven-ways.jpg
tags: []
seo_title: 7 Façons Efficaces Pour Accélérer Votre Site
seo_desc: 'By Jared Wolff

  This post is originally from my blog on www.jaredwolff.com.

  Web rankings are dictated by how fast you serve your content.

  You need to optimize to get that top spot. As an added benefit your visitors will
  thank you. (or not even notice ...'
---

Par Jared Wolff

**Cet article provient à l'origine de mon blog sur [www.jaredwolff.com](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/).**


Les classements web sont dictés par la rapidité avec laquelle vous servez votre contenu.

Vous devez optimiser pour obtenir la première place. En prime, vos visiteurs vous en remercieront. (ou ne remarqueront même pas  ce qui est une bonne chose !)

Dans cet article, je vous montre comment optimiser votre site pour la vitesse.

Commençons.

## Obtenir la Base de Référence

Tout d'abord, échantillonnons votre site.

L'outil [PageSpeed Insights de Google](https://developers.google.com/speed/pagespeed/insights/) devrait être votre première étape. Après l'avoir utilisé, vous saurez si votre site est optimisé pour le mobile et le bureau.

Google base ses tests de vitesse sur la rapidité avec laquelle votre page rend le contenu. c'est-à-dire qu'ils mesurent le temps qu'il faut pour que votre site web atteigne les yeux de vos visiteurs. Plus l'attente est longue, plus le score est bas.

Voici une capture d'écran de [cette page](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/) sur mon blog.

![Capture d'écran de PageSpeed Insights](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Screen_Shot_2019-07-07_at_11-d667f3ba-39e7-4de8-85dc-5cb0ff9cdb2c.33.30_AM.png)

Cette capture d'écran a été prise après avoir optimisé quelques gros problèmes. [J'ai abandonné Disqus](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/), j'ai intégré mon CSS et mon Javascript. Les performances sont passées de la fourchette 50/100 à la fourchette 90/100 sur mobile. Pas mal !

L'une de mes principales plaintes concernant PageSpeed Insights est sa **lenteur**.

Comme... **extrêmement lent.**

La solution ?

*Lighthouse.*

### Utiliser Lighthouse

[Lighthouse](https://github.com/GoogleChrome/lighthouse) est un package `npm` que vous pouvez installer sur votre ordinateur. C'est essentiellement PageSpeed Insights, mais en mieux. (PageSpeed Insights est basé sur Lighthouse)

Lorsque vous l'exécutez localement, vous conservez toutes les informations générées par les tests. (Bien que je sois sûr que Chrome envoie des informations sur ce que vous faites... ?)

Voici comment commencer :

1. Pour installer, vous pouvez exécuter :

        npm install -g lighthouse

    Assurez-vous également d'avoir une version de Google Chrome installée. J'utilise [Chrome Canary](https://www.google.com/chrome/canary/).

2. Ensuite, vous pouvez l'exécuter et obtenir un rapport comme ceci :

        lighthouse https://www.jaredwolff.com --view

    `--view` ouvrira le rapport dans votre navigateur web par défaut. Voici un rapport de la même page que précédemment :

    ![Capture d'écran de Lighthouse](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Screen_Shot_2019-07-07_at_2-9830dfd1-91ff-47bf-9d50-419e13fb4c5c.36.47_PM.png)

Il inclut non seulement les performances, mais aussi l'accessibilité, les meilleures pratiques et les suggestions SEO.

L'inconvénient est que vous devrez exécuter ce test page par page. Je vous suggère d'échantillonner les pages qui contiennent beaucoup de contenu. *Ainsi, vous testez le pire de votre site.* Une fois que vous avez corrigé le pire, votre site entier verra une amélioration des performances !

## Passer au Statique

![Logos des générateurs de sites statiques](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Copy_of_Particle_Bluetooth-385a56b6-9f74-4a2d-9ab3-fd0ef8daa8a4.png)

Vous souvenez-vous lorsque les sites web étaient 100% HTML & CSS ?

Au fil des années, nous sommes passés du HTML pur à Ruby On Rails, et lentement, nous revenons en arrière.

La raison ?

La vitesse.

Chaque fois que vous visitez un site web exécutant Flask, Ruby on Rails ou similaire, cela se passe quelque chose comme ceci :

1. Faire une demande pour une page
2. Le serveur assemble votre site
3. Le serveur minifie et gzip
4. Le serveur envoie le contenu au navigateur

Cela en soi ne prend pas longtemps. Lorsque vous multipliez cela par des milliers ou des dizaines de milliers, vous commencez à rencontrer des problèmes.

Et si vous faisiez tout l'*assemblage* une seule fois ?

C'est l'avantage d'un site web généré statiquement.

Examinons comment cela fonctionne :

### Comment fonctionne un générateur de site statique ?

Un générateur de site statique est une collection de modèles et de styles. Ils peuvent être assemblés pour générer différents contenus.

En backend, les générateurs de sites statiques utilisent le markdown et (parfois) le JSON.

Lorsque c'est le moment de compiler, les modèles sont assemblés. Le Markdown est converti en HTML puis injecté dans les modèles. Le résultat ? Un répertoire de sortie de pages "dynamiques" riches. (Un peu comme celle que vous lisez en ce moment si vous êtes sur [mon site](https://www.jaredwolff.com) !)

Personnellement, mon blog est alimenté par [Hugo](https://gohugo.io). J'ai également expérimenté avec [Middleman](https://middlemanapp.com) et [Jekyll](https://jekyllrb.com). Peu importe ce que vous cherchez, vous trouverez probablement un générateur de site statique qui répondra à vos besoins ! Netlify propose une liste de générateurs de sites statiques classés par popularité. [Consultez-la ici.](https://www.staticgen.com)

### Plugins à Gogo

Les générateurs de sites statiques ne se contentent plus de compiler des sites. Ils optimisent, minifient et redimensionnent les images. Cette fonctionnalité intégrée est une autre raison de considérer un site généré statiquement. Exploitez ces ressources, et votre site sera notablement plus rapide.

Par exemple, j'utilisais à l'origine `highlight.min.js` pour la coloration syntaxique du code. Depuis que j'ai découvert la coloration syntaxique intégrée dans Hugo, j'ai abandonné `highlight.min.js`. Hugo injecte le CSS dans le HTML pour les blocs de code. Résultat : une page bien formatée (et statique) !

## Intégrer Javascript et CSS

![Flèches](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/arrows-2029157_1280-76cb0525-f4bf-4f1b-aa80-344c448f0fe5.png)

Comme je l'ai mentionné dans la section précédente, vous subirez un impact sur les performances lorsque vous devrez charger quoi que ce soit d'extra.

Récemment, Hugo a obtenu la capacité de copier le contenu d'un fichier dans le code HTML final. C'est fantastique pour des choses comme le CSS et le Javascript. Ainsi, tout est intégré dans votre fichier HTML. Aucun chargement supplémentaire requis !

Par exemple, je place mon fichier `style.css` complet dans l'en-tête du site. Ainsi, tous les styles sont appliqués immédiatement.

    <!-- Css -->
    {{- $style := resources.Get "/css/style.css" -}}
    <style>
      {{ ( $style | minify ).Content | safeCSS }}
    </style>

Dans le pied de page, j'exporte le `lazysizes.min.js` minifié dans une balise `<script>`. Il est important que cela soit chargé dès que possible car cela dicte comment le reste du site sera chargé.

    <!-- Script de Chargement Paresseux -->
    {{- $lazysizes := resources.Get "/js/lazysizes.min.js" -}}
    <script>
      {{ ( $lazysizes | minify ).Content | safeJS }}
    </script>

**Note de Bas de Page :** `style.css` et `lazysizes.min.js` sont situés dans mon dossier de thème principal sous `assets`. Hugo utilise le dossier `assets` pour rechercher ces fichiers. Si vous avez un site Hugo et que vous souhaitez intégrer votre CSS et Javascript, je vous recommande de [consulter cette ressource.](https://gohugo.io/hugo-pipes/bundling/#readout)

**Deuxième Note de Bas de Page :** Comme vous pouvez le voir ci-dessus, j'utilise la fonction `minify` intégrée de Hugo pour les éléments intégrés. Le Javascript est déjà minifié, mais pas `style.css`. Il existe également une autre méthode programmatique pour minifier tous vos actifs. J'en parlerai plus en détail dans la section **Optimisation avec Gulp**.

## Utiliser ce qui est intégré

Vous avez peut-être remarqué que l'importation de Javascript peut avoir un impact. L'utiliser pour chaque fonctionnalité d'un site web pourrait entraîner des performances médiocres !

Par exemple, nous pourrions utiliser une bibliothèque Javascript pour la validation de formulaire. Mais existe-t-il une meilleure façon ?

(oui)

Vous pouvez utiliser les balises HTML5 comme `required` et utiliser `pattern` pour valider dans le navigateur. Si vous voulez un exemple, consultez le [formulaire de contact](https://www.jaredwolff.com/about/) sur mon site web.

![Capture d'écran du formulaire de contact](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Screen_Shot_2019-07-09_at_5-a66144a9-0394-447b-b8ab-4233e61c1152.44.10_AM.png)

Toute la validation que vous voyez est faite dans le navigateur. Pas de Javascript supplémentaire. Pas de retard de chargement. ?

Une excellente ressource pour tout cela se trouve ici : [https://css-tricks.com/form-validation-part-1-constraint-validation-html/](https://css-tricks.com/form-validation-part-1-constraint-validation-html/) Chris propose également une partie détaillée étape par étape sur la validation en Javascript vanilla. Vous pouvez aller plus loin si vous le souhaitez.

## Organiser le Code

L'endroit où vous placez votre Javascript et votre CSS affectera les performances. Par exemple, je place mon Javascript et mon CSS à des emplacements stratégiques. La feuille de style principale dans le `<head>`, sinon le reste est dans le pied de page ou intégré avec le HTML. De même, le Javascript réside principalement en bas de la page. Ainsi, toutes les choses importantes sont chargées en premier.

Voici un exemple de la façon dont j'organise mon Javascript :

    ...
    </footer>
    ...

    <script src="https://code.jquery.com/jquery-3.4.1.min.js"   integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="   crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>

Je vous encourage à expérimenter pour voir ce qui améliore les performances de votre site. Si vous pouvez vous passer de certaines bibliothèques Javascript, je vous encourage fortement à les supprimer !

## Chargement Paresseux

![Panda Paresseux](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/panda-1892023_1280-cdcbd99d-7f9a-4ac3-9d32-0d01c5f67f8b.png)

Le chargement paresseux est un moyen efficace de différer le chargement des actifs non visibles. Cela améliore ce que Google appelle l'expérience "time to interactive". Un bonus supplémentaire est que si le visiteur ne fait pas défiler vers le bas, les images ne sont pas chargées. Ainsi, économisant de la bande passante et de l'argent pour les sites à fort trafic.

Le chargement paresseux se présente sous la forme de Javascript. Il existe quelques bibliothèques :

- [Lazysizes](https://github.com/aFarkas/lazysizes) ( 11k) - semble être le plus populaire dans ce domaine. Il est plus volumineux que certaines des alternatives. Je teste son utilité autour du chargement paresseux des iframes et du contenu Javascript qui n'est pas immédiatement nécessaire. Par exemple, j'intègre une iframe pour le [graphique Google Docs dans ce post](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/#live-example). Dans le même post, je charge également paresseusement la [vidéo YouTube vers la fin de l'article](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/#you-did-it).
- [Layzr.js](https://github.com/callmecavs/layzr.js) ( 5.5k) - pour les images uniquement
- [lozad](https://github.com/ApoorvSaxena/lozad.js) ( 5.4k) - fait tout ce que fait lazysizes. Cette bibliothèque est axée sur l'utilisation de l'API Intersection Observer. Alors que Lazysizes utilise à la fois l'API Intersection Observer et
- [yall](https://github.com/malchata/yall.js) ( 800) - Cette bibliothèque est également axée sur l'utilisation de l'API Intersection Observer.

### Configuration du Chargement Paresseux

C'est extrêmement simple à configurer. Je vais vous montrer comment utiliser `lazysizes`

1. Inclure le fichier dans votre HTML

        <script src="lazysizes.min.js" async=""></script>

    (Ou si vous utilisez Hugo, injectez-le directement dans votre HTML comme je l'ai fait dans **Intégrer Javascript et CSS**)

2. Ajoutez la classe `lazyload` à ce que vous chargez paresseusement
3. Changez la balise `src` en `data-src`

### Observez la Magie

Lorsque quelqu'un visite votre site, le chargeur paresseux commence à surveiller où se trouve l'utilisateur. Lorsque le visiteur fait défiler, il charge le contenu bientôt visible marqué avec la classe `lazyload`.

Voici un exemple pour une vidéo YouTube intégrée sur [cette page](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/#you-did-it) :

    <iframe class="lazyload" width="700px" height="400px" data-src="https://www.youtube.com/embed/IR2W0GmRKk8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Cela empêche l'iframe de se charger jusqu'à ce que l'utilisateur ait fait défiler à proximité. Sympa !

## Optimisation avec Gulp

![Logo de Gulp](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Copy_of_Particle_Bluetooth-f6420aa8-5c0b-40b3-b478-86b14e5782b0.jpg)

Tout ne peut pas être optimisé par Jekyll ou Hugo. Alors, que pouvez-vous faire ?

Entrez `gulp`

`gulp` est mon outil de choix pour optimiser mon site Hugo. Il existe une large gamme de plugins bien supportés pour `gulp`. Ils peuvent tout faire, de l'optimisation des images à la minification du HTML.

Voici quelques-uns de mes préférés :

`gulp-uglify` - minifie et compresse le Javascript. Je n'ai qu'une seule bibliothèque Javascript à laquelle cela s'applique pour le moment. Si votre projet est lourd en Javascript, regardez définitivement `gulp-uglify`.

`gulp-htmlmin` - minifie le HTML. Vous pouvez également l'utiliser pour minifier le Javascript et le CSS intégrés.

`gulp-imagemin` - probablement le plugin gulp le plus utile pour mes besoins. Pour le moment, je l'utilise pour redimensionner, convertir en jpg puis convertir en jpeg progressif. C'est relativement rapide et, combiné avec `gulp-cache`, cela ne doit être fait qu'une seule fois ! Cela peut sembler compliqué, mais le résultat produit des tailles d'image que Lighthouse adore.

### Exemple

Si vous êtes curieux, voici un extrait de mon `gupfile.js` pour `imagemin`

    gulp.task("resize", function() {
      return gulp
        .src(["content/**/**/*.+(png|jpg|jpeg|gif)"])
        .pipe(cache(imagemin([
          imagemingm.resize({width: 720}),
          imagemingm.convert('jpg'),
          imageminmozjpeg({quality: 80})
        ],{
        verbose: true
        }), {
          fileCache: new Cache({ tmpDir: path.join(process.env.PWD, 'node_modules'), cacheDirName: '.cache' })
        }))
        .pipe(gulp.dest("public/"));
    });

Quelques points importants à noter

- J'ai utilisé `**` pour désigner une valeur générique pour un nom de répertoire. Selon la profondeur de vos images, vous devrez peut-être ajouter plus de `**/` à votre chemin. Cela fonctionne bien pour mon chemin qui est généralement `/contents/post-name/images/image-file.jpg`
- La configuration d'autres plugins qui ne sont pas inclus avec `gulp-imagemin` peut être déroutante. `imageminmozjpeg`, par exemple, est importé séparément. Je l'ai configuré en haut de mon fichier comme suit : `var imageminmozjpeg = require('imagemin-mozjpeg');`
- Enfin, vous pouvez voir que j'utilise `gulp-cache` ici. Selon l'endroit où vous construisez votre site, vous n'aurez peut-être pas à définir d'options. J'utilise Netlify pour mon site. La seule façon pour que `gulp-cache` fonctionne est de définir `tmpDir` et `cacheDirName` vers le dossier `node_modules`. Ainsi, lorsque votre site est construit, votre cache est rechargé. Pas de redimensionnement des images si nous n'en avons pas besoin !

En utilisant `gulp-cache`, mes temps de construction + déploiement sont passés de 10 minutes à ~60 secondes. ? Échanger la légère augmentation de la taille du cache contre le temps de calcul en vaut définitivement la peine. De plus, je suis sûr que Netlify est heureux à ce sujet !

## Supprimer le Superflu

![Empreinte de main sale](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Copy_of_Particle_Bluetooth-3-13292779-1b90-4ee9-8fe3-f547938260b9.jpg)

Lorsque la commodité est présente, il y a toujours un compromis.

C'est ce que je constatais en continuant à utiliser Google Analytics et des services comme Disqus. Disqus, en particulier, avait tendance à me rendre fou. (Avez-vous déjà regardé votre console de débogage Javascript sur un site utilisant Disqus ? Vous comprendrez pourquoi...)

J'ai récemment écrit un tutoriel sur la façon de passer de [Disqus à Commento auto-hébergé](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/). Il y a deux avantages à faire le changement :

1. Vous obtenez le contrôle de votre contenu de site. Il n'y a pas de service tiers qui pourrait disparaître demain. (C'est à vous de vous assurer que votre contenu est sauvegardé ! Un avantage de [payer pour un service](https://www.commento.io) au lieu de l'héberger).
2. Vous obtiendrez un gain de performance !
J'ai testé avant et après et les résultats sont là. Disqus était un frein majeur à l'utilisation du réseau et du CPU.
Commento est léger et l'utilisation des ressources est minimale. Parfait compagnon pour un site généré statiquement !

En tant que propriétaire de site, la qualité et la vitesse dépendent entièrement des fonctionnalités de votre site. N'oubliez pas qu'il peut y avoir de meilleures alternatives. Pas besoin de vendre votre âme à Google, Disqus ou qui que ce soit si vous n'en avez pas besoin !

## Audit de Site

Alors que je termine cet article, je veux vous laisser avec un autre outil pratique.

**L'outil d'Audit de Site de Serpstat.**

Je l'utilise pour explorer mon site à intervalles réguliers. C'est extrêmement utile pour détecter tous types d'erreurs. Par exemple, il a récemment détecté quelques images cassées. J'ai fait quelques modifications et tout était de nouveau opérationnel !

![Capture d'écran de l'Audit de Site de Serpstat](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/images/Screen_Shot_2019-07-07_at_1-66610613-306c-44d6-b55a-34b75655623a.59.54_PM.png)

Si vous voulez garder votre site sans erreur, rien ne vaut un outil d'audit de site comme celui de Serpstat !

## Vous n'avez jamais fini

Vous avez bien lu. Vous n'aurez jamais fini.

Améliorer les performances pour un site en développement actif est sans fin. Malgré vos meilleurs efforts, vous pourriez passer des jours à optimiser des images et à charger paresseusement. Au final, combien cela en vaut-il la peine ? C'est une question à laquelle j'essaie encore de répondre moi-même !

J'espère que vous avez trouvé cet article utile. Quel a été votre plus grand enseignement ? Avez-vous un conseil d'optimisation que je n'ai pas mentionné ? Faites-le savoir dans les commentaires ci-dessous !