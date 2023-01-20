function updateStudentDegree(name,desc,id){
    let degreeNameInputField = document.getElementById("degreeNameInputField");
    let degreeDescriptionInputField = document.getElementById("degreeDescriptionInputField");
    let degreeIdFormInput = document.getElementById("degreeIdFormInput");

    degreeIdFormInput.value = id.toString();
    degreeNameInputField.value = name.toString();
    degreeDescriptionInputField.value = desc.toString();
}


//enter function to update project here.