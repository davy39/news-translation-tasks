---
title: How the Redis Hash Table Scan Function Works
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-23T13:15:23.000Z'
originalURL: https://freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eUYhCqLYo_cQpMSQvelQOw.jpeg
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: Redis
  slug: redis
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ehud Tamir

  One of the big challenges for me as a software developer is reading other people’s
  code. For this post, I read an interesting piece of C code that I didn’t know before,
  and I’m about to present it to you. The code I’m going to talk abou...'
---

By Ehud Tamir

One of the big challenges for me as a software developer is reading other people’s code. For this post, I read an interesting piece of C code that I didn’t know before, and I’m about to present it to you. The code I’m going to talk about is part of the [**Redis**](https://en.wikipedia.org/wiki/Redis) database, and it can be found [here](https://github.com/antirez/redis/blob/e504583b7806d946da9c3627784d551a742be4d0/src/dict.c#L838).

Redis is a key-value database. Every entry in the database is a mapping from a key to a value. Values can have several types. There are integers, lists, hash tables and more. Behind the scenes, the database itself is also a hash table. In this post, we’ll explore the SCAN command in Redis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUYhCqLYo_cQpMSQvelQOw.jpeg)
_By © User:Colin / Wikimedia Commons, CC BY-SA 4.0, [https://commons.wikimedia.org/w/index.php?curid=30343877](https://commons.wikimedia.org/w/index.php?curid=30343877" rel="noopener" target="_blank" title=")_

### Redis SCAN

SCAN is a cursor-based iteration command, allowing a client to go over all the elements in a table. This cursor-based scanner accepts an integer **cursor** on each call, and returns **a batch of items** and the **cursor value** to be used in the next call to SCAN. The initial cursor value is 0, and when SCAN returns 0 as the next cursor value, it means that the scan is done and all elements were seen by the client.

The SCAN command has a few interesting properties:

1. It guarantees that all items present in the table will be returned _at least once_.
2. It is **stateless**. The table doesn’t save any data about its active scanners. This also means that scans don’t lock the database.
3. It is resilient to table resizing. To maintain O(1) access time, hash tables sustain a certain [load factor](https://en.wikipedia.org/wiki/Hash_table#Key_statistics). The load factor measures how “full” the table is at a given time. When the load factor gets too large or too small, the table is resized. SCAN will maintain its guarantees even if called while the table is being resized.

### Implementation

SCAN is implemented in dict.c, in the function `dictScan()`. This is the function’s signature and additional housekeeping:

```c
unsigned long dictScan(dict *d,
                       unsigned long v,
                       dictScanFunction *fn,
                       dictScanBucketFunction* bucketfn,
                       void *privdata)
{
    dictht *t0, *t1;
    const dictEntry *de, *next;
    unsigned long m0, m1;

    if (dictSize(d) == 0) return 0;
    // ...
```

Things worth noting:

* The function accepts 5 parameters: `dict *d`, the dictionary to be scanned, `unsigned long v`, the cursor, and 3 other parameters that we’ll get into later.
* The function returns the cursor value to be used in the next call to this function. If the function returns 0, it means that the scan is done.
* `if (dictSize(d) == 0) return 0;`. When the dictionary is empty the function returns 0 to indicate that the scan is done.

#### 1. Normal scanning

The following code scans a bunch of elements:

```c
if (!dictIsRehashing(d)) {
    t0 = &(d->ht[0]);
    m0 = t0->sizemask;

    /* Emit entries at cursor */
    if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
    de = t0->table[v & m0];
    while (de) {
        next = de->next;
        fn(privdata, de);
        de = next;
    }
    
    /* Set unmasked bits so incrementing the reversed cursor
     * operates on the masked bits */
    v |= ~m0;

    /* Increment the reverse cursor */
    v = rev(v);
    v++;
    v = rev(v);
    
} else {
    // ...
```

Let’s go over it step-by-step. Let’s start with the first line below:

```
if (!dictIsRehashing(d)) {
    t0 = &(d->ht[0]);
    m0 = t0->sizemask;
```

Rehashing is the process of spreading elements evenly across a table after it is resized. The dict.c hash table rehashes _incrementally_, which means that it doesn’t rehash the entire table at once, but little-by-little. Every operation done on the table, like add, delete, find, also performs a rehash step. This allows to keep the table available for operations during rehashing. Due to the way that rehashing is implemented, the function works differently during rehashing. We’ll start by looking at what happens when the table isn’t rehashing.

A pointer to the hash table is saved in the local variable `t0`, and its **size mask** is saved in `m0`. **Size mask:** dict.c hash tables are always `2^n` in size. For a given table size, the size mask is `2^n-1`, which is a binary number with its `n` least-significant bits set to 1. For example, for `n=4; 2^n-1 = 00001111`. For a given key, its location in the hash table will be the last `n` bits of the **hash** of the key. We’ll see this in action in a bit.

The dict.c hash table uses [open addressing](https://en.wikipedia.org/wiki/Open_addressing). Every entry in the table is a linked-list of elements with conflicting hash value. This is called a **bucket**. In this next part, a **bucket** of elements is scanned:

```
/* Emit entries at cursor */
if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
de = t0->table[v & m0];
while (de) {
    next = de->next;
    fn(privdata, de);
    de = next;
}
```

Note the use of the **size mask**: `t0->table[v &` m0`]`. v might be outside the indexable range of the tabl`e. v &` m0 uses the size mask to keep only the la`s`t n digits `o`f v, and yields a valid index into the table.

You may have guessed by now what `bucketfn` is for. `bucketfn` is provided by the caller and is applied to each bucket of elements. It is also passed `privdata`, which is arbitrary data passed to `dictScan()` by the caller. In a similar fashion, `fn` is applied to all the entries in the bucket on-by-one. Note that a bucket may be empty, in which case its value is `NULL`.

OK, so we iterated over a bucket of elements. What’s next? We’re going to return the cursor value for the next call to `dictScan()`. This is done by incrementing the current cursor `v`, but with a twist! The cursor is first reversed, then incremented, and then reversed again:

```
    /* Set unmasked bits so incrementing the reversed cursor
     * operates on the masked bits */
    v |= ~m0;
    /* Increment the reverse cursor */
    v = rev(v);
    v++;
    v = rev(v);
```

First, `v |= ~m0` sets all the non-masked bits in `v` to 1. The effect is that when reversing `v` and incrementing, these bits will be effectively ignored. Then, `v` is reversed, incremented and reversed again. Let’s look at an example:

```
Table size = 16 (n = 4, m0 = 16-1 = 00001111)
v = 00001000 (Current cursor)
v |= ~m0;    // v == 11111000  (~m0 = 11110000)
v = rev(v);  // v == 00011111
v++;         // v == 00100000
v = rev(v);  // v == 00000100
```

After this bit-magic, `v` is returned.

**Why is the cursor reversed before it’s incremented?** The table might grow between iterations. This guarantees that the cursor stays valid. When the table grows, additional bits are added to its size mask **from the left**. By incrementing the reversed number, we can expand the smaller table’s indices into the bigger one.

For example: Let’s say the old table’s size was 16 (size mask `00001111`) and cursor was `00001000`. When the table grows to 32 elements its size mask will be `00011111`. All the elements previously in the `00001000` slot will map to either `00001000`or `00011000` in the new table. These cursors are compatible with both smaller and larger tables!

#### 2. Scanning during table rehashing

The last part we need to understand is how the scan work while the table is rehashing. **Incremental rehashing** is implemented in dict.c by having two active tables at the same time. A second table is created when the hash table is resized. New items are added to the new table. On every rehash step elements from the old table are moved to the new table. When the old table becomes empty it is removed.

When performing a scan, both old and new tables are scanned for elements, starting from the **smaller** **table**. After the items in the smaller table are scanned, the _complementing items_ from the larger table are scanned. Thus all the elements covered by the cursor `v` are scanned. Let’s see what this looks like. This is the entire code snippet, we’ll break it down below:

```c
    } else {  // dictIsRehashing(d)
        t0 = &d->ht[0];
        t1 = &d->ht[1];

        /* Make sure t0 is the smaller and t1 is the bigger table */
        if (t0->size > t1->size) {
            t0 = &d->ht[1];
            t1 = &d->ht[0];
        }

        m0 = t0->sizemask;
        m1 = t1->sizemask;

        /* Emit entries at cursor */
        if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
        de = t0->table[v & m0];
        while (de) {
            next = de->next;
            fn(privdata, de);
            de = next;
        }

        /* Iterate over indices in larger table that are the expansion
         * of the index pointed to by the cursor in the smaller table */
        do {
            /* Emit entries at cursor */
            if (bucketfn) bucketfn(privdata, &t1->table[v & m1]);
            de = t1->table[v & m1];
            while (de) {
                next = de->next;
                fn(privdata, de);
                de = next;
            }

            /* Increment the reverse cursor not covered by the smaller mask.*/
            v |= ~m1;
            v = rev(v);
            v++;
            v = rev(v);

            /* Continue while bits covered by mask difference is non-zero */
        } while (v & (m0 ^ m1));
    }
```

First of all, `t0` and `t1` are used to store the smaller and larger tables respectively, with `m0` and `m1` the size masks for each. Then the smaller table is scanned, just like we saw earlier.

Next, the cursor is used to index into the larger table, using the larger size mask `m1`: `de = t1->table[v & m1]`. In the inner loop, the cursor is incremented to cover all the expansions of the smaller table’s index.

For example, if the index of the bucket in the smaller table was `0100`, and the larger table is twice as large, the indices covered in this loop will be `00100` and `10100`. The do-while’s condition prevents from incrementing the cursor beyond the range covered by the small table’s bucket: `while (v & (m0 ^ m1));`. I’ll leave it to you to understand this last bit :)

That’s it! We’ve covered the entire hash table scan function. The only missing piece is the implementation of `rev(v)`, which is a general function to reverse the bits in a number. The implementation used in dict.c is particularly interesting as it achieves an O(log n) running time. I might cover it in a future post.

Thanks for reading! Many thanks to [Dvir Volk](https://www.freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52/undefined) for his inspiration and support! Thanks to [Jason Li](https://www.freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52/undefined) for his feedback that helped me correct an error in the post.

