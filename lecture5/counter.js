// if counter does not have a value in local storage then set it to 0
if (!localStorage.getItem('counter'))
{
    localStorage.setItem('counter', 0);
}

function count()
{
    // getting counter from local storage
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    // update the value of counter in local storage
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});