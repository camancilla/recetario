$(document).on("ready", iniciar);

function iniciar(){
	var ele=document.getElementById('contMenu');
	$("#displayMenu").click(function(){
		ele.style.display = ele.style.display == 'none' ? 'block' : 'none';
	});
}