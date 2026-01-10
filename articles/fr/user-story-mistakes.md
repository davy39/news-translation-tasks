---
title: Erreurs que votre équipe pourrait commettre en rédigeant des user stories -
  et comment les corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T17:20:09.000Z'
originalURL: https://freecodecamp.org/news/user-story-mistakes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b15740569d1a4ca2997.jpg
tags:
- name: agile development
  slug: agile-development
- name: user story
  slug: user-story
seo_title: Erreurs que votre équipe pourrait commettre en rédigeant des user stories
  - et comment les corriger
seo_desc: 'By Vikash Koushik

  There''s a lot of information out there on how to write user stories and why it''s
  important. And yet, many of us make mistakes that cost us a lot.

  There are many who even prefer an alternative method. (Here’s another one.) And
  it''s o...'
---

Par Vikash Koushik

Il existe de nombreuses informations sur [comment rédiger des user stories](https://zepel.io/agile/user-stories/) et pourquoi c'est important. Pourtant, beaucoup d'entre nous commettent des erreurs qui nous coûtent cher.

Certains préfèrent même une [méthode alternative](https://jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27?ref=hackernoon.com). ([En voici une autre](https://dev.to/redfred7/enough-with-the-user-stories-already-2a8a?ref=hackernoon.com).) Et c'est souvent parce qu'ils sont frustrés par des user stories mal rédigées.

Autant il est important de savoir comment rédiger de bonnes user stories, autant il est crucial de savoir comment ne pas en écrire.

Aujourd'hui, de nombreuses équipes logicielles souhaitent adopter des processus agiles. Elles veulent placer l'utilisateur au centre de leur processus de développement produit. Et cela a tout son sens. Après tout, vous construisez le produit pour vos utilisateurs, n'est-ce pas ?

Souvent, lorsque nous rédigeons des user stories, nous pensons écrire du point de vue de l'utilisateur, mais nous finissons par les biaiser avec nos propres préjugés et connaissances. Et bien souvent, ces erreurs sont interconnectées et ne font qu'empirer avec le temps.

Dans cet article, je vais parler de certaines erreurs courantes que les équipes commettent en rédigeant des user stories.

## Des user stories trop larges

Lorsque les user stories sont trop larges, des informations cruciales concernant l'action attendue et le besoin peuvent être omises. Si vos user stories contiennent beaucoup de "_et_", "_ou_" ou "_que_", c'est un bon indicateur qu'elles sont trop larges et que vous devriez envisager de les réécrire.

De plus, il y a de fortes chances que votre user story trop large soit en réalité une [épopée](https://www.agilealliance.org/glossary/epic?ref=hackernoon.com).

Un exemple de user story trop large pourrait ressembler à ceci :

"_En tant qu'utilisateur, je souhaite continuer à lire l'article plus tard lorsque je serai sur le chemin du retour, sans avoir besoin de m'inscrire et de retrouver l'endroit exact où je me suis arrêté._"

Dans ce cas, vous pouvez voir que la user story essaie d'atteindre deux objectifs : ne pas avoir besoin de s'inscrire et ne pas avoir à retrouver où l'on a arrêté la lecture. Au lieu d'essayer de tout entasser dans une seule user story, envisagez de la décomposer en plusieurs user stories.

Voici à quoi cela pourrait ressembler après décomposition :

"_En tant qu'utilisateur, je souhaite continuer à lire l'article plus tard sans avoir à m'inscrire_"

"_En tant qu'utilisateur, je veux continuer à lire là où je me suis arrêté, afin de ne pas avoir à chercher le dernier paragraphe que j'ai lu_"

## Des user stories trop détaillées

Lorsque les user stories sont décomposées en trop de détails, vous commencez à parler de la manière dont vous allez les implémenter. Cela détourne l'attention de l'utilisateur et conduit à une mauvaise communication des attentes au sein de l'équipe.

Voici un exemple de user story trop détaillée qui parle des détails d'implémentation :

"_Définir une structure de base de données relationnelle et scalable afin de pouvoir l'utiliser pour implémenter tout cas d'utilisation futur possible._"

Quelle valeur commerciale a une excellente base de données relationnelle si l'utilisateur final ne peut pas l'utiliser ? De plus, cette user story est écrite du point de vue de l'entreprise et non de celui de l'utilisateur. Lorsque vous commencez à inclure les détails d'implémentation, les user stories ne sont plus écrites du point de vue de l'utilisateur.

## Des user stories non négociables

Les user stories ne sont pas destinées à être des descriptions spécifiques et précises d'une fonctionnalité. Par conséquent, elles ne doivent pas être gravées dans le marbre.

Voici un exemple de user story non négociable : "_En tant qu'utilisateur, je veux un bouton "Tout effacer" dans l'onglet des notifications, afin de pouvoir supprimer les anciennes notifications._"

Vous pouvez clairement voir que l'utilisateur souhaite pouvoir supprimer les anciennes notifications. Bien qu'avoir un bouton "Tout effacer" soit une solution, vous pouvez également effacer automatiquement la notification après sa lecture !

Voici un scénario classique pour vous aider à identifier si vos user stories sont trop rigides :

Parfois, une user story peut avoir été écrite d'une certaine manière, et votre équipe trouve difficile de l'implémenter parce qu'il existe une alternative plus simple.

Dans des cas comme ceux-ci, l'équipe devrait être prête à compromettre l'approche, à condition que cela ne nuise pas à la valeur que l'utilisateur en retire.

## Des user stories répétées dans les critères d'acceptation

Bien trop souvent, je remarque que les critères d'acceptation répètent la user story, mais avec des mots différents.

Voici à quoi cela ressemble :

**User story :** "_En tant qu'utilisateur, je veux ajouter des formulaires pop-up à mon blog, afin de capturer l'adresse e-mail du visiteur avant qu'il ne quitte le site._"

**Critères d'acceptation :** "_Étant donné qu'un lecteur visite un blog, lorsqu'il essaie de partir, le formulaire pop-up devrait apparaître pour lui demander de s'abonner au blog._"

Les critères d'acceptation doivent communiquer les conditions à remplir pour que la story soit marquée comme terminée. Cela garantit que vous recueillez des commentaires, aidez l'équipe à planifier et suivez leur travail. Cela rend la user story plus riche, plus précise et plus facilement testable. Et surtout, cela aligne votre équipe sur ce qu'elle est censée livrer.

Voici un meilleur exemple :

**Pour la user story :** "_En tant qu'utilisateur, je veux recevoir des notifications lorsque d'autres ajoutent des commentaires afin d'être à jour._"

**Critères d'acceptation :** "_Étant donné que j'ai l'application ouverte lorsque j'écris sur le document, l'icône de cloche devrait se mettre à jour pour afficher les notifications non lues avec un compteur._"

## Des user stories avec un utilisateur non défini

Il peut sembler ridicule de mentionner la persona de l'utilisateur dans chaque user story, encore et encore. Cependant, cela peut ajouter une valeur considérable en termes de résultat.

Cela est particulièrement important si votre produit a plus d'une persona d'utilisateur. Il y aura, bien sûr, des fonctionnalités qui seront construites spécifiquement pour différentes personas. Si vous voulez que votre équipe soit plus alignée sur le résultat que vous attendez d'elle, elle doit savoir qui sont les utilisateurs finaux et quel bénéfice ils retireront de la fonctionnalité.

Si vous cherchez un exemple pour cela, presque tous les exemples que j'ai fournis ci-dessus sont de bons exemples de ce qu'il ne faut pas faire. Ne vous inquiétez pas, c'était intentionnel pour que je puisse en parler. :)

Chaque fois que vous rédigez une user story qui commence par "_En tant qu'utilisateur..._" ou "_En tant que visiteur..._" ou "_En tant que lecteur..._", vous laissez place à l'ambiguïté. Définir clairement qui est cette personne ira loin pour donner à votre équipe le contexte dont elle a besoin.

Chez [Zepel](https://zepel.io/), nous recommandons d'écrire la persona au lieu d'utilisateur/visiteur/lecteur. Cela signifie que votre user story ressemblera à ceci :

"_En tant qu'écrivain, je veux recevoir une notification lorsque d'autres ajoutent des commentaires dans l'application Google Docs, afin de ne pas avoir à actualiser la page sans cesse._"

## Des user stories avec un mauvais contexte

Bien trop souvent, nous finissons par rédiger des user stories juste pour la forme. Après un certain point, presque toutes les user stories commencent à se ressembler.

Voici un exemple : "_En tant que gestionnaire de contenu, je veux un éditeur de texte afin de pouvoir éditer du texte._"

Tout ce que cela dit à votre équipe, c'est que vous voulez qu'ils construisent un éditeur de texte et rien d'autre. Si vous avez écrit un tas de user stories depuis un moment, il est préférable de faire une pause et de les revisiter avec un regard neuf.

Parfois, même après une pause, vous pourriez ne pas être en mesure de trouver quelque chose de plus significatif. Cela peut être un bon indicateur que vous devez parler davantage à vos utilisateurs et mieux comprendre leurs besoins. Il n'y a vraiment aucun intérêt à essayer de le sortir de votre cerveau.

## Conclusion

Bien qu'utiliser un modèle de user story puisse être utile, ce n'est jamais aussi simple que de remplir un formulaire à trous dans votre outil agile.

Parce qu'une erreur lors de la rédaction de user stories conduit souvent à une série d'autres erreurs comme sous-produit. Et même si vous parvenez à rédiger correctement des user stories, ce n'est que le début. Vous devriez toujours permettre à votre équipe d'analyser les stories - d'un point de vue technique - pour les aider à estimer et créer les prochaines étapes nécessaires.