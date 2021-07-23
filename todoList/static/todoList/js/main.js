const toggleNav = () => {
	const sidebar = document.getElementById("sidebar");
	const content = document.getElementById("content");

	if (sidebar.style.width == "0px") {
		sidebar.style.width = "305px";
		content.style.marginLeft = "305px";
		sidebar.style.paddingLeft = "35px";
	} else {
		sidebar.style.width = "0";
		content.style.marginLeft = "0";
		sidebar.style.paddingLeft = "0";
	}
};


const setActive = () => {
	anchors = document.querySelectorAll('.nav-item');
	for(i=0; i<anchors.length; i++) { 
	  if(document.location.href.indexOf(anchors[i].querySelector('a').href)>=0) {
		anchors[i].classList.add("active");
	  }
	}
}
  
window.onload = setActive;


const toggleTaskForm = () => {
	let isClosed = false
	const form = document.querySelector(".new-task-form");
	form.classList.forEach(c => isClosed = c === 'closed' ? true : false );

	if (isClosed) {
		form.classList.remove('closed');
		form.querySelector("input[name='task']").focus()
	}
	else form.classList.add('closed')
	
}
