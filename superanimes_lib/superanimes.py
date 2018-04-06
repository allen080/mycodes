#!C:\Python34\python.exe
import requests
import shutil
import sys

class Superanimes(object):
	'''
	Biblioteca desenvolvida para facilitar o download de animes e desenhos do site https://www.superanimes.site

	*OBS: biblioteca ainda nao esta finalizada e se encontra na sua versao de testes

	uso: s = Superanimes('anime')
	'''
	def __init__(self,anime):
		self.anime = ''
		for i in anime.strip():
			if i==' ':
				self.anime+='-'
			else:
				self.anime+=i

		self.url = 'http://www.superanimes.site/anime/%s/episodio-'%self.anime
		if requests.get('http://www.superanimes.site/anime/%s'%self.anime).ok:
			self.status = 'anime found on superanimes'
		else:
			self.status = 'anime not found'
	def num_episodes(self):
		'''
		return the number of eps of the anime/cartoon
		'''
		quant_ep=1

		while True:
			req = requests.get(self.url+str(quant_ep))

			if req.status_code!=200:
				quant_ep-=1
				break
			else:
				quant_ep+=1

		return quant_ep

	def search(self):
		'''
		return a list with names of animes/cartoon founds.
		'''
		search_anime = ''

		for i in self.anime:
			if i=='-':
				search_anime+='+'
			else:
				search_anime+=i
		search_url = 'https://www.superanimes.site/busca?parametro=%s'%search_anime
		
		temp = sys.stderr
		sys.stderr = open('nul','w')

		search = requests.get(search_url,verify=False).text.split()

		animes_found = set()

		for i in range(len(search)):
			if 'superanimes.site/anime' in search[i] or 'superanimes.site/cartoon' in search[i]: #and 'title' in search[i]: #and 'title="Animes"' not in search[i]:
				anime = search[i].split('"')[1].split('/')[-1]

				if 'anime'!=anime.lower() and 'cartoon'!=anime.lower():
					animes_found.add(anime)

		sys.stderr = temp
		return list(animes_found)

	def download(self,first_ep,last_ep=False):
		'''
		Downloads some eps from the anime/cartoon

		self.first_ep = the first ep to download.

		self.last_ep = the last ep in the range of eps to download. if last_ep is not set, it will download only the first ep.
		'''
		if not last_ep:
			last_ep=first_ep

		for ep in range(first_ep,last_ep+1):
			
			url_download = self.url+str(ep)+'/baixar'
			name = '%s-episode_%i.mp4'%(self.anime,ep)

			req = requests.get(url_download).text.split()

			print('[*] Downloading episode %i'%ep)

			for html in range(len(req)):
				if 'Clique' in req[html]:
					download = req[html-2].split('"')[1]
					
					temp = sys.stderr
					sys.stderr = open('nul','w')
					
					r = requests.get(download,verify=False,stream=True)
					r.raw_decode_content = True

					temp = sys.stderr
					sys.stderr = open('nul','w')

					with open(name,'wb') as episode:
						shutil.copyfileobj(r.raw,episode)

			print('[*] file saved as %s\n'%name)
			sys.stderr = temp
	def download_all(self):
		'''
		Downloads all episodes on the anime/cartoon.
		'''
		eps = self.num_episodes()
		print('[*] Downloading all %i episodes\n'%eps)
		self.download(1,eps+1)

if __name__=='__main__':
	s = Superanimes('jojo')
	l = s.search()
	print(l); i=int(input('escolha um: '))
	s = Superanimes(l[i])
	print(s.num_episodes())
	
	#print(s.num_episodes)
	#s.download(111,111)
	#print(s.search())