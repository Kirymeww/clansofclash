document.addEventListener('DOMContentLoaded', () => {
    const clickButton = document.getElementById('click-button');
    const counter = document.getElementById('counter');
    let count = 0;

    clickButton.addEventListener('click', () => {
        count++;
        counter.textContent = count;
    });
});
