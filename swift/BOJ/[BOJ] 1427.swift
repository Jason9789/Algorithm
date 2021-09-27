import Foundation

var n: Int = Int(readLine()!)!

var list = Array<Int>()
var result: String = ""

while n > 0 {
    let temp = n  % 10
    n /= 10
    list.append(temp)
}

list.sort(by: >)

list.forEach {
    result += String($0)
}

print(result)
