---
title: Ce que 500+ articles de blog m'ont appris sur l'écriture de grands articles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-31T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-500-blog-posts-taught-me-about-writing-great-articles
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/writing-technical-articles-banner.png
tags:
- name: Blogging
  slug: blogging
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: Ce que 500+ articles de blog m'ont appris sur l'écriture de grands articles
seo_desc: "By Burke Holland\nI've written a lot of blog posts. Somewhere north of\
  \ 500 to be exact. All of them are technical. \nAbout two dozen of them are actually\
  \ good. \nThe rest are just a meandering hot mess of grammatical errors, code snippets\
  \ that don't wor..."
---

Par Burke Holland

J'ai écrit beaucoup d'articles de blog. Quelque part au nord de 500 pour être exact. Tous sont techniques. 

Environ deux douzaines d'entre eux sont réellement bons. 

Le reste n'est qu'un méli-mélo de fautes de grammaire, de fragments de code qui ne fonctionnent pas et d'une utilisation sans fin de "it's" vs "its". Pourquoi ne puis-je pas faire cela correctement ? Ce n'est pas si compliqué.

MAIS. Je ne suis pas ici pour parler de mes échecs. C'est pour cela que la thérapie existe. Je suis ici pour parler de la douzaine de roses qui ont fleuri dans un champ littéraire de fèces. Voici les conseils dont vous avez besoin pour écrire les meilleurs articles techniques.

### Écrire pour les débutants  

À ce jour, mon article le plus populaire sur Medium (en termes de vues) est, "Voici comment vous pouvez réellement utiliser les variables d'environnement Node".  

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-46.png)

Lorsque j'écrivais l'article, je me demandais si j'étais la dernière personne au monde à ne pas comprendre pleinement les variables d'environnement. Clairement, je ne le suis pas. La leçon à tirer de cela est que **si vous pensez que quelque chose est trop simple pour en écrire, vous devriez probablement en écrire**.

Surestimer le public est l'erreur la plus courante que vous puissiez faire lorsque vous écrivez des articles techniques. Vous n'avez pas besoin de disséquer un compilateur ou d'inventer un framework pour avoir quelque chose à dire. [Lea Verou](https://twitter.com/LeaVerou) a fait une présentation entière sur une propriété CSS. UNE. Et c'est l'une des meilleures présentations que j'aie jamais vues.

%[https://www.youtube.com/watch?v=b9HGzJIcfDE]

Choisissez des sujets simples et plongez-vous dedans. Il y a beaucoup plus de personnes intéressées à apprendre comment tronquer des chaînes de caractères que de personnes intéressées à avoir une argumentation structurée sur la façon de résoudre le [problème des philosophes mangeurs](https://en.wikipedia.org/wiki/Dining_philosophers_problem). 

Notez que je juge la popularité des articles en fonction des vues. Il y a quelques conjectures sur le fait de savoir si cela est une bonne mesure du succès. Après tout, un bon clickbait vous obtiendra des vues. Il existe des sites dont le modèle économique entier est basé sur cela, et nous ne les tenons pas en particulièrement haute estime. 

Une autre mesure que nous pourrions examiner est le "Taux de lecture". L'article ci-dessus a un "Taux de lecture" de 25%. Un quart des personnes qui ont visité l'article l'ont réellement lu. Plus le pourcentage est élevé, mieux c'est. Il s'avère que la manière la plus simple d'augmenter ce pourcentage est simplement d'écrire des articles plus courts. Jetez un coup d'œil... 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-47.png)

Ce sont des articles jetables qui ne font que 2 ou 3 paragraphes de long. De l'écriture paresseuse. Moi qui lance des turds en l'air pour pouvoir dire que j'ai écrit quelque chose cette semaine-là. 

Nous semblons être dans une culture obsédée par cet objectif. Créez du contenu plus court ! Les gens le liront ! Oui, ils le liront, mais un peu de la même manière qu'ils lisent les panneaux de signalisation ; dévalant l'autoroute à un milliard de voies de l'internet, se bourrant le visage de Combos et retenant virtuellement rien de ce qu'ils voient.

Le % de lecture n'est pas un bon objectif. Il encourage tout le monde à simplement lancer des turds, et ce qui monte, doit redescendre.

Une meilleure mesure, je pense, est la métrique "Lectures". Combien de personnes ont réellement lu l'article ? Maintenant, nous ne savons pas comment Medium calcule cela, mais [ils attestent](https://help.medium.com/hc/en-us/articles/215108608-Your-stats) que c'est "combien de spectateurs ont lu toute l'histoire". Selon cette métrique, un nouvel article émerge comme le meilleur.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-48.png)

