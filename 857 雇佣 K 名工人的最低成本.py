class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        worker=[]
        for q, w in zip(quality, wage):
            worker.append([w*1.0/q, q, w])
        worker.sort()
        print("worker is :", worker)
        heap=[]
        qSum=0
        res=float('inf')
        for r, q, w in worker:
            heapq.heappush(heap, -q)
            qSum+=q 
            if len(heap)>K:
                item = heapq.heappop(heap)
                print(item)
                qSum= item+qSum
            if len(heap)==K:
                res=min(res, r*qSum)
        return res