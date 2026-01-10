---
title: Comment créer vos propres commandes sous Linux
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-02-17T23:04:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-own-command-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/BB
seo_title: Comment créer vos propres commandes sous Linux
---

Alias-Commands---Brief.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Dans cet article, apprenons à créer vos propres commandes sous Linux.\n  \ Oui – nous allons parler de la création d'une commande alias. \nAvant de commencer,\n  \ je veux vous dire comment l'idée de ce tutoriel est venue. \nL'un des followers\n  \ de mon blog m'a demandé ..."
---

Dans cet article, apprenons à créer vos propres commandes sous Linux. Oui – nous allons parler de la création d'une commande alias. 

Avant de commencer, je veux vous dire comment l'idée de ce tutoriel est venue. 

L'un des followers de mon blog m'a demandé, 

"Hey Arun ! Je me demande comment ton cerveau peut stocker autant de commandes. Comment est-ce possible ?"

"J'apprends Linux et j'écris du code depuis que j'ai commencé l'université (presque 7+ ans). Pendant cette période, j'ai rencontré beaucoup d'erreurs et j'ai résolu chacune d'entre elles par moi-même, ce qui m'a aidé à les maîtriser", ai-je répondu. 

"Même alors, comment peux-tu mémoriser ces flags et options avec chaque commande ?", a-t-il demandé. 

"Je ne peux pas mémoriser chaque commande avec ses options et flags. Donc, je crée mes propres commandes", ai-je répondu. 

"Quoi ? Tu as créé tes propres commandes ? Puis-je créer mes propres commandes ?", a-t-il demandé avec grande excitation. 

"Oui. Tu peux. C'est ce qu'on appelle une commande alias sous Linux", ai-je répondu. 

Il m'a demandé d'écrire un blog à ce sujet et le voici. Apprenons à propos des commandes `alias` dans ce blog. 

## Qu'est-ce que les commandes Alias sous Linux ?

La commande `alias` fournit une valeur de chaîne qui remplace un nom de commande lorsqu'il est rencontré. 

La commande `alias` vous permet de créer des raccourcis pour les longues commandes, les rendant plus faciles à retenir et à utiliser. Elle aura la même fonctionnalité que si la commande entière était exécutée. 

## Comment créer vos propres commandes Linux

En utilisant la commande `alias`, vous serez en mesure de créer vos propres commandes. C'est si simple de créer votre propre commande. 

Voici la syntaxe pour la commande `alias` :

```bash
alias [alias-name[=string]...]
```

Regardons un exemple de création de votre propre commande. 

Supposons que vous voulez créer une commande appelée `cdv`, et entrer la commande dans le terminal devrait vous amener au répertoire `Videos`. 

Habituellement, pour naviguer vers un répertoire, nous utilisons la commande `cd`. Pour naviguer vers `Videos`, nous devons utiliser `cd Videos` comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-121.png)
_Commande terminal pour naviguer vers le répertoire `Videos`_

Créons notre commande appelée `cdv` pour naviguer vers le répertoire `Videos`. Pour y parvenir, vous devez entrer la commande suivante dans votre terminal :

```bash
alias cdv="cd Videos"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-149.png)
_Commande terminal (`alias`) pour créer notre propre commande_

Nous avons créé notre commande. D'après la capture d'écran ci-dessus, vous pouvez voir qu'elle ne retourne rien. 

Mais, comment pouvons-nous vérifier que la commande est créée et qu'elle fonctionne ? 

Il n'y a qu'une seule façon de vérifier si la commande fonctionne : c'est en exécutant la commande créée. 

Exécutez la commande cdv sur votre terminal pour voir ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-150.png)
_Exécuter la commande créée `cdv`_

BOOM !!! Vous avez créé votre propre commande. 

## Comment voir les commandes Alias créées

Vous pouvez avoir la question suivante après avoir créé quelques commandes :

Supposons que j'ai créé plusieurs commandes alias. Comment puis-je les voir toutes ensemble ? Comment puis-je voir la commande équivalente de mon alias ? 

Vous pouvez voir toutes vos commandes alias en ajoutant le flag `-p` à la commande `alias` comme ceci :

```bash
alias -p
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-122.png)
_Commande terminal pour voir toutes les commandes alias créées_

J'ai créé de nombreuses commandes alias. D'après la capture d'écran ci-dessus, vous pouvez voir toutes les commandes alias que j'ai créées. 

## Comment supprimer une commande Alias sous Linux

