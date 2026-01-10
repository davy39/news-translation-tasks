---
title: Ressources d'accessibilité pour les développeurs
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2023-09-05T22:49:13.000Z'
originalURL: https://freecodecamp.org/news/accessibilty-websites-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/a11y.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
seo_title: Ressources d'accessibilité pour les développeurs
seo_desc: 'Accessibility is never a "nice-to-have" requirement when it comes to developing
  websites and apps. It''s a "must-have" that should be an integral part of your design
  and development process.

  Ensuring good accessibility is a fundamental responsibility ...'
---

L'accessibilité n'est jamais une exigence "agréable à avoir" lorsqu'il s'agit de développer des sites web et des applications. C'est un "must-have" qui devrait faire partie intégrante de votre processus de conception et de développement.

Garantir une bonne accessibilité est une responsabilité fondamentale pour les développeurs. Cela peut aider leurs applications à offrir une expérience équitable à tous les utilisateurs.

Mais il peut être facile de se perdre dans un terrier de lapin lorsqu'on apprend les meilleures pratiques en matière d'accessibilité.

Heureusement, il existe de nombreuses ressources disponibles qui vous apprennent à créer des sites web et des applications accessibles. Dans cet article, je vais discuter des trois sites web que je consulte fréquemment lorsque j'ai des questions sur l'accessibilité : W3C WCAG, WebAIM et a11yprojects.

Examinons chacun d'eux et comment vous pouvez les utiliser pour créer des projets plus accessibles.

## W3C WCAG

Tout d'abord, il y a [**W3C WCAG**](https://www.w3.org/WAI/standards-guidelines/wcag/). Comme indiqué sur le site Web des Web Content Accessibility Guidelines (WCAG), WCAG fournit "des stratégies, des normes, des ressources pour rendre le Web accessible aux personnes handicapées".

Les directives énumérées sur ce site web fournissent des cadres complets pour les développeurs afin de rendre les pages web universellement accessibles.

WCAG aide les développeurs à créer des espaces numériques qui sont utilisables, perceptibles, exploitables et robustes.

