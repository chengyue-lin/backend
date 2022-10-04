//
//  FirstoreManager.swift
//  book-firebase
//
//  Created by Ian on 2022/5/11.
//

import Foundation
import Firebase
import FirebaseFirestore

class FirestoreManager: ObservableObject {

    init() {
        print("Firestore Manager is initialized")
    }
    
    func fetchAllBooks() {
        let db = Firestore.firestore()
        
        db.collection("books").getDocuments() { (querySnapshot, error) in
            if let error = error {
                print("Error getting documents: \(error)")
            } else {
                for document in querySnapshot!.documents {
                    print("\(document.documentID): \(document.data())")
                }
            }
        }
    }
    
    func createBook() {
        let db = Firestore.firestore()
        let isbn = "000000002"
        let docRef = db.collection("books").document(isbn)
        
        docRef.setData(["title": "The Cather in the Rye: 2", "author_lastname": "Saligner", "author_first": "J.D."]) { error in
            if let error = error {
                print("Error writing document: \(error)")
            } else {
                print("📝 Document successfully written!")
            }
        }
    }
    
    func updateBook() {
        let db = Firestore.firestore()
        let isbn = "000000002"
        let docRef = db.collection("books").document(isbn)
        
        docRef.updateData(["title": "The Cather in the Rye 2: This time its personal!", "author_first": "J.D."]) { error in
            if let error = error {
                print("Error updating document: \(error)")
            } else {
                print("📝 Document successfully updated!")
            }
        }
        
    }
    
    func deleteBook() {
        let db = Firestore.firestore()
        let isbn = "000000002"
        let docRef = db.collection("books").document(isbn)
        
        docRef.delete()
    }
   
    
}
