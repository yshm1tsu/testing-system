function copyToClipboard(code) {
    const el = document.createElement('textarea')
    el.style.position = 'absolute'
    el.style.left = '-9999px'
    el.value = `${document.location.host}/passTest/${code}`
    document.body.appendChild(el)
    el.select()
    document.execCommand('copy')
    document.body.removeChild(el)
}

function generateQuestionTemplate(index) {
    return `
        <div class="mb-5 test-creation-form__question form__wrapper" id="question_form_${index}" data-options=1>
            <input type="hidden" name="question_form_options_index_${index}" value=1  id="question_form_options_index_${index}" />
            <div class="mb-4">
                <label for="question_title_${index}">Текст вопроса</label>
                <textarea id="question_title_${index}" class="form-control" name="question_title_${index}"></textarea>
            </div>
            <div class="mb-4">
                <label for="question_points_${index}">Кол-во баллов за вопрос</label>
                <input type="number" class="form-control" id="question_points_${index}" name="question_points_${index}" />
            </div>
            <div class="mb-4">
                <p>Варианты ответа</p>
                <table class="table">
                    <tr>
                        <th>Текст</th>
                        <th class="text-center">Верно</th>
                        <th></th>
                    </tr>
                </table>
                <div class="text-center question-form__add-option-btn">
                    <svg onClick="addQuestionOption(${index})" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-plus-circle-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4a.5.5 0 0 0-1 0v3.5H4a.5.5 0 0 0 0 1h3.5V12a.5.5 0 0 0 1 0V8.5H12a.5.5 0 0 0 0-1H8.5V4z"/>
                    </svg>
                </div>
            </div>
            <div class="text-center">
                <button type="button" class="btn btn-danger" onClick="deleteQuestionForm(${index})">Удалить</button>
            </div>
        </div>
    `
}

function generateOptionTemplate(index, opt_index) {
    return `
        <td>
            <input type="text" class="form-control col-8" name="question_option_${index}_${opt_index}"/>
        </td>
        <td>
            <input type="radio" class="form-check-input col-4" value="false" name="question_option_is_correct_${index}" />
        </td>
        <td class="test-creation-form__question__delete-icon" onClick="deleteQuestionOption(${index}, ${opt_index})">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x-circle-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-4.146-3.146a.5.5 0 0 0-.708-.708L8 7.293 4.854 4.146a.5.5 0 1 0-.708.708L7.293 8l-3.147 3.146a.5.5 0 0 0 .708.708L8 8.707l3.146 3.147a.5.5 0 0 0 .708-.708L8.707 8l3.147-3.146z"/>
            </svg>
        </td>
    `
}

const questionForms = document.getElementById('question-forms')
let questionFormsCount = 0
let questionFormsIndex = 0

const optionsIndex = new Map()
const optionsCount = new Map()

function addQuestionForm() {
    const div = document.createElement('div')
    div.innerHTML = generateQuestionTemplate(questionFormsIndex)
    questionForms.appendChild(div)
    optionsIndex.set(questionFormsIndex, 0)
    optionsCount.set(questionFormsIndex, 0)
    addQuestionOption(questionFormsIndex)
    questionFormsIndex++
    questionFormsCount++
    if (questionFormsCount >= 1) {
        document.getElementById('test-creation-submit').disabled = false
    }
    document.getElementById('question_max_index').value = questionFormsIndex
}

function deleteQuestionForm(index) {
    const questionForm = document.getElementById(`question_form_${index}`)
    questionForm.remove()
    optionsIndex.delete(index)
    optionsCount.delete(index)
    questionFormsCount--
    if (questionFormsCount <= 0) {
        document.getElementById('test-creation-submit').disabled = true
    }
    document.getElementById('question_max_index').value = questionFormsIndex
}

function addQuestionOption(index) {
    if (optionsCount.get(index) === 5) {
        return
    }
    const questionForm = document.getElementById(`question_form_${index}`)
    const tr = document.createElement('tr')
    tr.id = `question_option_${index}_${optionsIndex.get(index)}`
    tr.innerHTML = generateOptionTemplate(index, optionsIndex.get(index))
    questionForm.querySelector('table tbody').appendChild(tr)
    optionsIndex.set(index, optionsIndex.get(index) + 1)
    optionsCount.set(index, optionsCount.get(index) + 1)
    document.getElementById(`question_form_options_index_${index}`).value = optionsIndex.get(index)
}

function deleteQuestionOption(index, opt_index) {
    if (optionsCount.get(index) === 1) {
        return
    }
    const el = document.getElementById(`question_option_${index}_${opt_index}`)
    el.remove()
    optionsCount.set(index, optionsCount.get(index) - 1)
}

const createTestForm = document.getElementById('createTestForm')
createTestForm && createTestForm.addEventListener('submit', onCreateTestSubmit)

function onCreateTestSubmit(event) {
    const formData = new FormData(createTestForm)
    event.preventDefault()
    document.querySelectorAll(`#${createTestForm.id} input, #${createTestForm.id} textarea`).forEach(el => el.classList.remove('error'))
    document.querySelectorAll(`input[type="radio"]`).forEach(element => element.value = element.parentElement.previousElementSibling.children[0].value)
    validateCreateForm(formData)
}

async function validateCreateForm(formData) {
    const data = await request('/validateCreateTest/', 'POST', formData)
    if (data.success === false) {
        data.errors.forEach(el => {
            document.querySelector(`input[name=${el}], textarea[name=${el}]`).classList.add('error')
        })
    } else {
        createTestForm.submit()
    }
}

const passTestForm = document.getElementById('passTestForm')
passTestForm && passTestForm.addEventListener('submit', onPassTestSubmit)

function onPassTestSubmit(event) {
    const formData = new FormData(passTestForm)
    event.preventDefault()
    if (formData.get('name')) {
        passTestForm.submit()
    } else {
        document.querySelector('input[name="name"]').classList.add('error')
    }
}

function join(el) {
    const code = document.getElementById('join-code').value
    const link = `/passTest/${code}`
    window.location.href = link
}

async function request(url, method = 'GET', body = null) {
    const response = await fetch(url, {method, body})
    const json = await response.json()
    return json
}