---
title: Comment j'ai analysé un million d'articles Medium pour savoir combien de claps
  obtiennent les grandes histoires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:57:30.000Z'
originalURL: https://freecodecamp.org/news/how-i-analyzed-a-million-medium-articles-to-learn-how-many-claps-great-stories-get-d688cf92759f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Fa8l3RP4Pp4872OwTocfOg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Inspiration
  slug: inspiration
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: Comment j'ai analysé un million d'articles Medium pour savoir combien de
  claps obtiennent les grandes histoires
seo_desc: 'By Harrison Jansma

  This article is for the writers of Medium. If you have ever been frustrated with
  the response your stories get, this article can help you.

  My name is Harrison Jansma, and I write about data. Over the last few weeks, I collected
  and...'
---

Par Harrison Jansma

_Cet article est destiné aux écrivains de Medium. Si vous avez déjà été frustré par la réponse que vos histoires reçoivent, cet article peut vous aider._

Je m'appelle Harrison Jansma, et j'écris sur les données. Au cours des dernières semaines, j'ai collecté et analysé les claps d'un million d'histoires Medium. Ainsi, je pourrais répondre à la question qui me dérange le plus en tant qu'écrivain sur Medium. À savoir,

> _Comment mes histoires se comparent-elles à celles d'écrivains similaires sur Medium ?_

Bien que je sois un écrivain, je ne suis pas particulièrement créatif. Pour faire face, je dois motiver mon écriture par la compétition. Me fixer des objectifs basés soit sur la performance de mes histoires passées, soit sur la performance des histoires dans mon fil d'actualité.

**Malheureusement, cette comparaison tue lentement ma capacité à écrire.**

Le problème est que je me fixe des objectifs pour mon écriture sans savoir si ces objectifs sont raisonnables.

