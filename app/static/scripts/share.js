question = document.querySelector('.question')
answer = document.querySelector('.answer')
submit = document.querySelector('.submit-btn')
flashedMessage = document.querySelector('.flashed-message-js')

submit.addEventListener(
    'click',
    () => {
        console.log(answer.value);
        fetch(
            '/share/vote',
            {
                method: 'POST',
                body: JSON.stringify({
                    question: question.placeholder,
                    answer: answer.value
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            }
        )
            .then(() => {
                flashedMessage.innerHTML = `
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
                You have successfully voted.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            `
            })
    }
)
