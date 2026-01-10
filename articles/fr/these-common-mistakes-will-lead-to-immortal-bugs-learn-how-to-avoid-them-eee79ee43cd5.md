---
title: Ces erreurs courantes mènent à des bugs immortels. Apprenez à les éviter.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T23:25:53.000Z'
originalURL: https://freecodecamp.org/news/these-common-mistakes-will-lead-to-immortal-bugs-learn-how-to-avoid-them-eee79ee43cd5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_tDOnN79K8WqoVD0
tags:
- name: bugs
  slug: bugs
- name: Life Lesson
  slug: life-lesson
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
- name: WeChat
  slug: wechat
seo_title: Ces erreurs courantes mènent à des bugs immortels. Apprenez à les éviter.
seo_desc: 'By David Yu

  Didn’t we already fix that?

  The question that you or your teammate would ask after the product manager posts
  a snapshot of the bug.

  This whole event feels like a Deja Vu. You try to retrace the time you fixed that
  bug in the commits, but ...'
---

Par David Yu

**_Ne l'avons-nous pas déjà corrigé ?_**

La question que vous ou votre coéquipier poseriez après que le chef de produit ait publié une capture d'écran du bug.

Tout cet événement semble être un déjà-vu. Vous essayez de retracer le moment où vous avez corrigé ce bug dans les commits, mais quel est l'intérêt ?

La réalité est que si vous ne trouvez pas la cause racine du bug, il reviendra comme l'Hydre de Lerne.

