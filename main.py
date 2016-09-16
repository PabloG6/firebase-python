#demo


import firebase
from firebase.reference import database
from firebase.app.App import Firebase
firebaseConnection = Firebase.firebase("testing-6aa1e.firebaseio.com")


mainRef = database.database(firebaseConnection).ref("path").ref("to").ref("data").push({"data":"data"})
mainRef.get()