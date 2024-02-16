function sortThreads() {
    var select = document.querySelector('.sort-select');
    var selectedOption = select.options[select.selectedIndex].textContent;
    var threadGrid = document.getElementById('thread-grid');
    var threads = threadGrid.querySelectorAll('.thread-window');

    var sortedThreads = Array.from(threads);

    if (selectedOption === "По бампам") 
    {
        sortedThreads.sort(function(a, b) 
        {
            return parseInt(a.getAttribute('data-all-posts')) - parseInt(b.getAttribute('data-all-posts'));
        });
    } else if (selectedOption === "По времени") 
    {
        sortedThreads.sort(function(a, b) {
            return new Date(a.getAttribute('data-creation-time')) - new Date(b.getAttribute('data-creation-time'));
        });
    } else if (selectedOption === "По постам") 
    {
        sortedThreads.sort(function(a, b) {
            return a.textContent.localeCompare(b.textContent);
        });
    }

    for (var i = 0; i < sortedThreads.length; i++) 
    {
        threadGrid.appendChild(sortedThreads[i]);
    }
}