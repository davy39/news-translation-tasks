---
title: 'Rails : Comment définir une contrainte d''index unique interchangeable'
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2019-07-15T10:50:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-unique-interchangeable-index-constraint-in-rails
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca178740569d1a4ca4ec3.jpg
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: 'Rails : Comment définir une contrainte d''index unique interchangeable'
seo_desc: Setting uniqueness validation in rails is something you’ll end up doing
  quite often. Perhaps, you even already added them to most of your apps. However,
  this validation only gives a good user interface and experience. It informs the
  user of the error...
---

Définir une validation d'unicité dans Rails est quelque chose que vous finirez par faire assez souvent. Peut-être avez-vous même déjà ajouté ces validations à la plupart de vos applications. Cependant, cette validation ne fait qu'offrir une bonne interface utilisateur et une bonne expérience. Elle informe l'utilisateur des erreurs empêchant les données d'être persistées dans la base de données.

### Pourquoi la validation d'unicité n'est pas suffisante

Même avec la validation d'unicité, des données indésirables sont parfois enregistrées dans la base de données. Pour plus de clarté, examinons un modèle d'utilisateur présenté ci-dessous :

```ruby
class User
    validates :username, presence: true, uniqueness: true
end
```

Pour valider la colonne username, Rails interroge la base de données avec SELECT pour vérifier si le username existe déjà. Si c'est le cas, il affiche « Username already exists ». Si ce n'est pas le cas, il exécute une requête INSERT pour persister le nouveau username dans la base de données.


