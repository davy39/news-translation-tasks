---
title: 'Hash Table Explained: What it Is and How to Implement It'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/hash-tables
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8e740569d1a4ca385f.jpg
tags:
- name: data structures
  slug: data-structures
seo_title: null
seo_desc: A hash table, also known as a hash map, is a data structure that maps keys
  to values. It is one part of a technique called hashing, the other of which is a
  hash function. A hash function is an algorithm that produces an index of where a
  value can be ...
---

A hash table, also known as a hash map, is a data structure that maps keys to values. It is one part of a technique called hashing, the other of which is a hash function. A hash function is an algorithm that produces an index of where a value can be found or stored in the hash table.

Some important notes about hash tables:

1. Values are not stored in a sorted order.
2. You must account for potential collisions. This is usually done with a technique called chaining. Chaining means to create a linked list of values, the keys of which map to a certain index. 

## Implementation of a hash table

The basic idea behind hashing is to distribute key/value pairs across an array of placeholders or "buckets" in the hash table.

A hash table is typically an array of linked lists. When you want to insert a key/value pair, you first need to use the hash function to map the key to an index in the hash table. Given a key, the hash function can suggest an index where the value can be found or stored:

```text
index = f(key, array_size)
```

This is often done in two steps:

```text
hash = hashfunc(key)
index = hash % array_size
```

Using this method, `hash` is independent of the size of the hash table. `hash` is reduced to an index – a number between 0, the start of the array, and `array_size - 1`, the end of the array – using the modulo (%) operator.

Consider the following string, `S`:

```text
string S = “ababcd”
```

You need to count the frequency of all the characters in `S`. The easiest way to do this is to iterate through all the possible characters and count the frequency of each, one by one. 

This works, but it's slow – the time complexity of such an approach is O(26*N), with `N` being the size of the string `S` multiplied by 26 possible characters from A-Z.

```c
void countFre(string S)
    {
        for(char c = ‘a’;c <= ‘z’;++c)
        {
            int frequency = 0;
            for(int i = 0;i < S.length();++i)
                if(S[i] == c)
                    frequency++;
            cout << c << ‘ ‘ << frequency << endl;
        }
    }
```

**Output:**

```text
a 2
b 2
c 1
d 1
e 0
f 0
…
z 0
```

Let's take a look at a solution that uses hashing.

Take an array and use the hash function to hash the 26 possible characters with indices of the array. Then iterate over `S` and increase the value of the current character of the string with the corresponding index for each character. 

The complexity of this hashing approach is O(N), where N is the size of the string.

```text
int Frequency[26];

    int hashFunc(char c)
    {
        return (c - ‘a’);
    }

    void countFre(string S)
    {
        for(int i = 0;i < S.length();++i)
        {
            int index = hashFunc(S[i]);
            Frequency[index]++;
        }
        for(int i = 0;i < 26;++i)
            cout << (char)(i+’a’) << ‘ ‘ << Frequency[i] << endl;
    }
```

Output

```text
a 2
b 2
c 1
d 1
e 0
f 0
…
z 0
```

## Hash Collisions

Since your hash map will probably be significantly smaller than the amount of data you're processing, hash collisions are unavoidable. There are two main approaches to handling collisions: _chaining_ and _open addressing_.

### Chaining

As mentioned earlier, chaining means that each key/value pair in the hash table, the value is a linked list of data rather than a single cell. 

For example, imagine that the key 152 holds the value "John Smith". If the value "Sandra Dee" is added to the same key, "Sandra Dee" is added as another element to key 152, just after "John Smith".

```
152: [["John Smith", "p01"]]

...

152: [["John Smith", "p01"] ["Sandra Dee", "p02"]]
```

The main drawback of chaining is the increase in time complexity. Instead of 0(1) as with a regular hash table, each lookup will take more time since we need to traverse each linked list to find the correct value.

### Open addressing

Open addressing means that, once a value is mapped to a key that's already occupied, you move along the keys of the hash table until you find one that's empty. For example, if "John Smith" was mapped to 152, "Sandra Dee" will be mapped to the next open index:

```
152: ["John Smith", "p01"] 

...

152: ["John Smith", "p01"],
153: ["Sandra Dee", "p02"]
```

The main drawback to open addressing is that, when you look up values, they might not be at the key map you expect them at. Instead, you have to traverse different parts of the hash table to find the value you're looking for.

