---
title: Comment les bonnes pratiques Git m'ont fait économiser des heures de retravail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:37:15.000Z'
originalURL: https://freecodecamp.org/news/how-git-best-practices-saved-me-hours-of-rework-cf227bad9a50
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fbmqZte8Tx-KfrZlkw4q4g.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment les bonnes pratiques Git m'ont fait économiser des heures de retravail
seo_desc: 'By Hemal Patel

  Recently I was working on the task to upgrade a certificate for a NodeJS application.
  This was last touched two years ago for a feature enhancement. Any live issue raised
  to this app would require immediate attention, although the app ...'
---

Par Hemal Patel

Récemment, je travaillais sur la tâche de mise à jour d'un certificat pour une application NodeJS. Cela avait été touché pour la dernière fois il y a deux ans pour une amélioration de fonctionnalité. Tout problème **en direct** soulevé pour cette application nécessiterait une attention immédiate, bien que l'application n'ait été utilisée qu'en interne.

L'application est ancienne. Les modules Core-NodeJS-Infra n'ont pas été mis à jour depuis plus de deux ans. Les services en aval sont obsolètes. La manière dont nous appelons les services en aval a changé. L'échéance serrée est la cerise sur le gâteau. Je savais que cela allait être une montée en roller-coaster.

J'ai passé trois jours à faire fonctionner l'application.

Les modules Infra sont mis à jour ? Vérifié.

Les services en aval fonctionnent correctement ? Vérifié.

Les flux UI fonctionnent correctement ? Vérifié.

L'un de nos membres d'équipe avait touché l'application pour une mise à jour il y a plus d'un an. Il a souligné que le repo à partir duquel j'ai forké était lui-même un repo forké. Une autre équipe avait travaillé sur ce repo, et ensuite notre équipe avait travaillé sur le repo original à partir de ce point  mais mon membre d'équipe ne sait pas à partir de quel point. Donc c'était un peu le bazar !

Nous avons un outil "Ownership" qui montre le repo correct et il m'a "menti". Donc la situation était comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vWPKaIKu8tCtgYQyo-Ejsw.jpeg)
_Forkception_

Oui, c'était Forkception ! WTF et FML étaient les deux premières pensées qui me sont venues à l'esprit. J'**aurais dû** travailler sur le repo en direct mais, **au lieu de cela**, j'ai travaillé sur un fork qui était obsolète. Comme je suis stupide !

Première pensée  mes trois jours de travail ont été gaspillés, et je dois recommencer à zéro.

Deuxième pensée ? Laissez-moi demander à mon vieux ami Git?. Il m'aide depuis très longtemps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fbmqZte8Tx-KfrZlkw4q4g.png)

**Moi**  "Hey Git? Je suis dans de gros ennuis et j'ai besoin de ton aide pour résoudre ce problème."

**Git**  "Hey ! Ok, alors nous devons commencer par ce qui est en direct d'abord. Crée une nouvelle branche appelée **upgrade**, et pointe cette branche vers le code en direct. Tu peux utiliser un [git hard reset](https://git-scm.com/docs/git-reset#git-reset---hard) pour cela."

**Moi**  "Ok, je vais le faire."

À ce stade, la situation ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GRnnYUHYrJU3CF5V-miFUg.jpeg)
_Utilisation des fonctionnalités Git_

**Git**  "Nous devons savoir ce qui a changé entre develop et upgrade. Peux-tu lister les fichiers qui diffèrent entre ta branche **upgrade** et **develop** ? Vérifie ces fichiers individuellement, et détermine quel type de changements il y avait."

**Moi**  "Cool. Je vois trois types de changements. Il y a un service S1 que je dois appeler différemment. Il y a un service S2 que je dois appeler en utilisant un endpoint différent. Il y a un service S3 que je dois appeler en utilisant des paramètres différents. Je vois aussi que le fichier **package.json** dans la branche **upgrade** a déjà certaines des packages mis à jour. Donc seulement quelques packages doivent être changés."

**Git**  "Super que tu aies séparé les changements. Maintenant montre-moi le log Git de ta branche **develop**. J'espère que tu as suivi certaines pratiques de base de Git, par exemple toujours avoir un code compilable dans chaque commit. Le message de commit devrait décrire ce que tu as changé."

