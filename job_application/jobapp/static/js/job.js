document.addEventListener('DOMContentLoaded', function() {
    const currentlyWorkingCheckbox = document.querySelector('#id_currently_working');
    const currentCtcContainer = document.querySelector('.current-ctc-container');

    function toggleCurrentCtcField() {
        currentCtcContainer.style.display = currentlyWorkingCheckbox.checked ? 'block' : 'none';
    }

    toggleCurrentCtcField();  // Initial state

    currentlyWorkingCheckbox.addEventListener('change', function() {
        toggleCurrentCtcField();
    });
});
