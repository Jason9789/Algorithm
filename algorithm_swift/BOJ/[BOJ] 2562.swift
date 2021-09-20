//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation


var list = [Int]()

for _ in 0...8 {
    let n = Int(readLine()!)!
    list.append(n)
}

let maxList: Int = list.max()!

print(maxList)
print(list.firstIndex(of: maxList)!+1)
