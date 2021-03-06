//
//  main.swift
//  swift-Data-Structures
//
//  Created by 전판근 on 2020/12/27.
//

import Foundation

public struct Stack<Element> {
    private var storage: [Element] = []
    
    public init() {}
    
    public init(_ elements: [Element]) {
        storage = elements
    }
    
    public mutating func push(_ element: Element) {
        storage.append(element)
    }
    
    @discardableResult
    public mutating func pop() -> Element? {
        return storage.popLast()
    }
    
    public func peek() -> Element? {
        return storage.last
    }
    
    public var isEmpty: Bool {
        return peek() == nil
    }
}

extension Stack: ExpressibleByArrayLiteral {
    public init(arrayLiteral elements: Element...) {
        storage = elements
    }
}

extension Stack: CustomStringConvertible {
    
    public var description: String {
        let topDivider = "----top----\n"
        let bottomDivider = "\n-----------"
        
        let stackElements = storage
            .map { "\($0)" }
            .reversed()
            .joined(separator: "\n")
        
        return topDivider + stackElements + bottomDivider
    }
}

print("---Example of using a stack---")
var stack = Stack<Int>()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack)

if let poppedElement = stack.pop() {
    assert(4 == poppedElement)
    print("Popped : \(poppedElement)")
}


print("Example of initializing a stack from an array")
let array = ["A", "B", "C", "D"]
var stack2 = Stack(array)
print(stack2)
stack2.pop()
print(stack2)

print("Example of initializing a stack from an array literal")
var stack3: Stack = [1.0, 2.0, 3.0, 4.0]
print(stack3)
stack3.pop()
print(stack3)
