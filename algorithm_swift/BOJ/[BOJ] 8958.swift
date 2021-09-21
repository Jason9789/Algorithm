//
//  main.swift
//  swift-algo
//
//  Created by 전판근 on 2021/09/19.
//

import Foundation

let n = Int(readLine()!)!
var list = [String]()

(0..<n).forEach { i in
    list.append(readLine()!)
}

for i in list {
    var score: Int = 0
    var cnt: Int = 0
    
    for index in i {
        if index == "X" {
            cnt = 0
            continue
        } else {
            cnt += 1
        }
        
        score += cnt
    }
    
    print(score)
    
}



