### 思路1 

从左向右遍历，num[i+1] > num[i]，则抛弃num[i+1]这个数。

利用栈或双端队列，本质上是以空间换时间的方法。

时间复杂度O(N)
空间复杂度O(N)

