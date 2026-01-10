---
title: 'L''architecture du triangle inversé : comment gérer de grands projets CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-05T15:58:12.000Z'
originalURL: https://freecodecamp.org/news/managing-large-s-css-projects-using-the-inverted-triangle-architecture-3c03e4b1e6df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l6ZhrrSG2cqp_ObV1jZrgQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'L''architecture du triangle inversé : comment gérer de grands projets
  CSS'
seo_desc: 'By Luuk Gruijs

  You’re assigned a small task to fix some little styling issues here and there. You’ve
  found the correct CSS rules to apply the fix, so you quickly drop those rules at
  the bottom of your CSS file, push your changes, and then move on wit...'
---

Par Luuk Gruijs

On vous confie une petite tâche pour corriger quelques petits problèmes de style ici et là. Vous avez trouvé les bonnes règles CSS pour appliquer la correction, alors vous ajoutez rapidement ces règles en bas de votre fichier CSS, vous poussez vos changements, puis vous passez à des choses plus importantes.

Avec le temps, cela arrive plusieurs fois et avant que vous ne vous en rendiez compte, « le bas » de votre fichier CSS se compose de quelques centaines de lignes de code que personne ne comprend et que personne n'ose supprimer car cela briserait inévitablement des choses.

Reconnaissez-vous ce scénario parce que vous l'avez fait vous-même ou que vous avez vu des collègues le faire ? Eh bien, continuez à lire et promettez-vous de ne plus jamais faire cela, car voici une méthode plus simple pour gérer vos fichiers CSS.

### Présentation de l'architecture du triangle inversé

L'architecture du triangle inversé, également connue sous le nom d'ITCSS, est une méthodologie pour structurer votre CSS de la manière la plus efficace et la moins gaspilleuse.

ITCSS a été introduit pour la première fois par Harry Roberts et peut être mieux visualisé par un triangle en couches à l'envers. ITCSS définit les règles CSS partagées d'un projet de manière logique et saine, tout en fournissant un niveau solide d'encapsulation et de découplage qui empêche les règles CSS non partagées d'interférer les unes avec les autres.

ITCSS est très flexible car il ne vous impose pas d'utiliser des méthodologies spécifiques de conventions de nommage comme SMACCS, OOCSS ou BEM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4oGYOCrfBqsjnqGwZ_GaHg.jpeg)

### Les principes

ITCSS fonctionne en structurant votre projet CSS entier selon ces 3 principes :

1. **Générique à explicite**  
Nous commençons par les styles les plus génériques, de bas niveau, qui attrapent tout. Cela pourrait être des paramètres de police ou, par exemple, des variables de couleur si vous utilisez SCSS.
2. **Faible à haute spécificité**  
Les sélecteurs de la plus faible spécificité apparaissent au début de votre projet. La spécificité augmente progressivement. De cette façon, nous évitons les conflits de spécificité et les remplacements de spécificité utilisant `!important`.
3. **Large portée à localisé**  
Les sélecteurs au début de notre projet affectent beaucoup d'éléments DOM, par exemple vos styles de réinitialisation du navigateur, tandis que les sélecteurs plus tard dans notre projet deviennent très localisés, par exemple des styles spécifiques pour un composant.

### Les couches du triangle

En respectant les principes ci-dessus, nous devons diviser notre CSS en couches. Chaque couche doit être introduite à un endroit qui respecte chacun des critères.

Il arrive souvent que le CSS soit regroupé par, par exemple, des styles typographiques, des styles de formulaire et des styles pour un composant spécifique. Ces groupes ne sont souvent pas importés dans l'ordre le plus efficace et cela crée des problèmes d'héritage ou de spécificité.

Dans ITCSS, chaque couche est une progression logique de la précédente. Elle augmente en spécificité, se rétrécit en portée et devient plus explicite. Cela signifie que notre CSS est plus facile à mettre à l'échelle, car nous ajoutons simplement à ce qui existe déjà et ne remplaçons pas ce qui a été écrit précédemment.

