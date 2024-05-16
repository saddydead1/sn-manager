import Foundation
import AsyncHTTPClient


let addr = "http://127.0.0.1:7072"

var request = HTTPClientRequest(url: addr)
let response = try await HTTPClient.shared.execute(request, timeout: .seconds(30))
print("HTTP head", response)
if response.status == .ok {
    let body = try await response.body.collect(upTo: 1024 * 1024) // 1 MB

} else {
    // handle remote error
}
