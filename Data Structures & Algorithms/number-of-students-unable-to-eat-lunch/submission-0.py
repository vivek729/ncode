class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sq = deque(students)
        cont_rejected = 0
        qlen = len(sq)
        while sq and sandwiches:
            if sq[0] == sandwiches[0]:
                sq.popleft()
                sandwiches.pop(0)
                cont_rejected = 0
            else:
                sq.append(sq.popleft())
                cont_rejected += 1
                if cont_rejected == len(sq):
                    return cont_rejected
        
        return 0
