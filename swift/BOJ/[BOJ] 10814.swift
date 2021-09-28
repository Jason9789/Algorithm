import Foundation

var n: Int = Int(readLine()!)!
var list = [(Int, String, Int)]()

for i in 0..<n {
    
    let temp = readLine()!.split(separator: " ").map { String($0) }
    
    list.append( (Int(temp[0])!, temp[1], i) )
}


list.sorted { lhs, rhs in
    
    if lhs.0 == rhs.0 {
        return lhs.2 < rhs.2
    }
    
    return lhs.0 < rhs.0
}.forEach { l in
    print("\(l.0) \(l.1)")
}

