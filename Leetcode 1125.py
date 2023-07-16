"""
1125. Smallest Sufficient Team
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.
"""
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        mainTeam = []
        map = {}
        i = 0
        for skill in req_skills:
            map[skill] = i
            i += 1

        reqSkills = (1 << i) - 1
        skills = self.getPeopleSkillsMask(people, map)
        localTeam = []
        self.findTeam(reqSkills, skills, 0, 0, localTeam, mainTeam)
        return mainTeam

    def getPeopleSkillsMask(self, people, map):
        skills = []
        for person in people:
            skillMask = 0
            for skill in person:
                skillMask |= 1 << map[skill]
            skills.append(skillMask)
        return skills

    def findTeam(self, reqSkills, skills, teamSkills, person, localTeam, mainTeam):
        if len(mainTeam) > 0 and len(localTeam) >= len(mainTeam) - 1 or person == len(skills):
            return

        localTeam.append(person)

        if (teamSkills | skills[person]) == reqSkills:
            if len(mainTeam) == 0 or len(localTeam) < len(mainTeam):
                mainTeam[:] = localTeam[:]
            localTeam.pop()
            return
        elif (teamSkills | skills[person]) > teamSkills:
            self.findTeam(reqSkills, skills, teamSkills | skills[person], person + 1, localTeam, mainTeam)

        localTeam.pop()
        self.findTeam(reqSkills, skills, teamSkills, person + 1, localTeam, mainTeam)