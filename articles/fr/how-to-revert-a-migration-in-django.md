---
title: Comment annuler une migration dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-07-16T21:23:44.330Z'
originalURL: https://freecodecamp.org/news/how-to-revert-a-migration-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745937479722/d02a1abc-33b1-4506-8001-033b4ec43130.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment annuler une migration dans Django
seo_desc: 'So, you''re working with Django, you''ve run a migration, and now something’s
  broken. Maybe you added a field that shouldn''t be there.

  Maybe you renamed a model, and suddenly your database is a mess. Or maybe you''re
  just experimenting and want to roll ...'
---

Donc, vous travaillez avec Django, vous avez exécuté une migration, et maintenant quelque chose est cassé. Peut-être avez-vous ajouté un champ qui ne devrait pas être là.

Peut-être avez-vous renommé un modèle, et soudain votre base de données est un vrai désordre. Ou peut-être êtes-vous simplement en train d'expérimenter et souhaitez-vous revenir en arrière.

C'est là que l'annulation des migrations entre en jeu.

Savoir comment annuler une migration dans Django est tout aussi important que de savoir comment en créer une. Il ne s'agit pas d'être parfait, mais d'être capable de corriger les erreurs rapidement, sans panique. J'ai déjà été dans cette situation.

Une seule migration peut tout casser si elle se passe mal. Mais la bonne nouvelle, c'est que Django vous donne des outils pour revenir en arrière en toute sécurité.

Permettez-moi de vous guider à travers ce processus, en utilisant un langage simple et des étapes claires.

## Table des matières

