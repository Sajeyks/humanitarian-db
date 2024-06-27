document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const listItems = document.querySelectorAll('.searchable');
    const activeTagsContainer = document.getElementById('activeTags');
    let activeTags = new Set();

    function updateList() {
        const searchTerm = searchInput.value.toLowerCase();

        listItems.forEach(item => {
            const name = item.dataset.name.toLowerCase();
            const place = (item.dataset.place || '').toLowerCase();
            const tags = Array.from(item.querySelectorAll('.tag')).map(tag => tag.textContent.toLowerCase());
            
            const matchesSearch = name.includes(searchTerm) || place.includes(searchTerm);
            const matchesTags = activeTags.size === 0 || tags.some(tag => activeTags.has(tag));

            if (matchesSearch && matchesTags) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('input', updateList);

    document.querySelectorAll('.tag').forEach(tag => {
        tag.addEventListener('click', function() {
            const tagText = this.textContent.toLowerCase();
            if (activeTags.has(tagText)) {
                activeTags.delete(tagText);
                this.style.opacity = '1';
            } else {
                activeTags.add(tagText);
                this.style.opacity = '0.5';
            }
            updateActiveTagsDisplay();
            updateList();
        });
    });

    function updateActiveTagsDisplay() {
        activeTagsContainer.innerHTML = '';
        activeTags.forEach(tag => {
            const tagElement = document.createElement('span');
            tagElement.textContent = tag;
            tagElement.classList.add('tag', `tag-${tag.replace(' ', '-')}`);
            tagElement.addEventListener('click', function() {
                activeTags.delete(tag);
                updateActiveTagsDisplay();
                updateList();
            });
            activeTagsContainer.appendChild(tagElement);
        });
    }

    // Image modal
    const imageModal = document.getElementById('imageModal');
    imageModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const imgSrc = button.getAttribute('data-src');
        const modalImage = imageModal.querySelector('.modal-image');
        modalImage.src = imgSrc;
    });
});