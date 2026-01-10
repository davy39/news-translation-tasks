---
title: 'JSON Object Examples: Stringify and Parse Methods Explained'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-16T23:05:00.000Z'
originalURL: https://freecodecamp.org/news/json-stringify-method-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c8f740569d1a4ca32e4.jpg
tags:
- name: JavaScript
  slug: javascript
- name: json
  slug: json
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'JSON Stringify

  The JSON.stringify() method converts a JSON-safe JavaScript value to a JSON compliant
  string.

  What are JSON-safe values one may ask! Let’s make a list of all JSON-unsafe values
  and anything that isn’t on the list can be considered JSON...'
---

## **JSON Stringify**

The `JSON.stringify()` method converts a _JSON-safe_ JavaScript value to a JSON compliant string.

What are JSON-safe values one may ask! Let’s make a list of all JSON-unsafe values and anything that isn’t on the list can be considered JSON-safe.

#### **JSON-unsafe values:**

* `undefined`
* `function(){}`
* (ES6+) `Symbol`
* An object with circular reference(s) in it

#### **Syntax**

```javascript
  JSON.stringify( value [, replacer [, space]])
```

In its simplest and most used form:

```javascript
  JSON.stringify( value )
```

#### **Parameters**

`value` : The JavaScript value to be ‘stringified’.

`replacer` : (Optional) A function or an array which serves as a filter for properties of the value object to be included in the JSON string.

`space` : (Optional) A numeric or string value to provide indentation to the JSON string. If a numeric value is provided, that many spaces (upto 10) act as indentaion at each level. If a string value is provided, that string (upto first 10 chracters) acts as indentation at each level.

#### **Return type**

The return type of the method is: `string`.

## **Description**

The JSON-safe values are converted to their corresponding JSON string form. The JSON-unsafe values on the other hand return :

* `undefined` if they are passed as values to the method
* `null` if they are passed as an array element
* nothing if passed as properties on an object
* throws an error if its an object with circular references(s) on it.

```javascript
  //JSON-safe values
  JSON.stringify({});                  // '{}'
  JSON.stringify(true);                // 'true'
  JSON.stringify('foo');               // '"foo"'
  JSON.stringify([1, 'false', false]); // '[1,"false",false]'
  JSON.stringify({ x: 5 });            // '{"x":5}'
  JSON.stringify(new Date(2006, 0, 2, 15, 4, 5))  // '"2006-01-02T15:04:05.000Z"'
  
  //JSON-unsafe values passed as values to the method
  JSON.stringify( undefined );					// undefined
  JSON.stringify( function(){} );					// undefined

  //JSON-unsafe values passed as array elements
  JSON.stringify({ x: [10, undefined, function(){}, Symbol('')] });  // '{"x":[10,null,null,null]}' 
 
 //JSON-unsafe values passed as properties on a object
  JSON.stringify({ x: undefined, y: Object, z: Symbol('') });  // '{}'
  
  //JSON-unsafe object with circular reference on it
  var o = { },
    a = {
      b: 42,
      c: o,
      d: function(){}
    };

  // create a circular reference inside `a`
  o.e = a;

  // would throw an error on the circular reference
  // JSON.stringify( a );
```

`JSON.stringify(...)` behaves differently if an object passed to it has a `toJSON()` method defined on it. The return value from the `toJSON()` method will be serialized instead of the object itself.

This comes in exceptionally handy when an object contains any illegal JSON value.

```javascript
   //JSON-unsafe values passed as properties on a object
   var obj = { x: undefined, y: Object, z: Symbol('') };
   
   //JSON.stringify(obj);  logs '{}'
   obj.toJSON = function(){
    return {
      x:"undefined",
      y: "Function",
      z:"Symbol"
    }
   }
   JSON.stringify(obj);  //"{"x":"undefined","y":"Function","z":"Symbol"}"
    
  //JSON-unsafe object with circular reference on it
  var o = { },
    a = {
      b: 42,
      c: o,
      d: function(){}
    };

  // create a circular reference inside `a`
  o.e = a;

  // would throw an error on the circular reference
  // JSON.stringify( a );
  
  // define a custom JSON value serialization
  a.toJSON = function() {
    // only include the `b` property for serialization
    return { b: this.b };
  };

  JSON.stringify( a ); // "{"b":42}"
```

