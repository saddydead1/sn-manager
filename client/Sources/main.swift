import SocketIO
import Foundation

let addr = URL(string: "http://127.0.0.1:7072")!

let manager = SocketManager(socketURL: addr, config: [.log(true), .compress])
let socket = manager.defaultSocket

socket.on(clientEvent: .connect) {data, ack in
    if(socket.status == .connected) {
        print("socket connected")
    }
}

socket.connect()