![Image](https://cdn-media-1.freecodecamp.org/images/1*hH5gt56WcMwTKl_iF50Uuw.png)
_Log Git sur la branche develop_

**Moi**  "Oui, j'ai un total de quatre commits dans la branche **develop**. Un commit était pour rendre le projet compilable. Il y en a un pour chacun des trois appels de service."

**Git**  "Parfait ! Il semble que tu aies suivi les meilleures pratiques correctement. Commençons par stabiliser la compilation du projet en mettant à jour le package.json. Passe à la branche **upgrade** et fais une copie du package.json  package-copy.json. Maintenant, en utilisant Git [replace](https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/), mets à jour le package.json de la branche upgrade avec celui de la branche develop, et exécute la diff entre package.json et package-copy.json. Puisque le code en direct a déjà certains des packages changés, et a des versions différentes, tu devras mettre à jour en regardant la diff."

![Image](https://cdn-media-1.freecodecamp.org/images/1*rFVh4Jf6JCpLgBDj9Qj_6g.jpeg)
_**Rendre le projet compilable**_

**Moi**  "Laisse-moi essayer cela. Ok, il compile et fonctionne."

**Git**  "Super ! Maintenant, travaillons sur les appels de service. Je vois que tu as un commit pour chaque changement d'appel de service dans la branche develop. Il est temps de [cherry pick](https://git-scm.com/docs/git-cherry-pick). Choisis de l'appel de service le moins compliqué au plus compliqué. Choisis, fusionne, et résous les conflits. Assure-toi de vérifier si le projet est dans un état compilable **après** chaque cherry-pick et **avant** chaque commit."

**Moi**  "S1 fait. S2 fait. S3 fait. Merci, Git"

**Git**  "Je t'en prie. Mais c'est toi qui t'es aidé, en suivant les pratiques de commit Git, et en ne traitant pas Git comme un simple stockage de code."

### **Qu'ai-je fait ici ? ?**

#### Commiter les changements liés

Prends une pause un instant et réfléchis si ce changement devrait aller dans ce commit. Un commit qui dit "change: service-s1 endpoints" et qui contient des changements de service-s2 ne ferait que créer de la confusion.

#### Ne commite pas un travail à moitié fait

Nous avons souvent entendu le mantra "commit early, commit often". Dans l'exemple ci-dessus, tu peux avoir un commit pour différents endpoints du même service. Cela s'appelle [**Sausage Making**](https://sethrobertson.github.io/GitBestPractices/#sausage).

Cependant, je squash personnellement mes petits commits en utilisant le **mode interactif de git rebase**. Cela m'aide à avoir un changement logique, qui peut être certifié, et cela aide un Committer de Confiance à réviser ton code également. Cela est beaucoup plus préférable pour les projets à grande échelle.

#### Teste ton code avant de commiter

Nous devrions penser à Git comme une machine à états, et toute machine devrait être dans un état compilable à tout moment.

#### Écrire de bons messages de commit

C'est une partie cruciale. Je prends toujours une pause un instant et réfléchis si je serai capable de comprendre  après trois mois  le type de changement dans ce commit en regardant simplement le message de commit.

### Conclusion

J'ai pu résoudre rapidement le bazar. J'ai pu sortir de ce moment WTF et FML simplement parce que j'ai suivi quelques bonnes pratiques. Elles existent pour une raison et sont comme le sel dans la nourriture  tu ne réalises leur valeur que lorsqu'elles ne sont pas utilisées.

Les erreurs arriveront tôt ou tard, inconsciemment. Mais assure-toi de suivre consciemment certaines pratiques autour de Git.

Je suis un fan des [messages de commit sémantiques Git](https://gist.github.com/mutewinter/9648651#file-commit_format_examples-txt), qui aident à naviguer à travers l'historique Git. Parce que, soyons honnêtes, tu ne peux pas t'attendre à ce que tout le monde utilise les mêmes mots pour chaque message de commit. Cependant, le **type de message** peut être attendu.

Cela aide à s'assurer que, après chaque commit, ton projet peut être compilé  ce qui est vraiment utile.

VSCode a un support génial pour Git. Cela devient super facile de voir les conflits et de les résoudre, parfois avec un seul clic. Voir l'exemple ci-dessous ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BtLN8xTuTbJgXkJMPD7GgA.jpeg)

### Références

* [Bonnes Pratiques Git](https://sethrobertson.github.io/GitBestPractices/)
* [Intégration Super Géniale du Contrôle de Version dans VSCode](https://code.visualstudio.com/Docs/editor/versioncontrol)
* [Messages de Commit Sémantiques Git](https://seesparkbox.com/foundry/semantic_commit_messages)
* Astuce Git ?: C[omment "fusionner" des fichiers spécifiques d'une autre branche](https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/)
* Astuce Git ?: G[it  documentation git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
* Astuce Git ?: G[it  documentation git-reset](https://git-scm.com/docs/git-reset#git-reset---hard)

Un merci spécial à mes amis [**Saurabh Rajani**](https://www.linkedin.com/in/saurabh-rajani-72268590/?originalSubdomain=in) et [**Anish Dhargalkar**](https://www.linkedin.com/in/anishdhargalkar/) qui m'ont aidé avec l'affinage du contenu.