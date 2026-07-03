class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1

        # build a map of who trusts who
        trust_map = {}
        for a, b in trust:
            if a in trust_map:
                trust_map[a].append(b)
            else:
                trust_map[a] = [b]

        trusted_by_map = {}
        for a, b in trust:
            if b in trusted_by_map:
                trusted_by_map[b].append(a)
            else:
                trusted_by_map[b] = [a]

        print(trusted_by_map)

        # if the entrusted person is trusted by n-1 people and does not trust anyone
        # return that person
        for person in range(1, n + 1):
            if person in trusted_by_map and len(trusted_by_map[person]) == n - 1:
                # check if this person trusts anyone from trust_map
                if person not in trust_map:
                    return person

        return -1