//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2021/01/09.
//

import Foundation

var array = Array<Int>()

var n = Int(readLine()!)!

for _ in 1...n {
    var nums = readLine()!.split(separator: " ").map { Int($0)! }
    
    let sum: Int = nums[0] + nums[1]
    
    array.append(sum)
    nums.removeAll()
}

for i in 0...n-1 {
    print("Case #\(i+1): \(array[i])")
}

