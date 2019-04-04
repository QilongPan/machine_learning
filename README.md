#算法导论
##基本数据结构
###栈和队列
栈(stack)实现的是一种后进先出(last-in,first-out,LIFO)策略。  
队列(queue)实现的是一种先进先出(first-in,first-out,FIFO)策略。  
###链表
链表其中的各对象按线性顺序排列。数组的线性顺序由数组下标决定，然而链表的是由各个对象里的指针决定的。链表中的每个元素都是一个对象，拥有关键字和对象的指针。






# 机器学习
Implement machine learning algorithm

#BI想法
##数据基本操作模块
- 采用python进行开发，比如mysql采用pymysql，hdfs采用hive等。
- 数据基本操作模块，对数据库，集群等数据源进行增删改查操作。
- 数据分析模块，能使用平台提供的算法进行分析。

#hive技术手册
Hive数据仓库软件支持使用SQL读取、写入和管理驻留在分布式存储中的大型数据集。结构可以投影到已经存储的数据上。用户可以通过命令行工具和JDBC驱动程序连接到Hive。  
hive提供的特性如下：
- 支持通过SQL轻松访问数据的工具，从而支持数据仓库任务，如提取/转换/加载(ETL)、报告和数据分析。  
- 一种将结构强加于各种数据格式的机制
- 访问直接存储在HDFS或其他数据存储系统(如HBase)中的文件。
# 反事实后悔最小化(CFR)
##介绍
在过去的10年里，人工智能取得了意想不到的进步。在图像处理和语音识别方面的巨大进步中，吸引了媒体大量关注的是人工智能在各种游戏中战胜人类。在OpenAI玩Dota2和DeepMind玩雅达利游戏的背景下，最重要的成就是AlphaGo在围棋中击败了韩国围棋大师。这是第一次机器在围棋中展现出超人的表现，仅次于1997年深蓝卡斯帕罗夫国际象棋—。这是人工智能领域的一个历史性时刻。  

大约在同一时间，一组来自美国、加拿大、捷克共和国和芬兰的研究人员已经在研究另一款游戏:无限注德州扑克。
[http://https://baike.baidu.com/item/%E5%BE%B7%E5%85%8B%E8%90%A8%E6%96%AF%E6%89%91%E5%85%8B/83440?fr=aladdin&fromid=6411849&fromtitle=%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B](http://https://baike.baidu.com/item/%E5%BE%B7%E5%85%8B%E8%90%A8%E6%96%AF%E6%89%91%E5%85%8B/83440?fr=aladdin&fromid=6411849&fromtitle=%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B "德州扑克")
  
多年来(他们关于扑克的第一篇论文可以追溯到2005年)，阿尔伯塔大学(现在与谷歌Deepmind合作)和卡内基梅隆大学(Carnegie Mellon University)的研究人员一直在耐心研究博弈论的进展，最终目标是解决扑克问题。  

2015年，Oskari Tammelin, Neil Burch, Michael Johanson 和 Michael Bowling 创造了一个名为**Cepheus**的电脑程序，首次取得巨大成功。他们在论文中发表了他们的研究成果，题目很简单:《Solving Heads-Up Limit Texas Hold’em》和《Heads-up Limit Hold’em Poker is Solved》

##Cepheus-有限注德州扑克  
尽管这些论文的题目声称解决了扑克问题——形式上它实际上已经解决了。从本质上来说，解决“提前限制”意味着研究人员能够提出一种近似于纳什均衡的策略(与人类一生中最初的策略难以区分)。在两个人的零和博弈中，使用纳什均衡的策略也是任何玩家在不了解对手策略的情况下所能做的最好的事情。  

本质上，研究Cepheus的研究人员有效地计算了所有可能的离线游戏情境的可能反应。计算并存储了tb级的向量，这些向量表示在所有游戏场景中可能的操作的概率分布。虽然这听起来不像AlphaGo的深度神经网络那么吸引人，但计算纳什均衡策略概要的算法在某种程度上类似于AlphaGo/AlphaZero中使用的算法。两种解决方案的共同之处在于，都是从与自身的对抗中学习。Cepheus的核心算法-反事实后悔最小化(Counterfactual Regret Minimization),也是本文的主题。

##DeepStack-神经网络玩无限注德州扑克
在Cepheus的之后两年，另一个成功的扑克机器人问世了——这次它可以在无限注德州扑克中战胜人类。它的名字叫DeepStack，它以神经网络辅助下的连续再求解为核心。  

再求解是子博弈求解技术之一。子博弈是基于当前决策点的博弈树。从非常高级的角度来看，子游戏求解意味着在与父节点分离的情况下求解子游戏。换句话说，重新求解是一种在给定决策点上仅为游戏剩余部分重构策略概要文件的技术。
  
Deepstack的创造者使用了连续的重新求解，在整个游戏中只维护了两个向量。结果证明，这两个向量足以在当前子博弈(决策点)中不断重构近似于纳什均衡的策略概要。

在DeepStack中，深度神经网络被用来克服由它的创建者提出的与不断重新求解有关的计算复杂性。这个复杂性问题来自于整个游戏中任意决策点的反事实值向量的重新计算。直接的方法是应用反事实后悔最小化求解器，但这实际上是不可行的。Deepstack通过限制CFR求解器的深度和广度来处理这个问题(这在某种程度上类似于AlphaGo的值和策略网络)。广度受操作抽象的限制(只包含折叠、调用、2或3个bet操作，以及全部操作)。  

为了评估DeepStack对人类的性能，来自17个国家的33名专业玩家(在国际扑克联盟的帮助下)被挑选出来，每人玩3000手牌。游戏通过在线界面进行。DeepStack指出平均每100手可以赢得492 mbb/g。Deepstack战胜了所有的玩家，只有一个人的结果在统计学上并不显著。  

##Libratus-DeepStack的主要竞争对手来自卡内基梅隆大学
2017年1月，又向超人扑克的表现迈进了一步。Libratus-由卡内基梅隆大学的 Tuomas W. Sandholm和他的同事们开发的德州扑克—，击败了由4名专业选手组成的队伍: Jason Les, Dong Kim, Daniel McCauley, 和 Jimmy Chou。这场名为“大脑vs人工智能”的比赛在匹兹堡的一家赌场举行，历时20天，共有约12万次对局。参与者被认为比DeepStack的对手更强大。奖金总额20万美元，按比例分配给4名选手。  
Libratus使用了三种主要的不同方法:
