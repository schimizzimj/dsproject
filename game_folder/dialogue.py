'''
Stores all dialogue from the different NPCs in the game. Each list within the
dialogue list is an individual conversation. Additionally, file can be update with
the file name of the spritesheet (although the NPC class must be updated).
'''

game_json = {
	'npcs': [
		{
			'name': 'Professsor Bui',
			'rand': False,
			'file': '',
			'dialogue': [
				[
					'~~WAKE ME UP! Wake me up inside.~~',
					'Oh hello..',
					'Welcome to Systems Programming!'
				]
			]
		},

		{
			'name': 'Professsor Brockman',
			'rand': False,
			'file': '',
			'dialogue': [
				[
				'Welcome to Logic Design!',
				'Are you ready for adventure?'
				]
			]
		},

		{
			'name': 'Professsor Emrich',
			'rand': False,
			'file': './img/scott.png',
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Are you ready for adventure?'
				]
			]
		},

		{
			'name': 'Professsor Kumar',
			'rand': False,
			'file': './img/shreya.png',
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Thanks for coming down to the front.'
                'Here\'s a million points'
				]
			]
		},

		{
			'name': 'Squirrel',
			'rand': True,
			'dialogue': [
				['SQUEAK'],
				['Squeak squeak squeak squeak']
			]
		}
	]
}
