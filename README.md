# Blender-align-node
节点多种方便对齐分布方式
## 安装方式
![image](https://github.com/yunkezengren/Blender-align-node/assets/98995559/5a2d8163-e825-4b93-8860-a02652a390da)
### 下载压缩包解压放进 C:\Users\用户名\AppData\Roaming\Blender Foundation\Blender\3.6(相应版本号)\scripts\addons 
### 然后再在偏好设置开启插件
![image](https://github.com/yunkezengren/Blender-align-node/assets/98995559/4b5b6687-229a-494d-92f5-edb3ac06a810)
#### 注意 不能直接安装压缩包原因:使用了一些中文名图标,直接安装压缩包会乱码
根据https://github.com/3DSinghVFX/align_nodes 代码框架修改添加(十分感谢)

1.选中节点可以直接对齐(不需要特意选一个活动节点)

2.增加了一些对齐方式

3.对齐可以保持节点的顺序

两个饼菜单快捷键分别为Shift Q | Ctrl Q，具体可以在偏好设置-键位映射-按键绑定-搜索 Shift Q 然后修改

![对齐饼菜单](https://github.com/yunkezengren/Blender-align-node/assets/98995559/61279459-67f0-4141-a7da-447cdbd05a35)
![分布饼菜单](https://github.com/yunkezengren/Blender-align-node/assets/98995559/fed572e1-5956-432b-b789-22120c8b3a63)

#### 两种网格分布
![两种网格分布](https://github.com/yunkezengren/Blender-align-node/assets/98995559/868a4db2-27b0-4705-8028-ca6136025cd6)


巨大不足:涉及到节点frame框架，不好对齐，只能先去掉frame，排列好再加上

对别的一些情况效果不佳(比如挨得特别紧的,节点框架frame用的多的)

主要是在新建节点树时让节点树始终整洁，而不是把一个杂乱节点树瞬间对好(这种可以尝试内置的对齐插件或选中部分比较有规律的杂乱节点分批对齐)
