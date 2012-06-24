import sublime, sublime_plugin
import commands

platform =  sublime.platform()
packages_path = sublime.packages_path()
packages_path = packages_path.replace(' ', '\ ')

class rungiboCommand(sublime_plugin.WindowCommand, sublime.Window):
	string = packages_path+'/Gitignore/gibo '
	first_chosen = ''
	chosen_array = []
	names = ''

	first_list = ['Actionscript', 'Android', 'Autotools', 'CakePHP', 'CFWheels', 'C', 'C++', 'Clojure', 'CMake', 'CodeIgniter', 'Compass', 'Concrete5', 'Coq', 'CSharp', 'Delphi', 'Django', 'Drupal', 'Erlang', 'ExpressionEngine', 'Finale', 'ForceDotCom', 'FuelPHP', 'gcov', 'Go', 'Grails', 'GWT', 'Haskell', 'Java', 'Jboss', 'Jekyll', 'Joomla', 'Jython', 'Kohana', 'LaTeX', 'Leiningen', 'LemonStand', 'Lilypond', 'Lithium', 'Magento', 'Maven', 'nanoc', 'Node', 'Objective-C', 'OCaml', 'Opa', 'opencart', 'OracleForms', 'Perl', 'PlayFramework', 'Python', 'Qooxdoo', 'Rails', 'R', 'RhodesRhomobile', 'Ruby', 'Scala', 'SeamGen', 'SketchUp', 'SugarCRM', 'Symfony2', 'Symfony', 'SymphonyCMS', 'Target3001', 'Tasm', 'Textpattern', 'TurboGears2', 'Unity', 'VB.Net', 'Waf', 'Wordpress', 'Yii', 'ZendFramework', 'Archives', 'CVS', 'Eclipse', 'Emacs', 'Espresso', 'FlexBuilder', 'IntelliJ', 'Linux', 'Matlab', 'Mercurial', 'ModelSim', 'MonoDevelop', 'NetBeans', 'OSX', 'Quartus2', 'Redcar', 'RubyMine', 'SASS', 'SBT', 'SublimeText', 'SVN', 'Tags', 'TextMate', 'vim', 'VisualStudio', 'Windows', 'XilinxISE']

	second_list = ['Done', 'Actionscript', 'Android', 'Autotools', 'CakePHP', 'CFWheels', 'C', 'C++', 'Clojure', 'CMake', 'CodeIgniter', 'Compass', 'Concrete5', 'Coq', 'CSharp', 'Delphi', 'Django', 'Drupal', 'Erlang', 'ExpressionEngine', 'Finale', 'ForceDotCom', 'FuelPHP', 'gcov', 'Go', 'Grails', 'GWT', 'Haskell', 'Java', 'Jboss', 'Jekyll', 'Joomla', 'Jython', 'Kohana', 'LaTeX', 'Leiningen', 'LemonStand', 'Lilypond', 'Lithium', 'Magento', 'Maven', 'nanoc', 'Node', 'Objective-C', 'OCaml', 'Opa', 'opencart', 'OracleForms', 'Perl', 'PlayFramework', 'Python', 'Qooxdoo', 'Rails', 'R', 'RhodesRhomobile', 'Ruby', 'Scala', 'SeamGen', 'SketchUp', 'SugarCRM', 'Symfony2', 'Symfony', 'SymphonyCMS', 'Target3001', 'Tasm', 'Textpattern', 'TurboGears2', 'Unity', 'VB.Net', 'Waf', 'Wordpress', 'Yii', 'ZendFramework', 'Archives', 'CVS', 'Eclipse', 'Emacs', 'Espresso', 'FlexBuilder', 'IntelliJ', 'Linux', 'Matlab', 'Mercurial', 'ModelSim', 'MonoDevelop', 'NetBeans', 'OSX', 'Quartus2', 'Redcar', 'RubyMine', 'SASS', 'SBT', 'SublimeText', 'SVN', 'Tags', 'TextMate', 'vim', 'VisualStudio', 'Windows', 'XilinxISE']


	def run(self):
		self.window.show_quick_panel(self.first_list, self.first_select)

	def first_select(self, index):
		if index > -1:
			self.first_chosen = index
			self.names = self.first_list[index];
			self.window.show_quick_panel(self.second_list, self.second_select)


	def second_select(self, index):
		if index > -1:
			if index == 0:
				self.write_file()
			else:
				self.names = self.names+' '+self.second_list[index]
				self.window.show_quick_panel(self.second_list, self.second_select)


	def write_file(self):
		self.string = self.string + self.names

		output = commands.getoutput(self.string)

		view = sublime.active_window().new_file()
		edit = view.begin_edit()
	   	view.insert(edit, 0, output)
	   	view.end_edit(edit)