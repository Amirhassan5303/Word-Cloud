from wordcloud import WordCloud
import matplotlib.pyplot as plt


movies = open('data/movies.txt').readlines()
movies = list(map(str.strip, movies))

text = ' '.join(movies)

wordcloud = WordCloud(background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
wordcloud.to_file('data/movies.png')


