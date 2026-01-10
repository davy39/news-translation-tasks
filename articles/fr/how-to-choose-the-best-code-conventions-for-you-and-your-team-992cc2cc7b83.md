---
title: Comment choisir les meilleures conventions de code pour vous et votre équipe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T21:30:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-best-code-conventions-for-you-and-your-team-992cc2cc7b83
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OcAtcYPz7bzbXr40
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment choisir les meilleures conventions de code pour vous et votre équipe
seo_desc: 'By Ofer Vugman

  Put an end to the never-ending debate


  _Photo by [Unsplash](https://unsplash.com/@johnjac?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">John Jackson on <a href="https://unsplash.com?utm_source=medium&ut...'
---

Par Ofer Vugman

#### **Mettez fin au débat sans fin**

![Image](https://cdn-media-1.freecodecamp.org/images/1n2grhWszDdGlSdNlQCg75q4JI6fUIk9Uu6t)
_Photo par [Unsplash](https://unsplash.com/@johnjac?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">John Jackson</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

_- "Écoute, ces variables privées devraient aller après les publiques !"_  
_- "Pas question ! Les variables publiques vont avant les privées !"_  
_- "Demandons à Deb, et laissons-la décider"_  
_- "Attendez, pourquoi ces constantes ne sont-elles pas en camelCase ?"_

👨‍♂️ 👩‍♀️

Levez la main si vous vous êtes déjà retrouvé dans ce genre de discussion. Bon, ne la levez pas vraiment, mais quelque chose me dit que certains d'entre vous ont peut-être participé à ce scénario une ou deux fois.

En tant que développeur depuis une décennie, je me suis retrouvé dans plusieurs discussions, certains pourraient dire trop nombreuses, sur les conventions de code. Ces discussions, aussi utiles soient-elles, dégénèrent parfois en divagations philosophiques sans fin. Et puis elles commencent à aborder des sujets allant de l'indentation à la structure des dossiers.

Cela peut être douloureux.

Alors, comment décidez-vous vraiment quelle est la meilleure convention, et mieux encore, les meilleures conventions existent-elles ? Je vais tout expliquer ici, afin que vous puissiez mettre fin à ces divagations philosophiques, une fois pour toutes.

### Alors pourquoi avons-nous même besoin de conventions ?

Afin de déterminer quelle est la meilleure convention et si elles existent même, nous devons d'abord comprendre _pourquoi_ nous avons même besoin de conventions.

Il y a plus d'une raison, mais je vais me concentrer sur la plus importante : **la lisibilité**.

Et si je décidais de passer à l'écriture en majuscules uniquement. COMME CI, CE QUI PEUT SEMBLER ÉTRANGE. Vous le remarquez immédiatement, et votre cerveau commence à traiter ce qui est différent.

Prenez cet exemple simple, et pensez au nom des variables ou à l'indentation. Si chaque fois que vous revenez au code et qu'il est écrit différemment, ce serait comme si vous recommenciez à zéro. Mais lorsque vous codez avec des conventions, votre code est plus facile à comprendre, et donc lisible, même s'il a été écrit il y a des mois.

Cela devient encore plus crucial lorsque vous travaillez au sein d'une équipe de développeurs, où chacun écrit son propre code avec sa convention préférée. Le temps passé à comprendre et à réviser le code de chacun prendra... eh bien... vous voyez le point.

**Afin de collaborer avec d'autres développeurs de manière efficace et qualitative, vous devez avoir une convention commune.**

> "Les programmes doivent être écrits pour que les gens les lisent, et seulement accessoirement pour que les machines les exécutent." — Hal Abelson

### Comment choisir la meilleure convention de code

Que vous veniez de commencer à coder, que vous fassiez partie d'une équipe de développeurs géniale, ou que vous veniez de devenir CTO, comment choisissez-vous vos conventions de code ?

Voici mon guide pour choisir la meilleure convention de code :

1. **Inspirez-vous des équipes de développeurs que vous admirez** : Rien ne vaut l'expérience, et certaines des plus grandes et des plus intelligentes entreprises publient leurs directives de codage. Par exemple, Airbnb a publié leurs guides de style [javascript](https://github.com/airbnb/javascript) et [ruby](https://github.com/airbnb/ruby), et Google a publié leurs propres guides de style [Java](https://google.github.io/styleguide/javaguide.html) et [Python](https://google.github.io/styleguide/pyguide.html). Que vous aimiez ces entreprises ou non, si vous additionnez les années d'expérience de chacun de leurs développeurs, cela fait des milliards. Essayez d'appliquer certains de ces guides de style d'entreprises à votre propre équipe.
2. **Collectez les connaissances de vos pairs** : Nous avons de la chance de faire partie d'une communauté aussi dynamique. En fait, l'un des plus grands avantages d'être développeur aujourd'hui est notre communauté. Que ce soit sur [Slack](http://slack.com), [Spectrum](https://spectrum.chat/), [Discord](https://discordapp.com/), ou toute autre plateforme de collaboration, vous pouvez toujours trouver des groupes compétents pour poser une question sur les conventions de code et obtenir des réponses de développeurs du monde entier, instantanément.
3. **Ignorez les exemples de code.** Oui, ignorez-les simplement. De temps en temps, je tombe sur du code qui a été copié/collé d'une réponse sur [Stackoverflow](https://stackoverflow.com/), ou quelque chose de similaire. Ce que les gens oublient parfois, c'est que les exemples de code qu'ils viennent de copier ont probablement été écrits comme réponse à une question technique, ou comme explication pour une bibliothèque. Dans la plupart des cas, l'auteur n'avait pas l'intention de, ni le temps de s'occuper des conventions de code.

Ces conseils devraient vous aider à commencer et peuvent poser les bases pour introduire des conventions de code pour votre équipe de développeurs.

Et maintenant, un peu de philosophie.

### Les "meilleures" conventions existent-elles ?

Cela dépend de ce que signifie "meilleures". Si Airbnb ou Google utilisent une certaine convention, ou si 10 différents CTO vous ont dit que leur convention est la meilleure — cela signifie-t-il que c'est la meilleure convention pour vous ?

De plus, les conventions sont sujettes à changement. Peut-on nommer "meilleure" quelque chose qui change avec le temps ?

Lorsque j'ai commencé chez [Lemonade](https://www.lemonade.com/) en tant que seul développeur front-end, j'ai trouvé difficile de lire le code écrit par le développeur précédent. Cela aurait pu être la meilleure convention pour lui, mais pas pour moi. J'ai donc réécrit chaque morceau de code sur lequel j'ai travaillé en utilisant mes conventions. Avec le temps, d'autres développeurs ont rejoint l'équipe et nos conventions ont évolué.

Chaque développeur venait d'un milieu différent, avec des normes et des conventions différentes. Pour formaliser nos conventions, nous avons utilisé le guide de style javascript d'Airbnb comme point de départ. Nous avons examiné les conventions de ce guide et changé ou supprimé celles avec lesquelles nous n'étions pas d'accord, et adopté celles que nous aimions. Nous avons même adopté des conventions que les développeurs ont apportées de leur propre expérience, et les avons intégrées dans notre convention principale.

Le processus d'évaluation de chaque convention et de décision sur son adoption n'a pas seulement amélioré la lisibilité de notre code, mais a également amélioré notre travail d'équipe. (Plus sur cela dans un futur article !)

Voici la vérité : **il n'existe pas de définition universelle pour les meilleures conventions, car elles n'existent tout simplement pas.**

![Image](https://cdn-media-1.freecodecamp.org/images/TMEHrum5-VFAoJBR5yPJgrZpevkRgXRtCvc3)

Contrairement à ce qu'on vous a appris à l'école, il n'y a pas toujours une seule bonne réponse à chaque question. Dans ce cas, il peut y en avoir beaucoup.

Les développeurs ont différentes façons d'implémenter des choses différentes ou même identiques. Certains d'entre nous préfèrent que tous les noms de membres de classe commencent par un préfixe 'm_'. Certains aiment utiliser des indentations de deux espaces, d'autres préfèrent les tabulations, certains pourraient dire que l'utilisation du mot `Utils` dans un nom de classe est incorrecte. Minus, cette discussion est sans fin, mais toutes ces préférences viennent avec une bonne raison.

À la fin de la journée, tout se résume à la convention qui améliore la lisibilité de votre code. Celle qui permet à votre équipe de mieux communiquer, d'avancer plus rapidement et avec une meilleure efficacité.

Rappelez-vous, les conventions de code ne sont que des suggestions. Oui, une fois que vous avez décidé d'une convention à utiliser, vous devez la suivre. Mais rappelez-vous : elles ne sont pas gravées dans la pierre et sont sujettes à changement. Permettez-vous d'expérimenter avec différentes conventions jusqu'à ce que vous trouviez celle qui vous convient le mieux, à vous et à votre équipe.

Alors, quelles sont les meilleures conventions de code ? Facile - les vôtres !