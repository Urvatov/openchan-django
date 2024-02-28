
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
    var post = document.getElementById(id)

    var form_text = document.getElementById("posting-form-text")

    form_text.value += "<<" + id + "\n"
    
    form_text.focus()
}

