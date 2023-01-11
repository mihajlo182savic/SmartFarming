$(document).ready(function(){

	$('#userLogin').click(function(){
		var user = {
			username: $('#user').val(),
			password: $('#pass').val(),
		};
		$.ajax({
			type: 'POST',
			url: '/userLogin',
			contentType: 'application/json',
			data: JSON.stringify(user),
			success: function(res){sessionStorage.setItem('usernameLog',user.username)},
			error: function(err){console.log('error')}
		});
	});
});
