import random

def drops(event, entity):
    if event == 'death' and entity['drops'] and entity['instigator']:
        if entity['instigator']:
            inv = entity.world.from_id(entity['instigator'])['inventory']
        
        for item, amount in entity['drops'].items():
            if item in map(lambda x: x['name'], entity.world.item_types):
                if entity['instigator']:
                    if item in inv:
                        inv[item] += random.randint(amount[0], amount[1]) # amount is a tuple (min, max)
                        
                    else:
                        inv[item] = random.randint(amount[0], amount[1])
                        
                else:
                    if item in entity.world.find_place(entity.place)['items']:
                        entity.world.find_place(entity.place)['items'][item] += random.randint(amount[0], amount[1])
                        
                    else:
                        entity.world.find_place(entity.place)['items'][item] = random.randint(amount[0], amount[1])
                
            else:
                print("Warning: Item {} dropped by a {} not found in world's item definitions!".format(
                    item,
                    entity.variant['name']
                ))
                
        for item, amount in entity['inventory'].items():
            if item in map(lambda x: x['name'], entity.world.item_types):
                if 'alwaysDrop' in entity.world.find_item(item)['flags']: 
                    if entity['instigator']:    
                        if item in inv:
                            inv[item] += amount
                            
                        else:
                            inv[item] = amount
                    
                    else:
                        if item in entity.world.find_place(entity.place)['items']:
                            entity.world.find_place(entity.place)['items'][item] += amount
                            
                        else:
                            entity.world.find_place(entity.place)['items'][item] = amount
                
            else:
                print("Warning: Item {} dropped by a {} not found in world's item definitions!".format(
                    item,
                    entity.variant['name']
                ))
                
        if entity['instigator']:
            entity.world.from_id(entity['instigator'])['inventory'] = inv