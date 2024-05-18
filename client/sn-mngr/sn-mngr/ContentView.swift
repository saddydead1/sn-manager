//
//  ContentView.swift
//  sn-mngr
//
//  Created by saddydead on 16.05.2024.
//

import SwiftUI


struct ContentView: View {
    @Bindable var viewMod: LoginViewModel
    
    var body: some View {
        VStack {
            if !viewMod.auth {
                Text("Sonoma Manager v3").font(.title2)
                
                VStack(spacing: 15){
                    TextField("Логин", text: $viewMod.user.name)
                        .customStyle()
                    SecureField("Пароль", text: $viewMod.user.pass)
                        .customStyle()
                }
            
                Button("Войти") {
                    viewMod.login()
                }
            } else {
                Text("123")
                
                Button("Выйти") {
                    viewMod.logout()
                }
            }
        
        }
        .padding()
    }
}

#Preview {
    ContentView(viewMod: LoginViewModel())
}


struct StyleView: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .frame(width: 300, height: 40)
            .background(.gray.opacity(0.03))
            .clipShape(RoundedRectangle(cornerRadius: 10))
    }
    
    
}

extension View {
    func customStyle() -> some View {
        modifier(StyleView())
    }
}
