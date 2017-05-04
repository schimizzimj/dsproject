'''
Stores all dialogue from the different NPCs in the game. Each list within the
dialogue list is an individual conversation. Additionally, file can be update with
the file name of the spritesheet (although the NPC class must be updated).
'''

game_json = {
	'npcs': [
		{
			'name': 'Professor Bui',
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
			'name': 'Professor Brockman',
			'rand': False,
			'file': '',
			'dialogue': [
				[
				'Welcome to Logic Design!',
				'Are you ready for adventure?'
				],
				[
				"I don't have a game.",
				"Why don't I have a game?!"
				]
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
		},

		{
			'name': 'Professor Emrich',
			'rand': False,
			'file': ['emrich/emrich1.png',
					'emrich/emrich2.png',
					'emrich/emrich3.png',
					'emrich/emrich4.png'],
			#'file': './img/scott.png',
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Are you ready for adventure?'
				],
				[
				"I don't have a game.",
				"Why don't I have a game?!"
				]
			],
			'logic': {
				'spoken': False,
				'completed': False
			}
		},

		{
			'name': 'Professor Kumar',
			'rand': False,
			'file': 'shreya.png',
			'dialogue': [
				[
				'Welcome to Data Structures!',
				'Thanks for coming down to the front.'
                "Here's a million points!"
				],
				[
				"I think you've already completed the task.",
				"Here's a million more points though!"
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
