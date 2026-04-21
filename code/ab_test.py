import math
from scipy import stats

a_imps = int(input("a 노출수 : "))
a_clicks = int(input("a 클릭수 : "))
b_imps = int(input("b 노출수 : "))
b_clicks = int(input("b 클릭수 : "))

# 클릭률 = 노출수 / 클릭수
a_ctr = float(a_clicks / a_imps)
b_ctr = float(b_clicks / b_imps)

print(a_ctr, b_ctr)

# 클릭률 차이
ctr_diff = abs(b_ctr - a_ctr)

# 클릭률 표준오차
a_SE = math.sqrt((a_ctr*(1-a_ctr))/a_imps)
b_SE = math.sqrt((b_ctr*(1-b_ctr))/b_imps)

SE_diff = round(math.sqrt(a_SE**2 + b_SE**2), 5)

#z-score
z = round(ctr_diff/SE_diff, 2)
print('z :', z )

p_value = 2 * (1 - stats.norm.cdf(abs(z))) # 양측 검증이라 1에서 뺌
print(p_value)

if p_value >= 0.05:
    print('귀무가설 기각 실패, p-value : ', p_value)
elif p_value < 0.05:
    print('귀무가설 기각, p-value : ', p_value)
else:
    print('error')