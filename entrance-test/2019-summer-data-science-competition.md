
### 人工智能学院《从Kaggle竞赛深入数据科学》入学测试

![](images/kkb-ai.png)

#### 各位同学大家好，欢迎报名我们的课程。 因为我们的课程是面向具备一定基础的提高课程，所以为了保证课程的质量，请参加《Kaggle数据科学竞赛强化》课程的同学完成以下入学测试。 


###### 以下包含10个问题。若10个问题中有超过5个问题回答正确，则具备参加此课程的能力。问题答案附在测试的末尾，请各位同学进行**自我**打分、评估。

#### Question1: 目前常用的贝叶斯分类方法，我们往往称为朴素贝叶斯分类（Naive Bayes Classification）。 该分类器之所以叫“朴素”贝叶斯的原因是：

`---by [慧科集团开课吧人工智能学院](www.huike.com)`



![image.png](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563440941&di=2ebd7b5a1c2b6b657a96e44df13f84db&imgtype=jpg&er=1&src=http%3A%2F%2Fi2.wp.com%2Fwww.scienceprog.com%2Fwp-content%2Fuploads%2F2016%2F07%2FThomas_Bayes.png%3Fresize%3D468%2C308)

```
[ ] A. 常用的贝叶斯分类使用的数据量较小，相对比较简单，所以称为“朴素”分类器；

[ ] B. 此贝叶斯分类方法只能解决类别较少的分类问题，所以称为“朴素”分类器；

[ ] C. 此贝叶斯分类器对条件概率，例如 Pr(A|CB)进行了简化，简化成了Pr(A|B)，所以称为“朴素”分类器；

[ ] D. 此贝叶斯分类方法只能进行分类问题，不能进行回归(Regression)，所以称为“朴素”分类器.
```

#### Question2: 如果我们把机器学习的模型看成是定义一个函数f(x; \theta)，该函数接受一个输入向量 `x`，该输入是我们对现有数据进行的数据表征（Representation）. 然后基于我们的函数，获得期望的输出。而机器学习的过程可以看做是对`f(x)`的相关参数 `\theta`进行优化的过程。那么，如果我们现在要进行预测或者分类的程序包含城市名称信息，例如“北京”，“武汉”，那么，如何把“北京”，“武汉”等城市信息进行表征成所需的向量`x`?



![](https://ss1.baidu.com/-4o3dSag_xI4khGko9WTAnF6hhy/image/w%3D500/sign=cfe520699c45d688a302b2a494c27dab/faedab64034f78f0fb2e73a977310a55b3191c46.jpg)
```
[ ] A. 使用中国的邮政编码作为每个城市的向量代码，输入f(x)时，北京就是 [10000,], 武汉就是[43000,];

[ ] B. 按照音标对城市进行排序，输入f(x)时，北京就是 [1, ], 武汉可能是 [20, ];

[ ] C. 将城市表征成one-hot形式，如果一个有5个城市，则北京是 [0,0,0,0, 1], 武汉是 [1, 0, 0, 0, 0];

[ ] D. 将城市的信息与人口统计学、位置等信息进行表征，例如北京和武汉的向量分别是： [城市人口的平均年龄，经度，维度];
```

#### Question3: 关于过拟合(overfitting)和欠拟合(underfitting)的表述中，错误的是？



![](https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3114984120,189427060&fm=11&gp=0.jpg)

```
[ ] A. 过拟合和欠拟合是机器学习中非常常见的现象；

[ ] B. 造成过拟合的原因往往是机器学习模型中需要拟合的参数过少造成的；

[ ] C. 造成欠拟合的原因往往是机器学习模型的模型过于简单或者函数定义错误造成的；

[ ] D. 增加训练数据并不能有效解决欠拟合（under fitting）问题;
```

#### Question4: 深度学习中，关于softmax函数的描述，错误的是？

![](https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2466996520,3559654331&fm=26&gp=0.jpg)


```
[ ] A. 把经过神经网络求得的值变成概率分布。这个概率分布可以用作概率的真实估计;

[ ] B. logstic函数是softmax的一维特殊形式；

[ ] C. 当softmax的输入值较大时，例如[19999, 23333, 433399]，往往会出现数据溢出错误;

[ ] D. softmax函数是一种常用的Loss函数，可以用来衡量模型的优良;
```

#### Question5: 关于卷积神经网络(Convolutional Neural Networks)描述错误的是？

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562846550351&di=f1e9db7d3d7d09ab9effc08ed0c1f936&imgtype=0&src=http%3A%2F%2Fimg.mp.sohu.com%2Fupload%2F20170509%2Ffa55cb0309fe4972af9982eb733832fe_th.png)

