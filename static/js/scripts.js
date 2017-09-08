$(document).ready(function() {
	
	$("#main").height($(window).height()-$("#nav").height());

});

$("#run").click(function(){
	// data = {"query": $("#query").val()};

	$.ajax({
		url: 'http://127.0.0.1:5000/query',
		type: 'POST',
		dataType: 'json',
		data:{"query":$("#query").val()},

	    success: function(resp) {
	    	console.log(resp)
		
			htmlString = "<h5>"+resp.query+"</h5>";
			

			htmlString +="<table class='striped highlight'><thead><tr>";

			for(column in resp.columns)
				htmlString +="<th>"+resp.columns[column]+"</th>";

			htmlString+="</tr></thead>";

			for(row in resp.data){
				htmlString+="<tr>";
				for(col in resp.data[row]){
					htmlString +="<td>"+resp.data[row][col]+"</td>";
				}
				htmlString+="</tr>";
			}

			htmlString+="</table>";

			$("#right-top").hide();
			$("#right-top").html(htmlString).fadeIn('400', function() {
			
 			Materialize.toast('Query returened '+resp.numrows+' rows.', 4000, 'green') // 'rounded' is the class I'm applying to the toast

			});

	}});


});