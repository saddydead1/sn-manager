import SocketIO
import Foundation

let addr = URL(string: "http://127.0.0.1:7072")!

class SocketHandler: NSObject {
    
    static let sharedInstance = SocketHandler()
    let manager = SocketManager(socketURL: addr, config: [.log(true), .compress])
    var Socket: SocketIOClient!
    
    override init() {
        super.init()
        Socket = manager.defaultSocket
        Socket.on("connect", callback: { (data, ack) in
                    debugPrint(" ===== socket connected =====")
                })
    }
    
    func getSocket() -> SocketIOClient {
        return Socket
    }
    
    func Connect() {
        Socket.connect()
    }
}
