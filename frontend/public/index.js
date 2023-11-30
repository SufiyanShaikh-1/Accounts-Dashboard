tecton.connected.then(function() {
    // Be sure to wrap all of your javascript in tecton.connected.then()
    // This code will execute after tecton has initialized.
    document.querySelector('#my_submit').addEventListener('click', function() {
        var valid = validate_input_fields();
        if (valid) {
            submitForm();
        }
    });
});
