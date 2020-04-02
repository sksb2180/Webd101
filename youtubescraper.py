from pytube import Playlist, YouTube

#website = 'https://www.youtube.com/playlist?list=PLE50-dh6JzC6dHxpAno-a6W7QpWdAFN20'
#r = requests.get(website)
#soup = BeautifulSoup(r.text,features="lxml")
#tgt_list = [a['href'] for a in soup.find_all('a', href=True)]
#tgt_list = [n for n in tgt_list if re.search('watch', n)]
#unique_list = []
#for n in tgt_list:
#    if n not in unique_list:
 #       unique_list.append(n)
# all the videos link in a playlist
#unique_list = ['https://www.youtube.com' + n for n in unique_list]
#for link in unique_list:
#    print(link)
#    y = YouTube(link)
#    t = y.streams
#    t[0].download(output_path=r'C:\Users\sksb2\OneDrive\Desktop\Shared')



pl = Playlist("https://www.youtube.com/playlist?list=PLaL2yxczKLcB-XsKN_31vfmYuhTAQYrJu")

for u in pl.video_urls[31:]:
    print(u)
    y = YouTube(u)
    t = y.streams
    t[0].download(output_path=r'C:\Users\sksb2\OneDrive\Desktop\Shared')

