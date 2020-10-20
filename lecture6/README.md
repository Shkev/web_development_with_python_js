# Lecture 6: User Interfaces

* Javascript commonly used to create single page web applications
    * Only has one page instead of loading different pages
* JS can be used to fetch data from different webpages as part of the site
    * Removed the need to reload entire pages for small change to a site
    * Use `history.pushState()` to add to the url of the page without loading a new page
* `window.popstate()` allows using the back/forward button on browser with the JS hidden/showing pages

## Window

* `window` object has methods that give useful information about the user's browser
    * Differs from the `document` object. Does not refer to entire web page, only what the user can see
* `window.innerwidth` returns width of browser window
* `window.innerheight` return height of browser window
* `window.scrollY` returns the number of pixels the user has scrolled down from the top of the document
* `document.body.offsetHeight` is the height of the entire document
    * Can be used to detect if the user has scrolled to the bottom of the page
        * If `window.innerheight + window.scrollY === document.body.offsetHeight`

## Animation

* CSS supports animation
* Set animation name, duration, and type (ex: "forwards")
* Define animation with `@keyframes NAME` and defining start and finish states
* JS can control animations
    * Pause/play with `style.animationPlayState`

## ReactJS

* React src: https://unpkg.com/react@16/umd/react.development.js
* Allows for cleaner JS code
* Different from React becauase it doesn't use imperative programming
    * Uses components in the html code to modify it
    * Each component represented as a *class*
* Also uses ReactDOM and Babel
    * ReactDOM src: https://unpkg.com/react-dom@16/umd/react-dom.development.js
    * Babel src: https://unpkg.com/babel-standalone@6/babel.min.js
* Include variables in HTML with `{VARNAME}`

### Classes

* A class represents a "new" user-created HTML element (called a component)
* Components can be used as their own tags (even in other componenets)
* All classes need a `render()` method
    * Tells browser what HTML to render
    * Ex:
    ```js
    render() {
        return (
            <h1>Hello</h1>
        )
    }
    ```
* Access "arguments" given to a component with `this.props.ARGNAME`
* Things that are going to change are stored in the state of a component