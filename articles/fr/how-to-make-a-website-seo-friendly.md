---
title: Comment rendre un site Web SEO-friendly et le maintenir ainsi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-20T11:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-website-seo-friendly
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/park-pano.png
tags:
- name: 'Digital Marketing '
  slug: digital-marketing
- name: marketing
  slug: marketing
- name: SEO
  slug: seo
- name: Web Development
  slug: web-development
seo_title: Comment rendre un site Web SEO-friendly et le maintenir ainsi
seo_desc: 'By Adam Henson

  Amidst the economic devastation of COVID-19, online businesses have become dependent
  on SEO now more than ever. Times like these illustrate the power and importance
  of Search Engine Optimization.

  What is SEO?

  SEO is the practice of inc...'
---

Par Adam Henson

Au milieu de la dévastation économique de la COVID-19, les entreprises en ligne sont devenues dépendantes du SEO plus que jamais. Des périodes comme celles-ci illustrent le pouvoir et l'importance de l'optimisation pour les moteurs de recherche.

### Qu'est-ce que le SEO ?

Le SEO est la pratique qui consiste à augmenter la quantité et la qualité du trafic vers une page web grâce aux résultats de recherche organiques. Les résultats de recherche organiques sont dérivés d'un algorithme interne du moteur de recherche et non le résultat de la publicité payante. Ci-dessous se trouve une liste de termes associés.

* **SERP** ou Search Engine Results Page est simplement la page de résultats qui génère des clics. Ces pages incluent une combinaison de résultats de recherche payants et organiques.
* **SEM** ou Search Engine Marketing est la pratique de marketing d'une entreprise utilisant des publicités payantes qui apparaissent sur les SERPs.
* **PPC** signifie pay-per-click, un modèle de marketing internet dans lequel les annonceurs paient des frais chaque fois qu'une de leurs annonces est cliquée.

Apprendre les bases du SEO et des sujets plus avancés peut être un processus déconcertant. Dans cet article, nous allons examiner des étapes simples pour aider à créer des pages web SEO-friendly et des outils pour les maintenir.

## Contenu pertinent et significatif

Le facteur le plus important pour un site web SEO-friendly est un contenu unique, pertinent et significatif. Bien que cela semble évident, il est plus facile de se tromper que de réussir.

Une compréhension approfondie des utilisateurs du site web est cruciale pour maîtriser la création de contenu. Un contenu qui établit une forte connexion avec l'utilisateur stimulera l'interaction et réduira le taux de rebond. Les moteurs de recherche reconnaissent le temps que les utilisateurs passent sur un site web et les niveaux d'interaction.

**Ne soyez pas trop malin**. Le SEO n'est pas un jeu de cartes dans lequel vous devez surpasser l'adversaire. "L'optimisation excessive" est un terme qui décrit des techniques anciennes qui tentent de tromper les moteurs de recherche, comme le "bourrage de liens" et le "bourrage de contenu" par exemple. Dans le passé, certains trucs se sont avérés efficaces, mais ils étaient finalement de courte durée.

**La stratégie de mots-clés** peut mener au succès en SEO lorsqu'elle est bien faite. Trouver le bon équilibre entre l'utilisation des mots-clés et la pertinence du sujet est crucial pour atteindre ce succès.

**La variété du contenu** et du format est un moyen efficace de retenir l'attention. Un ensemble riche de contenu incluant des images, des vidéos, des tableaux et des listes captivera ces regards.

**Organiser le contenu** dans une hiérarchie de site web logique est un autre aspect fondamental dans la création d'un site web SEO-friendly. La page d'aide de la Search Console de Google "[Search Engine Optimization (SEO) Starter Guide](https://support.google.com/webmasters/answer/7451184?hl=en#hierarchy)" fournit un guide élaboré pour organiser le contenu.

## Balisage sémantique et données structurées

Un contenu bien construit est clé pour le SEO, tout comme un code bien construit que nos navigateurs et moteurs de recherche utilisent pour interpréter le contenu.

De nombreuses balises HTML ont une signification sémantique qui aide les interprètes à comprendre et classer les types de contenu. En tant que développeurs web, nous nous sentons parfois impuissants dans le monde du marketing lourd du SEO, mais écrire un **balisage sémantique** est l'un des outils les plus impactants dans notre ceinture à outils.

Pourquoi écrire chaque élément HTML comme un `div` alors que nous avons un spectre complet de balises pour identifier différents types de contenu. Ci-dessous se trouvent quelques-unes des balises sémantiques les plus utiles.

* Titres de page
* Descriptions de page
* Paragraphes
* Listes
* Articles
* Sections
* En-têtes
* Pieds de page
* Etc, etc

Encore une fois, il est important d'être malin en rédigeant du HTML, mais pas trop malin. Une répartition bien équilibrée de mots-clés partagés à travers les titres, descriptions, h1 et h2 peut aller loin. Les titres et descriptions doivent être uniques entre les pages et pertinents en contenu.

