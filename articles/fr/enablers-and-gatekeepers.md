---
title: La Valeur des Facilitateurs et des Gardiens dans les Équipes de Développement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-20T13:20:00.000Z'
originalURL: https://freecodecamp.org/news/enablers-and-gatekeepers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b8f740569d1a4ca2c97.jpg
tags:
- name: teamwork
  slug: teamwork
seo_title: La Valeur des Facilitateurs et des Gardiens dans les Équipes de Développement
seo_desc: "By Ovidiu Bute\nTeams should set and uphold a set of values. These come\
  \ in different shapes and forms. Whether it’s being honest, transparent, responsible,\
  \ or blameless. The list just goes on. \nValues are only important if they’re connected\
  \ to behavio..."
---

Par Ovidiu Bute

Les équipes devraient établir et respecter un ensemble de **valeurs**. Celles-ci prennent différentes formes. Qu'il s'agisse d'être honnête, transparent, responsable ou sans reproche. La liste est longue.

Les valeurs ne sont importantes que si elles sont liées à des comportements, c'est-à-dire à la manière dont vous agissez habituellement, quelle que soit la situation. Personne ne se comporte de manière erratique sur une période prolongée. Après suffisamment de réflexion, des schémas émergent, et ces schémas peuvent être associés à des valeurs. Je souhaite me concentrer sur deux d'entre elles dans cet article.

## Les Facilitateurs

Tout au long de ma carrière d'ingénieur logiciel, j'ai souvent entendu le terme **facilitation**. Tout d'abord, permettre à quelqu'un de faire quelque chose peut avoir des connotations à la fois positives et négatives. Je pense que c'est seulement dans cette industrie qu'il est acceptable de dire que vous allez faciliter le travail de quelqu'un. Dans tout autre contexte, vous recevriez des regards étranges rien que pour le dire.

Alors, qu'y a-t-il de spécial dans une équipe de facilitation ? Cela signifie généralement développer et maintenir des composants dont d'autres équipes peuvent bénéficier.

Si vous livrez des logiciels à des clients, vous dépendez probablement d'un système d'intégration continue. S'il tombe en panne, vous êtes pratiquement bloqué. Donc, quelqu'un, ou une équipe de personnes, doit le maintenir et le faire fonctionner presque 24h/24 et 7j/7.

Pouvez-vous imaginer votre entreprise livrer sans votre système CI ? Si ce n'est pas le cas, alors l'équipe qui le possède vous **permet** de faire votre travail.

## Les Gardiens

**Garde** est un terme que vous n'entendez pas souvent. Un gardien est quelqu'un dont le travail est de ne laisser personne entrer dans ce qu'il protège.

L'équipe CI est responsable de sa disponibilité, ils le mettent à jour de temps en temps, implémentent de nouvelles fonctionnalités, corrigent des bugs, appliquent des correctifs de sécurité, etc. Étant donné que tout le monde dans l'entreprise dépend de leur travail, il est naturel de s'attendre à ce qu'ils aient toujours beaucoup de travail planifié devant eux. Il est courant dans de nombreuses entreprises que des développeurs d'autres équipes soient intéressés à les aider même si ce n'est pas exactement leur travail.

## Devez-vous être un facilitateur ou un gardien ?

Imaginez que vous êtes passionné par les systèmes CI et que vous remarquez un problème avec la configuration de votre entreprise. C'est quelque chose que vous savez comment corriger, alors vous décidez de le faire.

Après avoir préparé votre correctif pour soumission, il y a vraiment deux scénarios différents qui pourraient se produire, et ils ont à voir avec les valeurs. Voyons comment les prochaines étapes se dérouleraient avec deux équipes totalement différentes, A et B, qui défendent des valeurs différentes.

Vous parlez à l'équipe A et ils acceptent de revoir votre correctif. Ils suggèrent des améliorations basées sur leur expérience et travaillent avec vous pour le livrer. Vous gagnez plus d'informations sur ce que signifie vraiment faire partie de l'équipe.

Vous avez manqué un cas limite et ils vous le font remarquer. Vous retournez le corriger et le resoumettez, et votre correctif est finalement accepté. Ils vous informent également de ce qui est prévu dans les mois à venir au cas où vous trouveriez d'autres problèmes.

Vous envoyez votre correctif à l'équipe B. Vous n'entendez rien pendant quelques jours et décidez de les contacter en personne. Ils vous disent qu'ils sont débordés de travail et n'ont pas le temps de regarder votre proposition.

Vous continuez à essayer de les convaincre que c'est une petite correction qui améliore grandement l'expérience des développeurs, mais ils ne veulent pas en entendre parler et vous disent finalement que ce n'est pas votre travail de penser au CI. Vous abandonnez et retournez travailler. Six mois plus tard, ils corrigent le problème, mais vous ne l'apprenez que par hasard.

L'équipe B est ce que j'appellerais une équipe de **gardiens**, même si leur mission officielle est de faciliter, tout comme l'équipe A. Ils ne laissent pas les gens entrer s'ils n'y sont pas obligés. Cette équipe bénéficie rarement de l'expertise des outsiders. C'est un peu comme comparer le propriétaire à l'open source.

Mais bien que je sois sûr que vous préféreriez interagir avec la première équipe, il peut être utile de considérer leur perspective avant de porter un jugement.

Il est clair que l'équipe A valorise le travail d'équipe. Si vous apportez une amélioration, ils prendront le temps de la revoir, de vous faire savoir s'ils prévoyaient déjà de faire la même chose, ou de pointer les défauts de votre solution.

L'équipe B suppose que puisque vous n'êtes pas dans l'équipe, vous n'avez vraiment pas à vous soucier de leur domaine de travail et vous ne devriez même pas essayer. Mais le comportement de l'équipe B est-il _objectivement_ mauvais ? Comme dans toutes les choses liées au logiciel, cela dépend.

Et si l'équipe B maintenait un composant logiciel critique pour une banque ? Si vous étiez à leur place, seriez-vous si enthousiaste à l'idée de laisser des contributeurs externes entrer ? Et si votre amélioration contenait un bug ? Si cela arrive, ce n'est pas votre responsabilité, vous n'êtes pas dans l'équipe. Ce sont eux qui doivent le corriger.

Ou peut-être que leur logiciel est si complexe qu'il est impossible pour quiconque à l'extérieur de contribuer sans un long processus d'intégration.

Vous devriez également sérieusement considérer que l'équipe A doit **allouer du temps** pour travailler avec vous, donc ils font le choix que vous valez l'investissement. Si votre amélioration potentielle se révèle être un fardeau à l'avenir, alors ils ne récupéreront pas ce temps. Il est perdu.

En revanche, l'équipe B est plus draconienne avec leur temps. Ils se considèrent (peut-être à juste titre) comme des experts dans leur domaine, et leur hypothèse est que, sauf si vous êtes dans l'équipe, vous n'avez pas assez de contexte pour suggérer des améliorations. Vous ne devriez signaler que les problèmes à eux et ils s'en occuperont éventuellement.

Ce sont certainement des positions extrêmes et je les ai rendues ainsi pour qu'il soit plus facile de les conceptualiser. En réalité, les équipes sont à la fois des facilitateurs et des gardiens, selon la situation. Mais les valeurs prévalent toujours, et il est important de comprendre cela lorsque vous devez travailler avec d'autres équipes.