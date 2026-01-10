---
title: Comment bloquer les sites web improductifs et augmenter votre productivité
  en utilisant JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:56:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-block-unproductive-websites-and-boost-your-productivity-using-javascript-20534011cccc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9-xBdZXdd_FT1X-DTTX75A.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
seo_title: Comment bloquer les sites web improductifs et augmenter votre productivité
  en utilisant JavaScript
seo_desc: 'By Madhav Bahl

  Tired of wasting your time on various unproductive websites? Why not make a script
  which would help you limit the time you spend on these websites?

  Does this sound familiar…?


  Just another day, scrolling through my Social Media feed an...'
---

Par Madhav Bahl

Fatigué de perdre votre temps sur divers sites web improductifs ? Pourquoi ne pas créer un script qui vous aiderait à limiter le temps que vous passez sur ces sites ?

Cela vous semble familier… ?

> Juste une autre journée, à faire défiler mon fil d'actualité sur les **réseaux sociaux** et à regarder des memes. J'ai réalisé qu'il s'était écoulé 4 heures depuis que j'étais assis à la même position et que je "ne faisais rien". Je détestais ça ! Je devais faire quelque chose. L'idée m'est venue : pourquoi ne pas créer un script qui m'aiderait à limiter le temps que je passe sur ces sites ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*bIF5jb6o8DpD_JvS.jpg)
_Arrêtez de faire défiler votre fil d'actualité et faites quelque chose xD (source : [https://www.writerswrite.com/writingmemes/](https://www.writerswrite.com/writingmemes/" rel="noopener" target="_blank" title="))_

Et si nous créions un script qui bloquerait tous ces sites ? Le script vous permet de les utiliser uniquement à certaines heures spécifiques de la journée. Cela semble légitime ! Faisons-le. :-)

Oui, je sais qu'il existe de nombreuses méthodes faciles pour bloquer n'importe quel site web. Il suffit de télécharger un plugin Chrome, ou un logiciel qui le ferait pour nous. Bien sûr, c'est assez facile ! Mais allons, nous sommes des développeurs, nous ne faisons pas ces choses ! Lorsque nous avons besoin de quelque chose, nous développons des scripts plutôt que d'utiliser des astuces aléatoires pour faire le travail… n'est-ce pas ?!

Si vous souhaitez télécharger le script directement, vous pouvez le faire à partir d'[ici](https://github.com/MadhavBahlMD/Control-Yourself/blob/master/JavaScript/blocker.js).

### Commençons !

Contrairement à mes autres articles de tutoriel, vous n'aurez pas besoin d'une structure de répertoire ou d'un environnement de développement pour ce projet. Tout ce dont vous avez besoin, c'est de NodeJS installé sur votre système et d'un bon éditeur de texte. Vous pouvez créer ce script en utilisant n'importe quel langage de votre choix qui supporte la gestion de fichiers. J'ai choisi JavaScript parce que je l'adore !

![Image](https://cdn-media-1.freecodecamp.org/images/0*Fhqu52MS8kbjNWKY.png)
_**J'❤️ JavaScript !** (source : [https://brendaneich.com/2015/06/from-asm-js-to-webassembly/](https://brendaneich.com/2015/06/from-asm-js-to-webassembly/" rel="noopener" target="_blank" title="))_

### L'idée de base

L'idée derrière ce bloqueur que nous allons créer est très simple. Il existe un fichier nommé `hosts`. Nous pouvons ajouter l'URL de n'importe quel site web et l'URL d'un site web vers lequel nous voulons rediriger le premier site web. Quelque chose comme ceci :

```
127.0.0.1    www.facebook.com
```

Maintenant, chaque fois que nous essayons d'ouvrir Facebook, il sera automatiquement redirigé vers 127.0.0.1 (localhost). Cela bloquera indirectement le site web.

Le fichier hosts dont je parle est présent dans `C:\Windows\System32\drivers\etc\hosts` si vous utilisez Windows. Si vous êtes un utilisateur de Mac ou Linux, l'emplacement de ce fichier est : `/etc/hosts`.

### Modifions le fichier…

Avant de commencer le code, essayons de modifier le fichier et voyons si cela fonctionne. Veuillez noter que seul l'utilisateur avec des droits d'administrateur peut modifier ce fichier. Si vous êtes sous Windows, vous pouvez cliquer avec le bouton droit sur ce fichier et l'ouvrir en tant qu'administrateur. Si vous utilisez Linux, vous pouvez utiliser la commande sudo. J'utilise nano pour ouvrir le fichier, vous pouvez utiliser un autre éditeur de votre choix.

```
sudo nano /etc/hosts
```

Après avoir tapé cette commande, il vous demandera d'entrer votre mot de passe. Vous pouvez l'entrer et ouvrir votre fichier. Essayons-le :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0MXqMMIcuM34PF780gIO-w.gif)

