$(document).ready(function() {
	
	$("#main").height($(window).height()-$("#nav").height());

});

$("#run").click(function(){

	$.ajax({
		url: 'http://127.0.0.1:5000/query',
		type: 'POST',
		dataType: 'json',
	    success: function(resp) {
		alert("HERE");
		
		// queue = resp.queue;
		// console.log(queue)
		// for(item in queue){
		// 	tokens = queue[item].path.split("/");
		// 	fname = tokens[tokens.length-1];
		// 	// Currently being processed
		// 	// htmlString = "<li id='"+queue[item].itemId+"'class='collection-item'><div>"+fname+"<a class='secondary-content'>Cheesecake-PC</a></div></li>"
		// 	htmlString = "<li id='item"+queue[item].itemId+"'class='collection-item'><div><span class='tooltipped' data-position='right' data-delay='50' data-tooltip='"+queue[item].path+"'>"+fname+"</span><a href='#' data-id='"+queue[item].itemId+"'class='secondary-content remove-from-queue' ><i class='queue-clear material-icons'>clear</i></a></div></li>"
		// 	$("#queue-content").append(htmlString);
			
		// }
		// $('.tooltipped').tooltip('remove');
		// $('.tooltipped').tooltip({delay: 50});

		// $(".remove-from-queue").click(function(event){
		// 	removeFromQueue($(this).data("id"));
		// });

	}});


});