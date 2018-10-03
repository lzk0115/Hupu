from wordcloud import WordCloud
import matplotlib.pyplot as plt
words = []
with open('sampleList.txt', 'r') as fin:
    for line in fin:
        words.append(line.strip())

word = WordCloud(font_path="fangsong_GB2312.ttf",max_words=1000,width=1080, height=920).generate(' '.join(words[:1000]))
plt.imshow(word)
plt.axis('off')
plt.show()