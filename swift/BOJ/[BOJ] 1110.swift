//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation


//let n = Int(readLine()!)!
//
//var cnt: Int = 0
//var result: Int = n
//
//repeat {
//
//    let num = (String(result).map{ Int(String($0))! })
//    let sum = String(result).reduce(0, { $0+Int(String($1))! })
//
//
//    result = num[1] * 10 + sum % 10
//    cnt += 1
//
//} while  (n != result)
//
//print(cnt)


let N = Int(readLine()!)!

var cycle = 0
var newN = N

repeat {
    let l = newN / 10
    let r = newN % 10
    let sum = l + r
    
    newN = r * 10 + sum % 10
    cycle += 1
} while (N != newN)

print(cycle)
