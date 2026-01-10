---
title: Comment créer votre propre gestionnaire de dotfiles Linux à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T19:16:38.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-dotfiles-manager-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/download--10-.png
tags:
- name: GitHub
  slug: github
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
seo_title: Comment créer votre propre gestionnaire de dotfiles Linux à partir de zéro
seo_desc: "By Bhupesh Varshney\nAs a new linux ? user, you might realize that there\
  \ are a bunch of configuration files present in your system. These special files\
  \ are called \"dotfiles\". \nIn this tutorial we will learn how to make a dotfiles\
  \ manager and create a ..."
---

Par Bhupesh Varshney

En tant que nouvel utilisateur linux ?, vous pourriez réaliser qu'il y a un ensemble de fichiers de configuration présents dans votre système. Ces fichiers spéciaux sont appelés "dotfiles". 

Dans ce tutoriel, nous allons apprendre comment créer un gestionnaire de dotfiles et faire une sauvegarde de ces fichiers sur GitHub.

**Quels sont ces .dotfiles, pourriez-vous demander ? Et pourquoi en avons-nous besoin ?**

Les dotfiles sont généralement associés à des programmes spécifiques installés sur votre système et sont utilisés pour personnaliser ces programmes/logiciels.

Par exemple, si vous avez [zsh](http://zsh.sourceforge.net/FAQ/) comme shell par défaut, vous aurez un fichier `.zshrc` dans votre répertoire HOME.
D'autres exemples incluent :

1. `.vimrc` : ce mauvais garçon est utilisé pour configurer votre éditeur VIM.
2. `.bashrc` : disponible par défaut, utilisé pour changer les paramètres bash.
3. `.bash_aliases` : ce fichier est généralement utilisé pour stocker vos alias de commandes.
4. `.gitconfig` : stocke les configurations liées à Git.
5. `.gitmessage` : Utilisé pour fournir un modèle de message de commit lors de l'utilisation de `git commit`.

Ces **.dotfiles** changent avec le temps à mesure que vous commencez à personnaliser linux selon vos besoins.

Créer une sauvegarde de ces fichiers est nécessaire si, dans certains cas, vous faites une erreur ? et souhaitez revenir à un état stable précédent. C'est là que le VCS (Version Control Software) entre en jeu. 

Ici, nous allons apprendre comment automatiser cette tâche en écrivant un simple script shell et en stockant nos dotfiles sur GitHub.

<figure>
	<img alt="lets do it rock" src="https://media.giphy.com/media/efPA2YD9BFWS30GJ5v/giphy.gif">
	<figcaption>Source : giphy.com</figcaption>
</figure>


## Contenu
* [Premières étapes, Visualisation du script](#heading-installation)
* [Obtenir les dépendances](#heading-obtenir-les-dependances)
* [Commencer à coder, Module par Module](#heading-commencer-a-coder)
* [Embellir notre script](#heading-embellir-notre-script)
* [Le résultat final](#heading-le-resultat-final)
* [Résumé, Points clés](#heading-resume)


## Premières étapes

Oh, avant d'aller plus loin, nommons notre script : **dotman**, (dot)file (man)ager.
Aimez-vous cela ? ?

Avant d'écrire notre première ligne de code, nous devons définir nos exigences et la conception de la manière dont notre script shell doit fonctionner.

### Nos exigences

Nous allons rendre dotman simple et facile à utiliser. Il doit être capable de :

1. _Trouver les dotfiles présents dans notre système ?._
2. _Différencier les fichiers présents dans notre dépôt git de ceux sur notre système._
3. _Mettre à jour notre dépôt de dotfiles (soit en poussant vers le dépôt distant, soit en tirant depuis celui-ci)._
4. _Être facile à utiliser (nous ne voulons pas 5 arguments différents dans un seul script)._

### Visualisons
<!---Insérer le diagramme ici -->

![dotman-flowchart](https://drive.google.com/uc?export=view&id=1TQgnRGEcpMF4VKYI8aEIJv9sD6XvWOwv)

## Obtenir les dépendances

1. `Git`
Nous avons besoin de Git, car nous pourrions vouloir revenir à une version précédente de notre dotfile. De plus, nous allons stocker nos dotfiles dans un hôte VCS (GitHub/GitLab/Bitbucket/Gittea).
Vous n'avez pas Git installé ? Consultez le [guide suivant](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) pour apprendre comment l'installer selon votre système.

2. `Bash`
Cela sera disponible par défaut sur vos machines Linux/Unix/MacOS.
Vérifiez cela en vérifiant la version `bash --version`.
Cela devrait ressembler à ceci. Ne vous inquiétez pas trop de la version, car notre script fonctionnera bien pour Bash >=3.

  ```bash
  GNU bash, version 4.4.20(1)-release (i686-pc-linux-gnu)
  Copyright (C) 2016 Free Software Foundation, Inc.
  License GPLv3+: GNU GPL version 3 ou ultérieure <http://gnu.org/licenses/gpl.html>

  Ce logiciel est libre ; vous êtes libre de le changer et de le redistribuer.
  Il n'y a AUCUNE GARANTIE, dans la mesure permise par la loi.
  ```


## Commencer à coder

Alors maintenant nous avons tout configuré. Lancez votre éditeur/IDE préféré.

<figure>
	<img alt="coder chimpanzee" src="https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif">
	<figcaption>Source : giphy.com</figcaption>
</figure>

Nous devons déclarer un [she bang](https://en.wikipedia.org/wiki/Shebang_(Unix)) pour indiquer que nous allons invoquer un interpréteur pour l'exécution.
Au début du script, incluez cette ligne :

```bash
#!/usr/bin/env bash

```

La commande (programme) `env` est exécutée comme un nouveau processus qui appelle ensuite la commande fournie comme argument. 

Dans notre cas, `bash` est automatiquement démarré par le processus env. C'est sa responsabilité de `env` de trouver où se trouve `bash` sur notre système et de substituer son chemin dans le script.
Vous pourriez remplacer `bash` par, par exemple, `python` ou `ruby`.

Maintenant, changez simplement les permissions du fichier pour rendre notre script exécutable.
```bash
chmod +x dotman.sh
```

Nous allons utiliser le style de programmation fonctionnelle dans ce script, c'est-à-dire que chaque partie de la tâche sera à l'intérieur d'une certaine _fonction()_.
Suivons le diagramme que nous avons visualisé ci-dessus et écrivons notre première fonction, `init_check()`.

Nous allons nous baser uniquement sur 2 entrées de l'utilisateur :
1. `DOT_DEST` : l'emplacement du dépôt dans votre système local.
2. `DOT_REPO` : l'URL du dépôt distant des dotfiles.

Ces 2 variables doivent être présentes dans votre configuration de shell par défaut (par exemple `.bashrc`). Nous apprendrons comment faire cela plus tard dans ce tutoriel.

```bash
init_check() {
	# Vérifier si c'est une première utilisation ou non
	if [[ -z ${DOT_REPO} && -z ${DOT_DEST} ]]; then
	    # montrer le menu de configuration initiale
		# initial_setup
	else
		# repo_check
	    # manage
	fi
}
```

L'option `-z` est utilisée pour vérifier si une variable est définie ou non (c'est-à-dire si elle est disponible pour notre script ou non). Si elle ne l'est pas, alors nous allons invoquer notre fonction `initial_setup()`. Sinon, nous vérifierons si le dépôt est cloné et est présent dans le dossier `DOT_DEST`.

Maintenant, codons la fonction `initial_setup` :

```bash
initial_setup() {
	echo -e "\n\nPremière utilisation, Configuration de d\u25cbtman"
	echo -e "....................................\n"
	read -p "Entrez l'URL du dépôt de dotfiles : " -r DOT_REPO

	read -p "Où dois-je cloner $(basename "${DOT_REPO}") (${HOME}/..): " -r DOT_DEST
	DOT_DEST=${DOT_DEST:-$HOME}
	if [[ -d "$HOME/$DOT_DEST" ]]; then
		# cloner le dépôt dans le répertoire de destination
		if git -C "${HOME}/${DOT_DEST}" clone "${DOT_REPO}"; then
			add_env "$DOT_REPO" "$DOT_DEST"
			echo -e "\ndotman configuré avec succès"
			goodbye
		else
			# arguments invalides pour quitter, Dépôt Non Trouvé
			echo -e "\n$DOT_REPO Indisponible. Quitter"
			exit 1
		fi
	else
		echo -e "\n$DOT_DEST N'est pas un répertoire valide"
		exit 1
	fi
}
```

Assez basique, n'est-ce pas ? Maintenant, passons cela ensemble et comprenons ce qui se passe.

- L'instruction `read` est une commande shell intégrée utilisée pour prendre une entrée depuis le terminal. L'option `-p` spécifie une invite avant de prendre une entrée. 
- La ligne suivante après read est appelée [Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html). Si l'utilisateur ne saisit pas DOT_DEST, alors la valeur par défaut est assignée comme `/home/username/` (Si DOT_DEST n'est pas défini ou est nul, l'expansion de $HOME est substituée). Sinon, la valeur saisie par l'utilisateur est substituée.
- Le `-d` à l'intérieur de l'instruction if vérifie si le répertoire existe (ou techniquement) si le répertoire fourni par l'utilisateur est effectivement un chemin valide dans notre système ou non.
- L'option `-C` est utilisée dans git pour cloner le dépôt vers un chemin spécifié par l'utilisateur.

Maintenant, voyons comment exporter des variables d'environnement dans la fonction `add_env()`.

```bash
add_env() {
	# exporter des variables d'environnement
	echo -e "\nExportation des variables d'environnement DOT_DEST & DOT_REPO ..."

	current_shell=$(basename "$SHELL")
	if [[ $current_shell == "zsh" ]]; then
		echo "export DOT_REPO=$1" >> "$HOME"/.zshrc
		echo "export DOT_DEST=$2" >> "$HOME"/.zshrc
	elif [[ $current_shell == "bash" ]]; then
		# supposer que nous avons un repli vers bash
		echo "export DOT_REPO=$1" >> "$HOME"/.bashrc
		echo "export DOT_DEST=$2" >> "$HOME"/.bashrc
	else
		echo "Impossible d'exporter DOT_REPO et DOT_DEST."
		echo "Envisagez de les exporter manuellement".
		exit 1
	fi
	echo -e "Configuration pour SHELL : $current_shell a été mise à jour."
}
```

Exécuter `echo $SHELL` dans votre terminal vous donnera le chemin de votre shell par défaut.
La commande `basename` est utilisée pour imprimer le "Nom" de notre SHELL (c'est-à-dire le nom réel sans aucun / initial).

```bash
> echo $SHELL
/usr/bin/zsh
> basename $SHELL
zsh
```

- L'export est une instruction bien utilisée : elle vous permet d'exporter :) des variables d'environnement.
- `>>` est appelé un opérateur de redirection, c'est-à-dire que la sortie de l'instruction **echo "export DOT_DEST=$2"** est dirigée (ajoutée) à la fin du fichier `zshrc`.


Maintenant, une fois que l'utilisateur a terminé la configuration initiale, nous devons lui montrer les options de "gestion".

![manage-menu-flowchart](https://drive.google.com/uc?export=view&id=1TJC7-umrI6JuNAZHFVzGawFz9FQGvBq3)

```bash
manage() {
	while :
	do
		echo -e "\n[1] Montrer les différences"
		echo -e "\n[2] Pousser les dotfiles modifiés vers le dépôt distant"
		echo -e "\n[3] Tirer les dernières modifications depuis le dépôt distant"
		echo -e "\n[4] Lister tous les dotfiles"
		echo -e "\n[q/Q] Quitter la session"
		# Le choix par défaut est [1]
		read -p "Que voulez-vous que je fasse ? [1]: " -n 1 -r USER_INPUT
		# Voir Parameter Expansion
		USER_INPUT=${USER_INPUT:-1}
		case $USER_INPUT in
			[1]* ) show_diff_check;;
			[2]* ) dot_push;;
			[3]* ) dot_pull;;
			[4]* ) find_dotfiles;;
			[q/Q]* ) exit;;
			* )     printf "\n%s\n" "Entrée invalide, essayez à nouveau";;
		esac
	done
}
```

- Vous êtes déjà familier avec `read`. L'option `-n 1` spécifie la longueur de l'entrée autorisée, dans notre cas l'utilisateur ne peut entrer qu'un seul caractère parmi 1, 2, 3, 4, q et Q.

Maintenant, nous devons trouver tous les dotfiles dans notre répertoire HOME.

```bash
find_dotfiles() {
	printf "\n"
	readarray -t dotfiles < <( find "${HOME}" -maxdepth 1 -name ".*" -type f )
	printf '%s\n' "${dotfiles[@]}"
}
```

La fonction est divisée en 2 parties :
1. `find`
La commande find, comme vous l'avez deviné, recherche des fichiers et des répertoires dans notre système. Comprenons-la partie par partie.
- L'option `-type f` spécifie que nous voulons uniquement rechercher des fichiers réguliers et non des répertoires, des fichiers de caractères ou de blocs, ou des fichiers de périphériques.
- L'option `-maxdepth` indique à find de descendre au plus 1 niveau (un entier non négatif) de répertoires en dessous des points de départ. Vous pourriez rechercher des sous-répertoires en remplaçant 1 par 2, 3, etc.
- `-name` prend un motif (glob) pour la recherche. Par exemple, vous pouvez rechercher tous les fichiers `.py` : `-name ".py"`.

2. `readarray` (également un synonyme de `mapfile`)
lire les lignes de l'entrée standard dans la variable de tableau indexé `dotfiles`.
L'option `-t` supprime tout délimiteur de fin (par défaut nouvelle ligne) de chaque ligne lue.

> Note : Si vous avez une ancienne version de Bash (<4), `readarray` pourrait ne pas être présent comme une commande intégrée. Nous pouvons obtenir la même fonctionnalité en utilisant une boucle `while` à la place.

```bash
while read -r value; do
    dotfiles+=($value)
done < <( find "${HOME}" -maxdepth 1 -name ".*" -type f )
```


Nous allons maintenant créer l'une des fonctions les plus importantes de notre script, `diff_check`.

```bash
diff_check() {

	if [[ -z $1 ]]; then
		declare -ag file_arr
	fi

	# dotfiles dans le dépôt
	readarray -t dotfiles_repo < <( find "${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")" -maxdepth 1 -name ".*" -type f )

	# vérifier la longueur ici ?
	for (( i=0; i<"${#dotfiles_repo[@]}"; i++))
	do
		dotfile_name=$(basename "${dotfiles_repo[$i]}")
		# comparer la version HOME du dotfile avec celle du dépôt
		diff=$(diff -u --suppress-common-lines --color=always "${dotfiles_repo[$i]}" "${HOME}/${dotfile_name}")
		if [[ $diff != "" ]]; then
			if [[ $1 == "show" ]]; then
				printf "\n\n%s" "Exécution de diff entre ${HOME}/${dotfile_name} et "
				printf "%s\n" "${dotfiles_repo[$i]}"
				printf "%s\n\n" "$diff"
			fi
			file_arr+=("${dotfile_name}")
		fi
	done
	if [[ ${#file_arr} == 0 ]]; then
		echo -e "\n\nAucun changement dans les dotfiles."
		return
	fi
}

show_diff_check() {
	diff_check "show"
}
```

Notre objectif ici est de trouver les dotfiles déjà présents dans le dépôt et de les comparer avec ceux disponibles dans notre répertoire HOME.

- Le mot-clé `declare` nous permet de créer des variables. L'option `-a` est utilisée pour créer des tableaux et `-g` indique à declare de rendre les variables disponibles "globalement" dans le script.
- `${#file_arr}` nous donne la longueur du tableau.

La commande suivante importante est `diff` qui est utilisée pour comparer les fichiers ligne par ligne. Par exemple :
```bash
> echo -e "abc\ndef\nghi" >> fileA.txt
> echo -e "abc\nlmn\nghi" >> fileB.txt
> cat fileA.txt
abc
def
ghi
> cat fileB.txt
abc
lmn
ghi
> diff -u fileA.txt fileB.txt
--- fileA.txt	2020-07-17 16:24:16.138172662 +0530
+++ fileB.txt	2020-07-17 16:24:26.686075270 +0530
@@ -1,3 +1,3 @@
 abc
-def
+lmn
 ghi
```

La fonction `dot_push()`.

```bash
dot_push() {
	diff_check
	echo -e "\nLes dotfiles suivants ont changé : "
	for file in "${file_arr[@]}"; do
		echo "$file"
		cp "${HOME}/$file" "${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	done

	dot_repo="${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	git -C "$dot_repo" add -A
	
	echo -e "Entrez le message de commit (Ctrl + d pour sauvegarder) :"
	commit=$(</dev/stdin)

	git -C "$dot_repo" commit -m "$commit"
	
	# Exécuter Git Push
	git -C "$dot_repo" push
}
```

Nous écrasons les fichiers ici en les copiant dans notre dépôt de dotfiles en utilisant la commande `cp`.

Et enfin la fonction `dot_pull()` :

```bash
dot_pull() {
	# tirer les changements (s'il y en a) depuis le dépôt hôte
	echo -e "\nTirer les dotfiles ..."
	dot_repo="${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	echo -e "\nTirer les changements dans $dot_repo\n"
	git -C "$dot_repo" pull origin master
}
```

## Embellir notre script

Jusqu'à présent, nous avons réalisé ce que nous avions initialement visualisé.
Mais vous savez quoi, quelque chose manque ....... ?

**Couleurs**

<figure>
	<img alt="Colorful cat rainbow waves" src="https://media1.tenor.com/images/83bc087deefaf265255b9a6196915e8a/tenor.gif">
	<figcaption>Source : tenor.com</figcaption>
</figure>

Il y a beaucoup de façons de faire cela, mais la plus populaire est d'utiliser des [séquences d'échappement](https://wiki.bash-hackers.org/scripting/terminalcodes). Mais nous allons utiliser un outil appelé `tput` qui est une interface conviviale pour afficher des couleurs selon le terminal de l'utilisateur. Il est disponible par défaut dans Linux/MacOS.
Voici une courte démonstration.

Pour imprimer du texte en **gras**
```bash
echo "$(tput bold)This$(tput sgr0) word is bold"
```
Pour changer la couleur de fond.
```bash
echo "$(tput setab 10)This text has green background$(tput sgr0)"
```
Pour changer la couleur du texte
```bash
echo "$(tput setaf 10)This text has blue color$(tput sgr0)"
```
Vous pouvez également combiner des attributs.
```bash
echo "$(tput smul)$(tput setaf 10) This text is underlined & green $(tput rmul)$(tput sgr0)"
```

Je vous laisse cette tâche : ajoutez vos couleurs préférées dans le script.
Lisez ce [guide](http://linuxcommand.org/lc3_adv_tput.php) pour en apprendre et explorer davantage sur tput.

## Le résultat final

J'espère que vous êtes toujours avec moi à ce stade. Mais c'est la fin :( et nous avons maintenant un joli gestionnaire de dotfiles.

<figure>
	<img alt="Happy and excited kermit" src="https://media.giphy.com/media/DYH297XiCS2Ck/giphy.gif">
	<figcaption>Source : giphy.com</figcaption>
</figure>

Maintenant, exécutez simplement le script (si vous ne l'avez pas déjà fait) pour le voir en action.

```bash
./dotman.sh
```

Vous pouvez voir ma version de [**dotman**](https://github.com/Bhupesh-V/dotman/blob/master/dotman.sh) si vous avez besoin d'une référence. N'hésitez pas à créer des problèmes si vous avez des questions sur ce tutoriel ou à me les [envoyer par email](mailto:varshneybhupesh@gmail.com) directement.

[![Bhupesh-V/dotman - GitHub](https://gh-card.dev/repos/Bhupesh-V/dotman.svg?fullname=)](https://github.com/Bhupesh-V/dotman)

Je l'ai rendu disponible en tant que modèle afin que vous puissiez l'utiliser pour créer votre propre version de dotman.

## Résumé

Récapitulons quelques points importants que nous avons appris dans ce tutoriel.

1. Utilisez `basename /chemin/vers/dossier/fichier/` pour obtenir le nom du fichier à partir d'un chemin.
2. Utilisez `git -C /chemin/vers/cloner/cloner https://repo.url` pour cloner le dépôt dans un répertoire différent du répertoire de travail actuel.
3. `echo $SHELL` peut être utilisé pour déterminer quel est votre shell par défaut.
4. Utilisez `find` pour rechercher des fichiers et des dossiers dans votre système Linux.
5. La commande `diff` est utilisée pour comparer 2 fichiers. Similaire à `git diff`.
6. Les tableaux déclarés à l'intérieur d'une fonction ne sont accessibles qu'à l'intérieur de cette fonction. Utilisez l'option `-g` pour les rendre globaux, par exemple `declare -ag file_arr`.
7. `tput` peut être utilisé pour afficher du texte colorisé sur le terminal.

Si vous avez aimé ce tutoriel, vous pouvez lire plus de mes articles sur [mon blog](https://bhupesh-v.github.io). Vous pouvez également me suivre sur [Twitter](https://twitter.com/bhupeshimself).

Bonne apprentissage ?