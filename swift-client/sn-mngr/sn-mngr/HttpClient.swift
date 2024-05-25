import Foundation


func test() {
    let url = URL(string: "http://127.0.0.1:7072")!

    var request = URLRequest(url: url)

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        if let data = data {
            print(data)
        } else if let error = error {
            print("HTTP Request Failed \(error)")
        }
    }

    task.resume()
}
