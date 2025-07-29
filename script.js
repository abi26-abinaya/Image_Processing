document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const imageInput = document.getElementById('imageInput');
    const filterSelect = document.getElementById('filterSelect');

    if (!imageInput.files.length) {
        alert("Please select an image to upload.");
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);
    formData.append('filter', filterSelect.value);

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.filename) {
            const imageURL = `http://127.0.0.1:5000/processed/${data.filename}`;
            const filteredImage = document.getElementById('filteredImage');
            filteredImage.src = imageURL;
            filteredImage.style.display = 'block';
        } else {
            alert('Error from server: ' + JSON.stringify(data));
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        alert("Failed to upload image. Is the Flask server running?");
    });
});
