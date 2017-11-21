import scrapy
import json

class PokemonSpider(scrapy.Spider):
	name = 'pokemon'

	def start_requests(self):
		yield scrapy.Request(url = 'https://pokemondb.net/pokedex/national', callback = self.parse)

	def parse(self, response):
		arr = []
		
		for card in response.css('span.infocard-tall'):
			id   = card.css('small::text').extract_first()
			name = card.css('.ent-name::text').extract_first()
			url_details = 'http://pokemondb.net/pokedex/%s' % name.lower()
			types = []
			
			for type in card.css('small.aside a'):
				types.append(type.css('::text').extract_first())

			arr.append({
				'id': id,
				'name': name,
				'url_details': url_details,
				'types': types
			})
			
		with open('pokemons.json', 'wb') as f:
			json.dump(arr, f)
		# name = response.css('span.infocard-tall .ent-name::text').extract_first()
		# self.log('Pokemon Name : %s' % name)
		# id = response.css('span.infocard-tall small::text').extract_first()
		# self.log('Pokemon id: %s' % id)
		# types = response.css('span.infocard-tall small.aside a::text').extract_first()
		# self.log('Pokemon type: %s' % types)
		