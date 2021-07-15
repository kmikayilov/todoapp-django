const toggleNav = () => {
	const sidebar = document.getElementById("sidebar")
	const content = document.getElementById("content")

	if (sidebar.style.width == "0px" || !sidebar.style.width) {
		sidebar.style.width = "250px"
		sidebar.style.paddingLeft = "35px"
		content.style.marginLeft = "250px"
	} else {
		sidebar.style.width = "0"
		sidebar.style.paddingLeft = "0"
		content.style.marginLeft = "0"
	}
}
