createBtn = document.querySelector('.create-poll')
question = document.getElementById('question')
ansOne = document.getElementById('possible-answer-one')
ansTwo = document.getElementById('possible-answer-two')
ansThree = document.getElementById('possible-answer-three')
ansFour = document.getElementById('possible-answer-four')
correctAns = document.getElementById('correct-answer')

createBtn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log(question.value, ansOne.value, ansTwo.value, ansThree.value, ansFour.value, correctAns.value);
    fetch(
        '/create-poll',
        {
            method: 'POST',
            headers: {
                'Content-Type':
                    'application/json;charset=utf-8'
            },
            body: JSON.stringify({
                question: question.value,
                firstAns: ansOne.value,
                secondAns: ansTwo.value,
                thirdAns: ansThree.value,
                fourthAns: ansFour.value,
                correctAns: correctAns.value
            })
        }
    )
})