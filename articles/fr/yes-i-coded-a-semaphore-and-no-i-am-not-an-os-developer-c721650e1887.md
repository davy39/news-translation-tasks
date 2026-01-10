---
title: Oui, j'ai codé un Sémaphore et non, je ne suis pas un développeur de systèmes
  d'exploitation.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T21:06:56.000Z'
originalURL: https://freecodecamp.org/news/yes-i-coded-a-semaphore-and-no-i-am-not-an-os-developer-c721650e1887
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qKfV6Xbz-CAx11Hgd__z5Q.jpeg
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Oui, j'ai codé un Sémaphore et non, je ne suis pas un développeur de systèmes
  d'exploitation.
seo_desc: 'By Sajal Sarwar Sharma

  When you might be using semaphores in your daily coding life


  Semaphores!


  You are sitting in an 8th standard Mathematics classroom reading about Pythagorean
  Triplets, you are mugging up the Pythagoras Theorem. The famous equat...'
---

Par Sajal Sarwar Sharma

#### Quand vous pourriez utiliser des sémaphores dans votre vie de codage quotidienne

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKfV6Xbz-CAx11Hgd__z5Q.jpeg)
_Sémaphores !_

> Vous êtes assis dans une salle de classe de mathématiques de 8ème année, en train de lire sur les triplets pythagoriciens, vous apprenez par cœur le théorème de Pythagore. La célèbre équation _(a * a) + (b * b) = (c * c)_ est gravée dans votre esprit.

> Avance rapide de 10 ans — vous vous souvenez encore de ce jour et vous vous demandez pourquoi, au nom de Dieu, on vous a enseigné cette équation, vous n'avez jamais vraiment rencontré quoi que ce soit de pratique dans la vie qui utilise cette équation et cela vous fait remettre en question notre système éducatif actuel.

C'est un scénario qui nous fait nous demander si ces années d'éducation de notre vie valaient vraiment l'effort. Beaucoup d'entre nous seront d'accord pour dire qu'une grande partie de notre éducation ne nous aide pas réellement dans notre vie pratique.

Je suis un développeur de logiciels travaillant sur un produit SaaS, et j'ai des révélations qui me font contempler les différences frappantes entre mes connaissances théoriques et ma vie pratique. Mais de temps en temps, des choses apparaissent dans les scénarios et les lieux les plus inhabituels. Elles me font me demander si nous ignorons et n'apprécions pas vraiment ce qui se passe sous le capot et qui alimente notre vie quotidienne.

### L'énoncé du problème

