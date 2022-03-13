import operator
from dataclasses import dataclass
from enum import Enum


@dataclass
class ConfInterval:
    start: str
    stop: str

    def check(self, v):
        _cfg = {
            '>=': operator.ge,
            '<=': operator.le,
            '>': operator.gt,
            '<': operator.lt,
        }
        start, op_start = None, None
        stop, op_stop = None, None
        for k, _op in _cfg.items():
            if self.start.startswith(k) and start is None:
                start, op_start = int(self.start[len(k):]), _op
            if self.stop.startswith(k) and stop is None:
                stop, op_stop = int(self.stop[len(k):]), _op

        if op_start(v, start) and op_stop(v, stop):
            return True
        return False


@dataclass
class KPI(ConfInterval):
    pass


@dataclass
class EXP(ConfInterval):
    pass


@dataclass
class PLAN(ConfInterval):
    pass


default = ('>=0', '<=1000')


class ConfigSalesman(Enum):
    hour_rate = 80
    coefficient_by_plan = [
        (PLAN('>0', '<90'), EXP(*default), {'coef': 0.5, 'extra': 0}),
        (PLAN('>=90', '<100'), EXP(*default), {'coef': 0.8, 'extra': 0}),
        (PLAN('>=100', '<1000'), EXP(*default), {'coef': 1.5, 'extra': 0}),
    ]
    config_kpi = [
        (
            KPI('>0', '<85'),
            EXP('>0', '<=1000'),
            {'coef': 1, 'extra': 0}
        ),
        (
            KPI('>=85', '<105'),
            EXP('>=0', '<1000'),
            {'coef': 1, 'extra': 0}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>=0', '<=5'),
            {'coef': 1, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>5', '<=10'),
            {'coef': 1.02, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>10', '<=15'),
            {'coef': 1.05, 'extra': 500}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>15', '<=20'),
            {'coef': 1.07, 'extra': 700}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>20', '<=1000'),
            {'coef': 1.1, 'extra': 1000}
        ),
    ]


class ConfigDriver(Enum):
    hour_rate = 100
    coefficient_by_plan = [
        (PLAN('>0', '<80'), EXP(*default), {'coef': 0.8, 'extra': 0}),
        (PLAN('>=80', '<100'), EXP(*default), {'coef': 0.9, 'extra': 0}),
        (PLAN('>=100', '<1000'), EXP(*default), {'coef': 1.1, 'extra': 0}),
    ]
    config_kpi = [
        (
            KPI('>0', '<90'),
            EXP('>0', '<=1000'),
            {'coef': 0.9, 'extra': 0}
        ),
        (
            KPI('>=90', '<100'),
            EXP('>=0', '<1000'),
            {'coef': 1, 'extra': 0}
        ),
        (
            KPI('>=100', '<1000'),
            EXP('>=0', '<=5'),
            {'coef': 1, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>5', '<=10'),
            {'coef': 1.02, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>10', '<=15'),
            {'coef': 1.05, 'extra': 500}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>15', '<=20'),
            {'coef': 1.07, 'extra': 700}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>20', '<=1000'),
            {'coef': 1.1, 'extra': 1000}
        ),
    ]


class ConfigAccountant(Enum):
    hour_rate = 110
    coefficient_by_plan = [
        (PLAN('>0', '<90'), EXP(*default), {'coef': 0.85, 'extra': 0}),
        (PLAN('>=90', '<100'), EXP(*default), {'coef': 0.95, 'extra': 0}),
        (PLAN('>=100', '<1000'), EXP(*default), {'coef': 1.3, 'extra': 0}),
    ]
    config_kpi = [
        (
            KPI('>0', '<80'),
            EXP('>0', '<=1000'),
            {'coef': 0.9, 'extra': 0}
        ),
        (
            KPI('>=80', '<100'),
            EXP('>=0', '<1000'),
            {'coef': 1, 'extra': 0}
        ),
        (
            KPI('>=100', '<1000'),
            EXP('>=0', '<=5'),
            {'coef': 1, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>5', '<=10'),
            {'coef': 1.02, 'extra': 200}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>10', '<=15'),
            {'coef': 1.05, 'extra': 500}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>15', '<=20'),
            {'coef': 1.07, 'extra': 700}
        ),
        (
            KPI('>=105', '<1000'),
            EXP('>20', '<=1000'),
            {'coef': 1.1, 'extra': 1000}
        ),
    ]


parse_conf = {
    'водитель': ConfigDriver,
    'продавец': ConfigSalesman,
    'бухгалтер': ConfigAccountant,
}
