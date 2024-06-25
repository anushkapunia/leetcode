class Solution(object):
    def carPooling(self, trip, capacity):
        
        picktrip = []
        droptrip = []
        for i in trip:
            picktrip.append([i[0],i[1]])
            droptrip.append([i[0],i[2]])
        picktrip = sorted(picktrip, key = lambda x: x[1])
        droptrip = sorted(droptrip, key = lambda x: x[1])
        i=0
        j=0
        l = len(trip)
        while i < l:
            if picktrip[i][1] < droptrip[j][1]:
                capacity -= picktrip[i][0]
                i+=1
            else:
                capacity += droptrip[j][0]
                j+=1
            if capacity < 0:
                return False
        return capacity>= 0