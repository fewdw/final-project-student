    # put test
    def test_put_should_work(self):
        url = "http://127.0.0.1:5000/students/"
        payload = {
            "id": "63a13a5da4acd21e65360820",
            "student_id":"UPDATEDupdated-student_id",
            "status" : "UPDATEDstatus",
            "first_name" : "UPDATEDfirst_name",
            "last_name" : "UPDATEDlast_name",
            "email" : "UPDATEDemail",
            "gender" :  "UPDATEDgender",
            "professor_name" : "UPDATEDprofessor_name",
            "year_of_graduation" : "UPDATEDyear_of_graduation",
            "degree" : "degree",
            "projectId" : "projectId",
            "programming_language" : "UPDATEDprogramming_language"    
        }
        



if __name__ == '__main__':
    unittest.main()
