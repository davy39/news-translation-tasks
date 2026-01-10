---
title: Linux chmod et chown – Comment changer les permissions et la propriété des
  fichiers sous Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-27T00:38:38.000Z'
originalURL: https://freecodecamp.org/news/linux-chmod-chown-change-file-permissions
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/guided-exercise--1-.png
tags:
- name: information security
  slug: information-security
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Linux chmod et chown – Comment changer les permissions et la propriété
  des fichiers sous Linux
seo_desc: "Linux is a multi user OS which means that it supports multiple users at\
  \ a time. \nAs many people can access the system simultaneously and some resources\
  \ are shared, Linux controls access through ownership and permissions. \nLinux file\
  \ ownership\nIn Linu..."
---

Linux est un système d'exploitation multi-utilisateurs, ce qui signifie qu'il supporte plusieurs utilisateurs simultanément.

Comme de nombreuses personnes peuvent accéder au système en même temps et que certaines ressources sont partagées, Linux contrôle l'accès via la propriété et les permissions.

## Propriété des fichiers sous Linux

Sous Linux, il existe trois types de propriétaires : `user` (utilisateur), `group` (groupe) et `others` (autres).

### **Utilisateur Linux**

Un utilisateur est le propriétaire et créateur par défaut du fichier. Cet utilisateur est donc également appelé propriétaire.

### **Groupe Linux**

Un groupe d'utilisateurs est une collection d'utilisateurs. Les utilisateurs appartenant à un groupe auront les mêmes permissions de groupe Linux pour accéder à un fichier/dossier.

Vous pouvez utiliser des groupes pour attribuer des permissions en masse au lieu de les attribuer individuellement. Un utilisateur peut également appartenir à plusieurs groupes.

### **Autres**

Tout utilisateur qui ne fait pas partie des classes utilisateur ou groupe appartient à cette classe.

## Permissions des fichiers Linux

Les permissions des fichiers se divisent en trois catégories : `read` (lecture), `write` (écriture) et `execute` (exécution).

### **Permission de lecture**

Pour les fichiers réguliers, les permissions de lecture permettent aux utilisateurs d'ouvrir et de lire le fichier uniquement. Les utilisateurs ne peuvent pas modifier le fichier.

De même, pour les répertoires, les permissions de lecture permettent de lister le contenu du répertoire sans aucune modification dans celui-ci.

### **Permission d'écriture**

Lorsque les fichiers ont des permissions d'écriture, l'utilisateur peut modifier (éditer, supprimer) le fichier et l'enregistrer.

Pour les dossiers, les permissions d'écriture permettent à un utilisateur de modifier son contenu (créer, supprimer et renommer les fichiers à l'intérieur) et de modifier le contenu des fichiers pour lesquels l'utilisateur a des permissions d'écriture.

### **Permission d'exécution**

Pour les fichiers, les permissions d'exécution permettent à l'utilisateur d'exécuter un script exécutable. Pour les répertoires, l'utilisateur peut y accéder et accéder aux détails des fichiers dans le répertoire.

Ci-dessous se trouve la représentation symbolique des permissions pour l'utilisateur, le groupe et les autres.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-157.png)
_Représentation symbolique des permissions_

Notez que nous pouvons trouver les permissions des fichiers et dossiers en utilisant la liste longue (`ls -l`) sur un terminal Linux.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-158.png)
_Sortie de la liste longue_

Dans la sortie ci-dessus, `d` représente un répertoire et `-` représente un fichier régulier.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-159.png)

## **Comment changer les permissions sous Linux en utilisant la commande `chmod`**

Maintenant que nous connaissons les bases des propriétés et des permissions, voyons comment nous pouvons modifier les permissions en utilisant la commande `chmod`.

**Syntaxe de `chmod` :**

```bash
chmod permissions filename
```

Où,

* `permissions` peut être read (lecture), write (écriture), execute (exécution) ou une combinaison de ceux-ci.
* `filename` est le nom du fichier pour lequel les permissions doivent être changées. Ce paramètre peut également être une liste de fichiers pour changer les permissions en masse.

