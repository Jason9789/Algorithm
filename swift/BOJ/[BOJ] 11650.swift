import Foundation

var n: Int = Int(readLine()!)!

var points = [[Int]]()

for _ in 0..<n {
    points.append( readLine()!.split(separator: " ").map { Int(String($0))! } )
}


points.sorted { lhs, rhs -> Bool in

    return lhs[0] < rhs[0] || (lhs[0] == rhs[0] && lhs[1] < rhs[1])
    
}.forEach { point in
    print("\(point[0]) \(point[1])")
    
}
