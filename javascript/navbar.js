// Get all dropdown-content ids and add hover events
var dropdownheader = document.getElementsByClassName("dropdown");
var i;

console.log(dropdownheader);

for (i = 0; i < dropdownheader.length; i++) {
    dropdownheader[i].addEventListener("mouseover", function () {
        this
            .getElementsByClassName("dropdown-content")[0]
            .style
            .display = "flex";

        this
            .getElementsByClassName("chevron-span")[0]
            .style
            .transform = "rotate(180deg)";

        this
            style.textDecoration = "underline";

    });


    dropdownheader[i].addEventListener("mouseout", function (event) {
        var dropdownContent = this.getElementsByClassName("dropdown-content")[0];
        
        // Ensure we don't hide the dropdown if the mouse moves to the dropdown content
        if (!dropdownContent.contains(event.relatedTarget) && !this.contains(event.relatedTarget)) {
            dropdownContent.style.display = "none";

            this
                .getElementsByClassName("chevron-span")[0]
                .style
                .transform = "rotate(0deg)";
        }
    });
}

// Handle navigation
function Gotolink(link) {
    window.location.assign(link);
}
