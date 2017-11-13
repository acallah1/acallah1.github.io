var mid;
function loadRec(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student04.cse.nd.edu:51020/recommendations/101",true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log(xhr.responseText);
			var result = JSON.parse(xhr.responseText);
			mid = result["movie_id"];
			document.getElementById("title").innerHTML = result["movie_id"];
			loadRating();
			loadMovie();
		}
	}
	xhr.send(null);
}

function loadRating(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student04.cse.nd.edu:51020/ratings/"+mid, true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			var result = JSON.parse(xhr.responseText);
			document.getElementById("rating").innerHTML = result["rating"];
		}
	}	                 
	xhr.send(null);
	
}
function loadMovie(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student04.cse.nd.edu:51020/movies/"+mid,true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			var result = JSON.parse(xhr.responseText);
			document.getElementById("title").innerHTML = result["title"];
		    document.getElementById("image").src = "http://student04.cse.nd.edu/skumar5/images" + result["img"];
		}
	}
	
	xhr.send(null);

}

function sendVote(rating){
	var xhr = new XMLHttpRequest();
	xhr.open("PUT", "http://student04.cse.nd.edu:51020/recommendations/101", true);
	xhr.onreadystatechange = function() {
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log(xhr.responseText);
			loadRec();
		}
	}
	dict = {"rating" : rating, "movie_id" : mid}
	xhr.send(JSON.stringify(dict));	
}

window.onload = function(){
	loadRec();
}

document.getElementById("upbutton").addEventListener("click", function(){
	sendVote(5);
});
document.getElementById("downbutton").addEventListener("click", function(){
    sendVote(1);
});
