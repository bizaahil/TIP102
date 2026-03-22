def num_VIP_guests(vip_passes, guests):
    
    vip_set = []
    count = 0

    for i in range(len(vip_passes)):
        vip_set.append(vip_passes[i])

    for guest in guests:
        if guest in vip_set:
            count += 1

    return count



vip_passes1 = "aAb"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))