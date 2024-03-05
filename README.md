# leetcode提交记录
| 题目编号 | 题目描述 | 解法关键点 |
| --- | --- | --- |
| **链表** |
| [0002](https://leetcode.cn/problems/add-two-numbers/) | 两数相加 | 处理好`进位`和`余数`，注意最后进位的处理 |
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
| [0328](https://leetcode.cn/problems/odd-even-linked-list/) | 奇偶链表 | `双指针`，奇偶节点`交替前进` |
| [0707](https://leetcode.cn/problems/add-two-numbers/) | 设计实现自定义链表 | `指定位置插入节点` |
| **哈希表** |
| [0001](https://leetcode.cn/problems/two-sum/description/) | 两数之和 | `哈希表`记录遍历过的元素及其位置：`{num: index}` |
| [0015](https://leetcode.cn/problems/3sum/description/) | 三数之和 | 使用双层循环，内层循环使用`集合` |
| [0242](https://leetcode.cn/problems/valid-anagram/) | 有效的字母异位词 | 长度为26的`数组哈希表`记录字母出出现次数 |
| [0349](https://leetcode.cn/problems/intersection-of-two-arrays/description/) | 两个数组的交集 | 使用`集合` |
| [0454](https://leetcode.cn/problems/4sum-ii/) | 四数相加 | 使用`哈希表`记录前两个数字之和，再遍历后两个数字 |
| **字符串** |
| [0028](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 字符串第一个匹配项 | `KMP`算法，用`前缀表`加速 |
| [0151](https://leetcode.cn/problems/reverse-words-in-a-string/) | 翻转字符串中的单词 | `倒叙双指针`，从最右侧开始遍历 |
| [0344](https://leetcode.cn/problems/reverse-string/) | 翻转字符串 | `双指针`从左右两侧向内收缩 |
| [0459](https://leetcode.cn/problems/repeated-substring-pattern/) | 重复的子字符串 | `KMP`算法 |
| [0541](https://leetcode.cn/problems/reverse-string-ii/) | 翻转字符串 | `双指针`从左右两侧向内收缩，for循环指定步长 |
| **栈与队列** |
| [0020](https://leetcode.cn/problems/valid-parentheses/) | 有效的括号 | `栈`，遇到左括号就将右括号入栈，判断`栈顶` |
| [0042](https://leetcode.cn/problems/trapping-rain-water/) | 接雨水 | `单调栈`存`index`，维护一个`单调下降区域`，上升就出栈 |
| [0150](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) | 逆波兰表达式 | `栈`中是有效的RPN序列，出栈两个数，计算后再放回栈 |
| [0225](https://leetcode.cn/problems/implement-stack-using-queues/) | 用队列实现栈 | 通过`循环pop`将FIFO转变为LIFO |
| [0232](https://leetcode.cn/problems/implement-queue-using-stacks/) | 用栈实现队列 | `双栈法`，一个栈负责入队列，一个栈负责逆序元素 |
| [0347](https://leetcode.cn/problems/top-k-frequent-elements/) | 前K个高频元素 | `哈希表`和`优先级队列`，先统计每个元素出现的次数，再入堆出堆 |
| **二叉树** |
| [0094](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 中序遍历 | `中左右`，root不为空再入栈并走左节点，否则出栈处理并走右节点 |
| [0098](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 验证二叉搜索树 |  |
| [0101](https://leetcode.cn/problems/symmetric-tree/) | 对称二叉树 | `队列`，每层节点内/外侧子节点`成对`入队 |
| [0102](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 层序遍历 | `队列`，root入队，对`每层`的节点依次出队再左/右节点入队 |
| [0104](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 二叉树的最大深度 | `队列`，类似`层序遍历`，每一层累加1，最终完成遍历即可 |
| [0105](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 从前中序还原二叉树 | 哈希表映射中序`val:index`，根据中序切割左右子树 |
| [0106](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | 从中后序还原二叉树 | 哈希表映射中序`val:index`，根据中序切割左右子树 |
| [0108](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 有序数组转为二叉搜索树 |  |
| [0110](https://leetcode.cn/problems/balanced-binary-tree/) | 判断二叉树是否平衡 |  |
| [0111](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) | 二叉树的最小深度 | `队列`，类似`层序遍历`，当左右节点都为空返回此时深度 |
| [0112](https://leetcode.cn/problems/path-sum/) | 路径总和 | 类似`前后序遍历`，栈中存放`(node, curr_sum)` |
| [0113](https://leetcode.cn/problems/path-sum-ii/) | 路径总和 | 类似`前后序遍历`，栈中存放`(node, visited)`，初始visited为空 |
| [0144](https://leetcode.cn/problems/binary-tree-preorder-traversal/) | 前序遍历 | `中左右`，根节点入栈，出栈处理，再右/左节点入栈 |
| [0145](https://leetcode.cn/problems/binary-tree-postorder-traversal/) | 后序遍历 | `左右中`，根节点入栈，出栈处理，再左/右节点入栈，最后逆序 |
| [0226](https://leetcode.cn/problems/invert-binary-tree/) | 翻转二叉树 | `栈`，类似`前后序遍历`，拿到根节点的左右节点，`交换左右`即可 |
| [0236](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 二叉树的最近公共祖先 |  |
| [0257](https://leetcode.cn/problems/binary-tree-paths/) | 二叉树的所有路径 |  |
| [0450](https://leetcode.cn/problems/delete-node-in-a-bst/) | 二叉搜索树的删除 |  |
| [0501](https://leetcode.cn/problems/find-mode-in-binary-search-tree/) | 二叉搜索树的众数 |  |
| [0530](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/) | 二叉搜索树的最小绝对差 |  |
| [0617](https://leetcode.cn/problems/merge-two-binary-trees/) | 合并二叉树 | `队列`，每次出队列两节点，分别判断两节点的左右节点 |
| [0669](https://leetcode.cn/problems/trim-a-binary-search-tree/) | 修剪二叉搜索树 |  |
| [0700](https://leetcode.cn/problems/search-in-a-binary-search-tree/) | 二叉搜索树的搜索 |  |
| [0701](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) | 二叉搜索树的插入 |  |
