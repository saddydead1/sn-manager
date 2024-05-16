//
//  ContentView.swift
//  sn-mngr
//
//  Created by saddydead on 16.05.2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Sonoma Manager v3").font(.title2)
            Button("test") {
                print(123)
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