```
[ ] A. 卷积神经网络中，Pooling层的作用是减少数据维度，降低需要训练的参数，从而减少过拟合;

[ ] B. 卷积神经网络中，Batch Normalization的作用是减弱层数过多造成的信息传播困难；

[ ] C. Dropout可以提高模型的泛化能力；

[ ] D. 卷积神经网络中，权值参数的初始化并不会很大程序上影响模型的拟合能力
```

#### Question6:关于词向量(word Vector)的描述，正确的是？

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562846589069&di=5e6fafde2a15a894208bb3ecc1c12a86&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170803%2Fec65ba9b93bc4a9aa373aaddbd1a6408_th.jpg)


``` 
[ ] A. 词向量的目标是把意思相近的单词变成向量空间距离接近的向量集合； 

[ ] B. 训练词向量需要对单词的相似度进行打标，进行监督学习；

[ ] C. 训练词向量时，包含的单词种类越多，训练的单词聚类效果越好；

[ ] D. 随着人工智能技术的快速发展，目前词向量能够比较好的解决一词多义问题；
```

#### Qustion7: 关于深度学习与GPU之间关系的描述，错误的是？

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562846634904&di=7932716e20edc90853cf3777f869af98&imgtype=0&src=http%3A%2F%2Fimgsa.baidu.com%2Fexp%2Fw%3D500%2Fsign%3D8db2f4de7af0f736d8fe4c013a54b382%2Fb999a9014c086e063b43fdea00087bf40bd1cbac.jpg)

```
[ ] A. 深度学习中大量使用到了矩阵（matrix）的计算；

[ ] B. 矩阵运算可以使用GPU进行并行加速处理；

[ ] C. 使用GPU可以提供模型最终的准确率；

[ ] D. GPU原本是进行图像处理的，但是深度学习和图像处理所相关的主要操作是类似的；
```

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562846728004&di=947f293e3ffdedb04337aa6b2b43236a&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170721%2F29983980671345e793695516f889240b_th.jpg)

#### Qustion8: 如果要对Python的某个dictionary, D, 按照值的大小进行排序，以下方法中，错误的是：




```
[ ] A. 
    import operator as op
    
    D = {1: 0, 2: 3}
    sorted(D.items(), key=lambda x: op.getitem(x, 0))
```

```
[] B. 
    D = {1: 0, 2: 3}
    sorted(D.items(), key=lambda x: x[0])
```

```
[ ] C. 
    D = {1: 0, 2: 3}
    sorted(D, key=lambda x: x.value)
```

```
[ ] D.
    D = {1: 0, 2: 3}
    [(x, D[x]) for x in sorted(D, key=lambda x: D[x])]
```

#### Qustion9: 以下 Python 代码不能正确运行的是? 

```
[ ] A. 
    D = {1: 0, 2: 3}
    
    P1 = (1, 2)
    D[P1] = 'red'
   
```

```
[ ] B. 
    D = {1: 0, 2: 3}
  
    P1 = [1, 2]
    D[P1] = 'green'
```

```
[ ] C. 
    test_func = lambda x: x[1]
    
    def some_func(a, b):
        return b(a)
    
    P1 = (1, 2)
    some_func(P1, test_func)
```

```
[ ] D. 
    def fib(n):
        return fib(n-1) + fib(n-2) if n > 1 else n
        
    print(fib(10))
```

#### Qustion10: 以下哪个变量是可以作为Python集合的元素的？

```
[ ] A:  some_fronzen = frozenset({1, 2, 3})

[ ] B:  some_list = [1, 2, 3]

[ ] C:  some_set = {1, 2, 3}

[ ] D:  some_dict = {1: 2}
```

### 参考答案: 
1. C
2. C或者D
3. B
4. D
5. D
6. A
7. C
8. C
9. B
10. A

#### 因为我们的课程是针对有一定基础的同学，如果你能回答对5个或者以上，则具备参加课程的能力。所以，你做对了吗？ 如果做对了，请联系我们的教务开始进行正式付费，谢谢。