#### **The `replacer`**

The `replacer`, as mentioned earlier, is a filter which indicates which properties are to be included in the JSON string. It can either be an array or a function. When an array, the replacer contains the string representations of only those properties which are to be included in the JSON string.

```javascript
  var foo = {foundation: 'Mozilla', model: 'box', week: 45, transport: 'car', month: 7};
  JSON.stringify(foo, ['week', 'month']);    // '{"week":45,"month":7}', only keep "week" and "month" properties
```

If `replacer` is a function, it will be called once for the object itself, and then once for each property in the object, and each time is passed two arguments, _key_ and _value_. To skip a _key_ in the serialization, `undefined` should be returned. Otherwise, the _value_ provided should be returned. If any of these _values_ are objects themselves, the `replacer` function serializes them recursively as well.

```javascript
  function replacer(key, value) {
    // Filtering out properties
    if (typeof value === 'string') {
      return undefined;
    }
    return value;
  }

  var foo = {foundation: 'Mozilla', model: 'box', week: 45, transport: 'car', month: 7};
  JSON.stringify(foo, replacer);  // '{"week":45,"month":7}'
```

If an array is passed to `JSON.stringify()` and `replacer` returns `undefined` for any of its elements, the element’s value is replaced with `null`. `replacer` functions cannot remove values from an array.

```javascript
  function replacer(key, value) {
    // Filtering out properties
    if (typeof value === 'string') {
      return undefined;
    }
    return value;
  }

  var foo = ['Mozilla', 'box', 45, 'car', 7];
  JSON.stringify(foo, replacer);  // "[null,null,45,null,7]"
```

#### **The `space`**

The `space` parameter used for indentation makes the result of `JSON.stringify()` prettier.

```javascript
  var a = {
    b: 42,
    c: "42",
    d: [1,2,3]
  };

  JSON.stringify( a, null, 3 );
  // "{
  //    "b": 42,
  //    "c": "42",
  //    "d": [
  //       1,
  //       2,
  //       3
  //    ]
  // }"

  JSON.stringify( a, null, "-----" );
  // "{
  // -----"b": 42,
  // -----"c": "42",
  // -----"d": [
  // ----------1,
  // ----------2,
  // ----------3
  // -----]
  // }"
```

## **JSON Parse**

The `JSON.parse()` method parses a string and construct a new object described by a string.

### Syntax:

```javascript
    JSON.parse(text [, reviver])
```

### Parameters:

`text` The string to parse as JSON

`reviver`(Optional) The function will receive `key` and `value` as arguments. This function can be used to transform the result value.

Here is an example on how to use `JSON.parse()`:

```javascript
var data = '{"foo": "bar"}';

console.log(data.foo); // This will print `undefined` since `data` is of type string and has no property named as `foo`

// You can use JSON.parse to create a new JSON object from the given string
var convertedData = JSON.parse(data);

console.log(convertedData.foo); // This will print `bar
```

[Repl.it Demo](https://repl.it/MwgK/0)

Here is an example with `reviver`:

```javascript
var data = '{"value": 5}';

var result = JSON.parse(data, function(key, value) {
    if (typeof value === 'number') {
        return value * 10;
    }
    return value;
});

// Original Data
console.log("Original Data:", data); // This will print Original Data: {"value": 5}
// Result after parsing
console.log("Parsed Result: ", result); // This will print Parsed Result:  { value: 50 }
```

In the above example, all numeric values are being multiplied by `10` - [Repl.it Demo](https://repl.it/Mwfp/0)

## More info on JSON:

* [JSON syntax](https://guide.freecodecamp.org/javascript/standard-objects/json/json-syntax)
* [Turn your website into a mobile app with 7 lines of JSON](https://www.freecodecamp.org/news/how-to-turn-your-website-into-a-mobile-app-with-7-lines-of-json-631c9c9895f5/)

