//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

let c: Int = Int(readLine()!)!

for _ in 0..<c {
    var array = readLine()!.split(separator: " ").map { Double(String($0))! }
    
    let caseCnt: Double = array.removeFirst()
    var cnt: Double = 0
    
    let sum: Double = Double(array.reduce(0, { $0 + Int($1)} ))
    let average: Double = sum / Double(caseCnt)
    
    array.forEach {
        if $0 > average {
            cnt += 1
        }
    }
        
    let result = cnt / caseCnt * 100
    let str = String(format: "%.3f", result)
    
    print("\(str)%")
    
}
