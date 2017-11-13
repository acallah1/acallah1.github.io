function Dropdown(){
	this.createDropdown = function(dict, id, selected) {
		this.item = document.createElement("SELECT");
		this.item.id = id;
		for( var key in dict){
			option = document.createElement("OPTION");
			option.value = key;
			option.innerHTML = dict[key];
			if(option.value == selected){
				option.selected = "selected"
			}
			this.item.appendChild(option);
		}
	}
	
	this.getSelected = function(){
		return this.item.options[this.item.selectedIndex].value;
	}
}


function Label(){
	this.createLabel = function(text,id){
				this.item = document.createElement("p");
				this.item.id = id;
				this.item.innerHTML = text;
	}
	
	this.setText = function(text){
		this.item.innerHTML = text;
	}
}

function Item(){
	this.addToDocument = function(){
		document.body.appendChild(this.item);
	}
}

function Button(){
	this.createButton = function(text,id){
				this.item = document.createElement("BUTTON");
				this.item.id = id;
				this.item.innerHTML = text;
	}
	this.addClickEventHandler = function(handler,args){
		function inner(){
			handler(args)
		}
		this.item.onmouseup = inner;
	}
}
