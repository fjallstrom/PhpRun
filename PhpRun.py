import sublime, sublime_plugin, os, commands

class PhprunCommand(sublime_plugin.TextCommand):

    def run(self, edit):  
		path = self.view.file_name()
		root, extension = os.path.splitext(path)
		if extension in [".php"]:

			# first check if we have any errors
			command = "php -l " + path
			response = commands.getoutput(command)

			if "No syntax errors detected in" in response:
				# if no errors, display php output
				command = "php " + path
				response = commands.getoutput(command)

			sublime.error_message("--- PHP Run output: ---\n" + response)