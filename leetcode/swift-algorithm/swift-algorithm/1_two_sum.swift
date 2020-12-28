//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2020/12/28.
//

import Foundation

//MARK:- 시간 복잡도 O(n^2)
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0..<nums.count {
            for j in i+1..<nums.count {
                if (nums[i] + nums[j] == target) {
                    return [i, j]
                }
            }
        }
        return []
    }
}


//MARK:- 시간 복잡도 O(n) HashTable 사용
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var nums_map: Dictionary = [Int:Int]()
        
        for i in 0..<nums.count {
            let ans1 = nums[i]
            let ans2 = target - ans1
            
            if let j = nums_map[ans2] { return [j, i] }
            nums_map[ans1] = i
        }
        
        return []
    }
}
