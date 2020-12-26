//
//  main.swift
//  swift-Data-Structures
//
//  Created by 전판근 on 2020/12/26.
//

import Foundation

//MARK:- Node

public class Node<Value> {
    public var value: Value
    public var next: Node?
    
    public init(value: Value, next: Node? = nil) {
        self.value = value
        self.next = next
    }
}

extension Node: CustomStringConvertible {
    
    public var description: String {
        guard let next = next else {
            return "\(value)"
        }
        return "\(value) -> " + String(describing: next) + " "
    }
}

// MARK:- LinkedList 연결리스트

public struct LinkedList<Value> {
    
    public var head: Node<Value>?
    public var tail: Node<Value>?
    
    public init() {}
    
    private mutating func copyNodes() {
        guard var oldNode = head else {
            return
        }
        
        head = Node(value: oldNode.value)
        var newNode = head
        
        while let nextOldNode = oldNode.next {
            newNode!.next = Node(value: nextOldNode.value)
            newNode = newNode!.next
            
            oldNode = nextOldNode
        }
        tail = newNode
    }
    
    public var isEmpty: Bool {
        return head == nil
    }
    
    // push
    public mutating func push(_ value: Value) {
        head = Node(value: value, next: head)
        if tail == nil {
            tail = head
        }
    }
    
    // append
    public mutating func append(_ value: Value) {
        // 1
        guard !isEmpty else {
            push(value)
            return
        }
        
        // 2
        tail!.next = Node(value: value)
        
        // 3
        tail = tail!.next
    }
    
    // insert
    public func node(at index: Int) -> Node<Value>? {
        // 1
        var currentNode = head
        var currentIndex = 0
        
        // 2
        while currentNode != nil && currentIndex < index {
            currentNode = currentNode!.next
            currentIndex += 1
        }
        
        return currentNode
    }
    
    // 1
    @discardableResult
    public mutating func insert(_ value: Value, after node: Node<Value>) -> Node<Value> {
        // 2
        guard tail !== node else {
            append(value)
            return tail!
        }
        // 3
        node.next = Node(value: value, next: node.next)
        return node.next!
    }
    
    // Removing values from the list
    @discardableResult
    public mutating func pop() -> Value? {
        defer {
            head = head?.next
            if isEmpty {
                tail = nil
            }
        }
        return head?.value
    }
    
    // removeLast
    @discardableResult
    public mutating func removeLast() -> Value? {
        // 1
        guard let head = head else {
            return nil
        }
        // 2
        guard head.next != nil else {
            return pop()
        }
        // 3
        var prev = head
        var current = head
        
        while let next = current.next {
            prev = current
            current = next
        }
        // 4
        prev.next = nil
        tail = prev
        return current.value
    }
    
    @discardableResult
    public mutating func remove(after node: Node<Value>) -> Value? {
        defer {
            if node.next === tail {
                tail = node
            }
            node.next = node.next?.next
        }
        return node.next?.value
    }
    
    
}

extension LinkedList: Collection {
    public var startIndex: Index {
        return Index(node: head)
    }
    
    public var endIndex: Index {
        return Index(node: tail?.next)
    }
    
    public func index(after i: Index) -> Index {
        return Index(node: i.node?.next)
    }
    
    public subscript(position: Index) -> Value {
        return position.node!.value
    }
    
    
    public struct Index: Comparable {
        
        public var node: Node<Value>?
        
        static public func == (lhs: Index, rhs: Index) -> Bool {
            switch (lhs.node, rhs.node) {
            case let (left?, right?):
                return left.next === right.next
                
            case (nil, nil):
                return true
            default:
                return false
            }
        }
        
        static public func <(lhs: Index, rhs: Index) -> Bool {
            guard lhs != rhs else {
                return false
            }
            let nodes = sequence(first: lhs.node) { $0?.next }
            return nodes.contains { $0 === rhs.node }
        }
    }
}

extension LinkedList: CustomStringConvertible {
    public var description: String {
        guard let head = head else {
            return "Empty list"
        }
        return String(describing: head)
    }
}


//MARK:- Result

print("-- example of push --")
var list = LinkedList<Int>()
list.push(3)
list.push(2)
list.push(1)

print(list)

print("-- example of append --")
var list2 = LinkedList<Int>()
list2.append(1)
list2.append(2)
list2.append(3)

print(list2)


print("-- example of inserting at a particular index --")
var list3 = LinkedList<Int>()
list3.push(3)
list3.push(2)
list3.push(1)

print("Before inserting: \(list3)")
var middleNode = list3.node(at: 1)!

for _ in 1...4 {
    middleNode = list.insert(-1, after: middleNode)
}

print("After inserting: \(list3)")


print("-- example of pop --")
var list4 = LinkedList<Int>()
list4.push(3)
list4.push(2)
list4.push(1)

print("Before popping list : \(list4)")
let poppedValue = list4.pop()
print("After popping list : \(list4)")
print("Popped valued : " + String(describing: poppedValue))


print("-- example of removing the last node")
var list5 = LinkedList<Int>()
list5.push(3)
list5.push(2)
list5.push(1)

print("Before removing last node : \(list5)")
let removedValue = list5.removeLast()

print("After removing last node : \(list5)")
print("Removed value : " + String(describing: removedValue))


print("-- example of removing a node after a particular node")
var list6 = LinkedList<Int>()
list6.push(3)
list6.push(2)
list6.push(1)

print("Before removing at particular index : \(list6)")
let index = 1
let node = list6.node(at: index - 1)!
let removedValue2 = list6.remove(after: node)

print("After removing at index \(index) : \(list6)")
print("Removed value : " + String(describing: removedValue2))


print("-- example of using collection --")
var list7 = LinkedList<Int>()
for i in 0...9 {
    list7.append(i)
}

print("List7 : \(list7)")
print("First element : \(list7[list7.startIndex])")
print("Array containing first 3 elements : \(Array(list7.prefix(3)))")
print("Array containing last 3 elements : \(Array(list7.suffix(3)))")

let sum = list7.reduce(0, +)
print("Sum of all values: \(sum)")

// Copy on Write
print("-- example of array cow --")
let array1 = [1, 2]
var array2 = array1

print("array1 : \(array1)")
print("array2 : \(array2)")

print("--- After adding 3 to array 2 ---")
array2.append(3)
print("array1 : \(array1)")
print("array2 : \(array2)")


print("-- example of linked list cow --")
var list8 = LinkedList<Int>()
list8.append(1)
list8.append(2)
var list9 = list8

print("List8 : \(list8)")
print("List9 : \(list9)")

print("After appending 3 to list9")
list9.append(3)
print("List8 : \(list8)")
print("List9 : \(list9)")

