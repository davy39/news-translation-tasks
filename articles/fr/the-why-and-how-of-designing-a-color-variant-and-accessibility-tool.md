---
title: Comment et pourquoi j'ai conçu un outil de variante de couleur et d'accessibilité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T11:00:48.000Z'
originalURL: https://freecodecamp.org/news/the-why-and-how-of-designing-a-color-variant-and-accessibility-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Splash.png
tags:
- name: Accessibility
  slug: accessibility
- name: colors
  slug: colors
- name: Design
  slug: design
- name: UI Design
  slug: ui-design
- name: ux design
  slug: ux-design
seo_title: Comment et pourquoi j'ai conçu un outil de variante de couleur et d'accessibilité
seo_desc: 'By Stephen McLean

  As a developer, choosing colors for my designs has always been one of the more difficult
  tasks. To help I tend to use tools like Coolors, SASS Color Generator, and this
  color contrast checker.

  My process used to look something like ...'
---

Par Stephen McLean

En tant que développeur, choisir des couleurs pour mes designs a toujours été l'une des tâches les plus difficiles. Pour m'aider, j'ai tendance à utiliser des outils comme [Coolors](https://coolors.co/), [SASS Color Generator](http://scg.ar-ch.org/), et [ce vérificateur de contraste de couleur](https://webaim.org/resources/contrastchecker/).

Mon processus ressemblait autrefois à ceci :

1. Générer une palette en utilisant Coolors
2. Choisir des variantes pour chaque couleur en utilisant SASS Color Generator
3. Associer des variantes ensemble en combinaisons arrière-plan/premier plan.
4. Vérifier que les paires sont accessibles en utilisant le vérificateur de contraste de couleur.
5. Ajouter mes couleurs choisies à mon outil de design préféré (Figma).
6. Ajuster les couleurs et répéter à partir de l'étape 2.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Original-Process.png)
_L'ancien processus_

# Alors, quel était le problème ?

Mon ancien processus impliquait beaucoup d'allers-retours entre différentes applications. Je ne pouvais pas ajuster mes couleurs et voir l'impact sur l'accessibilité en temps réel. Au lieu de cela, je devais copier/coller des codes HEX d'une application à une autre. Ensuite, lorsque j'étais prêt à commencer le développement, je devais créer manuellement les variables en SASS/CSS et copier les valeurs à nouveau.

# Et la solution ?

Créer un outil où je pourrais faire (presque) tout en un seul endroit. Mon objectif était de passer à un processus comme celui-ci :

1. Générer une palette en utilisant Coolors
2. Choisir des variantes, associer des couleurs et faire des ajustements en utilisant une seule application.
3. Ajouter les couleurs résultantes à mon outil de design préféré.

Je voulais également que l'application puisse exporter mes couleurs en code afin d'avoir un bon point de départ pour le développement.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/New-Process.png)
_Le nouveau processus_

# La preuve de concept initiale

Je voulais avoir quelque chose d'opérationnel le plus rapidement possible afin de pouvoir commencer à le tester. À cette fin, je me suis mis à créer un prototype.

## Cas d'utilisation

La première étape pour mettre ensemble un prototype était de définir les cas d'utilisation qui le piloteraient.

1. **En tant qu'utilisateur, je veux générer des variantes pour mes couleurs de base.**

Je voulais pouvoir ouvrir l'application, ajouter mes couleurs de base, choisir les variantes, puis les ré-exporter vers mon outil de design. Simple, non ?

**2. En tant qu'utilisateur, je veux vérifier si une paire de couleurs arrière-plan/premier plan est accessible.**

À partir des couleurs de base entrées ou de leurs variantes, je voulais pouvoir vérifier si deux couleurs étaient accessibles lorsqu'elles étaient associées ensemble.

**3. En tant qu'utilisateur, je devrais pouvoir voir l'impact que le changement d'une couleur de base a sur l'accessibilité.**

Je voulais pouvoir obtenir un retour en temps réel sur les paires de couleurs que j'avais choisies chaque fois que je faisais des ajustements à mes couleurs de base.

## Une version (très approximative) fonctionnelle

Avec les cas d'utilisation définis, je me suis ensuite mis à concevoir le prototype. J'ai créé une palette de couleurs, conçu un ensemble limité de composants, et finalement abouti à une solution qui avait trois "modes" ou pages, l'utilisateur devant passer de l'un à l'autre pour accomplir ses tâches.

Plutôt que de le décrire davantage, regardons.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/poc.gif)
_Mon premier brouillon en action_

Comme vous pouvez le voir sur l'image ci-dessus, le prototype a réalisé tout ce que je voulais en fonction des cas d'utilisation initiaux... En quelque sorte.

