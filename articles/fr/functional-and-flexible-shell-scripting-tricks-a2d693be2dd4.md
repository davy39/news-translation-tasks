---
title: Astuces de script shell fonctionnelles et flexibles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-07T16:15:12.000Z'
originalURL: https://freecodecamp.org/news/functional-and-flexible-shell-scripting-tricks-a2d693be2dd4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ZB2nVJjipU4repVb
tags:
- name: automation
  slug: automation
- name: General Programming
  slug: programming
- name: Scripting
  slug: scripting
- name: shell script
  slug: shell-script
- name: 'tech '
  slug: tech
seo_title: Astuces de script shell fonctionnelles et flexibles
seo_desc: 'By BinHong Lee

  Shell scripts vs python or Perl

  It''s 2020 now, who writes shell scripts anymore? Am I right? Well, apparently I
  do. ¯_(ツ)_/¯

  There are some good arguments for that here and here which mainly revolve around
  2 things:


  Shell exists in al...'
---

Par BinHong Lee

### Scripts shell vs Python ou Perl

Nous sommes en 2020, qui écrit encore des scripts shell ? N'est-ce pas ? Eh bien, apparemment, moi. 🿏_(ツ)_/🿏

Il y a de bons arguments pour cela [ici](https://stackoverflow.com/questions/796319/strengths-of-shell-scripting-compared-to-python#796343) et [ici](https://www.linuxquestions.org/questions/linux-newbie-8/what-is-the-difference-between-perl-and-shell-scripting-4175486499/) qui tournent principalement autour de 2 choses :

1. Le shell existe dans tous les systèmes Unix et utilise les fonctionnalités par défaut du système.
2. Le shell est une « fonction de commande interactive » conçue pour obtenir des entrées utilisateur pendant leur exécution.

De plus, voici une lecture supplémentaire pertinente sur les différences entre `sh` et `bash` [ici](https://stackoverflow.com/questions/5725296/difference-between-sh-and-bash).

### Arguments

Dans certaines occasions, vous devrez passer un argument (ou en attendre un) dans le script, comme vous pourriez passer un paramètre à une fonction. Dans ce cas, vous utiliserez quelque chose comme `$1` pour le premier argument, `$2` pour le second. Voici un exemple de ce à quoi cela pourrait ressembler :

Dans le script `run_this.sh` :

```
echo "Le message d'entrée était $1."
```

Exécution de la commande :

```
./run_this.sh userInputLe message d'entrée était userInput.
```

*Remarque : Les paramètres sont séparés par des espaces, donc si vous souhaitez entrer une chaîne contenant un espace, il faudra peut-être faire quelque chose comme `./run_this.sh "user input"` pour que `"user input"` soit compté comme `$1` entièrement.*

Dans le cas où vous n'êtes pas sûr de la longueur de l'entrée utilisateur et que vous souhaitez tout capturer, vous utiliserez `$@` à la place. Dans l'exemple suivant, j'ai pris toute la chaîne et je l'ai imprimée mot par mot après l'avoir divisée en un tableau de chaînes selon les espaces.

Dans le script `run_this.sh` :

```
userInputs=($@)for i in "${userInputs[@]}"; do  echo "$i"done
```

Exécution de la commande :

```
./run_this.sh who knows how long this can gowhoknowshowlongthiscango
```

### Fonctions

Si vous avez fait de la programmation, vous devriez être familier avec le concept de *fonctions*. C'est essentiellement un ensemble de commandes/opérations que vous allez répéter encore et encore. Au lieu de les répéter plusieurs fois dans votre code, vous pouvez les mettre dans une fonction. Ensuite, il suffit d'appeler la fonction, ce qui réduit effectivement le nombre de lignes de code à écrire.

*Note : Si vous ne le savez pas déjà, le nombre de lignes de code (LOC) est une métrique horrible pour toute sorte de mesure en termes de programmation. Ne me croyez pas sur parole, croyez [Bill Gates](https://www.goodreads.com/quotes/536587-measuring-programming-progress-by-lines-of-code-is-like-measuring) :*

> « Mesurer les progrès de la programmation par le nombre de lignes de code, c'est comme mesurer les progrès de la construction d'un avion par son poids. »

Voici à quoi ressemble une fonction normale :

```
# Déclaration de la fonctiondoSomething() {
```

```
}
```

```
# Appel de la fonctiondoSomething
```

Assez simple et facile à comprendre. Voici quelques différences entre les fonctions dans les scripts shell et un langage de programmation normal.

### Paramètres

Si vous deviez passer un paramètre/utiliser un paramètre dans une fonction en Java, vous devez les déclarer dans la déclaration de la fonction. Ils ressemblent à ceci.

```
public static void main(String[] args) {    doSomething("random String");}
```

```
private static void doSomething (String words) {    System.out.println(words);}
```

Dans le shell, cependant, ils ne nécessitent aucune déclaration de types ou de noms. Chacun d'eux est comme un script séparé qui vit dans le script lui-même. Si vous deviez utiliser un paramètre, passez-le simplement et appelez-le comme vous le feriez si vous preniez une entrée pour ce script au niveau supérieur. Quelque chose comme ceci :

```
doSomething() {    echo $1}
```

```
doSomething "random String"
```

1. Similaire à ci-dessus, si vous voulez tout prendre, vous utiliserez `$@` au lieu de `$1` puisque `$1` n'utiliserait que la première entrée (et `$2` pour la seconde, etc.).
2. Les fonctions doivent être déclarées avant l'endroit où elles sont appelées. (Généralement au début du fichier avant toute opération principale.)

### Retour

Supposons que nous créons un script comme ci-dessous nommé `run_this.sh` :

```
doSomething() {    echo "magic"    return 0}
```

```
output=`doSomething`echo $output
```

Maintenant, exécutons-le et voyons ce qui est assigné à la variable `output`.

```
$ ./run_this.shmagic
```

Remarquez qu'au lieu de `0`, il affiche `magic`. Cela est dû au fait que lorsque vous faites `output=`doSomething``, il assigne le message de sortie à `output` au lieu de la valeur de retour, puisque le message de sortie est la manière dont vous communiquez presque tout dans le script shell.

Alors, quand est-il judicieux d'utiliser l'appel `return` ? Lorsque vous l'utilisez dans le cadre d'une instruction if. Quelque chose comme ceci :

Dans le script `run_this.sh` :

```
doSomething() {    echo "magic"    return 0}
```

```
if doSomething; then    echo "C'est vrai !"fi
```

Exécution de la commande :

```
./run_this.shC'est vrai !
```

Dans ce cas, `return 0` signifie `vrai` tandis que `return 1` signifie `faux` dans un sens `booléen` traditionnel.

### Écho multi-ligne

Il arrive que vous deviez imprimer un message multi-ligne. Il y a plusieurs façons de procéder. La manière la plus simple est d'utiliser `echo` plusieurs fois comme ceci :

```
echo "ligne1"echo "ligne2"echo "ligne3"
```

Cela fonctionne, mais ce n'est probablement pas la manière la plus élégante de procéder. Au lieu de cela, vous pouvez utiliser `cat << EOF`. Quelque chose comme ceci :

```
cat << EOFligne1ligne2ligne3EOF
```

Remarquez qu'il ne doit y avoir rien (y compris des espaces ou des tabulations) avant `EOF`. Si vous voulez le faire dans une instruction `if`, cela devrait ressembler à ceci.

```
if [ "a" == "a" ]; then  cat << EOFligne1ligne2ligne3EOFfi
```

Remarquez que même les messages eux-mêmes sont alignés à gauche. Cela est dû au fait que si vous les laissez avec des tabulations, le message de sortie affiché dans la ligne de commande sera également tabulé. De plus, si `EOF` est tabulé, le shell se plaindra et terminera généralement le script à cet endroit.

### Drapeaux / Options

Vous avez probablement vu certains scripts ou commandes qui permettent d'ajouter des drapeaux (et parfois des arguments pour le drapeau spécifique). Quelque chose comme `git commit -a -m "Some commit message"`.

Voici un exemple rapide de ce à quoi cela ressemble (j'ai essayé d'être aussi complet que possible avec l'exemple.)

Dans le script `run_this.sh` :

```
while getopts ac: opt; do    case $opt in        a)            echo "\"a\" a été exécuté."            ;;        c)            echo "\"c\" a été exécuté avec le paramètre \"$OPTARG\"."            ;;        \?)            echo "Option invalide : -$opt"            exit 1            ;;        :)            echo "l'option -$opt nécessite un argument."            exit 1            ;;    esacdone
```

Exécution de la commande :

```
./run_this.sh
```

```
./run_this.sh -a"a" a été exécuté.
```

```
./run_this.sh -coption -c nécessite un argument.
```

```
./run_this.sh -c abcd"c" a été exécuté avec le paramètre "abcd".
```

```
./run_this.sh -a -c abc"a" a été exécuté."c" a été exécuté avec le paramètre "abc".
```

```
./run_this.sh -xOption invalide : -x
```

Dans l'exemple ci-dessus, les différences entre l'option `-a` et `-c` sont que dans la ligne `getopts`, `c` a un deux-points (`:`) qui le suit, indiquant ainsi au programme de s'attendre à un paramètre pour l'option. Une autre chose à garder à l'esprit est que les options doivent être déclarées de manière alphabétique. Si vous déclarez quelque chose comme `acb`, la déclaration `b` serait ignorée, et l'utilisation du drapeau `-b` conduirait au message d'erreur au lieu du cas `b` dans la condition switch.

Merci d'avoir lu !

### À propos de moi

Je travaille actuellement chez Facebook en tant qu'ingénieur logiciel. Je passe une partie de mon temps libre à expérimenter et à construire de nouvelles choses avec des technologies que je trouve amusantes et intéressantes. Suivez mon voyage d'exploration [ici](https://binhong.me/blog) ou sur [GitHub](https://github.com/binhonglee).

### Références

* [Petit tutoriel getopts](http://wiki.bash-hackers.org/howto/getopts_tutorial)
* [Comment afficher une chaîne multi-ligne en Bash](https://stackoverflow.com/questions/10969953/how-to-output-a-multiline-string-in-bash#10970616)