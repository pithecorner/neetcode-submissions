class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = []
        hash_map = {}
        for i,s in enumerate(strs):
            if "".join(sorted(s)) in hash_map:
                hash_map["".join(sorted(s))].append(i)
            else:
                hash_map["".join(sorted(s))] = [i]

        for e, i in enumerate(hash_map):
            for j in hash_map[i]:
                if e < len(list):
                    list[e].append(strs[j])
                    print(j)
                else:
                    while len(list) < e:
                        list.append(None)
                    list.append([strs[j]])
  
        return list
"""
    Return is a nested list.
    Take in strs as argument.
    Ouput keeps original order of letters in value.
    Constraints have no obvious catch

    sort is done in place.
    sorted() creates a new variables

"""
