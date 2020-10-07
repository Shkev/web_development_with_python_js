document.addEventListener('DOMContentLoaded', function() {

    let submit = document.querySelector('#submit');
    let task_input = document.querySelector('#task');

    // by default disable the submit button
    submit.disabled = true;
    // when something is typed enable the submit button
    task_input.onkeyup = () => {
        if (task_input.value.length > 0)
        {
            submit.disabled = false;
        }
        else
        {
            submit.disabled = true;
        }
    };

    //when a form is submitted get the submitted text and save it as a task
    document.querySelector('form').onsubmit = () => {
        const task = task_input.value;

        // create a new list element with the entered task
        const li = document.createElement('li');
        li.innerHTML = task

        // adding the new list element under the unordered list (ul) tag in the html
        document.querySelector('#tasks').append(li);
        submit.disabled = true;

        // clearing the input form after the task is entered
        task_input.value = '';

        // stop form from submitting
        return false;
    };
});
