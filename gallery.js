const images = [
  'images/gallery/FETUSSSSSSS66666SJHJHJS40994898989089064.png',
  
  
  'images/gallery/CRINGE_02.png',
  'images/gallery/fucky_coloros_SAVU0.png',
  
  
  
  
  
  'images/gallery/marie_666.png',
  'images/gallery/sdg9uidsf9g8sdfudgf.png',
  'images/gallery/dsasadsadsdasdadasdadsdssds_transpaas.png',
  'images/gallery/mael_05_out_01dsasasads.png',
  'images/gallery/Screenshotdsasds 2025-11-06 16fgfgfg3343.png',
  'images/gallery/dsfadfasffffffffffffffffffasdf.png',
  'images/gallery/monk_06.png',

  
  
];

function loadGallery() {
    const container = document.querySelector('.gallery-container');
    if (!container) return;
    
    // Create one row per image (not 2 images per row)
    for (let i = 0; i < images.length; i++) {
        const row = document.createElement('div');
        row.className = 'gallery-row';
        
        const img = document.createElement('img');
        img.src = images[i];
        img.className = 'gallery-img';
        row.appendChild(img);
        
        container.appendChild(row);
    }
}

document.addEventListener('DOMContentLoaded', loadGallery);