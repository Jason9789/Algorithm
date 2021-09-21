//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

let n = Int(readLine()!)!
var list: [Double] = readLine()!.split(separator: " ").map { Double(String($0))! }
var average: Double = 0

let maxList: Double = list.max()!

for i in 0..<n {
    let temp: Double = Double(list[i] / maxList * 100)
    
    list[i] = temp
    average += temp
}

print(average/Double(n))


