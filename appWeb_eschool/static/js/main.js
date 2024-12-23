document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    const organizationSlider = document.querySelector('.organization-slider');
    if (organizationSlider) {
        const organizationSplide = new Splide(organizationSlider, {
            arrows: false,
            autoplay: true,
            type: 'loop',
            perPage: 4,
            gap: 30,
            breakpoints: {
                767.98: {
                    perPage: 2,
                }
            }
        });
        organizationSplide.mount();
        console.log('Organization slider mounted');
    }

    // Inisialisasi slider utama untuk testimonial
    const testiMain = new Splide('#main-slider', {
        type: 'fade',
        pagination: false,
        arrows: false,
        perPage: 1,
        autoplay: true,
        speed: 800,
    });

    const testiThumb = new Splide('#thumbnail-slider', {
        type: 'loop',
        padding: 30,
        gap: 15,
        pagination: false,
        focus: 'center',
        perPage: 3,
        autoplay: true,
        speed: 300,
    });

    testiMain.sync(testiThumb);
    testiMain.mount();
    testiThumb.mount();
    console.log('Testimonial sliders mounted');

    // Inisialisasi lightGallery
    const lightGalleryContainer = document.getElementById('lightgallery');
    if (lightGalleryContainer) {
        lightGallery(lightGalleryContainer, {
            selector: '.gallery-img',
            download: false,
            zoom: true,
            enableDrag: true,
        });
        console.log('LightGallery initialized');
    }

    
});
