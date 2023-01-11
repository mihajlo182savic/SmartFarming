$('#changeUser').click(function(){
	var edit = {
		oldUsername: JSON.stringify(sessionStorage.getItem('usernameLog')),
		newUsername: $('#newUser').val()
	};
	$.ajax({
		type: 'POST',
		url: '/profileEditUsername',
		contentType: 'application/json',
		data: JSON.stringify(edit),
		success: function(res){console.log(res)},
		error: function(err){console.log('error')}
	});
});

$('#changePass').click(function(){
	var edit = {
		username: JSON.stringify(sessionStorage.getItem('usernameLog')),
		newPassword: $('#newPass').val()
	};
	$.ajax({
		type: 'POST',
		url: '/profileEditPassword',
		contentType: 'application/json',
		data: JSON.stringify(edit),
		success: function(res){console.log(res)},
		error: function(err){console.log('error')}
	});
});

$('#insertPhone').click(function(){
	var edit = {
		username: JSON.stringify(sessionStorage.getItem('usernameLog')),
		phone: $('#newPhone').val()
	};
	$.ajax({
		type: 'POST',
		url: '/profileEditInsertPhone',
		contentType: 'application/json',
		data: JSON.stringify(edit),
		success: function(res){console.log(res)},
		error: function(err){console.log('error')}
	});
});

$('#showPhone').click(function(){
	var data = {
		username: JSON.stringify(sessionStorage.getItem('usernameLog')),
	}
	$.ajax({
		type: 'POST',
		url: '/getPhone',
		contentType: 'application/json',
		data: JSON.stringify(data),
		success: function(res){console.log(JSON.parse(res)[0][0])},
		error: function(err){console.log('error')}
	});
});