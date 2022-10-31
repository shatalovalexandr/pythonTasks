import numpy as np


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity

    def theLift(self):
        answer = [0]
        up, down = True, False
        lift = []
        # while True:
        for i in range(len(self.queues)):
            for p in lift:
                if p == i:
                    lift.pop(lift.index(p))
                    if i not in answer:
                        answer.append(i)
            if len(lift) < self.capacity and len(self.queues[i]) > 0:
                for j in range(len(self.queues[i])):
                    if self.queues[i][j] > i:
                        lift.append(self.queues[i][j])
                        if answer[-1] != i:
                            answer.append(i)
                        break
            # print('Floor: ', i)
            # print('Answer: ', answer)
        for i in range(len(self.queues) - 1, -1, -1):
            for p in lift:
                if p == i:
                    lift.pop(lift.index(p))
                    if i not in answer:
                        answer.append(i)
            if len(lift) < self.capacity and len(self.queues[i]) > 0:
                for j in range(len(self.queues[i])):
                    if self.queues[i][j] < i:
                        lift.append(self.queues[i][j])
                        if answer[-1] != i:
                            answer.append(i)
                        break
            # if down:
            #     break
            #
            # up, down = False, True

        if answer[-1] != 0:
            answer.append(0)
        return answer


# Floors:    G     1      2        3     4      5      6         Answers:
# tests = [[((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]]]
tests = [[((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
         [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
         [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
         [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]]]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    # print(np.array_equal(lift.theLift(), answer))
    print(lift.theLift())
