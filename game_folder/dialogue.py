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
					'Welcome to Systems Programming!',
					'Could you do me a favor and unbork these computers?'
				],
				[
					'That did not go to well.',
					"I'll give you an extension then."
				],
				[
					'You did it! Congrats!',
					'~~City of stars, are you shining just for me?~~',
					'~~City of stars...'
				]
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
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
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
		},

		{
			'name': 'Professsor Emrich',
			'rand': False,
			'file': ['img/emrich/emrich1.png',
					'img/emrich/emrich2.png',
					'img/emrich/emrich3.png',
					'img/emrich/emrich4.png'],
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Are you ready for adventure?'
				]
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
		},

		{
			'name': 'Professsor Kumar',
			'rand': False,
			'file': '',
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Are you ready for adventure?'
				]
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
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
