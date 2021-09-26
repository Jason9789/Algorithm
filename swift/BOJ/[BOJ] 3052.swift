//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

var list = Array<Int>()
var removeList = Set<Int>()

for _ in 0...9 {
    
    let n = Int(readLine()!)!
    let result = n % 42
    
    list.append(result)
}

removeList = Set(list)

print(removeList.count)
