class MinStack:

    def __init__(self):
        self.list=[]

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        minum=float("inf")
        for i in self.list:
            if i<minum:
                minum=i
        return minum

        

