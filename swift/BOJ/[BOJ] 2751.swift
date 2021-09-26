//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

let n: Int = Int(readLine()!)!
var list = Array<Int>()

for _ in 0..<n {
    list.append(Int(readLine()!)!)
}

list.sort()

list.forEach {
    print($0)
}
