const images = [
  'images/gallery/cm_06.PNG',
  'images/gallery/dafgsetrysytry.PNG',
  'images/gallery/headdy.PNG',
  'images/gallery/pixel05.PNG',
  'images/gallery/pixel06.PNG',
  'images/gallery/pixel11.PNG',
];

function loadGallery() {
    const container = document.querySelector('.gallery-container');
    if (!container) return;
    
    for (let i = 0; i < images.length; i += 2) {
        const row = document.createElement('div');
        row.className = 'gallery-row';
        
        // First image
        const img1 = document.createElement('img');
        img1.src = images[i];
        img1.className = 'gallery-img';
        row.appendChild(img1);
        
        // Second image (if exists)
        if (images[i + 1]) {
            const img2 = document.createElement('img');
            img2.src = images[i + 1];
            img2.className = 'gallery-img';
            row.appendChild(img2);
        }
        
        container.appendChild(row);
    }
}

document.addEventListener('DOMContentLoaded', loadGallery);