**Les données structurées** sont un nouveau format de données, suivant la [spécification JSON-LD](https://json-ld.org/), qui peut être intégré dans les pages HTML. Les moteurs de recherche comme Google interprètent les données structurées pour comprendre le contenu de la page, ainsi que pour recueillir des informations sur le web et le monde en général comme expliqué dans "[Understand how structured data works](https://developers.google.com/search/docs/guides/intro-structured-data)". Ci-dessous se trouve un exemple simple.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Foo Software | Website Quality Monitoring",
  "url": "https://www.foo.software",
  "sameAs": [
    "https://www.facebook.com/www.foo.software",
    "https://www.instagram.com/foosoftware/",
    "https://github.com/foo-software",
    "https://www.linkedin.com/company/foo-software"
  ]
}
</script>
```

## Accessibilité et performance du site web

Les moteurs de recherche continueront sûrement à élever la barre des normes web acceptables. [En 2018, Google a annoncé le début de sa migration vers l'indexation mobile-first](https://webmasters.googleblog.com/2018/03/rolling-out-mobile-first-indexing.html) et a élargi en annonçant [l'indexation mobile-first pour l'ensemble du web en 2020](https://webmasters.googleblog.com/2020/03/announcing-mobile-first-indexing-for.html). La performance et l'accessibilité des pages web englobent des métriques centrées sur l'utilisateur qui peuvent finalement impacter le SEO.

**La performance du site web** capture le parcours de l'utilisateur, marquant divers moments de l'expérience utilisateur. Ci-dessous se trouvent des métriques de performance importantes.

* **[First contentful paint (FCP)](https://web.dev/fcp/):** mesure le temps à partir du moment où la page commence à charger jusqu'à ce qu'une partie du contenu de la page soit rendue à l'écran. 
* **[Largest contentful paint (LCP)](https://web.dev/lcp/):** mesure le temps à partir du moment où la page commence à charger jusqu'à ce que le plus grand bloc de texte ou élément d'image soit rendu à l'écran.
* **[First input delay (FID)](https://web.dev/fid/):** mesure le temps à partir du moment où un utilisateur interagit pour la première fois avec votre site (c'est-à-dire lorsqu'il clique sur un lien, tape sur un bouton, ou utilise un contrôle personnalisé, alimenté par JavaScript) jusqu'au moment où le navigateur est réellement capable de répondre à cette interaction.
* **[Time to Interactive (TTI)](https://web.dev/tti/):** mesure le temps à partir du moment où la page commence à charger jusqu'à ce qu'elle soit visuellement rendue, que ses scripts initiaux (le cas échéant) aient chargé, et qu'elle soit capable de répondre rapidement aux entrées de l'utilisateur de manière fiable.
* **[Total blocking time (TBT)](https://web.dev/tbt/):** mesure la quantité totale de temps entre FCP et TTI où le thread principal était bloqué suffisamment longtemps pour empêcher la réactivité des entrées.
* **[Cumulative layout shift (CLS)](https://web.dev/cls/):** mesure le score cumulé de tous les décalages de mise en page inattendus qui se produisent entre le moment où la page commence à charger et celui où son [état de cycle de vie](https://developers.google.com/web/updates/2018/07/page-lifecycle-api) change pour devenir caché.

**L'accessibilité du site web** est un autre concept important à garder à l'esprit lors de la construction d'un site web optimisé pour les moteurs de recherche. Non seulement il y a une variété d'humains qui lisent nos sites web, mais aussi une variété de machines comme les lecteurs d'écran qui font de même.

> Améliorer l'accessibilité rend votre site plus utilisable pour tout le monde. ~ Addy Osami | [Conseils d'accessibilité pour les développeurs web](https://web.dev/a11y-tips-for-web-dev/)

## Outils SEO

Dans cet article, nous avons examiné des moyens d'améliorer le SEO, mais comment maintenir ces normes au fil du temps ? De nombreux outils peuvent nous aider à analyser et à surveiller le SEO.

[Vérification automatisée de Lighthouse par Foo](https://www.foo.software/lighthouse) surveille la qualité des pages web avec Lighthouse. Il fournit des rapports détaillés sur le SEO, la performance et l'accessibilité. Des plans gratuits et premium sont disponibles.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/automated-lighthouse-check.png)
_Tableau de bord de la vérification automatisée de Lighthouse_

[**Google Search Console**](https://search.google.com/search-console/about) est un incontournable pour tout propriétaire de site web qui se soucie du SEO. Il fournit des informations sur les termes de recherche qui reçoivent du trafic organique et un niveau granulaire d'analyse. Vous pouvez filtrer par lieu, appareil et plus encore.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/google-search-console.png)
_Tableau de bord des performances de Google Search Console_

## Conclusion

Le SEO n'est pas une pratique facile à maîtriser, mais parmi les astuces tendances du métier qui viennent et disparaissent avec le temps, l'approche la plus efficace devrait venir naturellement. Un contenu significatif et bien formé, combiné à un code bien formé, livré de manière performante et accessible, satisfera sûrement les dieux du SEO.