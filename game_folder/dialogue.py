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
			'file': ['bui/bui1.png',
					'bui/bui2.png',
					'bui/bui3.png',
					'bui/bui4.png'],
			'dialogue': [
				[
					'~~WAKE ME UP! Wake me up inside.~~',
					'Oh hello..',
					'Welcome to Systems Programming!',
					'Normally I would start class...',
					'but hackers are attacking the student machines!',
					'I need you to use spidey to shoot down the viruses.',
					'Use the arrow keys to aim and the up arrow to shoot webs.'
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
				"Hey Player, your name came out of the bag!",
				"You've been voluntold to come up to the board and show off your knowledge of logic gates!"
				],
				[
				'Flip the cards to match the logic gates...',
				"BUT DON'T GET BITTEN!"
				],
				[
				"Aww... you got bit!",
				"Try again and there might be some raisins in it for you!"
				],
				[
				"Way to go! Thanks for coming to class!",
				""
				]
			],
			'logic': {
				'called': False,
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
			'file': '',
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
			'file': '',
			'dialogue': [
				['SQUEAK'],
				['Squeak squeak squeak squeak']
			],
			'logic': {}
		},
		{
			'name': 'Professor Bualuan',
			'rand': False,
			'file': ['bualuan/bualuan1.png',
					'bualuan/bualuan2.png',
					'bualuan/bualuan3.png',
					'bualuan/bualuan4.png'],
			'dialogue': [
				[
					'Hi, Professor. Can I please have my PIN number?'
				],
				[
					'Sure. Just go and catch three squirrels first.'
				],
				[
					'Good job! Here you go.'
				],
				[
					'6:55, good time!'
				],
				[
					'7:50, better luck next semester.'
				],
				[
					'Come to Salsa Night at Legends!'
				]
			],
			'logic': {
				'spoken': False,
				'completed': False,
				'squirrels': 0,

			}
		},
	]
}
