def displayInventory(inventory):
    print('Inventory:')
    total_item = 0
    for k,v in inventory.items():
        print(str(v)+'  '+k)
        total_item += v
    print('Totoal number of items:'+ str(total_item))

def addedInventory(inventory,addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
        else:
            inventory[addedItems[i]] = 1
    return inventory

inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin', 'gold coin', 'ruby']
inv = addedInventory(inv,dragonLoot)
displayInventory(inv)
