---
title: Types de formation en développement logiciel – Une analyse de données sur l'efficacité
  des outils de formation pour les carrières en TI
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2021-11-29T21:06:01.000Z'
originalURL: https://freecodecamp.org/news/types-of-software-development-training
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-christina-morillo-1181298.jpg
tags:
- name: learn to code
  slug: learn-to-code
- name: software development
  slug: software-development
seo_title: Types de formation en développement logiciel – Une analyse de données sur
  l'efficacité des outils de formation pour les carrières en TI
seo_desc: "How you train for your career is one of the most consequential decisions\
  \ you'll ever make. But it's hard to narrow down your options for a career in software\
  \ development or IT.\nMedicine is easy: pick a medical school and apply.\nBut programming?\
  \ \n\nWil..."
---

La manière dont vous vous formez pour votre carrière est l'une des décisions les plus importantes que vous prendrez jamais. Mais il est difficile de réduire vos options pour une carrière en développement logiciel ou en TI.

La médecine est simple : choisissez une école de médecine et postulez.

Mais la programmation ? 

* Ce que vous apprendrez dans un diplôme de quatre ans en informatique sera-t-il obsolète au moment où vous obtiendrez votre diplôme ? 
* Une université offre-t-elle de meilleurs résultats qu'une autre ? 
* Les bootcamps intensifs (et coûteux) fonctionnent-ils vraiment ? 
* Est-il possible d'apprendre tout ce dont vous aurez besoin par vous-même en utilisant des ressources en ligne gratuites ?

Les coûts des programmes peuvent varier de gratuit à plusieurs centaines de milliers de dollars. Et ils peuvent vous faire entrer et sortir en quelques mois, ou s'étendre sur une décennie ou plus. 

En même temps, le retour sur investissement en termes de revenus tout au long de votre vie variera également considérablement.

Il ne suffit pas de suivre ce que font tous vos amis ou ce que "tout le monde dit" être suffisant. Vous aurez besoin de données.

Dans cette analyse, je vais vous présenter quelques outils de données super utiles conçus pour vous aider à évaluer à la fois les institutions individuelles et les grandes catégories de formation professionnelle. 

