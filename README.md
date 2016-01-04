# django-example
[![codecov.io](https://codecov.io/github/DLRSP/example/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/example?branch=master)
[![master](https://travis-ci.org/DLRSP/example.svg?branch=master)](https://travis-ci.org/DLRSP/example)

	$ mkdir example
	$ cd example
	$ git init
	$ git config credential.helper store
	$ git config --global user.name "KingDade"
	$ git config --global user.email davide.larosa.88@gmail.com
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
	$ git branch
	