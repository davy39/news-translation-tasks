---
title: Donnez un bilan de santé à votre Front End
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-20T04:54:16.000Z'
originalURL: https://freecodecamp.org/news/give-your-front-end-a-health-check-952c857ecdb4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6g5YyCI8qhLbQP5QVdJ3Dw.jpeg
tags:
- name: Design
  slug: design
- name: learning to code
  slug: learning-to-code
- name: QA
  slug: qa
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Donnez un bilan de santé à votre Front End
seo_desc: 'By Ewa Mitulska-Wójcik

  You’ve built out all your user stories and your app is working. Now’s it’s ready
  to submit as done, so you can move on with your life.

  Not so fast!

  You need to give your code a health check first.

  A professional singer wouldn’t...'
---

Par Ewa Mitulska-Wójcik

Vous avez développé toutes vos user stories et votre application fonctionne. Maintenant, elle est prête à être soumise comme terminée, afin que vous puissiez passer à autre chose.

Pas si vite !

Vous devez d'abord donner un bilan de santé à votre code.

Un chanteur professionnel ne commencerait pas à chanter avant d'avoir vérifié à la fois son micro et ses haut-parleurs. Vous ne devriez pas déployer avant d'avoir vérifié votre front end, votre back end, et tout ce qui se trouve entre les deux.

Je suis une personne impatiente, mais le codage me fait ralentir. Être développeur m'apprend à réfléchir au moins deux fois, à poser des questions jusqu'à ce que le code fonctionne, et à attendre un moment avant de célébrer le succès.

L'itération est la clé car un bon produit n'est jamais terminé. La clé est d'itérer sur les versions dont vous êtes fier, et non sur celles qui sont loin d'être prêtes à être mises en ligne.

Alors traitez cela comme une checklist finale avant de passer en production.

#### 1. Soyez réactif

Comment votre application se comporte-t-elle lorsque vous redimensionnez la fenêtre du navigateur ? Où se trouvent vos points de rupture dans le code ? Est-elle suffisamment fluide pour s'adapter à toutes les tailles sans gros problèmes ?

Il existe une variété infinie de tailles d'écran. Il est impossible d'avoir tous les appareils à portée de main, mais il est facile d'émuler leur comportement.

