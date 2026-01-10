---
title: How to Build an LSM Tree Storage Engine from Scratch – Full Handbook
subtitle: ''
author: Ramesh Sinha
co_authors: []
series: null
date: '2025-12-18T20:25:02.609Z'
originalURL: https://freecodecamp.org/news/build-an-lsm-tree-storage-engine-from-scratch-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766089431510/433ff03f-8aca-4a87-82d3-0b6d6c1f371c.png
tags:
- name: Databases
  slug: databases
- name: lsmtree
  slug: lsmtree
- name: storage solutions
  slug: storage-solutions
- name: Go Language
  slug: go
- name: heap
  slug: heap
- name: handbook
  slug: handbook
seo_title: null
seo_desc: 'Databases are one of the most important parts of a software system. They
  allow us to store huge amounts of data in an organized way and retrieve it efficiently
  when we need it.

  In the early days, when the volume of data was relatively small, engineer...'
---

Databases are one of the most important parts of a software system. They allow us to store huge amounts of data in an organized way and retrieve it efficiently when we need it.

In the early days, when the volume of data was relatively small, engineers prioritized fast data retrieval and stored data in [B-tree structures](https://en.wikipedia.org/wiki/B-tree) that made searching efficient.

But over time, we started building systems that needed to ingest massive amounts of data like logs, metrics, likes, chats and tweets. This made it necessary to design a storage system that would make writing faster.

One such storage system is the LSM-tree (Log-Structured Merge tree).

In this tutorial, rather than immediately diving into the theoretical concepts of an LSM-Tree Storage system, I’ll take a practical, problem-driven approach. I believe that learning through solving problems is far more effective and engaging than simple memorization of concepts.

By approaching these ideas progressively, my goal is to guide you step by step through real-world engineering challenges and solutions, giving you a front-row seat to the intricacies of building a robust storage system from scratch.

We’ll begin by identifying real-world challenges that arise in database design – like handling write-heavy workloads, ensuring data durability, or managing efficient storage. These challenges will set the stage for each feature and component of LSM-Trees.

Through this method, we’ll explore the foundations of LSM-Tree storage systems and dive deeper into their key components: MemTable, SSTable, Write-Ahead Log (WAL), and Manifest File.

We’ll also examine the Write and Read paths, explore Durability and Crash-Recovery mechanisms, and conclude with one of the most critical processes: Compaction.

By the end of this handbook, you’ll understand not just what these components are but also why they are designed the way they are and how they solve the unique challenges of building modern, high-performance databases.

### **What We’ll Cover:**

1. [Prerequisites](#heading-prerequisites)
    
2. [What is an LSM Tree?](#heading-what-is-an-lsm-tree)
    
3. [Preface: Setting up to Build an LSM-Tree Database](#heading-preface-setting-up-to-build-an-lsm-tree-database)
    
    * [Initial Feature Set: Laying the Foundation of the Database System](#heading-initial-feature-set-laying-the-foundation-of-the-database-system)
        
    * [MemTable: In-Memory Data Storage](#heading-memtable-in-memory-data-storage)
        
    * [SSTable: Persisting Data for Durability](#heading-sstable-persisting-data-for-durability)
        
    * [The WAL (Write Ahead Log ): Crash Recovery Made Simple](#heading-the-wal-write-ahead-log-crash-recovery-made-simple)
        
    * [Manifest File: Tracking the State of the Database](#heading-manifest-file-tracking-the-state-of-the-database)
        
    * [Update and Delete: Handling Mutability in an Immutable System](#heading-update-and-delete-handling-mutability-in-an-immutable-system)
        
    * [Compaction: Cleaning Up Stale and Deleted Data](#heading-compaction-cleaning-up-stale-and-deleted-data)
        
4. [Conclusion](#heading-conclusion)
    
    * [Complete Code](#heading-complete-code)
        

## **Prerequisites**

While this tutorial is designed to be comprehensive and approachable, it’ll be helpful if you come in with some foundational knowledge in the following areas:

* **Programming in Golang**: Familiarity with Go syntax, error handling, and standard libraries (example `os,` `encoding/gob`, `container/heap`) will make it easier to work through the implementation examples.
    
* **Basic data structures and algorithms:** Concepts such as maps, heaps, some sorting algorithms, and early termination are leveraged throughout the tutorial.
    
* **Understanding persistent storage:** Awareness of the differences between in-memory and disk-based storage, as well as sequential versus random read/write operations will be helpful in grasping performance-related trade-offs.
    
* **General database knowledge:** If you're familiar with key-value databases or CRUD operations (Create, Read, Update, Delete), you’ll have a head start.
    
* **Concurrency**: Basic understanding of threads and concurrency.
    

While having experience in these areas will deepen your understanding of the concepts and reduce the learning curve, I will provide sufficient detail and practical explanations at every step ensuring you gain the insights necessary to follow along and build your own LSM-tree-based storage engine.

## What is an LSM Tree?

A log-structured merge-tree (or LSM tree) is a data structure that makes database writes super fast by recording new data in memory first, then periodically sorting and merging it into larger files on disk.

The “log” in its name refers to the fact that it saves data in a log-structured format (rather than simply storing it). We will come to what those logs are in a little bit.

LSM trees keep appending new data to the existing data, instead of looking for something that exists and updating it. In other words, you don't have to spend any CPU cycles thinking about where to store data – just append it at the end.

An LSM tree also has "tree" in its name, but does it actually store data in a tree? Not really. The “tree” here is mostly an abstract concept. It refers to the hierarchical organization of levels (L0, L1, L2, and so on), not a tree data structure with nodes and pointers. Again, we will come to those levels in a little bit, but for now, let’s just say it makes sense to call it a tree given that it stores data in a leveled fashion.

Just note that there isn't a tangible tree structure in play (like a binary trees or graph) – it’s not node-based storage.

Finally, there is the "merge" part of the name. For now, suffice it to say that you’ll soon see how this storage engine merges data to save storage by avoiding duplication.

Personally, I think that "Log-Structured Merge **System**" would be clearer than "tree," but "LSM tree" is the established term in the industry, so that's what we'll use.

## Preface: Setting up to Build an LSM-Tree Database

Now that we have set the context, lets put this theory into practice and start building our own LSM-tree-based database storage engine from scratch.

To follow along with this tutorial:

* Make sure you have Golang installed on your system. If not, you can download and install it from the [official Go website](https://go.dev/).
    
* Set up your development environment and create a new Go module for this project by running: `go mod init lsm-db`
    
* Keep a code editor or IDE ready to try out the examples.
    

### Initial Feature Set: Laying the Foundation of the Database System

When I’m designing or building a system, I like to think that the system already exists, and I assume that I can just start calling functions that support the features of the system. I’ll follow that pattern here and assume that the following functions of the LSM tree exist and we can invoke those functions from [main.go](http://main.go).

```go
db, err := NewDB[string, string](3, 3) // there is a feature to create new with some parameters we will get to
db.Put("a", "apple") // a feature to add key value
db.Delete("a") // a feature to delete a key
val, _ := db.Get("a") // a feature to get value given a key
```

As we progress through this journey, I’ll introduce essential features such as in-memory storage, flushing data to disk, and handling duplicate keys. We’ll also explore more advanced components, including a Write-Ahead Log (WAL) to ensure crash tolerance, a Manifest file to maintain the database state across application restarts, and a Compaction process to clean up redundant or stale data by merging older SSTables.

By the end of this tutorial, you will gain a clear understanding of how all these components work together to form a robust and efficient LSM-tree-based storage system.

### MemTable: In-Memory Data Storage

We’re building a database storage system, so of course you’ll need a way to store data. This means you need some kind of backing storage. This backing storage in an LSM tree is called a MemTable. The "Mem" refers to its in-memory storage. The benefit of in-memory storage is that it’s orders of magnitude faster than storing on disk.

For simplicity, at the core of the MemTable you can use a map (or dictionary depending on the programming language) as the underlying data structure to store key-value pairs. The map allows for fast lookups, insertions, and deletions, making it ideal for in-memory storage where performance is crucial. So the structure for MemTable will look like:

```go
type MemTable[K comparable, V any] struct {
    data map[K]V // this is primary storage map. It's generic so that you
                  // can store any kind of data
}
```

Above code defines a `MemTable` struct, where `data` is a map that acts as the main storage for our key-value pairs. Since the `data` field is a map, you’ll be able to quickly add, retrieve, or delete values associated with a given key.

You must have noticed something new in the code. The use of `<K comparable, V any>`. This syntax is Go’s **generic types** feature, which allows us to write flexible code that can handle different data types.

Generics are a way to write code that is independent of any specific data type. They allow you to write functions and data structures that can work with a string, int, float, or any custom type you define, without sacrificing type safety.

In the above code, K and V are type parameters. They say: "This MemTable can work with any Key type K that is comparable, and any value type V."

Now that you have the MemTable, think of what functions it should provide to its clients. Well, the clients need to be able to save and retrieve values associated with a key, so the following functions would fit naturally:

```go
func (m *MemTable[K, V]) Put(key K, value V) {
    m.data[key] = value
}

func (m *MemTable[K, V]) Get(key K) (V, bool) {
    value, ok := m.data[key]
    var zero V
    if !ok {
        return zero, false
    }
    return value, true
}
```

The above code has `Put` and a `Get` functions – let’s break them down:

* **Put**: This function allows the client to insert a key-value pair into the MemTable. If the key already exists in the map, its value will be updated with the new value provided as an argument. This is effectively the `write` operation of our key-value store.
    
* **Get**: This function is responsible for retrieving a value associated with a give key from the MemTable. It returns two values, the value itself (of type `V`) and a boolean (`true` or `false`). The boolean indicates whether the key was found in the map. If the key does not exist, the function return a `zero value` (more on that below) along with `false`.
    

Did you notice `var zero V`?

It's pretty interesting. Think of a situation where we don't get a value from the map – say the key is not there, or something else is wrong. What should the function `Get` return in that case? Can it return an int (0), or a string "Not found", or some random object (foo)? You don't know anything about the type yet (Generics), so you can't tell it what to return.

In this case, the compiler comes to the rescue. Go has this zero value concept: everything should have a zero value. An int has 0, string has "", bool has false, and pointer, slice, and map have nil. By saying `var zero V` you are telling the compiler, "I don't know the type yet, you figure out the type while compiling and put that type here as the return type." Neat!

I missed one thing though: how would a client invoke these functions? Right, we need a way to build the MemTable type.

To construct and initialize a MemTable, we can use a **factory function**: a common programming pattern for creating and returning new objects or instances without directly exposing the underlying implementation details.

```go
func NewMemTable[K comparable, V any]() *MemTable[K, V] {
    return &MemTable[K, V]{
        data: make(map[K]V),
    }
}
```

Notice how we’ve initialized the data field using the built-in `make` function. Here’s why we do this:

Go has a built-in function called `make`, which is used to allocate and initialize slices, maps, and channels. This allocation ensures that they are ready for use without the risk of runtime panics.

You might wonder, why not use the `new` function to allocate the map? After all, developers coming from other programming backgrounds (like C++ or Java) might expect to use `new` for all types of memory allocation. But Go **differentiates how it manages memory for composite types versus basic/numeric types**, and that’s where `make` comes in.

This distinction matters because the `new` function only **allocates memory** for an object and returns a *pointer* to that memory. The object itself is not initialized, meaning that while the memory is allocated, the map isn’t ready to use. If we try to perform operations (like adding a key-value pair) on a `map` only allocated using `new`, it will cause a runtime panic because the map wasn’t correctly initialized.

For example:

```go
m := new(map[string]int) // Allocates a pointer to an uninitialized map
(*m)["a"] = 1            // This will panic because the map is not initialized
```

On the other hand, `make` both allocates and **initializes the map**, ensuring it’s fully functional right away. That’s why the correct way to create a map is:

```go
m1 := make(map[string]int) // Initializes the map properly
m1["a"] = 1                // This works as expected
```

Now that you have the MemTable which can store data in memory, let's hook it up and use it.

But before that, do you remember at the beginning that I used functional invocations like `db.Put` and `db.Get`? Well, what is `db`? Because we are building a database storage system, it makes more sense to name the interface `db` instead of MemTable, right? And to be honest, it seems like MemTable is going to be part of the database system, not the whole system, doesn't it?

Even if it's not intuitive at the moment to define something like a DB type, let's just do it. Trust me, it will start to get clearer as we move along. This `db` type will wrap adding and retrieving data from MemTable.

```go
type DB[K comparable, V any] struct {
    memtable *MemTable[K, V]
}

// factory function for DB type
func NewDB[K comparable, V any]() (*DB[K, V], error) {
    memtable := NewMemTable[K, V]()
    return &DB[K, V]{
        memtable: memtable,
    }, nil
}
```

Let's just define the Put and Get functions which will invoke corresponding functions in MemTable:

```go
func (db *DB[K, V]) Put(key K, value V) error {
    db.memtable.Put(key, value)
    return nil
}

func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        return val, nil
    }
    var zero V
    return zero, errors.New("key not found")
}
```

Let's integrate whatever we’ve built so far and run it. To run add below code in main.go and run using `go run main.go`

```go
db, err := NewDB[string, string]()
if err != nil {
    log.Fatalf("Failed to create DB: %v", err)
}
db.Put("a", "apple")
val, _ := db.Get("a")
log.Printf("Get('a') = %s (should be 'apple')", val)
```

Look at that, you have built an in-memory database where your clients can store and fetch data from. It’s using generics so you can store any kind of values (int, string, objects).

Now say you shipped this solution and then it crashes. Your clients will lose all the data. Why will this crash? For one thing, memory is limited and at some point you’re going to run out of it. So there are two major problems with just in-memory storage:

1. It's not durable.
    
2. Unbounded memory usage is going to crash the system.
    

How do we solve these problems?

Here's a thought: what if we flush the MemTable data to disk at some regular interval? That way we can ensure that MemTable doesn't grow out of bounds. Also if the db crashes, we won’t lose all the data. We’ll still lose the data that hasn’t been flushed yet, but that's way better than losing all of it.

### SSTable: Persisting Data for Durability

An SSTable is a sorted string table. I wish they’d called it a "Secondary Storage" table, but historically keys and values were strings – hence sorted string table. An SSTable is a persistent, ordered, and immutable file that stores key-value pairs. It’s a file stored on disk, so it's pretty clear that it’s persistent (durable).

Let’s discuss a couple key features of the SSTable:

* **It’s ordered**: There is an incentive to store the keys in a sorted order, and it makes searching keys faster and efficient. If not for that, you'd have to scan the whole file to be able to find a key. Later, I will point out some code that leverages sorted storage.
    
* **It’s immutable**: Once an SSTable file is written, it can’t be modified. To update or delete a key, you must write a new record in a newer SSTable. This simplifies the design and makes reads and writes very predictable.
    

But wait, how does that simplify the design?

One of the most complex things in software engineering is dealing with concurrency. Let’s say you’re writing to a file and another thread updates it underneath. How do you know you have the correct data?

With immutable design, you don't have to worry about this at all. You are 100% confident that the data you are reading has not been altered by anybody else. I’ll take that as a massive simplification: you don't have to deal with locks, starvation, staleness, and so on.

#### How does it make the write path predictable?

I will answer this partially here and come back to it when we have completed some more implementation. You’ll see that every write in our code follows the exact same steps. There is not a single different condition or edge case.

In a traditional database (using a B-Tree), a typical write involves:

1. Finding the data on disk.
    
2. Reading the block of data from disk into memory.
    
3. Modifying the data in memory.
    
4. Writing the entire block back to disk.
    

The more steps, the more unpredictable performance can get, because the write can be fast if data is already in the memory cache or slow if there are multiple disk seeks needed.

Granted, our code is an overly simplified version, but the extension of this concept still stands true in real LSM implementations.

#### How does it make the read path predictable?

Read is predictable because any number of threads can read the same SSTable file at the same time without any problem, with full confidence that data has not been updated.

In contrast, when reading from a mutable data structure, you have to worry that another thread might be in the process of changing the data you are trying to read.

To prevent this, B-Tree-based databases use complex locking mechanisms, and that adds overhead and unpredictability.

I should raise a caution here: the Read in LSM tree storage is not always predictable. It can be faster if data is read from memory and it can be very slow if multiple SSTables need to be looked up to find the key.

Having said that, you don't have to worry about other performance bottlenecks because of locks. Meaning, in B-Tree storage, your read query can be slower because another write query is holding a lock. In simple low-concurrency use cases, you will mostly get amazing read performance from a B-Tree structure, but this advantage wears off as concurrency increases.

LSM tree was built for highly concurrent, write-heavy use cases, and at times slower reads are a trade-off.

The takeaway that gives you ammunition to design better is that B-trees are better for read-heavy workloads. Reads are generally faster and more consistent, but performance can have unpredictable outliers under high write concurrency due to locking.

An LSM tree is better for write-heavy workloads. Writes are much faster. Reads are generally slower and more variable, but their performance profile is more predictable under high write concurrency because there is no read-write locking.

Let's implement an SSTable to see how it works.

**The write path:**

```go
func writeSSTable[K comparable, V any](memtable *MemTable[K, V], path string) (*SSTable[K, V], error) {
    file, err := os.Create(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()
    
    pairs := make([]Pair[K, V], 0, len(memtable.data))
    for k, v := range memtable.data {
        pairs = append(pairs, Pair[K, V]{Key: k, Value: v})
    }
    
    sort.Slice(pairs, func(i, j int) bool {
        return any(pairs[i].Key).(string) < any(pairs[j].Key).(string)
    })
    
    encoder := gob.NewEncoder(file)
    for _, pair := range pairs {
        if err := encoder.Encode(pair); err != nil {
            return nil, err
        }
    }
    
    return &SSTable[K, V]{path: path}, nil
}
```

The following things are important to note from the above code:

1. `sort.Slice`: Remember I spoke about order earlier? So we store data in the SSTable in a sorted fashion, and we will see how we leverage it in the read path.
    
2. I have used the gob encoding package. An encoder makes life simpler for you because it streams the data to and from Go data structures to binary streams that can be stored on disk. It handles all the complexity of representing types, field names, and values in a standardized binary format, so that you don't have to.
    

**The read path:**

```go
func (s *SSTable[K, V]) Get(key K) (V, error) {
    file, err := os.Open(s.path)
    if err != nil {
        var zero V
        return zero, err
    }
    defer file.Close()
    
    decoder := gob.NewDecoder(file)
    
    for {
        var pair Pair[K, V]
        if err := decoder.Decode(&pair); err != nil {
            if err == io.EOF {
                break
            }
            var zero V
            return zero, err
        }
        
        // for simple comparison we are assuming key is just string
        keyInDB := any(pair.Key).(string)
        if keyInDB == any(key).(string) {
            if any(pair.Value).(string) == TOMBSTONE {
                var zero V
                return zero, ErrNotFound
            }
            return pair.Value, nil
        }
        
        if keyInDB > any(key).(string) {
            var zero V
            return zero, ErrNotFound
        }
    }
    
    var zero V
    return zero, ErrNotFound
}
```

On the read path, look at `keyInDB > any(key).(string)`. This is one of the examples of how we took advantage of storing data in a sorted key order. The moment we find a key in the SSTable **that is greater than the key** we are looking for, we stop looking because it’s obvious all other keys will be greater than this, so we won't find our key anymore.

Now that you have implemented the SSTable, you just have to decide when to flush data from the MemTable to the SSTable. You can just define max size for MemTable and flush it to disk on the write path when the max size is reached.

I am skipping some variables, boilerplate code, and simplifying things for brevity. I will post a GitHub link with the complete implementation later.

```go
type DB[K comparable, V any] struct {
    memtable        *MemTable[K, V]
    maxMemtableSize int
    memtableSize    int
    sstables        []*SSTable[K, V]
    sstableCounter  int
}

func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    sstables := make([]*SSTable[K, V], 0)
    memtable := NewMemTable[K, V]()
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        sstables:        sstables,
    }, nil
}

func (db *DB[K, V]) Put(key K, value V) error {
    db.memtable.Put(key, value)
    db.memtableSize++
    
    if db.memtableSize >= db.maxMemtableSize {
        if err := db.flushMemtable(); err != nil {
            return err
        }
    }
    
    return nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    return nil
}
```

You'll notice that every time we flush to disk, we write to a new SSTable versus using a single SSTable for the whole database. This is the immutability aspect we discussed earlier.

```go
func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        return val, nil
    }
    
    for i := len(db.sstables) - 1; i >= 0; i-- {
        sstable := db.sstables[i]
        val, err := sstable.Get(key)
        if err != nil {
            if err == ErrNotFound {
                continue
            }
            var zero V
            return zero, err
        }
        return val, nil
    }
    
    var zero V
    return zero, ErrNotFound
}
```

One important aspect to note on the read path is that we are reading the newest SSTable first. This is because the newest SSTable has the most updated value for the key.

So, say you have a key "a" with value "apple", and along the way you update that value for "a" to be "apricot". You'd have flushed it to a new SSTable (for immutability), and so if you were to read an older SSTable, first you'd get the older value. So by reading the newer SSTable first, we get the correct value and we don't have to worry about updating older SSTables.

### The WAL (Write Ahead Log ): Crash Recovery Made Simple

Now that we have an SSTable, our data is durable and we are safe from losing data upon crashes. Are we really safe, though? Think of a scenario where a crash happens before we flush to the SSTable. We know MemTable has a max threshold, and until then, data lives in memory. So we’re still prone to losing data if a crash happens before the flush.

This is where the WAL (Write Ahead Log) comes into the picture. It’s the single most important aspect of the LSM tree.

We’ll follow a simple rule: "Before we write a piece of data to the in-memory MemTable, we first write it to a log file on disk."

If a crash happens and the database starts again, the first thing it does is look for a WAL, read it if one is found, and replay all the data into MemTable. This process reconstructs the MemTable to the exact state it was in right before the crash.

It's natural to think that if all of your writes are first written to disk it will impact performance. You aren’t wrong, but at the same time there are nuances.

The writes to WAL are different in that they are append-only sequential writes, meaning random disk seeks are not required. On a traditional spinning hard drive (HDD), this is fast because the disk's read/write head does not have to move to a new location. On a modern solid-state drive (SSD), sequential writes are also much faster than random writes.

Whatever small performance impact we accept is a trade-off for durability.

Now that we know what WAL does, let's implement it. Two key functions of WAL are to write to a file on disk and replay MemTable upon start.

Note that in the factory function below (NewWAL), the file has been opened in append mode.

```go
func NewWAL[K comparable, V any](path string) (*WAL[K, V], error) {
    file, err := os.OpenFile(path, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        return nil, err
    }
    return &WAL[K, V]{
        file:    file,
        encoder: gob.NewEncoder(file),
    }, nil
}

func (wal *WAL[K, V]) Write(key K, value V) error {
    entry := WALEntry[K, V]{Key: key, Value: value}
    return wal.encoder.Encode(&entry)
}

func ReplayWAL[K comparable, V any](path string) (*MemTable[K, V], error) {
    memtable := NewMemTable[K, V]()
    file, err := os.Open(path)
    if err != nil {
        if os.IsNotExist(err) {
            // If the file doesn't exist, that's fine. Return an empty memtable.
            return memtable, nil
        }
        return nil, err
    }
    defer file.Close()
    
    decoder := gob.NewDecoder(file)
    for {
        var entry WALEntry[K, V]
        if err := decoder.Decode(&entry); err != nil {
            if err == io.EOF {
                break // We've reached the end of the file.
            }
            return nil, err
        }
        memtable.Put(entry.Key, entry.Value)
    }
    
    return memtable, nil
}
```

A couple notes about the above code:

* **NewWAL**: This function creates an instance of the WAL for our database. It takes in the file path where the WAL data should be stored and opens the file using Go’s `os.OpenFile` function. Also, a `gob.Encoder` is initialized to simplify the encoding of Go data structures into binary format for efficient storage in the WAL file.
    
* **Write**: The Write function appends a new key-value pair to the WAL file. Every write operation to the MemTable first calls this function to ensure the update is durably recorded:
    
* **ReplayWAL:** This is the most important function. In the event of crash, this function comes to our rescue by reconstructing the MemTable from the WAL file. It replays the entries stored in the WAL file and writes it into MemeTable. Following it how it works:
    
    1. The function begins by creating a new empty MemTable instance that will be populated with key-value pairs.
        
    2. It then attempts to open the WAL file. If the file does not exist (example – if this is the first startup), the function assumes there’s nothing to recover and simply returns the empty MemTable.
        
    3. A `gob.Decoder` is used to read the WAL file, which helps to deserialize the saved binary-encoded `WALEntry` data back into key-value pairs.
        
    4. For each successfully decoded `WALEntry`, the key-value pair is added back into the MemTable using the `Put` function.
        

With this, the database can fully recover its state by replaying all the operations recorded in the WAL.

As far as integration is concerned, every time you create a new DB, you should think of replaying from an existing WAL and opening the WAL in append mode. Also, Put should first write to WAL.

```go
func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath) // this is the replay
    if err != nil {
        return nil, err
    }
    //open WAL in append mode
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        memtableSize:    len(memtable.data),
        wal:             wal,
        walPath:         walPath,
        sstables:        make([]*SSTable[K, V], 0),
    }, nil
}

func (db *DB[K, V]) Put(key K, value V) error {
//first write to WAL
    if err := db.wal.Write(key, value); err != nil {
        return err
    }
    
    db.memtable.Put(key, value)
    db.memtableSize++
    
    if db.memtableSize >= db.maxMemtableSize {
        if err := db.flushMemtable(); err != nil {
            return err
        }
    }
    
    return nil
}
```

### Manifest File: Tracking the State of the Database

By this point, the database is pretty robust and durable, but an important question lingers: upon restarts, how does our database know about SSTables? Knowing about all SSTables is important for fetching data.

So say our database crashed after writing several SSTables. Without knowing about these SSTables, the database will create a new slice of SSTables and all of our old data is gone – queries won't read those files.

To solve this problem, we introduce an inventory of SSTables called MANIFEST. Every time we successfully create a new SSTable in flushMemtable, we add its path to the MANIFEST and save the MANIFEST to disk.

The very first thing NewDB does on startup is read the MANIFEST. This gives it the list of all the file paths, and it uses this list to perfectly reconstruct its SSTables slice.

In short, MANIFEST determines the state of the DB.

Manifest contains a slice of SSTablePaths. The Read function will read the MANIFEST file to restore the knowledge of the SSTables. The Write function will write a new manifest file.

```go
type Manifest struct {
    SSTablePaths []string
}

func ReadManifest(path string) (*Manifest, error) {
    file, err := os.Open(path)
    if err != nil {
        if os.IsNotExist(err) {
            // If manifest doesn't exist, return empty manifest
            return &Manifest{SSTablePaths: []string{}}, nil
        }
        return nil, err
    }
    defer file.Close()
    
    var manifest Manifest
    decoder := gob.NewDecoder(file)
    err = decoder.Decode(&manifest)
    if err != nil {
        return nil, err
    }
    
    return &manifest, nil
}

func WriteManifest(path string, manifest *Manifest) error {
    tmpPath := path + ".tmp"
    file, err := os.Create(tmpPath)
    if err != nil {
        return err
    }
    
    encoder := gob.NewEncoder(file)
    if err := encoder.Encode(manifest); err != nil {
        file.Close()
        os.Remove(tmpPath)
        return err
    }
    
    if err := file.Close(); err != nil {
        return err
    }
    // Atomic Rename
    return os.Rename(tmpPath, path)
}
```

You'll notice that we aren’t modifying the existing MANIFEST file directly. Instead, we’re creating a temporary file, writing all the data to it, closing it, and then `atomically renaming` it to replace the old MANIFEST.

The `os.Rename()` operation is atomic on most filesystems, meaning it either completely succeeds or completely fails – there's no in-between state. This is crucial because if the system crashes while updating the MANIFEST, we need to ensure we don't end up with a corrupted file. We’ll discuss this again below when we’re talking about compaction.

With this approach, we either have the old valid MANIFEST or the new valid MANIFEST, never a partially written corrupted file.

From an integration standpoint, NewDB will read the manifest and set its SSTable slice based on that. The flush method, given that it writes to SSTable, will also write SSTable info to manifest to keep the db updated about new SSTables.

```go
type DB[K comparable, V any] struct {
    memtable        *MemTable[K, V]
    maxMemtableSize int
    memtableSize    int
    sstables        []*SSTable[K, V]
    sstableCounter  int
    wal             *WAL[K, V]
    walPath         string
    manifest        *Manifest
    manifestPath    string
}

func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    manifestPath := "MANIFEST"
    manifest, err := ReadManifest(manifestPath)
    if err != nil {
        return nil, err
    }
    
    sstables := make([]*SSTable[K, V], len(manifest.SSTablePaths))
    for i, path := range manifest.SSTablePaths {
        sstables[i] = &SSTable[K, V]{path: path}
    }
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        memtableSize:    len(memtable.data),
        wal:             wal,
        walPath:         walPath,
        manifest:        manifest,
        manifestPath:    manifestPath,
        sstables:        sstables,
    }, nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    
    db.manifest.SSTablePaths = append(db.manifest.SSTablePaths, sstablePath)
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    return nil
}
```

At this point, our DB has almost everything. It can write to memory (MemTable), persist to disk (sstable), and recover from crashes (WAL and manifest). You should include the update and delete feature for completeness – so let’s look at those next.

### Update and Delete: Handling Mutability in an Immutable System

By this time, you should know that in an LSM storage system, data is never updated – rather, new data is written. For example, if you have a data pair ("a": "apple") and over time this has to change to the pair ("a": "apricot"), a new pair will be written to a different SSTable without any change to the existing pair. And yes, this leads to duplicates.

Also, interestingly, data isn't even deleted during write operations. The reason for that is, in a traditional sense, if you have to delete ("a":"apple"), you will have to find where it lives on disk and remove it. This makes writes slow. So instead, a clever mechanism is used: instead of removing the data directly, you can mark the key as deleted by writing a special `TOMBSTONE` value.

So, in the case of deleting (a : apple), you wouldn't remove the key from any SSTable. Instead, you’d write a new key-value pair such as ("a": "TOMBSTONE"). Here’s what this achieves:

* The `"TOMBSTONE"` serves as a marker within the SSTable, telling the system that the key `"a"` has been logically deleted, even though it still physically exists in older SSTables.
    
* During future reads, any value associated with `"TOMBSTONE"` will be treated as deleted, ensuring that the entry no longer shows up in query results.
    
* This mechanism avoids the need for immediate deletions or expensive in-place updates, making write operations faster and simpler.
    

But this also raises the following questions:

1. How do you accurately read when there are duplicates? Meaning, how do users get ("a": "apricot") instead of ("a": "apple") because the former is latest and accurate?
    
2. How do you handle deletes to ensure deleted keys are not returned (and instead, a proper error message is returned)?
    
3. These stale and deleted data are garbage. How do you get rid of them to save on storage space?
    

As long as data is in MemTable (in-memory map), the duplicates are easy to handle: new values will just replace the old values.

But it gets tricky when data is in multiple SSTables. There is a very simple solution to this problem, and that is to just read the newer SSTable before older ones. That way, you will always read the latest value for a given key and exit early.

The following code in the read path ensures reading from newer SSTables before moving to older ones (note the loop starts from `len(db.sstables) - 1`):

```go
func (db *DB[K, V]) Get(key K) (V, error) {
    // Check memtable first
    if val, ok := db.memtable.Get(key); ok {
        if any(val).(string) == TOMBSTONE {
            var zero V
            return zero, ErrNotFound
        }
        return val, nil
    }
    
    // Then check sstables from newest to oldest
    for i := len(db.sstables) - 1; i >= 0; i-- {
        sstable := db.sstables[i]
        val, err := sstable.Get(key)
        if err != nil {
            if err == ErrNotFound {
                continue
            }
            var zero V
            return zero, err
        }
        return val, nil
    }
    
    var zero V
    return zero, ErrNotFound
}
```

And for delete, you could just add a new value "TOMBSTONE":

```go
func (db *DB[K, V]) Delete(key K) error {
    return db.Put(key, any(TOMBSTONE).(V))
}
```

Note: This implementation assumes V is a string type. In a production system, you would need a more robust way to handle tombstones that works with any value type.

Handling deleted keys becomes simple now. You can check for the value (in MemTable and SSTable) and return an error if the value is "TOMBSTONE":

```go
// db.go
func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        if any(val).(string) == TOMBSTONE { //got TOMBSTONE, return zero
            var zero V
            return zero, ErrNotFound
        }
        return val, nil
    }
    // ... rest of function
}
```

```go
// sstable.go
func (s *SSTable[K, V]) Get(key K) (V, error) {
    // ... earlier code
    
    keyInDB := any(pair.Key).(string)
    if keyInDB == any(key).(string) {
        if any(pair.Value).(string) == TOMBSTONE {
            var zero V
            return zero, ErrNotFound
        }
        return pair.Value, nil
    }
    
    // ... rest of function
}
```

### Compaction: Cleaning Up Stale and Deleted Data

We have handled all the scenarios so far except for one. It’s not a concern of serving read/write traffic but something that’s important for the health of the storage system.

Over time, the system has developed a lot of garbage (stale, deleted data) and needs a garbage collection mechanism. Compaction is a background maintenance process that cleans up and reorganizes data in an LSM storage system.

As the system grows, multiple SSTables have been created. This leads to reads needing multiple file operations to get values. By compacting (or merging) multiple SSTables into a single one, you avoid disk operation overhead. Along the way, you should also permanently delete data that has been TOMBSTONED.

Note: Compaction is the only time data is permanently deleted from an LSM storage system.

To grasp the concept of compaction, we are going to implement something called `Full Compaction` where you will merge all the existing SSTables into one larger SSTable. In real-world database implementations, the strategy is more complex, there are multi level compaction involved.

#### Compaction Algorithm

We’re going to implement `K-way merge` to perform compaction. It’s a general algorithm that takes K sorted lists and merges them into a single, combined sorted list. In this case, the K sorted lists are the SSTables, and you are going to merge all of them into a single SSTable.

Our SSTables are already sorted, so the idea of merging them involves:

1. Taking the smallest (first) keys from each SSTable
    
2. Finding the smallest among those keys
    
3. Storing the found smallest key into new SSTable file
    
4. Fetching next key from the SSTable the smallest key belongs to
    
5. Repeating this process for all SSTables
    

Here’s a simple example with numbers:

```bash
Assume we have 3 sorted lists:
List A : [4, 8, 12]
List B : [3, 9]
List C : [7, 10, 11]

In the first iteration, we will take (4, 3, 7) because those are the smallest keys for individual lists. 
We find the smallest among those, which is 3, and store 3 in the result list.

In the second iteration, we will take (4, 9, 7). Note that 3 has already been accounted for. 
We pick 4 and store it to the result list.

Repeating this until all lists are empty, we get:
Result List : [3, 4, 7, 8, 9, 10, 11, 12]
```

The core part of this algorithm is to find the smallest key among the smallest keys from the individual SSTables. Fortunately, we have a data structure called `Min-Heap` that does this for us. So, you’re going to take the smallest key from each SSTable and put them all onto a Min Heap for it to return the smallest among those. We’re going to leverage go’s `container/heap` package to get the Min-Heap data structure and corresponding algorithm to find minimum value and put it at the top of heap.

Min Heap needs you to provide a function for it to determine what is the smaller key between two keys, as it uses that logic to determine global minimum. The following function is implemented for that:

```go
func (h MinHeap[K, V]) Less(i, j int) bool {
    // again for simple comparison assume string key
    keyI := any(h[i].Pair.Key).(string)
    keyJ := any(h[j].Pair.Key).(string)
    if keyI != keyJ {
        return keyI < keyJ
    }
    // this is needed for the case when you have duplicate keys,
    // you will want to pick the one that is in newer sstable because that is latest
    return h[i].SSTableIndex > h[j].SSTableIndex
}
```

One important aspect about the above shown `Less` function is how it handles ties. So if we have two pairs with same key, which is lesser? Let’s assume two pairs as `(a: apple)` and `(a: apricot)`, where (a: apple) is the older value (written to an older SSTable), which pair should the Less function return as the lesser value?

The answer is the one which is in the newer SSTable (see `h[i].SSTableIndex > h[j].SSTableIndex`). It ensures that the SSTable with higher index (that is, latest) becomes the lesser value, so (a: apricot) wins. It’s is important to always get the newer value of a given key.

The code for compaction looks something like the following. Note that we’re discarding deleted values (TOMBSTONE) and the older values.

```go
// put this in a new file compaction.go
func MergeSSTables[K comparable, V any](sstables []*SSTable[K, V], newPath string) (*SSTable[K, V], error) {
    newFile, err := os.Create(newPath) // create a new sstable file
    if err != nil {
        return nil, err
    }
    defer newFile.Close() // prevent memory leak by ensuring file is closed
    
    newEncoder := gob.NewEncoder(newFile) // initialize encoder for new SSTable file
    
    
    files := make([]*os.File, len(sstables)) // open all the sstables
    decoders := make([]*gob.Decoder, len(sstables)) // initialize one decoder per ssltable file
    for i, sstable := range sstables {
        files[i], err = os.Open(sstable.path)
        if err != nil {
            return nil, err
        }
        defer files[i].Close() // prevent memory leak by ensuring file is closed
        decoders[i] = gob.NewDecoder(files[i])
    }
    
    // read first pair from each sstable and store in a pair array
    pairs := make([]Pair[K, V], len(decoders))
    emptySSTables := make([]bool, len(decoders)) // track empty sstables
    for i, decoder := range decoders {
        if err := decoder.Decode(&pairs[i]); err != nil {
            if err == io.EOF {
                emptySSTables[i] = true
                continue
            }
            return nil, err
        }
    }
    
    // push those pairs onto heap
    h := &MinHeap[K, V]{}
    for i, pair := range pairs {
        if !emptySSTables[i] {
            heap.Push(h, &HeapItem[K, V]{Pair: pair, SSTableIndex: i})
        }
    }
    
    // init the min-heap calculation algorithm from container/heap package
    heap.Init(h)
    
    var lastKey K
    firstKey := true
    
    // pop the min item from heap and store it into new sstable
    for h.Len() > 0 {
        item := heap.Pop(h).(*HeapItem[K, V])
        
        // If this key is a duplicate of the last one we saw, skip it
        if !firstKey && item.Pair.Key == lastKey {
            // We only care about the version from the newest SSTable,
            // which we have already processed
        } else {
            if any(item.Pair.Value).(string) != TOMBSTONE {
                // discard deleted
                if err := newEncoder.Encode(item.Pair); err != nil {
                    return nil, err
                }
            }
        }
        
        lastKey = item.Pair.Key
        firstKey = false
        
        // Push the next item from the same SSTable into the heap
        var nextPair Pair[K, V]
        if err := decoders[item.SSTableIndex].Decode(&nextPair); err == nil {
            heap.Push(h, &HeapItem[K, V]{Pair: nextPair, SSTableIndex: item.SSTableIndex})
        } else if err != io.EOF {
            return nil, err
        }
    }
    
    return &SSTable[K, V]{path: newPath}, nil
}
```

All the compaction magic has been packed in one function, `MergeSSTables`. The function has the following logical steps (and you can check the inline comments in the code to follow along):

1. We create a new destination SSTable file and initialize corresponding `gob.Encoder`
    
2. We open all the existing SSTable files, and store their references to `files array`. Also, we initialize one `gob.Decoder` per exiting SSTable file. To prevent memory leak, a `defer` statement ensures that each file will be closed once the function completes its work.
    
3. Each `decoder` reads the first key-value pair from its corresponding SSTable and stores it in the `pairs` array.
    
4. SSTables that are already exhausted (for example, are empty or have hit the end of the file) are marked as such in the `emptySSTables` slice, and we skip pushing them onto the heap.
    
5. We push each pair from the pairs array to `Min-Heap` and then initialize the `Min-Heap` calculation algorithm. This algorithm is present in Go’s `container/heap` package.
    
6. Each time the smallest key-value pair is popped from the min-heap, it’s compared with the previously processed key (`lastKey`). Duplicate keys (those whose values are already written) are skipped.
    
7. Values marked with a `"TOMBSTONE"` (logically deleted entries) are ignored and not written to the new SSTable, effectively cleaning up deleted data.
    
8. To continue the merge, the next key-value pair from the same SSTable (as the one we just processed) is read and pushed onto the heap, unless the end of the SSTable (`io.EOF`) has been reached.
    

To integrate this with the DB, you could use a compaction threshold and trigger compaction as part of the flush when this threshold is reached:

```go
type DB[K comparable, V any] struct {
    memtable            *MemTable[K, V]
    maxMemtableSize     int
    memtableSize        int
    sstables            []*SSTable[K, V]
    sstableCounter      int
    wal                 *WAL[K, V]
    walPath             string
    manifest            *Manifest
    manifestPath        string
    compactionThreshold int
}

func NewDB[K comparable, V any](maxMemtableSize int, compactionThreshold int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    manifestPath := "MANIFEST"
    manifest, err := ReadManifest(manifestPath)
    if err != nil {
        return nil, err
    }
    
    sstables := make([]*SSTable[K, V], len(manifest.SSTablePaths))
    for i, path := range manifest.SSTablePaths {
        sstables[i] = &SSTable[K, V]{path: path}
    }
    
    return &DB[K, V]{
        wal:                 wal,
        walPath:             walPath,
        memtable:            memtable,
        memtableSize:        len(memtable.data),
        maxMemtableSize:     maxMemtableSize,
        manifestPath:        manifestPath,
        manifest:            manifest,
        sstables:            sstables,
        compactionThreshold: compactionThreshold,
    }, nil
}

// a new compact function
func (db *DB[K, V]) Compact() error {
    compactedSSTablePath := fmt.Sprintf("data-compacted-%d.sstable", db.sstableCounter)
    compactedSSTable, err := MergeSSTables(db.sstables, compactedSSTablePath)
    if err != nil {
        return err
    }
    // write new SSTable to MANIFEST file
    db.manifest.SSTablePaths = []string{compactedSSTablePath}
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    //note delete only after writing manifest
    for _, sstable := range db.sstables {
        if err := os.Remove(sstable.path); err != nil {
            log.Printf("Failed to remove old sstable %s: %v", sstable.path, err)
        }
    }
    
    db.sstables = []*SSTable[K, V]{compactedSSTable}
    db.sstableCounter++
    
    return nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    
    db.manifest.SSTablePaths = append(db.manifest.SSTablePaths, sstablePath)
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    // trigger compaction
    if len(db.sstables) >= db.compactionThreshold {
        if err := db.Compact(); err != nil {
            log.Printf("Compaction failed: %v", err)
            return err
        }
    }
    
    return nil
}
```

Notice the `Compact()` function in the integrated DB code? This is where we invoke previously defined the `MergeSSTables` function to trigger the compaction process. After invoking `MergeSSTables`, we write a new SSTable to the MANIFEST file and then delete the older SSTables.

Previously, in the [Manifest File: Tracking the State of the Database](#heading-manifest-file-tracking-the-state-of-the-database), I spoke about atomic renaming `os.Rename(tmpPath, path)`. Let’s talk about why the atomic renaming of MANIFEST matters for compaction.

During compaction, we're making a major change to the database state: replacing multiple SSTables with a single compacted one. The MANIFEST update is critical here because it's the source of truth for which SSTables exist.

Let’s think about what could go wrong without atomic renaming:

1. You start writing the new MANIFEST (which points to the compacted SSTable)
    
2. System crashes mid-write
    
3. MANIFEST is corrupted and unreadable
    
4. On restart, the database has no idea which SSTables exist
    
5. All data is effectively lost
    

With atomic renaming:

1. We write the new MANIFEST to MANIFEST.tmp
    
2. We fully close and sync it to disk
    
3. We atomically rename MANIFEST.tmp to MANIFEST using `os.Rename(tmpPath, path)`
    
4. If crash happens before step 3: old MANIFEST is intact, we retry compaction
    
5. If crash happens during step 3: atomic operation either completes or doesn't – no corruption
    
6. If crash happens after step 3: new MANIFEST is in place, we're good
    

This is also why we delete the old SSTables only after successfully updating the MANIFEST. If we deleted them before updating MANIFEST and then crashed, the MANIFEST would still point to files that no longer exist.

#### Complete Picture:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1765740593067/c18083ad-bf8a-4cae-92d3-d690a61dac52.png align="center")

## Conclusion

Congratulations! You've built a working LSM tree storage engine from scratch. By following the problem-driven approach – discovering issues and implementing solutions as they arose – you've experienced how engineers think about building robust storage systems. I hope this is better than just memorizing the concepts.

**Key Takeaways**

* **Append-only writes** make LSM-trees fast for write-heavy workloads
    
* **Immutability** eliminates complex concurrency issues
    
* **Trade-off** is that LSM-tree favor writes over reads (opposite of B-trees)
    
* **Durability** requires multiple mechanism working together (WAL, MANIFEST, atomic operations)
    
* **Background maintenance** (compaction) is essential for long-term health and cost.
    

Important note: This is a learning implementation. This means that I intentionally simplified the code, so it’s **not production-ready**. Key limitations include:

* No concurrency control (missing mutexes/locks)
    
* No bloom filters for efficient lookups
    
* Simplified compaction strategy
    
* Type safety issues with generic tombstones
    
* Missing robust error recovery
    

### Complete Code:

Like I’ve mentioned before, I've omitted boilerplate code and helper functions for brevity. The complete, runnable implementation is available [at this GitHub repo](https://github.com/justramesh2000/lsm-db).

To learn more about production LSM implementations, study RocksDB, LevelDB, or read the original LSM tree paper by O'Neil et al: [https://www.cs.umb.edu/~poneil/lsmtree.pdf](https://www.cs.umb.edu/~poneil/lsmtree.pdf)