Nous pouvons changer les permissions en utilisant deux modes :

1. **Mode symbolique** : cette méthode utilise des symboles comme `u`, `g`, `o` pour représenter les utilisateurs, les groupes et les autres. Les permissions sont représentées par `r, w, x` pour la lecture, l'écriture et l'exécution, respectivement. Vous pouvez modifier les permissions en utilisant +, - et =.
2. **Mode absolu** : cette méthode représente les permissions sous forme de nombres octaux à 3 chiffres allant de 0 à 7.

Maintenant, voyons-les en détail.

### Comment changer les permissions en utilisant le mode symbolique

Le tableau ci-dessous résume la représentation des utilisateurs :

<table>
<thead>
<tr>
<th>Représentation de l'utilisateur</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>u</td>
<td>utilisateur/propriétaire</td>
</tr>
<tr>
<td>g</td>
<td>groupe</td>
</tr>
<tr>
<td>o</td>
<td>autres</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Nous pouvons utiliser des opérateurs mathématiques pour ajouter, supprimer et attribuer des permissions. Le tableau ci-dessous montre le résumé :

<table>
<thead>
<tr>
<th>Opérateur</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>+</td>
<td>Ajoute une permission à un fichier ou répertoire</td>
</tr>
<tr>
<td>-</td>
<td>Supprime la permission</td>
</tr>
<tr>
<td>=</td>
<td>Définit la permission si elle n'est pas présente auparavant. Remplace également les permissions si elles ont été définies précédemment.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Exemple :

Supposons que j'ai un script et que je veux le rendre exécutable pour le propriétaire du fichier `zaira`.

Les permissions actuelles du fichier sont les suivantes :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-161.png)

Découpons les permissions comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-160.png)

Pour ajouter les droits d'exécution (`x`) au propriétaire (`u`) en utilisant le mode symbolique, nous pouvons utiliser la commande suivante :

```bash
chmod u+x mymotd.sh
```

**Sortie :**

Maintenant, nous pouvons voir que les permissions d'exécution ont été ajoutées pour le propriétaire `zaira`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-162.png)

**Exemples supplémentaires pour changer les permissions via la méthode symbolique :**

* Supprimer les permissions de `lecture` et `écriture` pour le `groupe` et les `autres` : `chmod go-rw`.
* Supprimer les permissions de `lecture` pour les `autres` : `chmod o-r`.
* Attribuer la permission d'`écriture` au `groupe` et remplacer la permission existante : `chmod g=w`.

### Comment changer les permissions en utilisant le mode absolu

Le mode absolu utilise des nombres pour représenter les permissions et des opérateurs mathématiques pour les modifier.

Le tableau ci-dessous montre comment nous pouvons attribuer les permissions pertinentes :

<table>
<thead>
<tr>
<th>Permission</th>
<th>Attribuer la permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>lecture</td>
<td>ajouter 4</td>
</tr>
<tr>
<td>écriture</td>
<td>ajouter 2</td>
</tr>
<tr>
<td>exécution</td>
<td>ajouter 1</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Les permissions peuvent être révoquées en utilisant la soustraction. Le tableau ci-dessous montre comment vous pouvez supprimer les permissions pertinentes.

<table>
<thead>
<tr>
<th>Permission</th>
<th>Révoquer la permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>lecture</td>
<td>soustraire 4</td>
</tr>
<tr>
<td>écriture</td>
<td>soustraire 2</td>
</tr>
<tr>
<td>exécution</td>
<td>soustraire 1</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Exemple :**

* Définir `lecture` (ajouter 4) pour `user`, `lecture` (ajouter 4) et `exécution` (ajouter 1) pour le groupe, et seulement `exécution` (ajouter 1) pour les autres.

`chmod 451 file-name`

Voici comment nous avons effectué le calcul :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-163.png)

Notez que cela est équivalent à `r--r-x--x`.

* Supprimer les droits d'`exécution` pour `other` et `group`.

Pour supprimer l'exécution pour `other` et `group`, soustrayez 1 de la partie exécution des deux derniers octets.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-164.png)

