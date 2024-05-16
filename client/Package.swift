// swift-tools-version:5.8

import PackageDescription

let package = Package(
    name: "socket.io-test",
    platforms: [
        .macOS(.v10_15)
    ],
    products: [
        .executable(name: "socket.io-test", targets: ["YourTargetName"])
    ],
    dependencies: [
        .package(url: "https://github.com/swift-server/async-http-client.git", from: "1.9.0")
    ],
    targets: [
        .executableTarget(
            name: "YourTargetName",
            dependencies: [
                .product(name: "AsyncHTTPClient", package: "async-http-client"),
            ],
            path: "./Sources/"),
    ]
)
