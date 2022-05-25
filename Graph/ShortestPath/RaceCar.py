from collections import deque

class Solution: 
    def racecar(self, target: int) -> int:
        deq = deque()
        visited = set()
        deq.append((0, 1, 0)) # pos, speed, moves

        while deq:
            
            pos, speed, moves = deq.popleft()
            # print(pos, speed, moves)

            if pos == target:
                return moves

            # go ahead
            new_pos = pos + speed
            new_speed = speed * 2
            # print("new1:", new_pos, new_speed)
            if (new_pos, new_speed) not in visited and abs(new_pos - target) < target:
                visited.add((new_pos, new_speed))
                deq.append((new_pos, new_speed, moves + 1))

            # reverse
            new_pos = 0
            if pos < target:
                new_pos = target + (target - pos)
            if pos > target:
                new_pos = target - (pos - target)
            new_speed = 1
            # print("new2:", new_pos, new_speed)
            if (new_pos, new_speed) not in visited and abs(new_pos - target) < target:
                visited.add((new_pos, new_speed))
                deq.append((new_pos, new_speed, moves + 1))
         
        
        