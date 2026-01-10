---
title: Erreurs que vous avez probablement commises dans votre tâche de codage pour
  un entretien d'embauche
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T16:11:33.000Z'
originalURL: https://freecodecamp.org/news/mistakes-youve-probably-made-in-your-coding-task-for-a-job-interview-28e6db6a68ad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RGs1JM8T1Dmoqa23oe01Iw.png
tags:
- name: GitHub
  slug: github
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: Erreurs que vous avez probablement commises dans votre tâche de codage
  pour un entretien d'embauche
seo_desc: 'By Michael Lazarski

  You got this task from that company you want to work for! You are hyped and you
  immediately start to work on it. After a long night of coding, you are done and
  you think you implemented the best thing ever!

  So you send the task ba...'
---

Par Michael Lazarski

Vous avez reçu cette tâche de la part de cette entreprise pour laquelle vous souhaitez travailler ! Vous êtes enthousiaste et vous commencez immédiatement à travailler dessus. Après une longue nuit de codage, vous avez terminé et vous pensez avoir implémenté la meilleure chose jamais créée !

Alors vous envoyez la tâche à l'entreprise. Après un certain temps, vous recevez un email de cette entreprise. Vous êtes confiant d'avoir réussi et qu'ils vous envoient un projet de contrat !

Puis vous lisez l'email et vous ne pouvez pas croire ce que vous voyez. Ce n'est qu'un email de remerciement et ils ont décidé de choisir quelqu'un d'autre.

Qu'est-ce qui a mal tourné et comment auriez-vous pu vous améliorer ? Approfondissons le sujet !

#### Erreur 1 : vous n'avez pas lu la tâche avec suffisamment d'attention

Parfois, un seul mot peut changer complètement le sens de la tâche. Peut-être que vous n'avez pas remarqué le mot "responsive" la première fois, ou vous pensez simplement l'avoir compris mais vous ne saisissez pas vraiment de quoi il s'agit.

Alors lisez la tâche plusieurs fois pour bien la comprendre.

#### Erreur 2 : vous avez commencé à implémenter la tâche sans l'avoir complètement comprise

Donc vous avez corrigé l'erreur 1 mais vous avez encore des questions ? Demandez à la personne avec qui vous êtes en contact. Ce n'est pas mal de demander ! C'est même le contraire, car cela montre à l'entreprise que vous vous souciez d'un bon produit et que vous ne voulez pas perdre leur temps.

S'ils réagissent négativement, alors je resterais loin de cette entreprise car c'est le premier signe d'un environnement toxique où personne ne peut poser de questions.

#### Erreur 3 : vous n'utilisez pas Git (ou un autre système de contrôle de version)

S'il vous plaît ! S'il vous plaît ! N'envoyez pas un fichier ZIP de 60 Mo par email avec le dossier complet `node_modules`. OSX n'aime pas décompresser node_modules, donc la personne qui va examiner votre code n'aura même pas la chance de regarder votre code.

Utilisez Git à la place. Si vous ne connaissez pas Git, c'est la meilleure occasion de l'apprendre car beaucoup d'entreprises utilisent Git. Tôt ou tard, vous devrez l'apprendre.

#### Erreur 4 : vous n'avez pas écrit de bons messages de commit

Vous utilisez maintenant Git, c'est bien. Ne faites pas tout en un seul commit. Les entreprises regarderont votre `git log` pour lire les messages de commit. Vous devez vous rappeler que vous travaillerez en équipe, et dans une équipe, de bons messages de commit comptent. C'est important pour les autres membres de l'équipe, et pour vous dans 2 semaines lorsque vous devrez trouver un commit ou comprendre ce qui s'est passé dans cette partie de l'application. Alors commitez souvent et écrivez de bons messages courts.

#### Erreur 5 : vous avez oublié le fichier .gitignore

Cela nous ramène à l'erreur numéro 3. Si vous n'avez pas de fichier .gitignore, tout dans ce répertoire sera ajouté à Git. Donc encore une fois, vous enverrez le contenu complet de votre `node_modules`. Personne ne veut votre `node_modules`.

