//
//  MainTabView.swift
//  book-firebase
//
//  Created by Ian on 2022/5/11.
//

import SwiftUI

struct MainTabView: View {
    var body: some View {
        TabView {
            AuthenticationView()
            BooksView()
            addImageView()
        }
        .tabViewStyle(PageTabViewStyle(indexDisplayMode: .always))
    }
}

struct MainTabView_Previews: PreviewProvider {
    static var previews: some View {
        MainTabView()
    }
}
