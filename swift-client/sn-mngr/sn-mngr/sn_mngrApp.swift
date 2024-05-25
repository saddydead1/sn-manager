//
//  sn_mngrApp.swift
//  sn-mngr
//
//  Created by saddydead on 16.05.2024.
//

import SwiftUI

@main
struct sn_mngrApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView(viewMod: LoginViewModel())
        }
    }
}
