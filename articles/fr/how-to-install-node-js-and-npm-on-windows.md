---
title: Comment installer Node.js et npm sur Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T22:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e0c740569d1a4ca3b0a.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Windows
  slug: windows
seo_title: Comment installer Node.js et npm sur Windows
seo_desc: 'Installing Node.js and npm on Windows is very straightforward.

  First, download the Windows installer from the Node.js website. You will have the
  choice between the LTS (Long Term Support) or Current version.


  The Current version receives the latest f...'
---

Installer Node.js et npm sur Windows est très simple.

Tout d'abord, téléchargez l'installateur Windows depuis le [site web de Node.js](https://nodejs.org/). Vous aurez le choix entre la version **LTS** (Long Term Support) ou **Current**.

* La version **Current** reçoit les dernières fonctionnalités et mises à jour plus rapidement
* La version **LTS** renonce aux changements de fonctionnalités pour améliorer la stabilité, mais reçoit des correctifs tels que des corrections de bugs et des mises à jour de sécurité

Une fois que vous avez sélectionné une version qui répond à vos besoins, exécutez l'installateur. Suivez les invites pour sélectionner un chemin d'installation et assurez-vous que la fonction **npm package manager** est incluse avec le **Node.js runtime**. Cela devrait être la configuration par défaut.

Redémarrez votre ordinateur une fois l'installation terminée.

Si vous avez installé avec la configuration par défaut, Node.js devrait maintenant être ajouté à votre PATH. Ouvrez l'invite de commande ou PowerShell et entrez ce qui suit pour le tester :

```text
> node -v
```

La console devrait répondre avec une chaîne de version. Répétez le processus pour npm :

```text
> npm -v
```

Si les deux commandes fonctionnent, votre installation a réussi et vous pouvez commencer à utiliser Node.js !

## Plus d'informations sur Node.js

Selon son [dépôt GitHub](https://github.com/nodejs/node), Node.js est :

> Node.js est un environnement d'exécution JavaScript open-source et multiplateforme. Il exécute du code JavaScript en dehors d'un navigateur. Pour plus d'informations sur l'utilisation de Node.js, consultez le [site web de Node.js](https://nodejs.org/).

### Une analyse des faits sur Node.js :

* Node.js est un environnement d'exécution JavaScript construit sur le moteur V8 JavaScript de Chrome.  
Chaque navigateur dispose d'un moteur JavaScript intégré pour traiter les fichiers JavaScript contenus dans les sites web. Google Chrome utilise le moteur V8, qui est construit en C++. Node.js utilise également ce moteur ultra-rapide pour interpréter les fichiers JavaScript.
* Node.js utilise un modèle piloté par événements.  
Cela signifie que Node.js attend que certains événements se produisent. Il agit ensuite sur ces événements. Les événements peuvent être n'importe quoi, d'un clic à une requête HTTP. Nous pouvons également déclarer nos propres événements personnalisés et faire en sorte que Node.js écoute ces événements.
* Node.js utilise un modèle d'I/O non bloquant.  
Nous savons que les tâches d'I/O prennent beaucoup plus de temps que les tâches de traitement. Node.js utilise des fonctions de rappel pour gérer de telles requêtes.

Supposons qu'une tâche d'I/O particulière prend 5 secondes à s'exécuter, et que nous voulons effectuer cette I/O deux fois dans notre code.

**Python**

```python
import time

def my_io_task():
  time.sleep(5)
  print("done")

my_io_task()
my_io_task()
```

**Node.js**

```node
function my_io_task() {
    setTimeout(function() {
      console.log('done');
    }, 5000);
}

my_io_task();
my_io_task();
```

Les deux semblent similaires, mais le temps pris pour s'exécuter est différent. Le code Python prend 10 secondes pour s'exécuter tandis que le code Node.js ne prend que 5 secondes.

Node.js prend moins de temps grâce à son modèle d'I/O non bloquant. Le premier appel à `my_io_task()` démarre le minuteur et le laisse là. Il n'attend pas la réponse de la fonction. Au lieu de cela, il passe à l'appel de la deuxième `my_io_task()`, démarre le minuteur et le laisse là.

Lorsque le minuteur termine son exécution en 5 secondes, il appelle la fonction et imprime `done` sur la console. Puisque les deux minuteurs sont démarrés ensemble, ils se terminent ensemble et prennent donc le même temps.

## **Socket.io**

[Socket.io](https://socket.io/) est une bibliothèque Node.js conçue pour faciliter la communication en temps réel entre ordinateurs. Pour garantir cela, Socket.io utilise WebSockets pour établir une connexion entre le navigateur du client et le serveur. Cette bibliothèque utilise [Engine.IO](https://github.com/socketio/engine.io) pour établir la connexion.

### **Démos**

Pour avoir un aperçu de ce qui est possible, Socket.io propose deux démonstrations pour montrer ses cas d'utilisation possibles. Vous pouvez trouver les démonstrations à l'adresse [https://socket.io/demos/chat/](https://socket.io/demos/chat/) et trouver le lien vers la démonstration du tableau blanc sur la gauche.

### **Commencer**

Puisque Socket.io est une bibliothèque Node.js, vous devez vous assurer que Node.js est installé. Si ce n'est pas encore fait, obtenez la dernière version sur [Nodejs.org](https://nodejs.org/)

#### **macOS**

Node.js peut également être installé via [Homebrew](https://brew.sh/), un gestionnaire de paquets pour macOS.

Il suffit de taper `brew install node` pour installer Node.js.

Un guide [get started](https://socket.io/get-started/chat/) peut également être trouvé sur la page de Socket.io. Il montre comment construire facilement un chat en temps réel en seulement quelques lignes.

#### **Plus d'informations**

Plus d'informations sur Socket.io et sa documentation peuvent être trouvées à :

* [Socket.io](https://socket.io/)
* [Documentation Socket.io](https://socket.io/docs/)

### Plus d'informations sur Node.js

* [Site officiel de Node.js](https://nodejs.org/)
* [Node Version Manager](https://github.com/nvm-sh/nvm)
* [n: Interactive Node.js Version Manager](https://github.com/tj/n)
* [Documentation Node.js](https://nodejs.org/en/docs/)