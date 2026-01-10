---
title: 'Comment poser des questions efficaces : Un guide pratique pour les développeurs'
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2020-05-12T08:20:49.000Z'
originalURL: https://freecodecamp.org/news/asking-effective-questions-a-practical-guide-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/asking-effectively.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: career advice
  slug: career-advice
- name: debugging
  slug: debugging
- name: Developer
  slug: developer
- name: Google
  slug: google
- name: Problem Solving
  slug: problem-solving
- name: programing
  slug: programing
- name: research
  slug: research
seo_title: 'Comment poser des questions efficaces : Un guide pratique pour les développeurs'
seo_desc: 'Learning is a journey that never ends. At every point in your career, you
  will keep learning, re-learning, and un-learning.

  The ability to find answers to problems is key, and these answers can be gotten
  by either debugging, googling or asking questi...'
---

L'apprentissage est un voyage qui ne se termine jamais. À chaque étape de votre carrière, vous continuerez à apprendre, réapprendre et désapprendre.

La capacité à trouver des réponses aux problèmes est essentielle, et ces réponses peuvent être obtenues en débogant, en cherchant sur Google ou en posant des questions. Ce sont des compétences que tout le monde devrait apprendre.

Bien que poser des questions soit une bonne chose, le faire de manière incorrecte ou moins efficace peut conduire à des heures de travail improductif. Dans cet article, je vous montre comment poser des questions efficaces, devenir un meilleur utilisateur de Google et affiner vos compétences en résolution de problèmes.

## La méthode Lire Chercher Demander

