
function togglePostingForm(index)
{
    var form = document.getElementById("posting-form" + index)
    var button1 = document.getElementById("posting-button1")
    var button2 = document.getElementById("posting-button2")

    if (form.style.display === "none") 
    {
        form.style.display = "inline-block"; // Показываем div
        button.textContent = "Закрыть форму постинга"
    } 

    else 
    {
        form.style.display = "none"; // Скрываем div
        button.textContent = "Ответить в тред"
    }
}


function reply(id)
{
    post = document.getElementById(id)
    var form = document.getElementById("posting-form2")
    form_text = document.getElementById("posting-form-text")

    form_text.value += "<<" + id + "\n"
    
    form.style.display = "inline-block"
    form_text.focus()
}

function edit()
{   
    form_text = document.getElementById("46")
    form_text.value.replace(/\n/g, '<br/>');
}

