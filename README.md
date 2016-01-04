# django-example

	$ mkdir example
	$ cd example
	$ git init
	$ git config credential.helper store
	$ git config --global user.name "KingDade"
	$ git add *
	$ git commit -m "first commit"
	$ git remote add origin https://github.com/DLRSP/example
	$ git push -u origin master
	
	# create branches
	$ git checkout -b django-errors
	$ git push origin django-errors
	$ git checkout -b django-sp
	$ git push origin django-sp
	
	# check branches
	$ git branch
	
	$ git checkout master
	