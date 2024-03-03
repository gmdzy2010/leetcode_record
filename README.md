# leetcode提交记录

### 链表
| 题目编号 | 题目描述 | 解法关键点 |
| --- | --- | --- |
| [0002](https://leetcode.cn/problems/add-two-numbers/description/) | 两数相加 | 处理好`进位`和`余数`，注意最后进位的处理 |
| [0019](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | 删除倒数第 N 个节点 | `快慢指针`，快指针先走N步 |
| [0021](https://leetcode.cn/problems/merge-two-sorted-lists/) | 合并两个有序链表 | 先利用`归并`合并等长部分，剩余部分拼接上 |
| [0023](https://leetcode.cn/problems/merge-k-sorted-lists/) | 合并K个有序链表 | 使用小根堆`优先级队列`，注意定义节点大小比较方法 |
| [0024](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 两两交换链表节点 | 使用`穿针引线法`，和翻转链表的方法类似 |
| [0025](https://leetcode.cn/problems/reverse-nodes-in-k-group/) | K个一组翻转链表 | 对于每一组先`找尾节点`，再`翻转`，最后`拼接` |
| [0061](https://leetcode.cn/problems/rotate-list/) | 旋转链表 | 将链表`连接成环`，再在指定位置`断开` |
| [0082](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/) | 删除排序链表中的重复元素 | 获取`重复值`，再`内层循环`去除所有重复值 |
| [0083](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) | 删除排序链表中的重复元素 | 注意`先跳过`重复节点，`再移动`到下一个节点 |
| [0086](https://leetcode.cn/problems/partition-list/) | 分隔链表 | `三指针法`，使用额外两个链表，注意`切断环`再拼接 |
| [0092](https://leetcode.cn/problems/reverse-linked-list-ii/) | 翻转链表 | `头插法`，先找到待翻转区域头节点，再依次翻转 |
| [0142](https://leetcode.cn/problems/linked-list-cycle-ii/) | 环形链表 | 使用集合，判断走过的节点是否在集合中出现 |
| [0143](https://leetcode.cn/problems/reorder-list/) | 重排链表 | 先`遍历`得到所有节点，再使用`双指针`分别从头尾拼接各个节点 |
| [0146](https://leetcode.cn/problems/lru-cache/) | LRU缓存 | 使用`双向链表`和`哈希表`，定义`尾插`方法 |
| [0147](https://leetcode.cn/problems/insertion-sort-list/) | 对链表进行插入排序 | 先理解`插入排序`，再加上`头插法` |
| [0148](https://leetcode.cn/problems/sort-list/)| 排序链表 | 使用`快慢指针`找链表终点，再`合并`两个链表 |
| [0160](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | 链表相交 | 使用`集合`记录遍历过的节点 |
| [0203](https://leetcode.cn/problems/remove-linked-list-elements/) | 移除链表元素 | 注意被移除的节点`清除next引用`节约内存 |
| [0206](https://leetcode.cn/problems/reverse-linked-list/) | 翻转链表 | 定义`虚拟节点`prev，依次改变每个节点的next |
| [0328](https://leetcode.cn/problems/odd-even-linked-list/description/) | 奇偶链表 | `双指针`，奇偶节点`交替前进` |
| [0707](https://leetcode.cn/problems/add-two-numbers/description/) | 设计实现自定义链表 | `指定位置插入节点` |

### 哈希表
| 题目编号 | 题目描述 | 解法关键点 |
| --- | --- | --- |
| [0001](https://leetcode.cn/problems/two-sum/description/) | 两数之和 | `哈希表`记录遍历过的元素及其位置：`{num: index}` |
| [0015](https://leetcode.cn/problems/3sum/description/) | 三数之和 | 使用双层循环，内层循环使用`集合` |
| [0242](https://leetcode.cn/problems/valid-anagram/) | 有效的字母异位词 | 长度为26的`数组哈希表`记录字母出出现次数 |
| [0349](https://leetcode.cn/problems/intersection-of-two-arrays/description/) | 两个数组的交集 | 使用`集合` |
| [0454](https://leetcode.cn/problems/4sum-ii/) | 四数相加 | 使用`哈希表`记录前两个数字之和，再遍历后两个数字 |

### 字符串
| 题目编号 | 题目描述 | 解法关键点 |
| --- | --- | --- |
| [0028](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 字符串第一个匹配项 | `KMP`算法，用`前缀表`加速 |
| [0151](https://leetcode.cn/problems/reverse-words-in-a-string/) | 翻转字符串中的单词 | `倒叙双指针`，从最右侧开始遍历 |
| [0344](https://leetcode.cn/problems/reverse-string/) | 翻转字符串 | `双指针`从左右两侧向内收缩 |
| [0459](https://leetcode.cn/problems/repeated-substring-pattern/) | 重复的子字符串 | `KMP`算法 |
| [0541](https://leetcode.cn/problems/reverse-string-ii/) | 翻转字符串 | `双指针`从左右两侧向内收缩，for循环指定步长 |
