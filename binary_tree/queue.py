class Queue():
    
    def __init__(self):
        self.queue = []
        
    def enq(self, value):
        self.queue.append(value)
        
    def deq(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        if len(self.queue) > 0:
            output = '\n'
            output += '\n'.join([str(item) for item in self.queue])
            return output
        else:
            return 'Queue is empty'


if __name__ == '__main__':
    q = Queue()
    q.enq(10)
    q.enq(20)
    q.enq(30)
    q.enq(40)
    q.enq(50)
    q.enq(60)
    q.enq(70)
    q.enq(80)
    print(q)
    print('\n')
    print('dequeueing ' + str(q.deq()))
    print('dequeueing ' + str(q.deq()))
    print('\n' + "printing Queue")
    print(q)