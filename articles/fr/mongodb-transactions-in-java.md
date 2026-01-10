---
title: Comment utiliser les transactions dans MongoDB pour éviter les incohérences
  dans votre code Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T06:33:00.000Z'
originalURL: https://freecodecamp.org/news/mongodb-transactions-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ff9296a75d5f706921ca9ae.jpg
tags:
- name: database
  slug: database
- name: Java
  slug: java
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
seo_title: Comment utiliser les transactions dans MongoDB pour éviter les incohérences
  dans votre code Java
seo_desc: "By Haritha Yahathugoda\nThe Latest MongoDB version 4.2 introduced multi-document\
  \ transactions. This was a key feature that was missing from most NoSQL databases\
  \ (and which SQL DBs bragged about). \nA transaction, which can be composed of one\
  \ or more op..."
---

Par Haritha Yahathugoda

La dernière version de MongoDB, la 4.2, a introduit les [transactions multi-documents](https://docs.mongodb.com/v4.2/core/transactions/). Il s'agissait d'une fonctionnalité clé qui manquait à la plupart des bases de données NoSQL (et dont les bases de données SQL se vantaient). 

Une transaction, qui peut être composée d'une ou plusieurs opérations, agit comme une opération atomique. Si toutes les sous-opérations réussissent, cette transaction est considérée comme terminée. Sinon, elle échoue. 

Cela s'appelle l'atomicité. Il s'agit d'un concept important à comprendre pour maintenir la cohérence de vos données lors de la lecture/écriture de données de manière concurrente.

## Portée et objectifs de l'article

Le but de cet article est de vous présenter un exemple concret où des incohérences de données se produisent sans transactions. Ensuite, nous construirons une solution en Java en utilisant les transactions MongoDB pour les prévenir. 

En faisant cela, vous apprendrez à :

1. Éviter les [Conditions de Course](https://en.wikipedia.org/wiki/Race_condition) qui pourraient entraîner des incohérences de données
2. Construire des applications plus résilientes en utilisant les écritures re-essayables intégrées de Mongo

De plus, j'ai ajouté une fonction wrapper, `static <R> R withTransaction(final Function<ClientSession, R> executeFn);`, que vous pouvez utiliser pour améliorer la lisibilité du code. 

## Exemple : Comment gérer les transactions concurrentes sur le même compte bancaire 

Supposons que vous et votre conjoint partagez un compte bancaire joint. Chacun de vous va au distributeur automatique au même moment et commence à retirer de l'argent. 

```markdown
t1 -> Vous : Appuyez sur vérifier le solde. Le distributeur montre 100 dollars
t2 -> Conjoint : Appuyez sur vérifier le solde. Le distributeur montre 100 dollars
t3 -> Vous et votre conjoint : retirez 10 dollars
t4 -> Banque : initialise P1 et P2 pour traiter vos demandes et celles de votre conjoint.
t5 -> P1 et P2 ont vérifié le solde et ont vu 100 dollars
t6 -> P1 et P2 ont soustrait 10 dollars du solde
t7 -> P1 a mis à jour la base de données avec le nouveau solde de 90
t8 -> P2 a mis à jour la base de données avec le nouveau solde de 90
```

Dans l'exemple ci-dessus, les opérations ne se sont pas déroulées de manière séquentielle. Le processus P2 de la banque n'a pas attendu que P1 termine ses tâches. Si la banque avait attendu que P1 finisse de lire le solde, de calculer le nouveau solde et d'écrire le solde mis à jour dans la base de données avant de lire le solde le plus à jour, elle n'aurait pas perdu 10 dollars.

La solution à ce problème est les **transactions**. Vous pouvez les considérer comme quelque peu similaires aux [Verrous](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/concurrent/locks/package-summary.html), aux sémaphores et aux blocs synchronisés en Java. En Java, cela garantit que seul le détenteur du verrou exécute le code protégé par un verrou.

## Comment configurer les fonctions d'assistance

Passons maintenant à la partie codage. Je vais supposer que vous avez déjà configuré un MongoClient. Vous aurez besoin du [Pilote Java Mongo 3.8 ou supérieur](https://mongodb.github.io/mongo-java-driver/4.0/whats-new/#what-s-new-in-3-8).

```java
final static MongoClient client; // supposé que vous l'avez initialisé quelque part

public static ClientSession getNewClientSession() {
    return client.startSession();
}

public static TransactionOptions getTransactionOptions() {
    return TransactionOptions.builder()
        .readPreference(ReadPreference.primary())
        .readConcern(ReadConcern.LOCAL)
        .writeConcern(WriteConcern.MAJORITY)
        .build();
}


```

`getNewClientSession` retourne simplement une session pour une transaction. `ClientSession` est un identifiant pour une transaction particulière. Il s'agit d'une donnée importante que vous passez à toutes les opérations Mongo suivantes afin qu'elles puissent isoler les opérations. 

`getTransactionOptions` fournit des options pour la transaction. `ReadPreference.primary()` nous donne les informations les plus à jour sur un cluster lorsque nous lisons des données. `WriteConcern.MAJORITY` entraîne la confirmation par la base de données d'un commit après qu'elle a écrit avec succès sur la majorité des serveurs.

Au lieu de créer des sessions client et des options de transaction partout, nous devrions plutôt le faire dans une seule méthode et simplement passer les fonctions qui nécessitent l'atomicité.

```java
static <R> R withTransaction(final Function<ClientSession, R> executeFn) {
	final ClientSession clientSession = getNewClientSession();
	TransactionOptions txnOptions = this.getTransactionOptions();
       
	TransactionBody<R> txnBody = new TransactionBody<R>() {
		public R execute() {
			return executeFn.apply(clientSession);
		}
	};

	try {
		return clientSession.withTransaction(txnBody, txnOptions);
	} catch (RuntimeException e) {
		e.printStackTrace();
	} finally {
		clientSession.close();
	}
	return null;
}
```

La fonction ci-dessus exécute les opérations à l'intérieur d'une fonction passée en argument, l'argument `executeFn`, en tant qu'opération atomique ou transaction. Implémentons notre fonction de retrait d'argent en utilisant des transactions. 

Notez que je retourne `null`. Vous pourriez simplement lancer une nouvelle exception pour informer l'appelant que la transaction a échoué. Pour les besoins de cet exemple, retourner null implique un échec de la transaction.

## Exemple de compte bancaire en Java

```java
public class Account {
	@BsonId
    ObjectId _id;
	int balance;
    
    ... getters et setters
}

public class AccountService {
	public Collection<Account> getAccounts() {
    	return dbClient.getCollection('account', Account.class);
    }
    
    private Account currentBalance(ClientSession session, Bson accountId) {
    	return getAccounts().findOne(session, Filters.eq('_id', accountId)).first();
    }
    
	private int currentBalance(ClientSession session, Bson accountId) {
    	Account account = getAccounts().findOne(session, Filters.eq('_id', accountId)).first();
        return account.balance;
    }
    
    private int updateBalance(ClientSession session, Bson accountId, int newBalance) {
    	Account account = getAccounts().updateOne(session, Filters.eq('_id', accountId), Updates.set('balance', newBalance)).first();
        return account.balance;
    }
    
    public Account drawCash(ClientSession session, Bson accountId, int amount){
    	int currentBalance = this.currentBalance(accountId);
        int newBalance = currentBalance - amount;
        return updateBalance(session, accountId, amount);
    }
}
```

Dans l'extrait de code ci-dessus, la classe `Account` est un modèle de classe Java simple pour le compte de l'utilisateur. `AccountService` est un accesseur de base de données pour la collection de comptes. La méthode `drawCash` complète l'ensemble des opérations exécutées par un seul processus (P1 ou P2) décrit dans le premier exemple pour distribuer de l'argent à vous ou à votre conjoint. 

Maintenant, nous utilisons cette fonction `withTransaction` pour appeler `drawCash` :

```java
... Une API REST
AccountService accountService = ...; // Injection de dépendance

@Path('/account/withdraw') // Point de terminaison pour retirer de l'argent
withdrawMoney() {
	ObjectId accountId = ...// une méthode pour obtenir l'ID de compte de l'utilisateur actuel
    Account account = withTransaction(new Function<ClientSession, Account>() {
        @Override
        public Workflow apply(ClientSession clientSession) {
        	// Tout ce qui se trouve à l'intérieur de ce bloc s'exécute dans la même transaction tant que vous passez l'argument clientSession à mongo
            accountService.drawCash(clientSession, accountId, 10);
        }
    });

    if(Objects.isNull(account)){
        return "Échec du retrait d'argent";
    }
    return "Le nouveau solde du compte est " + account.balance;
}
```

Maintenant, si vous appelez ce point de terminaison deux fois, de manière concurrente, un utilisateur verra le solde final comme étant 90 et le second verra 80. 

Vous avez peut-être deviné que la transaction du second utilisateur aurait dû échouer. Oui, c'est le cas. Mais MongoDB dispose d'un mécanisme de nouvelle tentative intégré et il a automatiquement réessayé notre deuxième opération et a réussi.

## Un cas d'utilisation d'exemple dans le monde réel

Nous utilisons des transactions sur notre [convertisseur vidéo en ligne PS2PDF.com](https://www.ps2pdf.com/video-converter) pour empêcher un thread de remplacer les états de processus mis à jour par un autre. 

Par exemple, pour chaque processus de conversion vidéo, nous créons un document appelé Job sur la base de données. Il possède un champ de statut qui peut prendre des valeurs telles que `STARTED`, `IN_PROGRESS` et `COMPLETED`. 

Une fois que le thread a mis à jour le Job.status sur la base de données à `COMPLETED`, nous ne voulons pas qu'un thread lent revienne à `IN_PROGRESS`. Une fois qu'un travail est terminé, il ne peut plus être modifié. 

Nous utilisons la méthode `withTransaction` mentionnée ci-dessus pour garantir qu'aucune opération ne remplace le statut `COMPLETE`.

## Conclusion

J'espère que vous pouvez maintenant utiliser les transactions pour éviter les conditions de course dans vos applications. De plus, utilisez les fonctions intégrées `retryWrite` et `retryRead` pour améliorer la tolérance aux pannes. 

Je devrais souligner que les transactions MongoDB sont assez récentes, et il existe des articles qui identifient certaines incohérences qui se produisent dans des circonstances spéciales. Mais il est très peu probable que vous rencontriez ces problèmes.