* Attribuer `lecture`, `écriture` et `exécution` à `user`, `lecture` et `exécution` à `group` et seulement `lecture` aux autres.

Cela serait équivalent à `rwxr-xr--`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-165.png)

## Comment changer la propriété en utilisant la commande `chown`

Ensuite, nous allons apprendre comment changer la propriété d'un fichier. Vous pouvez changer la propriété d'un fichier ou d'un dossier en utilisant la commande `chown`. Dans certains cas, changer la propriété nécessite des permissions `sudo`.

Syntaxe de `chown` :

```bash
chown user filename

```

### Comment changer la propriété de l'utilisateur avec `chown`

Transférons la propriété de l'utilisateur `zaira` à l'utilisateur `news`.

`chown news mymotd.sh`

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-167.png)

Commande pour changer la propriété : `sudo chown news mymotd.sh`

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-168.png)

### Comment changer la propriété de l'utilisateur et du groupe simultanément

Nous pouvons également utiliser `chown` pour changer l'utilisateur et le groupe simultanément.

```bash
chown user:group filename
```

### Comment changer la propriété d'un répertoire

Vous pouvez changer la propriété de manière récursive pour le contenu d'un répertoire. L'exemple ci-dessous change la propriété du dossier `/opt/script` pour permettre à l'utilisateur `admin`.

```bash
chown -R admin /opt/script
```

### Comment changer la propriété du groupe

Dans le cas où nous devons uniquement changer le propriétaire du groupe, nous pouvons utiliser `chown` en précédant le nom du groupe par un deux-points `:`

```bash
chown :admins /opt/script
```

## Exercice guidé sur les permissions Linux

Jusqu'à présent, nous avons exploré les permissions, les propriétés et les méthodes pour les changer. Maintenant, nous allons renforcer notre apprentissage avec un exercice guidé.

**Objectif** : Créer des groupes et attribuer les permissions pertinentes à ses membres. Vérifier l'accès en y accédant depuis des utilisateurs non autorisés.

**Tâche** : Créer un groupe appelé `dev-team` et ajouter deux membres (John et Bob). Créer un dossier `/home/dev-team` et changer la propriété pour le groupe `dev-team`. Vérifier que les deux utilisateurs du groupe `dev-team` ont un accès en _lecture_ et _écriture_ au dossier.

Créer un autre groupe `project-manager` et ajouter un utilisateur `Fatima`. Vérifier si le dossier `/home/dev-team` est accessible par `Fatima`.

### Visualisation du problème

Nous pouvons visualiser le problème comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Notes_220426_040131_1.jpg)

**Étape 1 : Passer à l'utilisateur root.**
Passez à l'utilisateur root afin d'avoir les droits de créer de nouveaux utilisateurs et groupes.

<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `sudo` avec le flag `i`.

Si vous avez le mot de passe root, vous pouvez vous connecter en utilisant celui-ci également.

</details>

<details>
<summary> Afficher la solution
</summary><br>

Entrez `sudo -i` pour passer à l'utilisateur root.

Entrez `whoami` pour savoir si vous êtes l'utilisateur root :

