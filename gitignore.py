import sublime, sublime_plugin
import commands
import os

platform =  sublime.platform()
packages_path = sublime.packages_path()
packages_path = packages_path.replace(' ', '\ ')

class rungiboCommand(sublime_plugin.WindowCommand, sublime.Window):
	def run(self):
		print packages_path
		os.system('chmod +x '+packages_path+'/Gitignore/gibo')
		#filepath = self.view.file_name()
		files = commands.getoutput(packages_path+'/Gitignore/gibo --list')
		files_list = files.split('\n')
		files_list.remove('=== Languages ===')
		files_list.remove('=== Global ===')
		files_list = filter(None, files_list)
		#print files_list
		# files.remove(''Archives', 'CVS', 'Eclipse', 'Emacs', 'Espresso', 'FlexBuilder', 'IntelliJ', 'Linux', 'Matlab', 'Mercurial', 'ModelSim', 'MonoDevelop', 'NetBeans', 'OSX', 'Quartus2', 'Redcar', 'RubyMine', 'SASS', 'SBT', 'SublimeText', 'SVN', 'Tags', 'TextMate', 'vim', 'VisualStudio', 'Windows', 'XilinxISE'')
		#print files_list
		self.window.show_quick_panel(files_list, self.callback)

	def callback(self, index):
		if not self.window.views():
			self.window.new_file()

		files = commands.getoutput(packages_path+'/Gitignore/gibo --list')
		files_list = files.split('\n')
		files_list.remove('=== Languages ===')
		files_list.remove('=== Global ===')
		files_list = filter(None, files_list)
		
		#filter_array = ['Actionscript', 'Android', 'Autotools', 'CakePHP', 'CFWheels', 'C', 'C++', 'Clojure', 'CMake', 'CodeIgniter', 'Compass', 'Concrete5', 'Coq', 'CSharp', 'Delphi', 'Django', 'Drupal', 'Erlang', 'ExpressionEngine', 'Finale', 'ForceDotCom', 'FuelPHP', 'gcov', 'Go', 'Grails', 'GWT', 'Haskell', 'Java', 'Jboss', 'Jekyll', 'Joomla', 'Jython', 'Kohana', 'LaTeX', 'Leiningen', 'LemonStand', 'Lilypond', 'Lithium', 'Magento', 'Maven', 'nanoc', 'Node', 'Objective-C', 'OCaml', 'Opa', 'opencart', 'OracleForms', 'Perl', 'PlayFramework', 'Python', 'Qooxdoo', 'Rails', 'R', 'RhodesRhomobile', 'Ruby', 'Scala', 'SeamGen', 'SketchUp', 'SugarCRM', 'Symfony2', 'Symfony', 'SymphonyCMS', 'Target3001', 'Tasm', 'Textpattern', 'TurboGears2', 'Unity', 'VB.Net', 'Waf', 'Wordpress', 'Yii', 'ZendFramework']

		#editor_list = list(set(files_list) - set(filter_array))

		#print editor_list

		#What gitingore is chosen?
		if index <= 71:
			editor_list = ['None', 'Archives', 'CVS', 'Eclipse', 'Emacs', 'Espresso', 'FlexBuilder', 'IntelliJ', 'Linux', 'Matlab', 'Mercurial', 'ModelSim', 'MonoDevelop', 'NetBeans', 'OSX', 'Quartus2', 'Redcar', 'RubyMine', 'SASS', 'SBT', 'SublimeText', 'SVN', 'Tags', 'TextMate', 'vim', 'VisualStudio', 'Windows', 'XilinxISE']
			global chosen
			chosen = files_list[index]

			self.window.show_quick_panel(editor_list, self.callback2)


		else:
			os.system(packages_path+'/Gitignore/gibo '+files_list[index]+'>> /home/adam/Desktop/'+files_list[index]+'.gitignore')

	def callback2(self, index):

		if not self.window.views():
			self.window.new_file()

		editor_list = ['None', 'Archives', 'CVS', 'Eclipse', 'Emacs', 'Espresso', 'FlexBuilder', 'IntelliJ', 'Linux', 'Matlab', 'Mercurial', 'ModelSim', 'MonoDevelop', 'NetBeans', 'OSX', 'Quartus2', 'Redcar', 'RubyMine', 'SASS', 'SBT', 'SublimeText', 'SVN', 'Tags', 'TextMate', 'vim', 'VisualStudio', 'Windows', 'XilinxISE']
		os.system('rm -r '+packages_path+'/Gitignore/tmp/tmp.gitignore')
		if index == 0:
			
			os.system(packages_path+'/Gitignore/gibo '+chosen+' >> '+packages_path+'/Gitignore/tmp/tmp.gitignore')
		else:
			os.system(packages_path+'/Gitignore/gibo '+chosen+' '+editor_list[index]+' >> '+packages_path+'/Gitignore/tmp/tmp.gitignore')

		filebuf = open(packages_path+'/Gitignore/tmp/tmp.gitignore', 'r')
		bufferstring = filebuf.read()
		filebuf.close()
		view = sublime.active_window().new_file()
		edit = view.begin_edit()
   		view.insert(edit, 0, bufferstring)
   		view.end_edit(edit)