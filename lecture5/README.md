# Lecture 5: Javascript

* JS code is written in html files withing the `<script>` tag
* Code can also be included in a separate ".js" file
    * Added to html with `<script src='file_path'></script>`
* JS uses functions and each line ends with a `;`
* The `alert()` functions displays an alert to the user
* Create functions with the following syntax:
```js
function FUNC_NAME()
{
    code goes here
}
```
* Inline functions can be written either using the above notation or with `(PARAMS) => { ... }` (similar to lambda functions in python)
* Functions can be called within the html
* Include variables in strings (like in the alert function) by surrounding the string with `` `...` `` and include the variable you want to insert with `${}.`
    * Ex: `` `Hello my name is ${NAME}` ``
* Print to console with `console.log()` (like Python print function)

## Variables
* Define mutable variables with `let VAR_NAME = VALUE`
* Define immuatable variables with `const VAR_NAME = VALUE`
* **Objects:** Similar to Python dictionaries. Define:
```js
let person = {
    first: 'harry',
    last: 'potter'
}
```
* Access elements of objects with `object.attribute` (ex: `person.first`)
    * Data stored in JSON format

## Manipulating HTML
* HTML elements can be picked out using the event listener `document.querySelector()`
* `document.querySelectorAll()` returns a list of all elements with the given tag
* Get value of element with `.innerHTML` 
* `if` statements like in C
    * Equality is tested with `===`: tests that the value of two things is the same and that their type is the same
* Attriutes of html tags can be modified with JS. 
    * Ex: `document.querySelector('button').onclick` accesses the onclick attribute of the button tag and lets you modify it
* Access and change CSS of html elements with `.style.CSS_ELEMENT`
* The `this` object refers to the html element currenly being looked at
* For HTML elements like lists, new list elements can be added in between the tags with the `.append()` method
* Have something occur multiple times in intervals (once every 2 seconds for example) with the `setInterval(FUNC, INTERVAL_LEN)` function

### Event Listeners
* Browsers render HTML files from top to bottom so if you reference an html tag in a script before it is loaded then you will get an error
* This is fixed with the `document.addEventListener()`
    * Takes two arguments: What to look for (the event) and what do to when the event occurs (a function)
    * The `'DOMContentLoaded'` event is true once the entire html document has loaded (which can be used to fixed the above issue)

## Local Storage

* Allows the information from a site to persist when you refresh the page 
* Uses the two functions:
    * `getItem()` gets the item at the given key
    * `setItem()` sets the value at the given key to the given value
```js
localStorage.getItem(key);
localStorage.setItem(key, value);
```

## Ajax

* Other sites can be queried with the `fetch()` function
    * Sends a "promise" to the inputted site
    * The `.then` method tells it what to do once the promise is returned (when you get the requested data)
    * Runs asynchronously with the program