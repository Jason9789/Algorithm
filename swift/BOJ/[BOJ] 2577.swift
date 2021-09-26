//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

var N: Int = 1
var list = [Int](repeating: 0, count: 10)


(0..<3).forEach { _ in
    N *= Int(readLine()!)!
}

while N > 0 {
    let cnt = N % 10
    list[cnt] += 1
    N /= 10
}

list.forEach {
    print($0)
}
