---
title: Une comparaison réelle des frameworks front-end avec des benchmarks (mise à
  jour 2019)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T14:01:11.000Z'
originalURL: https://freecodecamp.org/news/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9M_Anr2z0eC8AT0adn52Nw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une comparaison réelle des frameworks front-end avec des benchmarks (mise
  à jour 2019)
seo_desc: 'By Jacek Schae

  Also available in:Turkish — thanks to @erdenizZz,Portugues — thanks to @felipefialho

  For the third time, we are comparing Front-End frameworks by using the Real World
  example apps. RealWorld example app gives us:

  RealWorld AppSomething...'
---

Par Jacek Schae

Également disponible en : 
[Turc](https://medium.com/@erdenizZz/front-end-frameworklerinin-ger%C3%A7ek-bir-kar%C5%9F%C4%B1la%C5%9Ft%C4%B1r%C4%B1lmas%C4%B1-2019-9f417c1c9261)  grâce à [@erdenizZz,](https://medium.com/@erdenizZz) 
[Portugais](https://medium.com/@felipefialho/front-end-frameworks-compara%C3%A7%C3%A3o-realword-com-benchmarks-vers%C3%A3o-2019-ed1024ee3cba)  grâce à [@felipefialho](http://twitter.com/felipefialho)

Pour la troisième fois, nous comparons les frameworks front-end en utilisant les [applications exemples Real World](https://github.com/gothinkster/realworld). L'application exemple RealWorld nous offre :

**Application RealWorld** 
Quelque chose de plus qu'un "todo". Habituellement, les "todos" ne transmettent pas assez de connaissances et de perspective pour construire des applications *réelles*.

**Standardisée** 
Un projet qui respecte certaines règles. Fournit une API back-end, un balisage statique, des styles et une spécification.

**Écrit ou révisé par un expert** 
Un projet réel et cohérent, que, idéalement, un expert de cette technologie aurait construit ou révisé.

### Quelles bibliothèques/frameworks comparons-nous ?

Au moment de l'écriture, il existe 18 implémentations de Conduit dans le [dépôt d'applications exemples RealWorld](https://github.com/gothinkster/realworld).

**Peu importe qu'il ait un grand nombre de followers ou non. La seule qualification est qu'il apparaisse sur la page du dépôt RealWorld.**

![Image](https://cdn-media-1.freecodecamp.org/images/mxmA13gZ63sf7YgfD2ZKaotbT5SDY9mXt9CD align="left")

*Frontends dans le dépôt* [*Real World*](https://github.com/gothinkster/realworld) *(Mars 2019)*

### Quelles métriques examinons-nous ?

#### **Performance**

Combien de temps cette application met-elle à afficher du contenu et à devenir utilisable ?

#### **Taille**

Quelle est la taille de l'application ? Nous ne comparerons que la taille du ou des fichiers JavaScript compilés. Le CSS est commun à toutes les variantes et est téléchargé depuis un CDN (Content Delivery Network). Le HTML est également commun à toutes les variantes. Toutes les technologies compilent ou transpilent vers JavaScript, nous ne mesurons donc que ce(s) fichier(s).

#### **Lignes de code**

Combien de lignes de code l'auteur a-t-il nécessaires pour créer l'application RealWorld selon la spécification ? Pour être équitable, certaines applications ont un peu plus de fonctionnalités, mais cela ne devrait pas avoir un impact significatif. Le seul dossier que nous quantifions est `src/` dans chaque application.

### Métrique #1 : Performance

Nous vérifierons le score de performance de l'[Audit Lighthouse](https://developers.google.com/web/tools/lighthouse/) intégré à Chrome. Lighthouse retourne un score de performance compris entre 0 et 100. 0 est le score le plus bas possible.

#### Paramètres de l'audit

![Image](https://cdn-media-1.freecodecamp.org/images/itrdsyHI0H0Jb0KJ5UJerNjzWqD9y53yBzzo align="left")

*Paramètres de l'audit Lighthouse pour toutes les applications testées*

La performance est un score combiné des métriques suivantes :

* First Contentful Paint

* First Meaningful Paint

* Speed Index

* First CPU Idle

* Time to Interactive

* Estimated Input Latency

Pour plus de détails, consultez le [Guide de notation Lighthouse](https://developers.google.com/web/tools/lighthouse/v3/scoring).

#### Performance TL;DR

Plus vous affichez rapidement et plus quelqu'un peut faire quelque chose rapidement, meilleure est l'expérience pour la personne qui utilise l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/atCnTzcBrZlj9WK-GtZdKHSilk8O8LoBN7UD align="left")

*Performance (points 0100)  plus c'est élevé, mieux c'est.*

*Note : PureScript a été ignoré en raison de l'absence d'application de démonstration.*

#### Conclusion

La plupart des applications obtiennent un score supérieur à 90. Vous ne ressentirez probablement pas une grande différence en termes de performance.

### Métrique #2 : Taille

La taille de transfert provient de l'onglet réseau de Chrome. En-têtes de réponse GZIPés plus le corps de la réponse, tels que livrés par le serveur.

Cela dépend de la taille de votre framework ainsi que des dépendances supplémentaires que vous avez ajoutées, et de la capacité de votre outil de construction à éliminer le code inutilisé de votre bundle.

#### Taille TL;DR

Plus le fichier est petit, plus le téléchargement est rapide et moins il y a à analyser.

![Image](https://cdn-media-1.freecodecamp.org/images/DRmH8Fz15DLxXguz9d8NR0eVanX0U9xW9jom align="left")

*Taille de transfert en KB  moins c'est mieux*

#### Conclusion

Il se passe beaucoup de choses sensationnelles dans ce domaine. Svelte  Le framework UI magique qui disparaît  tient vraiment sa promesse. Stencil est le nouveau venu dans ce benchmark et performe également assez bien. Tous deux sont relativement nouveaux et repoussent les limites de ce qui est possible en termes de taille.

### Métrique #3 : Lignes de code

En utilisant [cloc](https://github.com/AlDanial/cloc), nous comptons les lignes de code dans le dossier src de chaque dépôt. Les lignes vides et les commentaires ne font **pas** partie de ce calcul. Pourquoi est-ce significatif ?

> Si le débogage est le processus de suppression des bugs logiciels, alors la programmation doit être le processus de les mettre en place  Edsger Dijkstra

#### Lignes de code TL;DR

Cela montre à quel point une bibliothèque/framework/langage donné est concis. Combien de lignes de code avez-vous besoin pour implémenter presque la même application (certaines ont un peu plus de fonctionnalités) selon la spécification.

![Image](https://cdn-media-1.freecodecamp.org/images/Y7vQUAUrMzGi8l3K2VZujbrZYqAIPfKwYXZj align="left")

*\# lignes de code  moins c'est mieux*

*Note Imba : Imba a été ignoré car* [*cloc*](https://github.com/AlDanial/cloc) *ne peut pas traiter les fichiers* `.imba`.

*Note Elm : Les développeurs Elm écrivent le code un peu plus verticalement, d'où le nombre élevé de LoC  au moins c'est ce qu'*[*on m'a dit*](https://twitter.com/rtfeldman/status/983384187116949505)*.*

*Note Angular+ngrx : Le calcul des LoC a été effectué avec le dossier* `/libs` *uniquement, incluant les fichiers* `.ts` *et* `.html`. *Si vous pensez que cela est incorrect, veuillez me faire savoir quel est le nombre correct et comment vous l'avez calculé.*

*Note Hyperapp : Le LoC n'était pas correct lors de la publication de l'article, merci à* [*Mateusz Kwasniewski*](https://twitter.com/kwasniew) *d'avoir indiqué la bonne façon de calculer le LoC.*

#### Conclusion

ClojureScript avec re-frame vous offre le plus de fonctionnalités pour le LoC. Clojure est connu pour être particulièrement expressif. Si vous vous souciez de votre LoC, vous devriez jeter un coup d'œil à ClojureScript, AppRun et Svelte.

### Résumé

Gardez à l'esprit que ce n'est pas exactement une comparaison pomme à pomme. Certaines implémentations utilisent le code splitting et d'autres non. Certaines sont hébergées sur GitHub, d'autres sur Now et d'autres sur Netlify. Voulez-vous toujours savoir lequel est le meilleur ? Le meilleur est celui qui répond à vos besoins.

**Q :** Aimez-vous les types ? 
**A :** Regardez Elm, PureScript et TypeScript  Angular, AppRun, Dojo.

**Q :** Voulez-vous une empreinte très petite ? 
**A :** Jetez un coup d'œil à Svelte, Stencil et AppRun.

**Q :** Voulez-vous avoir la plus petite base de code à maintenir ? 
**A :** Jetez un coup d'œil à ClojureScript avec re-frame, AppRun et Svelte.

**Q :** Voulez-vous apprendre quelque chose de nouveau ? 
**A :** Choisissez celui que vous ne connaissez pas !

### FAQ

#### **#1 Pourquoi les frameworks X, Y et Z n'ont-ils pas été inclus dans cette comparaison ?**

Parce que l'implémentation n'est pas terminée dans le [dépôt RealWorld](https://github.com/gothinkster/realworld). Envisagez de contribuer ! Implémentez la solution dans votre bibliothèque/framework préféré et nous l'inclurons la prochaine fois !

#### #2 Pourquoi appelez-vous cela le monde réel ?

Parce que c'est un peu plus qu'une application To-Do. Par RealWorld, nous ne voulons pas dire que nous comparerons les salaires, la maintenance, la productivité, les courbes d'apprentissage, etc. Il existe [d'autres enquêtes](https://insights.stackoverflow.com/survey/2018/) qui répondent à certaines de ces questions. Ce que nous entendons par RealWorld est une application qui se connecte à un serveur, authentifie et permet aux utilisateurs de CRUD  tout comme une application réelle le ferait.

#### #3 Pourquoi n'avez-vous pas inclus mon framework préféré ?

Veuillez voir #1 ci-dessus, mais au cas où, le voici à nouveau : parce que l'implémentation n'est pas terminée dans le [dépôt RealWorld](https://github.com/gothinkster/realworld). Je ne fais pas toutes les implémentations  c'est un effort communautaire. Envisagez de contribuer si vous voulez voir votre framework dans la comparaison.

#### #4 Quelle version de la bibliothèque/framework avez-vous incluse ?

Celle qui est disponible au moment de la rédaction (mars 2019). Les informations proviennent du [dépôt RealWorld](https://github.com/gothinkster/realworld). Je suis sûr que vous pouvez trouver cela dans le [dépôt GitHub](https://github.com/gothinkster/realworld).

#### #5 Pourquoi avez-vous oublié d'inclure un framework plus populaire que celui de la comparaison ?

Encore une fois, voir ci-dessus. L'implémentation n'est pas complète dans le [dépôt RealWorld](https://github.com/gothinkster/realworld) ; c'est aussi simple que cela.

Merci à [Rich Harris](https://twitter.com/Rich_Harris) et [Richard](https://twitter.com/rtfeldman) Feldman pour avoir jeté un coup d'œil avant la publication.

#### Mises à jour :

Lorsque cet article a été publié, le TL;DR LoC avait la description suivante :

> Moins vous avez de lignes de code, plus la probabilité de trouver une erreur est faible. Vous avez également une base de code plus petite à maintenir. 
> 
> Si vous aimez cet article, vous devriez [me suivre sur Twitter](https://twitter.com/JacekSchae). Je n'écris/tweete que sur la programmation et la technologie.