![Image](https://lh5.googleusercontent.com/BXp1jq7tCUcP9meYKOz4G8fL_2hcEKK5roipT6sH7wugLhIizTFov8q37QTDTF0mNJtgI0QQm8vbrXaKq9JIQVq1hzcnBYYDr_Fy2KO6mEAR4fBfJy9uWoJ3VUu_JNxUYa0_ELfm)


Lorsque deux utilisateurs exécutent le même processus en même temps, la base de données peut parfois enregistrer les données malgré la contrainte de validation, et c'est là que les contraintes de base de données (index unique) interviennent.

Si l'utilisateur A et l'utilisateur B tentent tous deux de persister le même username dans la base de données en même temps, Rails exécute la requête SELECT. Si le username existe déjà, il informe les deux utilisateurs. Cependant, si le username n'existe pas dans la base de données, il exécute la requête INSERT pour les deux utilisateurs simultanément, comme illustré dans l'image ci-dessous.

![Image](https://lh3.googleusercontent.com/8-B6arsNFfdkLSkZbYt3F2KPPaFEbjAolPeDU9j3jMw3twF7r44uCum8dGNPGCduaLcX1E4n5QUTF4YUzPrPMI_QHyajoma8ULLyWo1aSYM5CJgu-1NEc3PDIuSpUFQvISE4Pu4y)


Maintenant que vous savez pourquoi l'index unique de la base de données (contrainte de base de données) est important, voyons comment le définir. Il est assez facile de définir un ou plusieurs index uniques de base de données pour une colonne ou un ensemble de colonnes dans Rails. Cependant, certaines contraintes de base de données dans Rails peuvent être délicates.

### Un rapide aperçu de la définition d'un index unique pour une ou plusieurs colonnes

C'est aussi simple que d'exécuter une migration. Supposons que nous avons une table users avec une colonne username et que nous voulons nous assurer que chaque utilisateur a un username unique. Vous créez simplement une migration et entrez le code suivant :

```ruby
add_index :users, :username, unique: true
```

Ensuite, vous exécutez la migration et c'est tout. La base de données garantit désormais qu'aucun username similaire n'est enregistré dans la table.

Pour plusieurs colonnes associées, supposons que nous avons une table requests avec les colonnes sender_id et receiver_id. De même, vous créez simplement une migration et entrez le code suivant :

```ruby
add_index :requests, [:sender_id, :receiver_id], unique: true
```

Et c'est tout ? *Oh oh, pas si vite.*

### Le problème avec la migration à colonnes multiples ci-dessus

Le problème est que les ids, dans ce cas, sont interchangeables. Cela signifie que si vous avez un sender_id de 1 et un receiver_id de 2, la table des demandes peut toujours enregistrer un sender_id de 2 et un receiver_id de 1, même s'ils ont déjà une demande en attente.

Ce problème se produit souvent dans une association autoréférentielle. Cela signifie que l'expéditeur et le destinataire sont tous deux des utilisateurs et que sender_id ou receiver_id est référencé à partir de user_id. Un utilisateur avec user_id(sender_id) de 1 envoie une demande à un utilisateur avec user_id(receiver_id) de 2.

Si le destinataire envoie une autre demande à nouveau, et que nous permettons de l'enregistrer dans la base de données, alors nous avons deux demandes similaires des mêmes deux utilisateurs (expéditeur et destinataire || destinataire et expéditeur) dans la table des demandes.

Cela est illustré dans l'image ci-dessous :

![Image](https://lh3.googleusercontent.com/9VNqmd8nuvhxKqJ3nVoZKS5ke1y5K-m6wQ7N5r8NPLSFYUnv3yeoMH2afGj89sGtsEhk3zsJbI30pB2WsgOOF1Xiijtqmv3mqbi1PxDzkIoQM0sfXGLZjcSTRrrIUTamG9RqGzEM)

### La solution courante

Ce problème est souvent résolu avec le pseudo-code suivant :

```ruby
def force_record_conflict
    # 1. Retourne s'il existe déjà une demande de l'expéditeur au destinataire
    # 2. Sinon, échange l'expéditeur et le destinataire
end
```

Le problème avec cette solution est que receiver_id et sender_id sont échangés à chaque fois avant d'être enregistrés dans la base de données. Par conséquent, la colonne receiver_id devra enregistrer le sender_id et vice versa.

Par exemple, si un utilisateur avec sender_id de 1 envoie une demande à un utilisateur avec receiver_id de 2, la table des demandes sera comme illustré ci-dessous :

![Image](https://lh3.googleusercontent.com/FhGRXh1uZOdxMsL1CvfKsM82kazpp_smHl7LkxNHpoxCxX6sChTbve5lQAotyW0WsqEITf7Ddc3C2XYG2-wwppSW4glymJqgPu4JmbiU1uxXR52c7EvWft73UHGf5-1gfmNW4ziC)


Cela peut ne pas sembler être un problème, mais il est préférable que vos colonnes enregistrent exactement les données que vous souhaitez qu'elles enregistrent. Cela présente de nombreux avantages. Par exemple, si vous devez envoyer une notification au destinataire via le receiver_id, vous interrogerez alors la base de données pour l'id exact à partir de la colonne receiver_id. Cela devient déjà plus confus dès que vous commencez à échanger les données enregistrées dans votre table des demandes.

### La solution appropriée

Ce problème peut être entièrement résolu en communiquant directement avec la base de données. Dans ce cas, je vais expliquer en utilisant PostgreSQL. Lors de l'exécution de la migration, vous devez vous assurer que la contrainte unique vérifie à la fois (1,2) et (2,1) dans la table des demandes avant d'enregistrer.

Vous pouvez le faire en exécutant une migration avec le code suivant :

```ruby
class AddInterchangableUniqueIndexToRequests < ActiveRecord::Migration[5.2]
    def change
        reversible do |dir|
            dir.up do
                connection.execute(%q(
                    create unique index index_requests_on_interchangable_sender_id_and_receiver_id on requests(greatest(sender_id,receiver_id), least(sender_id,receiver_id));
                    create unique index index_requests_on_interchangable_receiver_id_and_sender_id on requests(least(sender_id,receiver_id), greatest(sender_id,receiver_id));
                ))
            end

            dir.down do
                connection.execute(%q(
                    drop index index_requests_on_interchangable_sender_id_and_receiver_id;
                    drop index index_requests_on_interchangable_receiver_id_and_sender_id;
                ))
            end    
        end
    end
end
```

### Explication du code

Après avoir créé le fichier de migration, le `reversible` est utilisé pour s'assurer que nous pouvons revenir en arrière dans notre base de données lorsque nous devons le faire. Le `dir.up` est le code à exécuter lorsque nous migrons notre base de données et `dir.down` s'exécutera lorsque nous annulerons la migration ou reviendrons en arrière dans notre base de données.

`connection.execute(%q(...))` est utilisé pour indiquer à Rails que notre code est en PostgreSQL. Cela aide Rails à exécuter notre code en tant que PostgreSQL.

Puisque nos "ids" sont des entiers, avant d'enregistrer dans la base de données, nous vérifions si le plus grand et le plus petit (2 et 1) sont déjà dans la base de données en utilisant le code suivant :

```ruby
requests(greatest(sender_id,receiver_id), least(sender_id,receiver_id))
```

Ensuite, nous vérifions également si le plus petit et le plus grand (1 et 2) sont dans la base de données en utilisant :

```ruby
requests(least(sender_id,receiver_id), greatest(sender_id,receiver_id)) 
```

La table des demandes sera alors exactement comme nous l'entendons, comme illustré dans l'image ci-dessous :

![Image](https://lh5.googleusercontent.com/LHiuQRNBeyui8vuXx1hMWZfzVOBBkccmnFUml2A4kehPHg1xcpC35LsRan_8oggdmYH0zvBardwpIXHWDA-hiFTH4Grd7D6tejAATSJZLpS0l1aLig00KD8NUx7yrtTmICD1C0tI)

Et c'est tout. Bon codage !

### Références :

[Edgeguides](https://edgeguides.rubyonrails.org/active_record_validations.html#uniqueness) | [Thoughtbot](https://thoughtbot.com/blog/the-perils-of-uniqueness-validations)