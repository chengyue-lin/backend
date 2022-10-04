//
//  BooksView.swift
//  book-firebase
//
//  Created by Ian on 2022/5/11.
//

import SwiftUI


struct BooksView: View {
    
    @EnvironmentObject var firestoreManager: FirestoreManager
    
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 30)
                .fill(Color.yellow)
                .padding()
            
            VStack(spacing: 30) {
                Text("CRUD")
                    .font(.largeTitle)
                
                
                Button(action: {
                    firestoreManager.fetchAllBooks()
                }) {
                    Text("Download All Books")
                }
                

                Button(action: {
                    firestoreManager.createBook()
                }) {
                    Text("Create Books")
                }

                Button(action: {
                    firestoreManager.updateBook()
                }) {
                    Text("Update Book")
                }
                

                Button(action: {
                    firestoreManager.deleteBook()
                }) {
                    Text("Delete Book")
                }

            }
            .tint(.black)
            .buttonStyle(.borderedProminent)
            .controlSize(.large)
            
        }
    }
    
    
}

struct BooksView_Previews: PreviewProvider {
    static var previews: some View {
        BooksView()
    }
}