Voici une bonne collection de fichiers gitignore : [https://github.com/github/gitignore](https://github.com/github/gitignore)

#### Erreur 5 : vous envoyez un fichier Zip par email

Je veux dire, en tant que développeur, vous devez connaître GitHub, n'est-ce pas ? Alors utilisez-le ! Mettez votre code sur GitHub et envoyez le lien GitHub à votre contact. Votre contact vous en sera très reconnaissant.

* Aucun filtre anti-spam d'entreprise ne supprimera le fichier zip.
* Oui, même en 2019, les emails ont une limite de taille de fichier et vous pourriez atteindre cette limite.
* Il est plus facile de jeter un premier coup d'œil au code sans télécharger un fichier zip.
* Il est plus facile de le partager avec d'autres développeurs dans l'entreprise. Habituellement, plus d'un développeur regardera votre code.

#### Erreur 6 : vous n'avez pas de fichier README.md ou il n'est pas bon

GitHub affichera le fichier README.md et il sera visible sur la page principale de votre dépôt. Écrivez-y un contenu significatif. Par exemple, le nom de la tâche ou expliquez ce que fait cette tâche, peut-être ajoutez les dépendances... et cela m'amène à mon prochain point.

#### Erreur 7 : vous n'avez pas écrit d'instructions sur la façon de démarrer votre tâche

Oui, je peux aller dans le fichier package.json et regarder vos scripts et, s'ils sont significatifs, je peux comprendre lequel est le bon à faire ou peut-être pas. Alors s'il vous plaît, écrivez dans le README.md comment configurer et démarrer votre tâche pour que je puisse l'exécuter.

#### Erreur 8 : vous n'avez pas inclus un lien fonctionnel vers votre tâche

"Mais pourquoi devrais-je le faire alors que vous venez de me dire que je devrais écrire des instructions sur la façon de l'exécuter ?" est ce que vous vous demandez en ce moment. Pour rendre la révision de votre tâche aussi fluide que possible, afin que le réviseur ne soit pas agacé d'avoir dû passer une heure à comprendre comment voir si votre code fait réellement ce qui était mentionné dans la tâche.

Mettez une version fonctionnelle quelque part sur Internet où vous pouvez donner un lien au réviseur. Heroku, GitHub Pages, AWS ou Azure ne sont que quelques exemples qui offrent également des services gratuits pour cela.

#### Erreur 9 : ne pas supprimer les anciens/fichiers inutiles de la tâche

Ne soyez pas ce développeur qui a un dossier `_old` quelque part dans le dépôt git. En tant que réviseur de votre code, que dois-je faire avec ce dossier ? Dois-je le regarder ou peut-être pas ? Pourquoi est-il là ? Je ne sais même pas quoi dire. Alors s'il vous plaît, supprimez tous les fichiers inutiles et anciens de votre code.

#### Erreur 10 : vous n'avez pas écrit un bel email avec le lien vers votre dépôt GitHub

N'envoyez pas simplement un email vide avec un lien. Cela peut être considéré comme très impoli. Je veux dire, de l'autre côté, il y a aussi quelqu'un d'humain. Écrivez au moins : Bonjour X, comment allez-vous ? J'espère que tout va bien. Voici le lien vers ma tâche terminée [LE LIEN]. Passez une bonne journée. Cordialement, Michael.

### Erreur 11 : Ne dites pas que quelque chose est facile

"Javascript est facile et pas difficile". Je ne sais pas pourquoi les gens disent cela, mais c'est une chose courante. Vous pouvez remplacer Javascript par n'importe quoi. Tout est facile et difficile en même temps. Conduire une voiture est facile, mais conduire une voiture de Formule 1 est difficile.

Pourquoi est-ce important ? Cela montre à l'interviewer qu'il y a une sorte d'élitisme dans votre esprit. Que veux-je dire par là ? C'est la même chose lorsque les personnes nouvelles en programmation demandent : "Quel est le meilleur moyen de faire XYZ ?". Il n'y a ni meilleure façon ni une seule façon. Il n'y a pas une telle chose que le meilleur langage de programmation à utiliser ou à apprendre.

Donc si vous avez appris le C++, vous regardez maintenant de haut les développeurs JavaScript, cela montre que vous vous sentez comme si vous faisiez partie d'une escouade d'élite. Cela signifie simplement que vous avez appris un outil de votre ceinture à outils. Vous pouvez maintenant utiliser le marteau à griffes mais pas la masse. Oui, il sera plus facile d'apprendre maintenant la masse, mais les deux marteaux ont leurs propres avantages et inconvénients.

Alors s'il vous plaît, ne dites pas que les choses sont faciles. Très probablement, elles semblent faciles parce que vous ne les comprenez pas complètement.

#### Erreur 12 : vous n'écrivez pas de tests si les spécifications de l'emploi disent que vous devez savoir comment tester

C'est toujours un plus de montrer que vous pouvez écrire des tests. Ils n'ont pas besoin d'être parfaits. Vous n'avez pas besoin d'avoir 100% de couverture de code. Écrivez simplement quelques tests simples qui testent votre fonctionnalité principale et vous avez probablement un gros point positif.

#### Erreur 13 : ne pas diviser votre code en fichiers plus petits

Si vous envoyez un gros fichier avec 2000 lignes de code, il est difficile de le réviser. En tant que personne qui doit vérifier votre code, il est difficile de voir ce qui se passe dans ce fichier et comment le code s'écoule. Probablement, vous devez aussi faire défiler de haut en bas. Essayez plutôt de diviser votre code en fichiers plus petits. Cela sera également important plus tard pour le travail. Personne ne veut de code que vous seul comprenez mais aucun de vos membres d'équipe. S'il vous plaît, divisez-le. C'est tellement plus facile à réviser.

#### Erreur 14 : vous n'avez pas de commentaires de code ou vous écrivez simplement ce que fait la ligne suivante

Celle-ci, je la vois encore faire par des gens après quelques années de travail en tant que développeur. Des commentaires comme : `// Boucle à travers un tableau` et la ligne suivante est `Array.forEach()`. Oui, bonjour, Capitaine Évident. Ce serait mieux si vous décriviez ce que fait cette boucle de manière plus abstraite. `// préparation des données pour les envoyer via AJAX` ou quelque chose dans ce sens. Ainsi, les gens savent quelle est l'intention du code.

#### Erreur 15 : votre code est partout

```
const array = [ 1, 2];
```

```
array.forEach((a ) =>{ a = a+ 1;
```

```
console.log(a) ; });
```

Cela est vraiment difficile à lire et montre également que vous travaillez de manière très négligente. Aujourd'hui, nous avons des outils comme `eslint` et `prettier`. Chaque éditeur et IDE plus grand a cela intégré ou vous devez simplement installer un plugin/extension. Alors s'il vous plaît, utilisez-le.

#### Erreur 16 : vous ne nommez pas correctement vos variables

```
const b = true;const a = [];
```

Ce n'est pas facile à lire et pas utile pour comprendre ce qu'est `b`. Un bien meilleur nom pourrait être :

```
const isReady = true;const listOfPersons = [];
```

Encore une fois, ce ne sont que des exemples et chaque équipe aura sa propre façon de nommer les choses. Bien sûr, vous ne pouvez pas deviner ce style, mais faites simplement ce que vous sentez être un nom significatif et tenez-vous à un style.

#### Erreur 17 : vous commentez simplement l'ancien code

J'ai souvent vu cela et je ne comprends toujours pas pourquoi les gens font cela. Vous avez un fichier avec 100 lignes de code et 70 lignes sont simplement de l'ancien code qui est commenté et 30 lignes d'une implémentation réelle.

Dois-je lire l'ancien code ? Cela doit-il me montrer que vous l'avez fait mal la première fois et que vous l'avez réimplémenté ? Personne n'est parfait et n'écrit pas le code parfait la première fois. Alors s'il vous plaît, supprimez ce code. Si je veux voir si vous avez refactorisé le code, je devrais le voir dans les commits git avec des messages de commit git où je peux comprendre ce que vous avez fait.

#### Erreur 18 : vous n'avez pas vérifié si votre code fonctionne toujours

Cela arrive tout le temps. Vous recevez un email d'un candidat dimanche soir. Vous allez au travail lundi et commencez à vérifier le code et soudain vous recevez un deuxième email avec quelques mises à jour dans le code. Vous recevez également une promesse que cette fois-ci, cela fonctionne vraiment.

Alors s'il vous plaît, avant d'envoyer votre code. Arrêtez le programme, nettoyez le cache, installez les dépendances et redémarrez-le. Si cela fonctionne toujours, alors vous pouvez dire que vous êtes prêt.

#### Erreur 19 : vous avez changé quelque chose et n'avez pas vérifié si cela fonctionne toujours

Pour nos développeurs full-stack, nous avons une tâche où ils doivent sauvegarder des variables dans une base de données. Ils peuvent choisir la base de données, le schéma et comment sauvegarder les variables. Nous disons simplement que cela doit être sauvegardé. C'est là que les gens changent le code et ne vérifient pas si, après les changements, cela sauvegarde toujours dans la base de données. Par exemple, ils changent le schéma ou ils l'essayent simplement avec un petit fichier, etc.

Encore une fois, avant d'envoyer votre tâche, vérifiez si toutes les fonctions fonctionnent toujours comme elles le devraient et essayez de casser des choses. Personne ne dit que vous devez attraper chaque cas limite, mais au moins les choses les plus courantes qu'un utilisateur peut faire.

#### Erreur 20 : vous ne vous êtes pas préparé pour l'entretien de codage

Un certain temps s'est écoulé entre l'envoi de la tâche et l'entretien réel, peut-être une semaine ou plus. Vous vous souvenez vraiment encore de ce que vous avez fait dans cette tâche ? Comme pourquoi avez-vous résolu cette tâche de cette manière et quel était votre raisonnement lorsque vous avez implémenté votre tâche ?

L'un des objectifs de ce processus entier n'est pas de voir à quel point vous êtes bon en tant que programmeur, mais si vous correspondez à l'équipe et si vous êtes un joueur d'équipe. C'est plus une question de vos compétences sociales que de vos compétences en codage. S'il vous plaît, lisez votre propre code avant de passer à la partie entretien.

Ce ne sont que quelques exemples que j'ai vus. En avez-vous d'autres ? Commentez ci-dessous !

Peut-être voulez-vous que je révise votre code ? Ou vous donner quelques conseils pour vous aider ? Contactez-moi simplement sur l'un de mes comptes de réseaux sociaux et je peux essayer de vous aider. Bien sûr, je ne peux pas faire la tâche pour vous, mais je peux aider avec tout le reste !

**Merci d'avoir lu !**

**Dites Bonjour !** [Instagram](https://www.instagram.com/lampewebdev/) | [Twitter](https://twitter.com/lampewebdev) | [LinkedIn](http://(https://www.linkedin.com/in/michael-lazarski-25725a87) | [dev.to](https://dev.to/lampewebdev)