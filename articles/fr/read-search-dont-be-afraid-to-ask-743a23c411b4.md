---
title: Lire, Rechercher, (N'ayez pas peur de) Demander
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T23:41:20.000Z'
originalURL: https://freecodecamp.org/news/read-search-dont-be-afraid-to-ask-743a23c411b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WHsS88_D5RYVlYc5VUvNbQ.jpeg
tags:
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Lire, Rechercher, (N'ayez pas peur de) Demander
seo_desc: 'By Beth Qiang


  “As engineers and as developers, we’re paid to be frustrated…at the same time, we’re
  always in school. We’re always learning.”

  — Carlos Lazos, Episode 1 of the CodeNewbie Podcast


  Coding is a journey into ambiguity.

  Whether you’re desi...'
---

Par Beth Qiang

> « En tant qu'ingénieurs et développeurs, nous sommes payés pour être frustrés... en même temps, nous sommes toujours à l'école. Nous apprenons toujours. »

> — Carlos Lazos, [Épisode 1 du Podcast CodeNewbie](http://www.codenewbie.org/podcast/ep-1-bootcamps-water-coolers-and-hiring-devs)

Coder est un voyage dans l'ambiguïté.

Que vous conceviez une API RESTful, que vous dimensionniez une application pour des milliers d'utilisateurs, ou que vous essayiez simplement de positionner quelque chose correctement avec CSS, il y aura toujours des choses que vous ne savez pas.

La prochaine fois que vous serez bloqué et que vous ne saurez pas comment avancer, essayez la méthode « Lire-Rechercher-Demander » de Free Code Camp. Comme son nom l'indique, vous :

1. **lisez** la documentation ou l'erreur
2. **recherchez** sur Google
3. **demandez** de l'aide — sans avoir peur de demander !

Approfondissons chacun de ces points.

### Lire

Si vous savez que vous devez utiliser une certaine méthode, mais que vous ne savez pas comment l'implémenter, la documentation est un excellent point de départ. Si vous n'êtes pas sûr de la méthode dont vous avez besoin, vous pouvez souvent découvrir une solution simplement en cliquant dans la documentation.

Si vous obtenez des erreurs, lisez l'erreur ! Essayez de comprendre ce qu'elle essaie de dire. Si vous n'obtenez pas d'erreur, mais que vous ne savez pas vraiment ce qui se passe, vous pouvez essayer de déboguer via la méthode console.log().

Lorsque je construisais mes applications Free Code Camp et que je n'obtenais pas les résultats attendus, je journalisais presque tout : les instructions if, les instructions de retour de fonction, les méthodes de clic et les méthodes de timing.

Un outil utile pour cela est la console de votre navigateur. Si vous travaillez dans CodePen, il contient également une console.

Si vous suivez des blogs spécifiques (CSS Tricks en est un que je consulte souvent pour CSS), allez sur le blog et voyez s'il contient des articles pour vous aider avec les concepts qui vous posent problème.

Si vous êtes toujours bloqué, il est peut-être temps de vous tourner vers Google.

### Rechercher

Google deviendra rapidement votre meilleur ami, si ce n'est déjà fait. Mais Google peut parfois devenir cet ami ennuyeux auquel vous devez donner des coups de pouce pour obtenir des réponses utiles. Pour tirer le meilleur parti de cette amitié, il y a quelques points à garder à l'esprit.

L'un d'eux est que, souvent — surtout une fois que vous commencez à construire des applications — vous n'obtiendrez pas exactement la réponse dont vous avez besoin pour résoudre magiquement tous vos problèmes. Vous devrez généralement prendre ce que vous avez appris, puis l'appliquer à votre situation actuelle.

#### Soyez Spécifique, Soyez Concise

Une autre chose à garder à l'esprit est la manière de structurer vos recherches afin de pouvoir trouver efficacement des solutions à vos problèmes spécifiques.

Par exemple, tenter de remplacer un seul caractère à une position spécifique dans une chaîne est un problème auquel de nombreux nouveaux codeurs sont confrontés. Pour résoudre ce problème, vous pourriez rechercher de nombreuses choses sur Google.

« Je veux changer une chose dans une chaîne » donne une myriade de résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/Ctm6gLIrPoVg5PWG0rtsMlgz53K2xpjD4FZu)

Vous obtenez tout, des sous-chaînes à R en passant par « 10 façons cool d'obtenir plus de Word's Find and Replace » (que, suite à cette recherche, j'ai fini par marquer pour lire plus tard). Pas exactement ce que nous cherchons, cependant.

Lors de la recherche sur Google — surtout en ce qui concerne les problèmes de programmation — la convention que de nombreux programmeurs tendent à suivre est :

> [langage de programmation] [verbe] [mots-clés]

Essayons cela sur notre problème. Si nous entrons « javascript remplacer caractère dans chaîne », nous obtenons ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/-Bwweoa7vUoWpala0gXHLunHCchbCAseDd1c)

Cela semble beaucoup plus proche de ce que nous cherchons !

À ce stade, je cliquerai sur les premières entrées pour voir si elles sont utiles ou non. Si ce n'est pas le cas, j'essaierai de les analyser pour obtenir des mots-clés supplémentaires qui pourraient aider.

Donc, dans notre exemple, nous voulons simplement remplacer un caractère à une position spécifique, nous n'avons pas nécessairement besoin d'expressions régulières.

Le quatrième résultat de recherche est « Comment remplacer un caractère à un index particulier en JavaScript », donc je cliquerais dessus, puis je découvrirais que les chaînes sont immuables, et que vous ne pouvez pas changer un seul caractère !

Si j'ai encore des questions après cela, je pourrais ajouter « à un index » à ma recherche, et essayer d'en faire une autre.

#### Stack Overflow

Les résultats de Stack Overflow peuvent constituer une bonne partie de votre recherche Google. C'est une ressource fantastique qui contient des réponses à une énorme variété de questions de programmation. Habituellement, la personne qui a posé la question aura déjà sélectionné la réponse qui a le mieux fonctionné pour elle, et cette réponse apparaîtra en haut des résultats avec une coche verte.

Ce que je fais presque toujours, cependant, c'est parcourir toutes les réponses qui ont été publiées, y compris les commentaires. Ceux-ci contiennent parfois des discussions intéressantes, et d'autres fois des personnes disent carrément : « ceci est faux » ou « ceci est une mauvaise pratique ».

Une fois que je connais mes options et les avantages et inconvénients de chacune, je m'efforce de les implémenter.

### (N'ayez pas peur de) Demander

Lorsque vous avez cherché en rond pendant un moment et que vous n'avez rien trouvé qui fonctionne, il est peut-être temps de demander à un vrai être humain.

Les vrais êtres humains peuvent prendre toutes sortes de formes :

* vos amis (si vous avez des amis qui codent)
* des groupes de rencontre (si vous allez à des rencontres)
* d'autres campeurs sur les canaux Gitter et forums de Free Code Camp
* tout groupe Slack ou Facebook dont vous pourriez faire partie, entre autres

Avant de demander, cependant, vous devriez essayer de structurer votre question pour optimiser à la fois votre temps et le temps de la personne à qui vous demandez de l'aide.

« Mon application est cassée, que dois-je faire ? » ou « Je n'arrive pas à faire fonctionner cette fonctionnalité, que dois-je faire ? » ne sont pas très utiles pour qui que ce soit.

Comprenez le problème que vous rencontrez. Expliquez ce que vous attendez de votre code, puis comparez-le avec ce qu'il fait réellement. Expliquez ce que vous avez essayé jusqu'à présent, et incluez des extraits de code si vous pensez qu'ils aideront. (La plupart du temps, ils le feront.)

Lorsque j'ai commencé le programme, j'avais peur de poser des questions dans les forums ou les salons de discussion, pour deux raisons :

La première se résumait à la fierté : je pensais que je devrais être capable de comprendre pourquoi mon code faisait ce qu'il faisait. (« Je suis un être humain intelligent et capable. Je vais comprendre cela ! »)

La deuxième raison était l'insécurité. J'avais peur que les gens ne répondent pas, ou que personne ne veuille m'aider, ou que leur explication me dépasse, ou je ne voulais pas demander des éclaircissements et prendre encore plus de leur temps, ou... [insérez ici toutes les excuses possibles].

Je suis heureuse de dire que j'avais tort sur toutes les excuses que je pouvais imaginer. La communauté de Free Code Camp est composée de personnes très amicales, compétentes et patientes.

Une fois, quelqu'un a passé quelques heures avec moi alors que j'essayais de comprendre un concept et de trouver un bug. Il a été patient tout au long.

Je n'ai jamais eu quelqu'un qui me parle de haut ou qui pense que je suis stupide ou incapable. Je n'ai jamais eu quelqu'un qui ne répond pas à l'une de mes questions, aussi simple qu'elle ait pu paraître.

Les chances sont, si quelqu'un répond aux questions sur les forums ou dans le salon de discussion, c'est spécifiquement parce qu'il veut aider les autres !

En bonus, parfois, articuler clairement quel est votre problème vous permet de voir ce qui ne va pas. Il y a eu plusieurs fois où j'ai posé une question, pour immédiatement reconnaître ce que je devais faire ensuite. (Je remercie alors la personne, et elle répond : « Eh bien, je n'ai pas vraiment fait grand-chose... »)

### En Résumé

La méthode Lire, Rechercher, Demander consiste à optimiser votre propre temps et le temps de ceux qui vous aideraient. Elle vous encourage à apprendre et à trouver des solutions aux problèmes par vous-même avant de consulter les autres. Si vous avez essayé de le faire par vous-même et que vous n'avez pas avancé, cependant — n'ayez pas peur de demander de l'aide !

### Liens Utiles :

[Comment Commencer Lorsque Vous Êtes Bloqué](http://forum.freecodecamp.com/t/how-to-start-when-you-are-stuck/19427/4)

[Documentation JavaScript de Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

[Documentation de jQuery](http://api.jquery.com/)

[Une introduction au débogage JavaScript](http://www.w3schools.com/js/js_debugging.asp)

Le [principal salon de discussion Gitter de Free Code Camp](https://gitter.im/FreeCodeCamp/FreeCodeCamp) (il y a d'autres salons avec des objectifs plus spécifiques, comme obtenir de l'aide pour des projets front-end, ou trouver quelqu'un avec qui programmer en binôme, entre autres)

[Forum de Free Code Camp](http://forum.freecodecamp.com/)

En plus des canaux en ligne, Free Code Camp a [des rencontres et des groupes Facebook dans la plupart des grandes villes](http://forum.freecodecamp.com/t/free-code-camp-city-based-local-groups/19574/34). Je suis impliquée dans quelques-uns dans ma ville. Grâce à eux, j'ai pu rencontrer des gens, coder avec eux et trouver des gens pour aller à d'autres rencontres !