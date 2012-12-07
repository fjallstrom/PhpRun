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
			
			tmp_file_path = "/tmp/phprun-output.tmp"
       		
  			f = open(tmp_file_path, 'w+')
			f.write(response)
			f.close()

      		view = self.view.window().open_file(tmp_file_path)
