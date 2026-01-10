---
title: Conseils pour la ligne de commande Bash pour vous aider à travailler plus vite
subtitle: ''
author: Vinod Mathew Sebastian
co_authors: []
series: null
date: '2022-05-02T19:56:22.000Z'
originalURL: https://freecodecamp.org/news/bash-command-line-tips-to-help-you-work-faster
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Bash-1.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Productivity
  slug: productivity
seo_title: Conseils pour la ligne de commande Bash pour vous aider à travailler plus
  vite
seo_desc: 'Learning the command line is essential for any aspiring developer.

  And to execute commands on the command line, you need a shell.

  The Bash shell is popular in Unix-like operating systems like Mac and Linux. In
  fact in most Linux distros, Bash is the ...'
---

Apprendre la ligne de commande est essentiel pour tout développeur en herbe.

Et pour exécuter des commandes sur la ligne de commande, vous avez besoin d'un shell.

Le shell Bash est populaire dans les systèmes d'exploitation de type Unix comme Mac et Linux. En fait, dans la plupart des distributions Linux, Bash est le shell par défaut.

Vous pouvez également utiliser Bash dans Windows via WSL (Windows Subsystem for Linux).

Après avoir appris quelques commandes Bash de base, il est temps de passer à la vitesse supérieure.

Ce tutoriel n'est pas destiné aux débutants absolus, mais j'espère que les novices et les utilisateurs avancés pourront en tirer quelque chose.

Voici les 10 commandes Bash qui vous aideront à travailler plus vite avec votre terminal.

## 1. Utilisez Control + L pour effacer l'écran et Control + D pour quitter

Pour effacer l'écran du terminal, tapez `clear` sur la ligne de commande.

Pour quitter, tapez `exit`.

Mieux encore, appuyer sur Ctrl + l (⌘ + l) efface l'écran et Ctrl + d (⌘ + d) ferme le terminal.

## 2. Utilisez la commande `nohup` pour lancer des processus qui ne se terminent pas avec la session du terminal

Une fois les programmes chargés en mémoire, ils sont appelés processus.

Parfois, j'ouvre Firefox depuis la ligne de commande : `firefox https://freecodecamp.org`.

Mais dès que je ferme le terminal, Firefox plante aussi.

Pour éviter cela, utilisez la commande `nohup` (no hang up) : `nohup firefox https://freecodecamp.org`.

Maintenant, lorsque je ferme le terminal, Firefox ne plante pas mais mon onglet plante.

La solution : faites de Firefox un processus en arrière-plan en ajoutant le symbole `&`.

`nohup firefox https://freecodecamp.org &`

Maintenant, même si je quitte le terminal, tous mes onglets restent intacts.

## 3. Utilisez `pkill` pour tuer des processus en tapant seulement une partie du nom

En utilisant la commande `killall`, nous pouvons tuer un processus par son nom :

`killall firefox`

Mieux encore, utilisez `pkill` pour terminer en tapant seulement une partie du nom.

`pkill fire*`

## 4. Précédez la commande `time` pour savoir à quelle vitesse quelque chose s'exécute

Voulez-vous savoir combien de temps il faut pour exécuter quelque chose dans le shell ?

Il suffit de précéder `time` à la commande : `time gcc -g *.c`.

## 5. Sur Linux, utilisez `cat /etc/*rel*` pour voir le nom de la distribution

Taper `uname -a` montre les informations du système.

Voulez-vous double vérifier quelle distribution vous utilisez ?

Il suffit de taper `cat /etc/*rel*` sur le shell et d'appuyer sur entrer.

## 6. Utilisez la commande `sed` dans les fichiers texte pour trouver et remplacer

Voulez-vous remplacer plusieurs occurrences d'un mot dans un fichier texte ?

Utilisez la commande `sed`.

`sed s'/apples/oranges/g' myfile.txt`

Ici, toutes les occurrences du mot 'apples' sont changées en 'oranges'.

Si vous devez seulement remplacer la première occurrence dans chaque ligne, il suffit d'enlever le suffixe 'g' à la fin : `sed s'/apples/oranges/' myfile.txt`.

Le 'g' est pour *global*.

La barre oblique `/` est le délimiteur. En fait, vous pouvez utiliser n'importe quel délimiteur.

Utilisons un seul underscore `_` comme délimiteur : `sed s'_apples_oranges_'g myfile.txt`.

Utiliser simplement `sed` ne remplace que sur la sortie standard. Le fichier original reste inchangé.

Pour changer le fichier 'sur place', utilisez le flag `-i` : `sed -i s'_apples_oranges_g' myfile.txt`.

## 7. Connaître l'adresse IP publique de votre ordinateur en utilisant `curl`

Il existe deux types d'adresses IP : privées et publiques.

Un système attribue des adresses IP internes qui peuvent être vérifiées en utilisant la commande `ifconfig`.

Mais voulez-vous connaître l'IP publique de votre ordinateur – l'adresse IP que le FAI attribue à votre interface ?

En ligne, utilisez simplement `curl ifconfig.me ; echo` ou `curl ifconfig.co ; echo` sur la ligne de commande.

## 8. Utilisez Ctrl + R (⌘ + R) pour la recherche inverse

Appuyer sur la touche 'flèche vers le haut' montre la dernière commande que vous avez tapée.

Taper `history` montre toutes les commandes que vous avez tapées et qui sont stockées dans l'historique bash.

Mieux encore, tapez Ctrl + r (⌘ + r) sur le shell et commencez à taper la commande.

Au fur et à mesure que vous tapez, le shell complète automatiquement depuis l'historique. Appuyez sur 'entrée' dès que vous trouvez la correspondance.

**Si vous ne retenez qu'une seule chose de ce tutoriel, retenez cette combinaison de touches : Ctrl + r (⌘ + r).**

Cela vous fera gagner beaucoup de temps, garanti !

## 9. Utilisez le shell pour faire des maths

Pour des calculs simples qui n'impliquent pas de fractions en entrée ou en sortie, vous pouvez simplement utiliser :

```typescript
:~$ echo $((19*34))
:~$ 646
```

Pour des calculs qui impliquent des fractions, il suffit de faire `echo` de l'expression et de la rediriger vers la commande `bc`.

```typescript
:~$ echo "scale=2; 9*3/((2*2)+1)" | bc
:~$ 5.40
```

Ici, 'scale' est la précision dont nous avons besoin. Je l'ai spécifiée à deux décimales.

## 10. Utilisez l'expansion d'accolades pour créer des fichiers en masse

Comment créer 100 fichiers dans un dossier ?

*file1.txt, file2.txt, file3.txt ... file100.txt*

En utilisant l'expansion d'accolades : `touch file{1..100}.txt`.

Nous devons créer trois fichiers pour notre projet : app.html, app.css et app.js

Au lieu de les créer un par un, nous pouvons simplement utiliser l'expansion d'accolades pour les créer tous en une seule fois.

```typescript
:~$ touch app.{html,css,js}
:~$ ls
app.html app.css app.js
:~$
```

Ou dans le dossier du projet, nous devons créer cinq répertoires : images, css, src, templates et scripts.

Nous pouvons utiliser :

```typescript
:~$ mkdir {images,css,src,templates,scripts}
:~$ ls
images css src templates scripts
:~$
```

Un seul avertissement ici : assurez-vous simplement qu'il n'y a pas d'espaces entre les mots à l'intérieur des accolades.

## Conclusion

J'ai listé 10 conseils pour la ligne de commande Bash avec lesquels vous pouvez travailler plus rapidement sur le terminal.

Apprenez ces commandes Bash et cela vous sera utile dans votre parcours de programmation.

Bon codage !