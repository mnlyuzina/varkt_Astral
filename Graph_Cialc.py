from math import *
from matplotlib import pyplot as plt

# Масса Земли в килограммах, величина гравитационной постоянной
M_Earth = 5.976 * 10 ** 24
G = 6.67 * 10 ** -11
r_earth = 6378000
# Список удельных импульсов ступеней ракеты в секундах, список масс ступеней ракеты, список высот, на которых отбрасываются ступени
sp_imp = [360, 361, 361]
sp_m_stage = [458_900, 168_300, 46_562]
sp_r = [42_000, 120_000, 151_000]


# Масса ракеты в килограммах
M_main = 705_000
# Масса ракеты без топлива в килограммах
M_main_without_fuel = 636_100
# Запас топлива в ступенях
fuel1 = 15_100
fuel2 = 15_100
fuel3 = 18_700


def Cialc(imp, m1, m2):  # просчет изменения скорости
    return imp * log(m1/m2)


part_1 = abs(Cialc(sum(sp_imp)/len(sp_imp), M_main, M_main_without_fuel))
part_2 = abs(Cialc(sum(sp_imp[1:])/2, M_main - sp_m_stage[0], (M_main_without_fuel - sp_m_stage[0] - fuel1) + sp_m_stage[1] - fuel2 + sp_m_stage[2] - fuel3))
part_3 = abs(Cialc(sp_imp[2], M_main - sum(sp_m_stage[:2]), (M_main_without_fuel - sp_m_stage[0] - fuel1 - sp_m_stage[1] - fuel2)+ sp_m_stage[2]-fuel3))
print((M_main_without_fuel - sp_m_stage[0] - fuel1) + sp_m_stage[1] - fuel2 + sp_m_stage[2] - fuel3)
print(M_main - sp_m_stage[0])
print(part_3)

plt.plot([part_1, part_2, part_3], sp_r)
print(part_1, part_2, part_3)
plt.title('График зависимости скорости oт высоты')
plt.ylabel('м')
plt.xlabel('м/c')
plt.show()