Passez votre nom d'alias à la commande `unalias` en tant qu'argument pour supprimer la commande alias. 

```bash
unalias alias_name
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-123.png)
_Commande terminal (`unalias`) pour supprimer une commande alias_

## Comment supprimer toutes les commandes Alias sous Linux

Supposons que vous avez ajouté environ 20 commandes alias. Après un certain temps, vous avez réalisé que l'utilisation de commandes alias vous fera oublier les autres commandes à long terme. Craignant cela, vous souhaitez supprimer toutes les commandes alias. 

Nous avons une commande pour y parvenir :

```bash
unalias -a
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-124.png)
_Commande terminal pour supprimer toutes les commandes alias_

Vous pouvez être curieux d'en savoir plus sur une chose que j'ai écrite dans le passage ci-dessus. 

"Après un certain temps, vous avez réalisé que l'utilisation de commandes alias vous fera oublier les autres commandes à long terme"

Est-ce quelque chose dont vous devriez vous inquiéter ? Cela peut-il arriver ?

La réponse à votre première question est, oui. Définitivement, vous aurez cette sensation lorsque vous apprendrez et essayerez les commandes alias. Parce que j'ai eu la même sensation. 

La réponse à votre deuxième question est, absolument non. Cela entraînera une augmentation de la productivité. Il y a une forte chance que vous oubliiez la commande que vous avez créée, mais vous n'oublierez jamais la commande originale. Donc, je recommande toujours de revisiter vos commandes alias souvent et de vous assurer que vous utilisez toutes les commandes alias que vous avez créées. 

J'ai une surprise choquante pour vous. Ouvrez une fenêtre de terminal et créez une commande alias (nous utiliserons la commande `cdv` que nous avons créée ci-dessus). Ouvrez une autre fenêtre de terminal et tapez la commande `cdv` là-bas. 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-127.png)
_Commande terminal montrant la sortie de la commande alias non existante_

Surpris ? 

Oui. Si vous créez une commande alias, elle ne sera active que pour l'instance particulière du terminal. Elle ne sera pas créée de manière permanente, donc vous ne pourrez pas y accéder dans deux fenêtres de terminal différentes à moins d'exécuter la commande `alias` sur les deux terminaux. 

## Comment créer une commande Alias permanente

Pour créer une commande `alias` permanente, vous devez ajouter la commande alias au fichier de configuration du shell. Il existe de nombreuses configurations de shell disponibles. Quelques-uns des shells bien connus sont :

* Bash - ~/.bashrc
* Zsh - ~/.zshrc
* Fish - ~/.config/fish/config.fish

La plupart des distributions Linux fonctionnent avec `bash`, alors regardons comment créer un alias permanent dans le shell bash. Les autres shells fonctionnent à peu près de la même manière. 

Ouvrons le fichier `.bashrc` en utilisant Vim. 

```bash
sudo vim ~/.bashrc
```

Naviguez jusqu'en bas du fichier et appuyez sur `i` pour entrer en mode Insertion. Ajoutez la commande alias que vous souhaitez ajouter de manière permanente. 

```bash
alias cdv="cd Videos"
```

Enregistrez et quittez Vim en appuyant sur la touche `Esc` et en tapant `:wq`. 

Chaque fois que vous apportez une modification au fichier de configuration du shell, vous devez recharger le fichier pour que vos modifications prennent effet immédiatement. 

Toutes les fenêtres de terminal que vous ouvrez à partir de maintenant contiendront votre commande alias par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-139.png)
_Commande terminal pour voir toutes les commandes `alias`_

Vous pouvez ouvrir plusieurs fenêtres et vérifier en entrant la commande `alias -p`. 

## Quelques commandes Alias utiles à essayer

Voici un bonus pour vous tous. 

Dans l'entreprise où je travaille, nous suivons des commandes alias communes, que nous configurons dans la machine de tout le monde lors de l'intégration. Si les gens souhaitent ajouter leurs propres commandes, ils pourront le faire et cela ne sera pas reflété pour les autres (construit avec le principe OCP en tête). Nous nous sentons très productifs en utilisant ces commandes. 

J'ai prévu de partager une partie de ces commandes avec vous tous. 

