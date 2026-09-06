class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x: (x[0], -x[1]))

        max_defense = 0
        weak = 0

        for attack, defense in reversed(properties):
            if defense < max_defense:
                weak += 1
            max_defense = max(max_defense, defense)

        return weak