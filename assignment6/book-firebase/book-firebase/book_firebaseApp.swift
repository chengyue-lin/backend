//
//  book_firebaseApp.swift
//  book-firebase
//
//  Created by Ian on 2022/5/11.
//

import SwiftUI
import Firebase

@main
struct book_walkthroughApp: App {
    
    @StateObject var firestoreManager = FirestoreManager()
  
    init() {
        FirebaseApp.configure()
    }
    
    var body: some Scene {
        WindowGroup {
            MainTabView()
                .environmentObject(firestoreManager)
        }
    }
}