Vous pouvez soit suivre les instructions dans le fichier README de [ce](https://www.freecodecamp.org/news/p/4e15c27a-7862-4f28-9a1d-8ddf54f0befc/github.com/gogosoon/x-commands.git) dépôt, soit suivre les instructions ci-dessous pour configurer les commandes alias sur votre machine. 

### Naviguer vers le dossier Home

```bash
cd ~/
```

### Cloner le dépôt

Clonez le dépôt des commandes alias depuis GitHub :

```bash
git clone https://github.com/gogosoon/x-commands.git
```

### Ajouter une référence au fichier de commandes alias

Ouvrez le fichier `~/.bashrc` en utilisant Vim :

```bash
sudo vim ~/.bashrc
```

Ajoutez la ligne suivante à la fin du fichier :

```bash
source ~/x-commands/aliasCommands.sh
```

Enregistrez et quittez Vim en appuyant sur `Esc` et en tapant `:wq`

### Recharger le terminal

Rechargez le terminal en exécutant la commande suivante :

```bash
source ~/.bashrc
```

C'est tout. Vous êtes prêt. Pour vérifier que la configuration est faite et qu'elle est opérationnelle, exécutez la commande suivante dans le terminal :

```bash
welcome
```

On vous demandera d'entrer votre nom. Tapez votre nom et appuyez sur `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-151.png)
_Commande terminal pour vérifier l'installation des commandes alias_

Vous l'avez installé de la bonne manière si vous obtenez le message ci-dessus. 

Permettez-moi de vous expliquer les commandes `alias` auxquelles vous aurez accès en utilisant ce dépôt. 

<table>
  <tbody>
    <tr><td></td>
      <td><strong>Commande Alias</strong></td>
      <td><strong>Commande Originale</strong></td>
      <td><strong>Description</strong></td>
    </tr>
    <tr><td></td>
      <td>f</td>
      <td><code>cd $1</code></td>
      <td>Aller vers l'avant. Naviguer vers le répertoire suivant spécifié</td>
    </tr>
    <tr><td></td>
      <td>b</td>
      <td><code>cd ..</code></td>
      <td>Aller vers l'arrière. Naviguer en arrière d'un répertoire</td>
    </tr>
    <tr><td></td>
      <td>c</td>
      <td><code>code ./</code></td>
      <td>Ouvrir Visual Studio Code dans le répertoire courant</td>
    </tr>
    <tr><td></td>
      <td>e</td>
      <td><code>exit</code></td>
      <td>Fermer l'onglet/fenêtre du terminal</td>
    </tr>
    <tr><td></td>
      <td>home</td>
      <td><code>cd ~</code></td>
      <td>Naviguer vers le répertoire home</td>
    </tr>
    <tr><td></td>
      <td>a</td>
      <td><code>xdotool key ctrl+shift+t</code></td>
      <td>Ouvrir un nouvel onglet de terminal</td>
    </tr>
    <tr><td></td>
      <td>cdb</td>
      <td><code>cd -</code></td>
      <td>Aller au dernier répertoire où vous étiez précédemment</td>
    </tr>
    <tr><td></td>
      <td>gst</td>
      <td><code>git status</code></td>
      <td>Trouver le statut du dépôt git</td>
    </tr>
    <tr><td></td>
      <td>gpr</td>
      <td><code>git pull -r</code></td>
      <td>Pull et rebase les commits git</td>
    </tr>
    <tr><td></td>
      <td>glo</td>
      <td><code>git log --oneline</code></td>
      <td>Afficher les logs des commits git en une seule ligne simplifiée</td>
    </tr>
    <tr><td></td>
      <td>gcl</td>
      <td><code>git config -l</code></td>
      <td>Afficher la configuration git du dépôt courant</td>
    </tr>
    <tr><td></td>
      <td>gca</td>
      <td><code>git commit --amend</code></td>
      <td>Ajouter les changements courants au commit existant</td>
    </tr>
    <tr><td></td>
      <td>gcane</td>
      <td><code>git commit --amend --no-edit</code></td>
      <td>Ajouter les changements courants au commit existant sans éditer le message de commit existant</td>
    </tr>
    <tr><td></td>
      <td>ad</td>
      <td><code>~/Android/Sdk/emulator/emulator -list-avds</code></td>
      <td>Afficher les émulateurs Android disponibles</td>
    </tr>
    <tr><td></td>
      <td>off</td>
      <td><code>sudo /opt/lampp/lampp stop<br>poweroff<br>systemctl poweroff -i<br></code></td>
      <td>Éteindre votre machine</td>
    </tr>
    <tr><td></td>
      <td>bb</td>
      <td>
        <code>if [ -z "$1" ]<br>then<br>b;b<br>else<br>for (( i=0;i&lt;$1;i++ ))<br>do<br>b<br>done<br>fi<br></code>
      </td>
      <td>C'est une version avancée de la commande de retour en arrière. Entrer la commande <code>b</code> revient en arrière d'un seul
        répertoire. Mais entrer bb revient en arrière de 2 répertoires. Si vous voulez revenir en arrière de 5 répertoires, exécutez
        la commande <code>bb 5</code></td>
    </tr>
    <tr><td></td>
      <td>pokill</td>
      <td><code>kill $(lsof -t -i:$1)</code></td>
      <td>Tuer le programme en cours d'exécution sur le port</td>
    </tr>
    <tr><td></td>
      <td>cc</td>
      <td><code>sudo nano ~/x-commands/aliasCommands.sh</code></td>
      <td>Éditer le fichier des commandes alias</td>
    </tr>
    <tr><td></td>
      <td>bc</td>
      <td><code>sudo nano ~/.bashrc</code></td>
      <td>Éditer le fichier <code>.bashrc</code></td>
    </tr>
    <tr><td></td>
      <td>scc</td>
      <td><code>source ~/x-commands/aliasCommands.sh</code></td>
      <td>Rafraîchir le terminal après la mise à jour d'une commande alias</td>
    </tr>
    <tr><td></td>
      <td>bcc</td>
      <td><code>source ~/.bashrc</code></td>
      <td>Rafraîchir le terminal après la mise à jour du fichier <code>.bashrc</code></td>
    </tr>
    <tr><td></td>
      <td>welcome</td>
      <td>
        <code>echo Bienvenue dans l'automatisation shell<br>echo Entrez Votre Nom<br>read testName<br>echo Bienvenue dans le nouveau monde des raccourcis ~~ $testName ~~ Profitez du Codage....<br></code>
      </td>
      <td>Vérifier si l'installation des commandes alias est faite correctement</td>
    </tr>
  </tbody>
</table>

Si vous regardez attentivement le fichier aliasCommands.sh, vous verrez que j'ai ajouté quelques fonctions. Vous vous demandez peut-être pourquoi j'utilise des fonctions. Lisez la suite pour avoir un aperçu rapide de ce sujet. 

## Comment exécuter plusieurs commandes dans une seule commande Alias

Vous pouvez y parvenir de 2 manières. Permettez-moi de vous expliquer les deux ici. 

Apprenons cela avec un exemple. 

Disons que vous devez créer une commande alias appelée `gohome`. L'exécution de cette commande devrait vous amener au répertoire home et afficher le message "Navigué vers le répertoire home".

### Méthode #1 :

Cette méthode est la manière habituelle d'ajouter une commande `alias`. Vous devez ajouter les deux commandes séparées par un point-virgule (`;`). 

```bash
alias gohome="cd ~/;echo Navigué vers le répertoire home"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-148.png)
_Exécuter plusieurs commandes avec une seule commande alias - Méthode 1_

### Méthode #2

C'est une méthode un peu différente. Pour y parvenir, vous devez apporter une modification à votre fichier `.bashrc`. Vous devez définir une fonction dans le fichier `.bashrc` avec toutes les commandes imbriquées à l'intérieur. 

Ouvrez le fichier `.bashrc` en utilisant Vim. 

```bash
sudo vim ~/.bashrc
```

Entrez en mode insertion en appuyant sur la touche `i`. 

Créez une fonction nommée `gohome` avec les 2 commandes ci-dessus. 

```bash
function gohome() {
        cd ~/
        echo Navigué vers le répertoire home
}
```

Enregistrez et quittez Vim en appuyant sur la touche `Esc` et en tapant `:wq` en mode commande. 

Rechargez le terminal en exécutant `source ~/.bashrc` et vous pourrez vérifier la commande `gohome` maintenant. 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-152.png)
_Exécuter plusieurs commandes avec une seule commande alias - Méthode 2_

**Note :** La création d'une fonction ne la listera pas comme une commande alias lors de l'exécution de la commande `alias -p`. 

## Conclusion

Dans cet article, vous avez appris à créer vos propres commandes sous Linux. 

L'utilisation d'une commande alias augmentera définitivement votre productivité. J'ai été témoin d'une croissance exponentielle chez de nombreuses personnes après les avoir vues utiliser des commandes alias. Je vous recommande à tous de configurer vos propres commandes alias. 

Pour en savoir plus sur Linux, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_alias_command) et suivez-moi sur les réseaux sociaux.