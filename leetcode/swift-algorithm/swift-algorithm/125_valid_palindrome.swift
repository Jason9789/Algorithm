//
//  main.swift
//  swift-algorithm
//
//  Created by 전판근 on 2020/12/25.
//

import Foundation

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        
        let lowerString = s.lowercased()
        let alnumString = lowerString.replacingOccurrences(of: "[^a-z0-9]", with: "", options: .regularExpression)
        let reversedString = String(alnumString.reversed())
        
        return alnumString == reversedString
        
    }
}

//Solution.isPalindrome("A man, a plan, a canal: Panama")

var solution = Solution()
let sol = solution.isPalindrome("A man, a plan, a canal: Panama")

print(sol)

