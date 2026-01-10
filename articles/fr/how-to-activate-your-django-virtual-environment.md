---
title: Comment activer votre environnement virtuel Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-07-16T16:58:44.334Z'
originalURL: https://freecodecamp.org/news/how-to-activate-your-django-virtual-environment
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746123776834/337004ca-692e-4df9-89db-81e78a16c7fe.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: virtualization
  slug: virtualization
seo_title: Comment activer votre environnement virtuel Django
seo_desc: If you’re starting with Django, one of the first steps you’ll hear about
  is activating a virtual environment. And if that sounds a little technical, don’t
  worry – I’m going to walk you through exactly what that means, why it matters, and
  how to do it...
---

Si vous commencez avec Django, l'une des premières étapes dont vous entendrez parler est *l'activation d'un environnement virtuel*. Et si cela semble un peu technique, ne vous inquiétez pas – je vais vous guider à travers ce que cela signifie, pourquoi c'est important et comment le faire étape par étape, sans termes confus.

J'ai aidé beaucoup de gens à commencer avec Python et Django, et croyez-moi : comprendre les environnements virtuels dès le début peut vous éviter beaucoup de maux de tête plus tard.

Un environnement virtuel peut vous aider à garder vos projets Django organisés. Il évite également les conflits entre différentes versions de packages et vous donne un moyen plus propre de gérer vos outils de développement.

À la fin de ce guide, vous saurez non seulement comment activer votre environnement virtuel, mais aussi pourquoi vous devriez le faire.

Commençons.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'un environnement virtuel en Python ?](#heading-qu-est-ce-qu-un-environnement-virtuel-en-python)
    
