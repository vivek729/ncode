class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sq = deque(students)
        cont_rejected = 0
        qlen = len(sq)
        # cur_sandwich_index = 0

        # while sq and cur_sandwich_index < len(sandwiches):
        while sq and sandwiches:
            # if sq[0] == sandwiches[cur_sandwich_index]:
            if sq[0] == sandwiches[0]:
                sq.popleft()
                # cur_sandwich_index += 1
                sandwiches.pop(0)
                cont_rejected = 0
            else:
                sq.append(sq.popleft())
                cont_rejected += 1
                if cont_rejected == len(sq):
                    return cont_rejected
        
        return 0