"Vous ne devriez jamais jamais exécuter directement contre Node en production. Peut-être."

Ce qui m'amène à la deuxième astuce pour écrire des articles techniques réussis...

### Remettre en question le statu quo

Alors que je travaillais sur une démonstration avec un ami, il m'a mentionné de manière désinvolte que vous ne devriez jamais exécuter directement contre Node en production. Eh bien, je ne le savais pas. Je n'en avais jamais entendu parler. J'ai donc décidé de faire des recherches pour voir s'il avait raison. Il s'avère qu'il avait raison. Mais il avait aussi tort. La réponse, comme tout dans la vie, est, "ça dépend".

L'idéologie de la programmation est parsemée d'absolus. Ne jamais utiliser de déclarations ternaires. Ne jamais ouvrir un hyperlien dans la même fenêtre. Ne jamais pousser en production un vendredi à 17h. Ne jamais construire un site web qui ne fonctionne pas sur mobile. Ne jamais faire "Select *" à partir d'une base de données. Ne jamais forcer la poussée dans un dépôt Github. Et vous ne devriez jamais prendre aucune de ces choses au pied de la lettre. 

La programmation est en noir et blanc. La réalité ne l'est pas. Dès que vous entendez quelqu'un faire une déclaration absolue, c'est un bon moment pour un article de blog. Vous pourriez découvrir que l'absolu est absolument faux. J'ai déjà entendu dire que vous ne devriez jamais mettre de JavaScript dans du HTML. Ensuite, un gars nommé [Jordan](https://twitter.com/jordwalke?lang=en) a dit, "oui, mais vous pouvez mettre du HTML dans du JavaScript", et aujourd'hui nous avons [React](https://reactjs.org/).

Secouez les choses. Les lecteurs veulent une opinion originale et tout le monde aime un renégat.

Le paradoxe des absolus est que, autant les gens aiment que vous remettiez en question ceux qui existent, ils aiment aussi quand vous créez les vôtres.

### Parler en absolus

Si nous continuons la liste des articles les plus populaires, nous arrivons à "La meilleure configuration de Visual Studio Code au monde".

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-50.png)

Celui-ci a un nombre de vues beaucoup plus faible car il est publié dans ma publication personnelle. En passant, n'essayez pas de créer votre propre blog ou publication. C'est comme essayer de créer votre propre magazine ou chaîne de télévision. Vous pouvez le faire, mais c'est beaucoup plus facile d'aller là où les lecteurs sont déjà.

Notez également que, bien que cet article ait beaucoup moins de vues que le suivant (41K vs 113K), il n'a que 4K de lectures en moins (24K vs 28K).

Cet article fait une allégation extravagante - que ma configuration personnelle de VS Code est la meilleure au monde. Il s'agit d'une affirmation extrêmement subjective, et probablement pas même proche d'être exacte. Mais c'est génial pour un article de blog car cela fait réfléchir le lecteur, "Oh oui ?! Je serai le juge de cela, mon ami !". 

Chaque fois que vous faites une déclaration absolue, vous invitez les gens à venir voir si elle peut résister à un examen minutieux. Les développeurs ne peuvent vraiment pas s'en empêcher. Voir si les choses résistent à un examen minutieux est un peu ce que nous faisons.

Beaucoup de ces personnes ne seront pas d'accord avec vous. Ce n'est pas grave. En fait, c'est sain. Laissez les gens aimer les choses, mais laissez-les aussi **ne pas** aimer les choses. Il y aura des gens qui n'aimeront pas que j'aie dit d'utiliser des absolus. Ils vont dire que vous ne devriez jamais utiliser d'absolus, ce qui est en soi une déclaration absolue. Vous voyez ? Vous ne pouvez pas gagner, alors n'ayez pas peur quand au moins la moitié de vos lecteurs laissent des commentaires comme celui-ci...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-51.png)

Sentez la brûlure. Et il a 432 applaudissements - de loin le plus de tous les commentaires sur cet article. C'est bien. Laissez ces gens ne pas être d'accord ou ne pas aimer votre style d'écriture. Vous pouvez plaire à certaines personnes parfois.

Le seul article que j'aie jamais eu qui soit arrivé en tête sur Hacker News utilise une stratégie similaire...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-53.png)

Tout ? Cela a ruiné **tout** ?! Bien sûr que non. Tout le monde sait que DC a réellement tout ruiné quand ils ont fait, "Aquaman". Maintenant, vous voyez, vous voulez prendre à partie cette déclaration. Vous voyez comment cela fonctionne ? 

