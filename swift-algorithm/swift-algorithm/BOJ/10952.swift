//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2021/01/10.
//

import Foundation


var input = Array<Int>()
var sum = Array<Int>()

while true {
    
    input = readLine()!.split(separator: " ").map{ Int($0)! }
    
    if input[0] == 0 && input[1] == 0 {
        break;
    } else {
        sum.append(input[0] + input[1])
    }
    
    input.removeAll()
}

for i in 0..<sum.count {
    print(sum[i])
}