Une excellente section du W3C est [Easy Checks – A First Review of Web Accessibility](https://www.w3.org/WAI/test-evaluate/preliminary/#title). Dans cette section, les développeurs peuvent facilement apprendre les règles d'accessibilité en ce qui concerne les titres de page, les images, le texte et les interactions. La section Easy Checks est un excellent point de départ pour naviguer dans le W3C.

**Comment utiliser W3C WCAG :**

* Visitez le site Web W3C WCAG et explorez les directives et les critères de succès pertinents pour votre projet.

* Étudiez les techniques et les documents pour les technologies que vous utilisez.

* Vérifiez les exigences de conformité pour fixer des objectifs d'accessibilité pour votre site Web ou votre application.

Pour en savoir plus sur ces normes et comment rendre un site Web accessible, vous pouvez venir à W3C et étudier les critères nécessaires pour être considéré comme accessible. W3C WCAG est l'un des meilleurs sites Web pour apprendre les règles d'accessibilité.

## WebAIM

Sur le site Web de [WebAIM](https://wave.webaim.org/), ils déclarent qu'ils "donnent aux individus et aux organisations les moyens de créer et de livrer du contenu accessible".

WAVE est un outil d'évaluation de l'accessibilité. Un outil que WAVE offre est son extension de navigateur. Après avoir téléchargé l'extension de navigateur WAVE, vous pouvez inspecter vos pages et enregistrer les problèmes d'accessibilité avec la page. Ensuite, vous pouvez facilement déterminer comment corriger ces problèmes.

L'extension WAVE est disponible sur FireFox et Chrome et rend si simple la reconnaissance des problèmes d'accessibilité courants. Vous pouvez trouver des instructions sur la façon de télécharger l'extension WAVE sur l'onglet [extensions de WAVE](https://wave.webaim.org/extension/).

Après avoir téléchargé l'extension WAVE, vous pouvez aller dans vos extensions et l'exécuter. Trouver des problèmes d'accessibilité est aussi rapide que de cliquer sur un bouton. Par exemple, après avoir téléchargé WAVE, j'ai exécuté l'extension sur la page d'accueil du New York Times et j'ai été alerté des problèmes d'accessibilité que le site Web avait.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-10.17.10-PM.png align="left")

*Capture d'écran de la page d'accueil du New York Times avec l'extension WAVE pointant les erreurs d'accessibilité*

Dans la capture d'écran ci-dessus, vous pouvez voir la page d'accueil du New York Times avec l'extension WAVE en cours d'exécution. Sur le côté gauche de la capture d'écran, vous pouvez voir l'onglet de résumé de WAVE pointant 1 problème d'accessibilité dans la page d'accueil avec 120 erreurs. Il s'agit de l'onglet de résumé de WAVE, qui donne aux développeurs un aperçu des problèmes d'accessibilité dans la page.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-10.23.40-PM.png align="left")

*Capture d'écran de la page d'accueil du New York Times avec l'extension WAVE pointant les erreurs d'accessibilité*

WAVE va en profondeur et explique davantage l'onglet de résumé. En cliquant sur la section des détails de l'extension, les erreurs d'accessibilité sont listées en plus grands détails, que vous pouvez voir dans la capture d'écran ci-dessus.

L'erreur qui était dans la page de résumé est expliquée plus en détail dans la section des détails. WAVE souligne que l'erreur d'accessibilité était une image liée manquante de texte alternatif. Les 120+ avertissements sont également listés en beaucoup plus de détails, qui soulignent qu'il y a 8 textes alternatifs longs, 1 en-tête de premier niveau manquant, 4 liens redondants et bien plus encore.

L'onglet des détails est un excellent moyen de découvrir les problèmes d'accessibilité que votre page pourrait avoir et de vous donner un point de départ pour corriger les problèmes d'accessibilité.

**Comment utiliser WebAIM :**

* Installez l'extension de navigateur WAVE, puis exécutez-la sur vos pages web pour identifier et résoudre les problèmes d'accessibilité.

* Explorez le site Web de WebAIM pour des ressources supplémentaires, des articles et des matériaux de formation.

## a11yproject

[**a11yproject**](https://www.a11yproject.com/), prononcé "a-eleven-y-project" (avec "11" représentant les lettres omises dans le mot accessibilité) "est un effort communautaire pour rendre l'accessibilité numérique plus facile".

Ce site web affiche des articles qui parlent tous d'accessibilité. Les articles sont écrits par des développeurs et approuvés par l'équipe a11yproject.

Certains articles récents publiés sur a11yprojects incluent, [What is Semantic HTML?](https://www.a11yproject.com/posts/what-is-semantic-html/) et [The power of ChatGPT as a cognitive accessibility assistive technology for Traumatic Brain Injury survivors](https://www.a11yproject.com/posts/the-power-of-chatgpt-as-a-cognitive-accessibility-assistive-technology-for-traumatic-brain-injury-survivors/). Il y a beaucoup plus de sujets intéressants autour de l'accessibilité également.

Les projets a11y sont divisés en différentes catégories, qui vont des conseils rapides, des antécédents, des mythes, des tests rapides et bien plus encore. Les lecteurs peuvent aller sur a11yprojects et filtrer vers une catégorie d'article qu'ils veulent voir.

Les articles de a11yproject sont écrits par des développeurs qui sont passionnés par l'accessibilité et ont beaucoup de connaissances à partager avec les autres. Vous pouvez aller sur le site web de a11yprojects pour lire les dernières nouvelles sur l'accessibilité. Le site couvre tous les aspects de l'accessibilité, mais se concentre principalement sur l'accessibilité web.

**Comment utiliser a11yproject :**

* Visitez le site web de a11yproject pour lire des articles sur les meilleures pratiques d'accessibilité et les dernières nouvelles dans le domaine.

* Engagez-vous avec la communauté de l'accessibilité en participant à des discussions et en contribuant vos connaissances.

## Conclusion

Il existe de nombreuses ressources disponibles en ligne pour les développeurs afin d'apprendre les dernières nouvelles sur l'accessibilité. Il existe également de nombreuses communautés de développeurs qui sont passionnées par l'accessibilité.

W3C WCAG, WebAIM et a11yprojects ne sont que quelques ressources en ligne disponibles pour les développeurs afin de mener des recherches sur l'accessibilité. En allant sur ces trois sites web, les développeurs peuvent apprendre les dernières nouvelles sur l'accessibilité et étudier les critères d'accessibilité acceptables.