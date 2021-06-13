// Build queue by javascript array

class Queue {
    constructor(size) {
        this.list = Array(size);
        this.head = 0;
        this.tail = 0;
    }

    push(val) {
        this.list[this.tail++] = val;
    }

    empty() {
        return this.head === this.tail;
    }

    // pop the first element out
    pop() {
        if (this.empty()) {
            return null
        } else {
            return this.list[this.head++];
        }
    }

    // peak the first element
    peak() {
        if (this.empty()) {
            return
        } else {
            console.log(this.list[this.head])
        }
    }

    print() {
        for(let i = this.head; i < this.tail; i++) {
            console.log(this.list[i]);
        }
    }
}

let queue = new Queue(10) // put a size which is big enough
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.print() // 1,2,3,4
queue.peak() // 1
console.log(queue.pop()) // 1
console.log(queue.pop()) // 2
queue.print() // 3, 4
queue.peak() // 3
queue.push(5)
queue.print() // 3, 4, 5
queue.pop()
queue.pop()
queue.pop()
queue.pop() // do nothing
queue.print() // empty