class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        _map = {}
        day = 1
        while day <= N:
            if str(cells) in _map:
                looplen =  day - _map[str(cells)]
                k =  (N-day)//looplen
                day =  day + ( k * looplen)
            prev = cells[0]
            _map[str(cells)] = day 
            for cellidx in range(1,7):
                next =  cells[cellidx + 1]
                curr =  cells[cellidx]
                cells[cellidx] = 1 - (prev ^ next)
                prev = curr
            cells[0],cells[7] = 0,0
            day = day+1
        return cells