> _[Cliquez ici](https://5d112084bc6f2c00097f59a7--rainbo.netlify.com/) si vous souhaitez essayer le prototype vous-même, grâce à la magie des aperçus de déploiement Netlify._

# Le bon et le mauvais du design original

Je n'ai jamais eu l'intention que le premier prototype soit autre chose qu'une étape, et vous pouvez voir par vous-même qu'il était assez approximatif et imparfait.

Pour la version suivante, j'ai commencé par examiner **ce que j'aimais** dans le prototype.

## Mode Variante

J'étais assez satisfait de la façon dont la partie génération de variantes du prototype s'est avérée. Il était assez simple de choisir une couleur et d'obtenir votre liste de variantes. De plus, l'approche par onglets fonctionnait assez bien pour ajouter plusieurs couleurs de base.

## Pouvoir voir les changements d'accessibilité après avoir changé une couleur

Comme vous pouvez le voir dans la courte démonstration ci-dessus, il n'était plus nécessaire de copier/coller des codes HEX entre les applications. Je pouvais maintenant changer une de mes couleurs et voir comment cela affectait l'accessibilité des couleurs vraiment rapidement.

Ensuite, j'ai commencé à noter les choses que **je n'aimais pas** et qui devaient être **améliorées**.

## Les interactions n'étaient pas évidentes

En arrivant sur la page d'accueil, il n'était pas immédiatement évident de savoir comment procéder pour choisir des variantes et vérifier l'accessibilité. Vous auriez probablement compris qu'il fallait cliquer sur les tuiles éventuellement, mais c'était vraiment maladroit.

## Les modes étaient confus

Dans les designs initiaux, vous ne pouviez ajouter des paires qu'à partir de la vue palette, et vous ne pouviez ajouter/supprimer des variantes qu'à partir de la vue variantes. Tout cela impliquait beaucoup de changements entre les écrans et je me suis retrouvé frustré par la quantité de travail que l'application me faisait faire. Cela m'amène à mon prochain point.

## Trop de clics étaient nécessaires

Vous devez cliquer pour ajouter une variante. Ensuite, vous devez cliquer pour passer à la vue palette. Ensuite, vous devez cliquer plusieurs fois pour créer une paire. Ensuite, vous devez cliquer encore pour voir la paire que vous venez d'ajouter. Comme je l'ai mentionné ci-dessus, tout cela était assez maladroit et c'était probablement la pire partie du prototype et quelque chose que je savais devoir changer.

## Pas assez d'informations étaient visibles à l'écran en même temps

Plus je l'utilisais, plus je commençais à ne pas aimer le concept de "modes" que j'avais créé. Je pense que j'ai été influencé par le processus original qui a inspiré l'application et j'ai conçu les écrans en silos plutôt que de concevoir une expérience unifiée. Après avoir utilisé le prototype, j'ai décidé que je devais m'éloigner du concept de "modes" pour quelque chose qui, idéalement, pourrait tout être fait sur une seule page.

# Une deuxième tentative

J'ai tiré les leçons du prototype et me suis mis à créer une meilleure version de l'application.

Afin de **réduire le nombre d'interactions** requises, **réduire l'ambiguïté dans les interactions**, et **augmenter la quantité d'informations disponibles** pour l'utilisateur à la fois, j'ai décidé de passer à une interface utilisateur basée sur le glisser-déposer où l'utilisateur pourrait faire glisser des tuiles pour les ajouter à sa palette ou créer des vérifications d'accessibilité.

La cible de glisser-déposer serait toujours affichée et cela éviterait le besoin de changer d'écran.

Regardons ce que j'ai imaginé.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Kapture-2019-07-11-at-19.19.23.gif)
_La version actuelle_

Vous pouvez accéder à la version actuelle de l'application [ici](https://rainbo.xyz/).

# Prochaines étapes

L'application en est encore à ses débuts et bien que la deuxième version soit beaucoup plus proche de l'idée que j'avais en tête, il y a encore des améliorations à apporter.

## Importer depuis le code

En plus d'exporter la palette, je prévois d'ajouter la possibilité de lire les couleurs de base initiales à partir de code contenant des variables (SASS, et variables CSS pour commencer).

## Exporter vers plus de formats

Actuellement, vous ne pouvez exporter qu'en SASS. Je prévois d'ajouter la prise en charge des variables CSS, et d'autres formats à l'avenir.

## Intégrer avec les outils de design

Exporter vers du code est bien, mais ce serait encore mieux si je pouvais exporter la palette et ensuite l'importer en tant que calque ou style partagé dans un outil de design tel que Figma ou Sketch.

## Affiner l'interface utilisateur

Soyons honnêtes, ce n'est pas la meilleure application en termes d'apparence au monde. Je prévois d'ajuster les composants de l'interface utilisateur pour améliorer visuellement l'application.

## Retour d'information et signalement de bugs

Celui-ci se comprend de lui-même. Je ne peux améliorer l'application qu'avec les contributions de ceux qui l'utilisent. Pour cela, je prévois d'ajouter un formulaire de retour d'information à l'avenir.

# Retour d'information

En parlant de retour d'information... J'ai écrit cet article pour deux raisons. La première étant de vous guider à travers le processus que j'ai suivi pour arriver au design actuel dans l'espoir que vous puissiez en tirer des leçons.

La deuxième raison est que je voulais présenter l'outil à la communauté de développement et de design car je crois qu'il peut être utile pour beaucoup de gens, et aussi pour recueillir des retours sur son état actuel.

_Ainsi, si vous avez des pensées sur le design, la fonctionnalité, le processus que j'ai suivi pour créer l'outil, ou autre chose, j'adorerais les entendre !_

# Liens

[Prototype](https://5d112084bc6f2c00097f59a7--rainbo.netlify.com/)

[Version actuelle](https://rainbo.xyz/)

[Bibliothèque de composants](https://rainbo-components.netlify.com/)

---