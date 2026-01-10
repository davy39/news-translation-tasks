---
title: Comment exécuter des programmes R directement dans Jupyter Notebook en local
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-10-03T19:12:33.632Z'
originalURL: https://freecodecamp.org/news/how-to-run-r-programs-directly-in-jupyter-notebook-locally
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/pUAM5hPaCRI/upload/d8014cab22d10f9bade9077d0d4af34b.jpeg
tags:
- name: R
  slug: r-cjxu2ot2i000u7os1rdapoiqi
- name: R Language
  slug: r
- name: 'Jupyter Notebook '
  slug: jupyter-notebook
- name: jupyterhub
  slug: jupyterhub
- name: jupyter
  slug: jupyter
- name: Miniconda
  slug: miniconda
- name: anaconda
  slug: anaconda
seo_title: Comment exécuter des programmes R directement dans Jupyter Notebook en
  local
seo_desc: 'R is a popular programming language that’s now widely used in research-related
  fields like Bioinformatics.

  And to use R, you’ll need to install the R Compiler and R Studio. But did you know
  that you can also directly run your R code right in a Jupyte...'
---

R est un langage de programmation populaire qui est désormais largement utilisé dans des domaines liés à la recherche comme la bioinformatique.

Et pour utiliser R, vous devrez installer le compilateur R et R Studio. Mais saviez-vous que vous pouvez également exécuter directement votre code R dans un Jupyter Notebook ? Cela aide de nombreuses façons si vous êtes déjà habitué à utiliser Jupyter Notebook pour des tâches liées à l'apprentissage automatique en utilisant Python.

Dans ce tutoriel, je vais vous montrer exactement comment configurer votre machine locale pour exécuter le langage de programmation R directement dans Jupyter Notebook. Les processus que je vais vous montrer aujourd'hui sont également applicables à tous les principaux systèmes d'exploitation (Windows, MacOS et Linux).

## Table des matières

* [Installer Conda](#heading-installer-conda)
    
* [Créer un nouvel environnement](#heading-creer-un-nouvel-environnement)
    
* [Activer votre environnement Conda](#heading-activer-votre-environnement-conda)
    
* [Installer ipykernel et jupyter](#heading-installer-ipykernel-et-jupyter)
    
* [Installer R dans l'environnement Conda](#heading-installer-r-dans-lenvironnement-conda)
    
* [Ouvrir le Jupyter Notebook](#heading-ouvrir-le-jupyter-notebook)
    
* [Exécuter R dans Jupyter Notebook](#heading-executer-r-dans-jupyter-notebook)
    
* [Conclusion](#heading-conclusion)
    

## Installer Conda

Vous utilisez normalement Conda pour gérer plusieurs environnements en Python. Et ici, nous allons utiliser le même programme Conda pour installer R dans notre environnement. Vous pouvez utiliser soit [Anaconda](https://www.anaconda.com/) soit [Miniconda](https://docs.anaconda.com/miniconda/).

Je préfère Miniconda car il est si léger. Vous aurez également l'opportunité d'installer les derniers packages directement en utilisant Miniconda. Mais vous pouvez simplement opter pour Anaconda si vous êtes déjà à l'aise avec cela.

## Créer un nouvel environnement

Beaucoup de gens ont tendance à utiliser l'environnement de base. Mais je n'aime jamais utiliser l'environnement de base directement car vous avez généralement besoin de plusieurs environnements pour gérer différentes versions de packages.

Je vais donc créer un nouvel environnement où je travaillerai sur mes tâches liées au langage de programmation R en utilisant Jupyter Notebook.

Pour créer un nouvel environnement Conda, utilisez simplement la commande suivante :

```bash
conda create --name r-conda
```

Ici, `r-conda` est le nom de mon environnement Conda. Vous pouvez choisir un autre nom, mais gardez à l'esprit que le nom de l'environnement conda ne peut pas contenir d'espaces.

Cela créera un nouvel environnement Conda nommé `r-conda` pour moi.

## Activer votre environnement Conda

Si vous souhaitez travailler sur un environnement conda séparé, vous devrez vous assurer d'activer cet environnement conda spécifique avant de commencer à faire quoi que ce soit.

Je veux travailler sur l'environnement conda `r-conda`. Je peux donc simplement activer l'environnement conda en utilisant la commande suivante :

```bash
conda activate r-conda
```

Vous devez utiliser le nom exact de l'environnement conda que vous souhaitez si celui-ci est différent de `r-conda` dans la commande.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Gardez à l'esprit que vous devez activer l'environnement conda avec succès avant de continuer.</div>
</div>

Vous verrez le nom de l'environnement conda sous la forme `(nom-env-conda)` sur le côté gauche de votre terminal.

![activer l'environnement conda](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898007890/f8bf9ced-6c9e-4198-9116-63a32e7d0f03.png align="center")

## Installer `ipykernel` et `jupyter`

J'aime toujours installer `ipykernel` et `jupyter` dans tous mes environnements conda car ils aident à gérer les notebooks/labs Jupyter des différents environnements conda séparément.

Je vais donc les installer ensemble dans mon environnement conda en utilisant la commande ci-dessous :

```bash
conda install ipykernel jupyter
```

Cela installera à la fois `ipykernel` et `jupyter` dans l'environnement conda activé.

## Installer R dans l'environnement Conda

Pour installer R directement dans l'environnement conda, utilisez simplement la commande suivante :

```bash
conda install -c r r-irkernel
```

Cela installera les composants nécessaires qui permettent à votre ordinateur local d'exécuter le programme R dans votre Jupyter Notebook.

## Ouvrir le Jupyter Notebook

Maintenant, vous pouvez ouvrir le Jupyter Notebook soit en utilisant `jupyter notebook` soit `jupyter notebook --ip=0.0.0.0 --port=8889 --no-browser --allow-root --NotebookApp.token=''`. Assurez-vous simplement de modifier l'IP, le port, la configuration root et le token comme vous le jugez approprié pour votre travail.

Ouvrez le lien donné dans le terminal pour ouvrir Jupyter Notebook dans votre navigateur web.

![Ouvrir Jupyter Notebook](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898291254/b932284e-05af-4eec-a6aa-f6b9ad50dd1c.png align="center")

## Exécuter R dans Jupyter Notebook

Après avoir ouvert Jupyter Notebook dans votre navigateur web, lorsque vous souhaitez créer un nouveau notebook pour R, vous obtiendrez `R` directement dans le menu "Nouveau" comme l'image donnée ci-dessous.

![R dans le notebook](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898368089/a2d22b41-8ddd-480b-aaa4-65aeafb12f69.png align="center")

Maintenant, vous pouvez utiliser le langage R directement dans votre Jupyter Notebook !

![Exécuter "R" dans Jupyter Notebook](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898457072/05015331-742c-49c5-9325-b1d1cb1fc6cd.png align="center")

Vous pouvez également voir le logo du langage de programmation R en haut à droite de votre Notebook.

## Conclusion

Merci d'avoir lu l'article entier. J'espère que vous avez appris quelque chose de nouveau ici.

Si vous avez apprécié les procédures étape par étape, n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/). Je vous serais reconnaissant si vous pouviez m'endosser pour certaines compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/fahimfba/). Je vous recommande également de vous abonner à ma [chaîne YouTube](https://youtube.com/@FahimAmin) pour du contenu régulier lié à la programmation.

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de consulter [mon site web](https://fahimbinamin.com/) également.

Merci beaucoup ! 😀