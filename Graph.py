from matplotlib import pyplot as plt

# Масса Земли в килограммах, величина гравитационной постоянной

M_Earth = 5.976 * 10 ** 24
G = 6.67 * 10 ** -11
r_earth = 6378000

# Список масс (с учетом топлива) ступеней ракеты в килограммах, высот, на которых находилась ракета во время отброса ступеней

sp_m_stage = [0, 458_900, 168_300, 46_562]
sp_r = [0, 42_000, 120_000, 151_000]

# Список масс (с учетом топлива) ступеней ракеты в килограммах, высот, на которых находилась ракета во время отброса ступеней с учетом погрешностей

sp_m_stage_ksp = [0, 458_850, 168_268, 46_530]
sp_r_ksp = [0, 41_957, 119_970, 150_961.5]

# Масса ракеты в килограммах

M_main = 705_000

# Масса ракеты в килограммах с учетом погрешности

M_main_ksp = 704_968


def Law_of_Gravity(m2, h):  # просчет изменения силы притяжения
    return G * (M_Earth * m2) / ((r_earth + h) ** 2)


part_1 = Law_of_Gravity(M_main - sum(sp_m_stage[:1]), sp_r[0])
part_2 = Law_of_Gravity(M_main - sum(sp_m_stage[:2]), sp_r[1])
part_3 = Law_of_Gravity(M_main - sum(sp_m_stage[:3]), sp_r[2])
part_4 = Law_of_Gravity(M_main - sum(sp_m_stage[:4]), sp_r[3])

part_1_ksp = Law_of_Gravity(M_main_ksp - sum(sp_m_stage_ksp[:1]), sp_r_ksp[0])
part_2_ksp = Law_of_Gravity(M_main_ksp - sum(sp_m_stage_ksp[:2]), sp_r_ksp[1])
part_3_ksp = Law_of_Gravity(M_main_ksp - sum(sp_m_stage_ksp[:3]), sp_r_ksp[2])
part_4_ksp = Law_of_Gravity(M_main_ksp - sum(sp_m_stage_ksp[:4]), sp_r_ksp[3])

plt.plot([part_1, part_2, part_3, part_4], sp_r)
plt.plot([part_1_ksp, part_2_ksp, part_3_ksp, part_4_ksp], sp_r_ksp)
plt.title('График зависимости силы всемирного тяготения от высоты')
plt.ylabel('м')
plt.xlabel('н')
plt.legend(['Math', 'KSP'])
plt.show()
