---
title: How to Use Transactions in MongoDB to Prevent Inconsistencies in Your Java
  Code
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
seo_title: null
seo_desc: "By Haritha Yahathugoda\nThe Latest MongoDB version 4.2 introduced multi-document\
  \ transactions. This was a key feature that was missing from most NoSQL databases\
  \ (and which SQL DBs bragged about). \nA transaction, which can be composed of one\
  \ or more op..."
---

By Haritha Yahathugoda

The Latest MongoDB version 4.2 introduced [multi-document transactions](https://docs.mongodb.com/v4.2/core/transactions/). This was a key feature that was missing from most NoSQL databases (and which SQL DBs bragged about). 

A transaction, which can be composed of one or more operations, acts as an atomic operation. If all sub-operations succeed, that transaction is considered to be completed. Otherwise it fails. 

This is called atomicity. This is an important concept to understand to keep your data consistent when reading/writing data concurrently.

## Article Scope And Goals

The goal of this article is to present you with a real life example where data inconsistencies occur without transactions. Then we will build a solution in Java using MongoDB Transactions to prevent them. 

By doing so, you will learn to:

1. Avoid [Race Conditions](https://en.wikipedia.org/wiki/Race_condition) that could result in data inconsistencies
2. Build more resilient applications by using Mongo's build-in Retryable Writes

Also, I added one wrapper function, `static <R> R withTransaction(final Function<ClientSession, R> executeFn);`,  that you can use to improve code readability. 

## Example: How to Handle Concurrent Transactions Against the Same Bank Account 

Assume you and your spouse share a joint bank account. Each of you goes to the ATM at the same time and starts withdrawing money. 

```markdown
t1 -> You: Press check balance. ATM shows 100 dollars
t2 -> Spouse: Press check balance. ATM shows 100 dollars
t3 -> You & Spouse: withdraw 10 dollars
t4 -> Bank: initializes P1 and P2 to handle your and your spouse's requests.
t5 -> P1 and P2 checked the balance and saw 100 dollars
t6 -> P1 and P2 subtracted 10 dollars from the balance
t7 -> P1 updated the DB with the new balance of 90
t8 -> P2 updated the DB with the new balance of 90
```

In the above example, operations did not occur sequentially. The bank's process P2 did not wait for P1 to complete its tasks. If the bank had waited for P1 to finish reading the balance, calculating the new balance, and writing the updated balance back to the DB before it reading the most up to date balance, it wouldn't have lost 10 dollars.

The solution to this problem is **transactions**. You can think of them as somewhat similar to [Locks](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/concurrent/locks/package-summary.html), Semaphores, and Synchronized blocks in Java. In Java, it guarantees that only the Lock holder executes the code protected by a lock.

## How to Set Up Helper Functions

Now let's get to the coding part. I'm going to assume you already have a MongoClient setup. You will need [Java Mongo Driver 3.8 or higher](https://mongodb.github.io/mongo-java-driver/4.0/whats-new/#what-s-new-in-3-8).

```java
final static MongoClient client; // assumed you initialized this somewhere

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

`getNewClientSession` simply returns a session for a transaction. `ClientSession` is an identifier for a particular transaction. This is an important piece of data that you pass into all following Mongo operations so that it can isolate the operations. 

`getTransactionOptions` provides options for the Transaction. `ReadPreference.primary()` gives us the most up to date info on a cluster when we are reading data. `WriteConcern.MAJORITY` results in the DB acknowledging a commit after it successfully writes to the majority of the servers.

Instead of creating client sessions and transaction options everywhere, we should instead do it on a single method and just pass in the functions that need atomicity to it.

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

The above function runs operations inside a passed-in function, the `executeFn` argument, as an atomic operation or a transaction. Let's implement our money drawing function using transactions. 

Note that I am returning `null`. You could just throw a new exception to let the caller know that the transaction has failed. For the sake of this example, returning null implies transaction failure.

## Bank Account Example In Java

```java
public class Account {
	@BsonId
    ObjectId _id;
	int balance;
    
    ... getters and setters
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

In above code snippet, the `Account` class is a plain Java class model for  the user's account. `AccountService` is a database accessor for the accounts collection. The `drawCach` method completes the set of operations executed by a single process (P1 or P2) described in the first example to dispense money to either you or your spouse. 

Now we use this `withTransaction` function to call `drawCache`:

```java
... Some REST API 
AccountService accountService = ...; // Dependency injected

@Path('/account/withdraw') // Endpoint to withdraw money
withdrawMoney() {
	ObjectId accountId = ...// some method to get current users account ID
    Account account = withTransaction(new Function<ClientSession, Account>() {
        @Override
        public Workflow apply(ClientSession clientSession) {
        	// Everything inside this block run with in the same transaction as long as you pass the argument clientSession to mongo
            accountService.drawCash(clientSession, accountId, 10);
        }
    });

    if(Objects.isNull(account)){
        return "Failed to withdraw money";
    }
    return "New account balance is " + account.balance;
}
```

Now if you call this endpoint twice, concurrently, one user will see the final balance as 90 and the second one will see 80. 

You might have guessed that the second user's transaction should have failed. Yes, it did. But MongoDB has a built-in retry mechanism and it automatically retried our second operation again and succeeded.

## A Real-World Example Use Case

We use transactions on our [PS2PDF.com online video converter](https://www.ps2pdf.com/video-converter) to prevent one thread from overriding process states updated by another. 

For example, for each video convert process, we create a document called Job on the DB. It has a status field which can take values such as `STARTED`, `IN_PROGRESS`, and `COMPLETED`. 

Once the thread has updated the Job.status on the DB to `COMPLETED`, we don't want any slow thread reverting that message to `IN_PROGRESS`. Once a job has completed, it cannot be changed. 

We use the above mentioned `withTransaction` method to guarantee that no operation overrides the `COMPLETE` status.

## Conclusion

I hope you can now use transactions to avoid race conditions on your applications. Plus, use built-in `retryWrite` and `retryRead` to improve fault tolerance. 

I should point out that, MongoDB Transactions are pretty new, and there are articles out there that identify some inconsistencies that occur in special circumstances. But it is highly unlikely that you will run into these issues.

