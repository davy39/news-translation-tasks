---
title: Comment construire un éditeur de Markdown jouet avec Python et Tkinter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T16:30:21.000Z'
originalURL: https://freecodecamp.org/news/lets-create-a-toy-markdown-editor-with-python-tkinter
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/cover-1.png
tags:
- name: editor
  slug: editor
- name: Python
  slug: python
seo_title: Comment construire un éditeur de Markdown jouet avec Python et Tkinter
seo_desc: "By Palash Bauri\nMarkdown editors are trending these days. Everybody is\
  \ creating a markdown editor, and some of them are innovative while some of them\
  \ are boring. \nAs for myself, however, I have always been a fan of doing things\
  \ which haven't been don..."
---

Par Palash Bauri

Les éditeurs Markdown sont à la mode ces jours-ci. Tout le monde crée un éditeur Markdown, et certains sont innovants tandis que d'autres sont ennuyeux. 

Pour ma part, cependant, j'ai toujours été un fan de faire des choses qui n'ont pas été faites par d'autres. (Je vais expliquer ci-dessous pourquoi les autres développeurs ne veulent pas construire un éditeur Markdown avec Tkinter.)

Si vous êtes déjà familiarisé avec Python et Tkinter, vous pouvez facilement vous lancer dans ce guide.

