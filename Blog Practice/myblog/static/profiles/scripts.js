$(function(){
	function toggleText(){
		$.ajax({
			url: "ajax/toggle-follow",
			data: {"follow_change_to": $("#follow-button").text().trim()},
			dataType: "json",
			success: function(data){
				if (data["current_follow_status"] == "following"){
					$("#follow-button").text("- Unfollow");
				}
				else if (data["current_follow_status"] == "not following"){
					$("#follow-button").text(" + Follow");
				}
				else{
					alert("You should log in first!");
				}
			},
			error: function(){
				alert('error!');
			}
		})
	}

	$("#follow-button").on("click", toggleText);

});