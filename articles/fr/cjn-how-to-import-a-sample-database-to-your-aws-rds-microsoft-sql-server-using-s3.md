---
title: Comment importer une base de données d'exemple dans votre AWS RDS Microsoft
  SQL Server en utilisant S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T10:13:35.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-3.12.23-AM.png
tags:
- name: mssql
  slug: mssql-2
- name: Azure
  slug: azure
- name: Backup
  slug: backup
- name: database
  slug: database
- name: S3
  slug: s3
seo_title: Comment importer une base de données d'exemple dans votre AWS RDS Microsoft
  SQL Server en utilisant S3
seo_desc: 'By Clark Jason Ngo

  This guide was created because it was so hard to find a way to play around with
  a sample database using AWS RDS MSSQL Server. I hope you find this helpful.

  If you haven''t set up your AWS RDS Microsoft SQL Server and Azure Data Stud...'
---

Par Clark Jason Ngo

Ce guide a été créé car il était si difficile de trouver un moyen de manipuler une base de données d'exemple en utilisant AWS RDS MSSQL Server. J'espère que vous trouverez cela utile.

Si vous n'avez pas encore configuré votre AWS RDS Microsoft SQL Server et Azure Data Studio, consultez d'abord ce guide : _[Comment connecter votre AWS RDS Microsoft SQL Server en utilisant Azure Data Studio](https://www.freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio/)_.

Nous allons aborder les technologies présentées ci-dessous :  


![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-244.png)

* Base de données : AWS RDS Microsoft SQL Server Express Edition
* Outil de base de données et GUI : Azure Data Studio
* Copie de sauvegarde de la base de données d'exemple : Amazon S3 Bucket



## Copie de sauvegarde de la base de données d'exemple AdventureWorks

Pour obtenir les téléchargements OLTP de AdventureWorks, allez sur ce [lien](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15) et choisissez n'importe quelle base de données d'exemple. Dans mon exemple, j'ai choisi `AdventureWorks2017.bak`. Nous allons télécharger cela dans le S3 Bucket.

## Amazon S3 Bucket

### Création du S3 Bucket

1. Créez un bucket. Vous pouvez choisir n'importe quel nom de bucket (exemple : votrenom-sample-dbs).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-202.png)



2. Assurez-vous que la région est la même que celle de l'instance AWS RDS. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-203.png)

3. Cochez les cases suivantes :

* Bloquer l'accès public aux buckets et objets accordé via les _nouvelles_ listes de contrôle d'accès (ACL)
* Bloquer l'accès public et les objets accordés via _toute_ liste de contrôle d'accès (ACL)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-204.png)

4. Accédez à nouveau à votre bucket en cliquant sur le bucket que vous avez créé.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-205.png)

### Téléchargement du fichier vers le bucket S3

1. Cliquez sur **Télécharger**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-206.png)

2. Choisissez le fichier de sauvegarde de la base de données. Par exemple : `AdventureWorks2017.bak`. Continuez à choisir **Suivant** et choisissez **Télécharger** dans la section Révision.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-207.png)

3. Mettez à jour votre Stratégie de Bucket pour permettre l'accès à votre Bucket S3. Notez que votre ARN sera différent du mien. Cliquez sur **Enregistrer** ensuite.

```json
{
    "Version": "2012-10-17",
    "Id": "Policy1548223592786",
    "Statement": [
        {
            "Sid": "Stmt1548223591553",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::changethis/*"
        }
    ]
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-208.png)



## AWS RDS - MSSQL Server Express  


### Création d'un Groupe d'options pour votre instance RDS

1. Cliquez sur **Groupes d'options**,

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-194.png)

2. Créez un groupe d'options. Choisissez n'importe quel nom et description. Pour le Moteur, il doit correspondre à votre instance RDS. Dans mon exemple, j'ai utilisé SQL Server Express Edition donc je choisis `sqlserver-ex`.

Voici les Moteurs suivants et leurs abréviations :

* SQL Server Enterprise Edition : `sqlserver-ee`
* SQL Server Standard Edition : `sqlserver-se`
* SQL Server Web Edition : `sqlserver-web`
* SQL Server Express Edition : `sqlserver-ex`

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-195.png)

3. Une fois que vous avez créé le groupe d'options, vous devrez **Ajouter une option**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-199.png)

4. Choisissez **SQLSERVER_BACKUP_RESTORE** pour le nom de votre option. Pour le rôle IAM, il est préférable de créer un nouveau rôle.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-200.png)

5. Choisissez le bucket S3 où votre fichier de base de données est hébergé. Pour la planification, choisissez **Immédiatement**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-201.png)

6. Retournez à votre instance AWS RDS MSSQL Server et cliquez sur **Modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-196.png)

7. Choisissez le groupe d'options créé avec `sql-server-express-backup`, puis cliquez sur Continuer.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-197.png)

8. Choisissez **Appliquer immédiatement** pour la planification des modifications. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-198.png)

9. Retournez à la page de votre instance AWS RDS MSSQL Server et faites défiler vers le bas pour modifier _Gérer les rôles IAM_. Ajoutez le rôle IAM que vous avez créé dans S3. Pour la Fonctionnalité, choisissez **S3_INTEGRATION**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-210.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-211.png)

## Azure Data Studio

### Importation de la base de données d'exemple dans le bucket S3 via la fonction de restauration

1. Dans votre AWS RDS MSSQL Server connecté, créez une nouvelle requête et tapez ce qui suit :

```sql
exec msdb.dbo.rds_restore_database 
@restore_db_name='AdventureWorks-test', 
@s3_arn_to_restore_from='arn:aws:s3:::clark-sample-dbs/AdventureWorks2017.bak';
```



![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-209.png)

Actualisez votre Azure Data Studio. Essayez également de redémarrer l'application si votre base de données n'est pas apparue ou si vous n'avez pas la permission d'y accéder.

Vous avez terminé ! Bon travail ! 🎉

Ressources :

* [https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/](https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/)

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-243.png)