> Mais si vous commencez tout juste avec Python et/ou Tkinter, vous pouvez consulter ces ressources : 
> **Tutoriels Python :** [Tutoriel Python de FreeCodeCamp](https://www.freecodecamp.org/news/best-python-tutorial/) , [Liste de lecture Python 3 par sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln) , [Python pour débutants de FreeCodeCamp](https://www.youtube.com/watch?v=rfscVS0vtbw) etc. (D'autres peuvent être trouvés à une recherche Google)
> **Tutoriels Tkinter :** [Bases de Tkinter](https://pythonprogramming.net/python-3-tkinter-basics-tutorial/) , [Cours Tkinter de FreeCodeCamp](https://www.youtube.com/watch?v=YXPyB4XeYLA) , [Liste de lecture Tkinter de TheNewBoston](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d) etc. (D'autres peuvent être trouvés à une recherche Google)

Alors, avant de commencer, je veux expliquer pourquoi les gens ne veulent pas construire des éditeurs Markdown avec tkinter. C'est parce qu'il n'y a pas de moyen facile par défaut pour afficher la sortie HTML de l'entrée Markdown. Il n'y a même pas de widget tkinter par défaut pour afficher les données HTML. Vous pouvez simplement écrire/modifier du Markdown, mais il n'y a pas de moyen facile d'afficher la sortie à l'intérieur de votre application.

Mais un jour, alors que je me promenais dans les rues de l'Internet, j'ai trouvé quelque chose d'intéressant : [**tk_html_widgets**](https://github.com/paolo-gurisatti/tk_html_widgets). Il peut afficher la sortie HTML ! 

Mais bien sûr, il avait quelques problèmes : les polices étaient trop petites, et il n'avait pas de support pour attacher des photos distantes. Alors, comme d'habitude, j'ai créé ma propre fourche et j'ai corrigé quelques problèmes et j'ai amélioré la stabilité. Je l'ai nommé [tkhtmlview](https://github.com/bauripalash/tkhtmlview/). ?

Ugh, je pense que je vous ennuie ?, alors arrêtons de parler et commençons à construire.

## ?fe0f Commencer la construction :

Assurez-vous d'abord d'avoir Python 3 et Tkinter installés. Si ce n'est pas le cas, vous pouvez les télécharger ici : 
[python.org/downloads](https://www.python.org/downloads) (Tkinter est déjà inclus avec Python).

Les autres choses dont nous aurons besoin sont **tkhtmlview** et **markdown2**. Vous pouvez les installer en exécutant `pip install tkhtmlview markdown2` ou `pip3 install tkhtmlview markdown2` (si vous avez plusieurs versions de Python).

Maintenant, lancez votre éditeur ou IDE préféré et créez un nouveau fichier (par exemple, `tdown.py` (j'ai nommé l'éditeur _tdown_)).
Nous allons commencer par importer les bibliothèques nécessaires.

```python
from tkinter import *
from tkinter import font , filedialog
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
```
Dans la première ligne, nous importons tout (presque) depuis le package tkinter.

Dans la deuxième ligne, nous importons la police et filedialog. `font` est nécessaire pour styliser (par exemple, police, taille de police) notre champ de saisie, et filedialog est importé pour ouvrir des fichiers Markdown pour l'édition (et/ou pour sauvegarder notre fichier Markdown).

Dans la 3ème ligne, Markdown est importé pour nous aider à convertir notre source Markdown en HTML et à l'afficher dans le champ de sortie en utilisant HTMLLabel (que nous importons à la 4ème ligne).

Après cela, nous allons créer une classe de frame appelée Window qui héritera de la classe **Frame** de tkinter. Elle contiendra nos champs de saisie et de sortie.

```python

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="Helvetica", size=14)
        self.init_window()

    def init_window(self):
        self.master.title("TDOWN")
        self.pack(fill=BOTH, expand=1)

```

Ici, dans ce bloc de code, nous définissons d'abord une classe appelée Window qui hérite de la classe de widget Frame de tkinter. 

Maintenant, dans la fonction d'initialisation, nous prenons master comme argument qui servira de parent au frame. À la ligne suivante, nous initialisons un Frame. 

Ensuite, nous déclarons un objet de police personnalisé appelé `self.myfont` avec la famille de polices **Helvetica** (vous pouvez choisir n'importe quelle famille de polices que vous voulez) et la taille _14_ qui sera utilisée dans notre champ de saisie Markdown. 

Enfin, nous appelons la fonction _init_window_ où nous mettrons le cœur de notre application.

Dans la fonction _init_window_, nous définissons d'abord le titre de la fenêtre comme **TDOWN**. À la ligne suivante `self.pack(fill=BOTH, expand=1)`, nous disons à notre Frame de prendre tout l'espace de notre fenêtre. 

Nous définissons l'argument de mot-clé `fill` à `BOTH` qui est en fait importé de la bibliothèque tkinter. Il dit au frame de remplir la fenêtre à la fois horizontalement et verticalement, et l'argument de mot-clé `expand` est défini à 1 (signifie **True**) qui dit à notre Frame d'être extensible. En termes simples, le Frame remplira la fenêtre peu importe comment nous étirons la taille de la fenêtre ou la maximisons.

Maintenant, si vous exécutez le script `tdown.py`, vous ne verrez rien car nous avons seulement défini la classe mais ne l'avons jamais appelée.

Pour corriger cela, nous allons mettre ceci à la fin de notre script :

```python
root = Tk()
root.geometry("700x600")
app = Window(root)
app.mainloop()
```

Ici, nous créons un objet Tk et le stockons dans la variable root qui servira de racine à notre classe Window. 

Ensuite, nous définissons la géométrie de notre fenêtre à 700x600 - 700 est la hauteur et 600 est la largeur de la fenêtre. À la ligne suivante, vous pouvez voir que nous créons un objet Window. Nous poussons la variable **root** comme _root_ du frame et la stockons dans une variable appelée **app**. 

La prochaine chose que nous faisons est d'appeler simplement la fonction mainloop qui dit à notre application de s'exécuter ! ?

Maintenant, exécutez le script `tdown.py`. Vous verrez une fenêtre vide comme ceci si vous avez tout fait correctement :

![Frame Tkinter vide](https://www.freecodecamp.org/news/content/images/2020/01/blank.png)

Mais ce n'est qu'une fenêtre vide. Pour écrire quelque chose dans la fenêtre, nous devons ajouter un champ de texte où nous écrirons notre Markdown. Pour cela, nous allons utiliser le widget **Text** de tkinter.

```python
...
def init_window(self):
    self.master.title("TDOWN")
    self.pack(fill=BOTH, expand=1)

    self.inputeditor = Text(self, width="1")
    self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
```

> Ne vous laissez pas confondre par les **...** (trois points), je les ai mis là seulement pour signifier qu'il y a plusieurs lignes de code avant ce bloc de code.

Ici, nous créons un widget Text avec une largeur de **1**. Ne vous grattez pas la tête - ici les tailles sont faites en utilisant des ratios. Vous comprendrez cela plus clairement dans les prochaines secondes lorsque nous mettrons la boîte de sortie. ?

Nous l'emballons ensuite dans le Frame et lui disons d'être à la fois étirable horizontalement et verticalement.

Lorsque vous exécutez le script, vous verrez qu'un champ de saisie multiline a pris le contrôle de notre fenêtre. Si vous commencez à écrire dedans, vous remarquerez peut-être que les caractères sont si petits !

![Le champ de saisie a pris le contrôle de toute la fenêtre !](https://www.freecodecamp.org/news/content/images/2020/01/with_small_fonts.png)

Je savais déjà que ce problème allait survenir. C'est pourquoi je vous ai dit plus tôt de créer un objet de police personnalisé (_self.myfont_). Maintenant, si vous faites quelque chose comme ceci :

```python

self.inputeditor = Text(self, width="1" , font=self.myfont)
```

> (Ici, nous disons à notre widget Text d'utiliser notre police personnalisée au lieu de la petite police par défaut !)

...la taille de la police du champ de saisie sera augmentée à 14. Exécutez le script pour vérifier si tout a fonctionné parfaitement.

![La taille de la police a été augmentée à 14](https://www.freecodecamp.org/news/content/images/2020/01/font_size_increased.png)

Maintenant, je pense qu'il est temps d'ajouter la boîte de sortie où nous verrons la sortie HTML de notre source Markdown pendant que nous écrivons.

Pour cela, nous allons ajouter un HTMLLabel, quelque chose comme ceci à l'intérieur de la fonction `init_window` :

```python
self.outputbox = HTMLLabel(self, width="1", background="white", html="<h1>Bienvenue</h1>")
self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
self.outputbox.fit_height()
```
Nous utilisons `HTMLLabel` de *tkhtmlview* avec une largeur de **1** (encore une fois). Nous définissons la largeur à 1 car la fenêtre sera partagée entre le champ de saisie et la boîte de sortie avec un ratio de **1:1** (Vous comprendrez ce que je veux dire lorsque vous exécuterez le script).

L'argument de mot-clé `html` stocke la valeur qui sera affichée la première fois. 

Ensuite, nous l'emballons dans la fenêtre avec `side` comme `RIGHT` pour le mettre du côté droit du champ de saisie. Le `fit_height()` fait en sorte que les textes s'adaptent à l'intérieur du widget (autant que je sache... ?)

Maintenant, exécutez le code.

![Boîte de sortie ajoutée !](https://www.freecodecamp.org/news/content/images/2020/01/no_binding.png)

Maintenant, si vous commencez à écrire dans le champ de saisie, vous pourriez être déçu (mais ne le soyez pas !) de voir que la sortie n'est pas mise à jour au fur et à mesure que nous tapons. C'est parce que nous n'avons pas encore dit à notre programme de le faire.

Pour cela, nous allons d'abord lier un événement avec notre éditeur. Ensuite, chaque fois que le texte est modifié, la sortie sera mise à jour, quelque chose comme ceci :

```python
self.inputeditor.bind("<<Modified>>", self.onInputChange)
```
> Mettez cette ligne à l'intérieur de la fonction init_window().

Donc, en gros, cette ligne dit à `inputeditor` d'appeler la fonction `onInputChange` chaque fois que le texte est modifié. Mais comme nous n'avons pas encore cette fonction, nous devons l'écrire.

```python
...
def onInputChange(self , event):
    self.inputeditor.edit_modified(0)
    md2html = Markdown()
    self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0" , END)))
```    
Dans la première ligne, en utilisant `edit_modified(0)`, nous réinitialisons le drapeau Modified afin qu'il puisse être réutilisé. Sinon, après le premier appel d'événement, il ne fonctionnera plus.

Ensuite, nous créons un objet Markdown nommé md2html. À la dernière ligne, où d'abord nous.... attendez ! La dernière ligne peut être déroutante pour certains lecteurs. Alors laissez-moi la décomposer en trois lignes.

```python
markdownText = self.inputeditor.get("1.0" , END)
html = md2html.convert(markdownText)
self.outputbox.set_html(html)
```
Ici, dans la première ligne, nous récupérons le texte Markdown du haut vers le bas du champ de saisie. Le premier argument, `self.inputeditor.get`, lui dit de commencer à scanner à partir du 0ème caractère de la première ligne (1.0 => [NUMÉRO_DE_LIGNE].[NUMÉRO_DE_CARACTÈRE]), et le dernier argument lui dit d'arrêter de scanner lorsqu'il a atteint la fin.

Ensuite, nous convertissons le texte Markdown scanné en HTML en utilisant la fonction `md2html.convert()` et le stockons dans la variable `html`.

Enfin, nous disons à outputbox d'afficher la sortie en utilisant la fonction `.set_html()` !

Exécutez le script. Vous verrez un éditeur Markdown fonctionnel (presque). Au fur et à mesure que vous tapez dans le champ de saisie, la sortie sera également mise à jour !

Mais... notre travail n'est pas encore terminé. Les utilisateurs doivent pouvoir au moins ouvrir et sauvegarder leur texte.

Pour cela, nous allons ajouter un menu `Fichier` dans la barre de menus. C'est ici que les utilisateurs pourront ouvrir et sauvegarder des fichiers ainsi que quitter l'application.

Dans la fonction `init_window`, nous ajouterons ces lignes :

```python
self.mainmenu = Menu(self)
self.filemenu = Menu(self.mainmenu)
self.filemenu.add_command(label="Ouvrir", command=self.openfile)
self.filemenu.add_command(label="Enregistrer sous", command=self.savefile)
self.filemenu.add_separator()
self.filemenu.add_command(label="Quitter", command=self.quit)
self.mainmenu.add_cascade(label="Fichier", menu=self.filemenu)
self.master.config(menu=self.mainmenu)
```
Je vais faire cela rapidement : 

Ici, nous définissons un nouveau menu avec Frame comme parent. 

Ensuite, nous définissons un autre menu et le menu précédent comme parent. Il servira de menu `Fichier`. 

Puis nous ajoutons 3 sous-menus (Ouvrir, Enregistrer sous, et Quitter) et un séparateur en utilisant les fonctions `add_command()` et `add_separator()`. Le sous-menu **Ouvrir** exécutera la fonction `openfile`, le sous-menu **Enregistrer sous** exécutera la fonction `savefile`, et enfin **Quitter** exécutera une fonction intégrée `quit` qui fermera le programme.

Ensuite, en utilisant la fonction `add_cascade()`, nous disons au premier objet Menu d'inclure la variable `filemenu`. Cela inclut tous nos sous-menus avec l'étiquette `Fichier`. 

Enfin, nous utilisons `self.master.config()` pour dire à notre fenêtre d'utiliser `mainmenu` comme barre de menus de notre fenêtre.

![Menu ajouté](https://www.freecodecamp.org/news/content/images/2020/01/menus.png)

> Cela ressemblera à quelque chose comme ceci, mais ne l'exécutez pas encore. Vous obtiendrez des erreurs disant que les fonctions `openfile` et `savefile` ne sont pas définies.

Comme vous pouvez le voir maintenant, nous devons définir deux fonctions à l'intérieur de la classe Window où nous utiliserons filedialog de tkinter.

D'abord, définissons la fonction pour ouvrir les fichiers :

```python
def openfile(self):
    openfilename = filedialog.askopenfilename(filetypes=(("Fichier Markdown", "*.md , *.mdown , *.markdown"),
                                                                  ("Fichier Texte", "*.txt"), 
                                                                  ("Tous les Fichiers", "*.*")))
    if openfilename:
        try:
            self.inputeditor.delete(1.0, END)
            self.inputeditor.insert(END , open(openfilename).read())
        except:
            print("Impossible d'ouvrir le fichier !")     
```
Ici, nous montrons d'abord à l'utilisateur une boîte de dialogue de navigateur de fichiers qui lui permet de choisir un fichier à ouvrir en utilisant `filedialog.askopenfilename()`. Avec l'argument de mot-clé `filetypes`, nous disons à la boîte de dialogue de n'ouvrir que ces types de fichiers en passant un tuple avec les fichiers pris en charge (basiquement tous les types de fichiers) : 
* Les fichiers Markdown avec les extensions `.md`, `.mdown`, `.markdown`, 
* Les fichiers texte avec l'extension `.txt`, 
* et dans la ligne suivante, en utilisant une extension générique, nous disons à la boîte de dialogue d'ouvrir les fichiers avec n'importe quelle extension. 

Ensuite, nous vérifions si l'utilisateur a sélectionné un fichier ou non. Si oui, nous essayons d'ouvrir le fichier. Ensuite, nous supprimons tout le texte à l'intérieur du champ de saisie à partir du 0ème caractère de la première ligne jusqu'à la FIN du champ. 

Ensuite, nous ouvrons et lisons le contenu du fichier sélectionné et insérons le contenu dans le champ de saisie.

Si notre programme ne peut pas ouvrir un fichier, il imprimera l'erreur. Mais attendez, ce n'est pas une bonne façon de gérer les erreurs. Ce que nous pouvons faire ici, c'est afficher un message d'erreur à l'utilisateur qui ressemble à ceci :

![Affichage d'un message d'erreur](https://www.freecodecamp.org/news/content/images/2020/01/error.png)

Pour cela, nous allons d'abord importer `messagebox` du package tkinter.
```python
from tkinter import messagebox as mbox
```
Ensuite, au lieu d'imprimer simplement un message d'erreur comme nous l'avons fait ci-dessus, nous allons remplacer cette ligne par la ligne ci-dessous pour afficher un message d'erreur approprié à l'utilisateur.

```python

mbox.showerror("Erreur lors de l'ouverture du fichier sélectionné", "Oups !, Le fichier que vous avez sélectionné : {} ne peut pas être ouvert !".format(openfilename))
```
Cela créera un message d'erreur comme la capture d'écran ci-dessus que je vous ai montrée lorsque le fichier ne peut pas être ouvert. 

Dans la fonction `mbox.showerror`, le premier argument est le titre de la boîte de message. Le second est le message à afficher.

Maintenant, nous devons écrire une fonction `savefile` pour sauvegarder notre saisie Markdown.

```python
def savefile(self):
        filedata = self.inputeditor.get("1.0" , END)
        savefilename = filedialog.asksaveasfilename(filetypes = (("Fichier Markdown", "*.md"),
                                                                  ("Fichier Texte", "*.txt")) , title="Enregistrer le fichier Markdown")
        if savefilename:
            try:
                f = open(savefilename , "w")
                f.write(filedata)
            except:
                mbox.showerror("Erreur lors de l'enregistrement du fichier", "Oups !, Le fichier : {} ne peut pas être enregistré !".format(savefilename))

```                
Ici, nous scannons d'abord tout le contenu du champ de saisie et le stockons dans une variable. Ensuite, nous demandons à l'utilisateur le nom du fichier où il veut sauvegarder le contenu en donnant l'option pour deux types de fichiers (.md et .txt).

Si l'utilisateur choisit un nom de fichier, nous essayons de sauvegarder le contenu du champ de saisie stocké dans la variable `filedata`. Si une exception se produit, nous affichons à l'utilisateur un message d'erreur indiquant que le programme n'a pas pu sauvegarder le fichier.

N'oubliez pas de tester votre application pour vérifier les bugs ! Si vous et moi n'avons fait aucune erreur, nos programmes devraient fonctionner parfaitement et ressembler à quelque chose comme ceci : 

![Produit final](https://www.freecodecamp.org/news/content/images/2020/01/complete.png)

> **Le code source complet de cet éditeur Markdown 'tdown' est disponible sur [GitHub](https://github.com/bauripalash/tdown) et également sur [Repl.it](https://repl.it/@bauripalash/tdownlive) où vous pouvez tester l'éditeur sur votre navigateur !**

![Nous l'avons enfin fait !](https://media1.tenor.com/images/86bfdafc0ec6509e13b1c1748564b2e6/tenor.gif?itemid=9101932)

Si vous rencontrez des problèmes en suivant cet article, vous pouvez me le faire savoir dans les commentaires ou m'envoyer un message sur Twitter à [@bauripalash](https://twitter.com/bauripalash).

## Quelques notes :
* Tout d'abord, rappelez-vous que ceci n'est qu'un éditeur jouet. Si vous voulez construire un éditeur plus puissant, vous pouvez utiliser d'autres bibliothèques GUI telles que wxPython, PyQT, Kivy et bien d'autres qui ont au moins un meilleur support HTML ([Liste complète](https://wiki.python.org/moin/GuiProgramming)).

* Dans cet article, je n'ai montré que comment construire un éditeur *basique*. Vous pouvez également ajouter de nombreuses autres fonctionnalités sympas de votre choix, comme exporter en HTML ou PDF, ajouter des boutons pour simplifier l'écriture du Markdown... etc.

* Les modules de rendu HTML tkhtmlview ou tk_html_widgets ne sont pas entièrement stables et ne supportent que certaines fonctionnalités HTML de base, alors n'attendez pas trop.


Alors... J'espère que vous avez apprécié cet article et appris de nouvelles choses. N'oubliez pas de me faire savoir si vous êtes bloqué quelque part ou si vous ne comprenez pas quelque chose. 

Enfin, mais non des moindres, veuillez me faire savoir si j'ai fait des erreurs ci-dessus. Et j'adorerais entendre vos idées ou suggestions via les commentaires ou DM.

Merci. ?