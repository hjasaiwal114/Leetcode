class Solution:
    def average(self, salary: List[int]) -> float:
        total_salary = sum(salary)
        num_salaries = len(salary)
        avg_salary = total_salary / num_salaries
        return avg_salary
