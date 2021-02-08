class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        while i <= n:
        	if i == 1:
        		a = "1"
        	else:
        		a = self.helper("a")
        	i+=1
        return s


    def helper(s):
    	res = []
		count = 0    	
    	for i in range(len(s)):
    		if i > 0 and s[i] == s[i-1]:
    			count += 1
    			a = str(count) + s[i]
    			res[-1] = a

    		else:
    			count = 1
    			a = str(count) + s[i]
    			res.append(a)
    	return "".join(res)