* [Qu'est-ce qu'une migration dans Django ?](#heading-qu-est-ce-qu-une-migration-dans-django)
    
* [Comment annuler une migration dans Django](#heading-comment-annuler-une-migration-dans-django)
    
    * [Cas 1 : Annuler une migration déjà appliquée](#heading-cas-1-annuler-une-migration-déjà-appliquée)
        
    * [Cas 2 : Annuler une migration non encore appliquée](#heading-cas-2-annuler-une-migration-non-encore-appliquée)
        
* [Cas particulier : Annuler toutes les migrations (Tout réinitialiser)](#heading-cas-particulier-annuler-toutes-les-migrations-tout-réinitialiser)
    
* [Scénario d'exemple : Corriger une migration cassée](#heading-scenario-d-exemple-corriger-une-migration-cassée)
    
* [Pièges courants (Et comment les éviter)](#heading-pièges-courants-et-comment-les-éviter)
    
* [FAQs](#heading-faqs)
    
    * [Puis-je annuler plus d'une migration à la fois ?](#heading-puis-je-annuler-plus-d-une-migration-à-la-fois)
        
    * [Comment savoir quels noms de migration utiliser ?](#heading-comment-savoir-quels-noms-de-migration-utiliser)
        
    * [Est-il sûr d'annuler des migrations ?](#heading-est-il-sûr-d-annuler-des-migrations)
        
* [Ressources supplémentaires](#heading-ressources-supplementaires)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'une migration dans Django ?

Avant de parler de l'annulation d'une migration, assurons-nous que nous sommes sur la même longueur d'onde.

Une migration dans Django est un enregistrement des changements apportés à votre base de données. Elle suit les modèles que vous avez ajoutés ou modifiés, et applique ces changements à votre base de données réelle en utilisant SQL (en arrière-plan).

Vous créez généralement une migration avec cette commande :

```bash
python manage.py makemigrations
```

Et vous l'appliquez comme ceci :

```bash
python manage.py migrate
```

C'est à ce moment-là que Django met à jour vos tables de base de données pour qu'elles correspondent à vos modèles.

Maintenant, que faire si vous voulez annuler cette dernière étape ?

## Comment annuler une migration dans Django

Très bien, voici la partie principale. Disons que vous venez d'exécuter une migration et que vous voulez l'annuler. Il y a deux situations :

1. **Vous avez déjà appliqué la migration et vous voulez la inverser**
    
2. **Vous ne l'avez pas encore appliquée et vous voulez simplement la supprimer**
    

Occupons-nous des deux.

### Cas 1 : Annuler une migration déjà appliquée

Si vous avez déjà exécuté `python manage.py migrate`, Django a modifié votre base de données.

Pour inverser cette migration, utilisez ceci :

```bash
python manage.py migrate votre_nom_d_app nom_de_la_migration_précédente
```

Permettez-moi de décomposer cela :

* `votre_nom_d_app` est le nom de votre application Django (comme `blog`, `users`, ou `store`)
    
* `nom_de_la_migration_précédente` est le nom de la migration *avant* celle que vous voulez annuler
    

Passons par un exemple.

Supposons que vous avez ces migrations pour une application appelée `store` :

```python
0001_initial.py  
0002_add_price_to_product.py  
0003_change_price_field.py  
```

Si vous voulez annuler la migration `0003_change_price_field.py`, vous exécuteriez :

```bash
python manage.py migrate store 0002
```

Cela indique à Django de revenir à la migration `0002`, annulant ainsi tout ce qui est dans `0003`.

Une fois cela fait, vous verrez une sortie comme :

```python
Opérations à inverser :
   - Modifier le champ price sur product
```

Et votre base de données est revenue à l'état où elle était avant `0003`.

### Cas 2 : Annuler une migration non encore appliquée

Peut-être avez-vous exécuté `makemigrations`, mais pas `migrate`. Donc vous avez simplement créé le fichier de migration et n'avez pas encore touché à la base de données.

Dans ce cas, vous pouvez supprimer en toute sécurité le fichier de migration.

Allez simplement dans le dossier `migrations/` de votre application, et supprimez le fichier de migration indésirable (par exemple : `0003_change_price_field.py`).

Ensuite, vous pouvez réexécuter `makemigrations` avec les modifications correctes.

Conseil rapide : Ne supprimez pas `__init__.py` ou le fichier `0001_initial.py` sauf si vous savez ce que vous faites. Ce premier fichier est généralement requis.

## Cas particulier : Annuler toutes les migrations (Tout réinitialiser)

Parfois, vous voulez simplement effacer toutes les migrations et recommencer.

C'est courant lorsque vous êtes encore en développement, et que la structure de votre base de données est désordonnée.

Voici comment je procède généralement :

1. **Supprimez les fichiers de migration** à l'intérieur du dossier `migrations/` de votre application (sauf pour `__init__.py`)
    
2. **Supprimez la base de données** ou videz simplement les tables si vous utilisez SQLite ou une base de données de test
    
3. Exécutez :
    

```bash
python manage.py makemigrations
python manage.py migrate
```

Si vous utilisez SQLite, vous pouvez également simplement supprimer le fichier `.sqlite3` et recommencer.

Pour PostgreSQL ou MySQL, vous devrez supprimer et recréer la base de données, ou la réinitialiser en utilisant un outil comme `pgAdmin` ou `DBeaver`.

## Scénario d'exemple : Corriger une migration cassée

Supposons que vous avez ajouté un nouveau champ à un modèle :

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
```

Vous avez fait une faute de frappe :

```python
price = models.DecimalField(max_digits=6, decimal_places=2, default='free')
```

Oups. Django vous permet de faire ceci :

```bash
python manage.py makemigrations store
python manage.py migrate
```

Puis cela casse.

Vous pouvez corriger cela en revenant en arrière :

```bash
python manage.py migrate store 0001
```

Ensuite, corrigez la faute de frappe dans votre modèle et exécutez :

```bash
python manage.py makemigrations
python manage.py migrate
```

Vous êtes de nouveau sur la bonne voie !

## Pièges courants (Et comment les éviter)

* **Ne supprimez pas simplement une migration sans l'avoir inversée au préalable**. Cela peut confondre Django.
    
* **Vérifiez toujours quelles migrations sont appliquées** en utilisant :
    

```bash
python manage.py showmigrations
```

* **Gardez des sauvegardes de votre base de données**, surtout en production. Utilisez des outils comme `pg_dump` ou `mysqldump` si nécessaire.
    
* **Ne réinitialisez pas les migrations dans une application en production** sauf si vous y êtes absolument obligé. Cela peut perturber les données de production.
    

## FAQs

### Puis-je annuler plus d'une migration à la fois ?

Oui ! Vous revenez simplement à la migration *avant* celles que vous voulez annuler.

**Exemple :**

Vous avez appliqué :

```python
[X] 0001_initial  
[X] 0002_add_price_to_product  
[X] 0003_change_price_field  
[X] 0004_add_discount_field
```

Pour annuler à la fois `0004` et `0003`, exécutez :

```python
python manage.py migrate store 0002
```

Cela annule à la fois 0004 et 0003, ne laissant que 0001 et 0002 appliquées.

### **Comment savoir quels noms de migration utiliser ?**

Exécutez `python manage.py showmigrations` et vous verrez une liste comme :

```python
 [X] 0001_initial
 [X] 0002_add_price_to_product
 [X] 0003_change_price_field
```

Le `[X]` montre les migrations appliquées. Pour annuler `0003`, revenez à `0002`.

### **Est-il sûr d'annuler des migrations ?**

Oui, tant que vous n'avez pas apporté de modifications aux données qui dépendent de la migration. Testez toujours en développement avant d'essayer en production.

## Conclusion

Annuler des migrations dans Django n'est pas effrayant une fois que vous avez le coup de main. C'est comme utiliser l'annulation dans un document Word, vous devez simplement savoir jusqu'où revenir en arrière.

Maintenant que vous savez comment annuler une migration dans Django, quel est le problème de migration le plus délicat que vous avez rencontré et comment l'avez-vous résolu ?

Envoyez-moi un [message](http://x.com/_udemezue/) - J'adorerais entendre votre histoire.

### Ressources supplémentaires

* [Documentation officielle sur les migrations Django](https://docs.djangoproject.com/en/stable/topics/migrations/)
    
* [Primer sur les migrations Django par RealPython](https://realpython.com/django-migrations-a-primer/)
    
* [Erreurs courantes dans Django et comment les éviter](https://adamj.eu/tech/2021/04/27/django-migrations-dos-and-donts/)