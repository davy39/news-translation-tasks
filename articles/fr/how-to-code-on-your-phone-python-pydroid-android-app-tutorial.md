---
title: Comment créer une application Web sur votre téléphone – Tutoriel Python & Pydroid
  Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-23T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-on-your-phone-python-pydroid-android-app-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6029aa6f0a2838549dcc582d.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
- name: Python
  slug: python
seo_title: Comment créer une application Web sur votre téléphone – Tutoriel Python
  & Pydroid Android
seo_desc: 'By Precious Oladele

  Hey there, how are you? I''m an 18 year old a backend developer and an aspiring
  Machine Learning Engineer. And in this article, I''m going to be writing about how
  to build a web app on your phone using Python 😁. Let''s dive into it....'
---

Par Precious Oladele

Salut, comment ça va ? Je suis un développeur backend de 18 ans et un aspirant ingénieur en Machine Learning. Et dans cet article, je vais écrire sur comment créer une application web sur votre téléphone en utilisant Python 😁. Plongeons-nous dedans.

![Image](https://lh3.googleusercontent.com/TW_PdXBpgeWY4mLcHjFisp8e7Lk7Zsn1aFarXBkmvhEMP0XR5xzTDxhKcCizsrJ25rkPeMeWp7ctlG0Wy7_WFUS0bzT-JVJfpe6X_3OqnuE_df2q5B3KIrhl3EG47w3Dik3nIZE)

## **Conditions requises**

La première chose dont nous avons besoin ici est un téléphone Android, au moins la version 6.0 et supérieure. Mais que diriez-vous si je vous disais que c'est tout ce dont nous avons besoin ? Cela semble trop beau pour être vrai.

Maintenant, la prochaine chose à faire est d'installer une application mobile sur notre téléphone appelée pydroid3. 


![Image](https://lh6.googleusercontent.com/fwM9r46B-sTofVF6IybUOhCTYoM8vSAPfumfBIiiL_wWLQpgdQgeR2B_2-N28NtNLaA7HvTtsZxlXdX03anCGvbt4QAlhQ_wyb9_AIfqG9L4ZMCjQOrKLg5OFPeZgKrJdqKEeb8)

Comme vous pouvez le voir, pydroid3 est une application mobile qui vous permet d'écrire du Python sur votre téléphone portable, alors allez-y et installez-la. 

La prochaine chose à faire est d'installer Django. Si vous n'êtes pas familier avec Django, veuillez consulter la [documentation de Django ici](https://www.djangoproject.com/). 

Pour installer Django, nous devons ouvrir la navigation latérale dans notre pydroid3 et sélectionner Terminal :

![Image](https://lh6.googleusercontent.com/qO3djIyoXMZB8MzcIaFDmNddhB2t9XgLLgCzonR2CDkWJc0pXtap9gyGhqZfpv0uFCCvtYnynL6pAOfgactlDfpwoy03TfgqEoN2W_gAO7nOeoaLbySZEQkOSBuprhs67jc-Ens)

Ensuite, cliquez dessus et nous devrions voir ceci :

![Image](https://lh3.googleusercontent.com/fTwNrfhCQpxKBFbrsN3B6dt4kFWvDUEJElZ897o-d21XbiYj42gZBLhiLMt7ffvSp44OQBrubC9jK62WvzneTlF-7WxcZZygHEqo4hmQ_9V42Pw4FgvdKB75EA3fv4q5nGZiL7k)

Une fois cela fait, tout ce que vous avez à faire est de taper la commande suivante :

```python
pip install django
```

Et vous devriez obtenir ce qui suit. Je reçois un message "requirements satisfied" parce que je l'ai déjà installé.

![Image](https://lh6.googleusercontent.com/vYhoSBXGgvq2EiX6iXQ1RBLrvUe8zQHM3Aq65ZDIDRKSOoLqOrW5QQWE5yQ-ThbhzYTb6kwKf_jHzVoQ79wTbz2KZNv32oEBX1LjAFeMYaiQb4bebYOWii-h1W3EKQkTWvgA2_Q)

Il est installé avec succès, mais confirmons cela. Dans le terminal, tapez `django-admin` et appuyez sur Entrée.

Vous devriez obtenir ceci :

![Image](https://lh5.googleusercontent.com/jU17O6AVeFcy6rYMJ0mp_DEqnR9q51F-mhLZH1K7Ny8tixSeY7Xl8Jx27hBfxWfHPimt-1xCfO6x2AOlvYKYR92slC3sBwJNRg9uDJsJ6had0Yq1UTXZ5_CQvfCwwKneKCO_Gp4)

Cela signifie qu'il est réellement installé.

## Comment construire notre projet

Alors commençons à construire notre projet. Ouvrez votre terminal et tapez la commande suivante :

`django-admin startproject myapp`

Cela crée une application Django appelée myapp dans votre dossier racine.

Changez de répertoire en tapant `cd myapp` et tapez `python manage.py runserver`. Ensuite, vous devriez obtenir ceci :

![Image](https://lh6.googleusercontent.com/fqO-uHACjoAXNQSrm5Pikjr-GQQkY3SbkE3G9Sgel1XZbePIf7hJaePd8yGxdrbYiyRdpeWCFUYBNo6iKMzTJqZg3s8j6CTGIoZYH-YJjT-tjHA0FCKtdGJEGzNy0Y8Qj5uTQrg)

Maintenant, le serveur a démarré. Ensuite, pour le tester dans le navigateur, visitez [127.0.0.1:8000](http://127.0.0.1:8000).

![Image](https://lh3.googleusercontent.com/oqMFGPasUPLxuZoRqWHQ9mEhpitsg2XK8XPzLz_U-TvnFGzjkIaHVKUHXxwYkMDskLp_36F75BIAb-qv37bHccUESSZ9Jqa6XV7FGoWYk_IS8SfPYZfMTSNmo2ei-SMVa9cp_C8)

Et voilà ! Vous devriez voir que Django a été configuré avec succès.

La prochaine chose à faire est de créer notre application Django. Dans Django, le dossier de projet sert de racine tandis que l'application sert d'application elle-même. 

Pour créer une application Django, assurez-vous d'être toujours dans le répertoire, puis tapez `python manage.py startapp todo`. Cela crée une application To-do dans notre projet myapp comme ceci :

![Image](https://lh5.googleusercontent.com/ycIZAg7VGJO4Auwc7z_bsx5CU19Ks-rfubo_3amBKgvO-HeHb2I7mQu_loWg6leR22dvlMGh0FPgO1_-anmVpEHO4O4dlQik-MfiqF7Dx9BmxuI6YBjqPMcv8S3czgVCyftBu80)

Ensuite, dans le dossier todo, nous devrions voir quelque chose comme ceci :

![Image](https://lh6.googleusercontent.com/Fc60wk6pMuEQ8JvIwfOK2E1zezR9n_N-8o_X__F-yr1D1yD0BEuV62G9zoqG5GQnyA0shbI79JvNs3Z-YHunEoUyZw7LAt2eumkyKjj9M39sDbmDgzZ_axvjRyVeyLZC5ohVQmY)

Nous examinerons plus en détail les fichiers lorsque nous commencerons à travailler avec eux.

## Comment configurer notre application

Maintenant, rendons possible que l'application soit servie par le projet Django. Tout d'abord, ouvrez votre fichier `settings.py` dans le dossier myapp et ajoutez `'todo'` aux applications installées comme ceci :

![Image](https://lh4.googleusercontent.com/mxTcaRk-ON73sPH6XL31kvZmUJjfwn1knbhMgTJALeyx6l8A1umvtXjLazS34oTjbPZeivGGTe6w6zsEQ1QzhTjaYDJ5tHsbhpeyxAfrvABzGHrNsElcv7RR9kQZi_Tttt4PjIc)

Ensuite, nous devons ouvrir notre `urls.py` et ajouter ce qui suit à votre code :

```python
from django.urls import path, include

path('', include('todo.urls'))
```

![Image](https://lh6.googleusercontent.com/VEWQQt84a9DSeqmuT-LrE9EMmYnDnDfwJQQtJhI21WDTJf4EDaE212wj7BLoBX85Vjm90gFb6KsB6yGJ6PDyfgdTT9BL5hcmDZzNfIdHlceR40qJNVubaNKduXjA2viT7yqLJ14)

Ce qui s'est réellement passé, c'est que j'ai ajouté `include` à l'importation de `django.urls` path. Et en dessous du path (`admin`), nous avons créé un path vide qui pointe vers ou inclut le fichier `urls.py` dans le répertoire de l'application todo. J'espère que c'est clair.

Ensuite, nous devons créer un nouveau fichier dans le répertoire de fichiers todo nommé `urls.py` et y ajouter le code suivant :

```python
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home')
 ]
```

![Image](https://lh6.googleusercontent.com/cmxgwJ5PeIXW_yGgo9AKaVK10pDjGFl26gML6VicCQVLtsiCiorL5tBahCMOxHG-1HlrocwbaVod5SN6DFJFIZ5n1gidGOfJdaGW_p8holylN4aCUb-2ankvfIQygHz6cjT2tgc)

Nous avons importé `path` de `Django.urls` et également importé `views` du répertoire racine. Ensuite, nous avons créé nos `urlpatterns` avec la première partie comme lien racine. Comme vous pouvez le voir, views.index signifie simplement que nous pointons cette vue vers la fonction index dans le fichier `views.py`. Vous verrez comment cela fonctionne en un clin d'œil.

Passons à notre fichier `views.py` et ajoutons du code.

En haut, importez `HttpResponse` comme ceci :

`from django.http import HttpResponse`

Et ajoutez ceci en dessous :

```python
def index(request):
	return HttpResponse('Hello')
```

![Image](https://lh5.googleusercontent.com/QUpf-9cT8Z-dKXTkO1FTm2-IkjD3_NIfYSQCy_XlALUTnIg_XrrxKurZLAJ19DQCk1W5mqBx4Mo5IL9ycL5gGS_w4LyI4zXxSo8y23mNaZ2OodFg-qLEi3Dh2FN_m7ueYjPYrb4)

Comme vous pouvez le voir, nous avons créé la fonction index que nous avons appelée dans notre `urls.py` et nous avons passé un paramètre de requête dedans. Ensuite, nous avons retourné un `HttpResponse`. 

Mais avant que le `HttpResponse` puisse fonctionner, nous devons l'importer de `django.http import HttpResponse` – aussi simple que ABC. Essayons ceci : ouvrez votre terminal, cd dans myapp et tapez `python manage.py runserver` pour le tester.

![Image](https://lh3.googleusercontent.com/Tqb7c-adOuVHbyi-7XBQsv0HHJvxjUhcAZ3N4d5nkOEVNVwfSXxkENlD0l0UI3Jd4qLhO3k8ELDW6yG8yRiP0MmjkO0Q4TvGTYunQIBNgSMNrXxfI7ygMHeN2FtjoJc37mVIVr0)

Comme vous pouvez le voir, il a retourné la réponse. Donc ensuite, nous allons charger nos fichiers de modèle HTML.

Pour charger nos fichiers HTML, nous devons créer un dossier comme ceci dans le répertoire todo dans cet ordre :

`todo/templates/todo`

Dans le répertoire todo, créez un dossier appelé templates. À l'intérieur de ce dossier, créez un dossier appelé todo, aussi simple que cela.

Ensuite, allez-y et créez un simple fichier HTML appelé index.html et écrivez ceci dedans :

`<h1>Hello world</h1>`

Pour le charger, faites en sorte que votre code `views.py` ressemble à ceci :

```python
def index(request):
	return render(request, 'todo/index.html')
```

![Image](https://lh3.googleusercontent.com/mhirciumIf_FcO764txwH5MOMl40vkZ6f41c0oXFreX1UA2IiqQG9E42TfbUBCZto4xG6-vl0t5sQj3ID1FBk_gL074Rzm4pn5a8RmMsP7DuMZKYVi1KQg-Bk35yr1gJGiE2ukg)

Maintenant, au lieu de retourner une réponse, nous avons retourné une vue de rendu qui nous permet de rendre notre modèle HTML, sauvegardez ceci, ouvrez votre terminal, cd dans myapp et exécutez-le. Nous devrions avoir ceci

![Image](https://lh6.googleusercontent.com/NzW4_E80BNOtRq-E4qUg1GdvqHUUQQAxMAdUSGhxROCDkSUnzddSyX4E7Wz5_zPY29twa7D2PVmS85LYmCnzEAvgE-oU2MEk1mDeNhFW5FBuD2eAjDxpPkJfXiJAMEyk1uKZVkw)

Comme vous pouvez le voir, cela fonctionne bien - passons à l'étape suivante.

## Comment configurer les fichiers statiques 

Maintenant, pour configurer les fichiers statiques, créez un nouveau dossier dans votre répertoire todo et nommez-le static. À l'intérieur de ce dossier, créez un dossier et nommez-le todo.

Donc, cela devrait être comme ceci : `/static/todo/`.

Dans le répertoire todo, créez un fichier et nommez-le `main.css`. Ensuite, écrivons un peu de style dedans :

```css
body {
background-color: red;
}
```

Et sauvegardez-le.

Maintenant, rééditons notre fichier `index.html` en écrivant ce code :

```django
{% load static %}
<!Doctype html>
<html>
<head>
<title>My page</title>
<link rel="stylesheet" href="{% static 'todo/main.css' %}" >
</head>
<body>
Hello
</body>
</html>
```

![Image](https://lh5.googleusercontent.com/Luboze-gNbfQkpTZVwOChtQKrQpC2eWnsTAE41f9mDdWaqaKtk2yYAV0uP3ufKE_EDrpfCoRvOFlHmLCJKucPNB_kQmZoaAZB5reCcW2wrddbsDbRPoIe2iacGLpFfLEcGYZEnA)

Et maintenant, exécutons-le :

![Image](https://lh5.googleusercontent.com/ARWYir-7j8-yF9yCzc3bNuW1ZyLKOG30iljprX4AJsnyIdYLtK_0Of7Uu4WJLuufoyRkVL5LnG8J-bepoBcRzm1e57AuaLmbA5iIyO_RY_KsKRVrsc0OfGmDbLOkT-FIZECwIyY)

Si vous avez suivi avec moi, alors vous devriez avoir ce qui précède.

## Comment charger le panneau d'administration et les modèles 

Maintenant, pour charger notre panneau d'administration, nous devons créer un superutilisateur. C'est simple à faire – il suffit d'ouvrir votre terminal et de vous rendre dans le dossier myapp, puis de taper `python manage.py createsuperuser` et d'appuyer sur Entrée. Vous devriez voir ceci :

![Image](https://lh3.googleusercontent.com/PBTNq4SLyU4xMFsxh8wXuP0fUCnNKqL0zPiAqclNSPc4J7j4izPVgikXXQpaPqcPeSfFhrlQgf2xwyuhWz-s4RJWn1ftc5icsi9bt2QwmjKxjp3reecfmCxQ3GdVvE04HUAc8po)

Nous obtenons une erreur parce que nous n'avons pas encore exécuté `python manage.py migrate`. Alors tapez cela et appuyez sur Entrée, et vous devriez avoir quelque chose comme ceci :

![Image](https://lh3.googleusercontent.com/_oEnoQWnv1VRtZf8W60ZyfFVGQV-nFzYKX4oj45SLCLUlPNNyZOefRkIj8ROdoNdkgECWr4OKmxRVUsRZy2c27XwsM7wQ4_7xeJWnlzPrBFZ79t7J8zZXFJLtfDqJf1vrvtShjc)

Maintenant, tapez `python manage.py createsuperuser` et appuyez sur Entrée :

![Image](https://lh3.googleusercontent.com/t8Z8qo8Z3xNi9C86RjkiujHiS6en5b16eYPA5uMTfXAQYNpFjjuWaY_WEL0TrxLUlpaJJHzF143Vk0UuTQIzuD4GICQF4X1K2CF0vyb1ws33JN2W_FeyVu3xMOsn1posUZW0eFs)

Il suffit de remplir les informations d'identification. La prochaine chose à faire est d'exécuter notre serveur et de pointer vers 127.0.0.1:8000/admin.

![Image](https://lh6.googleusercontent.com/Uoen79EV8PaEDuhnt2eBaCnnJAEzHhLydikTi8BOxUSZ9DrGp9GbtUk-Um7TmMDW64Zd0RbAkXja8RjyqiX58hlWdFyrzHTUVN0NCx93e9BOx36Va4ysCX7JyJRlEmdUBnbltuA)

Connectez-vous et vous serez dirigé vers le tableau de bord :

![Image](https://lh3.googleusercontent.com/C8A8OermBdrvdB_6NEHg2mFgkkuVBsePdfdmlNhulSw2m7Jkdhea_jdDFNQnbvVgqxJcXj-ftbcNmdR6nYImJC2AV9edqcPB5pkhUm0zvImzzzAokHZ4bDwYe4BPPvnXsK18Ng0)

Maintenant que nous avons fait le panneau d'administration, travaillons avec le modèle (base de données). Nous allons créer un modèle qui collecte des contenus. Alors ouvrez votre fichier `models.py` et tapez ce code :

```python
class Post(models.Model):
	content = models.CharField(max_length=255, null=False)
    
    def __str__(self):
    	return self.content
```

![Image](https://lh4.googleusercontent.com/pyZXf_3jSGzz-sciBxAvb-ry4_TbZMnuHWWWAOl17LQ5hCi55DoKxzq0iYu6wuv8UsQhn3-w27GOzlt2N_9mpdKoHcZza9mWoBgselVQXC6bPD-ev-uTjlW1RbN1c2OussUgEpg)

Nous créons une classe qui a le paramètre `models.Model` et donne une variable `content` qui contient un `CharField()`, un peu comme un champ de texte. Enfin, nous créons une méthode magique `str` qui retourne le nom du modèle au lieu d'un objet.

Alors ensuite, nous devons exécuter la migration. Ouvrez votre terminal, cd dans myapp, et tapez `python manage.py makemigrations`. Vous devriez voir ceci :

![Image](https://lh6.googleusercontent.com/UBbVNNg1d8jhPTusB-HRRoUsqFfxaZdJLzSIzNIt3P4kby8Tor4G8Bme1e-yq8mOLFgfrUh3nb6MC3BSaOUQDr68_tEmIRtQBS7N7Y66wTbXdMMg-0EJ0svM3tw3j9GLgquC_IU)

Cela signifie qu'il a créé la table Post dans notre base de données. Ensuite, exécutez également `python manage.py migrate` ce qui donnera le résultat suivant :

![Image](https://lh6.googleusercontent.com/VyQYel1QFdxc2D5oSOdDD6QPth2jVC5_CTj8SVyDo8pAusvl6qjH7XQUhmhbfXNLjdUiAc566pYTj0O2c-AsRHwVLeDo2xeOv1HWsldCwH1oxu3sM5WJTNOj9-fpZEOfVHMYZ6k)

Cela signifie que tout est clair. Maintenant, pour l'ajouter à la page d'administration, ouvrez `admin.py` et tapez ce code :

```python
from .models import *

admin.site.register(Post)
```

![Image](https://lh3.googleusercontent.com/jzqRK8kVE6raStmHC8jJoqr8oYOXhygDpe8hoN_JdSRiF3Mpes3_Evw83U0nMczqgAobIY8zp_Z6ve-xb3jv6x7uChFzvdTyDqDZysD2j0pKxiGu2-V9pkvH02HKAzBA2HZr6WQ)

Nous avons importé toutes les classes de modèle du modèle et enregistré le modèle de post dans le panneau d'administration. Maintenant, si nous ouvrons le panneau d'administration, nous devrions voir le post et sauvegarder certaines données.

![Image](https://lh4.googleusercontent.com/E9gkvNmpFiCJg24zYj7GpLzsM8AsoGUkoZHcS1Z3bxMva_Z3Jov5Yy7UzbgU251laLwGGRWqaFK1iIrILblSyktYK42Q-fzgS6ihGf0LYxR0Zl9qvkmG7sneHM2KFRoSPDy2k3o)

Remarquez qu'il est maintenant dans la liste des applications todo :

![Image](https://lh3.googleusercontent.com/BSyVagLKFGvtINW-jnuhrXRoFdB87S5lGksH37z5uewqVCn_WBHP-eI8gF6BUoG56Dz-SnKUtRonFhNX--c23V07WfXhOxHmCmJ460cXAr__NjTAkvXB4JnxIXlbsQcRtDO0uNU)

Après avoir cliqué dessus, vous devriez voir ceci :

![Image](https://lh3.googleusercontent.com/4zxSgdVcDnDrpr6aIquG854x59GQb0ZMJ3D-YnAs-9EDR0EYwHl_HBAbrpPGGr7YLfWn0PjJA19aukrUcBbUMURpn4ofEGCwWF4541ee_-OKZQj_cWuv_yxWvUGYGOZfdzu6C90)

Ensuite, vous pouvez créer un post si vous le souhaitez.

## Comment afficher les données de la base de données dans la vue

Enfin, nous allons récupérer nos données de la base de données. Pour ce faire, nous devons mettre à jour notre `views.py` comme suit :

```python
from .models import *

def index(request):
	content = Post.objects.all()
    context = {'content': content}
    return render(request, 'todo/index.html', context)
```

![Image](https://lh4.googleusercontent.com/NHpq8LEAtu06ntzUodCuBZT86FS_u_TPphhlfZ-CiP5rFglQcjtRB0zUdK0jkz_udZeXRh8JNqdZOhRSfV9A69I63b8P5DtBGtQo44zmwufnGTaybAaWAL0yOn9T544_mdXaLN4)

C'est aussi simple que cela : nous avons importé tout depuis `models.py`, créé une variable appelée `content`, et récupéré toutes les données de la table Post. Ensuite, nous les avons passées sous forme de dictionnaire à notre vue. Donc dans notre index.html pour que cela fonctionne, ajoutez simplement ceci :

```django
{% for contents in content %}
{{content.content}}
{% endfor %}
```

![Image](https://lh4.googleusercontent.com/4zgGmOcVBVa906mn0AVk0Vh9MbaFeYS0VUVoOC00Jw6wtR54S55BMPjz5t0_z2LTgbs9Ldpt3VOKcEjgxMhSE63xGu8XKSx2tWbKFYp2ndxHc31pcAMFdSturJqEy07ca_IYC1c)

Ici, nous avons écrit une boucle en utilisant la balise de modèle et récupéré toutes les données de contenu. Maintenant, ouvrez votre terminal, cd dans myapp, et exécutez le serveur pour voir la magie opérer :

![Image](https://lh5.googleusercontent.com/gKJf7AGR-0ZxOCeD_QKGffg4d-wpK0Lk8Z0Fkdj39Rj1V6dpWGf_KA1iBDJ2xE-Lq_zsJQHq6eIywPujAVmEk_R7e-Ug7ox94Rk5x212Bk7cBm0fHaMnGtqQM9zscDELygE1LvI)

Cela fonctionne, mais confirmons cela :

![Image](https://lh5.googleusercontent.com/IVjbVn-_3Exnnoq2s0pvHTeL2paWcqogzg1mp_Aj15GtXKqUPerrFDGZ-SjYKqpUX8Es1KGo0fSWoAOACLgri_LcT5oV7tkG6dtL2OestlnQC25OzFdYEhcyb0KPH3b12BBdJTU)

Et le résultat devrait être le suivant :

![Image](https://lh3.googleusercontent.com/jlYy4UCV3MJd-JytvGUBLgC20k3-cduvDQ2O3FIb9kAF7VgRyGxyqb_G1Mjiqis261HQS68uIJUk5I9ccFJBFL6Ht3LiePvprBcsqkSS9lZZzJ_cc2noxJm32GPp9ytsiYl7t2o)

Violà – cela fonctionne bien. Enfin, vous pouvez simplement ajouter un saut de ligne pour que vous puissiez le lire plus clairement. Et nous avons terminé !

Merci d'avoir lu. Si vous souhaitez suivre un tutoriel approfondi sur Django, veuillez visiter ma chaîne YouTube [Devstack](https://youtube.com/channel/UCLcHGKxbEO1XGVETXqzYXLA) et vous abonner.