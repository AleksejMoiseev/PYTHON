

class BaseEmployee:
    def __init__(self, config, working_hours, plan_completion, experience, kpi, *args, **kwargs):
        self.config = config
        self.working_hours = working_hours
        self.plan_completion = plan_completion
        self.experience = experience
        self.kpi = kpi

    @property
    def get_kpi(self):
        return self.config.config_kpi.value

    @property
    def get_plan(self):
        return self.config.coefficient_by_plan.value

    @property
    def get_hour_rate_base(self):
        return self.config.hour_rate.value

    def get_extra_by_plan(self):
        for plan, _, extra in self.get_plan:
            if plan.check(self.plan_completion):
                return extra

    def get_extra_by_kpi(self):
        for kpi_interval, excp_interval, extra in self.get_kpi:
            if kpi_interval.check(self.kpi) and excp_interval.check(self.experience):
                return extra

    def get_base_salary(self):
        return self.working_hours * self.get_hour_rate()

    def get_hour_rate(self):
        pay_extra = self.get_extra_by_plan()
        if not pay_extra:
            return self.get_hour_rate_base
        return self.get_hour_rate_base * pay_extra['coef']

    def payroll(self):
        salary = self.get_base_salary()
        premium = self.get_extra_by_kpi()
        salary = salary * premium['coef'] + premium['extra']
        return salary


class Employee(BaseEmployee):
    def __init__(self, name, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.position = position
