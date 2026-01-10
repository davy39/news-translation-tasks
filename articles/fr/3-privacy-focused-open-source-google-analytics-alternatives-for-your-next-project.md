---
title: 3 alternatives open source à Google Analytics axées sur la confidentialité
  pour votre prochain projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-04T12:20:06.000Z'
originalURL: https://freecodecamp.org/news/3-privacy-focused-open-source-google-analytics-alternatives-for-your-next-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/markus-winkler-IrRbSND5EUc-unsplash.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: open source
  slug: open-source
seo_title: 3 alternatives open source à Google Analytics axées sur la confidentialité
  pour votre prochain projet
seo_desc: "By Leonardo Faria\nAs a content creator, I like to know the page analytics\
  \ of my website. \nOverall, I am curious to know how many people are reading my\
  \ content, where they came from (referrer and countries), and what the most popular\
  \ pages are.\n20 yea..."
---

Par Leonardo Faria

En tant que créateur de contenu, j'aime connaître les statistiques de mes pages web. 

Globalement, je suis curieux de savoir combien de personnes lisent mon contenu, d'où elles viennent (référent et pays), et quelles sont les pages les plus populaires.

Il y a 20 ans, des outils comme [Webalizer](http://www.webalizer.org/) étaient tout ce sur quoi nous pouvions compter. Des outils comme celui-ci analysaient les logs Apache et créaient des pages statiques avec les données traitées.

![capture d'écran de webalizer](https://www.freecodecamp.org/news/content/images/2020/09/webalizer.jpg)

Une autre façon d'obtenir des statistiques de pages était d'insérer une image - souvent invisible - sur votre site. En utilisant les en-têtes de requête envoyés au serveur, les gens pouvaient compter les visiteurs et obtenir un peu plus d'informations telles que l'IP d'origine, le navigateur et le système d'exploitation. Cette technique est ancienne, mais des services comme [statcounter](https://statcounter.com/) fournissent toujours cette fonctionnalité.

En 2005, Google a lancé Google Analytics après avoir acquis [Urchin](https://en.wikipedia.org/wiki/Urchin_(software)), une entreprise qui analysait également les logs de serveur. Sa présence n'a fait que croître depuis les premiers jours et son utilisation est bien plus importante que celle de ses concurrents. Mais, il y a quelques raisons [pour lesquelles vous devriez arrêter d'utiliser Google Analytics sur votre site web](https://plausible.io/blog/remove-google-analytics) : 

1) Il est détenu par Google, qui utilise les analyses à son propre bénéfice
2) Il affecte la vitesse du site en ajoutant 45 Ko aux requêtes de page
3) Il est trop invasif, collectant beaucoup de données personnelles dont vous n'avez pas besoin
4) Il est bloqué par de nombreux plugins et navigateurs, créant des données inexactes

Avec tout cela à l'esprit, je souhaite partager quelques alternatives open source que j'ai examinées au cours des derniers mois.

## Fathom

[Fathom](https://usefathom.com/) ([démo](https://app.usefathom.com/share/sqqvo/chimp+essentials)) est une application légère en Golang pour collecter des statistiques. 

Ils ont différents plans payants qui commencent à 14 $/mois. Ils ont également une version légère que vous pouvez installer sur votre serveur ou Heroku gratuitement.

![capture d'écran de Fathom](https://www.freecodecamp.org/news/content/images/2020/09/fathom.jpg)

La version légère utilise des cookies et vous donne des informations sur les visiteurs uniques, les vues de pages, le temps moyen passé sur le site, le taux de rebond, les pages les plus populaires et les principaux référents. Fathom stocke les données dans des bases de données SQLite, MySQL ou Postgresql.

## umami

[umami](https://umami.is/) ([démo](https://app.umami.is/share/ISgW2qz8/flightphp.com)) est une solution créée avec Next.js, ce qui la rend très facile à déployer. Dans mon cas, j'ai utilisé Vercel.

En plus des visiteurs uniques, des vues de pages, du temps moyen passé sur le site, du taux de rebond, des pages les plus populaires et des principaux référents, umami vous montre également des informations sur les pays, les navigateurs, les systèmes d'exploitation et les appareils.

![capture d'écran de umami](https://www.freecodecamp.org/news/content/images/2020/09/umami.jpg)

## Plausible

Je pense avoir entendu parler pour la première fois de [Plausible](https://plausible.io/) ([démo](https://plausible.io/plausible.io)) dans le podcast "[De-Google-ing your website analytics](https://changelog.com/podcast/396)" de Changelog. D'un point de vue produit, c'est agréable de voir une [feuille de route publique](https://plausible.io/roadmap) disponible afin que les clients puissent savoir ce qui arrive ensuite.

Leurs plans commencent à 6 $/mois et augmentent en fonction de vos vues de pages - comme Fathom. Ils ont également une option auto-hébergée en version _alpha_, mais je n'ai pas eu l'occasion de la tester.

![plausible](https://www.freecodecamp.org/news/content/images/2020/09/plausible.jpg)

## Conclusion

Il existe des alternatives, et vous n'avez pas à vous soucier d'une grande entreprise qui vous surveille, vous ou vos utilisateurs, avec ces options. Le temps de configuration de chaque service est très similaire, et une fois terminé, vous pouvez ajouter plusieurs sites comme vous le feriez avec Google Analytics.

Je n'ai pas de préféré. En termes de fonctionnalités, umami fournit toutes les informations de base que vous souhaitez connaître gratuitement. Il est également très facile à configurer sur des services comme Vercel ou Netlify. 

Fathom et Plausible offrent tous deux des essais gratuits afin que vous puissiez facilement tester leurs solutions avant de décider.

_Connaissez-vous une autre alternative minimaliste et open source à Google Analytics ? Faites-le moi savoir dans la section [commentaires](https://leonardofaria.net/2020/09/01/three-privacy-focused-open-source-google-analytics-alternatives/) de mon blog._

Si vous avez aimé cet article, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria). 

Photo de couverture par [Markus Winkler/Unsplash](https://unsplash.com/photos/IrRbSND5EUc)