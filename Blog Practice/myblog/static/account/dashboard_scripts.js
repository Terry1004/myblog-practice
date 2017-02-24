$(function(){

	//add csrf_token to ajax header

	function getCookie(c_name)
	{
		if (document.cookie.length > 0)
		{
			c_start = document.cookie.indexOf(c_name + "=");
			if (c_start != -1)
			{
				c_start = c_start + c_name.length + 1;
				c_end = document.cookie.indexOf(";", c_start);
				if (c_end == -1) c_end = document.cookie.length;
				return unescape(document.cookie.substring(c_start,c_end));
			}
		}
		return "";
	}


	$.ajaxSetup({
		headers: { "X-CSRFToken": getCookie("csrftoken") }
	});

	//setup complete


	//delete a blog as user clicks
	
	$(document).on("click", ".blog-delete", function(){
		$.ajax({
			url: "ajax/delete-blog",
			data: {"blog_id": $(this).attr("name")},
			dataType: "json",
			success: function(data){
				if (data["status"] == "successful"){
					alert("You have successfully delete your blog!");
					$("#blogs").load(location.href + " #blogs");
				}
				else if (data["status"] == "unauthorized"){
					alert("You are not authorized to delete this blog. Please log in first.");
				}
				else {
					alert("There is some error when deleting your blog. Please try again.");
				}
			}
		})
	})


	//alter the text and like status of a blog

	$(document).on("click", ".blog-like", function(){
		var blogId = $(this).attr("name");
		var likeCountId = "#blog-like-count-" + blogId;
		$.ajax({
			url: "ajax/like-blog",
			data: {"blogId": blogId},
			dataType: "json",
			context: this,
			success: function(data){
				if (data["status"] == "like"){
					$(this).addClass("like");
					alert("You have liked this blog!");
				}
				else if (data["status"] == "unlike"){
					$(this).removeClass("like");
					alert("You have unliked this blog!");
				}
				else if (data["status"] == "unauthorized"){
					alert("You must log in first.");
				}
				else {
					alert("There is some error when liking this blog. Please try again.");
				}
				$(likeCountId).load(location.href + " " + likeCountId);
			}
		})
	})


	//given a comment id to return the corresponding blog id

	function commentToBlogId(commentId){
		var commentBoxId = "#comment-box-" + commentId;
		var commentsBoxId = $(commentBoxId).parent().parent().attr("id");
		var blogId = commentsBoxId.split("-")[2];
		return blogId;
	}


	//add comments to either a blog or a comment

	function addComment(){
		var commentForm = $("#comment-form-container");

		if (arguments.length == 0){
			var blogBoxId = commentForm.prev().attr("id");
			var blogId = blogBoxId.split("-")[2];
			var commentsBoxId = "#comments-box-" + blogId;
			$.ajax({
				url: "ajax/add-comment/",
				type: "POST",
				data: {
					"replyTo": "None", 
					"commentContent": $("#id_comment_content").val(),
					"blogId": blogId
				},
				success: function(){
					alert("You have successfully add your comment!");
					commentForm.remove();
					$(".blog-comment").prop("disabled", false);
					$(".comment-reply").prop("disabled", false);
					$(commentsBoxId).load(location.href + " " + commentsBoxId);
				}
			})
		}
		else if (arguments.length == 1){
			var commentId = arguments[0];
			var commentsBoxId = commentForm.parent().parent().attr("id");
			var blogId = commentToBlogId(commentId);
			var commentsBoxId = "#comments-box-" + blogId;
			$.ajax({
				url: "ajax/add-comment/",
				type: "POST",
				data: {
					"replyTo": commentId,
					"commentContent": $("#id_comment_content").val()
				},
				success: function(){
					alert("You ave successfully add your reply!");
					commentForm.remove();
					$(".blog-comment").prop("disabled", false);
					$(".comment-reply").prop("disabled", false);
					$(commentsBoxId).load(location.href + " " + commentsBoxId);
				}
			})
		}
	}


	//main function for adding comment boxes as users click the buttons

	function addCommentBox(commentType){
		function addComment(){
			$(".blog-comment").prop("disabled", true);
			$(".comment-reply").prop("disabled", true);
			var Id = $(this).attr("name");
			var boxId;
			if (commentType == "comment"){
				boxId = "#blog-box-" + Id; 
			}
			else {
				boxId = "#comment-box-" + Id;
			}
			$(boxId).after(
				$("<div/>").attr(
					"id", "comment-form-container").load(
					commentType + "-form"))
		}
		return addComment
	}


	//this part is controlling how to add comments to a blog

	$(document).on("click", ".blog-comment", addCommentBox("comment"));

	$(document).on("submit", "#comment-form", function(e){
		e.preventDefault();
		addComment();
	})

	//complete


	//this part is controlling how to add comments to another comment

	$(document).on("click", ".comment-reply", addCommentBox("comment-reply"));

	$(document).on("submit", "#comment-reply-form", function(e){
		e.preventDefault();
		var commentBoxId = $("#comment-form-container").prev().attr("id");
		var commentId = commentBoxId.split("-")[2];
		addComment(commentId);
	})

	//complete


	//remove the comment form when user clicks cancel button

	$(document).on("click", "#cancel-comment", function(){
		$("#comment-form-container").remove();
		$(".blog-comment").prop("disabled", false);
		$(".comment-reply").prop("disabled", false);
	})


	//delete a comment

	$(document).on("click", ".comment-delete", function(){
		var commentId = $(this).attr("name");
		var blogId = commentToBlogId(commentId);
		var commentsBoxId = "#comments-box-" + blogId;
		$.ajax({
			url: "ajax/delete-comment",
			data: {"commentId": commentId},
			dataType: "json",
			success: function(data){
				if(data["status"] == "successful"){
					alert("You have successfully delete your comment!");
					$(commentsBoxId).load(location.href + " " + commentsBoxId);
				}
				else if (data["status"] == "unauthorized"){
					alert("You are not authorized to delete!");
				}
				else{
					alert("There is some error when deleting your comment. Please try again.");
				}
			}
		})
	})
})