freeCodeCamp a mis au point cette méthode incroyable pour ses étudiants appelée la méthode [Lire Chercher Demander](https://www.freecodecamp.org/forum/t/how-to-get-help-when-you-are-stuck-coding/19514) où vous pouvez résoudre vos problèmes efficacement tout en respectant le temps des autres.

Il est attendu que vous suiviez ces étapes dans l'ordre avant de poser une question.

* **Lire** l'erreur ou la documentation

* **Chercher** sur Google ou Stackoverflow

* **Demander** de l'aide

### Lire vos erreurs

La première étape pour trouver une solution à votre problème est de comprendre le problème lui-même. De nombreux développeurs posent des questions sans comprendre le problème. Rappelez-vous que vous voulez poser des questions efficacement et aussi respecter le temps de la personne à qui vous allez demander.

Le plus souvent, les réponses à vos bugs se trouvent dans les erreurs elles-mêmes. Ce n'est pas respectueux de poser des questions que vous auriez pu résoudre vous-même si vous aviez lu l'erreur.

Une excellente façon de déboguer vos erreurs est de journaliser l'erreur sur votre console ou terminal et de lire les erreurs. Cinq choses peuvent se produire à cette étape :

* Vous identifiez le bug

* Vous déterminez l'emplacement du bug (possiblement un fichier ou une section de votre code)

* Vous comprenez la ou les causes du bug

* Vous esquissez les corrections possibles du bug

* Vous implémentez les corrections possibles

Le plus souvent, juste cette étape seule peut vous aider à résoudre votre problème. Plus vous pratiquez cela, meilleur vous devenez en débogage et en correction de problèmes. Certains bugs peuvent être plus complexes que votre capacité, et alors vous devez chercher de l'aide ou des ressources externes.

### Lire la Documentation

Supposons que vous n'ayez pas pu corriger vos problèmes à partir de la première étape (mais que vous ayez au moins pu identifier le bug). Alors vous devez lire une documentation.

Cela peut ne pas s'appliquer à tous les bugs, mais assurez-vous de passer votre problème par cette étape avant de passer à la suivante. Après avoir identifié votre bug, il est temps de déterminer la cause et d'esquisser les corrections possibles.

> La documentation est un ensemble de documents fournis sur papier, ou en ligne, ou sur des médias numériques ou analogiques, tels que des cassettes audio ou des CD. Des exemples sont les guides utilisateur, les livres blancs, l'aide en ligne, les guides de référence rapide. La documentation papier ou imprimée est devenue moins courante. ~ [Wikipedia](https://en.wikipedia.org/wiki/Documentation)

La documentation sert de guide officiel pour un langage de programmation, un framework, une bibliothèque ou une technologie particulière. Le meilleur endroit pour obtenir une ressource de première main sur un problème spécifique est de consulter le guide d'aide officiel de la technologie.

Vous avez peut-être mal configuré quelque chose, installé un mauvais package ou oublié d'importer quelque chose. Mais lorsque vous lisez les docs de la technologie responsable du bug, cela peut vous aider à trouver une solution rapidement.

Récemment, je travaillais sur un projet Gatsby, et j'ai rencontré des erreurs de console et une page blanche en production. Mais cela ne se produisait pas en développement.

```python
TypeError: t.test is not a function
```

Si vague, n'est-ce pas ? Après avoir identifié l'emplacement du bug, lu les docs et essayé plusieurs corrections, j'ai découvert quelque chose : dans la configuration du plugin Google Analytics de Gatsby, j'ai laissé le tableau destiné à éviter l'envoi de hits de pageview depuis des chemins personnalisés vide.

```python
plugins: [
    {
      resolve: `gatsby-plugin-google-analytics`,
      options: {
        trackingId: 'UA-XXXXXXXX-1',
        head: false,
        anonymize: true,
        respectDNT: true,
        exclude: [''],
        pageTransitionDelay: 0,
      }
]
```

Après 3 heures de lecture de l'erreur, d'essais pour identifier le bug et de lecture des docs de Gatsby, j'ai compris que l'option `exclude[]` n'avait aucune valeur. La suppression de cela a résolu mon problème puisque je n'avais pas besoin d'exclure une page après tout.

Cela montre pourquoi vous devriez passer du temps à déboguer. Cela peut prendre du temps, et ce sera frustrant. Le bug peut sembler stupide, la correction peut être simple, mais cela en vaut la peine. Plus vous passez de temps à déboguer, meilleur vous devenez et plus vite vous corrigerez des bugs encore plus complexes la prochaine fois.

### Chercher

Maintenant, si vous avez lu vos erreurs et plusieurs docs, mais que votre bug devient plus complexe, il est temps de chercher sur le web "efficacement".

L'un des meilleurs endroits pour chercher des solutions à vos problèmes est [Google](https://google.com) puisqu'il crawl déjà le contenu de nombreuses pages web, communautés de développeurs et docs comme [StackOverflow](https://stackoverflow.com/), [Hashnode](https://hashnode.com/), [freeCodeCamp News](https://www.freecodecamp.org/news/), [MDN](https://developer.mozilla.org/en-US/docs/Web), [CSS tricks](https://css-tricks.com/), [Hackernoon](https://hackernoon.com/), et bien d'autres.

Voici quelques conseils de recherche Google utiles que vous pouvez essayer pour obtenir des réponses plus efficacement :

* Ajoutez un domaine spécifique pour canaliser votre recherche vers un site web particulier et gagner du temps. Vous pouvez ajouter `site: nomdusite` à votre recherche, et il ne retournera que les résultats de ce site web.

![Screen Shot 2020-05-12 at 12.49.06 PM.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1589268176790/vwk3EmzK9.png align="left")

* Cherchez un titre spécifique et du texte dans des sites spécifiques. Cela permettra à vos résultats d'inclure des ressources liées au mot-clé de titre ou de texte que vous avez spécifié.

> intitle:axe

> intitle:axe intext:web ui testing

> intitle:axe intext:web ui testing site:bolajiayodeji.com

![Screen Shot 2020-05-12 at 12.48.59 PM.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1589268185857/KA_B5_TTq.png align="left")

* Ajoutez des mots-clés spécifiques à votre recherche et extrayez des détails individuels comme les chemins de fichiers. Si votre bug est lié à Python, ajoutez-le à votre requête de recherche. S'il est lié à des objets, ajoutez cela aussi. Cela rationalisera les résultats à une plus large gamme de ressources possibles liées à votre bug, puisque des objets existent dans presque tous les langages de programmation.

* Google omet automatiquement la plupart des caractères non alphanumériques de vos requêtes. Les symboles comme **\`!@#$%^&\*(){}\[\]&lt;&gt;** ne sont pas inclus dans votre recherche. Vous pouvez donc vous concentrer sur des mots-clés plus spécifiques, comme discuté ci-dessus.

* Copiez et collez vos erreurs (en supprimant les informations spécifiques) ; il y a 99,9 % de chances que quelqu'un d'autre ait rencontré la même erreur et ait peut-être ouvert un problème ou écrit un article à ce sujet. Ne sous-estimez jamais le pouvoir de StackOverflow et des problèmes GitHub.

* Cherchez dans les dernières années puisque la programmation change assez rapidement. Cela garantira que vous ne tombiez pas sur des ressources redondantes.

* Répétez, essayez différents mots-clés et des mots-clés plus généraux plusieurs fois, et ouvrez plusieurs onglets jusqu'à ce que vous trouviez une réponse. Cela peut sembler étrange au début, mais en faisant cela de manière constante, vous vous améliorerez, et avec le temps, cela vous prendra moins de temps et moins d'onglets pour trouver une réponse.

### Demander

Maintenant vient le diamant tant recherché. Je vous conseillerais, avant de poser QUELLE QUE SOIT la question, de vous assurer que vous avez terminé les étapes 1 et 2.

Cela peut être difficile, mais plus vous vous y habituez tôt, mieux vous grandissez. J'ai eu des gens qui m'ont posé des questions, et quand j'ai copié et collé leur question dans Google, le premier résultat répondait à la question à 100 %. Cela ne se sent pas bien.

Le plus souvent, je devrais leur envoyer le lien. Pendant ce temps, ils auraient pu le faire eux-mêmes et m'économiser du temps tout en améliorant leurs compétences en résolution de problèmes.

Même si votre voisin travaille chez Google, si votre père est ingénieur logiciel, si votre ami proche a deux ans d'expérience de plus que vous, essayez de ne pas leur poser de questions jusqu'à ce que vous ayez investi du temps à trouver des solutions vous-même. Cela vous aidera à :

* Construire plus de confiance en soi, car vous n'aurez pas besoin de dépendre autant des autres. (Et si cet ami proche n'est pas disponible pour vous répondre un jour, que ferez-vous ?!)

* Économiser le temps de la personne à qui vous prévoyez de poser des questions. Il y a des tonnes de développeurs dans le monde, et vous n'êtes peut-être pas le seul à poser des questions à cette même personne. En complétant les étapes 1 et 2 d'abord, vous aidez également les autres avec moins d'expérience ou des problèmes plus complexes à obtenir des réponses rapidement.

* Construire vos compétences en résolution de problèmes, en débogage, en recherche et en utilisation de Google. Ce sont des compétences essentielles qui vous aideront à devenir un meilleur développeur. Vous ne maîtrisez une compétence que lorsque vous la pratiquez de manière constante, alors essayez de pratiquer cela régulièrement et regardez-vous grandir et maîtriser l'art.

%[https://twitter.com/iambolajiayo/status/1255694731482365952]

Mais disons que vous avez terminé les deux étapes, et que vous avez encore besoin d'aide externe d'un mentor, d'un développeur senior, d'un chef d'équipe, de la communauté locale, du groupe ou d'un ami. Comment alors poser des questions efficacement ?

* Complétez l'étape 1 et assurez-vous de comprendre déjà le problème

* Complétez l'étape 2 afin d'avoir au moins quelques idées sur les causes et solutions possibles du problème

* Maintenant, faites quelques recherches : vous posez soit la question dans des communautés de développeurs comme [Stackoverflow](https://stackoverflow.com/) ou [Hashnode](https://hashnode.com/), soit vous demandez de l'aide à une personne que vous pensez avoir plus d'expérience que vous.

* Les développeurs qui répondent aux questions dans les communautés de développeurs sacrifient leur temps pour vous aider. Aidez-les également en posant des "questions claires et concises". Vous devez choisir vos mots délibérément et précisément, en construisant vos phrases soigneusement pour éviter la confusion. À partir des étapes 1 et 2, rédigez correctement vos questions en fonction de :

    * Le "problème" que vous avez rencontré

    * Vos pensées sur ce que vous pensez qui pourrait être faux "basé sur vos recherches".

    * Preuve des efforts de recherche (Les développeurs seront plus heureux de vous aider une fois qu'ils verront que vous avez déjà fait quelques efforts). Ajoutez des liens vers les ressources que vous avez vérifiées et les solutions que vous avez déjà essayées.

    * Soyez familier avec des outils comme [CodePen](https://codepen.io/), [CodeSandBox](https://codesandbox.io/), [GitHub Gist](https://gist.github.com/), [Repl.it](https://repl.it/), et [GitHub](https://github.com/) afin de pouvoir facilement fournir un lien vers un extrait de votre code, un projet fonctionnel ou une [reproduction minimale](https://gist.github.com/Rich-Harris/88c5fc2ac6dc941b22e7996af05d70ff) sans avoir à taper trop de texte. **Veuillez essayer autant que possible de ne pas coller de code qui fait plus d'une ligne dans le chat.**

    * Prenez des captures d'écran claires et nettes lorsque cela est nécessaire. Le plus souvent, vous pouvez prendre une capture de vos erreurs de console pour des problèmes plus petits. Essayez de ne pas fatiguer les yeux de votre aide. Prenez des captures d'écran spécifiques et claires liées à votre erreur.

* Assurez-vous de poser la question à la bonne personne ou communauté. Ne posez pas une question liée à Python à quelqu'un qui ne connaît que Java. Vos recherches de l'étape précédente vous aideront ici. Il est également bon de marquer des communautés, des individus ou des groupes spécifiques où vous poserez régulièrement des questions en fonction de la pertinence de leurs réponses pour vous.

* Maintenant, n'ayez pas peur de demander. J'ai eu ma part de réponses toxiques de la part de personnes qui répondent avec des commentaires comme "c'est simple", "allez, googlez-le", "vous devriez savoir cela", et vous pourriez obtenir cela aussi :(. L'internet est une combinaison de bonnes et de personnes toxiques qui peuvent être ou non accueillantes. Ayez confiance en vous, vous avez fait votre part en complétant les étapes 1 et 2, alors posez la question librement.

## Conclusion

Vous n'avez pas besoin de "tout savoir", vous devez simplement "savoir et savoir comment et où trouver plus de connaissances".

Cher 10x, Senior, "C'est Simple", Ingénieur : veuillez noter que vous découragez les développeurs qui posent ces questions. J'ai dû lutter beaucoup avec ma confiance en moi il y a quelques années, et cela m'a pris un certain temps pour m'en remettre.

Il y a déjà tant de choses avec lesquelles les apprenants doivent lutter (apprentissage, syndrome de l'imposteur et problèmes personnels), alors veuillez ne pas ajouter à cela. Soyez accueillant, faites-les sentir comme s'ils appartenaient ici, et soutenez-les.

Votre réponse peut influencer intentionnellement ou non la décision de quelqu'un de poser des questions librement la prochaine fois. Si vous ne pouvez pas ou ne serez pas disponible, vous pouvez soit ne pas répondre du tout, soit répondre de manière amicale avec des commentaires.

Orientez les gens vers vos amis si vous n'avez pas le temps ou les capacités de vous occuper d'eux, donnez des critiques constructives et essayez de ne pas laisser une question sans commentaire ou impact.

> Les développeurs débutants ont besoin de soutien. Apprendre à coder est difficile, surtout si vous le faites seul. Si vous apprenez dans une salle de classe traditionnelle, assurez-vous de réseauter avec les autres étudiants. Faites vos devoirs ensemble. Discutez des problèmes. Si vous apprenez en ligne, il est très facile de se décourager. Trouvez des espaces de discussion avec d'autres personnes qui sont sur un chemin similaire et utilisez cet espace pour vous encourager mutuellement. Twitter rend également les experts accessibles pour vous (raison #49948 pour laquelle j'aime Twitter). Trouvez les experts dans ce que vous apprenez et consommez leur contenu. Posez-leur des questions si vous en avez besoin. L'important est de ne pas le faire seul. ~ [Angie Jones](https://townhall.hashnode.com/women-in-tech-angie-jones-cjyodxwfc003ls8s10syrzvq7)

L'industrie grandit chaque jour. Nous essayons tous d'apprendre et de nous améliorer à différents niveaux. De nombreuses communautés de développeurs sont solidaires et mettent leurs ressources à disposition. Assurez-vous de faire partie de ce mouvement, consommez ces ressources disponibles, contribuez à ces ressources et soyez un aideur de toutes les manières possibles.

Merci à tous les développeurs incroyables à travers le monde, créant et partageant des contenus/projets. Vos contributions sont les piliers qui soutiennent l'écosystème technologique aujourd'hui. ??

> Note rapide, j'interviewe des femmes incroyables dans la tech sur [She Inspires](https://hashnode.com/series/she-inspires-cjt0d02lq001e7ps2wo420g15) sur [Hashnode](https://hasnode.com) où je comprends l'état actuel de l'industrie technologique, j'obtiens des informations sur leur croissance personnelle et professionnelle, et j'inspire d'autres femmes à devenir meilleures. Lisez toutes les interviews passées [ici](https://hashnode.com/series/she-inspires-cjt0d02lq001e7ps2wo420g15), faites-moi confiance, cela vaut votre temps. :)

Ne passez pas toute votre vie à attendre le meilleur moment pour faire ce pas – écrivez cet article, construisez ce projet parallèle, postulez pour cet emploi ou posez cette question aujourd'hui. Le meilleur moment est toujours maintenant !