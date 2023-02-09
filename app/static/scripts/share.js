question = document.querySelector('.question')
answer = document.querySelector('.answer')
submit = document.querySelector('.submit-btn')

submit.addEventListener(
    'click',
    () => {
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
    }
)
