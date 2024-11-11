
document.querySelectorAll('img').forEach(img => {
    img.onerror = function () {
        this.onerror = null;
        this.src = '../js/default.jpg'; 
        this.alt = "default athlete image"; 
    };

    if (img.naturalWidth === 0) {
        img.onerror();
    }
});

