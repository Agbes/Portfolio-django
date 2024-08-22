document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });


    // Change active link on scroll
    let ticking = false;

    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                let scrollPosition = window.scrollY;

                document.querySelectorAll('section').forEach(section => {
                    if (scrollPosition >= section.offsetTop - 150 && scrollPosition < (section.offsetTop + section.offsetHeight)) {
                        let currentId = section.attributes.id.value;
                        removeAllActiveClasses();
                        addActiveClass(currentId);
                    }
                });

                ticking = false;
            });

            ticking = true;
        }
    });

    function removeAllActiveClasses() {
        document.querySelectorAll("nav ul li a").forEach((el) => {
            el.classList.remove("active");
        });
    }

    function addActiveClass(id) {
        let selector = `nav ul li a[href="#${id}"]`;
        document.querySelector(selector).classList.add("active");
    }

    // Flip the diploma cards on click
    document.querySelectorAll('.diploma-card').forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });
    });

    // Add hover effect to skill items
    document.querySelectorAll('.skill-item').forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.transform = 'scale(1.1)';
        });

        item.addEventListener('mouseout', () => {
            item.style.transform = 'scale(1)';
        });
    });
});