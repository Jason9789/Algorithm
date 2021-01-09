//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2021/01/10.
//

import Foundation

while let input = readLine() {
    print(input.split(separator: " ").map{ Int($0)! }.reduce(0, +))
}
