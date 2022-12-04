dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
# a=dict1.values()
# print(a)
print(dict1.get("class",{}).get("student",{}).get("marks",{}).get("web"))
