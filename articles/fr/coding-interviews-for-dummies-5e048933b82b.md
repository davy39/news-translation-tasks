---
title: Comment réussir l'entretien de codage – Conseils qui m'ont aidé à obtenir des
  offres d'emploi de Google, Airbnb et Dropbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-16T13:07:00.000Z'
originalURL: https://freecodecamp.org/news/coding-interviews-for-dummies-5e048933b82b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qf9fEs5XdOEQiWX3R6R6ww.jpeg
tags:
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment réussir l'entretien de codage – Conseils qui m'ont aidé à obtenir
  des offres d'emploi de Google, Airbnb et Dropbox
seo_desc: 'By Yangshun Tay

  Back in 2017, I went through some coding interviews and got offers from several
  large tech companies. So at that point, I decided to share what I''d learned in
  this article.

  And I''ve just updated it for 2022 so it''ll be super useful an...'
---

Par Yangshun Tay

En 2017, j'ai passé quelques entretiens de codage et j'ai reçu des offres de plusieurs grandes entreprises technologiques. À ce moment-là, j'ai décidé de partager ce que j'avais appris dans cet article.

Et je viens de le mettre à jour pour 2022 afin qu'il soit super utile et pertinent si vous êtes en recherche d'emploi maintenant.

Malgré des notes décents dans mon cours d'algorithmes CS101 et dans mon cours de structures de données à l'université, je frissonne à l'idée de passer un entretien de codage axé sur les algorithmes.

J'ai donc passé les trois derniers mois à comprendre comment améliorer mes compétences en entretien de codage et j'ai finalement reçu des offres de grandes entreprises technologiques comme **Google, Facebook, Airbnb, Lyft, Dropbox** et plus encore. 

Dans cet article, je vais partager les insights et les conseils que j'ai acquis en cours de route. Les candidats expérimentés peuvent également s'attendre à des questions sur la conception de systèmes, mais cela dépasse le cadre de cet article.

Beaucoup des concepts algorithmiques testés lors des entretiens de codage ne sont pas ceux que j'utilise habituellement au travail, où je suis ingénieur Front End (web). Naturellement, j'ai oublié pas mal de choses sur ces algorithmes et structures de données, que j'ai surtout appris pendant mes premières et deuxièmes années de fac.

C'est stressant de devoir produire du code (fonctionnel) lors d'un entretien, tandis que quelqu'un scrute chaque frappe que vous faites. Ce qui est pire, c'est qu'en tant qu'interviewé, vous êtes encouragé à communiquer votre processus de réflexion à voix haute à l'interviewer.

Je pensais autrefois que pouvoir penser, coder et communiquer simultanément était une tâche impossible, jusqu'à ce que je réalise que la plupart des gens ne sont simplement pas bons aux entretiens de codage lorsqu'ils commencent. L'entretien est une compétence que vous pouvez améliorer en étudiant, en vous préparant et en vous entraînant.

Ma récente recherche d'emploi m'a conduit à un voyage pour améliorer mes compétences en entretien de codage. Les ingénieurs Front End aiment se plaindre de la manière dont le processus de recrutement actuel est cassé parce que les entretiens techniques peuvent inclure des compétences non liées au développement front-end. Par exemple, écrire un algorithme de résolution de labyrinthe et fusionner deux listes triées de nombres. En tant qu'ingénieur Front End moi-même, je peux compatir avec eux.

Le front-end est un domaine spécialisé où les ingénieurs doivent se soucier de nombreux problèmes liés aux compatibilités des navigateurs, au Document Object Model, aux performances JavaScript, aux mises en page CSS, et ainsi de suite. Il est rare que les ingénieurs front-end implémentent certains des algorithmes complexes testés lors des entretiens.

> **Dans des entreprises comme Facebook et Google, les personnes sont d'abord des ingénieurs logiciels, puis des experts de domaine.**

Malheureusement, les règles sont fixées par les entreprises, pas par les candidats. Il y a une forte emphase sur les concepts généraux de l'informatique comme les algorithmes, les patrons de conception, les structures de données ; des compétences de base qu'un bon ingénieur logiciel devrait posséder. Si vous voulez le poste, vous devez jouer selon les règles fixées par les maîtres du jeu — améliorez vos compétences en entretien de codage !

Cet article est structuré en deux sections suivantes. N'hésitez pas à sauter à la section qui vous intéresse.

* La décomposition des entretiens de codage, et comment s'y préparer.
* Des conseils et astuces utiles pour chaque sujet d'algorithme (tableaux, arbres, programmation dynamique, etc.), ainsi que des questions pratiques recommandées sur LeetCode pour réviser les concepts de base et s'améliorer sur ces sujets.

