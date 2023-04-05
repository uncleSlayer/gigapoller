const loginBtn = document.querySelector('#login-btn')
const email = document.querySelector('#email')
const password = document.querySelector('#password')

const sendLoginInfo = async () => {
    fetch(
        '/login-auth',
        {
            method: 'POST',
            body: JSON.stringify(
                {
                    email: email.value,
                    password: password.value
                }
            ),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }
    )
    .then(
        (resp)=>{
            if(resp.status == 200){
                window.location.href = "/home"
            }
        }
    )
}

loginBtn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log(email.value, password.value);
    sendLoginInfo()
})