L'histoire commence un beau jour où j'étais assis tranquillement dans mon coin chaud et confortable du bureau en train de faire mon développement d'API habituel. Un ticket utilisateur est apparu disant qu'ils avaient reçu plusieurs communications de notre service et qu'ils en étaient ennuyés. J'ai vérifié le code, mais cela n'aurait pas dû arriver. Le cron qui s'exécute et envoie des communications à l'utilisateur final n'aurait dû l'envoyer qu'une seule fois (et **ce cron s'exécute toutes les heures**).

En même temps, j'ai reçu un pagerduty indiquant qu'il y avait une augmentation de l'utilisation du CPU sur mon serveur cron. Cela arrive généralement de temps en temps lorsqu'il y a beaucoup de tâches à traiter par plusieurs crons. J'ai vérifié le système, et à ma grande surprise, j'ai trouvé le problème qui causait tout ce chaos et ces tickets utilisateurs.

À mon horreur, j'ai vu plusieurs instances du même cron de communication s'exécuter en même temps, prenant les mêmes tâches et envoyant des communications. Cela expliquait tout. (Cela n'aurait pas dû arriver — la première instance du cron aurait dû terminer son exécution avant que la deuxième instance ne commence à s'exécuter. C'est ainsi que les tâches cron devraient fonctionner).

Ce jour-là, il y avait une augmentation du nombre de tâches que le cron devait gérer, ce qui faisait que le cron continuait à s'exécuter bien au-delà de son temps d'exécution habituel. Cela a conduit à un chevauchement (en d'autres termes, il continuait à s'exécuter même après une heure, et ensuite la deuxième instance est apparue).

Mon travail était tout tracé : je devais rendre l'exécution plus rapide et **ne jamais permettre à plusieurs instances du même cron de s'exécuter simultanément**.

### La solution

La première chose qui m'est venue à l'esprit a été d'implémenter des **Sémaphores** (enfin, ces cours de systèmes d'exploitation sont revenus en mémoire). Mon professeur avait raison de dire qu'un beau jour, j'utiliserais cette technique pour sauver ma propre vie.

> « Aujourd'hui est ce jour », ai-je pensé.

J'ai donc fait des recherches sur Google et je suis tombé sur de nombreuses ressources utiles pour accomplir ma tâche. Je vais écrire ici ce que j'ai appris et comment j'ai finalement réalisé que j'avais en fait implémenté le concept de Sémaphore tout du long.

### Étape 1

Dans votre répertoire de fichiers système, créez un fichier nommé **myCronPID.txt** qui stockera l'identifiant de processus (PID) du cron en cours d'exécution à cette instance particulière. Selon Wikipedia :

> En informatique, l'**identifiant de processus** (généralement appelé **processus ID** ou **PID**) est un nombre utilisé par la plupart des noyaux de systèmes d'exploitation — tels que ceux d'UNIX, de macOS et de Microsoft Windows — pour identifier de manière unique un **processus** actif.

### Étape 2

Trouvez l'identifiant de processus (PID) du cron en cours d'exécution. Cela peut être fait en utilisant le code ci-dessous (je vais utiliser PHP comme référence).

### Étape 3

Pour la première fois, le fichier **myCronPID.txt** sera vide. Stockez le PID actuel obtenu à l'étape 2 dans ce fichier. La fois suivante, lors de l'obtention du PID du cron en cours d'exécution (disons 5678), obtenez le PID du fichier **myCronPID.txt**. Le PID obtenu du fichier (disons 1234) sera l'identifiant de processus de l'instance de cron qui s'exécutait précédemment. Vérifiez si le PID 1234 est toujours en état d'exécution. Cela peut être trouvé facilement.

Dans les systèmes Linux, il y a un dossier **_/proc_** qui contient des dossiers pour les processus en cours d'exécution dans le système. Les noms des dossiers dans ce dossier **/proc** sont les identifiants de processus. Donc, disons que si le dossier **/proc** contient un dossier **1234**, cela implique qu'un processus avec le PID 1234 est en état d'exécution. S'il n'a pas un tel dossier, cela implique qu'il n'y a pas de processus avec le PID 1234 en cours d'exécution à cet instant particulier.

### Étape 4

Dans cette étape, obtenez le PID du fichier myCronPID.txt et vérifiez si le processus est toujours en cours d'exécution en utilisant le code donné à l'étape 3.

1. Si _isProcessRunning_ retourne vrai, cela implique que l'instance de cron en cours d'exécution précédente n'a pas terminé son exécution. Par conséquent, la nouvelle instance qui a appelé la fonction _isProcessRunning_ ne doit pas reprendre son exécution.
2. Si _isProcessRunning_ retourne faux, cela implique que l'instance de cron précédente a terminé son exécution. La nouvelle instance qui a appelé la fonction _isProcessRunning_ doit reprendre son exécution et mettre son propre identifiant de processus dans myCronPID.txt

### **Étape 5**

Mettre tout cela ensemble :

Dans votre instance de cron en cours d'exécution, invoquez simplement l'objet de la classe ci-dessus avec son constructeur approprié.

**$fileName** — Ce sera le nom du fichier qui stockera le PID du fichier cron.

**$rootDir** — Ce sera le répertoire racine de votre projet actuel.

Après l'invocation, utilisez les méthodes de l'Util dans votre code Cron comme suit :

Cela garantira qu'il n'y aura pas plusieurs instances de cron du même travail en cours d'exécution simultanément.

### Conclusion

Après avoir recherché tout cela et écrit le code ci-dessus, j'ai découvert que je n'avais implémenté rien d'autre que des Sémaphores tout du long. Mon professeur de systèmes d'exploitation aurait été fier aujourd'hui.

Cela m'a fait réfléchir à nouveau : nous apprenons simplement les concepts par cœur. Nous ne regardons pas les intricacies de nos apprentissages, mais plutôt nous travaillons sur des couches si abstraites que nous ne prenons pas le temps d'apprécier la beauté du travail qui se passe réellement sous le capot.

Notre système éducatif n'est pas toujours paralysé. La manière dont nous apprenons les choses fait toute la différence. Essayez de vous changer plutôt que de vous plaindre. Le monde est plein de merveilles et il est beau.

PS : J'espère que vous aimez mon article, corrigez-moi si je me trompe quelque part.