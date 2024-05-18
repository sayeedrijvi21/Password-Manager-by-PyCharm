document.getElementById('addPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const password = document.getElementById('password').value;

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, password }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadPasswords();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function loadPasswords() {
    fetch('/view')
        .then(response => response.json())
        .then(data => {
            const passwordList = document.getElementById('passwordList');
            passwordList.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `User: ${item.user} | Password: ${item.password}`;
                passwordList.appendChild(li);
            });
        });
}

// Load passwords on page load
window.onload = loadPasswords;
