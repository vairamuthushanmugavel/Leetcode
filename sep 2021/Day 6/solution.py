class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key = keysPressed[0]
        maxTime = releaseTimes[0]
        
        for idx in range(len(releaseTimes)):
            duration = releaseTimes[idx] - releaseTimes[idx - 1]
            if maxTime == duration:
                key = max(key,keysPressed[idx])
                
            if duration > maxTime:
                key = keysPressed[idx]
                maxTime = max(maxTime,duration)
            
        return key