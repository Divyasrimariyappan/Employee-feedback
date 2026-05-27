window.addEventListener('DOMContentLoaded', () => {

    const loginForm =
        document.getElementById('loginForm');

    const messageEl =
        document.getElementById('loginMessage');

    loginForm.addEventListener('submit', async (e) => {

        e.preventDefault();

        const username =
            document.getElementById('username').value;

        const password =
            document.getElementById('password').value;

        try {

            const response = await fetch('/login', {

                method: 'POST',

                headers: {
                    'Content-Type': 'application/json'
                },

                body: JSON.stringify({
                    username,
                    password
                })

            });

            const result = await response.json();

            if(result.success){

                messageEl.textContent =
                    'Login Successful';

                setTimeout(() => {

                    window.location.href = '/form';

                }, 1000);

            }

            else{

                messageEl.textContent =
                    result.message;
            }

        }

        catch(error){

            messageEl.textContent =
                'Error during login';
        }

    });

});