Le premier est l'outil de données de la [Postsecondary Value Commission](https://equity.postsecondaryvalue.org/datatool) du gouvernement américain. Vous pouvez télécharger l'ensemble de données complet au format CSV à partir de [cette page](https://equity.postsecondaryvalue.org/datatool/compare). Le deuxième ensemble de données provient de l'enquête 2018 de freeCodeCamp sur les développeurs, dont les données sont [publiquement disponibles](https://www.kaggle.com/freecodecamp/freecodecamp-2018-new-coder-survey-of-30k-devs).

Malheureusement, pour des raisons purement pratiques, les données que j'ai utilisées pour cet article sont toutes basées aux États-Unis. Je sais que beaucoup d'entre vous ne vivent et ne travaillent pas aux États-Unis. (Je suis moi-même Canadien.) Mais ce sont mes contraintes. 

Néanmoins, la plupart des principes de base que nous discuterons ici sont universels. Et votre propre pays a probablement son propre ensemble de ressources similaires qui peuvent vous mettre à jour avec ce qui est unique à votre partie du monde.

Vous pouvez trouver presque tous les outils que j'ai utilisés dans l'analyse dans le programme de mon [curriculum Teach Yourself Data Analytics in 30 Days](https://stories.thedataproject.net/). Donc, il y a cela.

Je devrais noter que toutes les informations que vous verrez ici sont basées sur des chiffres, et des chiffres incomplets en plus. Les informations sont intéressantes et, je crois, utiles. Mais elles ne sont pas garanties d'être objectivement correctes. L'analyse de données a ses limites. Son objectif est de représenter fidèlement le monde réel, mais les chiffres peuvent être trompeurs.

## La Postsecondary Value Commission

Parmi les riches données publiques disponibles sur [le site Web PostSecondary Value](https://equity.postsecondaryvalue.org/datatool/compare), trois métriques nous intéressent : 

1. Le seuil T-Zero (T0)
2. Les taux d'obtention de diplôme
3. Les taux de défaut de prêt

Ensemble, ces éléments peuvent nous donner une assez bonne idée des résultats que vous pouvez attendre des collèges de quatre ans en général, et des institutions individuelles.

Le _T0_ est conçu pour décrire le coût réel d'un diplôme de baccalauréat. C'est-à-dire, le coût cumulatif net estimé des frais de scolarité et autres dépenses connexes, en plus des coûts d'opportunité de ne pas travailler à temps plein pendant vos années d'études. 

Ils le font en utilisant les gains médians des diplômés du secondaire dans l'État d'origine d'un collège. En d'autres termes, le revenu que vous auriez pu espérer gagner si vous n'étiez pas allé au collège.

### Comment calculer le seuil T-Zero (T0)

Pour illustrer, disons que le coût total cumulé d'un programme de baccalauréat de quatre ans est de 200 000 $, mais que l'étudiant moyen peut s'attendre à recevoir des bourses Pell et des bourses d'études de 80 000 $. 

Par conséquent, le coût total cumulé net du diplôme est de 120 000 $. Pour obtenir le T0, ce nombre est amorti (réparti) sur dix ans, ce qui nous donne une valeur annuelle de 12 000 $. 

Nous ajoutons ensuite les gains annuels médians des diplômés du secondaire dans cet État - disons que c'est 30 000 $. Eh bien, 12 000 $ + 30 000 $ nous donne une valeur annuelle T0 de 42 000 $. 

Pour que votre investissement dans le collège soit rentable, vous devriez vous attendre à gagner au moins plus de 42 000 $ dix ans après le début de vos études. Si un grand nombre d'étudiants d'un collège gagnent significativement moins que le T0, alors vous devriez vous inquiéter de la qualité et de la valeur de leurs programmes.

### Qu'est-ce que le taux d'obtention de diplôme ?

Le taux d'obtention de diplôme est le pourcentage d'étudiants qui s'inscrivent dans un collège et obtiennent un diplôme de baccalauréat dans les 150 % du "temps prévu pour l'obtention du diplôme". 

Pour une école où il est prévu qu'un baccalauréat soit obtenu en quatre ans, 150 % serait six ans. Les taux d'obtention de diplôme ne tiennent pas compte des étudiants qui transfèrent et obtiennent leur diplôme dans d'autres institutions.

Une école où 80 % de ses étudiants obtiennent leur diplôme est probablement sur la bonne voie. Mais un collège avec un taux d'obtention de diplôme de 20 % fait définitivement quelque chose de mal.

### Qu'est-ce que le taux de défaut de prêt ?

Le taux de défaut de prêt est le pourcentage d'étudiants d'une école qui finissent par ne pas pouvoir suivre leurs remboursements de prêts étudiants. Une école avec un taux de défaut élevé parmi ses étudiants ne fait probablement pas assez pour assurer leur succès financier.

Intéressamment, j'ai trouvé une corrélation claire entre le coût du programme et les taux d'obtention de diplôme, et entre le coût du programme et les taux de défaut de prêt. Mais ce n'était pas la corrélation à laquelle je m'attendais. 

Jetez un coup d'œil à ce nuage de points où l'axe des x représente le prix net cumulatif moyen des collèges et l'axe des y représente les taux d'obtention de diplôme. La ligne de tendance OLS monte clairement avec les coûts. Ce qui signifie que plus le coût est élevé, plus il est probable que les étudiants le mènent à terme.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/completion.png)
_Il y a une corrélation positive claire entre le prix net cumulatif des collèges et les taux auxquels les étudiants terminent leurs programmes_

De même, ce graphique suivant montre que les taux de défaut de prêt étudiant diminuent à mesure que les coûts des programmes augmentent :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/default.png)
_Les taux de défaut de prêt étudiant diminuent à mesure que les coûts des programmes augmentent_

Je suppose que nous pouvons dire que plus les enjeux sont élevés, plus les gens prennent le défi au sérieux.

### Comment savoir si une école est bonne

Avant de regarder une école en particulier, vous avez vraiment besoin de savoir comment se porte l'ensemble de l'industrie. Les gains médians par rapport au T0 pour l'ensemble des 5 877 collèges mesurés sont de 13 909 $. 

Cela signifie que, parmi les étudiants qui ont fréquenté tous les collèges américains du système, la moitié gagne 13 909 $ de plus que leurs seuils T0. 

En même temps, 75 % des étudiants gagnent moins de 22 595 $ au-dessus du T0.

(Notez que ces chiffres ne sont pas tout à fait exacts - ce sont en fait des moyennes dérivées de valeurs médianes individuelles - mais ils sont suffisamment proches.)

Le taux d'obtention de diplôme moyen pour l'ensemble des 5 877 collèges est de 54,8 %. Cela signifie que plus de 45 % de tous les étudiants qui s'inscrivent dans les collèges américains ne parviennent pas à obtenir leur diplôme. C'est en fait un chiffre stupéfiant. Il suggère qu'une très grande proportion de tous les étudiants abandonnent (ou ne parviennent pas à terminer pour une raison quelconque) sans obtenir leur diplôme. 

Mais qu'en est-il des dizaines de milliers de dollars et des années de travail ? Tout est perdu. En fait, 11 % des étudiants dans le collège américain moyen finissent par faire défaut sur leurs prêts étudiants.

Que se passe-t-il ici ? D'une part, de nombreuses écoles semblent accepter des étudiants qui ne sont pas préparés pour le défi du collège. Les collèges gagnent, après tout, beaucoup d'argent pour chaque nouvelle inscription. Dans d'autres cas, les écoles ont peut-être simplement échoué à enseigner correctement à leurs étudiants.

Imaginez simplement si vous dirigiez une entreprise qui facturait plusieurs milliers de dollars pour un produit qui tombait en panne 45 % du temps et poussait 11 % de vos clients à l'insolvabilité financière. Pensez-vous que vous dirigeriez cette entreprise très longtemps ?

L'[explorateur de données](https://equity.postsecondaryvalue.org/datatool/institution) vous permet de rechercher n'importe quel collège dans le système. Consultez les écoles de votre région et portez une attention particulière à la relation entre le revenu médian (un nombre représentant le revenu que les étudiants réels de cette école gagnent dix ans après l'inscription initiale) et le T0. 

Si le T0 est plus élevé, cela signifie que la plupart des étudiants perdent en fait de l'argent avec leur éducation.

## L'enquête 2018 de freeCodeCamp sur les nouveaux codeurs

Bien qu'il s'agisse toujours d'une excellente représentation de l'état de l'industrie, ces données de trois ans ne rajeunissent pas. Alors, commençons.

Tout d'abord, quelques observations générales. Les 1 643 répondants américains de freeCodeCamp qui ont déclaré avoir une dette étudiante impayée détenaient en moyenne 36 171 $ de celle-ci. C'est très proche du dernier chiffre national (novembre 2021) de 39 351 $ rapporté par [Education Data](https://educationdata.org/student-loan-debt-statistics). Je pense que cela suggère que les données de freeCodeCamp sont largement représentatives des conditions réelles.

### Combien gagnent les diplômés du collège ?

Que reçoivent ces étudiants en échange de leur investissement ? Le revenu annuel moyen de tous les 3 645 répondants américains qui ont déclaré des revenus était de 41 874 $. 

Les 137 d'entre eux qui avaient une formation professionnelle, technique ou vocationnelle gagnaient un peu moins : 39 897 $. 

Les 1 399 ayant un diplôme de baccalauréat (dans n'importe quel domaine) gagnaient 45 818 $. 

Et les 139 qui avaient obtenu un diplôme professionnel (MBA, MD, JD, etc.) avaient un revenu moyen de 71 151 $. 

Contracter 36 000 $ de dette étudiante peut avoir du sens s'il y a une très forte chance que le programme que vous suivez vous rapportera un revenu à un niveau qui couvrira et dépassera éventuellement tous vos coûts. Si vos propres recherches ne vous laissent pas si confiant à ce sujet, alors vous devriez explorer des alternatives moins chères.

### Les bootcamps de codage en valent-ils la peine ?

En ce qui concerne le codage, l'une de ces alternatives moins chères est l'un des nombreux bootcamps intensifs qui ont vu le jour ces dernières années. 

La durée des cours de bootcamp se mesure en mois plutôt qu'en années, donc ils nécessitent évidemment un investissement plus petit. Mais ils ne sont pas exactement bon marché. Les frais de scolarité pour de nombreux bootcamps coûteront 10 000 $ ou plus et, comme ils sont généralement à temps plein, vous aurez besoin d'argent pour la nourriture et le logement pendant que vous êtes inscrit.

L'expérience du bootcamp se traduit-elle par un revenu plus élevé ? Les 3 411 répondants américains à l'enquête qui n'avaient jamais participé à un bootcamp et qui avaient déclaré leur revenu de l'année précédente gagnaient en moyenne 42 018 $. 

Étonnamment, les 234 répondants qui avaient participé à un bootcamp ont déclaré gagner seulement 39 771 $. De plus, 102 de ces étudiants de bootcamp qui n'avaient jamais fréquenté le collège ont néanmoins déclaré une dette étudiante moyenne de 22 941 $. 

Maintenant, je ne prétends pas que ce chiffre est une représentation vraie et absolue de tout le monde des bootcamps. Il y a certainement de nombreuses personnes pour qui les bootcamps fonctionnent merveilleusement. Mais 234 n'est pas un nombre insignifiant. C'est quelque chose à garder à l'esprit.

freeCodeCamp, en revanche, est conçu en pensant aux adultes occupés. À ce titre, les ressources d'apprentissage demandent aux apprenants de faire plus de travail que les écoles traditionnelles.

Le programme est composé de contenu vidéo et textuel complet, d'environnements de codage interactifs, et de projets et défis. Et les campeurs peuvent trouver du soutien parmi les groupes d'étude du monde entier. 

freeCodeCamp propose même une préparation extensive aux entretiens d'embauche. Et, bien sûr, tout est disponible dans le confort de votre maison et gratuitement.

Outre les bootcamps, cependant, il existe une autre catégorie de ressources d'apprentissage technologique : les cours en ligne.

### Les cours en ligne fonctionnent-ils ? Perspectives de l'analyse de données

Certaines ressources d'apprentissage en ligne (comme Khan Academy et, bien sûr, freeCodeCamp) sont disponibles gratuitement. 

D'autres, comme Coursera ou edX affiliés à des collèges de quatre ans, facturent pour la délivrance de certificats à la fin de leurs cours, mais leur contenu peut généralement être accessible gratuitement. 

Et le contenu fourni par des plateformes comme Pluralsight peut être accessible via des abonnements mensuels. Les coûts de toutes ces options sont significativement moins chers que ceux des collèges ou des bootcamps.

Alors, comment ces ressources se comparent-elles aux collèges et aux bootcamps en termes d'augmentation de revenu ? Le graphique ci-dessous présente certains des chiffres de l'enquête de freeCodeCamp.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/chart-2.png)
_fCC représente freeCodeCamp.org. freeCodeCamp associé à Pluralsight a donné le revenu moyen le plus élevé, suivi par Coursera et EdX._

Comme vous pouvez le voir, le revenu a augmenté d'environ 6 000 $ pour les 594 étudiants qui ont ajouté du contenu Coursera à leur portefeuille éducatif. 567 étudiants edX ont bénéficié de près de 5 000 $ de revenu supplémentaire. Les 1 529 étudiants de freeCodeCamp qui ont également utilisé Udemy ont vu près de 4 000 $ de plus. De manière inexplicable, vous risquiez de perdre 3 500 $ en utilisant les ressources de Khan Academy.

Mais qu'en est-il de ces chiffres de Pluralsight ? Maintenant, je devrais avouer que [je suis un auteur de contenu pour Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton), donc j'ai un intérêt dans cette course. Mais il est indéniable que Pluralsight a offert une prime de revenu moyenne de 12 000 $ par rapport aux utilisateurs accédant uniquement à freeCodeCamp. C'est une augmentation impressionnante de 24 %.

Encore une fois, tous ces chiffres ne sont que des hypothèses statistiques. Ils ne sont pas des prédictions fiables et solides de ce que vous vivrez réellement, et ils ne s'appliqueront pas également à tout le monde.

Mais ce sont des outils qui peuvent vous aider à réfléchir de manière plus productive à la façon dont vous devriez planifier votre éducation. Utilisez-les pour réfléchir à vos plans et espoirs dans le contexte de ce qui peut être abordable maintenant... et dans dix ans. Mais essayez également de voir au-delà du battage publicitaire de recrutement pour voir la véritable valeur sous-jacente.

Maintenant, c'est à vous de jouer.