2. [Pourquoi utiliser un environnement virtuel ?](#heading-pourquoi-utiliser-un-environnement-virtuel)
    
3. [Comment configurer et activer un environnement virtuel Django](#heading-comment-configurer-et-activer-un-environnement-virtuel-django)
    
    * [1\. Installer Python (si ce n'est pas déjà fait)](#heading-1-installer-python-si-ce-n-est-pas-deja-fait)
        
    * [2\. Installer virtualenv (optionnel mais utile)](#heading-2-installer-virtualenv-optionnel-mais-utile)
        
    * [3\. Créer un environnement virtuel](#heading-3-creer-un-environnement-virtuel)
        
    * [4\. Activer l'environnement virtuel](#heading-4-activer-l-environnement-virtuel)
        
4. [Que pouvez-vous faire après l'avoir activé ?](#heading-que-pouvez-vous-faire-apres-l-avoit-activer)
    
5. [Comment désactiver l'environnement virtuel](#heading-comment-desactiver-l-environnement-virtuel)
    
6. [FAQ](#heading-faq)
    
    * [Dois-je activer l'environnement à chaque fois ?](#heading-dois-je-activer-l-environnement-a-chaque-fois)
        
    * [Que faire si activate ne fonctionne pas ?](#heading-que-faire-si-activate-ne-fonctionne-pas)
        
    * [Puis-je utiliser VS Code ou un autre éditeur avec cela ?](#heading-puis-je-utiliser-vs-code-ou-un-autre-editeur-avec-cela)
        
7. [Conseils bonus](#heading-conseils-bonus)
    
    * [Ajouter un fichier .gitignore](#heading-ajouter-un-fichier-gitignore)
        
    * [Utiliser requirements.txt](#heading-utiliser-requirementstxt)
        
8. [Ressources utiles](#heading-ressources-utiles)
    
9. [Conclusion](#heading-conclusion)
    
10. [Apprentissage supplémentaire](#heading-apprentissage-supplementaire)
    

## Qu'est-ce qu'un environnement virtuel en Python ?

Un environnement virtuel est comme un espace de travail privé pour votre projet. Au lieu d'installer des packages (comme Django) globalement pour tout votre ordinateur, vous les installez dans cette petite bulle. Ainsi, différents projets ne se mélangent pas.

Imaginez que vous travaillez sur deux projets Django : l'un nécessite Django 3.2 et l'autre Django 4.1. Sans environnement virtuel, vous auriez des conflits de versions. Mais avec des environnements virtuels, chaque projet reste séparé et propre.

## Pourquoi utiliser un environnement virtuel ?

Voici pourquoi j'utilise *toujours* un environnement virtuel lorsque je travaille avec Django :

* Garde les dépendances de votre projet isolées.
    
* Évite les conflits de versions entre différents projets.
    
* Facilite la gestion et la désinstallation des packages.
    
* Plus important encore, **Django l'attend**, surtout si vous voulez suivre les meilleures pratiques.
    

## Comment configurer et activer un environnement virtuel Django

Parcourons le processus du début à la fin.

### 1\. **Installer Python (si ce n'est pas déjà fait)**

Vous avez besoin de Python 3.8 ou plus récent. Vous pouvez vérifier la version que vous avez en ouvrant votre terminal et en tapant :

```bash
python --version
```

Si vous voyez quelque chose comme `Python 3.11.7`, vous êtes prêt.

Si vous n'avez pas Python, téléchargez-le ici :

👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Assurez-vous de cocher la case **"Ajouter Python à PATH"** pendant l'installation si vous êtes sous Windows.

### 2\. Installer `virtualenv` (optionnel mais utile à connaître)

Python inclut un outil intégré appelé `venv`, et c'est ce que nous utiliserons dans ce tutoriel.

Cependant, certains développeurs préfèrent `virtualenv` car :

* Il fonctionne avec des versions plus anciennes de Python
    
* Il peut être légèrement plus rapide dans les environnements plus grands
    
* Il offre une certaine flexibilité supplémentaire
    

Pour installer `virtualenv`, exécutez simplement :

```bash
pip install virtualenv
```

**Note :** Vous n'avez pas besoin de `virtualenv` pour ce tutoriel, mais c'est bon à savoir. Nous utiliserons le `venv` intégré de Python pour la suite.

### 3\. **Créer un environnement virtuel**

Maintenant, allez dans votre dossier de projet Django (ou créez-en un) :

```bash
mkdir mon_projet_django
cd mon_projet_django
```

Puis exécutez :

```bash
python -m venv venv
```

* `python -m venv` utilise le module d'environnement virtuel intégré de Python
    
* `venv` est le nom du dossier qui stockera votre environnement (vous pouvez l'appeler comme vous voulez)
    

Cela crée un dossier appelé `venv/` dans votre répertoire de projet. Ce dossier contient tout ce dont votre environnement virtuel a besoin.

### 4\. **Activer l'environnement virtuel**

Voici la partie que tout le monde demande.

L'activation dépend de votre système d'exploitation.

#### Sur **Windows (CMD)** :

```bash
venv\Scripts\activate
```

#### Sur **Windows (PowerShell)** :

```bash
.\venv\Scripts\Activate.ps1
```

#### Sur **Mac ou Linux** :

```bash
source venv/bin/activate
```

Après l'avoir activé, votre prompt de terminal changera. Il ressemblera à quelque chose comme ceci :

```bash
(venv) nom-de-votre-ordinateur:mon_projet_django nom-d-utilisateur$
```

Ce `(venv)` au début signifie que l'environnement virtuel est actif.

## Que pouvez-vous faire après l'avoir activé ?

Maintenant qu'il est actif, vous pouvez installer Django (ou autre chose) juste pour ce projet :

```bash
pip install django
```

Cela installe Django à l'intérieur de l'environnement virtuel, et non globalement.

Pour double-vérifier :

```bash
pip list
```

Vous verrez Django et tous les autres packages installés listés là.

## Comment désactiver l'environnement virtuel

Lorsque vous avez terminé, tapez simplement :

```bash
deactivate
```

C'est tout. Votre terminal revient à la normale, et le Python de votre système n'est plus lié au projet.

## FAQ

### **Dois-je activer l'environnement à chaque fois ?**

Oui, chaque fois que vous ouvrez une nouvelle session de terminal et que vous voulez travailler sur votre projet Django, activez-le à nouveau en utilisant la commande pour votre système d'exploitation.

### **Que faire si** `activate` **ne fonctionne pas ?**

Si vous êtes sous Windows, PowerShell peut bloquer le script. Exécutez ceci :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Puis essayez d'activer à nouveau.

### **Puis-je utiliser VS Code ou un autre éditeur avec cela ?**

Absolument. VS Code détecte même automatiquement votre environnement virtuel. Vous pouvez sélectionner l'interpréteur depuis le coin inférieur gauche ou en appuyant sur `Ctrl+Shift+P` → "Python: Select Interpreter."

## Conseils bonus

### Ajouter un fichier `.gitignore`

Si vous utilisez Git, vous ne voulez pas télécharger le dossier `venv` sur GitHub. Ajoutez cette ligne à votre fichier `.gitignore` :

```python
venv/
```

### Utiliser `requirements.txt`

Une fois que vous avez installé les packages de votre projet, figez-les comme ceci :

```bash
pip freeze > requirements.txt
```

Ensuite, plus tard, vous (ou quelqu'un d'autre) pouvez les installer avec :

```bash
pip install -r requirements.txt
```

Cela est utile pour les projets d'équipe ou pour déplacer votre application sur un serveur.

## Conclusion

Activer votre environnement virtuel Django peut sembler une petite chose, mais c'est un grand pas vers devenir un développeur confiant et organisé.

Une fois que vous aurez pris le coup, cela deviendra une seconde nature – et votre vous futur vous remerciera de l'avoir appris de la bonne manière dès le début.

Aimeriez-vous vous connecter avec moi ? Vous pouvez le faire sur [X.com/_udemezue](https://X.com/_udemezue)

### Ressources utiles

* [Documentation officielle de Python sur `venv`](https://docs.python.org/3/library/venv.html)
    
* [Site officiel de Django](https://www.djangoproject.com/)
    
* [Tutoriel sur les environnements virtuels Python (Real Python)](https://realpython.com/python-virtual-environments-a-primer/)
    
* [Comment corriger "activate.ps1 ne peut pas être chargé" dans PowerShell](https://stackoverflow.com/questions/63443862/activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled)
    
### Apprentissage supplémentaire

Si vous êtes sérieux au sujet de Django, voici quelques ressources gratuites et payantes que je recommande :

* [Django pour débutants par William S. Vincent](https://djangoforbeginners.com/)
    
* [Cours intensif Django de FreeCodeCamp sur YouTube](https://www.youtube.com/watch?v=F5mRW0jo-U4)
    
* [CS50 Programmation Web avec Python et JavaScript](https://cs50.harvard.edu/web/2020/)