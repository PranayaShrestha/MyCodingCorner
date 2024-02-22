document.addEventListener('DOMContentLoaded', function() {
    // Select the header element
    var SignUp = document.getElementById('SignUp');

    // Add an event listener to track mouse movement
    document.addEventListener('mousemove', function(e) {
        // Ensure header exists before proceeding
        if (SignUp) {
            // Calculate the distance from the mouse cursor to the center of the header
            var distX = e.clientX - (header.offsetLeft + header.offsetWidth / 2);
            var distY = e.clientY - (header.offsetTop + header.offsetHeight / 2);

            // Apply a transformation to the header based on the mouse position
            header.style.transform = 'translate(' + distX / 20 + 'px, ' + distY / 20 + 'px)';
        }
    });
});
