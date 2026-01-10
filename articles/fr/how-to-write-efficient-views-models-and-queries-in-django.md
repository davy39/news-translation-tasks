---
title: Comment écrire des vues, modèles et requêtes efficaces dans Django
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-07-27T21:17:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-efficient-views-models-and-queries-in-django
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/cover.png
tags:
- name: Django
  slug: django
- name: Productivity
  slug: productivity
seo_title: Comment écrire des vues, modèles et requêtes efficaces dans Django
seo_desc: "I like Django. It’s a well-considered and intuitive framework with a name\
  \ I can pronounce out loud. You can use it to quickly spin up a weekend-sized project,\
  \ and you can also use it to run full-blown production applications at scale. \n\
  I’ve done both..."
---

J'aime Django. C'est un framework bien conçu et intuitif avec un nom que je peux prononcer à voix haute. Vous pouvez l'utiliser pour lancer rapidement un [projet de taille week-end](https://github.com/victoriadrake/react-in-django), et vous pouvez également l'utiliser pour exécuter des [applications de production à grande échelle](https://applybyapi.com).

J'ai fait les deux, et au fil des ans, j'ai découvert comment utiliser certaines fonctionnalités de Django pour une efficacité maximale. Ce sont :

* Vues basées sur des classes versus vues basées sur des fonctions
* Modèles Django
* Récupération d'objets avec des requêtes

Examinons comment ces outils vous permettent de créer une application Django performante, agréable à construire et à maintenir.

## Vues basées sur des classes versus vues basées sur des fonctions

Rappelez-vous que Django est entièrement en Python sous le capot. En ce qui concerne les vues, vous avez deux choix : les [fonctions de vue](https://docs.djangoproject.com/en/3.0/topics/http/views/) (parfois appelées "vues basées sur des fonctions"), ou les [vues basées sur des classes](https://docs.djangoproject.com/en/3.0/topics/class-based-views/).

Il y a quelques années, lorsque j'ai construit [ApplyByAPI](https://applybyapi.com) pour la première fois, il était initialement composé entièrement de vues basées sur des fonctions. Celles-ci offrent un contrôle granulaire et sont bonnes pour implémenter une logique complexe. Tout comme dans une fonction Python, vous avez un contrôle complet (en bien ou en mal) sur ce que fait la vue.

Mais avec un grand contrôle vient une grande responsabilité, et les vues basées sur des fonctions peuvent être un peu fastidieuses à utiliser. Vous êtes responsable de l'écriture de toutes les méthodes nécessaires pour que la vue fonctionne - c'est ce qui vous permet de personnaliser complètement votre application.

Dans le cas d'ApplyByAPI, il n'y avait que quelques endroits où ce niveau de fonctionnalité personnalisée était vraiment nécessaire. Ailleurs, les vues basées sur des fonctions ont commencé à rendre ma vie plus difficile. Écrire ce qui est essentiellement une vue personnalisée pour des opérations courantes comme l'affichage de données sur une page de liste est devenu fastidieux, répétitif et sujet aux erreurs.

Avec les vues basées sur des fonctions, vous devrez déterminer quelles méthodes Django implémenter afin de gérer les requêtes et de passer des données aux vues. Les tests unitaires peuvent prendre un certain travail à écrire. En bref, le contrôle granulaire que les vues basées sur des fonctions offrent nécessite également une certaine tedium granulaire pour une implémentation correcte.

J'ai fini par retarder ApplyByAPI pendant que je refactorisais la majorité des vues en vues basées sur des classes. Ce n'était pas une petite quantité de travail et de refactorisation, mais une fois terminé, j'avais un ensemble de petites vues qui ont fait une énorme différence. Je veux dire, regardez simplement celle-ci :

```python
class ApplicationsList(ListView):
    model = Application
    template_name = "applications.html"
```

C'est trois lignes. Mon ergonomie de développeur, et ma vie, sont devenues beaucoup plus faciles.

Vous pouvez penser aux vues basées sur des classes comme des modèles qui couvrent la plupart des fonctionnalités dont toute application a besoin. Il y a des vues pour afficher des listes de choses, pour voir une chose en détail, et des [vues d'édition](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/) pour effectuer des opérations CRUD (Create, Read, Update, Delete).

Parce que l'implémentation de l'une de ces vues génériques ne prend que quelques lignes de code, la logique de mon application est devenue dramatiquement succincte. Cela m'a donné moins de code répété, moins de places pour que quelque chose aille mal, et une application plus facile à gérer en général.

Les vues basées sur des classes sont rapides à implémenter et à utiliser. Les vues génériques basées sur des classes intégrées peuvent nécessiter moins de travail pour les tester, puisque vous n'avez pas besoin d'écrire des tests pour la vue de base que Django fournit. (Django fait ses propres tests pour cela ; pas besoin que votre application double-vérifie.)

Pour ajuster une vue générique à vos besoins, vous pouvez [sous-classer une vue générique](https://docs.djangoproject.com/en/3.0/topics/class-based-views/#subclassing-generic-views) et remplacer des attributs ou des méthodes. Dans mon cas, puisque je n'avais besoin d'écrire des tests que pour les personnalisations que j'ai ajoutées, mes fichiers de test sont devenus dramatiquement plus courts, tout comme le temps et les ressources nécessaires pour les exécuter.

Lorsque vous pesez le choix entre les vues basées sur des fonctions ou des classes, considérez le niveau de personnalisation dont la vue a besoin, et le travail futur qui sera nécessaire pour la tester et la maintenir.

Si la logique est courante, vous pourrez peut-être démarrer rapidement avec une vue générique basée sur une classe. Si vous avez besoin d'une granularité suffisante pour que la réécriture des méthodes d'une vue de base la rende trop compliquée, envisagez plutôt une vue basée sur une fonction.

## Modèles Django

Les [modèles](https://docs.djangoproject.com/en/3.0/topics/db/models/) organisent les concepts centraux de votre application Django pour les rendre flexibles, robustes et faciles à utiliser. Si elles sont utilisées judicieusement, les modèles sont un moyen puissant de colliger vos données en une source définitive de vérité.

Comme pour les vues, Django fournit certains types de modèles intégrés pour la commodité de l'implémentation de l'authentification de base, y compris les modèles [User](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/) et [Permission](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/). Pour tout le reste, vous pouvez créer un modèle qui reflète votre concept en [héritant d'une classe parente Model](https://docs.djangoproject.com/en/3.0/topics/db/models/#model-inheritance).

```python
class StaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name + " - " + self.user.email
```

Lorsque vous créez un modèle personnalisé dans Django, vous sous-classez [la classe Model de Django](https://github.com/django/django/blob/master/django/db/models/base.py) et profitez de toute sa puissance. Chaque modèle que vous créez correspond généralement à une table de base de données. Chaque attribut est un champ de base de données. Cela vous donne la capacité de créer des objets avec lesquels travailler que les humains peuvent mieux comprendre.

Vous pouvez rendre un modèle utile en définissant ses champs. De nombreux [types de champs intégrés](https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types) sont commodément fournis. Ceux-ci aident Django à déterminer le type de données, le [widget](https://docs.djangoproject.com/en/3.0/ref/forms/widgets/) HTML à utiliser lors du rendu d'un formulaire, et même les exigences de [validation de formulaire](https://docs.djangoproject.com/en/3.0/ref/forms/validation/). Si nécessaire, vous pouvez [écrire des champs de modèle personnalisés](https://docs.djangoproject.com/en/3.0/howto/custom-model-fields/).

Les [relations](https://docs.djangoproject.com/en/3.0/topics/db/models/#relationships) de base de données peuvent être définies à l'aide d'un champ [ForeignKey](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey) (plusieurs-à-un), ou un champ [ManyToManyField](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField) (je vous laisse trois essais). Si ceux-ci ne suffisent pas, il y a aussi un [OneToOneField](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.OneToOneField).

Ensemble, ceux-ci vous permettent de définir des relations entre vos modèles avec des niveaux de complexité limités uniquement par votre imagination. (Selon l'imagination que vous avez, cela peut être un avantage ou non.)

## Récupération d'objets avec des requêtes

Utilisez le Manager de votre modèle (`objects` par défaut) pour [construire un QuerySet](https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-objects). Il s'agit d'une représentation des objets dans votre base de données que vous pouvez affiner, en utilisant des méthodes, pour récupérer des sous-ensembles spécifiques. Toutes les méthodes disponibles sont dans l'[API QuerySet](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet) et peuvent être enchaînées pour encore plus de plaisir.

```py
Post.objects.filter(
    type="new"
).exclude(
    title__startswith="Blockchain"
)
```

Certaines méthodes retournent de nouveaux QuerySets, comme [`filter()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#filter), ou [`exclude()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exclude). Les enchaîner peut vous donner des requêtes puissantes sans affecter les performances, car les QuerySets ne sont pas récupérés de la base de données [jusqu'à ce qu'ils soient évalués](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#when-querysets-are-evaluated). Les méthodes qui évaluent un QuerySet incluent `get()`, [`count()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#count), `len()`, `list()`, ou `bool()`.

Itérer sur un QuerySet l'évalue également, évitez donc de le faire lorsque cela est possible pour améliorer les performances des requêtes. Par exemple, si vous voulez simplement savoir si un objet est présent, vous pouvez utiliser `exists()` pour éviter d'itérer sur les objets de la base de données.

Utilisez [`get()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.get) dans les cas où vous souhaitez récupérer un objet spécifique. Cette méthode lève [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/3.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned) si quelque chose d'inattendu se produit, ainsi que l'exception `DoesNotExist`, si, devinez.

Si vous souhaitez obtenir un objet qui peut ne pas exister dans le contexte d'une requête utilisateur, utilisez le pratique [`get_object_or_404()`](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-object-or-404) ou [`get_list_or_404()`](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-list-or-404) qui lève [`Http404`](https://docs.djangoproject.com/en/3.0/topics/http/views/#django.http.Http404) au lieu de [`DoesNotExist`](https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.DoesNotExist). Ces [raccourcis](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/) utiles sont adaptés à cet usage. Pour créer un objet qui n'existe pas, il y a aussi le pratique [`get_or_create()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get-or-create).

## Essentiels efficaces

Vous avez maintenant une bonne maîtrise de ces trois outils essentiels pour construire votre application Django efficace - félicitations !

Django peut faire beaucoup plus pour vous, alors restez à l'écoute pour les futurs articles.

Si vous allez construire sur GitHub, vous pourriez aimer configurer mon [django-security-check GitHub Action](https://github.com/victoriadrake/django-security-check). En attendant, vous êtes bien parti pour construire un beau projet logiciel.