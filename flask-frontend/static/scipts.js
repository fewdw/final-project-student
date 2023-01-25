function updateStudentDegree(name,desc,id){
    let degreeNameInputField = document.getElementById("degreeNameInputField");
    let degreeDescriptionInputField = document.getElementById("degreeDescriptionInputField");
    let degreeIdFormInput = document.getElementById("degreeIdFormInput");

    degreeIdFormInput.value = id.toString();
    degreeNameInputField.value = name.toString();
    degreeDescriptionInputField.value = desc.toString();
}

function updateStudentProject(name,desc,id){
    let projectNameInputField = document.getElementById("projectNameInputField");
    let projectDescriptionInputField = document.getElementById("projectDescriptionInputField");
    let projectIdFormInput = document.getElementById("projectIdFormInput");

    projectIdFormInput.value = id.toString();
    projectNameInputField.value = name.toString();
    projectDescriptionInputField.value = desc.toString();
}


//enter function to update project here.