Le contenu de cet article [peut être trouvé ici](https://www.techinterviewhandbook.org/). J'y apporterai des mises à jour si nécessaire.

Si vous êtes intéressé par le contenu Front End, consultez mon [manuel d'entretien front end ici](https://www.frontendinterviewhandbook.com/).

## Choisir un langage de programmation

Avant toute chose, vous devez choisir un langage de programmation pour votre entretien de codage algorithmique. 

La plupart des entreprises vous permettront de coder dans le langage de votre choix. La seule exception que je connais est Google. Ils permettent à leurs candidats de choisir uniquement parmi Java, C++, Python, Go ou JavaScript. 

Dans la plupart des cas, je recommande d'utiliser un langage que vous maîtrisez parfaitement, plutôt qu'un langage nouveau pour vous mais largement utilisé par l'entreprise.

Certains langages sont plus adaptés que d'autres pour les entretiens de codage. Il y en a aussi que vous devez absolument éviter. 

D'après mon expérience en tant qu'interviewer, la plupart des candidats choisissent Python ou Java. D'autres langages couramment sélectionnés incluent JavaScript, Ruby et C++. J'éviterais absolument les langages de bas niveau comme C ou Go, simplement parce qu'ils manquent de fonctions et de structures de données dans la bibliothèque standard.

Personnellement, Python est mon choix par défaut pour coder des algorithmes lors des entretiens. Il est concis et dispose d'une énorme bibliothèque de fonctions et de structures de données. 

L'une des principales raisons pour lesquelles je recommande Python est qu'il utilise des API cohérentes qui fonctionnent sur différentes structures de données, comme `len()`, `for ... in ...` et la notation de découpage sur les séquences (chaînes de caractères, listes et tuples). Obtenir le dernier élément d'une séquence est `arr[-1]`, et l'inverser est simplement `arr[::-1]`. Vous pouvez accomplir beaucoup avec une syntaxe minimale en Python.

Java est également un bon choix. Mais comme vous devrez constamment déclarer les types dans votre code, cela signifie entrer des frappes supplémentaires. Cela ralentira la vitesse à laquelle vous codez et tapez. Ce problème sera plus apparent lorsque vous devrez écrire sur un tableau blanc lors des entretiens sur site.

Les raisons de choisir ou non C++ sont similaires à celles de Java. En fin de compte, Python, Java et C++ sont des choix décents. Si vous avez utilisé Java depuis un certain temps et que vous n'avez pas le temps de vous familiariser avec un autre langage, je recommande de rester avec Java plutôt que d'apprendre Python à partir de zéro. Cela vous évite d'avoir à utiliser un langage pour le travail et un autre pour les entretiens. La plupart du temps, le goulot d'étranglement est dans la réflexion et non dans l'écriture.

Une exception à la convention de permettre au candidat de "choisir n'importe quel langage de programmation qu'il veut" est lorsque l'entretien est pour un poste spécifique à un domaine, comme les rôles d'ingénieur front-end, iOS ou Android. Vous devez être familiarisé avec le codage d'algorithmes en JavaScript, Objective-C, Swift et Java, respectivement.

Si vous devez utiliser une structure de données que le langage ne supporte pas, comme une file d'attente ou un tas en JavaScript, demandez à l'interviewer si vous pouvez supposer que vous avez une structure de données qui implémente certaines méthodes avec des complexités temporelles spécifiées. Si l'implémentation de cette structure de données n'est pas cruciale pour résoudre le problème, l'interviewer l'autorisera généralement. 

En réalité, être conscient des structures de données existantes et sélectionner celles appropriées pour résoudre le problème en question est plus important que de connaître les détails d'implémentation complexes.

## Révisez vos bases en CS101

Si vous avez quitté l'université depuis un certain temps, il est fortement conseillé de réviser les fondamentaux de l'informatique. Je préfère les réviser en pratiquant. Je parcours mes notes de l'université et révise les différents algorithmes tout en travaillant sur les problèmes d'algorithmes de LeetCode et Cracking the Coding Interview.

Si vous êtes intéressé par la manière dont les structures de données sont implémentées, consultez [Lago](https://github.com/yangshun/lago), un dépôt GitHub contenant des exemples de structures de données et d'algorithmes en JavaScript.

%[https://github.com/yangshun/lago]

## Maîtrise par la pratique

Ensuite, acquérez de la familiarité et maîtrisez les algorithmes et les structures de données dans votre langage de programmation choisi.

Pratiquez et résolvez des questions d'algorithmes dans votre langage choisi. Bien que Cracking the Coding Interview soit une bonne ressource, je préfère résoudre des problèmes en tapant du code, en le faisant tourner et en obtenant un retour instantané. 

Il existe divers juges en ligne, tels que [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/), et [CodeForces](http://codeforces.com/) pour vous entraîner à répondre à des questions en ligne et vous habituer au langage. D'après mon expérience, les questions de LeetCode sont les plus similaires aux questions posées lors des entretiens. Les questions de HackerRank et CodeForces sont plus similaires aux questions de programmation compétitive. 

Si vous pratiquez suffisamment de questions de LeetCode, il y a de bonnes chances que vous voyiez ou complétiez l'une de vos vraies questions d'entretien (ou une variante de celle-ci).

Apprenez et comprenez les complexités temporelles et spatiales des opérations courantes dans votre langage choisi. Pour Python, cette [page](https://wiki.python.org/moin/TimeComplexity) sera utile. Apprenez également à connaître l'algorithme de tri sous-jacent utilisé dans la fonction `sort()` du langage et ses complexités temporelles et spatiales (en Python, c'est Timsort, qui est un hybride). 

Après avoir terminé une question sur LeetCode, j'ajoute généralement les complexités temporelles et spatiales du code écrit en commentaires au-dessus du corps de la fonction. J'utilise les commentaires pour me rappeler de communiquer l'analyse de l'algorithme après avoir terminé l'implémentation.

Lisez les recommandations de style de codage pour votre langage et respectez-les. Si vous choisissez Python, référez-vous au [Guide de style PEP 8](https://pep8.org/). Si vous choisissez Java, référez-vous au [Guide de style Java de Google](https://google.github.io/styleguide/javaguide.html).

Apprenez et soyez familier avec les pièges et les écueils courants du langage. Si vous les signalez pendant l'entretien et évitez de tomber dedans, vous gagnerez des points bonus et impressionnerez l'interviewer, peu importe si l'interviewer est familier avec le langage ou non.

Acquérez une large exposition à des questions de divers sujets. Dans la seconde moitié de l'article, je mentionne les sujets d'algorithmes et les questions utiles pour chaque sujet à pratiquer. Faites environ 100 à 200 questions LeetCode, et vous devriez être bon.

Si vous préférez des cours où l'apprentissage est plus structuré, voici quelques recommandations. **Prendre des cours en ligne n'est en aucun cas une obligation pour réussir les entretiens.**

* [AlgoMonster](https://algo.monster/) vise à vous aider à réussir l'entretien technique **dans le temps le plus court possible**. Par des ingénieurs de Google, AlgoMonster utilise une approche basée sur les données pour vous enseigner les motifs de questions clés les plus utiles et contient des ressources pour vous aider à réviser rapidement les structures de données et algorithmes de base. Le meilleur de tout, AlgoMonster n'est pas basé sur un abonnement - payez une fois et obtenez un **accès à vie**.
* [Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview) par Educative développe les questions pratiques recommandées dans cet article mais aborde la pratique d'un point de vue de motifs de questions, une approche avec laquelle je suis également d'accord pour l'apprentissage et que j'ai personnellement utilisée pour m'améliorer aux entretiens de codage. Le cours vous permet de pratiquer des questions sélectionnées en Java, Python, C++, JavaScript et fournit également des solutions d'exemple dans ces langages. Apprenez et comprenez les motifs, ne mémorisez pas les réponses.

Et bien sûr, pratiquez, pratiquez et pratiquez encore !

## Phases d'un entretien de codage

Félicitations, vous êtes prêt à mettre vos compétences en pratique ! Lors d'un entretien de codage, l'interviewer vous posera une question technique. Vous écrirez le code dans un éditeur collaboratif en temps réel (écran téléphonique) ou sur un tableau blanc (sur place), et aurez 30 à 45 minutes pour résoudre le problème. C'est là que le vrai plaisir commence !

Votre interviewer cherchera à voir si vous répondez aux exigences du poste. C'est à vous de lui montrer que vous avez les compétences. Au début, il peut sembler étrange de parler pendant que vous codez, car la plupart des programmeurs n'ont pas l'habitude d'expliquer à voix haute leurs pensées pendant qu'ils tapent du code.

Cependant, il est difficile pour l'interviewer de savoir ce que vous pensez en regardant simplement votre code. Si vous communiquez votre approche à l'interviewer avant même de commencer à coder, vous pouvez valider votre approche avec lui. De cette façon, vous deux pouvez vous mettre d'accord sur une approche acceptable.

## Préparation pour un entretien à distance

Pour les entretiens téléphoniques et à distance, ayez une feuille de papier et un stylo ou un crayon pour noter des notes ou des diagrammes. Si on vous pose une question sur les arbres et les graphes, il est généralement utile de dessiner des exemples de la structure de données.

Utilisez des écouteurs. Assurez-vous d'être dans un environnement calme. Vous ne voulez pas tenir un téléphone dans une main et taper avec l'autre. Essayez d'éviter d'utiliser des haut-parleurs. Si le retour est mauvais, la communication est rendue plus difficile. Devoir vous répéter ne fera que résulter en la perte de temps précieux.

## Que faire lorsque vous obtenez la question

De nombreux candidats commencent à coder dès qu'ils entendent la question. C'est généralement une grosse erreur. D'abord, prenez un moment et répétez la question à l'interviewer pour vous assurer que vous avez compris la question. Si vous avez mal compris la question, alors l'interviewer peut clarifier.

Demandez toujours des clarifications sur la question dès que vous l'entendez, même si vous pensez qu'elle est claire. Vous pourriez découvrir que vous avez manqué quelque chose. Cela permet également à l'interviewer de savoir que vous êtes attentif aux détails.

Envisagez de poser les questions suivantes.

* Quelle est la taille de l'entrée ?
* Quelle est la plage des valeurs ?
* Quels types de valeurs y a-t-il ? Y a-t-il des nombres négatifs ? Des nombres à virgule flottante ? Y aura-t-il des entrées vides ?
* Y a-t-il des doublons dans l'entrée ?
* Quels sont certains cas extrêmes de l'entrée ?
* Comment l'entrée est-elle stockée ? Si on vous donne un dictionnaire de mots, est-ce une liste de chaînes ou un trie ?

Après avoir suffisamment clarifié la portée et l'intention du problème, expliquez votre approche de haut niveau à l'interviewer, même si c'est une solution naïve. Si vous êtes bloqué, envisagez diverses approches et expliquez à voix haute pourquoi cela peut ou non fonctionner. Parfois, votre interviewer peut donner des indices et vous guider vers le bon chemin.

Commencez par une approche brute-force. Communiquez-la à l'interviewer. Expliquez les complexités temporelles et spatiales et clarifiez pourquoi c'est mauvais. Il est peu probable que l'approche brute-force soit celle que vous coderez. À ce stade, l'interviewer posera généralement la redoutable question, « Peut-on faire mieux ? ». Cela signifie qu'ils recherchent une approche plus optimale.

C'est généralement la partie la plus difficile de l'entretien. En général, recherchez le travail répété et essayez de l'optimiser en mettant potentiellement en cache le résultat calculé quelque part. Référez-vous plus tard, plutôt que de tout recalculer. Je fournis quelques conseils pour aborder les questions spécifiques aux sujets en détail ci-dessous.

Ne commencez à coder qu'après que vous et votre interviewer avez convenu d'une approche et que vous avez reçu le feu vert.

## Commencer à coder

Utilisez un bon style pour écrire votre code. Lire le code écrit par d'autres n'est généralement pas une tâche agréable. Lire du code horriblement formaté écrit par d'autres est encore pire. Votre objectif est de faire comprendre votre code à votre interviewer afin qu'il puisse rapidement évaluer si votre code fait ce qu'il est censé faire et s'il résout un problème donné. 

Utilisez des noms de variables clairs et évitez les noms qui sont des lettres uniques, sauf s'ils sont pour l'itération. Cependant, si vous codez sur un tableau blanc, évitez d'utiliser des noms de variables verbeux. Cela réduit la quantité d'écriture que vous devrez faire.

Expliquez toujours à l'interviewer ce que vous écrivez ou tapez. Il ne s'agit pas de lire, mot à mot, à l'interviewer le code que vous produisez. Parlez de la section du code que vous êtes en train d'implémenter à un niveau supérieur. Expliquez pourquoi il est écrit ainsi, et ce qu'il essaie d'accomplir.

Lorsque vous copiez et collez du code, considérez si c'est nécessaire. Parfois c'est le cas, parfois non. Si vous vous retrouvez à copier et coller un gros morceau de code s'étendant sur plusieurs lignes, c'est probablement un indicateur que vous pouvez restructurer le code en extrayant ces lignes dans une fonction. Si ce n'est qu'une seule ligne que vous avez copiée, généralement c'est bien. 

Cependant, n'oubliez pas de changer les variables respectives dans votre ligne de code copiée lorsque cela est pertinent. Les erreurs de copie et de collage sont une source courante de bugs, même dans le codage quotidien !

## Après avoir codé

Après avoir terminé de coder, n'annoncez pas immédiatement à l'interviewer que vous avez terminé. Dans la plupart des cas, votre code n'est généralement pas parfait. Il peut contenir des bugs ou des erreurs de syntaxe. Ce que vous devez faire, c'est réviser votre code.

Tout d'abord, parcourez votre code du début à la fin. Regardez-le comme s'il avait été écrit par quelqu'un d'autre, et que vous le voyez pour la première fois et essayez d'y repérer des bugs. C'est exactement ce que fera votre interviewer. Révisez et corrigez tout problème que vous pourriez trouver.

Ensuite, imaginez de petits cas de test et parcourez le code (pas votre algorithme) avec ces exemples d'entrée. 

Les interviewers aiment quand vous lisez dans leurs pensées. Ce qu'ils font généralement après que vous avez terminé de coder, c'est vous faire écrire des tests. C'est un énorme plus si vous écrivez des tests pour votre code même avant qu'ils ne vous le demandent. Vous devriez émuler un débogueur lorsque vous parcourez votre code. Notez ou dites-leur les valeurs de certaines variables lorsque vous guidez l'interviewer à travers les lignes de code.

S'il y a de grands morceaux de code dupliqués dans votre solution, restructurez le code pour montrer à l'interviewer que vous valorisez la qualité du code. De plus, recherchez les endroits où vous pouvez faire une [évaluation en court-circuit](https://fr.wikipedia.org/wiki/%C3%89valuation_par_court-circuit).

Enfin, donnez les complexités temporelles et spatiales de votre code, et expliquez pourquoi elles sont telles. Vous pouvez annoter des morceaux de votre code avec leurs diverses complexités temporelles et spatiales pour démontrer votre compréhension du code. Vous pouvez même fournir les API de votre langage de programmation choisi. Expliquez les compromis dans votre approche actuelle par rapport aux approches alternatives, éventuellement en termes de temps et d'espace.

Si votre interviewer est satisfait de la solution, l'entretien se termine généralement ici. Il est également courant que l'interviewer vous pose des questions d'extension, comme comment vous géreriez le problème si toute l'entrée est trop grande pour tenir en mémoire, ou si l'entrée arrive sous forme de flux. C'est une question de suivi courante chez Google, où ils se soucient beaucoup de l'échelle. 

La réponse est généralement une approche de type diviser pour régner — effectuer un traitement distribué des données et ne lire que certains morceaux de l'entrée depuis le disque en mémoire, écrire la sortie sur le disque et les combiner plus tard.

## Pratiquez avec des entretiens simulés

Les étapes mentionnées ci-dessus peuvent être répétées encore et encore jusqu'à ce que vous les ayez complètement intériorisées et qu'elles deviennent une seconde nature pour vous. Une bonne façon de pratiquer est de s'associer avec un ami et de prendre des tours pour s'interviewer mutuellement.

Une excellente ressource pour se préparer aux entretiens de codage est [interviewing.io](https://iio.sh/r/DMCa). Cette plateforme propose des entretiens de pratique gratuits et anonymes avec des ingénieurs de Google et Facebook, ce qui peut mener à de vrais emplois et stages. 

Grâce à l'anonymat pendant l'entretien, le processus d'entretien inclusif est sans biais et à faible risque. À la fin de l'entretien, l'interviewer et l'interviewé peuvent fournir des commentaires mutuels dans le but de s'aider à s'améliorer.

Réussir les entretiens simulés débloquera la page des emplois pour les candidats et leur permettra de réserver des entretiens (également anonymement) avec des entreprises de premier plan comme Uber, Lyft, Quora, Asana, et plus encore. Pour ceux qui sont nouveaux dans les entretiens de codage, un entretien de démonstration peut être visionné sur [ce site](https://start.interviewing.io/interview/9hV9r4HEONf9/replay). Notez que ce site nécessite que les utilisateurs se connectent.

J'ai utilisé interviewing.io, à la fois en tant qu'interviewer et en tant qu'interviewé. L'expérience était excellente. [Aline Lerner](https://www.freecodecamp.org/news/coding-interviews-for-dummies-5e048933b82b/undefined), la PDG et cofondatrice de interviewing.io, et son équipe sont passionnées par la révolution du processus des entretiens de codage et aident les candidats à améliorer leurs compétences en entretien. 

Elle a également publié un certain nombre d'articles liés aux entretiens de codage sur le [blog interviewing.io](http://blog.interviewing.io/). Je recommande de s'inscrire le plus tôt possible avec interviewing.io, même s'il est en version bêta, pour augmenter les chances de recevoir une invitation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-58.png)

Une autre plateforme qui vous permet de pratiquer les entretiens de codage est [Pramp](https://pramp.com/). Alors qu'interviewing.io met en relation des chercheurs d'emploi potentiels avec des interviewers expérimentés en codage, Pramp adopte une approche différente. Pramp vous associe à un autre pair qui est également un chercheur d'emploi. Vous alternez les rôles d'interviewer et d'interviewé. Pramp prépare également des questions et fournit des solutions et des invites pour guider l'interviewé.

## Allez de l'avant et conquérez

Après avoir fait un nombre équitable de questions sur LeetCode et avoir suffisamment pratiqué les entretiens simulés, allez de l'avant et mettez vos nouvelles compétences en entretien à l'épreuve. 

Postulez à vos entreprises préférées ou, mieux encore, obtenez des recommandations de vos amis travaillant pour ces entreprises. Les recommandations ont tendance à être remarquées plus tôt et à avoir un taux de réponse plus rapide que de postuler sans recommandation. Bonne chance !

## Conseils pratiques pour les questions de codage

Cette section plonge profondément dans des conseils pratiques pour des sujets spécifiques d'algorithmes et de structures de données, qui apparaissent fréquemment dans les questions de codage. De nombreuses questions d'algorithmes impliquent des techniques qui peuvent être appliquées à des questions de nature similaire.

Plus vous avez de techniques dans votre arsenal, plus vos chances de réussir l'entretien sont grandes. Pour chaque sujet, il y a également une liste de questions recommandées, qui est précieuse pour maîtriser les concepts de base. Certaines des questions ne sont disponibles qu'avec un abonnement payant à LeetCode, ce qui, à mon avis, en vaut absolument la peine si cela vous permet de décrocher un emploi.

## Conseils généraux

Validez toujours l'entrée en premier. Vérifiez les entrées qui sont invalides, vides, négatives ou différentes. Ne supposez jamais que vous avez reçu les paramètres valides. Alternativement, clarifiez avec l'interviewer si vous pouvez supposer une entrée valide (généralement oui), ce qui peut vous faire gagner du temps en évitant d'écrire du code qui valide l'entrée.

Y a-t-il des exigences ou des contraintes de complexité temporelle et spatiale ?

Vérifiez les erreurs de décalage d'un.

Dans les langages où il n'y a pas de coercition de type automatique, vérifiez que la concaténation des valeurs est du même type : `int`, `str`, et `list`.

Après avoir terminé votre code, utilisez quelques exemples d'entrées pour tester votre solution.

L'algorithme doit-il s'exécuter plusieurs fois, peut-être sur un serveur web ? Si oui, l'entrée peut probablement être pré-traitée pour améliorer l'efficacité de chaque appel d'API.

Utilisez un mélange de paradigmes de programmation fonctionnelle et impérative :

* Écrivez des fonctions pures aussi souvent que possible.
* Utilisez des fonctions pures car elles sont plus faciles à raisonner et peuvent aider à réduire les bugs dans votre implémentation.
* Évitez de muter les paramètres passés à votre fonction, surtout s'ils sont passés par référence, sauf si vous êtes sûr de ce que vous faites.
* Atteignez un équilibre entre précision et efficacité. Utilisez la bonne quantité de code fonctionnel et impératif là où c'est approprié. La programmation fonctionnelle est généralement coûteuse en termes de complexité spatiale en raison de la non-mutation et de l'allocation répétée de nouveaux objets. D'autre part, le code impératif est plus rapide car vous opérez sur des objets existants.
* Évitez de dépendre de la mutation de variables globales. Les variables globales introduisent un état.
* Assurez-vous de ne pas muter accidentellement des variables globales, surtout si vous devez en dépendre.

Généralement, pour améliorer la vitesse d'un programme, nous pouvons choisir soit d'utiliser une structure de données ou un algorithme approprié, soit d'utiliser plus de mémoire. C'est un compromis classique entre espace et temps.

Les structures de données sont vos armes. Choisir la bonne arme pour la bonne bataille est la clé de la victoire. Connaissez les forces de chaque structure de données et la complexité temporelle pour ses diverses opérations.

Les structures de données peuvent être augmentées pour atteindre une complexité temporelle efficace à travers différentes opérations. Par exemple, une HashMap peut être utilisée avec une liste doublement liée pour atteindre une complexité temporelle O(1) pour les opérations `get` et `put` dans un [cache LRU](https://leetcode.com/problems/lru-cache/).

Les HashMaps sont probablement les structures de données les plus couramment utilisées pour les questions d'algorithmes. Si vous êtes bloqué sur une question, votre dernier recours peut être d'énumérer les structures de données possibles (heureusement, il n'y en a pas tant que ça) et de considérer si chacune d'elles peut être appliquée au problème. Cela a fonctionné pour moi à certaines occasions.

Si vous prenez des raccourcis dans votre code, dites-le à voix haute à votre interviewer, et expliquez-lui ce que vous feriez en dehors d'un entretien (sans contraintes de temps). Par exemple, expliquez que vous écrirez une regex pour analyser une chaîne plutôt que d'utiliser `split`, qui ne couvre pas tous les cas.

## Séquence

#### **Notes**

Les tableaux et les chaînes sont considérés comme des séquences (une chaîne est une séquence de caractères). Il y a des conseils pour traiter à la fois les tableaux et les chaînes, qui seront couverts ici.

Y a-t-il des valeurs en double dans la séquence ? Cela affecterait-il la réponse ?

Vérifiez les dépassements de séquence.

Soyez attentif au découpage ou à la concaténation de séquences dans votre code. Typiquement, le découpage et la concaténation de séquences nécessitent un temps O(n). Utilisez des indices de début et de fin pour délimiter un sous-tableau ou une sous-chaîne lorsque cela est possible.

Parfois, vous parcourez la séquence du côté droit plutôt que du côté gauche.

Maîtrisez la [technique de la fenêtre glissante](https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems) qui s'applique à de nombreux problèmes de sous-chaînes ou de sous-tableaux.

Lorsque vous avez deux séquences à traiter, il est courant d'avoir un index par séquence pour les parcourir. Par exemple, nous utilisons la même approche pour fusionner deux tableaux triés.

#### **Cas particuliers**

* Séquence vide
* Séquence avec 1 ou 2 éléments
* Séquence avec des éléments répétés

## Tableau

#### **Notes**

Le tableau est-il trié ou partiellement trié ? Si c'est l'un ou l'autre, une forme de recherche binaire devrait être possible. Cela signifie généralement que l'interviewer recherche une solution plus rapide que O(n).

Pouvez-vous trier le tableau ? Parfois, trier le tableau en premier peut simplifier considérablement le problème. Assurez-vous que l'ordre des éléments du tableau n'a pas besoin d'être préservé avant d'essayer de le trier.

Pour les questions où la somme ou la multiplication d'un sous-tableau est impliquée, la pré-calcul utilisant le hachage ou une somme, un produit de préfixe ou de suffixe peut être utile.

Si vous avez une séquence et que l'interviewer demande un espace O(1), il peut être possible d'utiliser le tableau lui-même comme une table de hachage. Par exemple, si le tableau a des valeurs uniquement de 1 à N, où N est la longueur du tableau, négativer la valeur à cet index (moins un) pour indiquer la présence de ce nombre.

#### **Questions pratiques**

* [Two Sum](https://leetcode.com/problems/two-sum/)
* [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
* [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
* [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
* [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
* [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
* [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* [3Sum](https://leetcode.com/problems/3sum/)
* [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Binaire

#### **Liens d'étude**

* [Bits, Bytes, Building With Binary](https://medium.com/basecs/bits-bytes-building-with-binary-13cb4289aafa)

#### **Notes**

Les questions impliquant des représentations binaires et des opérations bit à bit sont parfois posées. Vous devez savoir comment convertir un nombre de la forme décimale en forme binaire, et vice versa, dans votre langage de programmation choisi.

Quelques extraits de code utiles :

* Tester si le k-ième bit est défini : `num & (1 << k) != 0`
* Définir le k-ième bit : `num |= (1 << k)`
* Éteindre le k-ième bit : `num &= ~(1 << k)`
* Basculer le k-ième bit : `num ^= (1 << k)`
* Pour vérifier si un nombre est une puissance de 2 : `num & num - 1 == 0`.

#### **Cas particuliers**

* Vérifier le débordement/sous-débordement
* Nombres négatifs

#### **Questions pratiques**

* [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
* [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
* [Counting Bits](https://leetcode.com/problems/counting-bits/)
* [Missing Number](https://leetcode.com/problems/missing-number/)
* [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

## Programmation dynamique

#### **Liens d'étude**

* [Demystifying Dynamic Programming](https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296)

#### **Notes**

La programmation dynamique (DP) est généralement utilisée pour résoudre des problèmes d'optimisation. [Alaina Kafkes](https://www.freecodecamp.org/news/coding-interviews-for-dummies-5e048933b82b/undefined) a écrit un [article génial](https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296) sur la résolution des problèmes de DP. Vous devriez le lire.

La seule façon de s'améliorer en DP est avec la pratique. Il faut beaucoup de pratique pour reconnaître qu'un problème peut être résolu par DP.

Pour optimiser l'espace, parfois vous n'avez pas à stocker toute la table DP en mémoire. Les deux dernières valeurs ou les deux dernières lignes de la matrice suffiront.

#### **Questions pratiques**

* [0/1 Knapsack](http://www.geeksforgeeks.org/knapsack-problem/)
* [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
* [Coin Change](https://leetcode.com/problems/coin-change/)
* [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* [Longest Common Subsequence](https://github.com/yangshun/tech-interview-handbook/blob/master/algorithms)
* [Word Break Problem](https://leetcode.com/problems/word-break/)
* [Combination Sum](https://leetcode.com/problems/combination-sum-iv/)
* [House Robber](https://leetcode.com/problems/house-robber/) et [House Robber II](https://leetcode.com/problems/house-robber-ii/)
* [Decode Ways](https://leetcode.com/problems/decode-ways/)
* [Unique Paths](https://leetcode.com/problems/unique-paths/)
* [Jump Game](https://leetcode.com/problems/jump-game/)

## Géométrie

#### **Notes**

Lorsque vous comparez la distance euclidienne entre deux paires de points, utiliser dx² + dy² est suffisant. Il est inutile de prendre la racine carrée de la valeur.

Pour savoir si deux cercles se chevauchent, vérifiez que la distance entre les deux centres des cercles est inférieure à la somme de leurs rayons.

### **Graphe**

#### **Liens d'étude**

* [From Theory To Practice: Representing Graphs](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)
* [Deep Dive Through A Graph: DFS Traversal](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)
* [Going Broad In A Graph: BFS Traversal](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255)

#### **Notes**

Soyez familier avec les diverses représentations de graphes et les algorithmes de recherche de graphes, ainsi qu'avec leurs complexités temporelles et spatiales.

Vous pouvez recevoir une liste d'arêtes et être chargé de construire votre propre graphe à partir des arêtes pour effectuer un parcours. Les représentations courantes de graphes sont

* Matrice d'adjacence
* Liste d'adjacence
* HashMap de HashMaps

Certaines entrées semblent être des arbres, mais ce sont en réalité des graphes. Clarifiez cela avec votre interviewer. Dans ce cas, vous devrez gérer les cycles et maintenir un ensemble de nœuds visités lors du parcours.

#### **Algorithmes de recherche de graphes**

* Courants : Parcours en largeur d'abord (BFS), Parcours en profondeur d'abord (DFS)
* Peu courants : Tri topologique, algorithme de Dijkstra
* Rares : algorithme de Bellman-Ford, algorithme de Floyd-Warshall, algorithme de Prim et algorithme de Kruskal

Dans les entretiens de codage, les graphes sont couramment représentés sous forme de matrices 2-D, où les cellules sont les nœuds et chaque cellule peut se déplacer vers ses cellules adjacentes (haut, bas, gauche et droite). Il est donc important d'être familier avec le parcours d'une matrice 2-D. 

Lors du parcours récursif de la matrice, assurez-vous toujours que votre prochaine position est dans les limites de la matrice. Plus de conseils pour faire du DFS sur une matrice peuvent être trouvés [ici](https://discuss.leetcode.com/topic/66065/python-dfs-bests-85-tips-for-all-dfs-in-matrix-question/). Un modèle simple pour faire du DFS sur une matrice ressemble à ceci :

```py
def traverse(matrix):
  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  def dfs(i, j):
    if (i, j) in visited:
      return
    visited.add((i, j))
    # Traverse neighbors
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols: # Check boundary
        # Add any other checking here ^
        dfs(next_i, next_j)
  for i in range(rows):
    for j in range(cols):
      dfs(i, j)
```

#### **Cas particuliers**

* Graphe vide
* Graphe avec un ou deux nœuds
* Graphes disjoints
* Graphe avec cycles

#### **Questions pratiques**

* [Clone Graph](https://leetcode.com/problems/clone-graph/)
* [Course Schedule](https://leetcode.com/problems/course-schedule/)
* [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
* [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
* [Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
* [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
* [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Intervalle

#### **Notes**

Les questions d'intervalle sont des questions qui donnent un tableau de tableaux à deux éléments (un intervalle). Les deux valeurs représentent une valeur de début et une valeur de fin. Les questions d'intervalle sont considérées comme faisant partie de la famille des tableaux, mais elles impliquent certaines techniques courantes. Elles ont donc leur propre section spéciale.

Un exemple de tableau d'intervalles : `[[1, 2], [4, 7]]`.

Les questions d'intervalle peuvent être délicates pour ceux qui n'ont pas d'expérience avec elles. Cela est dû au grand nombre de cas à considérer lorsque les tableaux d'intervalles se chevauchent.

Clarifiez avec l'interviewer si `[1, 2]` et `[2, 3]` sont considérés comme des intervalles qui se chevauchent, car cela affecte la manière dont vous écrirez vos vérifications d'égalité.

Une routine courante pour les questions d'intervalle est de trier le tableau d'intervalles par la valeur de début de chaque intervalle.

Soyez familier avec l'écriture de code pour vérifier si deux intervalles se chevauchent et pour fusionner deux intervalles qui se chevauchent :

```js
def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]
  
def merge_overlapping_intervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]
```

#### **Cas particuliers**

* Intervalle unique
* Intervalles non chevauchants
* Un intervalle totalement inclus dans un autre intervalle
* Intervalles dupliqués

#### **Questions pratiques**

* [Insert Interval](https://leetcode.com/problems/insert-interval/)
* [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
* [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) et [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
* [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## Liste chaînée

#### **Notes**

Comme les tableaux, les listes chaînées sont utilisées pour représenter des données séquentielles. L'avantage des listes chaînées est que l'insertion et la suppression de code de n'importe où dans la liste est O(1), alors que dans les tableaux, les éléments doivent être déplacés.

Ajouter un nœud fictif à la tête et/ou à la queue peut aider à gérer de nombreux cas limites où des opérations doivent être effectuées à la tête ou à la queue. La présence de nœuds fictifs garantit que les opérations ne devront jamais être exécutées sur la tête ou la queue. Les nœuds fictifs éliminent le casse-tête de l'écriture de vérifications conditionnelles pour gérer les pointeurs nuls. Assurez-vous de les supprimer à la fin de l'opération.

Parfois, un problème de liste chaînée peut être résolu sans stockage supplémentaire. Essayez d'emprunter des idées au problème d'inversion d'une liste chaînée.

Pour la suppression dans les listes chaînées, vous pouvez soit modifier les valeurs des nœuds, soit changer les pointeurs des nœuds. Vous devrez peut-être conserver une référence à l'élément précédent.

Pour partitionner les listes chaînées, créez deux listes chaînées séparées et rejoignez-les.

Les problèmes de listes chaînées partagent des similitudes avec les problèmes de tableaux. Réfléchissez à la manière dont vous résoudriez un problème de tableau et appliquez-le à une liste chaînée.

Les approches à deux pointeurs sont également courantes pour les listes chaînées :

* Obtenir le k-ième nœud depuis la fin : Avoir deux pointeurs, où l'un est _k_ nœuds devant l'autre. Lorsque le nœud devant atteint la fin, l'autre nœud est _k_ nœuds derrière.
* Détecter les cycles : Avoir deux pointeurs, où un pointeur incrémente deux fois plus que l'autre. Si les deux pointeurs se rencontrent, cela signifie qu'il y a un cycle.
* Obtenir le nœud du milieu : Avoir deux pointeurs. Un pointeur incrémente deux fois plus que l'autre. Lorsque le nœud le plus rapide atteint la fin de la liste, le nœud le plus lent sera au milieu.

Soyez familier avec les routines suivantes car de nombreuses questions sur les listes chaînées utilisent une ou plusieurs de ces routines dans leur solution.

* Compter le nombre de nœuds dans la liste chaînée
* Inverser une liste chaînée en place
* Trouver le nœud du milieu de la liste chaînée en utilisant des pointeurs rapides ou lents
* Fusionner deux listes ensemble

#### **Cas particuliers**

* Nœud unique
* Deux nœuds
* Liste chaînée avec cycle. Clarifiez avec l'interviewer s'il peut y avoir un cycle dans la liste. Généralement, la réponse est non.

#### **Questions pratiques**

* [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/)
* [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
* [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
* [Reorder List](https://leetcode.com/problems/reorder-list/)

## Math

#### **Notes**

Si le code implique une division ou un modulo, n'oubliez pas de vérifier le cas de division ou de modulo par 0.

Lorsque qu'une question implique "un multiple d'un nombre", le modulo peut être utile.

Vérifiez et gérez le débordement et le sous-débordement si vous utilisez un langage typé comme Java et C++. Au minimum, mentionnez que le débordement ou le sous-débordement est possible et demandez si vous devez le gérer.

Pensez aux nombres négatifs et aux nombres à virgule flottante. Cela peut sembler évident, mais lorsque vous êtes sous pression lors d'un entretien, de nombreux points évidents passent inaperçus.

Si la question demande d'implémenter un opérateur tel que la puissance, la racine carrée ou la division, et qu'il doit être plus rapide que O(n), la recherche binaire est généralement l'approche.

#### **Quelques formules courantes**

* Somme de 1 à N = (n+1) * n/2
* Somme de GP = 2⁰ + 2¹ + 2² + 2³ + … 2ⁿ = 2^(n+1)-1
* Permutations de N = N! / (N-K)!
* Combinaisons de N = N! / (K! * (N-K)!)

#### **Cas particuliers**

* Division par 0
* Débordement et sous-débordement d'entiers

#### **Questions pratiques**

* [Pow(x, n)](https://leetcode.com/problems/powx-n/)
* [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
* [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

## Matrice

#### **Notes**

Une matrice est un tableau à deux dimensions. Les questions impliquant des matrices sont généralement liées à la programmation dynamique ou au parcours de graphes.

Pour les questions impliquant un parcours ou une programmation dynamique, faites une copie de la matrice avec les mêmes dimensions initialisées à des valeurs vides. Utilisez ces valeurs pour stocker l'état visité ou la table de programmation dynamique. Soyez familier avec cette routine :

```py
rows, cols = len(matrix), len(matrix[0])
copy = [[0 for _ in range(cols)] for _ in range(rows)
```

* De nombreux jeux basés sur une grille peuvent être modélisés comme une matrice. Par exemple, Tic-Tac-Toe, Sudoku, Crossword, Connect 4, et Battleship. Il n'est pas rare de se voir demander de vérifier la condition de victoire du jeu. Pour des jeux comme Tic-Tac-Toe, Connect 4, et Crosswords, la vérification doit être faite verticalement et horizontalement. Une astuce consiste à écrire du code pour vérifier la matrice pour les cellules horizontales. Ensuite, transposez la matrice, réutilisant la logique utilisée pour la vérification horizontale afin de vérifier les cellules initialement verticales (qui sont maintenant horizontales).
* Transposer une matrice en Python est simplement :

```py
transposed_matrix = zip(*matrix)
```

#### **Cas particuliers**

* Matrice vide. Vérifiez qu'aucun des tableaux n'a une longueur de 0.
* Matrice 1 x 1.
* Matrice avec une seule ligne ou colonne.

#### **Questions pratiques**

* [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
* [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
* [Rotate Image](https://leetcode.com/problems/rotate-image/)
* [Word Search](https://leetcode.com/problems/word-search/)

## Récursivité

#### **Notes**

La récursivité est utile pour la permutation, car elle génère toutes les combinaisons et les questions basées sur les arbres. Vous devriez savoir comment générer toutes les permutations d'une séquence ainsi que comment gérer les doublons.

N'oubliez pas de toujours définir un cas de base afin que votre récursivité se termine.

La récursivité utilise implicitement une pile. Par conséquent, toutes les approches récursives peuvent être réécrites de manière itérative en utilisant une pile. 

Méfiez-vous des cas où le niveau de récursivité devient trop profond et provoque un débordement de pile (la limite par défaut en Python est 1000). Vous pourriez obtenir des points bonus en signalant cela à l'interviewer. 

La récursivité ne sera jamais de complexité spatiale O(1) car une pile est impliquée, sauf s'il y a une [optimisation de l'appel terminal](https://stackoverflow.com/questions/310974/what-is-tail-call-optimization) (TCO). Découvrez si votre langage choisi supporte la TCO.

#### **Questions pratiques**

* [Subsets](https://leetcode.com/problems/subsets/) et [Subsets II](https://leetcode.com/problems/subsets-ii/)
* [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/)

## Chaîne de caractères

#### **Notes**

Veuillez lire les conseils ci-dessus sur les [séquences](https://github.com/yangshun/tech-interview-handbook/tree/master/algorithms#sequence). Ils s'appliquent également aux chaînes de caractères.

Demandez à propos de l'ensemble de caractères d'entrée et de la sensibilité à la casse. Habituellement, les caractères sont limités aux caractères latins minuscules, par exemple de a à z.

Lorsque vous devez comparer des chaînes où l'ordre n'est pas important (comme un anagramme), vous pouvez envisager d'utiliser un HashMap comme compteur. Si votre langage dispose d'une classe `Counter` intégrée comme Python, demandez à l'utiliser à la place.

Si vous devez conserver un compteur de caractères, une erreur courante est de dire que la complexité spatiale requise pour le compteur est O(n). La complexité spatiale requise pour un compteur est O(1) et non O(n). Cela est dû au fait que la limite supérieure est la plage de caractères, qui est généralement une constante fixe de 26. L'ensemble d'entrée est simplement des caractères latins minuscules.

Les structures de données courantes pour rechercher des chaînes de manière efficace sont

* [Trie/Arbre de préfixes](https://fr.wikipedia.org/wiki/Trie)
* [Arbre de suffixes](https://fr.wikipedia.org/wiki/Arbre_de_suffixes)

Les algorithmes de chaînes courants sont

* [Rabin Karp](https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp), qui effectue des recherches efficaces de sous-chaînes, en utilisant un hachage roulant
* [KMP](https://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt), qui effectue des recherches efficaces de sous-chaînes

#### **Caractères non répétitifs**

Utilisez un masque de bits de 26 bits pour indiquer quels caractères latins minuscules sont à l'intérieur de la chaîne.

```py
mask = 0
for c in set(word):
  mask |= (1 << (ord(c) - ord('a')))
```

Pour déterminer si deux chaînes ont des caractères communs, effectuez un `&` sur les deux masques de bits. Si le résultat est non nul, `mask_a & mask_b > 0`, alors les deux chaînes ont des caractères communs.

#### **Anagramme**

Un anagramme est un jeu de mots ou un jeu de lettres. Il est le résultat de la réorganisation des lettres d'un mot ou d'une phrase pour produire un nouveau mot ou une nouvelle phrase, tout en utilisant toutes les lettres originales une seule fois. Lors des entretiens, généralement, nous ne nous préoccupons que des mots sans espaces.

Pour déterminer si deux chaînes sont des anagrammes, il existe plusieurs approches plausibles :

* Le tri des deux chaînes devrait produire la même chaîne résultante. Cela prend O(nlgn) de temps et O(lgn) d'espace.
* Si nous mappons chaque caractère à un nombre premier et que nous multiplions chaque nombre mappé ensemble, les anagrammes devraient avoir le même multiple (décomposition en facteurs premiers). Cela prend O(n) de temps et O(1) d'espace.
* Le comptage de la fréquence des caractères aidera à déterminer si deux chaînes sont des anagrammes. Cela prend également O(n) de temps et O(1) d'espace.

#### **Palindrome**

Un **palindrome** est un mot, une phrase, un [nombre](https://fr.wikipedia.org/wiki/Nombre_palindromique), ou une autre séquence de [caractères](https://fr.wikipedia.org/wiki/Caract%C3%A8re_(informatique)) qui se lit de la même manière à l'envers et à l'endroit, comme _madam_ ou _racecar_.

Voici des moyens de déterminer si une chaîne est un palindrome :

* Inversez la chaîne et elle devrait être égale à elle-même.
* Ayez deux pointeurs au début et à la fin de la chaîne. Déplacez les pointeurs vers l'intérieur jusqu'à ce qu'ils se rencontrent. À tout moment, les caractères aux deux pointeurs doivent correspondre.

L'ordre des caractères dans la chaîne compte, donc les HashMaps ne sont généralement pas utiles.

Lorsque qu'une question porte sur le comptage du nombre de palindromes, une astuce courante est d'avoir deux pointeurs qui se déplacent vers l'extérieur, loin du milieu. Notez que les palindromes peuvent être de longueur paire ou impaire. Pour chaque position de pivot central, vous devez la vérifier deux fois : une fois en incluant le caractère et une fois sans le caractère.

* Pour les sous-chaînes, vous pouvez terminer tôt dès qu'il n'y a pas de correspondance.
* Pour les sous-séquences, utilisez la programmation dynamique car il y a des sous-problèmes qui se chevauchent. Consultez [cette question](https://leetcode.com/problems/longest-palindromic-subsequence/).

#### **Cas particuliers**

* Chaîne vide
* Chaîne à un seul caractère
* Chaînes avec un seul caractère distinct

#### **Questions pratiques**

* [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
* [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)
* [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
* [Valid Anagram](https://leetcode.com/problems/valid-anagram)
* [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
* [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)
* [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
* [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
* [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

## Arbre

#### **Liens d'étude**

* [Leaf It Up To Binary Trees](https://medium.com/basecs/leaf-it-up-to-binary-trees-11001aaf746d)

#### **Notes**

Un arbre est un graphe non orienté et connecté sans cycle.

La récursivité est une approche courante pour les arbres. Lorsque vous remarquez que le problème de sous-arbre peut être utilisé pour résoudre l'ensemble du problème, essayez d'utiliser la récursivité.

Lorsque vous utilisez la récursivité, n'oubliez pas de vérifier le cas de base, généralement lorsque le nœud est `null`.

Lorsque vous êtes invité à parcourir un arbre par niveau, utilisez la recherche en profondeur d'abord.

Parfois, il est possible que votre fonction récursive doive retourner deux valeurs.

Si la question implique la somme des nœuds le long du chemin, assurez-vous de vérifier si les nœuds peuvent être négatifs.

Vous devriez être très familier avec l'écriture des parcours pré-ordre, in-ordre et post-ordre de manière récursive. En extension, défiez-vous en les écrivant de manière itérative. Parfois, les interviewers demandent aux candidats l'approche itérative, surtout si le candidat termine d'écrire l'approche récursive trop rapidement.

## Arbre binaire

Le parcours in-ordre d'un arbre binaire est insuffisant pour sérialiser un arbre de manière unique. Le parcours pré-ordre ou post-ordre est également requis.

## Arbre binaire de recherche (BST)

Le parcours in-ordre d'un BST vous donnera tous les éléments dans l'ordre.

Soyez très familier avec les propriétés d'un BST. Validez qu'un arbre binaire est un BST. Cela revient plus souvent que prévu.

Lorsque qu'une question implique un BST, l'interviewer recherche généralement une solution qui s'exécute plus rapidement que O(n).

#### **Cas particuliers**

* Arbre vide
* Nœud unique
* Deux nœuds
* Arbre très déséquilibré (comme une liste chaînée)

#### **Questions pratiques**

* [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
* [Same Tree](https://leetcode.com/problems/same-tree/)
* [Invert or Flip Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
* [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
* [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
* [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
* [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
* [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
* [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
* [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
* [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Tries

#### **Liens d'étude**

* [Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
* [Implement Trie (Prefix Tree)](https://leetcode.com/articles/implement-trie-prefix-tree/)

#### **Notes**

Les tries sont des arbres spéciaux (arbres de préfixes) qui rendent la recherche et le stockage de chaînes plus efficaces. Les tries ont de nombreuses applications pratiques, telles que la réalisation de recherches et la fourniture de suggestions de saisie automatique. Il est utile de connaître ces applications courantes afin de pouvoir identifier facilement lorsqu'un problème peut être résolu efficacement à l'aide d'un trie.

Parfois, le prétraitement d'un dictionnaire de mots (donné dans une liste) dans un trie améliorera l'efficacité de la recherche d'un mot de longueur _k_ parmi _n_ mots. La recherche devient O(k) au lieu de O(n).

Soyez familier avec l'implémentation, à partir de zéro, d'une classe `Trie` et de ses méthodes `add`, `remove` et `search`.

#### **Questions pratiques**

* [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)
* [Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design)
* [Word Search II](https://leetcode.com/problems/word-search-ii/)

## Tas

#### **Liens d'étude**

* [Learning to Love Heaps](https://medium.com/basecs/learning-to-love-heaps-cef2b273a238)

#### **Notes**

Si vous voyez un top ou un plus bas _k_ mentionné dans la question, c'est généralement un signe qu'un tas peut être utilisé pour résoudre le problème, comme dans [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/).

Si vous avez besoin des _k_ éléments les plus élevés, utilisez un Min Heap de taille _k_. Parcourez chaque élément, en le poussant dans le tas. Chaque fois que la taille du tas dépasse _k_, retirez l'élément minimum. Cela garantira que vous avez les _k_ éléments les plus grands.

#### **Questions pratiques**

* [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
* [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## Conclusion

Les entretiens de codage sont difficiles. Mais heureusement, vous pouvez vous améliorer en les étudiant et en vous y préparant, et en faisant des entretiens simulés.

Pour résumer, pour bien réussir les entretiens de codage :

1. Choisissez un langage de programmation
2. Étudiez les fondamentaux de l'informatique
3. Pratiquez la résolution de questions algorithmiques
4. Intériorisez les [À faire et À ne pas faire des entretiens](https://github.com/yangshun/tech-interview-handbook/blob/master/preparing/cheatsheet.md)
5. Pratiquez en faisant des entretiens techniques simulés
6. Réussissez l'entretien pour obtenir le poste

En suivant ces étapes, vous améliorerez vos compétences en entretien de codage et serez un pas plus proche (ou probablement plus) de décrocher l'emploi de vos rêves.

Bonne chance !

Le contenu de cet article [peut être trouvé ici](https://www.techinterviewhandbook.org/). Les futures mises à jour seront publiées là-bas. Les demandes de tirage pour suggestions et corrections sont les bienvenues.

Si vous avez aimé cet article, partagez-le avec vos amis !

Vous pouvez également me suivre sur [GitHub](https://github.com/yangshun) et [Twitter](https://twitter.com/yangshunz).