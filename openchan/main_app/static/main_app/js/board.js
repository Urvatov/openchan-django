
function togglePostingForm()
{
    
    var form = document.getElementById("posting-form")
    var button = document.getElementById("posting-button")

    if (form.style.display === "none") 
    {
        form.style.display = "inline-block"; // Показываем div
        button.textContent = "Закрыть форму постинга"
    } 

    else 
    {
        form.style.display = "none"; // Скрываем div
        button.textContent = "Создать тред"
    }
}