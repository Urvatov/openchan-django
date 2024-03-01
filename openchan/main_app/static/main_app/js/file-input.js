var fileList = document.getElementById("file-list")
fileList.innerHTML = ""


function fileInput()
{
    fileList.innerHTML = ""
    var fileForm = document.getElementById("file-input")
    var files = fileForm.files
    var dataTransfer = new DataTransfer()

    for (var i = 0; i < files.length; i++)
    {
        if (i < 4)
        {
            fileList.innerHTML += "<p>" + files[i].name + "</p>"
            dataTransfer.items.add(files[i])
        }
    }

    fileForm.value = ''
    fileForm.files = dataTransfer.files
}

function addFile()
{
    
}