L'autre chose que nous pouvons glaner des trois articles les plus populaires, c'est qu'ils couvrent tous des technologies assez populaires - Node et VS Code. C'est une tendance qui se poursuit dans les statistiques.

### Écrire sur les technologies populaires

Si je continue à parcourir la liste, les prochains articles concernent soit React, soit VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-52.png)

Écrire sur les technologies populaires va vous attirer des lecteurs. C'est un peu une évidence, mais cela mérite d'être répété : **écrire sur les technologies populaires va vous attirer des lecteurs**. Écrire sur un produit ou une technologie obscure que personne n'a jamais entendue, c'est comme si vous aviez organisé une fête et que personne n'était venu. Pas que cela me soit jamais arrivé. Deux fois.

Pour moi, écrire sur ce qui est "à la mode" ressemble toujours à un dunk sur un panier de six pieds. C'est trop facile et personne n'est impressionné quand vous renversez le jouet [Fisher-Price Grow-To-Basketball](https://www.amazon.com/Fisher-Price-L5807-Grow-to-Pro-Basketball/dp/B0063IKACQ) de votre enfant de quatre ans. Mais le fait reste que parler de sujets qui intéressent les gens est simplement mieux que de parler de ceux qui ne les intéressent pas. Cela ne devrait pas être une révélation bouleversante.

Le truc est de trouver comment utiliser ces choses pour transmettre ce que vous voulez réellement dire dans un article. 

Par exemple, je travaille sur Azure chez Microsoft. Si je veux écrire un article sur les meilleures pratiques pour exécuter des applications Node sur Azure, je pourrais le faire et l'appeler "Meilleures pratiques pour exécuter Node sur Azure". Il y a un nom pour un article comme celui-ci. Il s'appelle, "documentation".

Au lieu de cela, j'ai écrit un article intitulé, "Vous ne devriez jamais jamais exécuter des applications Node en production. Peut-être." Cet article bénéficie à **tous** les développeurs Node tout en transmettant les idées sur la meilleure façon d'exécuter des applications Node sur Azure. Comme je ne suis plus limité à "Azure", je peux écrire pour tous les développeurs Node et vous n'avez pas besoin d'utiliser Azure pour bénéficier du contenu.

### Tous les clickbaits ne se valent pas

Les bons titres attirent les gens. Ils doivent le faire. Le volume d'informations que nous consommons quotidiennement nécessite que vous disiez quelque chose pour attirer l'attention des gens. 

Malheureusement, les gens ont abusé de ce concept en optimisant pour la métrique "Vues" ou "Pourcentage de lecture" ; mettant des turds derrière un titre conçu juste pour obtenir votre clic.

Nous appelons cela, "Clickbait".

Le Clickbait est mauvais. Il est mauvais parce que le titre est salace, mais le contenu est faible. C'est de la pure tromperie, et nous le détestons. Personne n'aime être trompé. Grâce aux gens qui abusent des titres pour les clics, nous en sommes arrivés au point où tout titre qui attire votre intérêt est considéré comme "clickbait". Sauf que ce n'est pas le cas.

Votre contenu n'est aussi bon que le titre qui le précède. Si le titre ne fait pas s'arrêter les gens et prêter attention, cela n'a vraiment pas d'importance à quel point votre contenu est bon, n'est-ce pas ? Tant que vous mettez de la substance dans votre contenu, n'ayez pas peur d'attirer courageusement les gens avec des titres forts. De tous les titres que j'ai imaginés, voici quelques-uns de mes préférés...



* OAuth a tout ruiné
* [Économisez 15% ou plus sur l'assurance automobile en passant à JavaScript simple](https://css-tricks.com/save-15-car-insurance-switching-plain-javascript/)
* [Comment augmenter la taille de votre page de 1500% avec Vue et Webpack](https://css-tricks.com/how-to-increase-your-page-size-by-1500-with-webpack-and-vue/)
* [Vous ne devriez jamais jamais exécuter Node.js en production. Peut-être.](https://medium.com/free-code-camp/you-should-never-ever-run-directly-against-node-js-in-production-maybe-7fdfaed51ec6)
* [Le meilleur CLI est celui que vous n'avez pas à installer](https://www.infoq.com/articles/azure-cloud-shell/)

Alors, comment écrire de meilleurs titres ? Dans la première itération du guide de style de freeCodeCamp, Quincy a recommandé l'outil [CoSchedule Headline Analyzer](https://coschedule.com/headline-analyzer). J'ai utilisé ce site de nombreuses fois. Il vous aide à écrire de meilleurs titres en donnant à votre titre un "score". 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-71.png)

Cet outil peut être un peu frustrant à utiliser. Il vous dira que vous avez besoin de plus de mots "communs" ou de phrases "émotionnelles", mais il ne vous dit pas quels sont ces éléments. C'est un peu un exercice, mais j'ai trouvé l'outil utile dans la mesure où il me force à créer des dizaines d'itérations d'un titre et je finis toujours par obtenir un meilleur titre que celui avec lequel j'ai commencé.

Pour mon dernier conseil, je n'ai pas de données. Je n'ai pas de graphiques à vous montrer ou de statistiques pour me soutenir. Mon dernier conseil est simplement appris à la dure dans les tranchées de la vie.

### Soyez vulnérable

Le psychologue Robert Glover a un jour dit, "Les êtres humains sont attirés par les aspérités des autres".

L'une des choses les plus engageantes que vous puissiez faire pour votre lecteur est simplement d'être vous-même. Si vous ne comprenez pas quelque chose, dites-le. Si un concept est confus, pointez-le. Si vous avez peur d'écrire sur quelque chose parce que vous pensez que vous pourriez vous tromper, écrivez-le. Votre honnêteté est ce qui fait finalement un excellent article de blog.

Mettez-vous en avant. Montrez aux gens comment vous avez résolu un problème et demandez-leur comment ils le feraient. Vous allez avoir tort. Tout le temps. C'est la vie. Et le truc, c'est que les gens **adorent** cela.

L'un des premiers articles que j'ai écrits pour CSS Tricks couvrait un problème assez simple dans React où j'avais besoin que du contenu soit rendu dynamiquement. J'étais nouveau dans React, donc je n'étais pas sûr de la façon dont les autres le faisaient.

Alors [j'ai demandé aux gens](https://css-tricks.com/solve-rendering-puzzle-react/).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-72.png)

Cet article a plus de commentaires que tout autre article que j'aie jamais écrit. Ce n'est pas un long article. Il ne fournit aucune sorte de révélation. Il expose également ma naïveté en tant que développeur React. Mais plus important encore, **il se connecte avec les gens**. Pourquoi ? Parce que tout le monde a des choses qu'il ne sait pas et qu'il pense que tout le monde sait déjà. Ils attendent simplement que quelqu'un se manifeste et le dise. Une fois que vous le faites, ils le feront aussi. 

Oui, vous allez obtenir les commentaires "tout le monde sait cela". Mais c'est faux. Tout le monde ne le sait pas. Après tout, vous ne le saviez pas. Et cette voix dans votre tête qui vous dit que vous êtes le seul ? C'est votre ego. En bref, la fierté vous empêche d'être authentique, et cela vous empêche finalement de vous connecter avec vos lecteurs.

### La fine ligne entre être intéressant et être offensant

Un mot d'avertissement : il y a une fine ligne entre écrire un contenu intéressant et être simplement un imbécile. Il est assez facile de passer de perspicace à simplement méchant. Je devrais savoir. Je l'ai fait.

Si je dis "OAuth a tout ruiné", je critique les personnes qui ont créé cette spécification. Il y a un être humain pensant et ressentant à l'autre bout de chaque technologie que vous utilisez. Dans le cas d'OAuth, le créateur lui-même avait déjà fait des déclarations pires à ce sujet, donc je me sentais à l'aise de ne pas simplement salir son travail en public. 

Même ainsi, j'ai pris un grand risque en faisant cela. C'est attendu. Vous allez devoir assumer une certaine quantité de risque pour écrire un grand contenu, soit parce que vous êtes vulnérable, parce que vous remettez en question le statu quo, ou simplement parce que vous êtes honnête. Mais vous **n'avez pas** à être un imbécile. Cette partie est facultative et l'internet ne manque pas exactement de contenu négatif.

### Écrivez

La chose la plus importante de toutes est simplement d'écrire. Aucun de ces conseils n'est bon si vous n'écrivez rien. Pour beaucoup de gens, c'est la partie la plus difficile. Sachez simplement que plus vous le faites, plus c'est facile. C'est un peu comme jouer de la guitare.

Je vous laisse avec cette inspiration. Voici Alexandr Misko. Mon avis est qu'il n'a pas simplement pris une guitare un jour et joué comme cela. Cela a pris beaucoup de pratique. L'écriture n'est pas différente. Si vous le faites assez, vous pourriez bien devenir l'Alexandr Misko du blogging.

%[https://www.youtube.com/watch?v=EMxiuq_tMq0]