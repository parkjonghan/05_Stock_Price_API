import matplotlib.pyplot as plt
from Investar import Analyzer  # ①

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

mk = Analyzer.MarketDB()  # ②
df = mk.get_daily_price('000020', '2021-01-23', '2021-02-05')  # ③

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.title('동화약품 (Investar Data)')
plt.plot(df.index, df['close'], 'c', label='Close')  # ④
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()