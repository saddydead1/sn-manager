

import PackageDescription

let package = Package(
    name: "MyCLI",
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .executableTarget(
            name: "MyCLI"),
    ]
)
