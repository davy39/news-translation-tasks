---
title: Comment éviter les pièges de la revue de code qui ralentissent votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-06T18:36:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-code-review-pitfalls-that-slow-your-productivity-down-b7a8536c4d3b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_9ClYv6zGLGlJJpg
tags:
- name: code review
  slug: code-review
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment éviter les pièges de la revue de code qui ralentissent votre productivité
seo_desc: 'By Michaela Greiler

  Code reviewing is an engineering practice used by many high performing teams. And
  even though this software practice has many advantages, teams doing code reviews
  also encounter quite a few code review pitfalls.

  In this article, I...'
---

Par Michaela Greiler

La revue de code est une pratique d'ingénierie utilisée par de nombreuses équipes performantes. Et même si cette pratique logicielle présente de nombreux avantages, les équipes effectuant des revues de code rencontrent également quelques pièges.

Dans cet article, je vous explique les principaux pièges de la revue de code dont vous devez être conscient pour vous assurer que la revue de code ne ralentit pas votre équipe. Connaître les pièges et problèmes qui peuvent survenir peut vous aider à garantir une expérience de revue de code productive et efficace. Ces résultats sont basés sur une [enquête que nous avons menée chez Microsoft avec plus de 900 participants](https://www.michaelagreiler.com/wp-content/uploads/2019/03/Code-Reviewing-in-the-Trenches-Understanding-Challenges-Best-Practices-and-Tool-Needs.pdf).

### Un processus typique de revue de code

Un processus typique de revue de code basé sur des outils ressemble à peu près à ceci : une fois que le développeur a terminé un morceau de code, il prépare le code pour qu'il soit soumis à une revue. Ensuite, il sélectionne des relecteurs qui sont informés de la revue. Les relecteurs examinent alors le code et donnent des commentaires. L'auteur du code travaille sur ces commentaires et améliore et modifie le code en conséquence. Une fois que tout le monde est satisfait, ou qu'un accord est atteint, le code peut être intégré dans la base de code.

Dans un autre article, j'ai décrit à quoi ressemble [un processus typique de revue de code chez Microsoft.](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/)

### La revue de code n'est pas toujours un processus fluide

Ces étapes semblent décrire un processus fluide. Mais, comme pour tout, en pratique, les choses ont tendance à être plus compliquées que prévu. Lors du processus de revue de code, il y a plusieurs pièges qui peuvent réduire l'expérience positive des revues de code pour toute l'équipe. Si elle n'est pas effectuée correctement, la revue de code peut également avoir un impact sur la productivité de toute l'équipe. Alors, examinons les difficultés et les pièges des revues de code.

Les deux principaux types de pièges de la revue de code concernent le temps passé sur les revues de code et la valeur que les revues de code apportent.

[Soyez conscient des pièges de la revue de code. Sinon, les revues de code peuvent ralentir votre équipe. Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=Be%20aware%20of%20code%20review%20pitfalls.%20Otherwise%2C%20code%20reviews%20can%20slow%20your%20team%20down.%20&via=mgreiler&related=mgreiler)

### Attendre les commentaires de la revue de code est pénible

L'un des principaux pièges auxquels sont confrontés les auteurs de code est de recevoir des commentaires en temps opportun. Attendre que les commentaires arrivent et ne pas pouvoir travailler sur le code entre-temps peut être un énorme problème. Même si les développeurs peuvent prendre d'autres tâches à effectuer, si la revue de code prend trop de temps, cela impacte la productivité du développeur et aussi la satisfaction du développeur.

Mais, pourquoi les commentaires de la revue de code prennent-ils autant de temps ?

### Les développeurs doivent jongler avec plusieurs responsabilités

Eh bien, la revue de code n'est pas la seule tâche que le relecteur de code doit effectuer. Au contraire, la revue de code — même si elle peut prendre une partie significative du temps de travail quotidien d'un développeur — n'est qu'une partie des responsabilités et des tâches d'un développeur. Il est donc très probable que le relecteur de code soit engagé dans d'autres activités et doive les arrêter ou les terminer avant de regarder la revue de code.

Si le timing n'est pas idéal, et surtout si le relecteur de code n'a pas anticipé ce changement, il est probable qu'il faille un certain temps avant qu'il ne regarde la revue. Les équipes à distance doivent également être conscientes des différences de fuseaux horaires. Sinon, les revues de code pourraient même prendre plus de temps.

### Les développeurs rencontrent des problèmes si les revues de code ne sont pas comptabilisées comme du travail réel

Les contraintes de temps sont réelles et elles affectent à la fois le relecteur de code et l'auteur du code. Faire une revue de code correcte prend du temps. Si les équipes veulent que les développeurs fassent des revues de code mais ne valorisent pas ou ne comptabilisent pas le temps que les développeurs passent sur les revues de code, cela devient un vrai problème.

![Image](https://cdn-media-1.freecodecamp.org/images/iO9crhcrMsfcZYZnlcTayHSfN647zOBnmRQs)
_Vous devez valoriser et planifier le temps passé à faire des revues de code.<br>Photo par [Unsplash](https://unsplash.com/photos/vcPtHBqHnKk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">freestocks.org</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

[Vous ne pouvez pas attendre des revues de code de qualité si vous ne valorisez pas le temps qu'un développeur y passe. Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=You%20can%27t%20expect%20quality%20code%20reviews%2C%20if%20you%20don%27t%20value%20the%20time%20a%20developer%20spends%20on%20them.&via=mgreiler&related=mgreiler)

### Ne pas récompenser les efforts et la performance de la revue de code

Il ne sert à rien de prétendre valoriser les revues de code si vous ne récompensez pas les efforts que les développeurs y consacrent. De nombreuses entreprises se concentrent sur la récompense des développeurs pour la quantité de code qu'ils écrivent ou les fonctionnalités qu'ils développent. Cela diminue la motivation et la capacité des développeurs à bien faire leur travail en s'entraidant (ce qui inclut la revue de code). Les efforts et la performance de la revue de code devraient être une pierre angulaire pour l'évaluation des performances ou les décisions de promotion.

[Si vous voulez que votre équipe fasse bien les revues de code, récompensez-les pour leur travail. Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=If%20you%20want%20your%20team%20to%20do%20code%20reviews%20well%2C%20reward%20them%20for%20their%20work.%20&via=mgreiler&related=mgreiler)

### Facteurs sociaux et dynamique d'équipe

Mais attendre une revue de code n'a pas toujours à voir avec le manque de temps ou un système de récompense manquant. En raison de son caractère social, les revues retardées peuvent être dues à des insécurités ou à la dynamique d'équipe. Surtout si la revue de code est écrasante, ou si le relecteur est nouveau dans le code, faire une revue de code peut être écrasant :

> _On s'attend à ce que je participe, mais je ne suis pas tout à fait sûr de comment faire. J'attendrai qu'une autre personne commence. — participant à l'étude_

### Les grandes revues sont difficiles à examiner

Un autre piège significatif de la revue de code est les grandes revues. Imaginez que vous êtes le relecteur, et que vous venez de recevoir cette revue. Vous pensez, bien, je vais rapidement regarder cela, mais une fois que vous ouvrez la revue, vous voyez ce grand changement de code. Plusieurs fichiers ont été modifiés, et toutes les modifications s'entremêlent dans la base de code. Quelle est votre première réaction ?

Probablement : waouh !

C'est exact. C'est exactement ce que nous avons vu en analysant des milliers de revues de code. Non seulement le temps de revue augmente avec la taille du changement de code, mais la qualité des commentaires diminue également. Eh bien, c'est probablement compréhensible.

> _10 lignes de code = 10 problèmes._

> _500 lignes de code = « ça a l'air bien. »_

> _Revues de code._

> _— I Am Devloper (@iamdevloper) [5 novembre 2013](https://twitter.com/iamdevloper/status/397664295875805184?ref_src=twsrc%5Etfw)_

Les grands changements de code sont tout simplement incroyablement difficiles à examiner. Si, en plus, le relecteur de code n'est pas très familier avec la partie de la base de code où le changement a eu lieu, la revue peut rapidement devenir un cauchemar.

[Les grandes revues de code sont difficiles à examiner. La qualité de la revue diminue avec la taille du changement, limitant ainsi la valeur que les équipes tirent des revues de code. Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=Large%20code%20reviews%20are%20hard%20to%20review.%20The%20quality%20of%20the%20review%20decreases%20with%20the%20size%20of%20the%20change%2C%20thus%20limiting%20the%20value%20teams%20get%20out%20of%20from%20code%20reviews.%20&via=mgreiler&related=mgreiler)

### Comprendre les changements de code nécessite quelques conseils

Comprendre les changements de code, et surtout la motivation d'un changement de code, est un autre piège de la revue de code auquel de nombreux relecteurs sont confrontés. Si aucune description n'explique le but du changement, la revue de code devient beaucoup plus difficile. Nous avons vu dans l'étude que si le relecteur de code ne comprend pas le changement de code, ou s'il est submergé par la quantité de changements, il ne peut pas donner de commentaires perspicaces.

> _C'est juste ce grand désordre incompréhensible. Ensuite, vous ne pouvez pas ajouter de valeur parce qu'ils vont juste vous l'expliquer et vous allez répéter ce qu'ils disent._

> _— développeur interviewé13_

### Ne pas recevoir de commentaires précieux diminue les bénéfices et la motivation des développeurs pour les revues de code

Sans aucun doute, passer du temps sur des revues de code et ne pas recevoir de commentaires utiles en retour est un problème. Même si l'équipe peut encore bénéficier du transfert de connaissances, la motivation du développeur à faire des revues de code et les bénéfices des revues de code diminuent lorsqu'ils ne reçoivent pas de commentaires précieux.

Il y a plusieurs raisons pour lesquelles les relecteurs ne donnent pas ou ne peuvent pas donner de commentaires perspicaces. Il se peut que le relecteur de code n'ait pas eu l'expertise nécessaire. Une autre raison courante est que le relecteur n'a pas eu assez de temps pour examiner minutieusement le changement.

Peut-être que le relecteur de code ne comprend pas le code. Il se peut également que le relecteur de code ne sache pas quels problèmes rechercher. [Comprendre ce qui fait la valeur des commentaires de revue de code](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/boosting-code-reviews-useful-comments) et mettre en œuvre les meilleures pratiques atténue ce piège.

### Une fois que la discussion principale porte sur le style, vous devez agir

Un autre problème qui peut survenir lors d'une revue de code s'appelle le « bikeshedding ». Le bikeshedding signifie que les développeurs se concentrent sur des problèmes mineurs et commencent à discuter de problèmes mineurs et négligent les problèmes sérieux.

Les raisons en sont multiples. Les défis courants en coulisses qui conduisent au bikeshedding sont que les développeurs ne comprennent pas le changement de code ou qu'ils n'ont pas assez de temps pour les revues de code. Parfois, le bikeshedding peut être un signe qu'il y a des problèmes avec la dynamique d'équipe.

[Si les gens discutent de problèmes mineurs lors des revues de code, vous devez examiner le problème sous-jacent. Pression du temps, revues trop grandes, rivalité ? Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=If%20people%20dispute%20about%20minor%20issues%20during%20code%20reviews%2C%20you%20have%20to%20take%20a%20look%20at%20the%20underlying%20issue.%20Time%20pressure%2C%20too%20large%20reviews%2C%20rivalry%3F%20&via=mgreiler&related=mgreiler)

### Atteindre un consensus peut nécessiter une discussion en face à face

Parfois, il peut arriver qu'il soit difficile d'atteindre un consensus. Cela peut se produire entre le relecteur de code et l'auteur du code, ou également entre plusieurs relecteurs de code directement. De telles situations doivent être traitées avec soin car la dynamique d'équipe est étroitement liée à ces événements. La communication via des outils et sous forme écrite peut aggraver ce problème. Si une tension semble exister, ou si des questions contentieuses doivent être discutées, passer à une discussion en face à face (soit en personne, soit via un appel vidéo) peut être une bonne idée.

### Les avantages de la revue de code l'emportent sur les efforts

J'espère que cette liste de pièges de la revue de code n'a pas changé votre avis sur les revues de code. Parce que, la bonne nouvelle est que si vous êtes conscient des pièges de la revue de code et que vous les contrariez, les revues de code sont une technique d'ingénierie très bénéfique. Et, il existe même d'autres moyens éprouvés de travailler efficacement avec les revues de code.

### Bonnes pratiques de revue de code

Dans le prochain article de [cette série sur la revue de code](https://www.michaelagreiler.com/code-review-blog-post-series/), je présente les meilleures pratiques pour aider à minimiser les pièges et les défis de la revue de code et garantir que votre équipe tire le meilleur parti de la pratique de la revue de code. Alors continuez à lire. Pour être informé lorsque je publierai le prochain article, suivez-moi sur [twitter](https://twitter.com/mgreiler).

J'ai préparé un e-Book exclusif sur la revue de code pour les abonnés à ma newsletter. Alors assurez-vous de [vous abonner à ma liste de diffusion](https://www.michaelagreiler.com/code-review-e-book/) et sécurisez votre e-Book sur la revue de code incluant une feuille de triche pratique des meilleures pratiques de revue de code.

_Publié à l'origine sur [https://www.michaelagreiler.com](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) le 6 avril 2019._