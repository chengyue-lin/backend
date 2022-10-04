//
//  addImageView.swift
//  book-firebase
//
//  Created by Ian on 2022/5/13.
//

import SwiftUI
import Firebase
import FirebaseStorage

struct addImageView: View {
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 30)
                .fill(Color.blue)
                .padding()
            
            VStack(spacing: 30) {
                Spacer()
                Text("Add Image")
                    .font(.title)
                Spacer()
                
                
                Button(action: {
                    upload()
                }) {
                    Text("upload image")
                }
                .tint(.black)
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
                Spacer()
                Text("Crashlytics")
                    .font(.title)
                Spacer()
                
                
                Button("Crash"){
                    fatalError("Crash was triggered")
                }
                .tint(.black)
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
                Spacer()
            }
        }
    }
    func upload() {
        let storage = Storage.storage()
        //upload the image in the local path
        guard let localImage = Bundle.main.url(forResource: "dog3", withExtension: "jpg") else { return }
        let ref = storage.reference().child("image/dog3.jpg")
        
        ref.putFile(from: localImage, metadata: nil) {
            (_, error) in
            if let error = error {
                print("Error upload image: \(error)")
            } else {
                print("Image successfully uploaded!")
            }
        }
    }
}

struct addImageView_Previews: PreviewProvider {
    static var previews: some View {
        addImageView()
    }
}
