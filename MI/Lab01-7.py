
def wordcount(data):
    dic = {}
    for i in data:
        dic[i]=dic.get(i,0)+1
    return dic

if __name__ == "__main__":
    text='''
When I do count the clock that tells the time,
And see the brave day sunk in hideous night;
When I behold the violet past prime,
And sable curls all silver'd o'er with white:
When lofty trees I see barren of leaves,
Which erst from heat did canopy the herd,
And summer's green, all girded up in sheaves,
Born on the bier with white and bristly beard;
Then of thy beauty do I question make,
That thou among the wastes of time must go,
Since sweets and beauties do themselves forsake,
And die as fast as they see others grow;
And nothing 'gainst Time's scythe can make defence
Save breed, to brave him when he takes thee hence.
'''
    pure=text.strip().strip(',;:.')
    print ("The result is%s" %wordcount(pure.split()))
    
