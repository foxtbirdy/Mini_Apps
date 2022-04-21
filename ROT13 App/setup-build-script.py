# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-21 22:29:09
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-21 22:56:12


import cx_Freeze

executables = [cx_Freeze.Executable("Program-Files/app.py")]

cx_Freeze.setup(
	name="ROT13 App",
	options= {
		"build_exe": {
			"packages": [
				"PyQt5",
				"pyperclip"],
			"include_files": ["Program-Files/design.css","Program-Files/resources.py"]

		}
	},
	version = "1.2",
	description = "Encrypts Raw Text into ROT13.",
	executables = executables
	)
