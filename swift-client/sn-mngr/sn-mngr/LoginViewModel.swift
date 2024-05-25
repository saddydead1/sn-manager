
//
//  LoginViewMOdel.swift
//  sn-mngr
//
//  Created by saddydead on 18.05.2024.
//

import Observation

@Observable
final class LoginViewModel {
    var user = User()
    var auth = false
    
    private var sampleUser = "123"
    private var samplePass = "123"
    
    
    func login() {
        guard user.name == sampleUser, user.pass == samplePass else {
            return
        }
        
        auth.toggle()
    }
    
    func logout() {
        auth.toggle()
    }
}