![Image](https://cdn-media-1.freecodecamp.org/images/G1a8qlikoBp5kKGRTMGbe01prUDNV39tSWJ5)
_Lequel de ces objectifs est raisonnable ?_

Les histoires dans mon fil d'actualité varient de 40 claps à 30K claps. Les trois premières histoires que j'ai écrites sur Medium variaient de 80 claps à 9K claps. Donc, dois-je me fixer comme objectif d'obtenir trente mille claps ? Dix mille claps ? Combien d'histoires atteignent réellement ce niveau d'engagement des lecteurs ?

Tant que les claps semblent varier considérablement d'une histoire à l'autre, les écrivains ne pourront jamais utiliser cette métrique pour se fixer des objectifs pour leur écriture.

J'ai donc fait de la compréhension des claps de Medium mon objectif. J'ai collecté des données de centaines de milliers d'histoires Medium, couvrant des sujets allant de la poésie à la technologie en passant par la politique. Avec ces données, j'ai trouvé exactement ce que je cherchais.

**J'ai trouvé un moyen pour les auteurs de comparer la performance de leurs écrits à d'autres histoires similaires sur Medium.**

### **Collecte d'un million d'histoires Medium.**

La première étape était de collecter des informations. Plus précisément, je devais obtenir les claps reçus par un grand nombre d'articles Medium.

J'ai donc parcouru les archives de Medium pendant quelques jours. Ensuite, j'ai créé un scraper web en Python (disponible sur [GitHub](https://github.com/harrisonjansma/Analyzing_Medium)). Le scraper web a extrait des données de milliers de cartes d'histoires.

![Image](https://cdn-media-1.freecodecamp.org/images/qiRCymOwTYpuCMzw-ZtM9rR94rwqy5SSNYzl)
_Exemple de données extraites d'une carte d'histoire._

**Une fois la collecte de données terminée, j'avais des données sur 993K articles Medium.** Ils couvraient 36 des tags les plus populaires de Medium, tous publiés au cours de la dernière année (août 2017 - août 2018).

![Image](https://cdn-media-1.freecodecamp.org/images/BS3XxeyXqDqzguCZTp82GsIzZ5Oe7tTAt1NJ)

### Analyse (presque) d'un million d'histoires Medium

Après avoir supprimé les histoires en double et les commentaires des données, il me restait 720K histoires uniques de 230K auteurs et 30K publications. Le nombre de claps reçus pour un article variait de zéro claps à [215K claps](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5).

Pour mieux comprendre la métrique des claps de Medium, je devais répondre à deux questions.

1. Combien de claps obtient l'histoire moyenne ?
2. Combien de claps obtient une histoire au-dessus de la moyenne ?

Commençons par la première question.

### Combien de claps obtient l'histoire moyenne ?

Sur Medium, la plupart des écrivains reçoivent un engagement médiocre de la part de leurs lecteurs. Cela peut être dû au fait que Medium est une plateforme gratuite pour les écrivains. Ou peut-être parce que le but de chaque écrivain n'est pas de recevoir un grand nombre de claps de la part de son public.

**Quelle que soit la raison, la plupart des articles reçoivent presque aucun applaudissement.** Parmi les 720K articles que j'ai analysés, 61,3 % ont reçu moins de 10 claps.

![Image](https://cdn-media-1.freecodecamp.org/images/AaMMtD3kRzB3-tPHI2-0n4jyYr4dSxJO76ZN)

**Si vous êtes un écrivain, vous ne devriez pas vous laisser décourager par cela.**

Qu'il s'agisse de l'heure de la journée ou des mystères du moteur de recommandation de Medium, l'engagement que vos histoires reçoivent ne dépend pas vraiment de vous.

Cependant, les auteurs les plus réussis sur Medium ne sont pas arrivés là par hasard. Ils ont publié du contenu de haute qualité (de manière constante) pendant longtemps et ont progressivement construit un public.

Vous pouvez faire de même.

### Combien de claps obtient une histoire au-dessus de la moyenne ?

Maintenant que vous savez combien de claps la plupart des histoires reçoivent, nous allons examiner l'autre extrémité du spectre : les histoires qui ont reçu plus de claps que la moyenne.

Malheureusement, il n'y a pas un nombre distinct de claps qu'un article doit avoir pour être au-dessus de la moyenne. Ce dont nous avons besoin, c'est de reformuler un peu la question. Au lieu de cela, nous demandons :

**Combien de claps obtiennent les 1 % des meilleures histoires ?**

Parmi les 720K histoires analysées, les 1 % des histoires les plus applaudies ont reçu plus de deux mille claps.

![Image](https://cdn-media-1.freecodecamp.org/images/fgxdN41uZIlk2kNyGR-HjmKD00o-t3SycXH5)

_Ce seuil se situe exactement à 2000,0 claps, plutôt qu'à un nombre comme 2112 en raison de la manière dont les données ont été collectées. Une fois que vous dépassez les mille claps, Medium abrévie vos claps reçus (ex. 2,2K). Donc le seuil strict se situe quelque part entre 2K et 2,1K. Mais deux mille sonne beaucoup mieux... Donc..._

**Ainsi, deux mille claps est le seuil pour qu'une histoire soit dans le top 1 % des histoires Medium.** Désormais, lorsque vous écrivez une histoire, vous pouvez utiliser cela comme objectif pour l'engagement des lecteurs. Vous pouvez également utiliser cela comme référence pour mesurer la performance de vos articles passés.

Deux mille claps est également une assez bonne métrique pour votre performance en tant qu'auteur.

Écrire une histoire dans le top 1 % n'est pas une mince affaire. Parmi les 230K auteurs dans les données, seulement 1,2 % avaient écrit un article avec plus de deux mille claps.

![Image](https://cdn-media-1.freecodecamp.org/images/8b4Mxfu9zpfXkXoActdoWcd0eCof6fD7b2ck)

Encore moins d'auteurs ont pu publier des articles avec plus de deux mille claps de manière constante. Le graphique suivant montre ce dont je parle.

![Image](https://cdn-media-1.freecodecamp.org/images/6PFhMUUA5x-1QzZb-uqeIS2BvOe-x60NIEv9)

Mais soyez averti, ce seuil pour le top 1 % inclut des articles écrits pour des genres très différents.

Pouvons-nous vraiment comparer la performance d'une histoire de poésie à celle d'une histoire d'auto-amélioration ? Chacune a un public très différent, variant en taille, en goût et en personnalité.

Heureusement, Medium sépare déjà son contenu avec des tags. Tout ce que nous avons à faire est de trouver le top 1 % de chaque tag sur Medium.

#### Combien de claps obtiennent les 1 % des meilleurs articles pour chaque tag ?

Voici les 99e percentiles des claps reçus par un article pour chacun des 36 tags de nos données.

![Image](https://cdn-media-1.freecodecamp.org/images/fZorT62hzde6AUndHgZ3XNrKjRNfwjmxvumk)

Certains des tags les plus suivis de Medium (Amélioration de soi, Productivité, Leçons de vie) ont les seuils les plus élevés pour être dans le top 1 %. Alors que le tag avec le plus d'histoires (Voyage) avait le seuil le plus bas.

Je n'ai pas été en mesure de trouver une raison à cette répartition, donc j'aimerais en discuter davantage dans les commentaires.

Voici les 99e percentiles individuels pour chacun des 36 tags d'histoires.

![Image](https://cdn-media-1.freecodecamp.org/images/h5KWt2Db1WcXb0d5XB1he5pjyxmuV9YBV-Cx)

Nous y voilà ! Vous pouvez utiliser les chiffres ci-dessus pour comparer la performance de vos histoires à celle d'auteurs similaires sur Medium.

Par exemple, puisque cet article a un tag de science des données, je pourrais me fixer comme objectif d'obtenir 2900 claps. Si je pouvais atteindre ce niveau d'engagement des lecteurs, cet article serait dans le top 1 % des articles liés à la science des données sur Medium.

### Conclusion

La plupart des histoires Medium reçoivent moins de dix claps, et le top 1 % des histoires de Medium reçoivent plus de deux mille claps. Vous pouvez utiliser ces métriques comme références pour mesurer la performance de vos articles, ou comme objectif pour écrire de futurs articles.

J'ai également inclus le seuil pour le top 1 % de 36 tags d'histoires populaires, afin que vous puissiez comparer votre travail à celui d'auteurs similaires sur Medium.

#### Suivez-moi si vous voulez plus d'articles de haute qualité sur la science des données. ?

_Il y avait quelques choses que j'ai apprises sur Medium qui ne sont pas directement pertinentes pour cet article. J'ai donc écrit une analyse complète de tout ce que j'ai trouvé. Si vous voulez savoir qui étaient : les auteurs les plus applaudis, les plus grandes publications, et bien plus encore, regardez [ici](https://github.com/harrisonjansma/Analyzing_Medium/blob/master/Medium_EDA.ipynb)._