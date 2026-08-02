class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        n = len(votes[0])
        rank = {}

        for team in votes[0]:
            rank[team] = [0] * n

        for vote in votes:
            for pos,team in enumerate(vote):
                rank[team][pos] += 1

        teams = list(rank.keys())
        teams.sort(key=lambda x: ([-c for c in rank[x]], x))

        return "".join(teams)