// focus event

var fieldName = document.getElementById('name');

fieldName.addEventListener('focus', function() {
	
	fieldName.setAttribute('value', 'I have the focus');

});

// blur event

fieldName.addEventListener('blur', function() {
	
	fieldName.setAttribute('value', 'I no longer have the focus');

});

