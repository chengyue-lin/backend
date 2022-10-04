//
//  AuthenticationVIew.swift
//  book-firebase
//
//  Created by Ian on 2022/5/11.
//

import SwiftUI
import Firebase
import GoogleSignIn

struct AuthenticationView: View {
    
    @State var email = ""
    @State var password = ""
    
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 30)
                .fill(Color.purple)
                .padding()
            
            VStack(spacing: 30) {
                
                Text("Authentication")
                    .font(.title)
                Spacer()
                
                TextField("Email", text: $email)
                    .textFieldStyle(.roundedBorder)
                SecureField("Password", text: $password)
                    .textFieldStyle(.roundedBorder)
                
                // Sign In
                Button(action: {
                    login()
                }) {
                    Text("Sign In")
                }
                .tint(.black)
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
                
                // Sign Up
                Button(action: {
                    signUp()
                }) {
                    Text("Sign Up")
                }
                .tint(.black)
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
                
                Button(action: {
                    google()
                }) {
                    Text("Google sign in")
                }
                .tint(.black)
                .buttonStyle(.borderedProminent)
                .controlSize(.large)
            }
            .padding(50)
        }
    }
    
    func google(){
        //https://blog.codemagic.io/google-sign-in-firebase-authentication-using-swift/
        guard let clientID = FirebaseApp.app()?.options.clientID else { return }
            
        let configuration = GIDConfiguration(clientID: clientID)
            
        guard let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene else { return }
        guard let rootViewController = windowScene.windows.first?.rootViewController else { return }
            
        GIDSignIn.sharedInstance.signIn(with: configuration, presenting: rootViewController) { (user, error) in
            if error != nil {
                print("Error signing up")
            } else {
                guard let authentication = user?.authentication, let idToken = authentication.idToken else{return}
                let credential = GoogleAuthProvider.credential(withIDToken: idToken, accessToken: authentication.accessToken)
                Auth.auth().signIn(with: credential){ (user, error) in
                    if error != nil {
                        print("Error signing up")
                    } else {
                        print("Success Sign in with Google.")
                    }
            }
        }
        }
    }
    
    // Signup to firebase
    func signUp() {
        Auth.auth().createUser(withEmail: email,
                               password: password) { (result, error) in
            if error != nil {
                print("Error signing up")
            } else {
                print("We have a new user: \(result?.user.uid ?? "no cred") ")
                let user = Auth.auth().currentUser
                user?.sendEmailVerification()
                print("The email verification sent!~")
            }
        }
    }
    
    // Login to firebase
    func login() {
        Auth.auth().signIn(withEmail: email,
                           password: password) { (result, error) in
            
            if error != nil {
                print("🔐 \(String(describing: error?.localizedDescription))")
            } else {
                print("🔐 SUCCESS")
                print("\tToken for API KEY: \(result?.user.uid ?? "no cred")")
            }
        }
    }
}




struct AuthenticationView_Previews: PreviewProvider {
    static var previews: some View {
        AuthenticationView()
    }
}

