//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2021/01/10.
//

import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let x = input[1]

print(readLine()!.split(separator: " ")
        .map{ Int(String($0))! }
        .filter{ $0 < x }
        .map{ "\($0)" }
        .joined(separator: " "))