D'accord, nous avons ajouté notre site web "à bloquer" dans le fichier hosts, vérifions maintenant si cela a fonctionné ou non. Pour le vérifier, allez sur n'importe quel navigateur web et rendez-vous sur ce site web.

![Image](https://cdn-media-1.freecodecamp.org/images/0*l-CTDo6vZEcLlSUu.png)
_Yippee ! Cela a fonctionné :3_

Maintenant que nous avons vérifié que notre concept est correct, codons le bloqueur.

### 1. Configuration des variables

Comme je l'ai dit plus tôt, il n'est pas nécessaire d'avoir une structure de répertoire complexe ou de configurer un environnement de développement. Tout ce que vous avez à faire est de créer un fichier JavaScript (par exemple, `blocker.js`) et de commencer à coder.

Tout d'abord, nous devons importer le module Node `fs` (système de fichiers) grâce auquel nous apporterons des modifications à notre fichier hosts. Vous pouvez lire la documentation complète de fs [ici](https://nodejs.org/api/fs.html).

```
const fs = require('fs');
```

Maintenant, nous devrons initialiser 3 variables :

1. **filePath** — Pour stocker le chemin du fichier hosts
2. **redirectPath** — Pour le chemin de redirection (ici, localhost)
3. **websites** — Tableau des sites web à bloquer

De plus, nous créerons une variable nommée `delay`. Cette variable stockera la valeur de la durée (en millisecondes) après laquelle notre script se répétera. L'idée de base est de garder le script en cours d'exécution en permanence pour vérifier s'il est temps de bloquer/débloquer les sites web. Pour le garder en cours d'exécution, nous utiliserons la méthode `setInterval()` en JavaScript. Nous pouvons également utiliser `while (true) {}` pour créer une boucle infinie.

Pour l'instant, nous gardons le temps après lequel la fonction se répète constant (par exemple, 10 secondes). Mais ce script peut être rendu plus intelligent en définissant la valeur de delay égale à la différence de temps entre l'heure actuelle et l'heure à laquelle l'état du script (bloquer/débloquer) doit être changé. Faire cela est beaucoup plus facile que ce que l'on pourrait penser — donc je veux que vous (le lecteur) le fassiez vous-même et m'envoyiez un [mail](http://www.madhavbahl.tech/), j'adorerais avoir de vos nouvelles ?

```
const filePath = "/etc/hosts";
const redirectPath = "127.0.0.1";
let websites = [
  "www.someRandomWebsite.com",
  "anotherWebsite.com"
];
let delay = 10000;
```

**Note** : Si vous êtes un utilisateur Windows, stockez ceci dans la variable filePath : C:\Windows\System32\drivers\etc\hosts

### 2. La fonction de blocage

Nous allons maintenant créer une fonction de blocage. Nous l'appelons à partir de la méthode setInterval pour la garder en cours d'exécution après chaque intervalle de temps donné.

```
let blocker = () => {
    ....
    ....
};
```

**Maintenant, nous allons remplir le code à l'intérieur de notre fonction de blocage.**

#### À l'intérieur de blocker : Obtenir l'heure actuelle

Tout d'abord, nous devons obtenir l'heure actuelle, puis vérifier s'il est temps de bloquer le site web ou de le débloquer.

```
let date = new Date();
let hours = date.getHours();
if (hours >= 14 && hours < 18) {
    console.log('Time to block websites');
    ....
    ....
} else {
    console.log('Time to unblock websites');
    ....
    ....
}
```

#### À l'intérieur de blocker : À l'intérieur de If — La condition If est vraie

Maintenant, nous devons lire le fichier hosts et convertir les données récupérées en chaîne de caractères (la fonction `readFile()` retournera les données de buffer qui doivent être converties en chaîne de caractères).

Après avoir lu le fichier, nous devons vérifier si chaque site web et le chemin de redirection sont présents dans le fichier hosts ou non. S'ils sont présents, nous pouvons les ignorer. Sinon, nous devons ajouter `redirectPath websiteURL` qui ressemblera à ceci :

```
127.0.0.1    www.someRandomWebsite
```

Pour implémenter cela, nous utiliserons une boucle for. La boucle itérera à travers chaque URL dans le tableau des sites web et vérifiera s'il existe à l'intérieur du fichier. Pour ce faire, nous utiliserons la méthode `indexOf()` des chaînes de caractères. Si la valeur est supérieure à zéro, c'est-à-dire que le site web donné est présent à l'intérieur du fichier hosts, nous pouvons simplement l'ignorer. Sinon, si la valeur n'est pas supérieure à zéro, nous devons ajouter le redirectPath et l'URL du site web (séparés par un espace) au fichier.

```
fs.readFile(filePath, (err, data) => {
    fileContents = data.toString();
    for (let i = 0; i < websites.length; i++) {
        let addWebsite = "\n" + redirectPath + " " + websites[i];
        if (fileContents.indexOf(addWebsite) < 0) {
            console.log('Website not present in hosts file');
            fs.appendFile(filePath, addWebsite, (err) => {
                if (err) return console.log(err);
                console.log('File Updated Successfully');
            });
        } else {
            console.log('Website is present');
        }
    }
});
```

#### À l'intérieur de blocker : À l'intérieur de Else — Si la condition est fausse

Si la condition est fausse, nous devons vérifier si les sites web de la liste sont présents dans le fichier hosts. S'ils sont présents, nous devons les supprimer.

Pour supprimer, nous utiliserons une astuce simple. Nous lirons le fichier ligne par ligne. Nous créons une chaîne de caractères vide et vérifions si la ligne actuelle contient l'un des sites web présents dans la liste. Si oui, nous l'ignorons simplement. Sinon, nous ajouterons cette ligne à la chaîne de caractères que nous avons initialisée. Après avoir vérifié la dernière ligne, nous remplacerons simplement le contenu actuel du fichier par cette chaîne de caractères completeContent.

Le code pour le faire est très simple. Initialisez d'abord une chaîne de caractères vide (`completeContent`). Ensuite, lisez le fichier ligne par ligne. Suivez les étapes données dans le code ci-dessous. Ensuite, remplacez le contenu du fichier par la variable completeContent.

```
// Initialiser la chaîne de caractères vide
let completeContent = '';
```

```
// Lire le fichier ligne par ligne
fs.readFileSync(filePath)
    .toString()
    .split()
    .forEach((line) => {
        ....
        ....
        ....
        // Faire la procédure donnée ci-dessous pour mettre à jour completeContent
    });
```

```
// Remplacer le contenu du fichier par la variable `completeContent`
fs.writeFile(filePath, completeContent, (err) => {
    if (err) {
        return console.log('Error!', err);
    }
});
```

Maintenant que nous avons accès à chaque ligne, nous pouvons vérifier si cette ligne contient un site web en utilisant un drapeau et une boucle for. Nous définissons le drapeau à 1 (ou vrai) puis exécutons une boucle pour itérer à travers la liste des sites web. Si la ligne contient le site web actuel (nous le vérifierons en utilisant la méthode `string.indexOf(substring)`), nous réinitialisons le drapeau à 0 et sortons de la boucle actuelle. En dehors de la boucle, nous vérifions si le drapeau est à 1 (ou vrai), nous ajoutons la ligne actuelle à la variable `completeContent`.

**Veuillez également noter** que si le drapeau est à 1, nous vérifions également si la ligne actuelle est la dernière ligne ou non. Si ce n'est pas la dernière ligne, nous ajoutons la ligne actuelle à la chaîne de caractères `completeContent` avec un `"\n"` afin que la ligne suivante soit ajoutée à `completeContent` à partir d'une nouvelle ligne (ou avec un saut de ligne). Suivez le code suivant à l'intérieur du forEach() du bloc de code ci-dessus.

```
let flag = 1;
for (let i = 0; i < websites.length; i++) {
    if (line.indexOf(websites[i]) >= 0) { // la ligne contient le site web
        flag = 0;
        break;
    }
}
```

```
if (flag == 1) {
    if (line === '')
        completeContent += line;
    else
        completeContent += line + "\n";
}
```

### 3. Exécution du code pour la fonction de blocage

Voici le code pour la fonction de blocage au cas où vous auriez été confus avec le code distribué dans la section 2 :

Maintenant, pour exécuter cette fonction en continu, nous pouvons opter pour `while (true) {}` comme boucle infinie. À l'intérieur, nous pouvons donner un certain délai afin qu'elle n'occupe pas le processeur en continu.

Ou, une meilleure option est d'utiliser la fonction `setInterval()`. Cela répète la fonction de blocage après un intervalle de temps spécifique. Mais, `setInterval()` s'exécutera pour la première fois après le délai spécifié. Par conséquent, nous devrons appeler la fonction de blocage une fois avant la fonction setInterval.

```
blocker();
setInterval(blocker, delay);
```

### 4. Tout est fait ! Vérifions notre script

Il est temps d'exécuter notre script. Pour exécuter le script, ouvrez le répertoire de travail actuel dans un terminal et tapez la commande suivante :

```
sudo node blocker.js
```

Si vous êtes un utilisateur Windows, vous pouvez ouvrir l'invite de commande en tant qu'administrateur, aller dans le répertoire du projet, puis exécuter la commande :

```
node blocker.js
```

Veuillez noter que, juste pour vérifier, je bloque `facebook.com`. Voici le test :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3csxXZL_6AjyODUwXucfbw.gif)
_Yuss ! Nous l'avons fait ❤️_

### 5. La dernière étape...

#### Pour Mac et Linux

Vous pouvez planifier ce script pour qu'il s'exécute chaque fois que quelqu'un démarre le système en utilisant crontab. Cron est un planificateur de tâches basé sur le temps dans les systèmes d'exploitation de type Unix. Vous pouvez en lire plus sur cron [ici](https://opensource.com/article/17/11/how-use-cron-linux).

Nous allons donc ajouter notre commande grâce à laquelle nous exécutons le script (`sudo node blocker.js`) dans la table cron. Faire cela est très simple : ouvrez le terminal en utilisant `ctrl+alt+t`, puis ouvrez crontab en utilisant `sudo crontab -e`. Cette commande ouvrira la table cron.

**Notez** que nous avons utilisé `sudo crontab`, et non `crontab`. Cela nous permettra de modifier la table cron.

Une fois que vous l'avez ouverte, ajoutez cette ligne à la fin (remplacez `path-to-script` par le chemin de votre répertoire de projet) :

```
@reboot node /path-to-script/blocker.js
```

C'est tout ! Faire cela exécutera votre script chaque fois que le système redémarre.

#### Pour Windows

Le script peut être planifié pour s'exécuter chaque fois que le système démarre sous Windows également. [Voici](https://www.howtogeek.com/138159/how-to-enable-programs-and-custom-scripts-to-run-at-boot/) un très bon article qui explique comment le faire.

### Où aller à partir de là ?

Êtes-vous un passionné de l'open source ? Voulez-vous contribuer à ce projet ?
Je commence un nouveau projet Open Source nommé **"Control-Yourself"** qui sera une application de bureau faite en utilisant [Electron](https://electronjs.org/). Les fonctionnalités incluront :

* Prendre les entrées des utilisateurs sur les heures auxquelles ils veulent bloquer quels sites web
* Suivre le temps qu'un utilisateur passe à regarder les sites web des réseaux sociaux
* Un minuteur Pomodoro
* Et une application de liste de tâches avec un rapport quotidien de progression de la productivité.

Consultez le [dépôt](https://github.com/MadhavBahlMD/Control-Yourself), et ajoutez un commentaire "intéressé" sur le problème qui vous intéresse.

Maintenant, laissez-moi vous donner le code complet avec des commentaires appropriés qui vous aideront à comprendre le code :

**Code complet (blocker.js)**

### C'est tout

Avez-vous trouvé l'article utile ?

[Abonnez-vous à TheLeanProgrammer](http://madhavbahl.tech/subscribe/) pour être le premier à être informé par moi des futures mises à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L-3kS5mz7jp4e8zV8WLoLQ.png)

N'hésitez pas à me contacter à tout moment si vous voulez discuter de quelque chose :D

Je serais plus que ravi si vous envoyez vos commentaires ou suggestions, ou si vous posez des questions. De plus, j'adore me faire de nouveaux amis — alors envoyez-moi simplement un mail.

> Merci beaucoup d'avoir lu jusqu'à la fin. Vous pouvez me contacter si vous avez besoin d'une assistance :
> Email : madhavbahl10[at]gmail[dot]com
> Web : [http://madhavbahl.tech/](http://madhavbahl.ml/)
> Github : [https://github.com/MadhavBahlMD](https://github.com/MadhavBahlMD)
> LinkedIn : [https://www.linkedin.com/in/madhavba_hl/_](https://www.linkedin.com/in/madhavbahl/)