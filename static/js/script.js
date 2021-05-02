AOS.init();
let stars = document.getElementById('stars');
let moon = document.getElementById('moon');
let rocket = document.getElementById('rocket');
let btn = document.getElementById('btn');
let text = document.getElementById('text');
let mountain_front = document.getElementById('mountain_front');

window.addEventListener('scroll', function () {
    let value = window.scrollY;
    stars.style.left = value * 0.25 + 'px';
    moon.style.top = value * 1.25 + 'px';
    rocket.style.left = value * 1.5 + 'px';
    mountain_front.style.right = value * 0 + 'px';
    text.style.marginRight = value * 1.75 + 'px';
    text.style.marginBottom = value * 0.15 + 'px';
    btn.style.marginTop = value * 1.5 + 'px';
});