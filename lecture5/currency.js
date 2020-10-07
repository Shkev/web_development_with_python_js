document.addEventListener("DOMContentLoaded", function() {
    // wait until the form is submitted to get the data
    document.querySelector('form').onsubmit = function() {
        // request the api data from the site and convert it to json format
        fetch("https://api.exchangeratesapi.io/latest?base=USD")
        .then(response => response.json())
        .then(data => {
            // get the currency that the user wants to convert to from the form
            const currency = document.querySelector('#currency').value.toUpperCase();
            let rate = data.rates[currency];
            // checking if the desired rate exists
            if (rate != undefined)
            {
                document.querySelector('#result h3').append(`1 USD = ${rate.toFixed(3)} ${currency}`);
            }
            else
            {
                document.querySelector('#result').innerHTML = "Invalid currency";
            }
        })
        .catch(error => {
            // handling an error if the api does not work
            console.log("Error: ", error);
        });

        return false;
    };
});