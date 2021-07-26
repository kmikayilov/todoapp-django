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

const toggleSideNav = (className) => {
    curWrapper = document.querySelector(`.${className}`)
    toggleIcon = curWrapper.querySelector('.toggle-icon')
    navItems = curWrapper.querySelector('.nav-items')

    if (navItems.style.height === "0px" || navItems.style.height === "") {
        navItems.style.height = "fit-content"
        toggleIcon.style.transform = 'rotate(0deg)' 
    } else {
        navItems.style.height = "0px"
        toggleIcon.style.transform = 'rotate(-90deg)' 
    }
}