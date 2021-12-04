import MPT

storage = {}

# 1. init() 构造树
mpt = MPT.MerklePatriciaTrie(storage)  

# 2. update() 添加节点
mpt.update(b'b', b'alphabet')
mpt.update(b'bird', b'animal')
mpt.update(b'boy', b'man')
mpt.update(b'boat', b'ship')
mpt.update(b'girl', b'woman')

# 3. get() 查询节点
print('boat:    ',mpt.get(b'boat'))

# 4. update() 更新节点
mpt.update(b'boat', b'Ship')

# 5. get() 查询节点
print('new boat:    ',mpt.get(b'boat'))

# 6. root() 返回根节点
root1 = mpt.root()

# 7. root_hash() 返回根节点的哈希值
root1hash = mpt.root_hash()

# 8. delete() 删除节点
mpt.delete(b'boy')

print("Root hash is     {}".format(root1hash.hex()))
print("New root hash is {}".format(mpt.root_hash().hex()))

# 9. init() 从旧mpt的根节点提取旧mpt 
mpt1 = MPT.MerklePatriciaTrie(storage, root = root1)

print('in old mpt, boy:    ', mpt1.get(b'boy'))
print('in newest mpt, boy: ', end='')
try:
    print(mpt.get(b'boy'))
except KeyError:
    pass
     #print('not exist in a new mpt.')



# # 保存当前树
# root1 = mpt.root()
# root1hash = mpt.root_hash()

# # 删除节点boy前后mpt根哈希值不同
# print("Root hash is     {}".format(root1hash.hex()))
# mpt.delete(b'boy')
# print('delete boy')
# print("New root hash is {}".format(mpt.root_hash().hex()))

# # 从旧mpt的根哈希提取旧mpt
# mpt1 = MPT.MerklePatriciaTrie(storage, root = root1)

# print('in old mpt, boy:    ',mpt1.get(b'boy'))
# print('in newest mpt, boy: ',end =' ')





