---
title: Slicing and Indexing in Python – Explained with Examples
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-29T14:26:25.000Z'
originalURL: https://freecodecamp.org/news/slicing-and-indexing-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Sabi.JPG
tags: []
seo_title: null
seo_desc: 'Slicing and indexing are two fundamental concepts in Python. They help
  you access specific elements in a sequence, such as a list, tuple or string.

  By using these techniques, you can extract substrings from strings, filter lists,
  and extract columns ...'
---

Slicing and indexing are two fundamental concepts in Python. They help you access specific elements in a sequence, such as a list, tuple or string.

By using these techniques, you can extract substrings from strings, filter lists, and extract columns from 2D lists, among other things.

Understanding how to use slicing and indexing is essential for working with data in Python, so let's explore these concepts in detail and provide real-life examples to help you understand how they work.

## Indexing in Python

Indexing is the process of accessing an element in a sequence using its position in the sequence (its index).

In Python, indexing starts from 0, which means the first element in a sequence is at position 0, the second element is at position 1, and so on.

To access an element in a sequence, you can use square brackets `[]` with the index of the element you want to access.

Let's consider the following example:

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[0]) # output: 'apple'
print(my_list[1]) # output: 'banana'
```

In the above code, we have created a list called `my_list` and then used indexing to access the first and second elements in the list using their respective indices.

## Slicing in Python

Slicing is the process of accessing a sub-sequence of a sequence by specifying a starting and ending index. In Python, you perform slicing using the colon `:` operator. The syntax for slicing is as follows:

```python
sequence[start_index:end_index]
```

where `start_index` is the index of the first element in the sub-sequence and `end_index` is the index of the last element in the sub-sequence (excluding the element at the `end_index`). To slice a sequence, you can use square brackets `[]` with the start and end indices separated by a colon.

For example:

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # output: ['banana', 'cherry']
```

In the above code, we have used slicing to access a sub-sequence of `my_list` containing the second and third elements.

You can also omit either the `start_index` or the `end_index` in a slice to get all the elements from the beginning or end of the sequence. For example:

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[:2]) # output: ['apple', 'banana']
print(my_list[2:]) # output: ['cherry', 'date']
```

In the first line of the above code, we have used slicing to get all the elements from the beginning of `my_list` up to (but not including) the element at index 2. In the second line, we have used slicing to get all the elements from index 2 to the end of `my_list`.

## Examples of Slicing and Indexing in Python

Let's take a look at some real-life examples of how you can use slicing and indexing in Python.

### Example 1: How to Extract Substrings from a String

Suppose we have a string representing a sentence, and we want to extract the first word from the sentence. We can do this using indexing as follows:

```python
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # output: "The"
```

In the above code, we have used indexing to extract the first three characters from the `sentence` string, which correspond to the first word. The `[:3]` syntax means that we are selecting all characters from the beginning of the string up to (but not including) the character at index 3.

We could also extract the second and third words from the sentence using slicing as follows:

```python
second_word = sentence[4:9]
third_word = sentence[10:15]
print(second_word) # output: "quick"
print(third_word) # output: "brown"
```

In these examples, we have used slicing to extract a range of characters from the `sentence` string. The `4:9` slice means that we are selecting characters starting from index 4 (inclusive) up to index 9 (exclusive), which correspond to the second word "quick". Similarly, the `10:15` slice means we are selecting characters starting from index 10 up to index 15 (exclusive), which correspond to the third word "brown".

### Example 2: How to Filter a List

Suppose we have a list of numbers and we want to extract all the odd numbers from the list. We can do this using slicing as follows:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = numbers[::2]
print(odd_numbers) # output: [1, 3, 5, 7, 9]
```

In the above code, we have used slicing to extract all the odd numbers from the `numbers` list. The `::2` slice means that we are selecting every other element starting from the first element, which correspond to the odd numbers in the list. Since we only want the odd numbers, we start with the first element (index 0) and then select every other element after that.

We could also extract all the even numbers from the list using slicing as follows:

```python
even_numbers = numbers[1::2]
print(even_numbers) # output: [2, 4, 6, 8]
```

In this example, we have used slicing to extract every other element starting from the second element (index 1), which correspond to the even numbers in the list.

### Example 3: How to Extract Columns from a 2D List

Suppose we have a 2D list representing a table of data, and we want to extract a particular column from the table. We can do this using list comprehension and indexing as follows:

```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data]
print(column) # output: [2, 5, 8]
```

In the above code, we have used list comprehension to extract the second element (index 1) from each row in the `data` list, and then combined these elements into a new list called `column`. The `row[1]` syntax means that we are selecting the second element from each row, which corresponds to the second column in the table.

We could also extract other columns from the table by changing the index used in the list comprehension, for example:

```python
column_0 = [row[0] for row in data]
column_2 = [row[2] for row in data]
print(column_0) # output: [1, 4, 7]
print(column_2) # output: [3, 6, 9]
```

In these examples, we have used indexing to select the first and third elements from each row, which correspond to the first and third columns in the table.

### Example 4: How to Modify Parts of a List

Suppose we have a list of numbers and we want to modify the values of some of the elements in the list. We can do this using slicing as follows:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = [10, 20, 30]
print(numbers) # output: [1, 10, 20, 30, 5, 6, 7, 8, 9]
```

In the above code, we have used slicing to select a range of elements from the `numbers` list (indices 1 to 3), and then replaced these elements with a new list `[10, 20, 30]`. The result is that the elements at indices 1 to 3 in the `numbers` list have been replaced with the new values.

We could also insert new elements into the list using slicing as follows:

```python
numbers[4:4] = [40, 50]
print(numbers) # output: [1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]
```

In this example, we have used slicing to insert a new list `[40, 50]` at index 4 in the `numbers` list. The `4:4` slice means that we are inserting the new list at index 4 (that is, before the element at index 4), but not deleting any existing elements.

## Conclusion

In this article, we have discussed the concepts of slicing and indexing in Python and provided several examples of how they can be used to manipulate lists and strings.

Slicing and indexing are powerful tools that can greatly simplify certain tasks in Python programming, such as selecting subsets of data, modifying lists, and extracting substrings. By understanding these concepts and using them effectively in your code, you can become a more efficient and effective Python programmer.
