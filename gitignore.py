import os
import zipfile

import sublime, sublime_plugin

class rungiboCommand(sublime_plugin.WindowCommand):

	_bp_list = []
	_bp_folder = 'boilerplates'
	_package_path = ''

	def _find_path(self):
		if not self._package_path:
			paths = [os.path.join(sublime.installed_packages_path(), 'Gitignore.sublime-package'),
					 os.path.join(sublime.packages_path(), 'Gitignore'),
					 os.path.join(sublime.packages_path(), 'Sublime-Gitignore')]
			for path in paths:
				if os.path.exists(path):
					self._package_path = path
					break

		return self._package_path

	def _listdir(self):
		package_path = self._find_path()
		if zipfile.is_zipfile(package_path):
			# Dealing with .sublime-package file
			package = zipfile.ZipFile(package_path, "r")
			path = self._bp_folder + "/"
			return [f.replace(path, '') for f in package.namelist() if f.startswith(path)]
		else:
			return os.listdir(os.path.join(package_path, self._bp_folder))

	def _loadfile(self, bp):
		package_path = self._find_path()
		if zipfile.is_zipfile(package_path):
			# Dealing with .sublime-package file
			package = zipfile.ZipFile(package_path, 'r')
			path = self._bp_folder + "/" + bp
			f = package.open(path, 'r')
			text = f.read().decode()
			f.close()
			return text
		else:
			file_path = os.path.join(package_path, self._bp_folder, bp)
			f = open(file_path, 'r')
			text = f.read().decode()
			f.close()
			return text

	def build_list(self):
		if not self._bp_list:
			for dir in self._listdir():
				self._bp_list.append(dir.replace('.gitignore', ''))

		self.chosen_array = []
		self.first_list = self._bp_list[:]  # Copy _bp_list
		self.second_list = ['Done'] + self._bp_list

	def show_quick_panel(self, options, done):
		# Fix from
		# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=10999
		sublime.set_timeout(lambda: self.window.show_quick_panel(options, done), 10)

	def run(self):
		self.build_list()
		self.show_quick_panel(self.first_list, self.first_select)

	def first_select(self, index):
		if index > -1:
			self.chosen_array.append(self.first_list[index])
			self.second_list.remove(self.first_list[index])
			self.show_quick_panel(self.second_list, self.second_select)

	def second_select(self, index):
		if index == 0:
			self.write_file()
			self.build_list()
		elif index > 0:
			self.chosen_array.append(self.second_list[index])
			self.second_list.remove(self.second_list[index])
			self.show_quick_panel(self.second_list, self.second_select)

	def write_file(self):
		final = ''

		for bp in self.chosen_array:
			text = self._loadfile(bp + ".gitignore")
			final = final + '###' + bp + '###\n\n' + text + '\n\n'

		final = final.strip()
		view = sublime.active_window().new_file()
		view.run_command('writegibo', {'bp': final})


class writegiboCommand(sublime_plugin.TextCommand):

	def run(self, edit, **kwargs):
		self.view.insert(edit, 0, kwargs['bp'])
		self.view.set_name('.gitignore')