![step1-1](https://www.freecodecamp.org/news/content/images/2022/04/step1-1.PNG)

Si vous n'avez pas d'accès `root`, utilisez les commandes en ajoutant `sudo`.

</details>

--- 

**Étape 2 : Créer un groupe `dev-team`**

<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `groupadd`.

Syntaxe : `groupadd group-name`

</details>

<details>
<summary> Afficher la solution
</summary><br>

Entrez `groupadd dev-team` pour créer le groupe `dev-team`

Vérifiez : `cat /etc/group | grep dev-team`

</details>

--- 

**Étape 3 : Créer deux nouveaux utilisateurs John et Bob et les ajouter au groupe `dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `useradd`.

`useradd` crée un nouvel utilisateur et l'ajoute au groupe spécifié.

Syntaxe : `useradd -G groupname username`

Où `-G` spécifie le groupe.

</details>

<details>
<summary> Afficher la solution
</summary><br>

`useradd -G dev-team John`

`useradd -G dev-team Bob`

Vérifiez : `cat /etc/group | grep dev-team`

![step3-1](https://www.freecodecamp.org/news/content/images/2022/04/step3-1.PNG)

</details>


--- 

**Étape 4 : Fournir des mots de passe pour les utilisateurs John et Bob**


<details>
<summary> Afficher l'indice
</summary><br>


Utilisez la commande `passwd`

`passwd` crée un mot de passe pour les utilisateurs.

Syntaxe : `passwd username`


</details>

<details>
<summary> Afficher la solution
</summary><br>

`passwd John`

`passwd Bob`

</details>



--- 

**Étape 5 : Créer un répertoire dans /home et le nommer `dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>


Utilisez la commande `mkdir`

`mkdir` crée un répertoire.

Syntaxe : `mkdir directory-name`


</details>

<details>
<summary> Afficher la solution
</summary><br>

`mkdir /home/dev-team`

Vérifiez :

![correction](https://www.freecodecamp.org/news/content/images/2022/04/correction.png)

</details>



--- 


**Étape 6 : Changer la propriété du groupe du dossier `dev-team` pour le groupe `dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `chown`

Syntaxe : `chown :group-name folder`


</details>

<details>
<summary> Afficher la solution
</summary><br>

`chown :dev-team /home/dev-team/`
    
![step6](https://www.freecodecamp.org/news/content/images/2022/04/step6.png)

</details>



--- 

**Étape 7 : Assurez-vous que les permissions du dossier `dev-team` permettent aux membres du groupe de créer et de supprimer des fichiers.**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `chmod`

Les permissions d'écriture permettent aux utilisateurs et aux groupes de créer et de supprimer des fichiers.

Syntaxe : `chmod permissions folder`

</details>

<details>
<summary> Afficher la solution
</summary><br>

`chmod g+w /home/dev-team/`

![step7](https://www.freecodecamp.org/news/content/images/2022/04/step7.png)

</details>




--- 


**Étape 8 : Assurez-vous que les 'autres' n'ont aucun accès aux fichiers du dossier `dev-team`.**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `chmod`

Supprimez les permissions de lecture, d'écriture et d'exécution pour les 'autres' si elles existent.

Syntaxe : `chmod permissions folder`


</details>

<details>
<summary> Afficher la solution
</summary><br>

`chmod o-rx dev-team `

![correction2](https://www.freecodecamp.org/news/content/images/2022/04/correction2.png)



</details>



--- 

**Étape 9 : Quitter la session `root` et passer à `John`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `exit` pour vous déconnecter de l'utilisateur root.

Utilisez `su` pour changer d'utilisateur.

Syntaxe : `su - user`

Pour confirmer l'utilisateur actuel, utilisez la commande `whoami`.

</details>

<details>
<summary> Afficher la solution
</summary><br>

`exit`

`su - John`

Vérifiez avec la commande `whoami`.

</details>



--- 


**Étape 10 : Naviguer vers le dossier : `/home/dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `cd` pour changer de dossier.

Syntaxe : `cd /path/to/folder`

Confirmez le chemin actuel avec `pwd`.

</details>

<details>
<summary> Afficher la solution
</summary><br>

`cd /home/dev-team`

</details>



--- 


**Étape 11 : Créer un fichier vide dans le dossier : `/home/dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `touch` pour créer un fichier vide.

Syntaxe : `touch filename`

</details>

<details>
<summary> Afficher la solution
</summary><br>

`touch john-file.txt`

Vérifiez : `ls -lrt`
  
![john](https://www.freecodecamp.org/news/content/images/2022/04/john.png)
    
</details>







--- 


**Étape 12 : Changer la propriété du groupe du fichier créé pour `dev-team` et vérifier.**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `chown` pour changer la propriété.

Syntaxe : `chown :group file-name`

</details>

<details>
<summary> Afficher la solution
</summary><br>

`chown :dev-team john-file.txt`

Une fois la propriété du groupe modifiée, tous les membres du groupe peuvent accéder à ce fichier.

Vérifiez `ls -lrt`

![step10](https://www.freecodecamp.org/news/content/images/2022/04/step10.PNG)

</details>




--- 


**Étape 13 : Quitter la session et passer à l'utilisateur `Bob`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `exit` pour quitter le terminal.

Utilisez `su` pour changer d'utilisateur.

Syntaxe : `su - user`

Pour confirmer l'utilisateur actuel, utilisez la commande `whoami`.

</details>

<details>
<summary> Afficher la solution
</summary><br>

`exit`

`su - Bob`

Vérifiez l'utilisateur actuel avec la commande `whoami`.



</details>





--- 


**Étape 14 : Naviguer vers le chemin `/home/dev-team`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `cd` pour changer de dossier.

Syntaxe : `cd /path/to/folder`

Confirmez le chemin actuel avec `pwd`.



</details>

<details>
<summary> Afficher la solution
</summary><br>

`cd /home/dev-team`


</details>





--- 


**Étape 15 : Découvrir les privilèges de `Bob` pour accéder à `john-file.txt`**


<details>
<summary> Afficher l'indice
</summary><br>


Utilisez la commande `ls -l` pour une liste détaillée.

Syntaxe : `ls -l | grep file-name`

Le groupe a-t-il les permissions `rw-` ?



</details>

<details>
<summary> Afficher la solution
</summary><br>

`ls -l | grep john-file.txt`

   
![step13](https://www.freecodecamp.org/news/content/images/2022/04/step13.PNG)

</details>



--- 


**Étape 16 : Modifier le fichier `john-file.txt` en étant connecté en tant que `Bob`**


<details>
<summary> Afficher l'indice
</summary><br>

Utilisez la commande `echo` pour ajouter du texte au fichier.

Syntaxe : `echo "Some text" >>file-name`

Cela redirigera le texte cité à la fin du fichier.

</details>

<details>
<summary> Afficher la solution
</summary><br>

`echo "This is Bob's comment" > john-file.txt`

Si toutes les permissions sont correctement définies, `Bob` sera autorisé à éditer et enregistrer ce fichier. Sinon, vous obtiendrez une erreur comme celle-ci : `Permission denied`.

Vérifiez `cat john-file.txt`
 
![bob-comment](https://www.freecodecamp.org/news/content/images/2022/04/bob-comment.png)
    
</details>



--- 



**Étape 17 : Créer un autre groupe `project-manager` et assigner un membre `Fatima` à celui-ci**


<details>
<summary> Afficher l'indice
</summary>

Utilisez la commande `groupadd` pour ajouter un nouveau groupe.

Syntaxe : `groupadd group-name`


Créez un nouvel utilisateur avec la commande `useradd`.
    
Utilisez le flag `-G` pour l'assigner à un groupe.

</details>

<details>
<summary> Afficher la solution
</summary>

```
groupadd project-manager
useradd -G project-manager Fatima
passwd Fatima
```

</details>

--- 


**Étape 18 : Naviguer vers le dossier `/home/dev-team` et vérifier si `Fatima` peut y accéder**


<details>
<summary> Afficher l'indice
</summary>

Utilisez `cd` pour naviguer vers `/home/dev-team`.

</details>

<details>
<summary> Afficher la solution



</summary>

`cd /home/dev-team`.

Nous obtenons cette erreur :

![fatima](https://www.freecodecamp.org/news/content/images/2022/04/fatima.png)

Cela est dû au fait que les `autres` n'ont aucun accès au dossier `dev-team`.

Si nous nous souvenons, voici les droits du dossier `dev-team`.

![recall](https://www.freecodecamp.org/news/content/images/2022/04/recall.png)

</details>

## Conclusion

Les permissions et les propriétés sont des concepts utiles pour renforcer la sécurité sur les systèmes d'exploitation multi-utilisateurs. J'espère que vous avez pu apprendre en profondeur comment changer les permissions et les propriétés.

Quelle est votre chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Merci à [Tom Mondloch](https://twitter.com/moTness) pour son aide avec l'exercice guidé.