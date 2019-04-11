from firebase import firebase

# FBConn=firebase.FirebaseApplication('https://fir-1-cd562.firebaseio.com/')

FBConn=firebase.FirebaseApplication('https://cm-2d863.firebaseio.com/')


while True:
    temp=int(input("what is the temp?"))
    data_to_upload={
        "Temp":temp
    }

    result=FBConn.post("/MyTestData/",data_to_upload)

    print(result)