Un autre grand avantage de suivre cette structure est que tout le monde sait toujours où trouver certaines règles CSS car elles sont placées de manière logique. Cela évite le problème des personnes qui ajoutent leurs règles CSS en bas du fichier.

Harry Roberts, le créateur d'ITCSS, a défini sept couches. Il les a ordonnées comme suit :

1. **Paramètres**  
Si vous utilisez un préprocesseur comme SCSS, c'est votre point de départ. Dans cette couche, vous définissez vos variables.
2. **Outils**  
Cette couche peut être utilisée pour vos outils. Pensez aux mixins et fonctions qui doivent être disponibles globalement. Si elles n'ont pas besoin de l'être, placez-les simplement dans la couche où elles sont nécessaires.
3. **Générique**  
Dans cette couche, nous logeons tous les styles très haut niveau et à large portée. Cette couche est souvent la même dans tous vos projets car elle contient des choses comme Normalize.css, les réinitialisations CSS et, par exemple, les règles de box-sizing.
4. **Éléments**  
Dans cette couche, nous mettons les styles pour les éléments HTML nus, sans classe. Vous pourriez, par exemple, penser aux soulignements pour les ancres au survol ou aux tailles de police pour les différents titres.
5. **Objets**  
Dans la couche objet, nous stylisons les premiers éléments qui ont des classes. Pensez à vos conteneurs, enveloppes ou lignes. Vous pouvez également définir votre grille ici.
6. **Composants**  
La couche composant est l'endroit où la plupart de la magie de stylisation se produit car vous styliserez vos éléments d'interface utilisateur ici. Dans les frameworks basés sur les composants comme Angular, Vue ou React, c'est la couche où vous importez votre stylisation pour chaque composant si vous ne les incluez pas directement dans votre composant.
7. **Atouts**  
La couche atouts est la couche sale. Même après avoir structuré votre stylisation selon les principes ITCSS, il peut arriver que vous deviez utiliser `!important` pour remplacer certains styles tiers, par exemple. Faites-le dans cette couche car c'est la couche la plus spécifique, locale et explicite.

### Le résultat final

Maintenant que j'ai expliqué les couches, il est temps de voir à quoi pourrait ressembler un résultat final simple.

```
// paramètres@import "globals";@import "branding";
```

```
// outils@import "mixins";
```

```
// generique@import "normalize";
```

```
// elements@import "fonts";@import "form";
```

```
// objets@import "grid";@import "wrappers";
```

```
// composants@import "header";@import "sidebar";@import "carousel";@import "card";
```

```
// atouts@import "overrides";
```

### Conclusion

Tout comme ITCSS ne vous impose pas d'utiliser certaines conventions de nommage, il ne vous impose pas d'utiliser toutes les couches. Utilisez une structure de couches qui fonctionne le mieux pour vous tout en maintenant les principes ITCSS de générique à explicite, de faible à haute spécificité et de large portée à localisé.

Si vous remarquez que vous devez remplacer des styles, cela signifie presque toujours que votre structure est inefficace. Si vous avez envie d'en apprendre plus sur ce sujet, je vous recommande de regarder cette vidéo :

### Vous cherchez un emploi à Amsterdam ?

Je travaille pour **Sytac** en tant que développeur front-end senior et nous recherchons des développeurs médians/seniors spécialisés dans Angular, React, Java ou Scala. Sytac est une entreprise de conseil ambitieuse aux Pays-Bas qui travaille pour de nombreuses entreprises renommées dans les secteurs bancaire, aérien, gouvernemental et de la vente au détail.

Si vous pensez avoir ce qu'il faut pour travailler avec les meilleurs, envoyez-moi un email à [luuk[dot]gruijs[at]sytac[dot]io](mailto:luuk.gruijs@sytac.io) et je serais ravi de vous en dire plus.