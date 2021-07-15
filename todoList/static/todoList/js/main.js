const toggleNav = () => {
	const sidebar = document.getElementById("sidebar");
	const content = document.getElementById("content");

	if (sidebar.style.width == "0px" || !sidebar.style.width) {
		sidebar.style.width = "305px";
		sidebar.style.paddingLeft = "35px";
		content.style.marginLeft = "305px";
	} else {
		sidebar.style.width = "0";
		sidebar.style.paddingLeft = "0";
		content.style.marginLeft = "0";
	}
};
