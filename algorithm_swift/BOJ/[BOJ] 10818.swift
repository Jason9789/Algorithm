//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation


let n = Int(readLine()!)!

var list: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }

print(list.min()!, list.max()!)