En passant du temps dans la [Code Review Room](http://gitter.im/freecodecamp/codereview), j'ai remarqué que beaucoup de gens se concentrent sur le développement pour les ordinateurs de bureau alors qu'ils devraient en fait tester leur application sur des appareils mobiles en premier.

Les outils des navigateurs nous permettent d'émuler l'affichage sur diverses tailles d'écran et orientations. Utilisez-les, ils sont gratuits.

Dans Chrome, vous pouvez accéder à une vue de débogage en cliquant avec le bouton droit sur n'importe quel élément de la page et en sélectionnant « inspecter l'élément », puis en allant en vue mobile et en émulant différents appareils.

![Image](https://cdn-media-1.freecodecamp.org/images/-ua5KuSR5Dd8cRXMnqINmcIOz671tz2jcycX)
_Mode d'émulation du navigateur Chrome_

#### 2. Considérez les cas particuliers et les états de l'application

Vide, erreur, succès, attente, page 404, ou clics dupliqués sur un bouton en attendant la réponse de l'API — comment votre application réagit-elle à ces situations ? Vous souciez-vous de ces états qui sont loin de la situation idéale pour laquelle vous avez codé ? Avez-vous des retours utiles pour vos utilisateurs lorsqu'ils rencontrent ces problèmes ? Avez-vous testé ces cas particuliers ? Écoutez-vous et répondez-vous dans votre application, ou est-ce que vous faites tout le discours ?

[Concevez, codez et testez pour tous les états](https://medium.com/@_mikehlee/designing-for-various-states-823816e49c8d#.4x0p9y4oh). Vérifier les flux utilisateurs peut vous aider beaucoup à vous débarrasser de ces points facilement oubliés et des impasses. Testez simplement votre travail avec quelques utilisateurs, ou au moins faites-le vous-même.

Mettez-vous à la place des utilisateurs en imaginant divers scénarios qui pourraient se produire, et rappelez-vous que cette application est complètement nouvelle pour cette personne.

Essayez des entrées de données incorrectes, aucune entrée du tout, des fautes d'orthographe, etc. Soyez imaginatif et essayez de casser votre code ! Mieux vaut que ce soit vous qui le fassiez avant vos utilisateurs.

#### 3. Optimisez vos performances

[Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) fait un excellent travail en vous disant ce qui pourrait être fait mieux.

Si vous voulez que d'autres puissent lire et examiner votre code, ne minifiez pas votre JavaScript ou CSS — cela rendra la lecture difficile pour les humains. Cependant, vous devriez le faire pour le code de production.

Pour la production, vous pouvez également utiliser des outils tels que [Grunt](http://gruntjs.com/) pour gérer et optimiser d'autres opérations pour vous.

En utilisant des tests tels que [PageSpeed](https://developers.google.com/speed/pagespeed/insights/), vous pouvez obtenir rapidement un avis non seulement sur les performances, mais aussi sur les problèmes d'utilisabilité. Les résultats des tests vous fournissent des suggestions prêtes à l'emploi pour améliorer votre code. Encore une fois, vous n'avez pas à accepter toutes les suggestions, choisissez simplement celles qui correspondent aux objectifs que vous souhaitez atteindre.

![Image](https://cdn-media-1.freecodecamp.org/images/gpyC5h6k-8EULkJEbqmpvG2NT4pYEyvijyox)
_Vérification de base de la santé UX avec l'outil PageSpeed_

#### 4. Faites des tests multi-navigateurs sur chaque appareil disponible

Beaucoup d'entre nous ont accès à au moins deux appareils différents (un ordinateur et un smartphone), et certains d'entre nous utilisent même des systèmes d'exploitation en dual boot. L'émulation de navigateur a ses défauts, alors utilisez le matériel natif lorsque cela est possible.

Vous n'avez pas à écrire des tests unitaires pour une petite application montrant des entrées wiki ou la météo locale pour vérifier si elles fonctionnent. Le développement piloté par les tests est une excellente pratique, mais pas la plus facile pour les nouveaux codeurs et cela peut être un excès de forme pour de courts extraits de code.

Ce dont vous devez être conscient, cependant, c'est que les tests font partie du travail d'un développeur front end, même s'il y a une énorme équipe de testeurs assise à côté de vous dans la même pièce. Avant d'assigner le ticket à un autre membre de l'équipe, vous devez vous assurer que cela fonctionne. Ne supposez pas, vérifiez.

Avec le code, cela fonctionne ou cela ne fonctionne pas. Il n'y a pas de _peut-être_ ou _je suppose_.

![Image](https://cdn-media-1.freecodecamp.org/images/Y4dBc-Jlv6Z9-VNPTUFTbneB2IlZyDJLjDIL)

Les tests multi-navigateurs peuvent être chronophages, mais il existe de nombreuses astuces pour les rendre plus efficaces. Par exemple, chaque fois que vous testez, essayez d'utiliser un navigateur différent.

Puisque vous le testez pendant que vous itérez sur le projet, vous pouvez tester votre code sur divers navigateurs plusieurs fois pendant la création de l'application elle-même. Ensuite, avant de lancer la version finale, il est beaucoup plus rapide de faire une vérification rapide de la santé du navigateur, puisque la majorité des problèmes ont probablement déjà été découverts et corrigés.

Les outils de développement des navigateurs et les extensions vous permettent également de découvrir facilement les contraintes d'accessibilité avant de mettre le projet en ligne. Vous pouvez également utiliser [BrowserStack](https://www.browserstack.com/), que j'ai trouvé utile pour faire des tests multi-navigateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/iaaki3R1d6VJli-BPruuxZjZfK7AMZ44i0NE)
_Audits d'accessibilité dans Chrome_

J'ai récemment [une belle checklist d'accessibilité](http://a11yproject.com/checklist.html). Si vous voulez approfondir le sujet, vous pourriez également aimer vérifier vos applications avec les [techniques ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques), des articles sur la [conception pour le clavier](http://www.washington.edu/accessibility/checklist/keyboard/), ou parcourir les [archives de Simply Accessible](http://simplyaccessible.com/archives/).

#### 5. Gardez la tête froide

![Image](https://cdn-media-1.freecodecamp.org/images/v5Gt3jiSASnmtq-MlDLbVdCP1XLATG3XOg1x)
_Source : giphy.com_

Vérifiez à nouveau la section head de votre HTML, et assurez-vous d'avoir des méta descriptions, une viewport configurée pour le mobile, une balise title, et une favicon. Gardez au moins les balises méta de base, telles que la description et l'auteur. Les règles de SEO changent rapidement, mais une description informative peut augmenter vos chances d'être cliqué sur une page de résultats de recherche encombrée.

Si vous êtes sérieux à propos de partager votre travail, facilitez la collaboration avec les autres. Gardez votre fichier README.md concis et explicatif. C'est ainsi que la plupart des gens verront votre projet sur GitHub, alors ne négligez pas ce fichier dans votre dépôt.

Si vous codez de petits projets sur CodePen, allez dans la section des paramètres et ajoutez une description de base de votre pen et des tags. Cela permettra à votre travail d'être plus facilement découvert et compris par les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/PjVA5vV2tsognA60zykdy442fBQnNd8QyA0i)
_Fournissez quelques petites infos sur vos pens._

Assurez-vous d'importer les assets et les bibliothèques de manière appropriée. Si vous souhaitez déplacer votre projet de CodePen vers un autre serveur, assurez-vous que les bibliothèques externes, les frameworks et les feuilles de style que vous avez utilisés dans votre pen sont inclus.

Si vous voulez simplement une copie pour votre GitHub et que c'est un petit projet, vous pouvez simplement exporter votre pen vers gist. Pour ce faire, utilisez le bouton d'exportation dans le coin inférieur droit de la vue Éditeur.

#### 6. Optimisation du code

Restez DRY (ne vous répétez pas). Une fois terminé, jetez un coup d'œil au code une fois de plus. Peut-être y a-t-il des extraits que vous répétez et qui pourraient être remplacés par une fonction intelligente. Analysez votre code une fois de plus et voyez ce qui pourrait être mieux écrit. Plus vous codez, plus vous devenez sage en DRY. Il est dit que c'est une bonne pratique d'apprentissage du code de revenir à son propre code après un certain temps et de le refactoriser. Essayez-le.

Avant de terminer le projet, **rangez vos jouets**.

![Image](https://cdn-media-1.freecodecamp.org/images/mM9kAlJLgYaNgFOAGkeR267qERrl7GJDL1ZZ)

Tous les logs de la console sont utiles pour le débogage pendant la création, mais indésirables pour le code de production.

Rendez les commentaires concis et clairs pour les autres qui lisent votre code, et de préférence en anglais, sauf si tout le monde dans votre équipe parle la même langue.

Assurez-vous qu'il n'y a pas d'erreurs de console et que tous vos assets se chargent correctement (pour cela, vérifiez l'onglet Réseau dans les outils de développement de votre navigateur).

Vous pouvez utiliser des validateurs de code pour [JavaScript](http://www.jslint.com/), [HTML](https://validator.w3.org/), et [CSS](http://csslint.net/). Comme avec PageSpeed, la clé est de comprendre ce qui vaut la peine d'être optimisé.

#### 7. Expérience utilisateur

Une vérification rapide de la santé UX de votre projet devrait inclure les bases comme :

* **Objectifs**. Les utilisateurs peuvent-ils résoudre leurs problèmes ? Leurs attentes sont-elles satisfaites ? Obtiennent-ils ce pour quoi ils sont venus sur votre application/site web ? Que dirait un utilisateur à propos de l'application en la voyant juste un instant ?
* **Impasses**. Avez-vous vérifié tous les chemins possibles que vos utilisateurs peuvent prendre ? Êtes-vous utile ? Fournissez-vous des retours juste au moment où un utilisateur en a besoin ?
* **Hiérarchie visuelle**. La hiérarchie est-elle maintenue ? Guidez-vous l'œil de l'utilisateur ? Votre appel à l'action est-il visible ? Avez-vous trop d'éléments à focaliser qui se battent pour être l'élément principal sur un écran donné ?
* **Largeur de ligne**. Votre texte est-il facile à scanner ? Vos lignes ne doivent pas dépasser 80 caractères. Et assurez-vous que vos lignes ne sont pas trop étroites avec trop de padding.
* **Lisibilité**. Votre texte est-il lisible ? Les images sont-elles de la bonne taille ? Y a-t-il un [contraste](http://leaverou.github.io/contrast-ratio/) approprié entre les éléments ?
* **Affordance**. Vos boutons ressemblent-ils à des boutons ? Vos liens se comportent-ils comme des liens ? Un utilisateur saura-t-il qu'un élément est cliquable ou tappable ? Votre curseur se transforme-t-il en un pointeur de doigt là où c'est approprié ?
* **Cohérence**. Êtes-vous cohérent dans votre application ? Ou utilisez-vous 5 couleurs différentes pour marquer la même chose ou l'avez-vous organisé ?
* [**Micro-interactions**](https://uxplanet.org/microinteractions-the-secret-to-great-app-design-4cfe70fbaccf#.ku163smuk). Aidez-vous vos utilisateurs à remarquer quand les éléments sont survolés en vue bureau ? Comment marquez-vous les interactions ? Répondez-vous à ce qu'un utilisateur fait dans votre application ?
* **Test en plein soleil**. Comment votre application se comporte-t-elle à l'extérieur en plein soleil ? Tout est-il lisible ?
* **Test avec un lecteur d'écran**. Avez-vous essayé d'utiliser votre application avec un lecteur d'écran ? Est-il possible de l'utiliser pleinement en étant dirigé uniquement avec Voice Over ou un autre outil de lecteur d'écran ?
* **Relisez votre copie**. Vous êtes-vous débarrassé des textes lorem ipsum ? Vos alertes, avertissements, etc., sont-ils écrits dans un langage humain, ou lisent-ils toujours comme si un développeur pressé les avait écrits ?

#### 8. Revue de code sur Gitter

Lorsque vous êtes prêt avec les points précédents, allez dans la [Code Review room](https://gitter.im/FreeCodeCamp/CodeReview). Les campeurs ont de la chance d'appartenir à une communauté où tout le monde comprend que vous êtes nouveau en codage. Ce n'est pas grave si vous faites des erreurs. Nous apprenons tous en pratiquant et améliorons progressivement notre code.

Les campeurs ont des antécédents de codage variés et sont tous à différents points du programme de Free Code Camp. Donc, trouver de l'aide est assez facile.

![Image](https://cdn-media-1.freecodecamp.org/images/9tIISkbM4C5XrVOusTWk9BhzRcoV0Aue5dx5)

**Ne demandez pas trop tôt**. Demandez des retours plus tard lorsque votre application a commencé à prendre son propre caractère et sa propre forme. Essayez de découvrir la réponse d'abord. Google et [Stack Overflow](http://stackoverflow.com/) sont vos premières étapes. Bien sûr, si vous êtes bloqué avec un problème, sautez dans la salle appropriée et demandez ! C'est la partie de la magie de Free Code Camp, n'est-ce pas ?

**Soyez précis sur ce que vous cherchez**. Poser des questions précises vous mène à de meilleures réponses. Poser une question générale comme « Voici mon code. Qu'en pensez-vous ? » vous obtiendrez une réponse générale. Cela peut apporter beaucoup de nouvelles idées à la lumière, et un regard frais qui peut être inspirant. Cependant, de nombreuses suggestions de conception sont assez subjectives (basées sur le goût personnel et la réaction instinctive après quelques secondes), alors ne sautez pas à la conclusion que vous devez refactoriser tout votre code simplement parce qu'une personne l'a dit. Demandez une justification si vous ne comprenez pas ce que l'autre personne voulait dire. Répétez votre question pour obtenir des retours des autres, et dormez sur les suggestions si vous n'êtes pas sûr que le changement soit bon pour votre projet.

J'adore recevoir des **retours constructifs**. C'est mieux d'obtenir une liste de suggestions qu'un tas de louanges. Les mots gentils sont parfois nécessaires, mais les commentaires informatifs pleins d'empathie sont meilleurs pour progresser. À mesure que vous progressez, votre motivation deviendra plus intrinsèque.

#### Projets plus grands, listes plus courtes

Plans de site, tests unitaires, tests fonctionnels, mise en cache, analytique, répertoires de fichiers appropriés, vérification que les assets ne sont pas manquants, CSS pour la version imprimable, optimisation SEO... cette liste pourrait continuer pendant un certain temps, c'est sûr.

Mais plus vous codez, plus la liste semble courte, car vous coderez simplement mieux et intérioriserez beaucoup de ces considérations.

_Je suis un développeur web en formation. Je suis une [Free Code Camper](http://www.freecodecamp.com/ewathedoer). Je publie sur [Medium](https://medium.com/@thedoer) et [tweete sur l'UX et les startups](http://twitter.com/thedoerdoes). J'adore les solutions utiles et la collaboration amicale._