![Image](https://cdn-media-1.freecodecamp.org/images/m8XUwZGMf2YTjk5zY2UhvOKC8qrJ2D5JEkIA)
_Source : [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hercules_and_the_Hydra_of_Lerna-_Hercules_grasps_his_club_with_both_hands_and_confronts_the_seven-headed_hydra,_from_the_series_%27The_Labors_of_Hercules%27_MET_DP832529.jpg" rel="noopener" target="_blank" title=")_

Voici quelques schémas qui mènent à des bugs immortels.

### Coder en dur une valeur

Lorsque nous faisons du développement front-end, nous utilisons souvent des données factices pour construire rapidement l'interface utilisateur. C'est bien.

Le problème est d'avoir des données factices à plusieurs endroits. Il est alors facile d'en oublier une ou deux lorsque vous poussez votre code.

Voici quelques conseils :

* Utilisez une seule variable pour vos données factices et partagez-la entre différents composants
* Écrivez un commentaire comme `// TODO: à supprimer plus tard` pour permettre une recherche facile plus tard
* Ne comptez pas sur le fait que les données backend soient toujours les mêmes

```
// ? 
```

```
<img src={require(`./assets/${backendData.fileName}.png`)} />
```

```
// Cela plantera si fileName est une chaîne inattendue
```

```
// ? 
```

```
let img;
```

```
try {
```

```
  img = require(`./assets/${backendData.fileName}.png`)
```

```
} catch(e) {  // Attraper l'erreur si le fichier n'existe pas
```

```
}<img src={img} />
```

```
// ? 
```

```
<img src={backendData.imgUrl} />
```

### Refactorisons plus tard

Votre base de code ne fera que grandir à mesure que vous y travaillerez. Votre client ou votre patron ne connaîtra pas l'effet négatif de ne pas refactoriser le code, car tout semble bien en surface.

De plus, il est toujours plus satisfaisant d'écrire quelque chose de nouveau et de le montrer aux autres. « Hé, regardez ce qu'il peut faire maintenant. »

Alors, comment savoir quand refactoriser le code ?

Selon [Refactor Guru](http://2018-10-28\t14:00\t21:00\t2018-10\t\u00a5300.00\t7:00:00\t-\u00a52,100.00\tDavid\tFront-End\tBug fixes: speaker/headphone control. Countdown timer based on start_time plus duration. Update call status from in_progress to ended), suivez la Règle des Trois

1. Lorsque vous faites quelque chose pour la première fois, faites-le simplement.
2. Lorsque vous faites quelque chose de similaire pour la deuxième fois, grimacez à l'idée de répéter mais faites la même chose quand même.
3. Lorsque vous faites quelque chose pour la troisième fois, commencez à refactoriser.

### Tout garder dans un seul fichier

Cela va de pair avec la refactorisation du code. Lorsque le projet est frais, il est difficile de prédire à quel point une fonctionnalité deviendra grande.

Dans le passé, j'avais un fichier qui est devenu des milliers de lignes de code. Refactoriser ce code est comme effectuer une chirurgie, délicat, mais gratifiant à la fin.

La plupart des gens ont un principe de la façon dont leur projet est structuré. Séparation des fichiers par pages, fonctionnalités, dev. ou production, méthode privée ou publique, modèle MVC, etc.

Comment structurer un dossier de projet est une grande discussion en soi. Je garderai cela pour un autre article.

### Ne pas écrire de spécifications pour l'API

« Attendez, pourquoi les images ne s'affichent-elles plus ? » demande le chef de produit aux développeurs front-end.

« Attendez, pourquoi les données n'ont-elles plus picture_url ? » Le développeur front-end vérifie la console pour la réponse du réseau.

« Oh oui, maintenant les images viennent en trois tailles. large_pic_url, med_pic_url, small_pic_url. » Le développeur back-end a entendu la discussion et est intervenu.

Ça vous dit quelque chose ?

Tout le monde essaie de faire son travail. Mais la synergie ne se produira pas dans le silo. C'est le travail de tout le monde de communiquer ce qui est nécessaire.

Voici quelques solutions simples pour commencer.

* Avant de construire une API, commencez par un fichier JSON des données auquel les développeurs front-end et back-end ont accès.
* Lorsque l'API est terminée, générez le document avec [https://github.com/apidoc/apidoc](https://github.com/apidoc/apidoc)
* Notifiez les changements importants avant le déploiement

Il existe des approches plus sophistiquées pour écrire des spécifications et gérer la documentation. Et j'aimerais entendre parler de l'approche que votre équipe utilise dans la section des commentaires.

### Fusionner du code sans lire les conflits

Casser des choses est moins préoccupant puisque vous pouvez toujours revenir au commit précédent.

C'est votre code ou celui de votre coéquipier qui disparaît pendant le processus qui pose problème.

Cela arrive souvent lorsque vous voulez « gagner du temps » et avancer.

En cas de doute, contactez le développeur qui a fait le commit qui entre en conflit avec le vôtre.

Lorsque vous faites une erreur, `git merge --abort` ou `git-reset --hard`.

Lorsque c'est cassé au-delà de toute réparation, supprimez le projet et clonez-le à nouveau.

Réfléchissez à deux fois avant de faire `git push -f`.

### Corriger un composant réutilisable sans le tester

Les composants réutilisables sont le tour de magie de chaque développeur. Comme lorsque le client vous présente le wireframe qui contient le même sélecteur de date sur plusieurs pages.

Dans votre esprit, vous pensez, « Je vais faire un composant de sélecteur de date génial. Écrire moins de code. Faire plus. »

Quelques mois plus tard, le client dit, « Je veux que le sélecteur de date sur cette page explose avec des feux d'artifice et sur les autres pages, différents chatons pour représenter les mois ». Maintenant, vous avez besoin que le sélecteur de date soit plus dynamique qu'il ne l'était.

Puis, après avoir fait les changements, vous découvrez que des feux d'artifice sortent des chatons.

Si vous êtes dans une grande équipe, vous pouvez différer l'assurance qualité à une autre équipe.

Mais s'il n'y a pas une telle fonctionnalité dans votre organisation, vous devrez faire une recherche globale du nom de votre composant pour voir ce que votre composant affecte.

Faites une note à vous-même de ces fichiers. Testez ces fichiers visuellement et fonctionnellement en fonction de ce qu'ils font.

### Chaque fois que vous dites, « C'est bien pour l'instant »

Vous savez que vous devrez y revenir plus tard. La clé est « ne pas oublier ».

Lorsque vous devez choisir entre la vitesse de développement et la stabilité du logiciel, nous devons faire attention à ne pas toujours mettre la vitesse comme priorité absolue. C'est similaire à conduire une voiture sans jamais vérifier l'état de la voiture.

Vous pouvez décider d'un ratio entre vitesse et assurance qualité. Peut-être que c'est deux itérations rapides et une itération d'assurance qualité, ce qui a du sens pour votre équipe.

### Conclusion

* Évitez de coder en dur une valeur si possible. Si vous devez le faire, laissez une note pour vous-même.
* Refactorisez lorsque vous faites la même chose pour la troisième fois.
* Divisez le code et refactorisez souvent
* Les ingénieurs front-end et back-end doivent travailler ensemble pour se mettre d'accord sur les données échangées.
* Si les conflits de fusion ne vous semblent pas clairs, vérifiez auprès de la personne qui a écrit le commit.
* Lorsque vous apportez des modifications à un composant réutilisable, testez les emplacements où il est utilisé.
* Trouvez un équilibre sain entre vitesse et qualité pour votre équipe.

### Pendant que nous y sommes...

Si vous voulez atteindre les 1 milliard d'utilisateurs de WeChat, vous devez d'abord le comprendre. Voici un [**glossaire gratuit**](https://pages.convertkit.com/b2469604dd/0c671fdd2d) pour commencer.